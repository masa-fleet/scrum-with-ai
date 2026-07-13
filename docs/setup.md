# 🚀 リポジトリのセットアップ

テンプレート レポジトリからユーザー リポジトリを作成した後、以下の手順でセットアップを完了する。

---

## Step 1 — GitHub Actions を有効にする

新しいリポジトリでは GitHub Actions はデフォルトで有効。無効にした場合は **Settings → Actions → General → Allow all actions** で再度有効にする。

---

## Step 2 — Issue ラベルを作成する

テンプレートには[標準ラベル](labels.md)を一括作成するワークフローが含まれているので、自動作成されます。もし自動作成されない場合には、以下の手順をお試しください。

1. リポジトリの **Actions** タブを開く
2. 左サイドバーで **🚀 Setup Repository** を選択
3. **Run workflow → Run workflow** をクリック（ブランチは `main` のまま）

   [![Run workflow button](https://img.shields.io/badge/Actions-Run%20workflow-2088FF?logo=github-actions&logoColor=white)](../../actions/workflows/setup.yml)

4. 実行完了を待つ（通常 30 秒以内）。すべてのラベルが作成され、ワークフローは**自動的に無効化**される

> **ラベルを再作成したい場合：**
> **Actions → 🚀 Setup Repository** のワークフローの三点メニューから **Enable workflow** を選択し、再度実行する。

---

## Step 3 — ブランチポリシーを適用する

[branch-policy.md](branch-policy.md) に定義されたブランチルールセットで `main` を保護する。

> **注意：** ブランチ保護設定はテンプレート レポジトリから自動的に継承されない。新しいユーザー レポジトリごとに手動で設定する必要がある。

---

## Step 4 — GitHub Projects を設定する（任意）

ラベルは GitHub Projects のビューと組み合わせて使える。

| ビュー名 | ラベルフィルター |
|----------|-----------------|
| `pbi` | `pbi` |
| `epic` | `epic` |
| `risk` | `risk` |

ラベルの一覧と使い方は [labels.md](labels.md) を参照。
