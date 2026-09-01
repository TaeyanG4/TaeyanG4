# Taeyang

<img src="assets/banner.png" width="100%" alt="fornaxworks — 아이디어를 출하 가능한 제품으로 벼립니다" />

**AI · 풀스택 개발자.** 주력은 AI와 풀스택이지만, 인프라·크롤링·데이터 파이프라인까지 필요한 만큼 혼자 끝냅니다.
*AI-focused full-stack developer — the range doesn't stop there: infra, crawling, data pipelines, whatever the project needs.*

소프트웨어공학 학사, 인공지능 석사. 논문 두 편 모두 "이론이 아니라 직접 돌아가는 걸" 만드는 데 썼습니다 — 학사 땐 Hadoop 클러스터를 직접 세워 전력 데이터를 병렬 처리했고, 석사 땐 비용 때문에 다들 타협하는 RAG 파이프라인을 실제로 가볍게 만들었습니다. 지금은 [fornaxworks](https://fornaxworks.com)에서 기획부터 배포까지 혼자 끝내는 외주 스튜디오를 막 시작했습니다.

개발 말고도 사업 운영 경험이 있습니다 — 2023년부터 유학 컨설팅 사업체를 대표로 직접 운영하며 고객 응대·계약·행정을 실무로 다뤄왔고, 그 감각을 그대로 fornaxworks에 옮기는 중입니다.

Bachelor's in Software Engineering, Master's in AI — both theses built working systems, not just theory. Currently opening [fornaxworks](https://fornaxworks.com), a one-person studio taking projects from spec to deployment.

---

## 지금 하고 있는 일 · Currently

- 🔭 [fornaxworks](https://fornaxworks.com) — 웹·모바일·AI 제품 개발 스튜디오 준비 중 (기획→설계→개발→배포→인수인계)
- 🎮 [project-owogg](https://github.com/TaeyanG4/project-owogg) — [owogg.com](https://owogg.com) 실서비스 운영/개발 중인 미니게임 플랫폼

## 대표 프로젝트 · Selected Projects

| | |
|---|---|
| **[project-owogg](https://github.com/TaeyanG4/project-owogg)** | 브라우저 미니게임 플랫폼. React 19 · Hono(Cloudflare Workers) · D1 · B2. Ports/Adapters 구조로 도메인 분리, e2e 테스트, staging 환경까지 갖춘 실서비스. → [owogg.com](https://owogg.com) |
| **[dexon-smart-ops-chatbot](https://github.com/TaeyanG4/dexon-smart-ops-chatbot)** | HDD SMART 데이터로 7일 고장 위험을 예측하는 Python/FastAPI 운영 의사결정 프로토타입. pytest + Docker + GitHub Actions CI/CD, 공개 전 개인정보 감사·비식별화까지 정식으로 거쳐 릴리스. |
| **[story_maker_with_photos](https://github.com/TaeyanG4/story_maker_with_photos)** | 사진 한 장으로 동화를 만드는 인터랙티브 스토리 플랫폼. GPT-4o(이야기 생성)+DALL·E 3(삽화) 연동. 대학원 수업에서 시스템 설계·UX·비즈니스 전략까지 정식 문서화. |
| **[project-forge](https://github.com/TaeyanG4/project-forge)** | 지금 보고 계신 [fornaxworks.com](https://fornaxworks.com) 그 자체. 프레임워크 없이 Python 스크립트(`bake.py`)로 직접 굽는 정적 사이트 + Cloudflare Worker. |
| **[kapt_predict](https://github.com/TaeyanG4/kapt_predict)** *(공개 예정)* | 공동주택 공사비 예측 모델(CatBoost). K-APT 공개 데이터 크롤러([kapt_crawler](https://github.com/TaeyanG4/kapt_crawler))의 후속작. |

## 연구 · Research

- **석사 논문 (2026)** — [경량 파이프라인 컨트롤러를 통한 질의 인식 기반 비용 효율적 RAG](https://www.riss.kr/link?id=T17380351)
  *Query-Aware Cost-Efficient RAG via a Lightweight Pipeline Controller* — 건국대학교 정보통신대학원
  모든 질의에 같은 고비용 RAG 파이프라인을 쓸 때 생기는 비용/지연 비효율을, 질의 난이도를 판단해 하이브리드 검색·재랭킹·HyDE를 동적으로 조절하는 경량 컨트롤러로 해결.
- **학사 논문 (2020)** — Parallelization of Data Mining in Power Industry Based on MapReduce (基于MapReduce的电力行业数据挖掘并行化实现) — 동북전력대학교
  3노드 Hadoop 클러스터를 직접 구축, MapReduce 기반 K-means로 스마트미터 전력 사용 패턴을 병렬 클러스터링.

## 자격증 · Certifications

**데이터·AI**: Big Data Analytics Engineer(빅데이터분석기사) · DAsP(Data Architecture Semi-Professional) · SQLD(SQL Developer) · ADsP(Advanced Data Analytics Semi-Professional) · AI-POT Level 1(AI Prompt Utilization) · AICE Associate
**개발·인프라**: Craftsman Programming(프로그래밍기능사) · Linux Master Level 2(리눅스마스터 2급)
<!-- 정보처리기사·네트워크관리사 2급은 실기 결과 확인 후 추가 (지금은 필기합격만 확인됨) -->

## 교육 · Education

- 건국대학교(Konkuk University) 정보통신대학원 융합정보기술학과 인공지능전공 — 석사 (2026.02)
- 동북전력대학교(Northeast Electric Power University, China) 소프트웨어공학과 — 학사 (2020.06)
- AI Bootcamp 16기 — 인공지능모델링 6개월 학습 + 1개월 기업 협업 프로젝트 (2022.10~2023.04)
- 이어드림스쿨 6기(중소벤처기업부 AI 기술인력 양성, 심화과정) — LLM Fine-tuning, RAG·Vector DB, LangChain/LangGraph, AI Agent·MCP, 산업 연계 팀 프로젝트, 주 1회 현직자 멘토링 (2026)

## 알고리즘 · Problem Solving

<img src="assets/BOJ memory - taeyang95.png" width="480" alt="BOJ memory - taeyang95" />

생성형 AI가 지금처럼 코드를 대신 짜주기 한참 전, 백준(BOJ)에서 문제 1,936개를 손으로 풀며 실력을 다졌습니다 (solved.ac 랭킹 #3,324). 이 이미지를 만들어준 사이트는 지금은 없어졌지만, 그 시절 기록은 남겨둡니다.
*Before AI could write code for you, 1,936 problems solved by hand on Baekjoon Online Judge (solved.ac rank #3,324). The site that generated this card is gone now — this is kept in memory of it.*

## Tech Stack

**주력 — 실제 프로젝트에 쓴 것** (레포별 `pyproject.toml`/`package.json` 기준)

- **Language** — Python, TypeScript/JavaScript, SQL, C/C++, R
- **Backend** — FastAPI, Hono, SQLAlchemy · Alembic, asyncpg/psycopg
- **Frontend** — React 19, React Router, Phaser.js(게임)
- **AI/ML** — LlamaIndex, LangChain/LangGraph, MCP, HuggingFace, LiteLLM, Langfuse, RAGAS, scikit-learn, XGBoost, CatBoost, crawl4ai, Hadoop/MapReduce
- **Infra/Data** — AWS, Cloudflare Workers · D1, Docker, PostgreSQL, Redis, Neo4j, Backblaze B2, GitHub Actions

**그 외 다룰 수 있는 것** — 프로젝트에 아직 안 썼지만 다룰 줄 아는 것들

Java(Spring Boot) · C#(.NET) · Kotlin · Go · Vue · MySQL/MongoDB · GCP

---

📫 [fornaxworks.com](https://fornaxworks.com) 에서 프로젝트 문의를 받고 있습니다.
