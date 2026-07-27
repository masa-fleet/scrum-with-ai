# Backlog Management

| ステータス | 意味 | 主な更新者 |
| --- | --- | --- |
| `New` | 新規作成された PBI。 | PBI 作成者 |
| `Approved` | PO が品質と優先度を確認した PBI。 | PO |
| `In Progress` | 現在の Sprint で実装中。 | Developers |
| `Done` | 受け入れ条件を満たした PBI。 | Scrum Team |

## 準備完了の定義（DoR）

1. PBI Issue Template の必須項目と見積もりを記入する。
2. `ai-review` ラベルを付けて AI レビューを実行する。
3. AI フィードバックを反映し、必要に応じて Dev Lead / DS Lead に相談する。
4. `human-review` 状態で PO が確認し、承認後に `Approved` へ更新する。

## ワークフロー

1. **PBI 作成（誰でも）**
   - `New` で起票する。
   - 高優先度 PBI はリファインメント対象とする。
2. **バックログリファインメント会（PO + Scrum Team + Stakeholders）**
   - PBI を優先付けする。
   - 次 Sprint に投入予定の PBI を含めた `Approved` 在庫全体を Sprint 容量の 1.5〜2 倍で維持する。
   - 未 `Approved` PBI をレビューし、内容を確定する。
3. **Sprint Planning（Scrum Team）**
   - `Approved` から実装対象を選び `In Progress` に移す。
   - 優先度、ベロシティ、見積もりで Sprint Backlog を確定する。
4. **Sprint Review / Demo（Scrum Team + Stakeholders）**
   - 完了機能をデモし、受け入れ条件を検証する。
   - 完了 PBI を `Done` に更新する。
   - 新しい気づきは次の PBI として追加する。

## セレモニー別アジェンダ例

- **バックログリファインメント会**
  - 次 Sprint 以降の PBI 優先順位確認
  - 高優先度 PBI の詳細化状況確認
  - `Approved` 移行可否の判断
- **Sprint Planning**
  - Sprint Goal の確認
  - `Approved` PBI の投入可否確認
  - 実装担当の割り当て
- **Sprint Review / Demo**
  - 完了項目のデモ
  - 受け入れ条件の確認
  - 追加 PBI の起票判断

## 運用ルール

- Sprint Planning で投入する PBI は事前に `Approved` にする。
- `Approved` の在庫を Sprint 容量の 1.5〜2 倍で維持する。
