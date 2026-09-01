# -*- coding: utf-8 -*-
"""README.md 를 원본으로 삼아 언어판 3종을 굽는다.

    python i18n.py

한국어판만 손보면 나머지는 여기 표만 고치면 된다. 뼈대(표, 뱃지, 이미지)는
그대로 두고 문장만 바꾸므로 레이아웃이 어긋날 일이 없다.
"""
import pathlib
import re

SRC = pathlib.Path(__file__).parent / "README.md"

NAV = {
    "ko": "**한국어** | [English](README.en.md) | [中文](README.zh.md) | [日本語](README.ja.md)",
    "en": "[한국어](README.md) | **English** | [中文](README.zh.md) | [日本語](README.ja.md)",
    "zh": "[한국어](README.md) | [English](README.en.md) | **中文** | [日本語](README.ja.md)",
    "ja": "[한국어](README.md) | [English](README.en.md) | [中文](README.zh.md) | **日本語**",
}

# 한국어 원문 -> 각 언어. 긴 문장부터 치환해야 부분 일치로 깨지지 않는다.
T = {
"en": {
"### AI와 풀스택 개발. 기획부터 배포까지 한 사람이 이어서 합니다.":
"### AI and full-stack development. One person carrying a product from spec to deployment.",

"건국대학교 정보통신대학원 인공지능전공 석사. 그 전에는 중국에서 4년간 소프트웨어공학을 공부했고 졸업논문을 중국어로 썼습니다.":
"MSc in Artificial Intelligence, Konkuk University Graduate School of Information and Telecommunications. Before that, four years of Software Engineering in China, where I wrote my undergraduate thesis in Chinese.",
"석사 논문은 RAG의 비용 문제를, 학사 논문은 전력 데이터의 규모 문제를 다뤘습니다.":
"My master's thesis took on the cost problem in RAG pipelines, my bachelor's the scale problem in power grid data.",
"지금은 [fornaxworks](https://fornaxworks.com)라는 이름으로 웹, 모바일, AI 제품을 만듭니다.":
"I now build web, mobile, and AI products under the name [fornaxworks](https://fornaxworks.com).",
"2023년부터 유학 컨설팅 사업체를 대표로 운영해와서 고객 응대와 계약, 행정은 이미 하던 일입니다.":
"Running a study abroad consulting agency as its owner since 2023 means client work, contracts, and administration are already familiar ground.",
"한국어 외에 영어, 중국어, 일본어로 소통할 수 있습니다.":
"I work in Korean, English, Chinese, and Japanese.",

"브라우저 미니게임 플랫폼. 자체 게임과 사용자 업로드 게임을 하나의 런타임에서 돌립니다. Ports/Adapters로 도메인을 분리했고 e2e 테스트와 staging 환경을 운영합니다.":
"Browser mini-game platform. First-party and user-uploaded games run on a single runtime. Domain logic sits behind ports and adapters, with e2e tests and a staging environment in operation.",
"HDD SMART 데이터로 7일 안에 고장날 디스크를 예측하고, 점검 순서와 근거 문서, 운영 Runbook을 같이 냅니다. 공개 전 추적 파일 252개를 전수 검사해 개인정보를 걷어냈습니다.":
"Predicts which HDDs will fail within seven days from SMART data, and returns an inspection order, supporting evidence, and an operations runbook. All 252 tracked files were audited and scrubbed of personal data before release.",
"사진 한 장을 동화로 바꾸는 인터랙티브 스토리 플랫폼. 대학원 과제로 시스템 설계와 UX, 비즈니스 전략까지 32p 문서로 정리했습니다.":
"Turns a single photo into an interactive illustrated story. Documented as graduate coursework across 32 pages covering system design, UX, and business strategy.",
"스튜디오 사이트. 프레임워크 없이 Python 스크립트로 HTML을 굽고 Cloudflare Worker에 올립니다. 로고와 OG 이미지도 코드로 그립니다.":
"The studio site itself. No framework: a Python script bakes the HTML and ships it to a Cloudflare Worker. The logo and OG image are drawn in code too.",
"공동주택 공사비 예측 모델. 직접 만든 크롤러 [kapt_crawler](https://github.com/TaeyanG4/kapt_crawler)로 모은 K-APT 공개 데이터를 씁니다.":
"Construction cost prediction model for apartment complexes, trained on public K-APT data collected by my own crawler, [kapt_crawler](https://github.com/TaeyanG4/kapt_crawler).",
"(공개 예정)": "(coming soon)",

"fornaxworks 견본실에 올려둔 데모입니다. 실제 납품물이 아니라 어디까지 만드는지 보여주려고 직접 만든 견본입니다.":
"Demos from the fornaxworks showroom. These are not client deliverables. I built them to show how far the work goes.",
"이미지를 누르면 브라우저에서 바로 열립니다.":
"Click an image to open it in your browser.",

"<b>PALLET</b> 웹 서비스": "<b>PALLET</b> Web service",
"가입, 권한, 결제까지 한 벌": "Sign-up, permissions, and billing in one set",
"<b>TAG</b> 커머스": "<b>TAG</b> Commerce",
"취소, 반품, 정산을 상태로 설계": "Cancellation, returns, and settlement modelled as state",
"<b>MAT</b> 모바일 앱": "<b>MAT</b> Mobile app",
"iOS와 Android를 한 코드로,<br>스토어 심사까지": "iOS and Android from one codebase,<br>store review included",
"<b>INDEX</b> 문서 검색 어시스턴트": "<b>INDEX</b> Document search assistant",
"하이브리드 검색과 재순위, 근거 문단 표기": "Hybrid retrieval, reranking, cited source passages",
"<b>CLERK</b> 반복 업무 에이전트": "<b>CLERK</b> Routine work agent",
"도구 호출 파이프라인, 최종 승인은 사람이": "Tool-calling pipeline, final approval stays with a human",
"<b>TALLY</b> 데이터 대시보드": "<b>TALLY</b> Data dashboard",
"차트보다 매일 최신이 되는 파이프라인": "The pipeline that stays current matters more than the chart",
"<b>STAMP</b> 사내 업무 시스템": "<b>STAMP</b> Internal business system",
"역할별 권한과 지울 수 없는 감사 로그": "Role-based permissions and an append-only audit log",
"<b>BRIDGE</b> 레거시 이관": "<b>BRIDGE</b> Legacy migration",
"무중단 단계 이관, 되돌릴 수 있는 배포": "Phased cutover with no downtime and a reversible deploy",
"<b>BEACON</b> 브랜드와 랜딩 사이트": "<b>BEACON</b> Brand and landing site",
"성능과 검색, 직접 고칠 수 있는 상태로": "Fast, findable, and editable by the people who own it",

"**[경량 파이프라인 컨트롤러를 통한 질의 인식 기반 비용 효율적 RAG](https://www.riss.kr/link?id=T17380351)**":
"**[Query-Aware Cost-Efficient RAG via a Lightweight Pipeline Controller](https://www.riss.kr/link?id=T17380351)**",
"Query-Aware Cost-Efficient RAG via a Lightweight Pipeline Controller<br>2026, 건국대학교 정보통신대학원":
"경량 파이프라인 컨트롤러를 통한 질의 인식 기반 비용 효율적 RAG<br>2026, Konkuk University Graduate School of Information and Telecommunications",
"모든 질의에 같은 고비용 파이프라인을 물리면 쉬운 질문에도 비용과 지연이 그대로 붙습니다.":
"Running every query through the same expensive pipeline makes easy questions pay full price in cost and latency.",
"질의 난이도를 먼저 재고, 하이브리드 검색과 재랭킹, HyDE를 필요할 때만 켜는 경량 컨트롤러를 붙였습니다.":
"I added a lightweight controller that estimates query difficulty first, then switches on hybrid retrieval, reranking, and HyDE only when they are needed.",
"基于MapReduce的电力行业数据挖掘并行化实现<br>2020, 동북전력대학교 Northeast Electric Power University":
"基于MapReduce的电力行业数据挖掘并行化实现<br>2020, Northeast Electric Power University",
"스마트미터가 쏟아내는 사용량 데이터는 단일 장비로 감당이 안 됩니다.":
"Smart meters produce more consumption data than a single machine can process.",
"가상머신에 3노드 Hadoop 클러스터를 올리고 MapReduce K-means로 사용 패턴을 나눴습니다.":
"I stood up a three-node Hadoop cluster on virtual machines and partitioned usage patterns with MapReduce K-means.",

"빅데이터분석기사": "Engineer Big Data Analysis",
"데이터아키텍처준전문가 (DAsP)": "Data Architecture Semi-Professional (DAsP)",
"SQL 개발자 (SQLD)": "SQL Developer (SQLD)",
"데이터분석준전문가 (ADsP)": "Advanced Data Analytics Semi-Professional (ADsP)",
"AI-POT 1급": "AI-POT Level 1",
"정보처리기사": "Engineer Information Processing",
"프로그래밍기능사": "Craftsman Programming",
"리눅스마스터 2급": "Linux Master Level 2",
"네트워크관리사 2급": "Network Administrator Level 2",
"컴퓨터활용능력 1급": "Computer Specialist in Spreadsheet and Database Level 1",
"HSK 5급": "HSK Level 5",

"<b>건국대학교 정보통신대학원</b> 융합정보기술학과 인공지능전공 석사":
"<b>Konkuk University</b> Graduate School of Information and Telecommunications, MSc in Artificial Intelligence",
"<b>이어드림스쿨 6기</b> 심화과정<br>중소벤처기업부 AI 기술인력 양성":
"<b>Yeardream School 6th cohort</b>, advanced track<br>Ministry of SMEs and Startups AI talent programme",
"LLM Fine-tuning, RAG와 Vector DB":
"LLM fine-tuning, RAG and vector databases",
"LangChain과 LangGraph, AI Agent와 MCP":
"LangChain and LangGraph, AI agents and MCP",
"산업 연계 팀 프로젝트":
"Industry-linked team project",
"<b>AI Bootcamp 16기</b> 인공지능모델링<br>6개월 학습 + 1개월 기업 협업":
"<b>AI Bootcamp 16th cohort</b>, AI modelling<br>6 months of study + 1 month industry collaboration",
"<b>동북전력대학교</b> (China) 소프트웨어공학과 학사<br>4년 과정, 재학 중 군복무 2년":
"<b>Northeast Electric Power University</b> (China), BSc in Software Engineering<br>4-year programme, with 2 years of military service during enrolment",

"### 신규 프로젝트 문의는 [fornaxworks.com](https://fornaxworks.com) 에서 받고 있습니다.":
"### New project enquiries are welcome at [fornaxworks.com](https://fornaxworks.com).",
},

"zh": {
"### AI와 풀스택 개발. 기획부터 배포까지 한 사람이 이어서 합니다.":
"### AI 与全栈开发。从策划到部署，由一个人一路负责到底。",

"건국대학교 정보통신대학원 인공지능전공 석사. 그 전에는 중국에서 4년간 소프트웨어공학을 공부했고 졸업논문을 중국어로 썼습니다.":
"建国大学信息通信研究生院人工智能专业硕士。此前在中国攻读软件工程本科四年，毕业论文以中文撰写。",
"석사 논문은 RAG의 비용 문제를, 학사 논문은 전력 데이터의 규모 문제를 다뤘습니다.":
"硕士论文处理 RAG 的成本问题，本科论文处理电力数据的规模问题。",
"지금은 [fornaxworks](https://fornaxworks.com)라는 이름으로 웹, 모바일, AI 제품을 만듭니다.":
"目前以 [fornaxworks](https://fornaxworks.com) 的名义承接 Web、移动端与 AI 产品开发。",
"2023년부터 유학 컨설팅 사업체를 대표로 운영해와서 고객 응대와 계약, 행정은 이미 하던 일입니다.":
"自 2023 年起以负责人身份经营留学咨询公司，客户沟通、合同与行政事务是本来就在做的工作。",
"한국어 외에 영어, 중국어, 일본어로 소통할 수 있습니다.":
"除韩语外，可使用英语、中文、日语沟通。",

"브라우저 미니게임 플랫폼. 자체 게임과 사용자 업로드 게임을 하나의 런타임에서 돌립니다. Ports/Adapters로 도메인을 분리했고 e2e 테스트와 staging 환경을 운영합니다.":
"浏览器小游戏平台。自研游戏与用户上传游戏运行在同一套运行时上。以 Ports/Adapters 分离领域逻辑，并运行 e2e 测试与 staging 环境。",
"HDD SMART 데이터로 7일 안에 고장날 디스크를 예측하고, 점검 순서와 근거 문서, 운영 Runbook을 같이 냅니다. 공개 전 추적 파일 252개를 전수 검사해 개인정보를 걷어냈습니다.":
"基于 HDD SMART 数据预测七天内可能故障的磁盘，并给出巡检顺序、依据文档与运维 Runbook。公开前对 252 个被跟踪文件做了全量审查，清除了个人信息。",
"사진 한 장을 동화로 바꾸는 인터랙티브 스토리 플랫폼. 대학원 과제로 시스템 설계와 UX, 비즈니스 전략까지 32p 문서로 정리했습니다.":
"把一张照片变成童话的互动故事平台。作为研究生课程作业，用 32 页文档整理了系统设计、UX 与商业策略。",
"스튜디오 사이트. 프레임워크 없이 Python 스크립트로 HTML을 굽고 Cloudflare Worker에 올립니다. 로고와 OG 이미지도 코드로 그립니다.":
"工作室官网本身。不用框架，由 Python 脚本生成 HTML 并部署到 Cloudflare Worker。Logo 与 OG 图像也由代码绘制。",
"공동주택 공사비 예측 모델. 직접 만든 크롤러 [kapt_crawler](https://github.com/TaeyanG4/kapt_crawler)로 모은 K-APT 공개 데이터를 씁니다.":
"住宅小区工程造价预测模型。使用自研爬虫 [kapt_crawler](https://github.com/TaeyanG4/kapt_crawler) 采集的 K-APT 公开数据。",
"(공개 예정)": "（即将公开）",

"fornaxworks 견본실에 올려둔 데모입니다. 실제 납품물이 아니라 어디까지 만드는지 보여주려고 직접 만든 견본입니다.":
"这些是放在 fornaxworks 样品间的演示。并非实际交付物，而是为了展示能做到什么程度而自行制作的样品。",
"이미지를 누르면 브라우저에서 바로 열립니다.":
"点击图片即可在浏览器中打开。",

"<b>PALLET</b> 웹 서비스": "<b>PALLET</b> Web 服务",
"가입, 권한, 결제까지 한 벌": "注册、权限、支付一整套",
"<b>TAG</b> 커머스": "<b>TAG</b> 电商",
"취소, 반품, 정산을 상태로 설계": "把取消、退货、结算设计成状态流转",
"<b>MAT</b> 모바일 앱": "<b>MAT</b> 移动应用",
"iOS와 Android를 한 코드로,<br>스토어 심사까지": "一套代码覆盖 iOS 与 Android，<br>含应用商店审核",
"<b>INDEX</b> 문서 검색 어시스턴트": "<b>INDEX</b> 文档检索助手",
"하이브리드 검색과 재순위, 근거 문단 표기": "混合检索与重排序，标注依据段落",
"<b>CLERK</b> 반복 업무 에이전트": "<b>CLERK</b> 重复性业务智能体",
"도구 호출 파이프라인, 최종 승인은 사람이": "工具调用流水线，最终审批仍由人来做",
"<b>TALLY</b> 데이터 대시보드": "<b>TALLY</b> 数据看板",
"차트보다 매일 최신이 되는 파이프라인": "比图表更重要的是每天自动保持最新的数据管道",
"<b>STAMP</b> 사내 업무 시스템": "<b>STAMP</b> 企业内部业务系统",
"역할별 권한과 지울 수 없는 감사 로그": "按角色划分权限与不可删除的审计日志",
"<b>BRIDGE</b> 레거시 이관": "<b>BRIDGE</b> 遗留系统迁移",
"무중단 단계 이관, 되돌릴 수 있는 배포": "不停机分阶段迁移，可回滚的发布",
"<b>BEACON</b> 브랜드와 랜딩 사이트": "<b>BEACON</b> 品牌与落地页",
"성능과 검색, 직접 고칠 수 있는 상태로": "兼顾性能与检索，并交付为可自行修改的状态",

"Query-Aware Cost-Efficient RAG via a Lightweight Pipeline Controller<br>2026, 건국대학교 정보통신대학원":
"Query-Aware Cost-Efficient RAG via a Lightweight Pipeline Controller<br>2026，建国大学信息通信研究生院",
"모든 질의에 같은 고비용 파이프라인을 물리면 쉬운 질문에도 비용과 지연이 그대로 붙습니다.":
"如果所有查询都走同一条高成本流水线，简单问题也要付出同样的成本与延迟。",
"질의 난이도를 먼저 재고, 하이브리드 검색과 재랭킹, HyDE를 필요할 때만 켜는 경량 컨트롤러를 붙였습니다.":
"因此加入了一个轻量控制器：先估计查询难度，只在需要时才启用混合检索、重排序与 HyDE。",
"基于MapReduce的电力行业数据挖掘并行化实现<br>2020, 동북전력대학교 Northeast Electric Power University":
"基于MapReduce的电力行业数据挖掘并行化实现<br>2020，东北电力大学",
"스마트미터가 쏟아내는 사용량 데이터는 단일 장비로 감당이 안 됩니다.":
"智能电表产生的用电数据量，单机已经无法处理。",
"가상머신에 3노드 Hadoop 클러스터를 올리고 MapReduce K-means로 사용 패턴을 나눴습니다.":
"在虚拟机上搭建三节点 Hadoop 集群，用 MapReduce K-means 对用电模式进行了聚类划分。",

"빅데이터분석기사": "大数据分析工程师",
"데이터아키텍처준전문가 (DAsP)": "数据架构准专家 (DAsP)",
"SQL 개발자 (SQLD)": "SQL 开发者 (SQLD)",
"데이터분석준전문가 (ADsP)": "数据分析准专家 (ADsP)",
"AI-POT 1급": "AI-POT 一级",
"정보처리기사": "信息处理工程师",
"프로그래밍기능사": "编程技能士",
"리눅스마스터 2급": "Linux Master 二级",
"네트워크관리사 2급": "网络管理师 二级",
"컴퓨터활용능력 1급": "计算机应用能力 一级",
"HSK 5급": "HSK 五级",

"<b>건국대학교 정보통신대학원</b> 융합정보기술학과 인공지능전공 석사":
"<b>建国大学信息通信研究生院</b> 融合信息技术学科 人工智能专业 硕士",
"<b>이어드림스쿨 6기</b> 심화과정<br>중소벤처기업부 AI 기술인력 양성":
"<b>Yeardream School 第6期</b> 进阶课程<br>韩国中小风险企业部 AI 技术人才培养",
"LLM Fine-tuning, RAG와 Vector DB":
"LLM 微调、RAG 与向量数据库",
"LangChain과 LangGraph, AI Agent와 MCP":
"LangChain 与 LangGraph、AI Agent 与 MCP",
"산업 연계 팀 프로젝트":
"产业联动团队项目",
"<b>AI Bootcamp 16기</b> 인공지능모델링<br>6개월 학습 + 1개월 기업 협업":
"<b>AI Bootcamp 第16期</b> 人工智能建模<br>6个月学习 + 1个月企业协作",
"<b>동북전력대학교</b> (China) 소프트웨어공학과 학사<br>4년 과정, 재학 중 군복무 2년":
"<b>东北电力大学</b>（中国）软件工程 本科<br>四年制，在学期间服兵役两年",

"### 신규 프로젝트 문의는 [fornaxworks.com](https://fornaxworks.com) 에서 받고 있습니다.":
"### 新项目咨询请访问 [fornaxworks.com](https://fornaxworks.com)。",
},

"ja": {
"### AI와 풀스택 개발. 기획부터 배포까지 한 사람이 이어서 합니다.":
"### AI とフルスタック開発。企画から本番リリースまで、一人が通しで担当します。",

"건국대학교 정보통신대학원 인공지능전공 석사. 그 전에는 중국에서 4년간 소프트웨어공학을 공부했고 졸업논문을 중국어로 썼습니다.":
"建国大学 情報通信大学院 人工知能専攻 修士。その前は中国でソフトウェア工学を4年間学び、卒業論文を中国語で書きました。",
"석사 논문은 RAG의 비용 문제를, 학사 논문은 전력 데이터의 규모 문제를 다뤘습니다.":
"修士論文では RAG のコスト問題を、学士論文では電力データの規模の問題を扱いました。",
"지금은 [fornaxworks](https://fornaxworks.com)라는 이름으로 웹, 모바일, AI 제품을 만듭니다.":
"現在は [fornaxworks](https://fornaxworks.com) という名前で Web・モバイル・AI プロダクトを作っています。",
"2023년부터 유학 컨설팅 사업체를 대표로 운영해와서 고객 응대와 계약, 행정은 이미 하던 일입니다.":
"2023年から留学コンサルティング事業を代表として運営しており、顧客対応や契約、事務手続きはすでに日常業務です。",
"한국어 외에 영어, 중국어, 일본어로 소통할 수 있습니다.":
"韓国語のほか、英語・中国語・日本語でやり取りできます。",

"브라우저 미니게임 플랫폼. 자체 게임과 사용자 업로드 게임을 하나의 런타임에서 돌립니다. Ports/Adapters로 도메인을 분리했고 e2e 테스트와 staging 환경을 운영합니다.":
"ブラウザ向けミニゲームプラットフォーム。自社ゲームとユーザー投稿ゲームを同一のランタイムで動かします。Ports/Adapters でドメインを分離し、e2e テストと staging 環境を運用しています。",
"HDD SMART 데이터로 7일 안에 고장날 디스크를 예측하고, 점검 순서와 근거 문서, 운영 Runbook을 같이 냅니다. 공개 전 추적 파일 252개를 전수 검사해 개인정보를 걷어냈습니다.":
"HDD の SMART データから7日以内に故障するディスクを予測し、点検順序・根拠文書・運用 Runbook をあわせて出します。公開前に追跡ファイル252件を全数検査し、個人情報を除去しました。",
"사진 한 장을 동화로 바꾸는 인터랙티브 스토리 플랫폼. 대학원 과제로 시스템 설계와 UX, 비즈니스 전략까지 32p 문서로 정리했습니다.":
"写真1枚を童話に変えるインタラクティブなストーリープラットフォーム。大学院の課題として、システム設計・UX・ビジネス戦略まで32ページの文書にまとめました。",
"스튜디오 사이트. 프레임워크 없이 Python 스크립트로 HTML을 굽고 Cloudflare Worker에 올립니다. 로고와 OG 이미지도 코드로 그립니다.":
"スタジオのサイトそのもの。フレームワークを使わず Python スクリプトで HTML を生成し、Cloudflare Worker に載せています。ロゴと OG 画像もコードで描いています。",
"공동주택 공사비 예측 모델. 직접 만든 크롤러 [kapt_crawler](https://github.com/TaeyanG4/kapt_crawler)로 모은 K-APT 공개 데이터를 씁니다.":
"集合住宅の工事費予測モデル。自作クローラー [kapt_crawler](https://github.com/TaeyanG4/kapt_crawler) で収集した K-APT の公開データを使っています。",
"(공개 예정)": "（公開予定）",

"fornaxworks 견본실에 올려둔 데모입니다. 실제 납품물이 아니라 어디까지 만드는지 보여주려고 직접 만든 견본입니다.":
"fornaxworks のショールームに置いているデモです。実際の納品物ではなく、どこまで作るのかを示すために自分で作った見本です。",
"이미지를 누르면 브라우저에서 바로 열립니다.":
"画像をクリックするとブラウザでそのまま開きます。",

"<b>PALLET</b> 웹 서비스": "<b>PALLET</b> Web サービス",
"가입, 권한, 결제까지 한 벌": "登録・権限・決済まで一式",
"<b>TAG</b> 커머스": "<b>TAG</b> EC",
"취소, 반품, 정산을 상태로 설계": "キャンセル・返品・精算を状態として設計",
"<b>MAT</b> 모바일 앱": "<b>MAT</b> モバイルアプリ",
"iOS와 Android를 한 코드로,<br>스토어 심사까지": "iOS と Android を1つのコードで、<br>ストア審査まで",
"<b>INDEX</b> 문서 검색 어시스턴트": "<b>INDEX</b> ドキュメント検索アシスタント",
"하이브리드 검색과 재순위, 근거 문단 표기": "ハイブリッド検索とリランキング、根拠段落の提示",
"<b>CLERK</b> 반복 업무 에이전트": "<b>CLERK</b> 定型業務エージェント",
"도구 호출 파이프라인, 최종 승인은 사람이": "ツール呼び出しパイプライン、最終承認は人が行う",
"<b>TALLY</b> 데이터 대시보드": "<b>TALLY</b> データダッシュボード",
"차트보다 매일 최신이 되는 파이프라인": "グラフよりも、毎日自動で最新になるパイプラインが要",
"<b>STAMP</b> 사내 업무 시스템": "<b>STAMP</b> 社内業務システム",
"역할별 권한과 지울 수 없는 감사 로그": "ロール別権限と、消せない監査ログ",
"<b>BRIDGE</b> 레거시 이관": "<b>BRIDGE</b> レガシー移行",
"무중단 단계 이관, 되돌릴 수 있는 배포": "無停止の段階的移行と、切り戻せるデプロイ",
"<b>BEACON</b> 브랜드와 랜딩 사이트": "<b>BEACON</b> ブランド・ランディングサイト",
"성능과 검색, 직접 고칠 수 있는 상태로": "速度と検索性を保ち、自分で直せる状態で引き渡す",

"Query-Aware Cost-Efficient RAG via a Lightweight Pipeline Controller<br>2026, 건국대학교 정보통신대학원":
"Query-Aware Cost-Efficient RAG via a Lightweight Pipeline Controller<br>2026年、建国大学 情報通信大学院",
"모든 질의에 같은 고비용 파이프라인을 물리면 쉬운 질문에도 비용과 지연이 그대로 붙습니다.":
"すべてのクエリを同じ高コストのパイプラインに通すと、簡単な質問にもコストとレイテンシがそのままかかります。",
"질의 난이도를 먼저 재고, 하이브리드 검색과 재랭킹, HyDE를 필요할 때만 켜는 경량 컨트롤러를 붙였습니다.":
"そこでクエリの難易度を先に見積もり、ハイブリッド検索・リランキング・HyDE を必要なときだけ有効にする軽量コントローラーを組み込みました。",
"基于MapReduce的电力行业数据挖掘并行化实现<br>2020, 동북전력대학교 Northeast Electric Power University":
"基于MapReduce的电力行业数据挖掘并行化实现<br>2020年、東北電力大学 Northeast Electric Power University",
"스마트미터가 쏟아내는 사용량 데이터는 단일 장비로 감당이 안 됩니다.":
"スマートメーターが吐き出す使用量データは、単一のマシンでは処理しきれません。",
"가상머신에 3노드 Hadoop 클러스터를 올리고 MapReduce K-means로 사용 패턴을 나눴습니다.":
"仮想マシン上に3ノードの Hadoop クラスタを構築し、MapReduce K-means で使用パターンを分類しました。",

"빅데이터분석기사": "ビッグデータ分析技士",
"데이터아키텍처준전문가 (DAsP)": "データアーキテクチャ準専門家 (DAsP)",
"SQL 개발자 (SQLD)": "SQL 開発者 (SQLD)",
"데이터분석준전문가 (ADsP)": "データ分析準専門家 (ADsP)",
"AI-POT 1급": "AI-POT 1級",
"정보처리기사": "情報処理技士",
"프로그래밍기능사": "プログラミング技能士",
"리눅스마스터 2급": "Linux Master 2級",
"네트워크관리사 2급": "ネットワーク管理士 2級",
"컴퓨터활용능력 1급": "コンピュータ活用能力 1級",
"HSK 5급": "HSK 5級",

"<b>건국대학교 정보통신대학원</b> 융합정보기술학과 인공지능전공 석사":
"<b>建国大学 情報通信大学院</b> 融合情報技術学科 人工知能専攻 修士",
"<b>이어드림스쿨 6기</b> 심화과정<br>중소벤처기업부 AI 기술인력 양성":
"<b>Yeardream School 第6期</b> 応用コース<br>韓国中小ベンチャー企業部 AI 技術人材育成",
"LLM Fine-tuning, RAG와 Vector DB":
"LLM ファインチューニング、RAG とベクトル DB",
"LangChain과 LangGraph, AI Agent와 MCP":
"LangChain と LangGraph、AI エージェントと MCP",
"산업 연계 팀 프로젝트":
"産業連携チームプロジェクト",
"<b>AI Bootcamp 16기</b> 인공지능모델링<br>6개월 학습 + 1개월 기업 협업":
"<b>AI Bootcamp 第16期</b> 人工知能モデリング<br>6か月の学習 + 1か月の企業協業",
"<b>동북전력대학교</b> (China) 소프트웨어공학과 학사<br>4년 과정, 재학 중 군복무 2년":
"<b>東北電力大学</b>（中国）ソフトウェア工学 学士<br>4年課程、在学中に兵役2年",

"### 신규 프로젝트 문의는 [fornaxworks.com](https://fornaxworks.com) 에서 받고 있습니다.":
"### 新規プロジェクトのご相談は [fornaxworks.com](https://fornaxworks.com) で受け付けています。",
},
}

ALT = {"en": "fornaxworks forging ideas into shippable products",
       "zh": "fornaxworks 把想法锻造成可交付的产品",
       "ja": "fornaxworks アイデアを出荷できるプロダクトへ鍛える"}


def build(lang):
    s = SRC.read_text(encoding="utf-8")
    s = s.replace(NAV["ko"], NAV[lang])
    s = s.replace("fornaxworks 아이디어를 출하 가능한 제품으로 벼립니다", ALT[lang])
    # 긴 원문부터 치환해야 짧은 문구가 먼저 먹어버리지 않는다
    for src in sorted(T[lang], key=len, reverse=True):
        s = s.replace(src, T[lang][src])
    return s


def main():
    for lang in ("en", "zh", "ja"):
        out = SRC.parent / f"README.{lang}.md"
        text = build(lang)
        out.write_text(text, encoding="utf-8")
        left = len(re.findall(r"[가-힣]", text))
        print(f"  README.{lang}.md  남은 한글 {left}자")


if __name__ == "__main__":
    main()
