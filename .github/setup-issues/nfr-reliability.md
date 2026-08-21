---
title: "[PBI] 信頼性 NFR を整理する"
labels:
  - pbi
  - setup
---

## 🎯 Goal

プロジェクトの信頼性要件を整理し、`docs/nfr/reliability.md` に保存する。

## 📖 Background & Context

可用性・復旧目標を早期に定義することで、冗長構成・バックアップ・フェイルオーバー設計の方向性が決まる。
AI がここに保存された要件を参照してインフラ設計や IaC に活用できる。

## ✅ Acceptance Criteria

- [ ] [RE:04](https://learn.microsoft.com/ja-jp/azure/well-architected/reliability/metrics) 可用性目標（SLA/SLO 例: 99.9% = 月 43 分以内のダウンタイム）が定義されている
- [ ] [RE:04](https://learn.microsoft.com/ja-jp/azure/well-architected/reliability/metrics) RTO（Recovery Time Objective、例: 障害発生から 1 時間以内に復旧）が定義されている
- [ ] [RE:04](https://learn.microsoft.com/ja-jp/azure/well-architected/reliability/metrics) RPO（Recovery Point Objective、例: 最大 15 分分のデータ損失まで許容）が定義されている
- [ ] [RE:09](https://learn.microsoft.com/ja-jp/azure/well-architected/reliability/disaster-recovery) バックアップ方針（頻度・保持期間・世代数）が定義されている
- [ ] [RE:10](https://learn.microsoft.com/ja-jp/azure/well-architected/reliability/monitoring) 障害検知・アラート方針（モニタリング対象・通知先）が決定されている
- [ ] [RE:05](https://learn.microsoft.com/ja-jp/azure/well-architected/reliability/redundancy) / [RE:07](https://learn.microsoft.com/ja-jp/azure/well-architected/reliability/self-preservation) フェイルオーバー戦略（アクティブ-スタンバイ / アクティブ-アクティブ、リージョン冗長等）が決定されている
- [ ] [RE:03](https://learn.microsoft.com/ja-jp/azure/well-architected/reliability/failure-mode-analysis) / [RE:07](https://learn.microsoft.com/ja-jp/azure/well-architected/reliability/self-preservation) 依存する外部サービスの障害に対する Fallback / Circuit Breaker 方針が定義されている
- [ ] 整理された内容が `docs/nfr/reliability.md` に保存されている

## 📝 参考

- [Azure Well-Architected Framework — 信頼性](https://learn.microsoft.com/ja-jp/azure/well-architected/reliability/)
- [信頼性設計レビューチェックリスト](https://learn.microsoft.com/ja-jp/azure/well-architected/reliability/checklist)

まずはこの Issue のコメント欄に決定事項や未決事項を書き込んでください。最終的に Copilot がコメントをもとに `docs/nfr/reliability.md` を作成します。
