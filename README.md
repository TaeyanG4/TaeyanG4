<div align="center">

<img src="assets/banner.gif" width="100%" alt="fornaxworks 아이디어를 출하 가능한 제품으로 벼립니다" />

### AI와 풀스택 개발<br>기획부터 배포까지 한 사람이 이어서 합니다

[https://fornaxworks.com](https://fornaxworks.com)

한국어 | [English](README.en.md) | [中文](README.zh.md) | [日本語](README.ja.md)

<a href="https://fornaxworks.com"><img src="assets/badges/fornaxworks-com.svg" alt="fornaxworks" /></a>
<a href="https://owogg.com"><img src="assets/badges/owogg-com.svg" alt="owogg" /></a>
<a href="https://afterformat.com"><img src="assets/badges/afterformat-com.svg" alt="afterformat" /></a>
<a href="https://blog.naver.com/taeyang95"><img src="assets/badges/blog.svg" alt="Blog" /></a>

</div>

<br>

---

## About

<br>
건국대학교 정보통신대학원에서 인공지능 전공하여 석사학위를 받았습니다<br>그 전에는 중국에서 4년간 소프트웨어공학을 공부했으며 학사 졸업논문 역시 중국어로 작성했습니다<br><br>
석사 논문에서는 RAG(Retrieval-Augmented Generation)의 비용 문제를 다뤘고 학사 논문에서는 Hadoop을 활용해 전력 데이터의 사용 패턴을 분석하는 연구를 진행했습니다<br><br>
현재는 <a href="https://fornaxworks.com">Fornax</a> 라는 이름으로 웹 모바일 AI 제품을 만들고 있습니다<br>또한 2023년부터 유학 컨설팅 사업체를 운영하며 고객 상담부터 계약까지 직접 담당해왔기 때문에 고객과의 커뮤니케이션과 비즈니스 실무에도 익숙합니다<br><br>
한국어를 비롯해 영어 중국어 일본어로 소통할 수 있습니다<br><br>
<br>

---

## Projects

<br>

| Project | Description | Stack |
|---|---|---|
| afterformat<br>[afterformat.com](https://afterformat.com) | 포맷 직후 다시 깔 프로그램을 골라 한 번에 받는 곳<br>프로그램 110개를 한국어·영어·일본어로 다루고 개인은 무료지만 기업은 유료인 프로그램을 근거와 확인 날짜까지 적어 구분합니다<br>winget 매니페스트를 매일 훑어 새 버전을 PR 로 올리고 사람이 확인해야 반영됩니다 | `Astro` `React` `Tailwind` `Cloudflare Workers` `D1` |
| project-owogg<br>[owogg.com](https://owogg.com) | 브라우저 미니게임 플랫폼<br>자체 게임과 사용자 업로드 게임을 하나의 런타임에서 돌립니다<br>Ports/Adapters로 도메인을 분리했고 e2e 테스트와 staging 환경을 운영합니다 | `React 19` `Hono` `Cloudflare Workers` `D1` `B2` |
| [dexon-smart-ops-chatbot](https://github.com/TaeyanG4/dexon-smart-ops-chatbot) | HDD SMART 데이터로 7일 안에 고장날 디스크를 예측하고 점검 순서와 근거 문서 운영 Runbook을 같이 냅니다<br>공개 전 추적 파일 252개를 전수 검사해 개인정보를 걷어냈습니다 | `FastAPI` `LlamaIndex` `LiteLLM` `Langfuse` `Docker` |
| [solarops-audit](https://github.com/TaeyanG4/solarops-audit) | 운영 데이터 품질 감사 파이프라인<br>공개 태양광 발전 자료 1,440만 행을 검증한 결과만 게시하고 실패하면 이전 결과를 지키며 월간 보고서의 숫자를 원본까지 추적합니다<br>빈 머신에서 Compose·Airflow·쿠버네티스까지 그대로 재현되는 것을 자동으로 확인합니다 | `Python` `Airflow` `Kubernetes` `PostgreSQL` `MinIO` |
| story_maker_with_photos | 사진 한 장을 동화로 바꾸는 인터랙티브 스토리 플랫폼<br>대학원 과제로 시스템 설계와 UX 비즈니스 전략까지 32p 문서로 정리했습니다 | `GPT-4o` `DALL·E 3` `Gradio` |
| kapt_predict | 공동주택 공사비 예측 모델<br>직접 만든 크롤러 [kapt_crawler](https://github.com/TaeyanG4/kapt_crawler)로 모은 K-APT 공개 데이터를 씁니다 | `CatBoost` `pandas` |

<br>

---

## Datasets

<br>

| Dataset | Description | Scale | Repo |
|---|---|---|---|
| [Kaggle Top Solutions and Strategies](https://www.kaggle.com/datasets/taeyangg4/kaggle-top-solutions-and-strategies) | 종료된 Kaggle 대회의 공개 풀이 글을 순위와 관계없이 모아 풀이마다 어떤 기법을 썼는지 원문 링크와 순위 근거까지 붙였습니다<br>요약과 기법 판정은 모델이 읽은 저자 주장입니다 | `70,576 rows` `4 files` | [repo](https://github.com/TaeyanG4/kaggle-top-solutions-and-strategies) |
| [KONEPS Public Procurement Intelligence](https://www.kaggle.com/datasets/taeyangg4/koneps-public-procurement-intelligence) | 한국 공공조달의 입찰·투찰·낙찰·계약과 관련 주체를 같은 키로 연결했습니다<br>단계마다 의미가 달라 하나로 합치지 않고 키와 출처를 그대로 보존합니다 | `8 files` `2.77 GB` | [repo](https://github.com/TaeyanG4/koneps-procurement-intelligence) |
| [South Korea Power Grid 5-Minute Data](https://www.kaggle.com/datasets/taeyangg4/south-korea-power-grid-5-minute) | 전력거래소의 수요 예측 발전기 지시량 추정 출력을 5분 간격으로 정리했습니다<br>전체 이력은 Parquet 최근 한 달은 CSV로 올려 둘 다 바로 열립니다 | `1B+ rows` `2.49 GB` | [repo](https://github.com/TaeyanG4/korea-power-grid) |
| [South Korea Customs Trade 2012-2026 HSK10](https://www.kaggle.com/datasets/taeyangg4/south-korea-customs-trade-hsk10) | 관세청 수출입 실적을 상대국 × 월 × 10자리 HSK 품목으로 정리하고 상위 HS 단위는 HSK10에서 파생해 함께 넣었습니다 | `22.35M rows` `1.17 GB` | [repo](https://github.com/TaeyanG4/korea-customs-trade) |
| [Smithsonian 25K Museum Image-Text Dataset](https://www.kaggle.com/datasets/taeyangg4/smithsonian-25k-museum-image-text) | 스미스소니언 Open Access의 이미지와 설명문을 권리까지 확인해 묶고 같은 유물이 학습과 평가에 나뉘어 섞이지 않도록 분할했습니다 | `24,972 images` `916 MB` | [repo](https://github.com/TaeyanG4/smithsonian-image-text) |
| [South Korea Food-Service Permits](https://www.kaggle.com/datasets/taeyangg4/korea-food-service-permits) | 전국 일반음식점·휴게음식점·제과점의 현재 영업 허가 상태를 한 번에 담은 스냅샷입니다 | `3.01M rows` `403 MB` | [repo](https://github.com/TaeyanG4/korea-business-lifecycle) |
| [Autonomous Driving Crash Reports (NHTSA)](https://www.kaggle.com/datasets/taeyangg4/nhtsa-autonomous-driving-crashes) | 미국 NHTSA가 받은 자율주행·ADAS 사고 보고서를 현행 보고 규정 기준으로 정리했습니다<br>보고 주체별 건수는 사고율이나 안전 순위가 아닙니다 | `3,263 rows` `123 cols` | [repo](https://github.com/TaeyanG4/nhtsa-autonomous-driving-crashes) |

<br>

---

## Showroom

<br>

[fornaxworks 견본실](https://fornaxworks.com/gallery.html)에 올려둔 데모입니다<br>실제 납품물이 아니라 어디까지 만드는지 보여주기위한 직접 만든 견본입니다<br>
이미지를 누르면 브라우저에서 바로 열립니다

<table align="center">
<tr>
<td width="33.33%" align="center" valign="top">
<a href="https://fornaxworks.com/pallet.html"><img src="assets/gallery/pallet.png" width="100%" alt="PALLET" /></a><br>
PALLET 웹 서비스<br>
가입 권한 결제까지 한 벌<br>
<code>TypeScript</code> <code>Next.js</code> <code>PostgreSQL</code>
</td>
<td width="33.33%" align="center" valign="top">
<a href="https://fornaxworks.com/shop.html"><img src="assets/gallery/shop.png" width="100%" alt="TAG" /></a><br>
TAG 커머스<br>
취소 반품 정산을 상태로 설계<br>
<code>Next.js</code> <code>PostgreSQL</code> <code>Payments</code>
</td>
<td width="33.33%" align="center" valign="top">
<a href="https://fornaxworks.com/mat.html"><img src="assets/gallery/mat.png" width="100%" alt="MAT" /></a><br>
MAT 모바일 앱<br>
iOS와 Android를 한 코드로<br>스토어 심사까지<br>
<code>React Native</code> <code>Expo</code>
</td>
</tr>
<tr>
<td width="33.33%" align="center" valign="top">
<a href="https://fornaxworks.com/guide.html"><img src="assets/gallery/index.png" width="100%" alt="INDEX" /></a><br>
INDEX 문서 검색 어시스턴트<br>
하이브리드 검색과 재순위 근거 문단 표기<br>
<code>Claude API</code> <code>pgvector</code> <code>FastAPI</code>
</td>
<td width="33.33%" align="center" valign="top">
<a href="https://fornaxworks.com/clerk.html"><img src="assets/gallery/clerk.png" width="100%" alt="CLERK" /></a><br>
CLERK 반복 업무 에이전트<br>
도구 호출 파이프라인 최종 승인은 사람이<br>
<code>Claude API</code> <code>Next.js</code>
</td>
<td width="33.33%" align="center" valign="top">
<a href="https://fornaxworks.com/board.html"><img src="assets/gallery/tally.png" width="100%" alt="TALLY" /></a><br>
TALLY 데이터 대시보드<br>
차트보다 매일 최신이 되는 파이프라인<br>
<code>React</code> <code>Python</code> <code>Airflow</code>
</td>
</tr>
<tr>
<td width="33.33%" align="center" valign="top">
<a href="https://fornaxworks.com/stamp.html"><img src="assets/gallery/stamp.png" width="100%" alt="STAMP" /></a><br>
STAMP 사내 업무 시스템<br>
역할별 권한과 지울 수 없는 감사 로그<br>
<code>Remix</code> <code>Prisma</code> <code>MySQL</code>
</td>
<td width="33.33%" align="center" valign="top">
<a href="https://fornaxworks.com/bridge.html"><img src="assets/gallery/bridge.png" width="100%" alt="BRIDGE" /></a><br>
BRIDGE 레거시 이관<br>
무중단 단계 이관 되돌릴 수 있는 배포<br>
<code>Docker</code> <code>Terraform</code> <code>AWS</code>
</td>
<td width="33.33%" align="center" valign="top">
<a href="https://fornaxworks.com/landing.html"><img src="assets/gallery/beacon.png" width="100%" alt="BEACON" /></a><br>
BEACON 브랜드와 랜딩 사이트<br>
성능과 검색 직접 고칠 수 있는 상태로<br>
<code>Next.js</code> <code>Vercel</code>
</td>
</tr>
<tr>
<td width="33.33%" align="center" valign="top">
<a href="https://fornaxworks.com/drive.html"><img src="assets/gallery/vital.png" width="100%" alt="VITAL" /></a><br>
VITAL 설비 예방 점검<br>
오늘 먼저 볼 장비를 근거와 함께<br>
<code>FastAPI</code> <code>XGBoost</code> <code>pgvector</code>
</td>
<td width="33.33%" align="center" valign="top">
<a href="https://fornaxworks.com/crawl.html"><img src="assets/gallery/sift.png" width="100%" alt="SIFT" /></a><br>
SIFT 공공 데이터 수집기<br>
무엇을 안 긁을지 먼저 정하는 수집기<br>
<code>Python</code> <code>pandas</code> <code>PyQt5</code>
</td>
<td width="33.33%" align="center" valign="top">
<a href="https://fornaxworks.com/solar.html"><img src="assets/gallery/solarops.png" width="100%" alt="SOLAROPS" /></a><br>
SOLAROPS 운영 데이터 품질 감사<br>
검증한 결과만 게시 숫자는 원본까지<br>
<code>Python</code> <code>Airflow</code> <code>Kubernetes</code>
</td>
</tr>
</table>

<br>

---

## Research

<br>

### Master's Thesis

> [경량 파이프라인 컨트롤러를 통한 질의 인식 기반 비용 효율적 RAG](https://www.riss.kr/link?id=T17380351)
>
> Query-Aware Cost-Efficient RAG via a Lightweight Pipeline Controller<br>2026 건국대학교 정보통신대학원
>
> 모든 질의에 같은 고비용 파이프라인을 물리면 쉬운 질문에도 비용과 지연이 그대로 붙습니다<br>
> 질의 난이도를 먼저 재고 하이브리드 검색과 재랭킹 HyDE를 필요할 때만 켜는 경량 컨트롤러를 붙였습니다

### Bachelor's Thesis

> 基于MapReduce的电力行业数据挖掘并行化实现
>
> Parallelization of Data Mining in Power Industry Based on MapReduce<br>2020 동북전력대학교 Northeast Electric Power University
>
> 스마트미터가 쏟아내는 사용량 데이터는 단일 장비로 감당이 안 됩니다<br>
> 가상머신에 3노드 Hadoop 클러스터를 올리고 MapReduce K-means로 사용 패턴을 나눴습니다

<br>

---

## Tech Stack

<br>

<div align="center">

### Language

![Python](assets/badges/python.svg)
![TypeScript](assets/badges/typescript.svg)
![JavaScript](assets/badges/javascript.svg)
![Java](assets/badges/java.svg)
![C#](assets/badges/csharp.svg)
![C++](assets/badges/cpp.svg)
![Kotlin](assets/badges/kotlin.svg)
![Go](assets/badges/go.svg)
![SQL](assets/badges/sql.svg)
![R](assets/badges/r.svg)

### AI / ML

![LangChain](assets/badges/langchain.svg)
![LlamaIndex](assets/badges/llamaindex.svg)
![Hugging Face](assets/badges/huggingface.svg)
![OpenAI](assets/badges/openai.svg)
![MCP](assets/badges/mcp.svg)
![RAG](assets/badges/rag-vectordb.svg)
![scikit-learn](assets/badges/scikit-learn.svg)
![XGBoost](assets/badges/xgboost.svg)
![CatBoost](assets/badges/catboost.svg)
![pandas](assets/badges/pandas.svg)
![NumPy](assets/badges/numpy.svg)
![Hadoop](assets/badges/hadoop.svg)

### Backend / Frontend

![FastAPI](assets/badges/fastapi.svg)
![Hono](assets/badges/hono.svg)
![Flask](assets/badges/flask.svg)
![Spring Boot](assets/badges/spring-boot.svg)
![.NET](assets/badges/dotnet.svg)
![SQLAlchemy](assets/badges/sqlalchemy.svg)
![React](assets/badges/react.svg)
![Vue](assets/badges/vue.svg)
![Phaser](assets/badges/phaser.svg)
![HTML5](assets/badges/html5.svg)
![CSS](assets/badges/css.svg)

### Infra / Data

![AWS](assets/badges/aws.svg)
![Cloudflare](assets/badges/cloudflare.svg)
![GCP](assets/badges/gcp.svg)
![Docker](assets/badges/docker.svg)
![PostgreSQL](assets/badges/postgresql.svg)
![MySQL](assets/badges/mysql.svg)
![MongoDB](assets/badges/mongodb.svg)
![Redis](assets/badges/redis.svg)
![Neo4j](assets/badges/neo4j.svg)
![Linux](assets/badges/linux.svg)
![GitHub Actions](assets/badges/github-actions.svg)


### Tools

![VS Code](assets/badges/vs-code.svg)
![Cursor](assets/badges/cursor.svg)
![JetBrains](assets/badges/jetbrains.svg)
![PyCharm](assets/badges/pycharm.svg)
![Windsurf](assets/badges/windsurf.svg)
![Antigravity](assets/badges/antigravity.svg)

![Claude Code](assets/badges/claude-code.svg)
![Codex](assets/badges/codex.svg)
![OpenCode](assets/badges/opencode.svg)
![Gemini](assets/badges/gemini.svg)

![Git](assets/badges/git.svg)
![Postman](assets/badges/postman.svg)
![Obsidian](assets/badges/obsidian.svg)

</div>

<br>

---

## Certifications & Education

<br>

<table align="center" width="100%">
<tr>
<th width="420">Data &amp; AI</th>
<th width="340">Dev &amp; Infra</th>
<th width="240">Language</th>
</tr>
<tr>
<td valign="top">

- 빅데이터분석기사
- 데이터아키텍처준전문가 (DAsP)
- SQL 개발자 (SQLD)
- 데이터분석준전문가 (ADsP)
- AICE Associate
- AI-POT 1급

</td>
<td valign="top">

- 정보처리기사
- 프로그래밍기능사
- 리눅스마스터 2급
- 네트워크관리사 2급
- 컴퓨터활용능력 1급

</td>
<td valign="top">

- HSK 5급

</td>
</tr>
</table>

<table align="center" width="100%">
<tr>
<th width="240">Period</th>
<th width="760">Program</th>
</tr>
<tr>
<td nowrap valign="top">2026.05 ~ 2026.08</td>
<td>

이어드림스쿨 6기 심화과정<br>중소벤처기업부 AI 기술인력 양성

- LLM Fine-tuning RAG와 Vector DB
- LangChain과 LangGraph AI Agent와 MCP
- 산업 연계 팀 프로젝트

</td>
</tr>
<tr>
<td nowrap valign="top">2023.09 ~ 2026.02</td>
<td>

건국대학교 정보통신대학원 융합정보기술학과 인공지능전공 석사<br>
[이수 과목 및 성적](assets/education/konkuk-masters-transcript-redacted.png)

</td>
</tr>
<tr>
<td nowrap valign="top">2022.10 ~ 2023.04</td>
<td>

[코드스테이츠 AI Bootcamp 16기](https://www.codestates.com/blog/content/ai-%EB%B6%80%ED%8A%B8%EC%BA%A0%ED%94%84-%EC%8B%9C%EA%B0%84%ED%91%9C) 인공지능모델링<br>6개월 학습 + 1개월 기업 협업

- Python·pandas 데이터 전처리 EDA 시각화와 통계
- 머신러닝 모델링·평가와 딥러닝 기반 컴퓨터 비전·자연어 처리
- SQL 데이터베이스와 Flask·Docker 기반 애플리케이션 개발·배포
- 실무 프로젝트와 기업 협업

</td>
</tr>
<tr>
<td nowrap valign="top">2014.09 ~ 2020.06</td>
<td>

동북전력대학교 (China) 소프트웨어공학과 학사<br>4년 과정 재학 중 군복무 1년 9개월

</td>
</tr>
</table>

<br>

---

## Algorithms

<br>

<div align="center">

<img src="assets/BOJ memory - taeyang95.png" width="760" alt="BOJ memory taeyang95" />

*Thanks BOJ<br>Good bye BOJ*

</div>

---

## etc

<br>

<div align="center">

<img src="assets/etc/1st.png" width="760" alt="Taeyang 1st place leaderboard" />

<img src="assets/etc/obwc-2025-result-with-standings.png" width="760" alt="osu! Beatmapping World Championship 2025 results and team standings" />

</div>

<br>

---

<div align="center">

### 신규 프로젝트 문의는 [fornaxworks.com](https://fornaxworks.com) 에서 받고 있습니다

</div>
