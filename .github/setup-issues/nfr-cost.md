---
title: "[PBI] コスト最適化 NFR を整理する"
labels:
  - pbi
  - setup
---

## 🎯 Goal

プロジェクトのコスト要件・制約を整理し、`docs/nfr/cost.md` に保存する。

## 📖 Background & Context

コスト要件を早期に定義することで、アーキテクチャ選択（サーバーレス vs コンテナ、リザーブドインスタンス vs オンデマンド）のトレードオフ判断が明確になる。
AI がここに保存された要件を参照してコスト試算や IaC 設計に活用できる。

## ✅ Acceptance Criteria

- [ ] [CO:02](https://learn.microsoft.com/ja-jp/azure/well-architected/cost-optimization/cost-model) 月間クラウドコスト予算（例: 月額 $500 以内）が定義されている
- [ ] [CO:03](https://learn.microsoft.com/ja-jp/azure/well-architected/cost-optimization/collect-review-cost-data) / [CO:04](https://learn.microsoft.com/ja-jp/azure/well-architected/cost-optimization/set-spending-guardrails) コスト上限アラートのしきい値（例: 予算の 80% 到達時に通知）が決定されている
- [ ] [CO:03](https://learn.microsoft.com/ja-jp/azure/well-architected/cost-optimization/collect-review-cost-data) リソースタグ付け規則（例: environment / team / cost-center タグ）が定義されている
- [ ] [CO:05](https://learn.microsoft.com/ja-jp/azure/well-architected/cost-optimization/get-best-rates) リザーブドインスタンス / Savings Plans の活用方針が決定されている
- [ ] [CO:08](https://learn.microsoft.com/ja-jp/azure/well-architected/cost-optimization/optimize-environment-costs) 開発・ステージング・本番環境のコスト按分方針が決定されている
- [ ] [CO:01](https://learn.microsoft.com/ja-jp/azure/well-architected/cost-optimization/create-culture-financial-responsibility) / [CO:03](https://learn.microsoft.com/ja-jp/azure/well-architected/cost-optimization/collect-review-cost-data) FinOps レビュー頻度（例: スプリントごとにコストレポートを確認）が決定されている
- [ ] 整理された内容が `docs/nfr/cost.md` に保存されている

## 📝 参考

- [Azure Well-Architected Framework — コスト最適化](https://learn.microsoft.com/ja-jp/azure/well-architected/cost-optimization/)
- [コスト最適化設計レビューチェックリスト](https://learn.microsoft.com/ja-jp/azure/well-architected/cost-optimization/checklist)
- [Azure Cost Management](https://learn.microsoft.com/ja-jp/azure/cost-management-billing/costs/overview-cost-management)

まずはこの Issue のコメント欄に決定事項や未決事項を書き込んでください。最終的に Copilot がコメントをもとに `docs/nfr/cost.md` を作成します。
