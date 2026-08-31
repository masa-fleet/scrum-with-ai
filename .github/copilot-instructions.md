# Copilot 指示

このリポジトリは、AI 支援による Scrum テンプレートです。すべてのコード、ドキュメント、Issue は Copilot が作成し、人間はレビューと承認のみを行います。

## 基本原則

- リポジトリ内の既存のファイルおよびフォルダー規約に従ってください。

## 非機能要件

NFR ドキュメントは `docs/nfr/` に保存されています。アーキテクチャ設計、コスト見積もり、IaC の作成、セキュリティ・信頼性・パフォーマンスに関するコードレビューでは、必ず参照してください。

- `docs/nfr/security.md` — 認証・認可・暗号化・コンプライアンス要件
- `docs/nfr/performance.md` — レスポンスタイム・スループット・スケーリング要件
- `docs/nfr/cost.md` — コスト予算・タグ付け・FinOps 方針
- `docs/nfr/reliability.md` — 可用性・RTO/RPO・バックアップ・フェイルオーバー要件
- `docs/nfr/operational-excellence.md` — ロギング・監視・デプロイ・オンコール要件

## 出力ガイドライン

- **Markdown ファイル:** 詳細な規則は `markdown.instructions.md` を参照してください。
- **コメント・提案:** 直接的に記述し、変更内容と理由を一文で示してください。
