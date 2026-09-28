# 랜딩 레퍼런스 조사 (2026-09-28, Aside 브라우저 실방문 10곳)

## 사이트별 요약

### 1) herdr-web-ui (devswha.github.io)
- **히어로:** "Your herdr agents, in a browser and on your phone." 10단어 정도의 직설형입니다. 서브카피는 "Read them as a chat, drop into the live terminal…" 버튼은 없고 설치 명령 박스와 Copy가 메인 CTA입니다(`curl -fsSL …/install.sh | sh`). 보조 링크는 "Try it in your browser first"(설치 없는 /demo/)와 "hand INSTALL.md to a coding agent"입니다.
- **데모:** 실제 녹화 mp4 2개(데스크톱 + 폰)를 설치 블록 바로 아래에 나란히 붙였습니다. 첫 화면 하단에 걸치고, 영상마다 무엇이 보이는지 캡션이 있습니다.
- **섹션 순서:** 히어로 → Nothing in between(카드 3) → Chat/Terminal/Prompts 스크린샷 → 지원 에이전트 표 → On your phone(3단계, 명령 포함) → 경쟁 비교표 → 푸터(MIT).
- **색/타이포:** 라이트, 따뜻한 베이지 #EEEAE2에 앰버브라운 #8C5000. Pretendard 산세리프, 모노는 명령에만 씁니다.
- **신뢰 장치:** 스타·로고·후기는 없습니다. 대신 에이전트 지원표(6행)와 경쟁 4종 비교표(7행), 그리고 "127.0.0.1에서만 listen" 같은 프라이버시 문구가 있습니다.
- **인상적인 패턴:** 솔직한 비교표입니다. 다른 제품이 더 맞는 경우까지 적어 둡니다("If you want tmux…, one of the others is the better fit").

### 2) ghostty.org
- **히어로:** h1이 없습니다. 설명 한 문장 "Ghostty is a fast, feature-rich, and cross-platform terminal emulator…"와 CTA 2개(Download, Documentation, 둘 다 아웃라인)뿐이고 설치 명령도 없습니다.
- **데모:** 화면 중앙의 가짜 macOS 터미널 창 안에서 ASCII 유령이 움직입니다. DOM 텍스트 애니메이션이고, 이것이 히어로 그 자체입니다.
- **섹션 순서:** 스크롤 없는 한 화면 페이지입니다. 헤더와 푸터도 없습니다.
- **색/타이포:** 다크 #0F0F11에 블루 #3551F3 하나. 산세리프 UI + JetBrains Mono(면적으로는 모노가 우세).
- **신뢰 장치:** 없습니다.
- **인상적인 패턴:** 제품 자체가 무대입니다. 브랜드 컬러 하나를 로고와 주 CTA에 같이 씁니다.

### 3) warp.dev
- **히어로:** "Open infrastructure for cloud software factories". 6단어 선언형이고 헤드라인까지 모노 56px입니다. CTA는 2개(request early access / download warp terminal)에 "$10,000 free usage" 한 줄이 붙습니다. 설치 명령은 히어로에 없고 하단 카드에 `curl … | bash`로만 나옵니다.
- **데모:** CTA 바로 아래 캔버스 애니메이션 "[ fig. 1 — the factory ] LIVE FACTORY.YAML"(112 agents로 퍼지는 장면, 카운터 포함). 사운드 이펙트도 있습니다.
- **섹션 순서:** 히어로 → 로고월(800k+ devs) → SDLC 01~06 카드 → 평가/벤치마크 차트 → 케이스 스터디(PR당 $80→$30) → 엔터프라이즈 사례 → Open at every layer(LAYER 01~04) → 거버넌스 → 제품 3카드 → FAQ.
- **색/타이포:** 라이트에 형광 라임 #EEF17C. 본문까지 거의 전부 모노(matterMono)입니다.
- **신뢰 장치:** 로고 8개, 모델별 벤치마크 수치, 케이스 스터디 수치가 있습니다. 비교표와 스타 수는 없습니다.
- **인상적인 패턴:** 페이지 전체를 기술 도판처럼 연출합니다. "[ fig. N ]" 캡션, 소문자 모노 라벨, 01~06 번호가 섹션마다 붙습니다.

### 4) zed.dev
- **히어로:** 맨 위에 공지 배너가 있습니다. 헤드라인은 "Your last next editor", 4단어 위트형이고 세리프 블루입니다. CTA 2개(Download now / Clone source)에 단축키 힌트 D/C가 붙고, 설치 명령은 없습니다.
- **데모:** 히어로 바로 아래 풀폭으로 실제 조작 가능한 HTML 에디터 목업이 들어갑니다(에이전트 채팅 + 코드 + 터미널). 기능 카드마다 영상이 있습니다.
- **섹션 순서:** 히어로 → Fast/Agentic/Collaborative → 인터랙티브 목업 → 실명 후기 → 기능 카드 → Open Source(GitHub 수치) → AI 기능 → 확장 생태계 → 세부 기능 → 팀의 편지 → 블로그 → 마감 CTA.
- **색/타이포:** 라이트 크림 배경에 블루 #1348DC. 제목은 IBM Plex Serif 계열, 본문은 산세리프, 모노는 적습니다.
- **신뢰 장치:** 90,674 Stars, 2,270 Contributors 등 GitHub 수치, 기여자 아바타월, 실명 후기 5개(Dan Abramov, José Valim 등).
- **카탈로그:** 확장 카드 구성은 이름, 다운로드 수(7.0M 등), 한 줄 설명, 제작자입니다. 다운로드 수 순으로 촘촘하게 깔립니다.
- **인상적인 패턴:** 스크린샷 대신 제품 UI를 HTML로 재현했고, 목업 속 코드도 농담으로 채워 읽는 재미를 줍니다.

### 5) linear.app (/homepage 기준)
- **히어로:** "The product development system for teams and agents", 9단어 정의형입니다. 서브카피는 "Purpose-built for planning and building products. Designed for the AI era." 히어로 본문에는 버튼 없이 "New · Loops →" 알약 공지만 있고, 설치 명령도 없습니다.
- **데모:** 히어로 바로 아래 풀폭 DOM 앱 목업이 있고, 섹션마다 칸반, 로드맵, 에이전트 채팅, 편집 가능한 코드 diff 목업이 이어집니다.
- **섹션 순서:** 히어로 → 로고월(7) → Fig 0.1~0.3 → 기능 4섹션 → Changelog → 후기 2개와 "40,000 teams" → 최종 CTA.
  - 기능 4섹션은 모두 같은 틀입니다: 제목 → 문단 → 목업 → Features 아코디언.
- **색/타이포:** 다크 전용 #08090A. 포인트 컬러가 거의 없고, Inter 산세리프에 모노(Berkeley Mono)는 코드에만 씁니다.
- **신뢰 장치:** 로고 7개, "over 40,000 product teams", 후기 2개.
- **인상적인 패턴:** 기능 섹션을 같은 틀로 반복해서 긴 페이지도 리듬이 일정합니다.

### 6) raycast.com/store (카탈로그)
- **히어로:** 헤드라인은 "Store" 한 단어(80px)이고, 서브카피는 "Sprinkle a little magic on your day…" 핵심 요소는 CTA 대신 ⌘K 검색입니다. 설치는 명령이 아니라 `raycast://` 딥링크로 앱을 바로 엽니다.
- **데모:** 스토어 목록에는 없습니다. 상세 페이지에서 정적 스크린샷 캐러셀(8장)로 보여줍니다.
- **섹션 순서:** 히어로(검색) → Featured 큰 카드 3 → 정렬 탭과 플랫폼 필터 → 2열 그리드 → 페이지네이션(332p) → 푸터(카테고리).
- **색/타이포:** 다크 #07080A, Inter 100%. 강조는 흰색 설치 버튼이 맡습니다.
- **카드 구성:**
  - 카드 정보: 아이콘, 이름, 설명, Install, 작성자, "N Commands", AI 배지, 설치수(762,412 등), "macOS only".
  - 정렬 탭: All / Recently Added / Most Popular.
  - 카테고리는 스토어 본문에 없고 푸터에만 있습니다.
- **상세 페이지:**
  - 상단: 설치수, 배지, Install 버튼.
  - 탭: Overview / Commands / Version History. 본문은 README형 문서입니다.
  - 우측 사이드바: Contributors, Compatibility, Categories, Source, Report Bug.
  - 하단: "People also like".
- **인상적인 패턴:** 카드 한 장에 판단에 필요한 메타가 다 들어 있습니다. 상세 페이지의 우측 사이드바는 플러그인 상세 템플릿으로 그대로 가져다 쓸 수 있습니다.

### 7) bun.sh
- **히어로:** "Bun is a **fast** JavaScript runtime & toolkit. All in one." "fast"만 핑크로 칠했습니다. 위쪽에 버전 배지 "NEW v1.4.2"가 있습니다. 설치 박스가 곧 CTA입니다(`curl -fsSL https://bun.sh/install | bash`, OS 탭, "View install script").
- **데모:** 설치 박스 바로 아래 탭형 벤치마크 막대차트(bun 0.21s vs npm 4.45s)가 있고, "replay in real time" 버튼이 붙습니다. 중간에 "A minute with Bun" 5단계 터미널 애니메이션(hover로 정지)이 있습니다.
- **섹션 순서:** 히어로와 Used by 로고 → 4 tools 카드(각각 REPLACES 라벨) → 1분 터미널 → 최신 릴리스 → In production → 설치 시나리오 6개 → 메모리 벤치 → 내장 API → 표준 라이브러리 그리드 → 프론트엔드 → 비교표(23행 접힘) → 마감 CTA(설치 명령 반복).
- **색/타이포:** 라이트, 마감 섹션만 다크. 포인트는 핑크 #FF1F8F. Archivo 800 헤드라인 + Martian Mono(모노 비중 큼).
- **신뢰 장치:** 로고 12개(Anthropic, Vercel, Cursor 등), 벤치마크 수치마다 방법론과 reproduce 링크, Boris Cherny(Claude Code 리드) 실명 인용, Bun/Node/Deno 비교표.
- **인상적인 패턴:** 모든 숫자에 "reproduce" 링크가 붙어 있어서 주장을 검증할 수 있습니다.

### 8) firecrawl.dev (insane-search의 가장 가까운 레퍼런스)
- **히어로:** "Power AI agents with **clean web data**". 핵심 구만 오렌지로 칠했습니다. 서브카피는 "…It's also open source." CTA 2개는 "Start for free"와 **"Setup for agents"**이고, nav에 GitHub 185.6K가 있습니다. 설치 명령은 섹션 01부터 나옵니다.
- **데모:** 히어로 안에 인터랙티브 위젯이 있습니다. URL 입력, Search/Scrape/Map/Crawl 모드 버튼, JSON 결과 패널로 구성됩니다.
- **섹션 순서:** 섹션마다 "[ 0N / 07 ]" 번호가 붙습니다.
  - 히어로와 로고 마퀴(150,000+)
  - 기능 카드와 코드 탭(Python/Node/cURL/CLI)
  - **Agent Ready**: Prompt/MCP/CLI 탭, "Copy and paste this into your AI agent", SKILL.md용 curl
  - 성능 벤토
  - 기능
  - 유즈케이스 탭
  - 오렌지 풀블록(Alexandria)
  - 트윗 후기 마퀴
  - Get started
  - FAQ
- **색/타이포:** 라이트에 오렌지 #FA5D19. Suisse 산세리프 + GeistMono(코드, 라벨, JSON).
- **신뢰 장치:**
  - 1,000 URL 벤치마크: Coverage 96% vs Puppeteer 79% vs cURL 75%, P95 3,387ms, "93% fewer tokens"
  - 로고 18개, 트윗 후기 8개, YC와 $75M 투자
- **인상적인 패턴:** 사람용 입구와 **에이전트용 입구**를 따로 둡니다. 에이전트에 붙여넣을 프롬프트 블록과 SKILL.md 링크까지 있습니다.

### 9) resend.com
- **히어로:** "Email for developers", 3단어로 세리프 96px입니다. 서브카피는 "The best way to reach humans instead of spam folders." CTA 2개(Get started / Documentation). 설치 명령은 없습니다.
- **데모:** 히어로에는 3D 캔버스 그래픽만 있습니다. 본문이 인터랙티브 중심입니다.
  - 코드 탭: 13개 언어 × 9개 프레임워크
  - Test mode: Send를 누르면 HTTP 200 로그가 쌓임
  - 웹훅 이벤트 피드
  - 실제 입력 가능한 에디터
- **섹션 순서:** 히어로 → 로고월(12) → Integrate this morning → DX(Test mode, Webhooks) → 에디터 → 연락처/분석 → React Email → Vercel CEO 단독 인용 → 대시보드 탭 → 후기 마퀴(10) → 마감 CTA.
- **색/타이포:** 순흑 다크, 포인트 컬러 거의 없음. h1만 세리프이고 나머지는 산세리프, 모노 비중도 꽤 큽니다.
- **신뢰 장치:** 로고 12개, 실명 후기 10개, 대표 인용 1개, SOC2/GDPR, 상태 표시.
- **인상적인 패턴:** 설명 대신 페이지 안에서 실행하게 하고, 실행 결과 로그를 보여줍니다.

### 10) smithery.ai (glama는 미사용)
- **히어로:** "Give agents more agency", 4단어 말장난형입니다. 서브카피는 "Connect agents to thousands of tools… Auth, credentials, and sessions handled for you." CTA 버튼은 0개이고 검색창(자동 포커스)과 마스코트가 있습니다.
- **데모:** 정적 터미널 블록에 `npx smithery auth login` → `mcp add notion` → `tool list` → `tool call` 순서로 명령을 쌓습니다. 블록마다 복사 버튼이 있습니다.
- **섹션 순서:** 공지 바 → 검색 히어로 → 추천 카드 18개와 "Browse 23,997+ MCPs" → 터미널 단계 → 3컬럼 가치 → Publish → 마감(`npx -y smithery setup` 복사 버튼).
- **색/타이포:** 라이트 웜 오프화이트 #E7E5DF에 오렌지 #FF5500. 다크 토글이 있고, pantheon 산세리프 + Fira Code입니다.
- **카탈로그:**
  - 카드 정보: 아이콘, 이름, Verified 배지, namespace 슬러그, "22.49k uses", 설명.
  - 사이드바 필터: Verified / Smithery managed. 카테고리 7개(Web Search, Browser Automation, Academic Research 등).
  - 결과 표시: "12,738 servers found (339ms)".
- **상세 페이지:**
  - 상단: Verified, 품질 점수 90/100, "last deployed 4 months ago".
  - 탭: Tools/Resources/Prompts, 도구마다 read-only 배지.
  - 우측 사이드바: Repo, License, 게시일.
- **인상적인 패턴:** 카드 클릭이 곧 "툴박스에 담기"입니다. 여러 개를 골라 한 번에 설치하는 장바구니 구조입니다.
- **아쉬운 점:** 홈의 "23,997+"와 카탈로그의 "12,738"이 서로 맞지 않습니다.

---

## 종합

### (a) 공통 패턴 5개
1. **짧은 정의형 헤드라인에 한 단어만 강조.** 대부분 3~10단어입니다. 핵심 단어 하나만 포인트 컬러로 칠합니다(bun의 "fast", firecrawl의 "clean web data").
2. **히어로 바로 밑에 살아있는 제품.** 스크린샷보다 DOM 목업, 인터랙티브 위젯, 터미널 애니메이션을 씁니다(zed, linear, firecrawl, ghostty, bun).
3. **히어로 직후 로고월/숫자 한 줄.** "800k+ devs", "150,000+ companies", "Used by" 같은 것으로 첫 스크롤 안에 사회적 증거를 둡니다.
4. **CTA는 2개 이하.** 주 CTA 하나(채움)와 보조 하나(Docs/Source, 아웃라인)입니다. 개발자 도구는 설치 명령 박스와 Copy가 주 CTA를 대신하기도 합니다(bun, herdr).
5. **포인트 컬러 하나 + 산세리프 + 코드용 모노.** 세리프는 제목에만 가끔 씁니다(zed, resend). 마지막 섹션에서 CTA나 설치 명령을 한 번 더 반복하는 것도 거의 공통입니다.

### (b) 차별화에 쓸 만한 패턴 3개
1. **에이전트용 입구 따로 두기 (firecrawl).** 허브와 각 플러그인 페이지에 "사람용 설치"와 "Claude Code에 붙여넣을 프롬프트/명령" 탭을 나란히 둡니다. Claude Code 플러그인이라는 성격에 딱 맞고, 경쟁 마켓(smithery)에는 없는 요소입니다.
2. **재현 가능한 증거 (bun + herdr).**
   - insane-search: 봇차단 사이트 N개에서 일반 fetch vs insane-search의 성공률을 보여주고, 방법론과 재현 명령을 붙입니다.
   - insane-research: 검증된 출처 수와 기각된 주장 예시를 보여줍니다.
   - 여기에 herdr식 솔직 비교표("이런 경우엔 다른 도구가 낫다")를 더하면 과장 없이 신뢰를 얻습니다.
3. **허브 카드 = Raycast 메타 + Smithery 장바구니.**
   - 카드 정보: 아이콘, 이름, 한 줄 기능, 슬래시 커맨드 수, 카테고리 배지, 설치수/스타.
   - 18개 중 여러 개를 체크하면 설치 명령이 한 줄로 합쳐져 복사되게 합니다.
   - 18개는 페이지네이션이 필요 없는 양이라, 카테고리 칩과 전체 그리드를 한 화면에 보여주면 됩니다.

### (c) 피해야 할 것 2개
1. **숫자 불일치와 근거 없는 수치.** Smithery는 홈 "23,997+"와 카탈로그 "12,738"이 달라서 오히려 신뢰를 깎았습니다. 설치수, 성공률, 스타 수는 한 출처로 통일하고, 측정 날짜와 방법을 붙이거나 아예 빼는 편이 낫습니다.
2. **기술 도판식 과잉 연출.** Warp식 fig. 캡션, 사운드 이펙트, 전면 모노는 세계관이 강하지만, 18종 허브에서는 정보 밀도를 떨어뜨리고 읽기 피로를 줍니다. 특히 한글 본문을 모노로 쓰면 가독성이 무너집니다. 모노는 명령어와 코드에만 쓰세요.
