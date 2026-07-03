---
title: "[PBI] GitHub Project ボードをセットアップする"
labels:
  - pbi
  - setup
---

## 🎯 Goal

GitHub Project テンプレートをコピーし、このリポジトリと連携する。

## 📖 Background & Context

プロジェクト毎に GitHub Project ボードを一から作成すると約 30 分かかる。
[テンプレートプロジェクト](https://github.com/users/masa-fleet/projects/9) をコピーすることで、設定済みのボードをすぐに使える。

## ✅ Acceptance Criteria

- [ ] GitHub Project テンプレートをコピーしている
- [ ] `Auto-add to project` ワークフローのフィルタをこのリポジトリに設定・有効化している
- [ ] このリポジトリをプロジェクトに紐づけている
- [ ] Security ビューをプロジェクトに追加している

## 📝 1. プロジェクトをコピーする

1. [テンプレートプロジェクト](https://github.com/users/masa-fleet/projects/9) を開く。
2. 右上の **...** メニューをクリックし、**Copy** を選択する。
3. Owner（自分のアカウントまたは Organization）を選択し、プロジェクト名を入力する。
4. **Copy project** をクリックする。

## 📝 2. Auto-add to project ワークフローを設定する

コピー後、`Auto-add to project` ワークフローは無効化された状態になっている。
以下の手順でフィルタを設定し、有効化する。

1. コピーしたプロジェクトを開き、右上の **...** → **Workflows** を選択する。
2. 左サイドバーの **Auto-add to project** をクリックする。
3. **Edit** をクリックする。
4. **Filters** のリポジトリドロップダウンでこのリポジトリを選択する。
5. フィルタテキストボックスに `is:issue,pr is:open` と入力する。
6. **Save and turn on workflow** をクリックする。

## 📝 3. リポジトリとプロジェクトを紐づける

1. このリポジトリの **Settings** タブを開く。
2. 左サイドバーの **Integrations** → **GitHub Projects** を選択する。
3. **Link a project** をクリックし、コピーしたプロジェクトを選択する。

## 📝 4. Security ビューを追加する

1. コピーしたプロジェクトを開く。
2. ビュータブ右端の **+** をクリックして新しいビューを追加する。
3. ビュー名を `Security` に設定する。
4. フィルタに `label:security` を設定する。
