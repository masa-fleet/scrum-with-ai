# Backlog Management

| ステータス | 意味 | 主な更新者 |
| --- | --- | --- |
| `New` | 新規作成された PBI。 | PBI 作成者 |
| `Approved` | PO または Development Lead が品質と優先度を確認した PBI。 | PO / Development Lead |
| `In Progress` | 現在の Sprint で実装中。 | Developers |
| `Done` | 受け入れ条件を満たした PBI。 | Scrum Team |

## ラベル運用

- PBI 作成者が起票時に `pbi` ラベルを付ける。
- PBI 作成者が DoR 確認前に `ai-review` を付ける。
- AI レビュー完了後に `human-review` が付き、PO が最終確認する。

## 準備完了の定義（DoR）

1. PBI Issue Template の必須項目を記入する。
2. `ai-review` ラベルを付けて AI レビューを実行する。
3. AI フィードバックを反映し、必要に応じて Dev Lead / DS Lead に相談する。
4. `human-review` 状態で PO が確認し、承認後に `Approved` へ更新する。

## ワークフロー

1. **PBI 作成（誰でも）**
   - `New` で起票する。
   - 初期優先度が分かる場合は記入する。
2. **PO バックログレビュー会（PO + Development Lead）**
   - PBI を優先付けする。
   - 次 Sprint 投入分に加えて、Sprint 容量の 1.5〜2 倍を目安に `Approved` 候補を整える。
   - 詳細化が必要な高優先度 PBI の担当を決める。
3. **バックログリファインメント会（Scrum Team + Stakeholders）**
   - 次 Sprint 群の計画前提をそろえる。
   - 未 `Approved` PBI をレビューし、内容を確定する。
4. **Sprint Planning（Scrum Team）**
   - `Approved` から実装対象を選び `In Progress` に移す。
   - 優先度、ベロシティ、見積もりで Sprint Backlog を確定する。
5. **Sprint Review / Demo（Scrum Team + Stakeholders）**
   - 完了機能をデモし、受け入れ条件を検証する。
   - 完了 PBI を `Done` に更新する。
   - 新しい気づきは次の PBI として追加する。

## 運用ルール

- 次 Sprint に投入する PBI は、Sprint Planning までに `Approved` である。
- レトロスペクティブ由来の改善 PBI は、チーム合意で Sprint 途中に追加する場合がある。この場合も着手前に PO が内容を確認する。
- `Approved` の在庫を Sprint 容量の 1.5〜2 倍で維持する。
