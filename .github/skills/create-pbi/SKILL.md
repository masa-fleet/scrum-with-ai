---
name: create-pbi
description: 短い要望から GitHub に PBI を作成・登録する。
---

# PBI を作成する

短い要望から GitHub に PBI を作成・登録する。

## 手順

1. `.github/ISSUE_TEMPLATE/pbi.yml` を読み、各入力項目の `description` を PBI の内容と品質の基準にする。
2. 要望の理解に必要なファイルだけを読み込む。リポジトリ全体のファイルを一括で読み込まない。
3. `gh issue list` などで既存 Issue の重複を確認する。重複候補があれば提示し、新規作成か既存 PBI の更新かをユーザーに確認する。
4. `gh repo view --json nameWithOwner,isPrivate` でリポジトリの Owner / Name と公開状態を取得する。
5. Public Repository で、要望に特定顧客の情報が含まれる場合は、顧客名、製品名、案件名、識別可能な固有情報を削除または一般化する。目的や受け入れ条件が変わる場合は作成前に確認する。
6. PBI 作成に必要な情報が不足している場合だけ質問する。それ以外はタイトルと本文の案を作成する。
7. Acceptance Criteria は約 5 個までにし、各項目に成果物の形式と格納場所を明記する。5 個を超え、Estimate が 8 を超える場合は PBI を分割する。
8. 作成前に案を表示し、1 回だけ確認を求める。
9. 確認後に以下を実行する。
   - `gh issue create --label pbi` で Issue を作成する。
   - リポジトリの自動追加設定で Issue がリンクされた Project に追加されるのを確認する。
   - Project のフィールド名と選択肢を使い、指定された Sprint を設定する。
10. Issue URL と挿入した Sprint を報告する。変更処理に失敗した場合は、完了したと報告せずエラーを示す。

応答と生成する PBI は簡潔にする。
