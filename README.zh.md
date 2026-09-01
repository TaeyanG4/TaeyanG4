<div align="center">

<img src="assets/banner.gif" width="100%" alt="fornaxworks 把想法锻造成可交付的产品" />

### AI 与全栈开发。从策划到部署，由一个人一路负责到底。

**[https://fornaxworks.com](https://fornaxworks.com)**

[한국어](README.md) | [English](README.en.md) | **中文** | [日本語](README.ja.md)

<a href="https://fornaxworks.com"><img src="https://img.shields.io/badge/fornaxworks.com-FF6B35?style=for-the-badge&logo=googlechrome&logoColor=white" alt="fornaxworks" /></a>
<a href="https://owogg.com"><img src="https://img.shields.io/badge/owogg.com-A855F7?style=for-the-badge&logo=gamejolt&logoColor=white" alt="owogg" /></a>
<a href="https://blog.naver.com/taeyang95"><img src="https://img.shields.io/badge/Blog-03C75A?style=for-the-badge&logo=naver&logoColor=white" alt="Blog" /></a>

</div>

<br>

---

## About

<br>

建国大学信息通信研究生院人工智能专业硕士。此前在中国攻读软件工程本科四年，毕业论文以中文撰写。
硕士论文处理 RAG 的成本问题，本科论文处理电力数据的规模问题。

目前以 [fornaxworks](https://fornaxworks.com) 的名义承接 Web、移动端与 AI 产品开发。
自 2023 年起以负责人身份经营留学咨询公司，客户沟通、合同与行政事务是本来就在做的工作。
除韩语外，可使用英语、中文、日语沟通。

<br>

---

## Projects

<br>

| Project | Description | Stack |
|---|---|---|
| **[project-owogg](https://github.com/TaeyanG4/project-owogg)**<br>[owogg.com](https://owogg.com) | 浏览器小游戏平台。自研游戏与用户上传游戏运行在同一套运行时上。以 Ports/Adapters 分离领域逻辑，并运行 e2e 测试与 staging 环境。 | `React 19` `Hono` `Cloudflare Workers` `D1` `B2` |
| **[dexon-smart-ops-chatbot](https://github.com/TaeyanG4/dexon-smart-ops-chatbot)** | 基于 HDD SMART 数据预测七天内可能故障的磁盘，并给出巡检顺序、依据文档与运维 Runbook。公开前对 252 个被跟踪文件做了全量审查，清除了个人信息。 | `FastAPI` `LlamaIndex` `LiteLLM` `Langfuse` `Docker` |
| **[story_maker_with_photos](https://github.com/TaeyanG4/story_maker_with_photos)** | 把一张照片变成童话的互动故事平台。作为研究生课程作业，用 32 页文档整理了系统设计、UX 与商业策略。 | `GPT-4o` `DALL·E 3` `Gradio` |
| **[project-forge](https://github.com/TaeyanG4/project-forge)**<br>[fornaxworks.com](https://fornaxworks.com) | 工作室官网本身。不用框架，由 Python 脚本生成 HTML 并部署到 Cloudflare Worker。Logo 与 OG 图像也由代码绘制。 | `Python` `Cloudflare Workers` |
| **[kapt_predict](https://github.com/TaeyanG4/kapt_predict)** （即将公开） | 住宅小区工程造价预测模型。使用自研爬虫 [kapt_crawler](https://github.com/TaeyanG4/kapt_crawler) 采集的 K-APT 公开数据。 | `CatBoost` `pandas` |

<br>

---

## Showroom

<br>

这些是放在 fornaxworks 样品间的演示。并非实际交付物，而是为了展示能做到什么程度而自行制作的样品。
点击图片即可在浏览器中打开。

<table align="center">
<tr>
<td width="33.33%" align="center" valign="top">
<a href="https://fornaxworks.com/pallet.html"><img src="assets/gallery/pallet.png" width="100%" alt="PALLET" /></a><br>
<b>PALLET</b> Web 服务<br>
注册、权限、支付一整套<br>
<code>TypeScript</code> <code>Next.js</code> <code>PostgreSQL</code>
</td>
<td width="33.33%" align="center" valign="top">
<a href="https://fornaxworks.com/shop.html"><img src="assets/gallery/shop.png" width="100%" alt="TAG" /></a><br>
<b>TAG</b> 电商<br>
把取消、退货、结算设计成状态流转<br>
<code>Next.js</code> <code>PostgreSQL</code> <code>Payments</code>
</td>
<td width="33.33%" align="center" valign="top">
<a href="https://fornaxworks.com/mat.html"><img src="assets/gallery/mat.png" width="100%" alt="MAT" /></a><br>
<b>MAT</b> 移动应用<br>
一套代码覆盖 iOS 与 Android，<br>含应用商店审核<br>
<code>React Native</code> <code>Expo</code>
</td>
</tr>
<tr>
<td width="33.33%" align="center" valign="top">
<a href="https://fornaxworks.com/guide.html"><img src="assets/gallery/index.png" width="100%" alt="INDEX" /></a><br>
<b>INDEX</b> 文档检索助手<br>
混合检索与重排序，标注依据段落<br>
<code>Claude API</code> <code>pgvector</code> <code>FastAPI</code>
</td>
<td width="33.33%" align="center" valign="top">
<a href="https://fornaxworks.com/clerk.html"><img src="assets/gallery/clerk.png" width="100%" alt="CLERK" /></a><br>
<b>CLERK</b> 重复性业务智能体<br>
工具调用流水线，最终审批仍由人来做<br>
<code>Claude API</code> <code>Next.js</code>
</td>
<td width="33.33%" align="center" valign="top">
<a href="https://fornaxworks.com/board.html"><img src="assets/gallery/tally.png" width="100%" alt="TALLY" /></a><br>
<b>TALLY</b> 数据看板<br>
比图表更重要的是每天自动保持最新的数据管道<br>
<code>React</code> <code>Python</code> <code>Airflow</code>
</td>
</tr>
<tr>
<td width="33.33%" align="center" valign="top">
<a href="https://fornaxworks.com/stamp.html"><img src="assets/gallery/stamp.png" width="100%" alt="STAMP" /></a><br>
<b>STAMP</b> 企业内部业务系统<br>
按角色划分权限与不可删除的审计日志<br>
<code>Remix</code> <code>Prisma</code> <code>MySQL</code>
</td>
<td width="33.33%" align="center" valign="top">
<a href="https://fornaxworks.com/bridge.html"><img src="assets/gallery/bridge.png" width="100%" alt="BRIDGE" /></a><br>
<b>BRIDGE</b> 遗留系统迁移<br>
不停机分阶段迁移，可回滚的发布<br>
<code>Docker</code> <code>Terraform</code> <code>AWS</code>
</td>
<td width="33.33%" align="center" valign="top">
<a href="https://fornaxworks.com/landing.html"><img src="assets/gallery/beacon.png" width="100%" alt="BEACON" /></a><br>
<b>BEACON</b> 品牌与落地页<br>
兼顾性能与检索，并交付为可自行修改的状态<br>
<code>Next.js</code> <code>Vercel</code>
</td>
</tr>
</table>

<br>

---

## Research

<br>

### Master's Thesis

> **[경량 파이프라인 컨트롤러를 통한 질의 인식 기반 비용 효율적 RAG](https://www.riss.kr/link?id=T17380351)**
>
> Query-Aware Cost-Efficient RAG via a Lightweight Pipeline Controller<br>2026，建国大学信息通信研究生院
>
> 如果所有查询都走同一条高成本流水线，简单问题也要付出同样的成本与延迟。
> 因此加入了一个轻量控制器：先估计查询难度，只在需要时才启用混合检索、重排序与 HyDE。

### Bachelor's Thesis

> **Parallelization of Data Mining in Power Industry Based on MapReduce**
>
> 基于MapReduce的电力行业数据挖掘并行化实现<br>2020，东北电力大学
>
> 智能电表产生的用电数据量，单机已经无法处理。
> 在虚拟机上搭建三节点 Hadoop 集群，用 MapReduce K-means 对用电模式进行了聚类划分。

<br>

---

## Tech Stack

<br>

<div align="center">

### Language

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=typescript&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![Java](https://img.shields.io/badge/Java-007396?style=for-the-badge&logo=openjdk&logoColor=white)
![C#](https://img.shields.io/badge/C%23-239120?style=for-the-badge)
![C++](https://img.shields.io/badge/C++-00599C?style=for-the-badge&logo=cplusplus&logoColor=white)
![Kotlin](https://img.shields.io/badge/Kotlin-7F52FF?style=for-the-badge&logo=kotlin&logoColor=white)
![Go](https://img.shields.io/badge/Go-00ADD8?style=for-the-badge&logo=go&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-CC2927?style=for-the-badge)
![R](https://img.shields.io/badge/R-276DC3?style=for-the-badge&logo=r&logoColor=white)

### AI / ML

![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white)
![LlamaIndex](https://img.shields.io/badge/LlamaIndex-3B0764?style=for-the-badge)
![Hugging Face](https://img.shields.io/badge/HuggingFace-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black)
![OpenAI](https://img.shields.io/badge/OpenAI-412991?style=for-the-badge)
![MCP](https://img.shields.io/badge/MCP-D97757?style=for-the-badge&logo=anthropic&logoColor=white)
![RAG](https://img.shields.io/badge/RAG%20%2F%20VectorDB-4B5563?style=for-the-badge)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white)
![XGBoost](https://img.shields.io/badge/XGBoost-337AB7?style=for-the-badge)
![CatBoost](https://img.shields.io/badge/CatBoost-FFCC00?style=for-the-badge&logoColor=black)
![pandas](https://img.shields.io/badge/pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Hadoop](https://img.shields.io/badge/Hadoop-66CCFF?style=for-the-badge&logo=apachehadoop&logoColor=black)

### Backend / Frontend

![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Hono](https://img.shields.io/badge/Hono-E36002?style=for-the-badge&logo=hono&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![Spring Boot](https://img.shields.io/badge/Spring%20Boot-6DB33F?style=for-the-badge&logo=springboot&logoColor=white)
![.NET](https://img.shields.io/badge/.NET-512BD4?style=for-the-badge&logo=dotnet&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-D71F00?style=for-the-badge&logo=sqlalchemy&logoColor=white)
![React](https://img.shields.io/badge/React-61DAFB?style=for-the-badge&logo=react&logoColor=black)
![Vue](https://img.shields.io/badge/Vue-4FC08D?style=for-the-badge&logo=vuedotjs&logoColor=white)
![Phaser](https://img.shields.io/badge/Phaser-8B5CF6?style=for-the-badge)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS](https://img.shields.io/badge/CSS-1572B6?style=for-the-badge&logo=css&logoColor=white)

### Infra / Data

![AWS](https://img.shields.io/badge/AWS-FF9900?style=for-the-badge)
![Cloudflare](https://img.shields.io/badge/Cloudflare-F38020?style=for-the-badge&logo=cloudflare&logoColor=white)
![GCP](https://img.shields.io/badge/GCP-4285F4?style=for-the-badge&logo=googlecloud&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
![MongoDB](https://img.shields.io/badge/MongoDB-47A248?style=for-the-badge&logo=mongodb&logoColor=white)
![Redis](https://img.shields.io/badge/Redis-FF4438?style=for-the-badge&logo=redis&logoColor=white)
![Neo4j](https://img.shields.io/badge/Neo4j-4581C3?style=for-the-badge&logo=neo4j&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)
![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-2088FF?style=for-the-badge&logo=githubactions&logoColor=white)

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

- 大数据分析工程师
- 数据架构准专家 (DAsP)
- SQL 开发者 (SQLD)
- 数据分析准专家 (ADsP)
- AICE Associate
- AI-POT 一级

</td>
<td valign="top" nowrap>

- 信息处理工程师
- 编程技能士
- Linux Master 二级
- 网络管理师 二级
- 计算机应用能力 一级

</td>
<td valign="top" nowrap>

- HSK 五级

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

<b>Yeardream School 第6期</b> 进阶课程<br>韩国中小风险企业部 AI 技术人才培养

- LLM 微调、RAG 与向量数据库
- LangChain 与 LangGraph、AI Agent 与 MCP
- 产业联动团队项目

</td>
</tr>
<tr>
<td nowrap valign="top">2023.09 ~ 2026.02</td>
<td>

<b>建国大学信息通信研究生院</b> 融合信息技术学科 人工智能专业 硕士

</td>
</tr>
<tr>
<td nowrap valign="top">2022.10 ~ 2023.04</td>
<td>

<b>AI Bootcamp 第16期</b> 人工智能建模<br>6个月学习 + 1个月企业协作

</td>
</tr>
<tr>
<td nowrap valign="top">2014.09 ~ 2020.06</td>
<td>

<b>东北电力大学</b>（中国）软件工程 本科<br>四年制，在学期间服兵役1年9个月

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

### 新项目咨询请访问 [fornaxworks.com](https://fornaxworks.com)。

</div>
