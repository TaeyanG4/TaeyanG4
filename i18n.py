# -*- coding: utf-8 -*-
"""README.md 를 원본으로 삼아 언어판 3종을 굽는다.

    python i18n.py
    python i18n.py --check

한국어판만 손보면 나머지는 여기 표만 고치면 된다. 뼈대(표, 뱃지, 이미지)는
그대로 두고 문장만 바꾼다. 미번역 문장이 있으면 모든 파일 쓰기를 중단한다.
--check는 파일을 쓰지 않고 번역 누락과 생성 결과의 차이를 확인한다.
"""
import argparse
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
"포맷 직후 다시 깔 프로그램을 골라 한 번에 받는 곳. 프로그램 110개를 한국어·영어·일본어로 다루고, 개인은 무료지만 기업은 유료인 프로그램을 근거와 확인 날짜까지 적어 구분합니다. winget 매니페스트를 매일 훑어 새 버전을 PR 로 올리고, 사람이 확인해야 반영됩니다.":
"Pick the programs you use and get them all back in one go after reformatting. 110 programs in Korean, English and Japanese, each marked with whether it is licensed for business use — with the evidence and the date it was checked. winget manifests are scanned daily and land as pull requests a person has to review.",

"종료된 Kaggle 대회의 공개 풀이 글을 순위와 관계없이 모아, 풀이마다 어떤 기법을 썼는지 원문 링크와 순위 근거까지 붙였습니다. 요약과 기법 판정은 모델이 읽은 저자 주장입니다.":
"Collected public solution writeups from completed Kaggle competitions regardless of rank, with the techniques used in each solution, links to the original posts, and evidence for the rankings. The summaries and technique labels reflect the model's reading of authors' claims.",

"한국 공공조달의 입찰·투찰·낙찰·계약과 관련 주체를 같은 키로 연결했습니다. 단계마다 의미가 달라 하나로 합치지 않고 키와 출처를 그대로 보존합니다.":
"Links tenders, bid submissions, awards, contracts, and related entities in Korean public procurement through common keys. Each stage has a different meaning, so the stages are kept separate and their keys and sources are preserved.",

"전력거래소의 수요 예측, 발전기 지시량, 추정 출력을 5분 간격으로 정리했습니다. 전체 이력은 Parquet, 최근 한 달은 CSV로 올려 둘 다 바로 열립니다.":
"Organizes the Korea Power Exchange's demand forecasts, generator dispatch quantities, and estimated output at 5-minute intervals. The full history is uploaded as Parquet and the most recent month as CSV, so both can be opened directly.",

"관세청 수출입 실적을 상대국 × 월 × 10자리 HSK 품목으로 정리하고, 상위 HS 단위는 HSK10에서 파생해 함께 넣었습니다.":
"Organizes Korea Customs Service import and export records by partner country × month × 10-digit HSK item, with higher HS levels derived from HSK10 and included alongside them.",

"스미스소니언 Open Access의 이미지와 설명문을 권리까지 확인해 묶고, 같은 유물이 학습과 평가에 나뉘어 섞이지 않도록 분할했습니다.":
"Pairs Smithsonian Open Access images with descriptions after checking their rights, and splits the data so the same object does not appear in both training and evaluation.",

"전국 일반음식점·휴게음식점·제과점의 현재 영업 허가 상태를 한 번에 담은 스냅샷입니다.":
"A snapshot of the current operating permit status of general restaurants, refreshment restaurants, and bakeries nationwide.",

"미국 NHTSA가 받은 자율주행·ADAS 사고 보고서를 현행 보고 규정 기준으로 정리했습니다. 보고 주체별 건수는 사고율이나 안전 순위가 아닙니다.":
"Organizes autonomous driving and ADAS crash reports received by the US NHTSA under the current reporting rules. Counts by reporting entity are not crash rates or safety rankings.",

"### AI와 풀스택 개발. 기획부터 배포까지 한 사람이 이어서 합니다.":
"### AI and full-stack development. One person carrying a product from spec to deployment.",

"건국대학교 정보통신대학원에서 인공지능 전공하여 석사학위를 받았습니다. 그 전에는 중국에서 4년간 소프트웨어공학을 공부했으며, 학사 졸업논문 역시 중국어로 작성했습니다.":
"I earned a master’s degree in Artificial Intelligence at Konkuk University Graduate School of Information and Telecommunications. Before that, I studied Software Engineering in China for four years and wrote my undergraduate thesis in Chinese.",
"석사 논문에서는 RAG(Retrieval-Augmented Generation)의 비용 문제를 다뤘고, 학사 논문에서는 Hadoop을 활용해 전력 데이터의 사용 패턴을 분석하는 연구를 진행했습니다.":
"My master’s thesis addressed the cost of RAG (Retrieval-Augmented Generation). My undergraduate research used Hadoop to analyze electricity consumption patterns.",
"현재는 <a href=\"https://fornaxworks.com\">Fornax</a> 라는 이름으로 웹, 모바일, AI 제품을 만들고 있습니다. 또한 2023년부터 유학 컨설팅 사업체를 운영하며 고객 상담부터 계약까지 직접 담당해왔기 때문에, 고객과의 커뮤니케이션과 비즈니스 실무에도 익숙합니다.":
"I currently build web, mobile, and AI products under the name <a href=\"https://fornaxworks.com\">Fornax</a>. I have also run a study abroad consulting business since 2023, handling client consultations and contracts directly, so I am familiar with client communication and business operations.",
"2023년부터 유학 컨설팅 사업체를 대표로 운영해와서 고객 응대와 계약, 행정은 이미 하던 일입니다.":
"Running a study abroad consulting agency as its owner since 2023 means client work, contracts, and administration are already familiar ground.",
"한국어를 비롯해 영어, 중국어, 일본어로 소통할 수 있습니다.":
"I communicate in Korean, English, Chinese, and Japanese.",

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

"[fornaxworks 견본실](https://fornaxworks.com/gallery.html)에 올려둔 데모입니다. 실제 납품물이 아니라 어디까지 만드는지 보여주기위한 직접 만든 견본입니다.":
"Demos from the [fornaxworks showroom](https://fornaxworks.com/gallery.html). These are not client deliverables. I built them to show how far the work goes.",
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
"운영 데이터 품질 감사 파이프라인. 공개 태양광 발전 자료 1,440만 행을 검증한 결과만 게시하고, 실패하면 이전 결과를 지키며, 월간 보고서의 숫자를 원본까지 추적합니다. 빈 머신에서 Compose·Airflow·쿠버네티스까지 그대로 재현되는 것을 자동으로 확인합니다.": "Operational data quality audit pipeline. Validates 14.4 million rows of public solar generation data, publishes only what passes, keeps the previous result when a run fails, and traces every number in the monthly report back to its source. An automated run confirms the whole stack, from Compose and Airflow to Kubernetes, reproduces on an empty machine.",
"<b>VITAL</b> 설비 예방 점검": "<b>VITAL</b> Predictive equipment maintenance",
"오늘 먼저 볼 장비를 근거와 함께": "Which machines to check today, with the evidence",
"<b>SIFT</b> 공공 데이터 수집기": "<b>SIFT</b> Public data collector",
"무엇을 안 긁을지 먼저 정하는 수집기": "A collector that decides first what not to scrape",
"<b>SOLAROPS</b> 운영 데이터 품질 감사": "<b>SOLAROPS</b> Operational data quality audit",
"검증한 결과만 게시, 숫자는 원본까지": "Publishes only validated results, traces numbers to the source",

"**[경량 파이프라인 컨트롤러를 통한 질의 인식 기반 비용 효율적 RAG](https://www.riss.kr/link?id=T17380351)**":
"**[Query-Aware Cost-Efficient RAG via a Lightweight Pipeline Controller](https://www.riss.kr/link?id=T17380351)**",
"Query-Aware Cost-Efficient RAG via a Lightweight Pipeline Controller<br>2026, 건국대학교 정보통신대학원":
"경량 파이프라인 컨트롤러를 통한 질의 인식 기반 비용 효율적 RAG<br>2026, Konkuk University Graduate School of Information and Telecommunications",
"모든 질의에 같은 고비용 파이프라인을 물리면 쉬운 질문에도 비용과 지연이 그대로 붙습니다.":
"Running every query through the same expensive pipeline makes easy questions pay full price in cost and latency.",
"질의 난이도를 먼저 재고, 하이브리드 검색과 재랭킹, HyDE를 필요할 때만 켜는 경량 컨트롤러를 붙였습니다.":
"I added a lightweight controller that estimates query difficulty first, then switches on hybrid retrieval, reranking, and HyDE only when they are needed.",
"> **基于MapReduce的电力行业数据挖掘并行化实现**\n>\n> Parallelization of Data Mining in Power Industry Based on MapReduce<br>2020, 동북전력대학교 Northeast Electric Power University":
"> Parallelization of Data Mining in Power Industry Based on MapReduce\n>\n> 基于MapReduce的电力行业数据挖掘并行化实现<br>2020, Northeast Electric Power University",
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
"성적표 보기 (개인정보 마스킹)": "View transcript (personal details redacted)",

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
"<b>동북전력대학교</b> (China) 소프트웨어공학과 학사<br>4년 과정, 재학 중 군복무 1년 9개월":
"<b>Northeast Electric Power University</b> (China), BSc in Software Engineering<br>4-year programme, with 1 year 9 months of military service during enrolment",

"### 신규 프로젝트 문의는 [fornaxworks.com](https://fornaxworks.com) 에서 받고 있습니다.":
"### New project enquiries are welcome at [fornaxworks.com](https://fornaxworks.com).",
},

"zh": {
"포맷 직후 다시 깔 프로그램을 골라 한 번에 받는 곳. 프로그램 110개를 한국어·영어·일본어로 다루고, 개인은 무료지만 기업은 유료인 프로그램을 근거와 확인 날짜까지 적어 구분합니다. winget 매니페스트를 매일 훑어 새 버전을 PR 로 올리고, 사람이 확인해야 반영됩니다.":
"重装系统后一次性取回常用软件的站点。以韩语、英语、日语收录 110 款软件，并标注个人免费但企业需付费的软件，附上依据与核对日期。每日扫描 winget 清单，新版本以 Pull Request 形式提交，需人工确认后才会发布。",

"종료된 Kaggle 대회의 공개 풀이 글을 순위와 관계없이 모아, 풀이마다 어떤 기법을 썼는지 원문 링크와 순위 근거까지 붙였습니다. 요약과 기법 판정은 모델이 읽은 저자 주장입니다.":
"收集已结束的 Kaggle 竞赛的公开解题文章，不限排名，并为每篇解答标注所用技术、原文链接和排名依据。摘要和技术判定反映的是模型对作者主张的解读。",

"한국 공공조달의 입찰·투찰·낙찰·계약과 관련 주체를 같은 키로 연결했습니다. 단계마다 의미가 달라 하나로 합치지 않고 키와 출처를 그대로 보존합니다.":
"用相同的键关联韩国公共采购的招标、投标、中标、合同及相关主体。各阶段含义不同，因此不合并为一体，原样保留键和来源。",

"전력거래소의 수요 예측, 발전기 지시량, 추정 출력을 5분 간격으로 정리했습니다. 전체 이력은 Parquet, 최근 한 달은 CSV로 올려 둘 다 바로 열립니다.":
"将韩国电力交易所的需求预测、发电机调度指令量和估算出力整理为 5 分钟间隔的数据。完整历史以 Parquet 格式上传，最近一个月以 CSV 格式上传，两者均可直接打开。",

"관세청 수출입 실적을 상대국 × 월 × 10자리 HSK 품목으로 정리하고, 상위 HS 단위는 HSK10에서 파생해 함께 넣었습니다.":
"将韩国关税厅的进出口实绩按贸易伙伴国 × 月 × 10 位 HSK 商品编码整理，并从 HSK10 派生上级 HS 层级，一并收录。",

"스미스소니언 Open Access의 이미지와 설명문을 권리까지 확인해 묶고, 같은 유물이 학습과 평가에 나뉘어 섞이지 않도록 분할했습니다.":
"核对权利后，将史密森尼 Open Access 的图片与说明文字整理在一起，并划分数据，避免同一件藏品同时出现在训练集和评估集中。",

"전국 일반음식점·휴게음식점·제과점의 현재 영업 허가 상태를 한 번에 담은 스냅샷입니다.":
"一次性收录全国一般餐饮店、休闲餐饮店和糕点店当前营业许可状态的快照。",

"미국 NHTSA가 받은 자율주행·ADAS 사고 보고서를 현행 보고 규정 기준으로 정리했습니다. 보고 주체별 건수는 사고율이나 안전 순위가 아닙니다.":
"按现行报告规定整理美国 NHTSA 收到的自动驾驶与 ADAS 事故报告。按报告主体统计的数量不代表事故率或安全排名。",

"### AI와 풀스택 개발. 기획부터 배포까지 한 사람이 이어서 합니다.":
"### AI 与全栈开发。从策划到部署，由一个人一路负责到底。",

"건국대학교 정보통신대학원에서 인공지능 전공하여 석사학위를 받았습니다. 그 전에는 중국에서 4년간 소프트웨어공학을 공부했으며, 학사 졸업논문 역시 중국어로 작성했습니다.":
"我在建国大学信息通信研究生院获得了人工智能专业硕士学位。此前在中国学习了四年软件工程，本科毕业论文也用中文撰写。",
"석사 논문에서는 RAG(Retrieval-Augmented Generation)의 비용 문제를 다뤘고, 학사 논문에서는 Hadoop을 활용해 전력 데이터의 사용 패턴을 분석하는 연구를 진행했습니다.":
"硕士论文研究了 RAG（检索增强生成）的成本问题，本科论文则使用 Hadoop 分析电力数据中的用电模式。",
"현재는 <a href=\"https://fornaxworks.com\">Fornax</a> 라는 이름으로 웹, 모바일, AI 제품을 만들고 있습니다. 또한 2023년부터 유학 컨설팅 사업체를 운영하며 고객 상담부터 계약까지 직접 담당해왔기 때문에, 고객과의 커뮤니케이션과 비즈니스 실무에도 익숙합니다.":
"目前以 <a href=\"https://fornaxworks.com\">Fornax</a> 的名义开发 Web、移动端和 AI 产品。自 2023 年起经营留学咨询业务，从客户咨询到签约都亲自负责，因此也熟悉客户沟通和业务实务。",
"2023년부터 유학 컨설팅 사업체를 대표로 운영해와서 고객 응대와 계약, 행정은 이미 하던 일입니다.":
"自 2023 年起以负责人身份经营留学咨询公司，客户沟通、合同与行政事务是本来就在做的工作。",
"한국어를 비롯해 영어, 중국어, 일본어로 소통할 수 있습니다.":
"可以使用韩语、英语、中文和日语沟通。",

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

"[fornaxworks 견본실](https://fornaxworks.com/gallery.html)에 올려둔 데모입니다. 실제 납품물이 아니라 어디까지 만드는지 보여주기위한 직접 만든 견본입니다.":
"这些是放在 [fornaxworks 样品间](https://fornaxworks.com/gallery.html)的演示。并非实际交付物，而是为了展示能做到什么程度而自行制作的样品。",
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
"운영 데이터 품질 감사 파이프라인. 공개 태양광 발전 자료 1,440만 행을 검증한 결과만 게시하고, 실패하면 이전 결과를 지키며, 월간 보고서의 숫자를 원본까지 추적합니다. 빈 머신에서 Compose·Airflow·쿠버네티스까지 그대로 재현되는 것을 자동으로 확인합니다.": "运营数据质量审计流水线。校验 1,440 万行公开光伏发电数据，只发布通过校验的结果，运行失败时保留上一版结果，并把月报中的每个数字追溯到原始数据。自动化运行确认了从 Compose、Airflow 到 Kubernetes 的整套环境能在空白机器上复现。",
"<b>VITAL</b> 설비 예방 점검": "<b>VITAL</b> 设备预防性巡检",
"오늘 먼저 볼 장비를 근거와 함께": "今天先查哪些设备，并附上依据",
"<b>SIFT</b> 공공 데이터 수집기": "<b>SIFT</b> 公共数据采集器",
"무엇을 안 긁을지 먼저 정하는 수집기": "先决定哪些不抓取的采集器",
"<b>SOLAROPS</b> 운영 데이터 품질 감사": "<b>SOLAROPS</b> 运营数据质量审计",
"검증한 결과만 게시, 숫자는 원본까지": "只发布已校验的结果，数字可追溯到原始数据",

"Query-Aware Cost-Efficient RAG via a Lightweight Pipeline Controller<br>2026, 건국대학교 정보통신대학원":
"Query-Aware Cost-Efficient RAG via a Lightweight Pipeline Controller<br>2026，建国大学信息通信研究生院",
"모든 질의에 같은 고비용 파이프라인을 물리면 쉬운 질문에도 비용과 지연이 그대로 붙습니다.":
"如果所有查询都走同一条高成本流水线，简单问题也要付出同样的成本与延迟。",
"질의 난이도를 먼저 재고, 하이브리드 검색과 재랭킹, HyDE를 필요할 때만 켜는 경량 컨트롤러를 붙였습니다.":
"因此加入了一个轻量控制器：先估计查询难度，只在需要时才启用混合检索、重排序与 HyDE。",
"> **基于MapReduce的电力行业数据挖掘并行化实现**\n>\n> Parallelization of Data Mining in Power Industry Based on MapReduce<br>2020, 동북전력대학교 Northeast Electric Power University":
"> Parallelization of Data Mining in Power Industry Based on MapReduce\n>\n> 基于MapReduce的电力行业数据挖掘并行化实现<br>2020，东北电力大学",
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
"성적표 보기 (개인정보 마스킹)": "查看成绩单（个人信息已遮盖）",

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
"<b>동북전력대학교</b> (China) 소프트웨어공학과 학사<br>4년 과정, 재학 중 군복무 1년 9개월":
"<b>东北电力大学</b>（中国）软件工程 本科<br>四年制，在学期间服兵役1年9个月",

"### 신규 프로젝트 문의는 [fornaxworks.com](https://fornaxworks.com) 에서 받고 있습니다.":
"### 新项目咨询请访问 [fornaxworks.com](https://fornaxworks.com)。",
},

"ja": {
"포맷 직후 다시 깔 프로그램을 골라 한 번에 받는 곳. 프로그램 110개를 한국어·영어·일본어로 다루고, 개인은 무료지만 기업은 유료인 프로그램을 근거와 확인 날짜까지 적어 구분합니다. winget 매니페스트를 매일 훑어 새 버전을 PR 로 올리고, 사람이 확인해야 반영됩니다.":
"初期化のあとに入れ直すソフトをまとめて取得できる場所。110本を韓国語・英語・日本語で扱い、個人は無料でも法人は有料というソフトを、根拠と確認日を添えて区別して表示します。winget のマニフェストを毎日走査し、新しいバージョンは人が確認するプルリクエストとして上がります。",

"종료된 Kaggle 대회의 공개 풀이 글을 순위와 관계없이 모아, 풀이마다 어떤 기법을 썼는지 원문 링크와 순위 근거까지 붙였습니다. 요약과 기법 판정은 모델이 읽은 저자 주장입니다.":
"終了した Kaggle 大会の公開解法記事を順位にかかわらず集め、各解法で使われた手法に原文リンクと順位の根拠を添えました。要約と手法の判定は、モデルが読み取った著者の主張です。",

"한국 공공조달의 입찰·투찰·낙찰·계약과 관련 주체를 같은 키로 연결했습니다. 단계마다 의미가 달라 하나로 합치지 않고 키와 출처를 그대로 보존합니다.":
"韓国の公共調達における入札・応札・落札・契約と関連主体を共通のキーで結びました。各段階で意味が異なるため、一つにまとめずキーと出典をそのまま保持しています。",

"전력거래소의 수요 예측, 발전기 지시량, 추정 출력을 5분 간격으로 정리했습니다. 전체 이력은 Parquet, 최근 한 달은 CSV로 올려 둘 다 바로 열립니다.":
"韓国電力取引所の需要予測、発電機への出力指示量、推定出力を5分間隔で整理しました。全履歴は Parquet、直近1か月は CSV で公開し、どちらもそのまま開けます。",

"관세청 수출입 실적을 상대국 × 월 × 10자리 HSK 품목으로 정리하고, 상위 HS 단위는 HSK10에서 파생해 함께 넣었습니다.":
"韓国関税庁の輸出入実績を相手国 × 月 × 10桁の HSK 品目で整理し、上位の HS 単位は HSK10 から派生させてあわせて収録しました。",

"스미스소니언 Open Access의 이미지와 설명문을 권리까지 확인해 묶고, 같은 유물이 학습과 평가에 나뉘어 섞이지 않도록 분할했습니다.":
"スミソニアン Open Access の画像と説明文を権利も確認してまとめ、同じ収蔵品が学習用と評価用の両方に含まれないように分割しました。",

"전국 일반음식점·휴게음식점·제과점의 현재 영업 허가 상태를 한 번에 담은 스냅샷입니다.":
"全国の一般飲食店・休憩飲食店・製菓店の現在の営業許可状況を一度に収録したスナップショットです。",

"미국 NHTSA가 받은 자율주행·ADAS 사고 보고서를 현행 보고 규정 기준으로 정리했습니다. 보고 주체별 건수는 사고율이나 안전 순위가 아닙니다.":
"米国 NHTSA が受け取った自動運転・ADAS の事故報告を、現行の報告規定に基づいて整理しました。報告主体別の件数は、事故率や安全性の順位を示すものではありません。",

"### AI와 풀스택 개발. 기획부터 배포까지 한 사람이 이어서 합니다.":
"### AI とフルスタック開発。企画から本番リリースまで、一人が通しで担当します。",

"건국대학교 정보통신대학원에서 인공지능 전공하여 석사학위를 받았습니다. 그 전에는 중국에서 4년간 소프트웨어공학을 공부했으며, 학사 졸업논문 역시 중국어로 작성했습니다.":
"建国大学 情報通信大学院で人工知能を専攻し、修士号を取得しました。その前は中国でソフトウェア工学を4年間学び、学士論文も中国語で執筆しました。",
"석사 논문에서는 RAG(Retrieval-Augmented Generation)의 비용 문제를 다뤘고, 학사 논문에서는 Hadoop을 활용해 전력 데이터의 사용 패턴을 분석하는 연구를 진행했습니다.":
"修士論文では RAG（検索拡張生成）のコスト問題を扱い、学士論文では Hadoop を使って電力データの使用パターンを分析しました。",
"현재는 <a href=\"https://fornaxworks.com\">Fornax</a> 라는 이름으로 웹, 모바일, AI 제품을 만들고 있습니다. 또한 2023년부터 유학 컨설팅 사업체를 운영하며 고객 상담부터 계약까지 직접 담당해왔기 때문에, 고객과의 커뮤니케이션과 비즈니스 실무에도 익숙합니다.":
"現在は <a href=\"https://fornaxworks.com\">Fornax</a> という名前で Web、モバイル、AI プロダクトを作っています。また、2023年から留学コンサルティング事業を運営し、顧客相談から契約まで直接担当してきたため、顧客とのコミュニケーションやビジネス実務にも慣れています。",
"2023년부터 유학 컨설팅 사업체를 대표로 운영해와서 고객 응대와 계약, 행정은 이미 하던 일입니다.":
"2023年から留学コンサルティング事業を代表として運営しており、顧客対応や契約、事務手続きはすでに日常業務です。",
"한국어를 비롯해 영어, 중국어, 일본어로 소통할 수 있습니다.":
"韓国語、英語、中国語、日本語でやり取りできます。",

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

"[fornaxworks 견본실](https://fornaxworks.com/gallery.html)에 올려둔 데모입니다. 실제 납품물이 아니라 어디까지 만드는지 보여주기위한 직접 만든 견본입니다.":
"[fornaxworks のショールーム](https://fornaxworks.com/gallery.html)に置いているデモです。実際の納品物ではなく、どこまで作るのかを示すために自分で作った見本です。",
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
"운영 데이터 품질 감사 파이프라인. 공개 태양광 발전 자료 1,440만 행을 검증한 결과만 게시하고, 실패하면 이전 결과를 지키며, 월간 보고서의 숫자를 원본까지 추적합니다. 빈 머신에서 Compose·Airflow·쿠버네티스까지 그대로 재현되는 것을 자동으로 확인합니다.": "運用データの品質監査パイプライン。公開されている太陽光発電データ 1,440 万行を検証し、通過した結果だけを公開します。失敗したときは前回の結果を守り、月次レポートの数字を元データまでたどれます。Compose・Airflow から Kubernetes まで、空のマシンでそのまま再現できることを自動で確認しています。",
"<b>VITAL</b> 설비 예방 점검": "<b>VITAL</b> 設備の予防点検",
"오늘 먼저 볼 장비를 근거와 함께": "今日まず点検する機器を根拠とともに",
"<b>SIFT</b> 공공 데이터 수집기": "<b>SIFT</b> 公共データ収集ツール",
"무엇을 안 긁을지 먼저 정하는 수집기": "何を集めないかを先に決める収集ツール",
"<b>SOLAROPS</b> 운영 데이터 품질 감사": "<b>SOLAROPS</b> 運用データ品質監査",
"검증한 결과만 게시, 숫자는 원본까지": "検証済みの結果だけを公開し、数字は元データまで",

"Query-Aware Cost-Efficient RAG via a Lightweight Pipeline Controller<br>2026, 건국대학교 정보통신대학원":
"Query-Aware Cost-Efficient RAG via a Lightweight Pipeline Controller<br>2026年、建国大学 情報通信大学院",
"모든 질의에 같은 고비용 파이프라인을 물리면 쉬운 질문에도 비용과 지연이 그대로 붙습니다.":
"すべてのクエリを同じ高コストのパイプラインに通すと、簡単な質問にもコストとレイテンシがそのままかかります。",
"질의 난이도를 먼저 재고, 하이브리드 검색과 재랭킹, HyDE를 필요할 때만 켜는 경량 컨트롤러를 붙였습니다.":
"そこでクエリの難易度を先に見積もり、ハイブリッド検索・リランキング・HyDE を必要なときだけ有効にする軽量コントローラーを組み込みました。",
"> **基于MapReduce的电力行业数据挖掘并行化实现**\n>\n> Parallelization of Data Mining in Power Industry Based on MapReduce<br>2020, 동북전력대학교 Northeast Electric Power University":
"> Parallelization of Data Mining in Power Industry Based on MapReduce\n>\n> 基于MapReduce的电力行业数据挖掘并行化实现<br>2020年、東北電力大学 Northeast Electric Power University",
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
"성적표 보기 (개인정보 마스킹)": "成績表を見る（個人情報をマスキング済み）",

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
"<b>동북전력대학교</b> (China) 소프트웨어공학과 학사<br>4년 과정, 재학 중 군복무 1년 9개월":
"<b>東北電力大学</b>（中国）ソフトウェア工学 学士<br>4年課程、在学中に兵役1年9か月",

"### 신규 프로젝트 문의는 [fornaxworks.com](https://fornaxworks.com) 에서 받고 있습니다.":
"### 新規プロジェクトのご相談は [fornaxworks.com](https://fornaxworks.com) で受け付けています。",
},
}

ALT = {"en": "fornaxworks forging ideas into shippable products",
       "zh": "fornaxworks 把想法锻造成可交付的产品",
       "ja": "fornaxworks アイデアを出荷できるプロダクトへ鍛える"}


def clean_format(text):
    """Remove decorative formatting without changing links, code, or numbers."""
    text = text.replace("**", "")
    text = re.sub(r"</?(?:b|strong)>", "", text)
    text = re.sub(r"&#x0*a0;|&#0*160;|&nbsp;|\u00a0", " ", text, flags=re.I)
    text = text.replace("Crash Reports — NHTSA", "Crash Reports (NHTSA)")
    text = text.replace(" — ", " ").replace("—", " ")
    # Protect HTML attributes, link targets, inline code, dates, and decimals.
    parts = re.split(r"(<[^>]+>|\]\([^)]*\)|`[^`]*`)", text)
    for i in range(0, len(parts), 2):
        part = re.sub(r"(?<!\d),|,(?!\d)", "", parts[i])
        part = re.sub(r"\. +(?=\||$)", " ", part)
        part = re.sub(r"\. +(?=\S)", "<br>", part)
        part = re.sub(r"\.(?=$|[\n<|*])", "", part)
        parts[i] = part
    return "".join(parts)


def build(lang):
    s = SRC.read_text(encoding="utf-8")
    s = s.replace(clean_format(NAV["ko"]), clean_format(NAV[lang]))
    s = s.replace("fornaxworks 아이디어를 출하 가능한 제품으로 벼립니다", ALT[lang])
    # 긴 원문부터 치환해야 짧은 문구가 먼저 먹어버리지 않는다
    for src in sorted(T[lang], key=len, reverse=True):
        s = s.replace(clean_format(src), clean_format(T[lang][src]))
    return clean_format(s)


def validate_translation(lang, text):
    # The language switcher and original master's thesis title stay in Korean.
    allowed = (
        "[한국어](README.md)",
        "경량 파이프라인 컨트롤러를 통한 질의 인식 기반 비용 효율적 RAG",
    )
    for original in allowed:
        text = text.replace(original, "")
    missing = [str(i) for i, line in enumerate(text.splitlines(), 1)
               if re.search(r"[가-힣ㄱ-ㅎㅏ-ㅣ]", line)]
    if missing:
        raise ValueError(f"README.{lang}.md: untranslated Korean at lines {', '.join(missing)}")


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Validate without writing files")
    args = parser.parse_args(argv)
    generated = {lang: build(lang) for lang in ("en", "zh", "ja")}
    # Validate every language before overwriting any existing translation.
    try:
        for lang, text in generated.items():
            validate_translation(lang, text)
    except ValueError as error:
        print(f"ERROR: {error}; no files written")
        return 1
    changed = []
    for lang, text in generated.items():
        out = SRC.parent / f"README.{lang}.md"
        if not out.exists() or out.read_text(encoding="utf-8") != text:
            changed.append(out.name)
            if not args.check:
                out.write_text(text, encoding="utf-8")
    if args.check and changed:
        print(f"Out of date: {', '.join(changed)}; no files written")
        return 1
    print("Translations validated" + (": " + ", ".join(changed) if changed else "; files are current"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
