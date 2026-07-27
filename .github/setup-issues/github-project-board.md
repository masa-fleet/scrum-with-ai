---
title: "[PBI] GitHub Project ボードをセットアップする"
labels:
  - pbi
  - setup
---

## 🎯 Goal

GitHub Project テンプレートをコピーし、このリポジトリと連携する。

## 📖 Background & Context

プロジェクト毎に GitHub Project ボードを 1 から作成すると作業だけでも約 30 分かかる。また、ビューの設定項目から考えると数時間かかる可能性もある。
[テンプレートプロジェクト](https://github.com/users/masa-fleet/projects/9) をコピーすることで、プロジェクト運営のノウハウが詰まった設定済みのボードをすぐに使える。

## ✅ Acceptance Criteria

- [ ] GitHub Project テンプレートを自分のレポジトリ/Organization にコピーしている
- [ ] `Auto-add to project` ワークフローのフィルタをこのリポジトリに設定・有効化している
- [ ] このリポジトリをプロジェクトに紐づけている

## 📝 1. プロジェクトをコピーする

1. [テンプレートプロジェクト](https://github.com/users/masa-fleet/projects/9) を開く。
2. 右上の [...] メニューをクリックし、[Make a Copy] を選択する。
3. Owner（自分のアカウントまたは Organization）を選択し、プロジェクト名を入力する。
4. [Copy project] をクリックする。

## 📝 2. Auto-add to project ワークフローを設定する

コピー後、`Auto-add to project` ワークフローは無効化された状態になっている。
以下の手順でフィルタを設定し、有効化する。

1. コピーしたプロジェクトを開き、右上の [Workflows] を選択する。
2. 左サイドバーの [Auto-add to project] をクリックする。
3. 右上の [Edit] ボタン をクリックする。
4. [Filters] のリポジトリドロップダウンでこのリポジトリを選択する。
5. フィルタテキストボックスに既存の文字列（例: `label:bug` などのプリセット）が入っている場合は、それらを全て削除してから `is:issue,pr is:open` と入力する。
6. [Save and turn on workflow] をクリックする。

## 📝 3. リポジトリとプロジェクトを紐づける

1. このリポジトリの [Projects] タブを開く。
2. [Link a project] をクリックし、コピーしたプロジェクトを選択する。
