<div align="center">

<img src="assets/banner.gif" width="100%" alt="fornaxworks アイデアを出荷できるプロダクトへ鍛える" />

### AI とフルスタック開発。企画から本番リリースまで、一人が通しで担当します。

**[https://fornaxworks.com](https://fornaxworks.com)**

[한국어](README.md) | [English](README.en.md) | [中文](README.zh.md) | **日本語**

<a href="https://fornaxworks.com"><img src="https://img.shields.io/badge/fornaxworks.com-FF6B35?style=for-the-badge&logo=googlechrome&logoColor=white" alt="fornaxworks" /></a>
<a href="https://owogg.com"><img src="https://img.shields.io/badge/owogg.com-A855F7?style=for-the-badge&logo=gamejolt&logoColor=white" alt="owogg" /></a>
<a href="https://blog.naver.com/taeyang95"><img src="https://img.shields.io/badge/Blog-03C75A?style=for-the-badge&logo=naver&logoColor=white" alt="Blog" /></a>

</div>

<br>

---

## About

<br>

建国大学 情報通信大学院 人工知能専攻 修士。その前は中国でソフトウェア工学を4年間学び、卒業論文を中国語で書きました。
修士論文では RAG のコスト問題を、学士論文では電力データの規模の問題を扱いました。

現在は [fornaxworks](https://fornaxworks.com) という名前で Web・モバイル・AI プロダクトを作っています。
2023年から留学コンサルティング事業を代表として運営しており、顧客対応や契約、事務手続きはすでに日常業務です。
韓国語のほか、英語・中国語・日本語でやり取りできます。

<br>

---

## Projects

<br>

| Project | Description | Stack |
|---|---|---|
| **[project-owogg](https://github.com/TaeyanG4/project-owogg)**<br>[owogg.com](https://owogg.com) | ブラウザ向けミニゲームプラットフォーム。自社ゲームとユーザー投稿ゲームを同一のランタイムで動かします。Ports/Adapters でドメインを分離し、e2e テストと staging 環境を運用しています。 | `React 19` `Hono` `Cloudflare Workers` `D1` `B2` |
| **[dexon-smart-ops-chatbot](https://github.com/TaeyanG4/dexon-smart-ops-chatbot)** | HDD の SMART データから7日以内に故障するディスクを予測し、点検順序・根拠文書・運用 Runbook をあわせて出します。公開前に追跡ファイル252件を全数検査し、個人情報を除去しました。 | `FastAPI` `LlamaIndex` `LiteLLM` `Langfuse` `Docker` |
| **[story_maker_with_photos](https://github.com/TaeyanG4/story_maker_with_photos)** | 写真1枚を童話に変えるインタラクティブなストーリープラットフォーム。大学院の課題として、システム設計・UX・ビジネス戦略まで32ページの文書にまとめました。 | `GPT-4o` `DALL·E 3` `Gradio` |
| **[project-forge](https://github.com/TaeyanG4/project-forge)**<br>[fornaxworks.com](https://fornaxworks.com) | スタジオのサイトそのもの。フレームワークを使わず Python スクリプトで HTML を生成し、Cloudflare Worker に載せています。ロゴと OG 画像もコードで描いています。 | `Python` `Cloudflare Workers` |
| **[kapt_predict](https://github.com/TaeyanG4/kapt_predict)** （公開予定） | 集合住宅の工事費予測モデル。自作クローラー [kapt_crawler](https://github.com/TaeyanG4/kapt_crawler) で収集した K-APT の公開データを使っています。 | `CatBoost` `pandas` |

<br>

---

## Showroom

<br>

fornaxworks のショールームに置いているデモです。実際の納品物ではなく、どこまで作るのかを示すために自分で作った見本です。
画像をクリックするとブラウザでそのまま開きます。

<table align="center">
<tr>
<td width="33.33%" align="center" valign="top">
<a href="https://fornaxworks.com/pallet.html"><img src="assets/gallery/pallet.png" width="100%" alt="PALLET" /></a><br>
<b>PALLET</b> Web サービス<br>
登録・権限・決済まで一式<br>
<code>TypeScript</code> <code>Next.js</code> <code>PostgreSQL</code>
</td>
<td width="33.33%" align="center" valign="top">
<a href="https://fornaxworks.com/shop.html"><img src="assets/gallery/shop.png" width="100%" alt="TAG" /></a><br>
<b>TAG</b> EC<br>
キャンセル・返品・精算を状態として設計<br>
<code>Next.js</code> <code>PostgreSQL</code> <code>Payments</code>
</td>
<td width="33.33%" align="center" valign="top">
<a href="https://fornaxworks.com/mat.html"><img src="assets/gallery/mat.png" width="100%" alt="MAT" /></a><br>
<b>MAT</b> モバイルアプリ<br>
iOS と Android を1つのコードで、<br>ストア審査まで<br>
<code>React Native</code> <code>Expo</code>
</td>
</tr>
<tr>
<td width="33.33%" align="center" valign="top">
<a href="https://fornaxworks.com/guide.html"><img src="assets/gallery/index.png" width="100%" alt="INDEX" /></a><br>
<b>INDEX</b> ドキュメント検索アシスタント<br>
ハイブリッド検索とリランキング、根拠段落の提示<br>
<code>Claude API</code> <code>pgvector</code> <code>FastAPI</code>
</td>
<td width="33.33%" align="center" valign="top">
<a href="https://fornaxworks.com/clerk.html"><img src="assets/gallery/clerk.png" width="100%" alt="CLERK" /></a><br>
<b>CLERK</b> 定型業務エージェント<br>
ツール呼び出しパイプライン、最終承認は人が行う<br>
<code>Claude API</code> <code>Next.js</code>
</td>
<td width="33.33%" align="center" valign="top">
<a href="https://fornaxworks.com/board.html"><img src="assets/gallery/tally.png" width="100%" alt="TALLY" /></a><br>
<b>TALLY</b> データダッシュボード<br>
グラフよりも、毎日自動で最新になるパイプラインが要<br>
<code>React</code> <code>Python</code> <code>Airflow</code>
</td>
</tr>
<tr>
<td width="33.33%" align="center" valign="top">
<a href="https://fornaxworks.com/stamp.html"><img src="assets/gallery/stamp.png" width="100%" alt="STAMP" /></a><br>
<b>STAMP</b> 社内業務システム<br>
ロール別権限と、消せない監査ログ<br>
<code>Remix</code> <code>Prisma</code> <code>MySQL</code>
</td>
<td width="33.33%" align="center" valign="top">
<a href="https://fornaxworks.com/bridge.html"><img src="assets/gallery/bridge.png" width="100%" alt="BRIDGE" /></a><br>
<b>BRIDGE</b> レガシー移行<br>
無停止の段階的移行と、切り戻せるデプロイ<br>
<code>Docker</code> <code>Terraform</code> <code>AWS</code>
</td>
<td width="33.33%" align="center" valign="top">
<a href="https://fornaxworks.com/landing.html"><img src="assets/gallery/beacon.png" width="100%" alt="BEACON" /></a><br>
<b>BEACON</b> ブランド・ランディングサイト<br>
速度と検索性を保ち、自分で直せる状態で引き渡す<br>
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
> Query-Aware Cost-Efficient RAG via a Lightweight Pipeline Controller<br>2026年、建国大学 情報通信大学院
>
> すべてのクエリを同じ高コストのパイプラインに通すと、簡単な質問にもコストとレイテンシがそのままかかります。
> そこでクエリの難易度を先に見積もり、ハイブリッド検索・リランキング・HyDE を必要なときだけ有効にする軽量コントローラーを組み込みました。

### Bachelor's Thesis

> **Parallelization of Data Mining in Power Industry Based on MapReduce**
>
> 基于MapReduce的电力行业数据挖掘并行化实现<br>2020年、東北電力大学 Northeast Electric Power University
>
> スマートメーターが吐き出す使用量データは、単一のマシンでは処理しきれません。
> 仮想マシン上に3ノードの Hadoop クラスタを構築し、MapReduce K-means で使用パターンを分類しました。

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
<th width="38%">Data &amp; AI</th>
<th width="34%">Dev &amp; Infra</th>
<th width="28%">Language</th>
</tr>
<tr>
<td valign="top">

- ビッグデータ分析技士
- データアーキテクチャ準専門家 (DAsP)
- SQL 開発者 (SQLD)
- データ分析準専門家 (ADsP)
- AICE Associate
- AI-POT 1級

</td>
<td valign="top">

- 情報処理技士
- プログラミング技能士
- Linux Master 2級
- ネットワーク管理士 2級
- コンピュータ活用能力 1級

</td>
<td valign="top">

- HSK 5級

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

<b>Yeardream School 第6期</b> 応用コース（韓国中小ベンチャー企業部 AI 技術人材育成）

- LLM ファインチューニング、RAG とベクトル DB
- LangChain と LangGraph、AI エージェントと MCP
- 産業連携チームプロジェクト

</td>
</tr>
<tr>
<td nowrap valign="top">2023.09 ~ 2026.02</td>
<td>

<b>建国大学 情報通信大学院</b> 融合情報技術学科 人工知能専攻 修士

</td>
</tr>
<tr>
<td nowrap valign="top">2022.10 ~ 2023.04</td>
<td>

<b>AI Bootcamp 第16期</b> 人工知能モデリング（6か月の学習 + 1か月の企業協業）

</td>
</tr>
<tr>
<td nowrap valign="top">2014.09 ~ 2020.06</td>
<td>

<b>東北電力大学</b>（中国）ソフトウェア工学 学士（4年課程、在学中に兵役2年）

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

### 新規プロジェクトのご相談は [fornaxworks.com](https://fornaxworks.com) で受け付けています。

</div>
