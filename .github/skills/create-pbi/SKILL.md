---
name: create-pbi
description: GPT-5.6 Luna を使い、短い要望から GitHub Project に PBI を作成・登録する。
---

# PBI を作成する

ユーザーの要望から PBI を作成し、リポジトリにリンクされた GitHub Project に登録する。
利用可能な場合は GPT-5.6 Luna を使用して実行する。

## 手順

1. `.github/ISSUE_TEMPLATE/pbi.yml` を読み、各入力項目の `description` を PBI の内容と品質の基準にする。
2. 要望に関係するファイルだけを読み、既存 Issue の重複を確認する。リポジトリ全体のファイルを一括で読み込まない。
3. `gh repo view --json nameWithOwner` でリポジトリの Owner / Name を取得する。
4. GraphQL の `repository.projectsV2` でリポジトリにリンクされた Project を取得する。Project ID はハードコードしない。
5. PBI 作成に必要な情報が不足している場合だけ質問する。それ以外はタイトルと本文の案を作成する。
6. 作成前に案を表示し、1 回だけ確認を求める。
7. 確認後に以下を実行する。
   - `gh issue create --label pbi` で Issue を作成する。
   - リポジトリの自動追加設定で Issue がリンクされた Project に追加されるのを確認する。
   - Project のフィールド名と選択肢を使い、指定された Sprint と `New` Status を設定する。
8. Issue URL と最終的な Project の値を報告する。変更処理に失敗した場合は、完了したと報告せずエラーを示す。

応答と生成する PBI は簡潔にする。
