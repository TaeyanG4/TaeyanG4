<div align="center">

<img src="assets/banner.gif" width="100%" alt="fornaxworks forging ideas into shippable products" />

### AI and full-stack development. One person carrying a product from spec to deployment.

**[https://fornaxworks.com](https://fornaxworks.com)**

[한국어](README.md) | **English** | [中文](README.zh.md) | [日本語](README.ja.md)

<a href="https://fornaxworks.com"><img src="assets/badges/fornaxworks-com.svg" alt="fornaxworks" /></a>
<a href="https://owogg.com"><img src="assets/badges/owogg-com.svg" alt="owogg" /></a>
<a href="https://afterformat.com"><img src="assets/badges/afterformat-com.svg" alt="afterformat" /></a>
<a href="https://blog.naver.com/taeyang95"><img src="assets/badges/blog.svg" alt="Blog" /></a>

</div>

<br>

---

## About

<br>

MSc in Artificial Intelligence, Konkuk University Graduate School of Information and Telecommunications. Before that, four years of Software Engineering in China, where I wrote my undergraduate thesis in Chinese.
My master's thesis took on the cost problem in RAG pipelines, my bachelor's the scale problem in power grid data.

I now build web, mobile, and AI products under the name [fornaxworks](https://fornaxworks.com).
Running a study abroad consulting agency as its owner since 2023 means client work, contracts, and administration are already familiar ground.
I work in Korean, English, Chinese, and Japanese.

<br>

---

## Projects

<br>

| Project | Description | Stack |
|---|---|---|
| **afterformat**<br>[afterformat.com](https://afterformat.com) | Pick the programs you use and get them all back in one go after reformatting. 110 programs in Korean, English and Japanese, each marked with whether it is licensed for business use — with the evidence and the date it was checked. winget manifests are scanned daily and land as pull requests a person has to review. | `Astro` `React` `Tailwind` `Cloudflare Workers` `D1` |
| **[project-owogg](https://github.com/TaeyanG4/project-owogg)**<br>[owogg.com](https://owogg.com) | Browser mini-game platform. First-party and user-uploaded games run on a single runtime. Domain logic sits behind ports and adapters, with e2e tests and a staging environment in operation. | `React 19` `Hono` `Cloudflare Workers` `D1` `B2` |
| **[dexon-smart-ops-chatbot](https://github.com/TaeyanG4/dexon-smart-ops-chatbot)** | Predicts which HDDs will fail within seven days from SMART data, and returns an inspection order, supporting evidence, and an operations runbook. All 252 tracked files were audited and scrubbed of personal data before release. | `FastAPI` `LlamaIndex` `LiteLLM` `Langfuse` `Docker` |
| **[solarops-audit](https://github.com/TaeyanG4/solarops-audit)** | Operational data quality audit pipeline. Validates 14.4 million rows of public solar generation data, publishes only what passes, keeps the previous result when a run fails, and traces every number in the monthly report back to its source. An automated run confirms the whole stack, from Compose and Airflow to Kubernetes, reproduces on an empty machine. | `Python` `Airflow` `Kubernetes` `PostgreSQL` `MinIO` |
| **[story_maker_with_photos](https://github.com/TaeyanG4/story_maker_with_photos)** | Turns a single photo into an interactive illustrated story. Documented as graduate coursework across 32 pages covering system design, UX, and business strategy. | `GPT-4o` `DALL·E 3` `Gradio` |
| **[project-forge](https://github.com/TaeyanG4/project-forge)**<br>[fornaxworks.com](https://fornaxworks.com) | The studio site itself. No framework: a Python script bakes the HTML and ships it to a Cloudflare Worker. The logo and OG image are drawn in code too. | `Python` `Cloudflare Workers` |
| **[kapt_predict](https://github.com/TaeyanG4/kapt_predict)** (coming soon) | Construction cost prediction model for apartment complexes, trained on public K-APT data collected by my own crawler, [kapt_crawler](https://github.com/TaeyanG4/kapt_crawler). | `CatBoost` `pandas` |

<br>

---

## Showroom

<br>

Demos from the fornaxworks showroom. These are not client deliverables. I built them to show how far the work goes.
Click an image to open it in your browser.

<table align="center">
<tr>
<td width="33.33%" align="center" valign="top">
<a href="https://fornaxworks.com/pallet.html"><img src="assets/gallery/pallet.png" width="100%" alt="PALLET" /></a><br>
<b>PALLET</b> Web service<br>
Sign-up, permissions, and billing in one set<br>
<code>TypeScript</code> <code>Next.js</code> <code>PostgreSQL</code>
</td>
<td width="33.33%" align="center" valign="top">
<a href="https://fornaxworks.com/shop.html"><img src="assets/gallery/shop.png" width="100%" alt="TAG" /></a><br>
<b>TAG</b> Commerce<br>
Cancellation, returns, and settlement modelled as state<br>
<code>Next.js</code> <code>PostgreSQL</code> <code>Payments</code>
</td>
<td width="33.33%" align="center" valign="top">
<a href="https://fornaxworks.com/mat.html"><img src="assets/gallery/mat.png" width="100%" alt="MAT" /></a><br>
<b>MAT</b> Mobile app<br>
iOS and Android from one codebase,<br>store review included<br>
<code>React Native</code> <code>Expo</code>
</td>
</tr>
<tr>
<td width="33.33%" align="center" valign="top">
<a href="https://fornaxworks.com/guide.html"><img src="assets/gallery/index.png" width="100%" alt="INDEX" /></a><br>
<b>INDEX</b> Document search assistant<br>
Hybrid retrieval, reranking, cited source passages<br>
<code>Claude API</code> <code>pgvector</code> <code>FastAPI</code>
</td>
<td width="33.33%" align="center" valign="top">
<a href="https://fornaxworks.com/clerk.html"><img src="assets/gallery/clerk.png" width="100%" alt="CLERK" /></a><br>
<b>CLERK</b> Routine work agent<br>
Tool-calling pipeline, final approval stays with a human<br>
<code>Claude API</code> <code>Next.js</code>
</td>
<td width="33.33%" align="center" valign="top">
<a href="https://fornaxworks.com/board.html"><img src="assets/gallery/tally.png" width="100%" alt="TALLY" /></a><br>
<b>TALLY</b> Data dashboard<br>
The pipeline that stays current matters more than the chart<br>
<code>React</code> <code>Python</code> <code>Airflow</code>
</td>
</tr>
<tr>
<td width="33.33%" align="center" valign="top">
<a href="https://fornaxworks.com/stamp.html"><img src="assets/gallery/stamp.png" width="100%" alt="STAMP" /></a><br>
<b>STAMP</b> Internal business system<br>
Role-based permissions and an append-only audit log<br>
<code>Remix</code> <code>Prisma</code> <code>MySQL</code>
</td>
<td width="33.33%" align="center" valign="top">
<a href="https://fornaxworks.com/bridge.html"><img src="assets/gallery/bridge.png" width="100%" alt="BRIDGE" /></a><br>
<b>BRIDGE</b> Legacy migration<br>
Phased cutover with no downtime and a reversible deploy<br>
<code>Docker</code> <code>Terraform</code> <code>AWS</code>
</td>
<td width="33.33%" align="center" valign="top">
<a href="https://fornaxworks.com/landing.html"><img src="assets/gallery/beacon.png" width="100%" alt="BEACON" /></a><br>
<b>BEACON</b> Brand and landing site<br>
Fast, findable, and editable by the people who own it<br>
<code>Next.js</code> <code>Vercel</code>
</td>
</tr>
<tr>
<td width="33.33%" align="center" valign="top">
<a href="https://fornaxworks.com/drive.html"><img src="assets/gallery/vital.png" width="100%" alt="VITAL" /></a><br>
<b>VITAL</b> Predictive equipment maintenance<br>
Which machines to check today, with the evidence<br>
<code>FastAPI</code> <code>XGBoost</code> <code>pgvector</code>
</td>
<td width="33.33%" align="center" valign="top">
<a href="https://fornaxworks.com/crawl.html"><img src="assets/gallery/sift.png" width="100%" alt="SIFT" /></a><br>
<b>SIFT</b> Public data collector<br>
A collector that decides first what not to scrape<br>
<code>Python</code> <code>pandas</code> <code>PyQt5</code>
</td>
<td width="33.33%" align="center" valign="top">
<a href="https://fornaxworks.com/solar.html"><img src="assets/gallery/solarops.png" width="100%" alt="SOLAROPS" /></a><br>
<b>SOLAROPS</b> Operational data quality audit<br>
Publishes only validated results, traces numbers to the source<br>
<code>Python</code> <code>Airflow</code> <code>Kubernetes</code>
</td>
</tr>
</table>

<br>

---

## Research

<br>

### Master's Thesis

> **[Query-Aware Cost-Efficient RAG via a Lightweight Pipeline Controller](https://www.riss.kr/link?id=T17380351)**
>
> 경량 파이프라인 컨트롤러를 통한 질의 인식 기반 비용 효율적 RAG<br>2026, Konkuk University Graduate School of Information and Telecommunications
>
> Running every query through the same expensive pipeline makes easy questions pay full price in cost and latency.
> I added a lightweight controller that estimates query difficulty first, then switches on hybrid retrieval, reranking, and HyDE only when they are needed.

### Bachelor's Thesis

> **Parallelization of Data Mining in Power Industry Based on MapReduce**
>
> 基于MapReduce的电力行业数据挖掘并行化实现<br>2020, Northeast Electric Power University
>
> Smart meters produce more consumption data than a single machine can process.
> I stood up a three-node Hadoop cluster on virtual machines and partitioned usage patterns with MapReduce K-means.

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
<th width="42%">Data &amp; AI</th>
<th width="34%">Dev &amp; Infra</th>
<th width="24%">Language</th>
</tr>
<tr>
<td valign="top" nowrap>

- Engineer Big Data Analysis
- Data Architecture Semi-Professional (DAsP)
- SQL Developer (SQLD)
- Advanced Data Analytics Semi-Professional (ADsP)
- AICE Associate
- AI-POT Level 1

</td>
<td valign="top" nowrap>

- Engineer Information Processing
- Craftsman Programming
- Linux Master Level 2
- Network Administrator Level 2
- Computer Specialist in Spreadsheet and Database Level 1

</td>
<td valign="top" nowrap>

- HSK Level 5

</td>
</tr>
</table>

<table align="center" width="100%">
<tr>
<th width="24%">Period</th>
<th>Program</th>
</tr>
<tr>
<td nowrap valign="top">2026.05 ~ 2026.08</td>
<td>

<b>Yeardream School 6th cohort</b>, advanced track<br>Ministry of SMEs and Startups AI talent programme

- LLM fine-tuning, RAG and vector databases
- LangChain and LangGraph, AI agents and MCP
- Industry-linked team project

</td>
</tr>
<tr>
<td nowrap valign="top">2023.09 ~ 2026.02</td>
<td>

<b>Konkuk University</b> Graduate School of Information and Telecommunications, MSc in Artificial Intelligence

</td>
</tr>
<tr>
<td nowrap valign="top">2022.10 ~ 2023.04</td>
<td>

<b>AI Bootcamp 16th cohort</b>, AI modelling<br>6 months of study + 1 month industry collaboration

</td>
</tr>
<tr>
<td nowrap valign="top">2014.09 ~ 2020.06</td>
<td>

<b>Northeast Electric Power University</b> (China), BSc in Software Engineering<br>4-year programme, with 1 year 9 months of military service during enrolment

</td>
</tr>
</table>

<br>

---

## Algorithms

<br>

<div align="center">

<img src="assets/BOJ memory - taeyang95.png" width="680" alt="BOJ memory taeyang95" />

*Thanks, BOJ. Good bye, BOJ.*

</div>

---

<div align="center">

### New project enquiries are welcome at [fornaxworks.com](https://fornaxworks.com).

</div>
