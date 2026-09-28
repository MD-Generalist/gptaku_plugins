#!/usr/bin/env python3
"""site/ 랜딩 3종(허브·insane-search·insane-research)을 ko/en/zh 문구 사전 하나로 생성한다.

문구는 전부 이 파일의 T 사전에만 있다. HTML은 ko 문구를 기본값으로 박고(noJS 대비),
site.js가 data-i 키로 언어를 바꿔 끼운다. 수치는 2026-09-28 실측값이다 — 손으로 바꾸지 말 것.
"""
import html
import json
import pathlib

SITE = pathlib.Path(__file__).resolve().parents[2] / "site"
REPO = "https://github.com/fivetaku/gptaku_plugins"
MKT = "/plugin marketplace add https://github.com/fivetaku/gptaku_plugins.git"

# ---------------------------------------------------------------- 공통 문구
COMMON = {
    "ko": {"nav_plugins": "플러그인", "tab_me": "직접 설치", "tab_ai": "Claude에게 맡기기", "copy": "복사",
           "_copied": "복사됨", "foot": "MIT 라이선스 · 비공식 커뮤니티 플러그인 (Anthropic과 무관)",
           "bar_n": "{n}개 담음", "bar_copy": "설치 명령 복사", "bar_clear": "비우기"},
    "en": {"nav_plugins": "Plugins", "tab_me": "Install yourself", "tab_ai": "Ask Claude", "copy": "Copy",
           "_copied": "Copied", "foot": "MIT License · Unofficial community plugins (not affiliated with Anthropic)",
           "bar_n": "{n} selected", "bar_copy": "Copy install commands", "bar_clear": "Clear"},
    "zh": {"nav_plugins": "插件", "tab_me": "自己安装", "tab_ai": "交给 Claude", "copy": "复制",
           "_copied": "已复制", "foot": "MIT 许可 · 非官方社区插件（与 Anthropic 无关）",
           "bar_n": "已选 {n} 个", "bar_copy": "复制安装命令", "bar_clear": "清空"},
}


def ai_prompt(lang, plugin):
    """'Claude에게 맡기기' 탭 문구. claude plugin CLI는 실재한다(claude plugin install --help로 확인)."""
    tgt = f"claude plugin install {plugin}@gptaku-plugins" if plugin else "claude plugin install <이름>@gptaku-plugins"
    return {
        "ko": f"터미널에서 `claude plugin marketplace add fivetaku/gptaku_plugins`와 `{tgt}`를 실행해 설치해 줘. 끝나면 Claude Code를 재시작하라고 알려줘.",
        "en": f"Run `claude plugin marketplace add fivetaku/gptaku_plugins` and `{tgt.replace('<이름>', '<name>')}` in the terminal to install it, then tell me to restart Claude Code.",
        "zh": f"请在终端运行 `claude plugin marketplace add fivetaku/gptaku_plugins` 和 `{tgt.replace('<이름>', '<名称>')}` 完成安装，然后提醒我重启 Claude Code。",
    }[lang]


# ---------------------------------------------------------------- 플러그인 18종 (plugin.json·README 기준)
PLUGINS = [
    ("insane-search", "Claude Code의 웹 요청이 403이나 WAF에 막히면 공개 경로를 차례로 시도해 본문을 가져옵니다.", "When a fetch is blocked by a 403 or WAF, it keeps trying public routes until the page's content comes back.", "Claude Code 抓取网页遇到 403 或 WAF 拦截时，逐级尝试公开路径，直到取回页面内容。"),
    ("insane-research", "질문 하나를 받으면 에이전트 여럿이 웹과 학술 자료를 동시에 조사해 인용이 달린 리포트로 정리합니다.", "Turns one question into a cited report, with several agents searching web and academic sources in parallel.", "输入一个问题，多个智能体并行检索网络与学术来源，生成附带内联引用的研究报告。"),
    ("insane-review", "관련 코드를 repomix로 묶어 로그인된 ChatGPT 웹의 GPT Pro에 보내고, 리뷰 결과를 받아옵니다.", "Packs your code with repomix and sends it to GPT Pro through your logged-in ChatGPT web session for review.", "用 repomix 打包相关代码，通过已登录的 ChatGPT 网页会话发给 GPT Pro，并取回评审结果。"),
    ("insane-design", "웹사이트의 실제 CSS를 파싱해 색상·타이포·간격·그림자 토큰을 AI가 바로 쓸 수 있는 design.md로 만듭니다.", "Parses a site's real CSS into a design.md of color, type, spacing and shadow tokens for AI agents.", "抓取网站真实 CSS，把颜色、排版、间距、阴影等令牌提取成 AI 可直接使用的 design.md。"),
    ("kkirikkiri", "하고 싶은 일을 한 문장으로 말하면 꼭 필요한 결정만 묻고 AI 에이전트 팀을 꾸려 실행합니다.", "Give it a goal in one sentence; it asks only what's missing, then builds and runs an AI agent team.", "用一句话描述目标，它只询问尚未确定的事项，然后组建并运行一支 AI 智能体团队。"),
    ("pumasi", "독립 모듈이 3개 이상인 작업에서 Claude가 설계를 맡고, Codex CLI 여러 개가 병렬로 구현합니다. 이미지 생성도 됩니다.", "For 3+ independent modules: Claude designs the interfaces, parallel Codex CLI workers implement them. Also generates images.", "适合 3 个以上独立模块的任务：Claude 负责设计接口，多个 Codex CLI 并行实现代码。也能生成图片。"),
    ("show-me-the-prd", "기획 경험이 없어도 아이디어 한 줄로 PRD·데이터 모델·단계 계획·AI 규칙 문서 4종을 만듭니다.", "For vibe coders: turns a one-line idea into a PRD, data model, phase plan and AI project spec.", "无需规划经验，用一句话想法生成 PRD、数据模型、阶段计划和 AI 项目规范 4 份文档。"),
    ("goaljaby", "PRD 폴더를 받아 내 언어로 된 검토 문서 5종을 만들고, 승인하면 바로 /goal 작업을 시작합니다.", "Turns a PRD folder into five review docs in your language, then starts Claude Code's /goal after you approve.", "读取 PRD 文件夹，生成 5 份评审文档，经你批准后立即启动 /goal 任务。"),
    ("skillers-suda", "전문가 에이전트 4명이 아이디어를 두고 토론하고 인터뷰한 뒤, 동작하는 Claude Code 스킬 파일을 만듭니다.", "Four expert agents debate your idea and interview you, then scaffold a working Claude Code skill.", "四位专家代理先讨论你的想法并进行访谈，再生成可用的 Claude Code 技能。"),
    ("vibe-sunsang", "Claude Code 대화 기록을 분석해 AI 활용 습관을 코칭하고, 성장 리포트를 만듭니다.", "Analyzes your Claude Code conversation history and coaches you to become a more effective AI collaborator.", "分析你的 Claude Code 对话记录，针对 AI 使用习惯给出辅导，并生成成长报告。"),
    ("docs-guide", "프로젝트에 설치된 버전에 맞춰 공식 문서를 실시간으로 가져와, 출처를 밝히고 답합니다.", "Answers library questions from live official docs matched to your installed version, with the source cited.", "按项目中安装的版本实时抓取官方文档来回答库和框架问题，并注明来源。"),
    ("git-teacher", "Git을 몰라도 \"저장해줘\", \"올려줘\"라고 말하면 구글 드라이브에 빗대어 설명하며 커밋·푸시·PR을 처리합니다.", "For Git beginners: save, upload and open PRs by asking in plain words, explained with Google Drive analogies.", "不懂 Git 也能用自然语言完成提交、推送和 PR，并用 Google Drive 类比讲解每一步。"),
    ("nopal", "한 문장 요청으로 Gmail·캘린더·드라이브·시트 등 Google Workspace 9개 서비스를 조합해 실행합니다.", "Turns a plain sentence into actions across Gmail, Calendar, Drive, Sheets and 5 more Google apps.", "一句话即可组合调用 Gmail、日历、云端硬盘、表格等 9 项 Google Workspace 服务。"),
    ("sangse", "제품 정보로 스마트스토어·쿠팡·컬리에 올릴 상세페이지 이미지 컷 10~20장을 만들고, 입력에 없는 주장은 쓰지 않습니다.", "Turns product facts into a 10–20 image-cut detail page for Korean shops, with no invented claims.", "根据产品资料生成适用于 Smart Store、Coupang、Kurly 的 10~20 张详情页切图，不编造任何信息。"),
    ("tikeytaka", "여러 .env 파일에 흩어진 API 키를 암호화 볼트 하나로 모으고, 한 번 갱신하면 모든 프로젝트에 전파합니다.", "Collects API keys scattered across .env files into one encrypted vault and syncs updates to every project.", "把散落在各个 .env 中的 API 密钥整合进一个加密保险库，一次更新即可同步到所有项目。"),
    ("ddiring", "세션을 여러 개 띄워 두고 쓸 때, 끝난 세션의 폴더·터미널 앱·마지막 요청을 알림 하나로 보여줍니다.", "For multi-session users: each completion notification shows the folder, host app and your last prompt.", "同时运行多个会话时，每条完成通知都会显示项目文件夹、所在终端应用和最后一条提示。"),
    ("dd", "클립보드의 긴 로그나 스크린샷을 붙여넣지 않고 Claude Code에 넘기며, 전체 내용은 로컬 파일에 보관합니다.", "Hands Claude Code your clipboard text or screenshot without pasting, keeping long logs out of the chat.", "无需粘贴，直接把剪贴板里的长日志或截图交给 Claude Code，完整内容保存在本地文件中。"),
    ("gaseo", "터미널에서 시작한 Claude Code 세션을 Paseo에 등록해, 앱에서 같은 대화를 이어갈 수 있게 합니다.", "Registers a Claude Code session you started in the terminal with Paseo, so you can continue it in the app.", "把在终端启动的 Claude Code 会话登记到 Paseo，之后可以在应用里继续同一段对话。"),
]

# ---------------------------------------------------------------- 페이지별 문구
HUB = {
    "ko": {"_title": "gptaku plugins — Claude Code 플러그인 18종",
           "h1": "Claude Code에 없던<br><span class=\"g\">도구 18개</span>",
           "lead": "Claude Code에 설치해 쓰는 플러그인 모음입니다. 막힌 웹페이지 읽기, 출처를 검증하는 리서치, 에이전트 팀 구성, API 키 관리처럼 기본 기능만으로는 번거로운 일을 슬래시 명령 하나로 처리합니다.",
           "feat_t": "먼저, 이 둘부터", "s_t": "Claude Code의 기본 fetch는 403, WAF, CAPTCHA를 만나면 거기서 포기합니다. insane-search는 공개 API와 피드부터 브라우저 TLS 지문, 실제 Chrome까지 단계를 올려 가며 공개된 본문을 가져오고, API 키는 필요 없습니다.", "r_t": "AI에게 리서치를 맡기면 출처가 불분명한 주장이 섞이기 쉽습니다. insane-research는 에이전트 여럿이 웹·학술·기술 자료를 동시에 조사하고, 핵심 주장은 2개 이상의 출처로 교차 검증해 A~E 등급이 붙은 인용 리포트로 전달합니다.",
           "see": "살펴보기 →", "all_t": "전체 플러그인", "all_s": "체크해 두면 설치 명령을 한 번에 복사할 수 있습니다.",
           "pick": "담기", "close_t": "마켓 한 번 등록하면,<br>나머지는 골라서."},
    "en": {"_title": "gptaku plugins — 18 plugins for Claude Code",
           "h1": "The <span class=\"g\">18 tools</span><br>Claude Code was missing",
           "lead": "A set of plugins you install into Claude Code. Reading blocked web pages, research with checked sources, building agent teams, managing API keys: jobs that are tedious with the built-in tools become a single slash command.",
           "feat_t": "Start with these two", "s_t": "Claude Code's default fetch gives up when a site answers with a 403, a WAF wall or a CAPTCHA. insane-search escalates from public APIs and feeds to browser TLS fingerprints and a real Chrome until one route returns the public content, with no API key needed.", "r_t": "AI research answers can easily mix in claims with no clear source. insane-research sends several agents across web, academic and technical sources in parallel, cross-checks key claims against at least two sources, and delivers a cited report with A–E source ratings.",
           "see": "Take a look →", "all_t": "All plugins", "all_s": "Check the ones you want and copy every install command at once.",
           "pick": "Add", "close_t": "Add the marketplace once.<br>Pick the rest."},
    "zh": {"_title": "gptaku plugins — 18 款 Claude Code 插件",
           "h1": "Claude Code 缺的<br><span class=\"g\">18 件工具</span>",
           "lead": "一套安装到 Claude Code 里使用的插件。读取被拦截的网页、带来源核验的研究、组建智能体团队、管理 API 密钥——这些用内置功能很麻烦的事，一条斜杠命令就能完成。",
           "feat_t": "先从这两个开始", "s_t": "Claude Code 默认的抓取遇到 403、WAF 或 CAPTCHA 就会放弃。insane-search 从公开 API 和订阅源逐级升级到浏览器 TLS 指纹和真实 Chrome，直到取回公开内容，全程无需 API 密钥。", "r_t": "让 AI 做研究，结论里很容易混入来源不明的说法。insane-research 让多个智能体并行检索网络、学术与技术来源，关键论断至少经 2 个来源交叉验证，最终交付带 A–E 来源评级的引用报告。",
           "see": "去看看 →", "all_t": "全部插件", "all_s": "勾选后可以一次复制全部安装命令。",
           "pick": "加入", "close_t": "添加一次插件市场，<br>其余按需挑选。"},
}

SEARCH = {
    "ko": {"_title": "insane-search — 포기는 배추 셀 때나",
           "eyebrow": "Claude Code 플러그인 · API 키 필요 없음",
           "h1": "포기는<br><span class=\"acc\">배추 셀 때나.</span>",
           "lead": "WebFetch가 403·WAF·CAPTCHA에 막힌 공개 페이지를, 공개 API와 피드 → 브라우저 TLS 지문 → 실제 Chrome 순으로 경로를 바꿔 가며 읽어 옵니다. API 키는 필요 없고, 로그인이나 유료 벽 앞에서는 멈춘 뒤 그 사실을 알려 줍니다.",
           "vs_t": "같은 URL, 다른 결과", "vs_s": "2026년 9월 28일, 쿠팡 \"키보드\" 검색 페이지.",
           "vs_a": "기본 WebFetch", "vs_a_n": "요청이 거부되어 본문을 받지 못함",
           "vs_b": "insane-search", "vs_b_big": "상품 60개", "vs_b_n": "52번째 경로(실제 Chrome)에서 성공 · 41초",
           "play_t": "그 52번을 그대로 재생하면", "cap": "실제 실행 기록(trace)을 재생한 화면입니다.",
           "facts_t": "오늘 돌려본 네 곳",
           "f1": "쿠팡 검색", "f1v": "WebFetch 403 → 52번째 시도, 실제 Chrome", "f1t": "41초",
           "f2": "레딧 인기글", "f2v": "curl 403 → 1번째 시도, 공식 RSS", "f2t": "1.7초",
           "f3": "네이버 블로그", "f3v": "빈 프레임 → 2번째 시도, 모바일 주소", "f3t": "1초",
           "f4": "X 프로필", "f4v": "로그인 벽 → 3번째 시도, 브라우저 TLS 지문", "f4t": "3초",
           "how_t": "막히면, 다음 길로",
           "st1": "공식 경로부터", "st1d": "RSS, 공개 API처럼 사이트가 원래 열어 둔 길을 먼저 찾습니다.",
           "st2": "브라우저처럼 보이기", "st2d": "실제 브라우저의 TLS 지문과 쿠키, 모바일 주소를 조합해 다시 시도합니다.",
           "st3": "진짜 브라우저", "st3d": "그래도 막히면 내 컴퓨터의 Chrome을 띄워 화면에 그려진 본문을 가져옵니다.",
           "honest_t": "솔직하게",
           "honest": "수천 페이지를 정해진 시간마다 긁어야 한다면 호스팅 크롤러가 더 맞습니다. 로그인해야 보이는 페이지와 유료 기사는 뚫지 않고, 못 읽었다고 알려 줍니다. insane-search의 자리는 대화하다 막힌 공개 페이지 하나입니다.",
           "close_t": "막히는 순간,<br>알아서 끼어듭니다."},
    "en": {"_title": "insane-search — 403 is not an answer",
           "eyebrow": "Claude Code plugin · No API key",
           "h1": "403 is not<br><span class=\"acc\">an answer.</span>",
           "lead": "When WebFetch hits a 403, a WAF or a CAPTCHA on a public page, insane-search switches routes (public APIs and feeds, then browser TLS fingerprints, then a real Chrome) until the content comes back. No API key needed. At logins and paywalls it stops and tells you so.",
           "vs_t": "Same URL, different outcome", "vs_s": "Coupang search for \"keyboard\", September 28, 2026.",
           "vs_a": "Built-in WebFetch", "vs_a_n": "Request refused, no content",
           "vs_b": "insane-search", "vs_b_big": "60 products", "vs_b_n": "Succeeded on route 52 (real Chrome) · 41s",
           "play_t": "All 52 attempts, replayed", "cap": "A replay of the actual execution trace.",
           "facts_t": "Four sites, run today",
           "f1": "Coupang search", "f1v": "WebFetch 403 → attempt 52, real Chrome", "f1t": "41s",
           "f2": "Reddit top posts", "f2v": "curl 403 → attempt 1, official RSS", "f2t": "1.7s",
           "f3": "Naver Blog", "f3v": "Empty frame → attempt 2, mobile URL", "f3t": "1s",
           "f4": "X profile", "f4v": "Login wall → attempt 3, browser TLS fingerprint", "f4t": "3s",
           "how_t": "Blocked? Next route.",
           "st1": "Official routes first", "st1d": "RSS feeds and public APIs the site already exposes.",
           "st2": "Look like a browser", "st2d": "Real browser TLS fingerprints, cookies and mobile URLs, in combination.",
           "st3": "Use a real browser", "st3d": "If all else fails, it opens Chrome on your machine and reads the rendered page.",
           "honest_t": "To be fair",
           "honest": "If you need to crawl thousands of pages on a schedule, a hosted crawler is the better fit. insane-search won't break into login-only pages or paywalls; it tells you it couldn't read them. It's built for the one public page that stopped your conversation.",
           "close_t": "The moment you're blocked,<br>it steps in."},
    "zh": {"_title": "insane-search — 403 不是终点",
           "eyebrow": "Claude Code 插件 · 无需 API 密钥",
           "h1": "403<br><span class=\"acc\">不是终点。</span>",
           "lead": "WebFetch 在公开页面上遇到 403、WAF 或验证码时，insane-search 会依次换用公开 API 与订阅源、浏览器 TLS 指纹、真实 Chrome，直到取回内容。无需 API 密钥；遇到登录墙或付费墙则停下并如实告诉你。",
           "vs_t": "同一个 URL，不同的结果", "vs_s": "2026 年 9 月 28 日，Coupang「键盘」搜索页。",
           "vs_a": "内置 WebFetch", "vs_a_n": "请求被拒绝，没有拿到内容",
           "vs_b": "insane-search", "vs_b_big": "60 件商品", "vs_b_n": "第 52 条路径（真实 Chrome）成功 · 41 秒",
           "play_t": "把这 52 次原样回放", "cap": "回放的是真实执行记录（trace）。",
           "facts_t": "今天实测的四个站点",
           "f1": "Coupang 搜索", "f1v": "WebFetch 403 → 第 52 次，真实 Chrome", "f1t": "41 秒",
           "f2": "Reddit 热帖", "f2v": "curl 403 → 第 1 次，官方 RSS", "f2t": "1.7 秒",
           "f3": "Naver 博客", "f3v": "空框架 → 第 2 次，移动版地址", "f3t": "1 秒",
           "f4": "X 个人主页", "f4v": "登录墙 → 第 3 次，浏览器 TLS 指纹", "f4t": "3 秒",
           "how_t": "被拦，就换路",
           "st1": "先走官方路径", "st1d": "先找网站本来就开放的 RSS 和公开 API。",
           "st2": "伪装成浏览器", "st2d": "组合真实浏览器的 TLS 指纹、Cookie 和移动版地址重新尝试。",
           "st3": "用真正的浏览器", "st3d": "还是不行，就在你的电脑上打开 Chrome，读取渲染后的正文。",
           "honest_t": "实话实说",
           "honest": "如果要按计划抓取成千上万个页面，托管爬虫更合适。需要登录的页面和付费文章它不会硬闯，而是告诉你读不了。insane-search 解决的是对话中卡住你的那一个公开页面。",
           "close_t": "被拦的那一刻，<br>它自动接手。"},
}

RESEARCH = {
    "ko": {"_title": "insane-research — 그럴듯함은 근거가 아니다",
           "eyebrow": "Claude Code 플러그인 · 멀티에이전트 딥리서치",
           "h1": "그럴듯함은<br><span class=\"acc\">근거가 아니다.</span>",
           "lead": "질문 하나를 주면 에이전트 여럿이 웹과 학술 자료를 동시에 조사해 인용이 달린 리포트로 정리합니다. 모든 출처에 A~E 등급을 매기고, 두 곳 이상에서 확인되지 않은 주장은 본문 대신 부록으로 보냅니다.",
           "n1": "에이전트", "n2": "출처", "n3": "본문 / 부록",
           "nums_s": "아래 샘플 리포트 한 건의 실제 수치입니다.",
           "play_t": "질문 하나가 리포트가 되기까지", "cap": "실제 리서치 세션(2026-08-23)의 기록을 재생한 화면입니다.",
           "gate_t": "검사는 코드가 합니다",
           "gate": "주장마다 출처를 장부에 적고, <code>validate_ledger.py</code>가 그 장부를 검사합니다. 통과하지 못하면 리포트 단계로 넘어가지 않습니다. 모델이 \"확인했다\"고 말하는 것만으로는 부족합니다.",
           "sample_t": "샘플 리포트", "sample_tag": "실제 산출물",
           "sample_h": "Claude Code 멀티세션 앱 번들 ID와<br>Windows 알림 구현 방법",
           "sample_p": "우리 알림 플러그인을 만들 때 실제로 쓴 리포트를 고치지 않고 공개합니다.", "sample_go": "원문 보기 →",
           "honest_t": "솔직하게",
           "honest": "개요만 빨리 필요하면 ChatGPT나 Gemini의 딥리서치가 더 편합니다. insane-research는 질문을 몇 개 되묻고 시간도 더 걸립니다. 기술 선택, 구현 근거, 숫자처럼 틀리면 손해가 큰 결정에 쓰세요.",
           "close_t": "틀리면 손해가 큰<br>결정 앞에서."},
    "en": {"_title": "insane-research — Plausible isn't proof",
           "eyebrow": "Claude Code plugin · Multi-agent deep research",
           "h1": "Plausible<br><span class=\"acc\">isn't proof.</span>",
           "lead": "Give it one question and several agents research web and academic sources in parallel, then write it up as a cited report. Every source gets an A–E grade, and any claim not confirmed by two or more sources goes to the appendix instead of the body.",
           "n1": "agents", "n2": "sources", "n3": "body / annex",
           "nums_s": "Real numbers from the sample report below.",
           "play_t": "From one question to a report", "cap": "A replay of a real research session (2026-08-23).",
           "gate_t": "Code does the checking",
           "gate": "Every claim is logged with its sources, and <code>validate_ledger.py</code> checks that ledger. If it fails, the report isn't written. A model saying \"verified\" is not enough.",
           "sample_t": "Sample report", "sample_tag": "Real output",
           "sample_h": "Claude Code multi-session app bundle IDs<br>and Windows notifications",
           "sample_p": "The report we actually used to build our notification plugin, published unedited (in Korean).", "sample_go": "Read the original →",
           "honest_t": "To be fair",
           "honest": "If you just need a quick overview, ChatGPT or Gemini deep research is easier. insane-research asks a few scoping questions and takes longer. Use it for decisions where being wrong is expensive: technology choices, implementation evidence, numbers.",
           "close_t": "For decisions<br>you can't afford to get wrong."},
    "zh": {"_title": "insane-research — 看起来像，不等于有据",
           "eyebrow": "Claude Code 插件 · 多智能体深度研究",
           "h1": "看起来像，<br><span class=\"acc\">不等于有据。</span>",
           "lead": "给它一个问题，多个智能体会并行检索网络与学术资料，整理成附带引用的报告。每个来源都有 A–E 评级，未经两个以上来源证实的论断不进正文，而是放进附录。",
           "n1": "智能体", "n2": "来源", "n3": "正文 / 附录",
           "nums_s": "以下是下方示例报告的真实数字。",
           "play_t": "从一个问题到一份报告", "cap": "回放的是一次真实研究会话（2026-08-23）的记录。",
           "gate_t": "由代码来核验",
           "gate": "每条论断都和来源一起记入台账，由 <code>validate_ledger.py</code> 检查。不通过，就不进入写报告的阶段。模型说一句「已核实」是不够的。",
           "sample_t": "示例报告", "sample_tag": "真实产出",
           "sample_h": "Claude Code 多会话应用 Bundle ID<br>与 Windows 通知实现",
           "sample_p": "我们开发通知插件时实际使用的报告，原样公开（韩文）。", "sample_go": "查看原文 →",
           "honest_t": "实话实说",
           "honest": "如果只想快速了解概况，ChatGPT 或 Gemini 的深度研究更方便。insane-research 会先问几个问题，耗时也更长。它适合那些一旦出错代价很大的决定：技术选型、实现依据、关键数字。",
           "close_t": "在错不起的<br>决定面前。"},
}


# ---------------------------------------------------------------- 조각
def i(key, d, tag="span", cls="", extra=""):
    c = f' class="{cls}"' if cls else ""
    return f'<{tag}{c} data-i="{key}"{extra}>{d["en"][key]}</{tag}>'


def install(plugin, pre=""):
    me = MKT + (f"\n/plugin install {plugin}@gptaku-plugins" if plugin else "")
    return f'''<div class="install" role="group">
  <div class="tabs" role="tablist"><button role="tab" aria-selected="true" data-tab="me" data-i="tab_me">{COMMON["en"]["tab_me"]}</button><button role="tab" aria-selected="false" data-tab="ai" data-i="tab_ai">{COMMON["en"]["tab_ai"]}</button></div>
  <div class="cmd" data-tab="me"><pre>{html.escape(me)}</pre><button class="copy" data-copy="1" data-i="copy">{COMMON["en"]["copy"]}</button></div>
  <div class="cmd prompt" data-tab="ai" hidden><pre data-i="{pre}ai">{html.escape(ai_prompt("en", plugin))}</pre><button class="copy" data-copy="1" data-i="copy">{COMMON["en"]["copy"]}</button></div>
</div>'''


def head(d, root, accent, cls):
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{d["en"]["_title"]}</title><meta name="description" content="{html.escape(d["en"].get("lead", d["en"].get("h1", "")).replace("<br>", " "))}">
<meta property="og:title" content="{d["en"]["_title"]}"><meta property="og:image" content="{root}assets/art/{cls}.jpg">
<link rel="icon" href="{root}assets/logo.svg"><link rel="stylesheet" href="{root}assets/site.css">
<style>:root{{--accent:{accent}}}</style></head><body class="{cls}">
<nav><div class="wrap"><a class="brand" href="{root}"><img src="{root}assets/logo.svg" alt="">gptaku plugins</a>
<div class="links"><a href="{root}#plugins" data-i="nav_plugins">{COMMON["en"]["nav_plugins"]}</a><a href="{REPO}">GitHub</a>
<div class="lang" role="group" aria-label="Language"><button data-l="en" aria-pressed="true">EN</button><button data-l="ko" aria-pressed="false">한국어</button><button data-l="zh" aria-pressed="false">中文</button></div></div></div></nav>
<main>'''


def foot(d, root):
    data = {l: {**COMMON[l], **d[l]} for l in ("ko", "en", "zh")}
    return f'''</main>
<footer><div class="wrap"><a href="{REPO}">GitHub</a><a href="{root}insane-search/">insane-search</a><a href="{root}insane-research/">insane-research</a><span class="r" data-i="foot">{COMMON["en"]["foot"]}</span></div></footer>
<script>window.I18N={json.dumps(data, ensure_ascii=False)};</script><script src="{root}assets/site.js"></script></body></html>'''


def video(root, base, label_key, d):
    return f'''<div class="media"><video data-base="{root}assets/media/{base}" src="{root}assets/media/{base}-en.mp4" poster="{root}assets/media/{base}-en-poster.png" autoplay muted loop playsinline data-i-attr="aria-label:{label_key}" aria-label="{d["en"][label_key]}"></video></div>
<p class="cap" data-i="cap">{d["en"]["cap"]}</p>'''


# ---------------------------------------------------------------- 허브
def build_hub():
    d = {l: dict(HUB[l]) for l in HUB}
    for l in d:
        d[l]["ai"] = ai_prompt(l, "")
        for n, *desc in PLUGINS:
            d[l][f"p_{n}"] = desc[["ko", "en", "zh"].index(l)]
    rows = "".join(
        f'<div class="row"><b>{n}</b>{i("p_" + n, d)}<label class="pick"><input type="checkbox" value="{n}"><span data-i="pick">{d["en"]["pick"]}</span></label></div>'
        for n, *_ in PLUGINS)
    body = f'''{head(d, "", "var(--coral)", "hub")}
<header class="wrap hero split">
  <div>{i("h1", d, "h1")}{i("lead", d, "p", "lead")}{install("")}</div>
  <div class="art"><img src="assets/art/hub.jpg" alt="Pegboard of tools in violet ink with one coral ladder taken down" width="1600" height="900"></div>
</header>
<section class="wrap">
  {i("feat_t", d, "h2")}<div style="height:40px"></div>
  <div class="two">
    <a class="card" href="insane-search/"><img class="thumb" src="assets/art/search.jpg" alt="" loading="lazy"><div class="pad"><h3>insane-search</h3>{i("s_t", d, "p")}<span class="more" data-i="see">{d["en"]["see"]}</span></div></a>
    <a class="card" href="insane-research/"><img class="thumb" src="assets/art/research.jpg" alt="" loading="lazy"><div class="pad"><h3>insane-research</h3>{i("r_t", d, "p")}<span class="more" data-i="see">{d["en"]["see"]}</span></div></a>
  </div>
</section>
<section class="wrap" id="plugins">{i("all_t", d, "h2")}{i("all_s", d, "p", "sub")}<div class="rows">{rows}</div></section>
<section class="wrap closing">{i("close_t", d, "h2")}{install("", "")}</section>
<div class="bar" role="status"><b></b><button class="copy" data-copy="picked" data-i="bar_copy">{COMMON["en"]["bar_copy"]}</button><button class="clear" data-i="bar_clear">{COMMON["en"]["bar_clear"]}</button></div>
{foot(d, "")}'''
    (SITE / "index.html").write_text(body)


# ---------------------------------------------------------------- insane-search
def build_search():
    d = {l: dict(SEARCH[l]) for l in SEARCH}
    for l in d:
        d[l]["ai"] = ai_prompt(l, "insane-search")
        d[l]["vlabel"] = d[l]["play_t"]
    facts = "".join(f'<div class="row">{i(f"f{k}", d, "b")}{i(f"f{k}v", d)}{i(f"f{k}t", d)}</div>' for k in range(1, 5))
    steps = "".join(f'<div class="step"><div class="n">0{k}</div><div>{i(f"st{k}", d, "h3")}{i(f"st{k}d", d, "p")}</div></div>' for k in range(1, 4))
    body = f'''{head(d, "../", "#D97757", "search")}
<header class="wrap hero center">{i("eyebrow", d, "span", "eyebrow")}{i("h1", d, "h1")}{i("lead", d, "p", "lead")}{install("insane-search")}</header>
<div class="wrap artwide"><div class="art"><img src="../assets/art/search.jpg" alt="Many violet routes stop at a wall with a 403 door; one coral route slips over the top" width="1600" height="900"></div></div>
<section class="wrap">{i("vs_t", d, "h2")}{i("vs_s", d, "p", "sub")}
  <div class="two">
    <div class="card panel">{i("vs_a", d, "div", "lbl")}<div class="big red">403</div>{i("vs_a_n", d, "div", "note")}</div>
    <div class="card panel">{i("vs_b", d, "div", "lbl")}<div class="big" style="color:var(--ok)" data-i="vs_b_big">{d["en"]["vs_b_big"]}</div>{i("vs_b_n", d, "div", "note")}</div>
  </div></section>
<section class="wrap">{i("play_t", d, "h2")}{video("../", "search", "vlabel", d)}</section>
<section class="wrap">{i("facts_t", d, "h2")}<div style="height:40px"></div><div class="rows">{facts}</div></section>
<section class="wrap narrow">{i("how_t", d, "h2")}<div class="steps">{steps}</div></section>
<section class="wrap narrow">{i("honest_t", d, "h2")}<div style="height:24px"></div>{i("honest", d, "p", "honest")}</section>
<section class="wrap closing">{i("close_t", d, "h2")}{install("insane-search")}</section>
{foot(d, "../")}'''
    (SITE / "insane-search" / "index.html").write_text(body)


# ---------------------------------------------------------------- insane-research
def build_research():
    d = {l: dict(RESEARCH[l]) for l in RESEARCH}
    for l in d:
        d[l]["ai"] = ai_prompt(l, "insane-research")
        d[l]["vlabel"] = d[l]["play_t"]
    body = f'''{head(d, "../", "#3FB950", "research")}
<header class="wrap hero center">{i("eyebrow", d, "span", "eyebrow")}{i("h1", d, "h1")}{i("lead", d, "p", "lead")}{install("insane-research")}</header>
<div class="wrap artwide"><div class="art"><img src="../assets/art/research.jpg" alt="Paper slips on violet threads pass through a sieve into a tall verified stack and a small annex tray" width="1600" height="900"></div></div>
<section class="wrap"><div class="stats">
  <div><b>8</b>{i("n1", d)}</div><div><b>109</b>{i("n2", d)}</div><div><b><span style="color:var(--ok)">42</span> / <span style="color:var(--warn)">32</span></b>{i("n3", d)}</div>
</div><p class="cap" style="text-align:center;margin-top:36px" data-i="nums_s">{d["en"]["nums_s"]}</p></section>
<section class="wrap">{i("play_t", d, "h2")}{video("../", "research", "vlabel", d)}</section>
<section class="wrap narrow">{i("gate_t", d, "h2")}<div style="height:24px"></div>{i("gate", d, "p", "honest")}</section>
<section class="wrap">{i("sample_t", d, "h2")}<div style="height:40px"></div>
  <a class="card" href="sample/"><div class="pad" style="padding:48px">{i("sample_tag", d, "span", "tag")}{i("sample_h", d, "h3")}{i("sample_p", d, "p")}<span class="more" data-i="sample_go">{d["en"]["sample_go"]}</span></div></a></section>
<section class="wrap narrow">{i("honest_t", d, "h2")}<div style="height:24px"></div>{i("honest", d, "p", "honest")}</section>
<section class="wrap closing">{i("close_t", d, "h2")}{install("insane-research")}</section>
{foot(d, "../")}'''
    (SITE / "insane-research" / "index.html").write_text(body)


if __name__ == "__main__":
    build_hub()
    build_search()
    build_research()
    print("built", SITE)
