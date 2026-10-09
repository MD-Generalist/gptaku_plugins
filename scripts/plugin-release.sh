#!/bin/bash
# 플러그인 서브모듈 릴리즈 워크플로
#
# 전제: worktree에서 작업 완료 → 서브모듈 브랜치에 커밋이 쌓인 상태
# 하는 일: 서브모듈 머지·푸시 → 부모 포인터 갱신·커밋 → (선택) 푸시
#
# 사용:
#   plugin-release.sh <플러그인명> <작업브랜치> [--push]
#   예: plugin-release.sh pumasi feat/cursor-worker --push
set -euo pipefail

fail() { echo "ERROR: $*" >&2; exit 1; }
[[ $# == 2 || ( $# == 3 && ${3} == --push ) ]] || fail 'Usage: plugin-release.sh <plugin> <source-branch> [--push]'
PLUGIN="$1"
BRANCH="$2"
[[ "$PLUGIN" =~ ^[A-Za-z0-9][A-Za-z0-9_-]*$ ]] || fail 'Invalid plugin name'
git check-ref-format --branch "$BRANCH" >/dev/null || fail 'Invalid branch name'
[[ "$BRANCH" != main ]] || fail 'Source branch must differ from main'
PUSH="${3:-}"
ROOT="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd -P)"
SUB="$ROOT/plugins/$PLUGIN"

[[ $(git -C "$ROOT" branch --show-current) == main ]] || fail 'Parent must be on main'
git -C "$ROOT" diff --cached --quiet || fail 'Parent index must be empty'
[[ $(git -C "$ROOT" ls-files --stage -- "plugins/$PLUGIN") == 160000\ * ]] || fail 'Plugin must be a tracked submodule'
for repo in "$ROOT" "$SUB"; do
  for state in MERGE_HEAD CHERRY_PICK_HEAD REVERT_HEAD rebase-merge rebase-apply sequencer; do
    state_path=$(git -C "$repo" rev-parse --git-path "$state")
    [[ "$state_path" == /* ]] || state_path="$repo/$state_path"
    [[ ! -e "$state_path" ]] || fail "Pending Git operation in $repo"
  done
done
current=$(git -C "$SUB" branch --show-current)
[[ "$current" == main || "$current" == "$BRANCH" ]] || fail 'Plugin must be on main or the source branch'
git -C "$SUB" show-ref --verify --quiet refs/heads/main || fail 'Missing main branch'
git -C "$SUB" show-ref --verify --quiet "refs/heads/$BRANCH" || fail 'Missing source branch'
SOURCE_SHA=$(git -C "$SUB" rev-parse "refs/heads/$BRANCH")

[ -d "$SUB/.git" ] || [ -f "$SUB/.git" ] || { echo "ERROR: $SUB 는 서브모듈이 아님"; exit 1; }

echo "▶ 1/6 서브모듈 상태 점검 ($PLUGIN)"
cd "$SUB"
git rev-parse --verify "$BRANCH" >/dev/null 2>&1 || { echo "ERROR: 브랜치 $BRANCH 없음"; exit 1; }
DIRTY=$(git status --porcelain | wc -l | tr -d ' ')
[ "$DIRTY" = "0" ] || { echo "ERROR: 서브모듈에 미커밋 $DIRTY개 — 먼저 커밋하거나 stash"; git status --short | head -5; exit 1; }

echo "▶ 2/6 버전 확인"
# Validate the actual merge tree before changing branches, index, or commits.
MERGED_TREE=$(git merge-tree --write-tree refs/heads/main "$SOURCE_SHA") || fail 'Merge conflicts; resolve separately'
VER=$(git show "$MERGED_TREE:.claude-plugin/plugin.json" | python3 -c '
import json, re, sys
version = json.load(sys.stdin)["version"]
pattern = r"(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)(?:-[0-9A-Za-z-]+(?:\.[0-9A-Za-z-]+)*)?(?:\+[0-9A-Za-z-]+(?:\.[0-9A-Za-z-]+)*)?"
if not isinstance(version, str) or not re.fullmatch(pattern, version):
    sys.exit("Invalid release version")
if "-" in version:
    prerelease = version.split("+", 1)[0].split("-", 1)[1]
    if any(part.isdigit() and len(part) > 1 and part.startswith("0") for part in prerelease.split(".")):
        sys.exit("Invalid numeric prerelease identifier")
print(version)
') || fail 'Invalid merged plugin manifest'
echo "   plugin.json version = $VER"
grep -q "^## $VER" CHANGELOG.md 2>/dev/null || echo "   ⚠ CHANGELOG.md에 '## $VER' 항목이 없음 — 확인 권장"

echo "▶ 3/6 서브모듈 머지 ($BRANCH → main)"
git checkout main -q
git merge --no-ff "$SOURCE_SHA" -m "merge $BRANCH (v$VER)" -q
echo "   머지 완료: $(git log --oneline -1)"

echo "▶ 4/6 서브모듈 푸시"
if [ "$PUSH" = "--push" ]; then
  git push origin main -q && echo "   pushed"
else
  echo "   (건너뜀 — --push 없음)"
fi

echo "▶ 5/6 부모 레포 포인터 갱신"
cd "$ROOT"
git add "plugins/$PLUGIN"
if git diff --cached --quiet; then
  echo "   포인터 변화 없음 (이미 최신)"
else
  git commit -q --only -m "chore: update $PLUGIN submodule to v$VER" -- "plugins/$PLUGIN"
  echo "   $(git log --oneline -1)"
fi

echo "▶ 6/6 부모 푸시"
if [ "$PUSH" = "--push" ]; then
  git push origin main -q && echo "   pushed"
else
  echo "   (건너뜀 — --push 없음)"
fi

echo
echo "✅ 완료. 정리하려면:"
echo "   cd $SUB && git branch -d $BRANCH"
echo "   Paseo 워크스페이스는 앱에서 archive"
