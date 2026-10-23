<div align="center">

<img src="assets/banner.gif" width="100%" alt="fornaxworks アイデアを出荷できるプロダクトへ鍛える" />

### AI とフルスタック開発。企画から本番リリースまで、一人が通しで担当します。

**[https://fornaxworks.com](https://fornaxworks.com)**

[한국어](README.md) | [English](README.en.md) | [中文](README.zh.md) | **日本語**

<a href="https://fornaxworks.com"><img src="assets/badges/fornaxworks-com.svg" alt="fornaxworks" /></a>
<a href="https://owogg.com"><img src="assets/badges/owogg-com.svg" alt="owogg" /></a>
<a href="https://afterformat.com"><img src="assets/badges/afterformat-com.svg" alt="afterformat" /></a>
<a href="https://blog.naver.com/taeyang95"><img src="assets/badges/blog.svg" alt="Blog" /></a>

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
| **afterformat**<br>[afterformat.com](https://afterformat.com) | 初期化のあとに入れ直すソフトをまとめて取得できる場所。110本を韓国語・英語・日本語で扱い、個人は無料でも法人は有料というソフトを、根拠と確認日を添えて区別して表示します。winget のマニフェストを毎日走査し、新しいバージョンは人が確認するプルリクエストとして上がります。 | `Astro` `React` `Tailwind` `Cloudflare Workers` `D1` |
| **[project-owogg](https://github.com/TaeyanG4/project-owogg)**<br>[owogg.com](https://owogg.com) | ブラウザ向けミニゲームプラットフォーム。自社ゲームとユーザー投稿ゲームを同一のランタイムで動かします。Ports/Adapters でドメインを分離し、e2e テストと staging 環境を運用しています。 | `React 19` `Hono` `Cloudflare Workers` `D1` `B2` |
| **[dexon-smart-ops-chatbot](https://github.com/TaeyanG4/dexon-smart-ops-chatbot)** | HDD の SMART データから7日以内に故障するディスクを予測し、点検順序・根拠文書・運用 Runbook をあわせて出します。公開前に追跡ファイル252件を全数検査し、個人情報を除去しました。 | `FastAPI` `LlamaIndex` `LiteLLM` `Langfuse` `Docker` |
| **[solarops-audit](https://github.com/TaeyanG4/solarops-audit)** | 運用データの品質監査パイプライン。公開されている太陽光発電データ 1,440 万行を検証し、通過した結果だけを公開します。失敗したときは前回の結果を守り、月次レポートの数字を元データまでたどれます。Compose・Airflow から Kubernetes まで、空のマシンでそのまま再現できることを自動で確認しています。 | `Python` `Airflow` `Kubernetes` `PostgreSQL` `MinIO` |
| **[story_maker_with_photos](https://github.com/TaeyanG4/story_maker_with_photos)** | 写真1枚を童話に変えるインタラクティブなストーリープラットフォーム。大学院の課題として、システム設計・UX・ビジネス戦略まで32ページの文書にまとめました。 | `GPT-4o` `DALL·E 3` `Gradio` |
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
<tr>
<td width="33.33%" align="center" valign="top">
<a href="https://fornaxworks.com/drive.html"><img src="assets/gallery/vital.png" width="100%" alt="VITAL" /></a><br>
<b>VITAL</b> 設備の予防点検<br>
今日まず点検する機器を根拠とともに<br>
<code>FastAPI</code> <code>XGBoost</code> <code>pgvector</code>
</td>
<td width="33.33%" align="center" valign="top">
<a href="https://fornaxworks.com/crawl.html"><img src="assets/gallery/sift.png" width="100%" alt="SIFT" /></a><br>
<b>SIFT</b> 公共データ収集ツール<br>
何を集めないかを先に決める収集ツール<br>
<code>Python</code> <code>pandas</code> <code>PyQt5</code>
</td>
<td width="33.33%" align="center" valign="top">
<a href="https://fornaxworks.com/solar.html"><img src="assets/gallery/solarops.png" width="100%" alt="SOLAROPS" /></a><br>
<b>SOLAROPS</b> 運用データ品質監査<br>
検証済みの結果だけを公開し、数字は元データまで<br>
<code>Python</code> <code>Airflow</code> <code>Kubernetes</code>
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

- ビッグデータ分析技士
- データアーキテクチャ準専門家 (DAsP)
- SQL 開発者 (SQLD)
- データ分析準専門家 (ADsP)
- AICE Associate
- AI-POT 1級

</td>
<td valign="top" nowrap>

- 情報処理技士
- プログラミング技能士
- Linux Master 2級
- ネットワーク管理士 2級
- コンピュータ活用能力 1級

</td>
<td valign="top" nowrap>

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

<b>Yeardream School 第6期</b> 応用コース<br>韓国中小ベンチャー企業部 AI 技術人材育成

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

<b>AI Bootcamp 第16期</b> 人工知能モデリング<br>6か月の学習 + 1か月の企業協業

</td>
</tr>
<tr>
<td nowrap valign="top">2014.09 ~ 2020.06</td>
<td>

<b>東北電力大学</b>（中国）ソフトウェア工学 学士<br>4年課程、在学中に兵役1年9か月

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
