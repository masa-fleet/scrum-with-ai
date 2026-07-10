---
title: "[PBI] main ブランチのポリシーを設定する"
labels:
  - pbi
  - setup
---

## 🎯 Goal

`main` ブランチにルールセットを適用し、すべての変更がレビュー経由でマージされる状態にする。

## 📖 Background & Context

ブランチ保護設定はテンプレートから新規リポジトリへ自動継承されないため、リポジトリ作成直後に手動で設定する必要がある。

## ✅ Acceptance Criteria

- [ ] [ブランチポリシー手順]({{REPO_BLOB_MAIN}}/docs/branch-policy.md) に沿って `main` ブランチポリシーを適用している
- [ ] 設定後、`main` への直接 push がブロックされることを確認している
