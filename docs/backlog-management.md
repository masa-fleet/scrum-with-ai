# Backlog Management

| ステータス | 意味 | 主な更新者 |
| --- | --- | --- |
| `New` | 新規作成された PBI。 | PBI 作成者 |
| `Approved` | PO が品質と優先度を確認した PBI。 | PO |
| `In Progress` | 現在の Sprint で実装中。 | Developers |
| `Done` | 受け入れ条件を満たした PBI。 | Scrum Team |

## PBI は Scrum Team の誰でも作成可能

- Scrum Team の誰もが PBI を作成できる。
- 誰もが意見やアイディアを提供できるオープンな環境づくりにつながる。
- 一番その分野に詳しい人が書くことで、非効率な確認や応答を減らせる。

## `Approved` までの手順

1. PBI Issue Template の必須項目と見積もり (Effort) を記入する。
2. `ai-review` ラベルを付けて AI レビューを実行する。
3. AI フィードバックを反映し、必要に応じて Dev Lead / DS Lead に相談する。
4. `human-review` ラベルが付いた状態で PO が確認し、承認後に `Approved` へ更新する。

## ワークフロー

1. **PBI 作成（誰でも）**
   - `New` で起票する。
   - 実施したい Sprint に追加する。実施 Sprint は Backlog Refinement ミーティングにて他の PBI との優先度を考慮して最終決定される。
2. **Backlog Refinement（Scrum Team + Stakeholders）**
   - Epic の分割に抜け漏れがないかを議論する。必要な場合、その場で Developers と分割する。
   - Sprint Goal やプロジェクトの優先度を元に PBI を優先付けする。
   - 高優先度の PBI をレビューし `Approved` 状態にする。 (`Approved` 在庫全体を 平均 Velocity の 1.5〜2 倍で維持するのが理想的)
3. **Sprint Planning（Scrum Team）**
   - 優先度、Velocity、PBI の合計 Effort を考慮して Sprint Backlog を確定する。
   - Sprint で実装する PBI を `Approved` から `In Progress` に変更する。
4. **Sprint Review / Demo（Scrum Team + Stakeholders）**
   - `Done` PBI のデモを実施し、受け入れ条件を PO が検証する (Developers は PR でレビュー済み)。
   - 受け入れ条件を満たしていない場合、PBI を reopen する (`Done` -> `In Progress`)。
   - 新しい気づきや、Acceptance Criteria にはないけれど追加実装すべきものは別 PBI として追加する。

## 運用ルール

- Sprint Planning で投入する PBI は事前に `Approved` にする。Scrum Team の時間を効果的に使うために、特別な事情が無い限り `Approved` 状態でない PBI は Sprint Planning では扱わない。
- `Approved` の在庫を Sprint 容量の 1.5〜2 倍で維持する。欲を言えば、3 - 4 Sprint 先の PBI を (タイトル記入だけでも良いので) 準備する。
- セレモニー別アジェンダは [scrum-ceremonies-agenda.md](scrum-ceremonies-agenda.md) を参照する。
