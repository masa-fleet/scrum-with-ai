---
title: "[PBI] パフォーマンス効率 NFR を整理する"
labels:
  - pbi
  - setup
---

## 🎯 Goal

プロジェクトのパフォーマンス要件を整理し、`docs/nfr/performance.md` に保存する。

## 📖 Background & Context

パフォーマンス要件を設計前に定義しておくことで、アーキテクチャの選択肢（キャッシュ、非同期処理、スケーリング戦略など）を適切に絞り込める。
AI がここに保存された要件を参照して技術選定やインフラ設計に活用できる。

## ✅ Acceptance Criteria

- [ ] レスポンスタイム目標（例: API p95 < 500ms）が定義されている
- [ ] スループット目標（例: ピーク 1,000 RPS）が定義されている
- [ ] 同時接続数の想定（例: 最大 500 同時ユーザー）が定義されている
- [ ] スケーリング戦略（水平/垂直、オートスケール閾値）が決定されている
- [ ] パフォーマンステスト方針（負荷テスト・スパイクテストの頻度・ツール）が決定されている
- [ ] データ量の想定（例: 月間 10 GB 増加、最大 1 TB）が定義されている
- [ ] キャッシュ戦略（対象データ、TTL、無効化方針）が決定されている
- [ ] 整理された内容が `docs/nfr/performance.md` に保存されている

## 📝 参考

- [Azure Well-Architected Framework — パフォーマンス効率](https://learn.microsoft.com/ja-jp/azure/well-architected/performance-efficiency/overview)

まずはこの Issue のコメント欄に決定事項や未決事項を書き込んでください。最終的に Copilot がコメントをもとに `docs/nfr/performance.md` を作成します。
