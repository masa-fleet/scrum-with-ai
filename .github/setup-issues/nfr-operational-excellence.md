---
title: "[PBI] オペレーショナルエクセレンス NFR を整理する"
labels:
  - pbi
  - setup
---

## 🎯 Goal

プロジェクトの運用要件（ロギング・監視・デプロイ・インシデント管理）を整理し、`docs/nfr/operational-excellence.md` に保存する。

## 📖 Background & Context

運用要件を設計段階で定義することで、オブザーバビリティ基盤やデプロイパイプラインの構成が早期に固まる。
AI がここに保存された要件を参照して CI/CD 設計や IaC に活用できる。

## ✅ Acceptance Criteria

- [ ] [OE:07](https://learn.microsoft.com/ja-jp/azure/well-architected/operational-excellence/observability) ログ収集方針（対象レベル・構造化ログ形式・保持期間）が定義されている
- [ ] [OE:07](https://learn.microsoft.com/ja-jp/azure/well-architected/operational-excellence/observability) メトリクス収集対象（例: CPU・メモリ・リクエスト数・エラー率）が定義されている
- [ ] [OE:07](https://learn.microsoft.com/ja-jp/azure/well-architected/operational-excellence/instrument-application) 分散トレーシング採用有無と使用ツール（例: OpenTelemetry）が決定されている
- [ ] [OE:07](https://learn.microsoft.com/ja-jp/azure/well-architected/operational-excellence/observability) / [OE:08](https://learn.microsoft.com/ja-jp/azure/well-architected/operational-excellence/incident-response) アラート条件と通知チャンネル（例: エラー率 > 1% → Teams / PagerDuty）が定義されている
- [ ] [OE:11](https://learn.microsoft.com/ja-jp/azure/well-architected/operational-excellence/safe-deployments) デプロイ戦略（例: Blue/Green、カナリア、ローリングアップデート）が決定されている
- [ ] [OE:03](https://learn.microsoft.com/ja-jp/azure/well-architected/operational-excellence/formalize-development-practices) / [OE:11](https://learn.microsoft.com/ja-jp/azure/well-architected/operational-excellence/safe-deployments) デプロイ頻度の目標（例: 1 スプリントに 1 回本番リリース）が定義されている
- [ ] [OE:08](https://learn.microsoft.com/ja-jp/azure/well-architected/operational-excellence/incident-response) オンコール体制とエスカレーションフローが定義されている
- [ ] 整理された内容が `docs/nfr/operational-excellence.md` に保存されている

## 📝 参考

- [Azure Well-Architected Framework — オペレーショナルエクセレンス](https://learn.microsoft.com/ja-jp/azure/well-architected/operational-excellence/)
- [オペレーショナルエクセレンス設計レビューチェックリスト](https://learn.microsoft.com/ja-jp/azure/well-architected/operational-excellence/checklist)

まずはこの Issue のコメント欄に決定事項や未決事項を書き込んでください。最終的に Copilot がコメントをもとに `docs/nfr/operational-excellence.md` を作成します。
