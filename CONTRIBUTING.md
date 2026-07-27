# コントリビューションガイド

## ポリシー

- **AI がコード・ドキュメントを作成。** 人間はレビューと承認のみ担当する。
- Copilot cloud agent に指示して変更を生成する。
- Copilot cloud agent を使用したことがない場合、[Expand your team with Copilot](https://github.com/skills/expand-your-team-with-copilot) を参照。

## コントリビューションの範囲

- **事前承認済みの Collaborator:** Issue 登録・レビュー・承認、Copilot cloud agent への指示出し
- **その他の方:** Issue 登録のみ

## 貢献の流れ（事前承認済みの Collaborator 向け）

1. Issue 作成（`PBI` Issue Template を使用する。必須項目は全て記入する。）
2. PBI 作成後、PBI に `ai-review` ラベルを付与し、AI にレビューしてもらう。
3. PBI 作成者は AI のフィードバックを元に PBI を更新する。
4. PO によるレビュー。承認後 `Approved` 状態に変更する。
5. Copilot cloud agent に割り当て
6. PR をレビュー・承認・マージ

## ブランチ・プルリクエストのルール

- `main` ブランチへの直接プッシュは禁止。必ずプルリクエストを経由する。
- プルリクエストには対応する Issue を紐付ける。
- 承認は作成者以外から最低 1 名以上必須とする。
- 上記を満たせば、作成者本人のマージを許可する。

## Issue 登録のガイドライン（全員共通）

- 重複を確認する。
- タイトルは明確に記載する。
- Issue Template の必須項目を記入する。

## 行動規範

- [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/) に従う。
