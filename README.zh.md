<div align="center">

<img src="assets/banner.gif" width="100%" alt="fornaxworks 把想法锻造成可交付的产品" />

### AI 与全栈开发。从策划到部署，由一个人一路负责到底。

[https://fornaxworks.com](https://fornaxworks.com)

[한국어](README.md) | [English](README.en.md) | 中文 | [日本語](README.ja.md)

<a href="https://fornaxworks.com"><img src="assets/badges/fornaxworks-com.svg" alt="fornaxworks" /></a>
<a href="https://owogg.com"><img src="assets/badges/owogg-com.svg" alt="owogg" /></a>
<a href="https://afterformat.com"><img src="assets/badges/afterformat-com.svg" alt="afterformat" /></a>
<a href="https://blog.naver.com/taeyang95"><img src="assets/badges/blog.svg" alt="Blog" /></a>

</div>

<br>

---

## About

<br>
我在建国大学信息通信研究生院获得了人工智能专业硕士学位。此前在中国学习了四年软件工程，本科毕业论文也用中文撰写。<br><br>
硕士论文研究了 RAG（检索增强生成）的成本问题，本科论文则使用 Hadoop 分析电力数据中的用电模式。<br><br>
目前以 <a href="https://fornaxworks.com">Fornax</a> 的名义开发 Web、移动端和 AI 产品。自 2023 年起经营留学咨询业务，从客户咨询到签约都亲自负责，因此也熟悉客户沟通和业务实务。<br><br>
可以使用韩语、英语、中文和日语沟通。<br><br>
<br>

---

## Projects

<br>

| Project | Description | Stack |
|---|---|---|
| afterformat<br>[afterformat.com](https://afterformat.com) | 重装系统后一次性取回常用软件的站点。以韩语、英语、日语收录 110 款软件，并标注个人免费但企业需付费的软件，附上依据与核对日期。每日扫描 winget 清单，新版本以 Pull Request 形式提交，需人工确认后才会发布。 | `Astro` `React` `Tailwind` `Cloudflare Workers` `D1` |
| project-owogg<br>[owogg.com](https://owogg.com) | 浏览器小游戏平台。自研游戏与用户上传游戏运行在同一套运行时上。以 Ports/Adapters 分离领域逻辑，并运行 e2e 测试与 staging 环境。 | `React 19` `Hono` `Cloudflare Workers` `D1` `B2` |
| [dexon-smart-ops-chatbot](https://github.com/TaeyanG4/dexon-smart-ops-chatbot) | 基于 HDD SMART 数据预测七天内可能故障的磁盘，并给出巡检顺序、依据文档与运维 Runbook。公开前对 252 个被跟踪文件做了全量审查，清除了个人信息。 | `FastAPI` `LlamaIndex` `LiteLLM` `Langfuse` `Docker` |
| [solarops-audit](https://github.com/TaeyanG4/solarops-audit) | 运营数据质量审计流水线。校验 1,440 万行公开光伏发电数据，只发布通过校验的结果，运行失败时保留上一版结果，并把月报中的每个数字追溯到原始数据。自动化运行确认了从 Compose、Airflow 到 Kubernetes 的整套环境能在空白机器上复现。 | `Python` `Airflow` `Kubernetes` `PostgreSQL` `MinIO` |
| story_maker_with_photos | 把一张照片变成童话的互动故事平台。作为研究生课程作业，用 32 页文档整理了系统设计、UX 与商业策略。 | `GPT-4o` `DALL·E 3` `Gradio` |
| kapt_predict | 住宅小区工程造价预测模型。使用自研爬虫 [kapt_crawler](https://github.com/TaeyanG4/kapt_crawler) 采集的 K-APT 公开数据。 | `CatBoost` `pandas` |

<br>

---

## Datasets

<br>

在 Kaggle 上公开的数据集。完整列表及质量与采用记录见 [kaggle-dataset-portfolio](https://github.com/TaeyanG4/kaggle-dataset-portfolio)，Kaggle 个人主页为 [taeyangg4](https://www.kaggle.com/taeyangg4)。

| Dataset | Description | Scale | Repo |
|---|---|---|---|
| [Kaggle Top Solutions and Strategies](https://www.kaggle.com/datasets/taeyangg4/kaggle-top-solutions-and-strategies) | 收集已结束的 Kaggle 竞赛的公开解题文章，不限排名，并为每篇解答标注所用技术、原文链接和排名依据。摘要和技术判定反映的是模型对作者主张的解读。 | `70,576 rows` `4 files` | [repo](https://github.com/TaeyanG4/kaggle-top-solutions-and-strategies) |
| [KONEPS Public Procurement Intelligence](https://www.kaggle.com/datasets/taeyangg4/koneps-public-procurement-intelligence) | 用相同的键关联韩国公共采购的招标、投标、中标、合同及相关主体。各阶段含义不同，因此不合并为一体，原样保留键和来源。 | `8 files` `2.77 GB` | [repo](https://github.com/TaeyanG4/koneps-procurement-intelligence) |
| [South Korea Power Grid 5-Minute Data](https://www.kaggle.com/datasets/taeyangg4/south-korea-power-grid-5-minute) | 将韩国电力交易所的需求预测、发电机调度指令量和估算出力整理为 5 分钟间隔的数据。完整历史以 Parquet 格式上传，最近一个月以 CSV 格式上传，两者均可直接打开。 | `1B+ rows` `2.49 GB` | [repo](https://github.com/TaeyanG4/korea-power-grid) |
| [South Korea Customs Trade 2012-2026 HSK10](https://www.kaggle.com/datasets/taeyangg4/south-korea-customs-trade-hsk10) | 将韩国关税厅的进出口实绩按贸易伙伴国 × 月 × 10 位 HSK 商品编码整理，并从 HSK10 派生上级 HS 层级，一并收录。 | `22.35M rows` `1.17 GB` | [repo](https://github.com/TaeyanG4/korea-customs-trade) |
| [Smithsonian 25K Museum Image-Text Dataset](https://www.kaggle.com/datasets/taeyangg4/smithsonian-25k-museum-image-text) | 核对权利后，将史密森尼 Open Access 的图片与说明文字整理在一起，并划分数据，避免同一件藏品同时出现在训练集和评估集中。 | `24,972 images` `916 MB` | [repo](https://github.com/TaeyanG4/smithsonian-image-text) |
| [South Korea Food-Service Permits](https://www.kaggle.com/datasets/taeyangg4/korea-food-service-permits) | 一次性收录全国一般餐饮店、休闲餐饮店和糕点店当前营业许可状态的快照。 | `3.01M rows` `403 MB` | [repo](https://github.com/TaeyanG4/korea-business-lifecycle) |
| [Autonomous Driving Crash Reports (NHTSA)](https://www.kaggle.com/datasets/taeyangg4/nhtsa-autonomous-driving-crashes) | 按现行报告规定整理美国 NHTSA 收到的自动驾驶与 ADAS 事故报告。按报告主体统计的数量不代表事故率或安全排名。 | `3,263 rows` `123 cols` | [repo](https://github.com/TaeyanG4/nhtsa-autonomous-driving-crashes) |

<br>

---

## Showroom

<br>

这些是放在 fornaxworks 样品间的演示。并非实际交付物，而是为了展示能做到什么程度而自行制作的样品。<br>
点击图片即可在浏览器中打开。

<table align="center">
<tr>
<td width="33.33%" align="center" valign="top">
<a href="https://fornaxworks.com/pallet.html"><img src="assets/gallery/pallet.png" width="100%" alt="PALLET" /></a><br>
PALLET Web 服务<br>
注册、权限、支付一整套<br>
<code>TypeScript</code> <code>Next.js</code> <code>PostgreSQL</code>
</td>
<td width="33.33%" align="center" valign="top">
<a href="https://fornaxworks.com/shop.html"><img src="assets/gallery/shop.png" width="100%" alt="TAG" /></a><br>
TAG 电商<br>
把取消、退货、结算设计成状态流转<br>
<code>Next.js</code> <code>PostgreSQL</code> <code>Payments</code>
</td>
<td width="33.33%" align="center" valign="top">
<a href="https://fornaxworks.com/mat.html"><img src="assets/gallery/mat.png" width="100%" alt="MAT" /></a><br>
MAT 移动应用<br>
一套代码覆盖 iOS 与 Android，<br>含应用商店审核<br>
<code>React Native</code> <code>Expo</code>
</td>
</tr>
<tr>
<td width="33.33%" align="center" valign="top">
<a href="https://fornaxworks.com/guide.html"><img src="assets/gallery/index.png" width="100%" alt="INDEX" /></a><br>
INDEX 文档检索助手<br>
混合检索与重排序，标注依据段落<br>
<code>Claude API</code> <code>pgvector</code> <code>FastAPI</code>
</td>
<td width="33.33%" align="center" valign="top">
<a href="https://fornaxworks.com/clerk.html"><img src="assets/gallery/clerk.png" width="100%" alt="CLERK" /></a><br>
CLERK 重复性业务智能体<br>
工具调用流水线，最终审批仍由人来做<br>
<code>Claude API</code> <code>Next.js</code>
</td>
<td width="33.33%" align="center" valign="top">
<a href="https://fornaxworks.com/board.html"><img src="assets/gallery/tally.png" width="100%" alt="TALLY" /></a><br>
TALLY 数据看板<br>
比图表更重要的是每天自动保持最新的数据管道<br>
<code>React</code> <code>Python</code> <code>Airflow</code>
</td>
</tr>
<tr>
<td width="33.33%" align="center" valign="top">
<a href="https://fornaxworks.com/stamp.html"><img src="assets/gallery/stamp.png" width="100%" alt="STAMP" /></a><br>
STAMP 企业内部业务系统<br>
按角色划分权限与不可删除的审计日志<br>
<code>Remix</code> <code>Prisma</code> <code>MySQL</code>
</td>
<td width="33.33%" align="center" valign="top">
<a href="https://fornaxworks.com/bridge.html"><img src="assets/gallery/bridge.png" width="100%" alt="BRIDGE" /></a><br>
BRIDGE 遗留系统迁移<br>
不停机分阶段迁移，可回滚的发布<br>
<code>Docker</code> <code>Terraform</code> <code>AWS</code>
</td>
<td width="33.33%" align="center" valign="top">
<a href="https://fornaxworks.com/landing.html"><img src="assets/gallery/beacon.png" width="100%" alt="BEACON" /></a><br>
BEACON 品牌与落地页<br>
兼顾性能与检索，并交付为可自行修改的状态<br>
<code>Next.js</code> <code>Vercel</code>
</td>
</tr>
<tr>
<td width="33.33%" align="center" valign="top">
<a href="https://fornaxworks.com/drive.html"><img src="assets/gallery/vital.png" width="100%" alt="VITAL" /></a><br>
VITAL 设备预防性巡检<br>
今天先查哪些设备，并附上依据<br>
<code>FastAPI</code> <code>XGBoost</code> <code>pgvector</code>
</td>
<td width="33.33%" align="center" valign="top">
<a href="https://fornaxworks.com/crawl.html"><img src="assets/gallery/sift.png" width="100%" alt="SIFT" /></a><br>
SIFT 公共数据采集器<br>
先决定哪些不抓取的采集器<br>
<code>Python</code> <code>pandas</code> <code>PyQt5</code>
</td>
<td width="33.33%" align="center" valign="top">
<a href="https://fornaxworks.com/solar.html"><img src="assets/gallery/solarops.png" width="100%" alt="SOLAROPS" /></a><br>
SOLAROPS 运营数据质量审计<br>
只发布已校验的结果，数字可追溯到原始数据<br>
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
> Query-Aware Cost-Efficient RAG via a Lightweight Pipeline Controller<br>2026，建国大学信息通信研究生院
>
> 如果所有查询都走同一条高成本流水线，简单问题也要付出同样的成本与延迟。
> 因此加入了一个轻量控制器：先估计查询难度，只在需要时才启用混合检索、重排序与 HyDE。

### Bachelor's Thesis

> 基于MapReduce的电力行业数据挖掘并行化实现
>
> Parallelization of Data Mining in Power Industry Based on MapReduce<br>2020 동북전력대학교 Northeast Electric Power University
>
> 智能电表产生的用电数据量，单机已经无法处理。
> 在虚拟机上搭建三节点 Hadoop 集群，用 MapReduce K-means 对用电模式进行了聚类划分。

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

- 大数据分析工程师
- 数据架构准专家 (DAsP)
- SQL 开发者 (SQLD)
- 数据分析准专家 (ADsP)
- AICE Associate
- AI-POT 一级

</td>
<td valign="top">

- 信息处理工程师
- 编程技能士
- Linux Master 二级
- 网络管理师 二级
- 计算机应用能力 一级

</td>
<td valign="top">

- HSK 五级

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

Yeardream School 第6期 进阶课程<br>韩国中小风险企业部 AI 技术人才培养

- LLM 微调、RAG 与向量数据库
- LangChain 与 LangGraph、AI Agent 与 MCP
- 产业联动团队项目

</td>
</tr>
<tr>
<td nowrap valign="top">2023.09 ~ 2026.02</td>
<td>

建国大学信息通信研究生院 融合信息技术学科 人工智能专业 硕士

</td>
</tr>
<tr>
<td nowrap valign="top">2022.10 ~ 2023.04</td>
<td>

AI Bootcamp 第16期 人工智能建模<br>6个月学习 + 1个月企业协作

</td>
</tr>
<tr>
<td nowrap valign="top">2014.09 ~ 2020.06</td>
<td>

东北电力大学（中国）软件工程 本科<br>四年制，在学期间服兵役1年9个月

</td>
</tr>
</table>

<br>

---

## Algorithms

<br>

<div align="center">

<img src="assets/BOJ memory - taeyang95.png" width="680" alt="BOJ memory taeyang95" />

*Thanks BOJ<br>Good bye BOJ*

</div>

---

## etc

<br>

<div align="center">

<img src="assets/etc/1st.png" width="680" alt="Taeyang 1st place leaderboard" />

<img src="assets/etc/obwc-2025-result.png" width="680" alt="osu! Beatmapping World Championship 2025 results" />

</div>

<br>

---

<div align="center">

### 新项目咨询请访问 [fornaxworks.com](https://fornaxworks.com)。

</div>
