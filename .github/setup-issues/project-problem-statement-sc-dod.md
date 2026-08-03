---
title: "[PBI] Project の Problem Statement, Success Criteria, Definition of Done を定義する"
labels:
  - pbi
  - setup
---

## 🎯 Goal

プロジェクトレベルの Problem Statement（課題）、Success Criteria（成功基準）、Definition of Done（完了の定義）を定義し、`docs/project` フォルダ配下に保存する。

## 📖 Background & Context

Problem Statement, Success Criteria, Definition of Done を最初に合意しておくことで、「何の課題を解くのか」「成功とは何か」「成功をどう測るか」についてチーム（TPM/PO、Dev、DS）とステークホルダーが共通認識を持てる。
特に AI/DS を含むプロジェクトでは、精度指標や評価方法の合意が遅れるとスプリント終盤で手戻りが発生しやすいため、ADS 直後に TPM、Dev Lead、DS Lead が揃って定義することが重要。

## ✅ Acceptance Criteria

- [ ] Problem Statement, Success Criteria, Definition of Done が定義され、`docs/project` フォルダ配下に markdown ファイルとして保存されている
- [ ] Success Criteria、Definition of Done には Dev（機能・非機能要件）と DS（精度・評価指標・モデル訓練等）両方の観点が含まれている
- [ ] Success Criteria は測定可能な指標（KPI）として定義可能な項目は定義する（Optional）。プロダクト全体の KPI との紐付けが分かるとより望ましい
- [ ] それぞれが担当するドメイン(Dev Lead or DS Lead)とTPMが内容をレビューし、合意が取れている
- [ ] スコープ外（対応しないこと）も明示されている

## 📝 1. Problem Statement を書く

**コツ**

- 「誰が」「どんな課題に困っているか」「なぜ今解く必要があるか」を 1〜3 文で簡潔に書く。
- 解決策（HOW）ではなく、課題（WHAT/WHY）にフォーカスする。
- 定量的な As-Is KPI（例: 応答時間、精度、工数）があれば入れると Success Criteria との対応が取りやすい。

**例**

> ドライバーが Agent を通して車両操作できず、Agent からの発話・車両操作が無いことでプロダクトならではの価値を提供できていない。

## 📝 2. Success Criteria を書く

**コツ（TPM/PO 観点）**

- プロジェクトの Success Criteria は、プロダクト全体の KPI（ビジネス指標）のどの部分をスコープにするかを明確にしてから設定する。
- 1 つの Primary Metric（意思決定に使う指標、例: 検索段階の Recall）と、複数の Supporting Metric（詳細分析用の指標、例: AI 判定段階の F1、レスポンスタイム）に分けると優先順位がぶれない。
- 「対応する」だけでなく「対応しない」ことも合意し、スコープの誤解を防ぐ。

**コツ（Dev 観点）**

- 機能要件（何ができるようになるか）と非機能要件（性能・スケーラビリティ・セキュリティなど）の両方を数値目標として書く。
- 例: レイテンシ（< XXX ms）、稼働率（XX.X%）、同時アクセスユーザー数（XXX 人規模）、セキュリティ要件（例: 個人情報の社外送信禁止、ログへの機密データ出力禁止、アクセス権限の最小化）。

**コツ（DS 観点）**

- プロダクト成熟度（PoC / MVP / Production）に応じて評価方法のレベルが異なることを踏まえる。
  - Offline 評価: 用意した Ground Truth データに基づく静的な精度評価（例: Precision, Recall, F1）。評価パイプラインの構築自体を Success Criteria として定義する
  - Online 評価: アプリ利用を通じて測定可能な評価（例: ユーザーの Accept 率、提案の妥当性スコア）
  - Business Level 評価: ビジネスインパクトに直結する指標（例: 工数削減率、アクティブユーザー数）
- 評価指標は「検索/候補生成の精度」「最終出力の精度」など評価対象のステップごとに分けて定義すると、ボトルネック特定がしやすい。
- リアルユーザーでの評価が難しい場合は、代替の評価方法（手動テスト、有識者レビューなど）と、その旨の制約を明記する。

**例（テーブル形式）**

| 指標区分 | 指標 | 目標値 |
| --- | --- | --- |
| Primary Metric | 検索段階の Recall | 90% 以上 |
| Supporting Metric | AI 判定段階の F1 | 70% 以上 |
| 非機能要件 | レスポンスタイム | 30 秒以内 |
| 非機能要件 | 同時アクセスユーザー数 | 数百〜数千人規模でスケール可能 |

## 📝 3. Definition of Done を書く

**コツ**

- Success Criteria の「測定方法」ではなく、「何が完成すれば Done と言えるか」という成果物・状態のチェックリストにする。
- Dev 成果物（機能、アーキテクチャ、CI/CD など）と DS 成果物（評価パイプライン、メトリクス実装、ドキュメント）を分けて書く。
- 誰が見ても判断できる客観的な基準にする（例: 「良い感じに動く」ではなく「〇〇のテストが全て通過する」）。

**例**

- [ ] ユーザーの要件に基づいて機能が提案・生成できる
- [ ] Production 向けにスケーラブルなアーキテクチャが設計・デプロイされている
- [ ] 評価メトリクスの実装・ドキュメントがリポジトリに追加されている
- [ ] 精度評価・改善のパイプラインが構築されている

## 📝 実施時期の目安

- Sprint 0 で TPM、Dev Lead、DS Lead が集まり、ドラフトを作成する。
- Sprint 1 開始前にステークホルダーとレビュー・合意を完了させる。
- プロジェクト途中でスコープや前提が変わった場合は、都度更新し変更履歴を残す。
