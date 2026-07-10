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

- [ ] `main` ブランチ向けルールセットが作成されている
- [ ] 直接 push / 強制 push / ブランチ削除がブロックされている
- [ ] プルリクエストレビュー必須（必要レビュアー数 1）になっている
- [ ] [ブランチポリシー手順]({{REPO_BLOB_MAIN}}/docs/branch-policy.md) に沿って設定されている

## 📝 設定手順

1. **Settings → Rules → Rulesets** を開く
2. **New ruleset → Import a ruleset** をクリックする
3. [`.github/branch-policy-template.json`]({{REPO_BLOB_MAIN}}/.github/branch-policy-template.json) をアップロードする
4. 内容を確認して **Create** をクリックする
