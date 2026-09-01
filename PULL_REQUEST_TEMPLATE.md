# セキュリティ設定ファイルの追加

GitHub セキュリティ機能を有効化するための設定ファイルを追加します。

## 📝 変更内容

- ✅ `dependabot.yml`: npm と GitHub Actions の自動更新スキャン設定
- ✅ `codeql.yml`: CodeQL による Code Scanning workflow（全言語対応）
- ✅ `secret-scanning.yml`: Secret Scanning workflow（全ブランチ対応）

## ⚙️ 重要パラメーター

### 1. dependabot.yml

| パラメーター | 設定値 | 意味 |
|-----------|--------|------|
| **interval** | weekly | 週1回のスキャン |
| **day** | monday | 月曜日に実行 |
| **time** | 03:00 (npm) / 04:00 (Actions) | UTC 時間。npm は毎週月曜 3:00 UTC、Actions は 4:00 UTC |
| **open-pull-requests-limit** | 10 (npm) / 5 (Actions) | 同時に開く PR の上限 |
| **reviewers / assignees** | haonuma | PR の Reviewer と Assignee |
| **labels** | dependencies, dependabot | 自動作成 PR に付与するラベル |

**実行スケジュール:**
- 毎週月曜日に Dependabot が自動実行
- npm パッケージと GitHub Actions の脆弱性をスキャン

### 2. codeql.yml

| パラメーター | 設定値 | 意味 |
|-----------|--------|------|
| **on.push.branches** | ["main"] | main ブランチへの push で実行 |
| **on.pull_request.branches** | ["main"] | main への PR 時に実行 |
| **language** | ["cpp", "csharp", "go", "java", "javascript", "python", "ruby"] | 複数言語対応（テンプレート向け） |
| **fail-fast** | false | 1言語の分析失敗時も他言語は継続 |
| **continue-on-error** | true | スキャン対象コードなしでもワークフロー成功 |
| **permissions** | contents: read, security-events: write | 必要な権限 |

**実行タイミング:**
- main ブランチへの Push 時
- main への PR 作成時
- 存在する言語のみをスキャン（存在しない言語はスキップ）

**テンプレート対応:**
- ユーザーがテンプレートからリポジトリを作成し、任意の言語で実装を開始しても、自動的に対応言語をスキャン
- スキャン対象コードがない言語はエラーにならず、ワークフロー全体は成功

### 3. secret-scanning.yml

| パラメーター | 設定値 | 意味 |
|-----------|--------|------|
| **on.push** | ブランチ指定なし | すべてのブランチへの push で実行 |
| **on.pull_request** | ブランチ指定なし | すべてのブランチへの PR 時に実行 |
| **fetch-depth** | 0 | リポジトリ全体の履歴を取得（秘密情報検出用） |
| **permissions** | contents: read, security-events: write | 必要な権限 |

**実行タイミング:**
- Push 時（すべてのブランチ）
- PR 作成時（すべてのブランチ）

**秘密情報漏えい防止の強化:**
- 開発ブランチでも秘密情報の混入をキャッチ
- main ブランチに到達する前に検出・ブロック可能

## 📊 スキャン実行スケジュール

| 機能 | スキャン間隔 | 実行トリガー |
|-----|-----------|----------|
| **Dependabot** | 週1回（月曜 3:00 UTC） | スケジュール + 手動トリガー可能 |
| **Code Scanning (CodeQL)** | 常時 | main への Push、PR |
| **Secret Scanning** | 常時 | すべてのブランチ（Push、PR） |

## 📖 参考

- セキュリティ設定の詳細: [docs/security/github-security-features.md](https://github.com/masa-fleet/scrum-with-ai/blob/main/docs/security/github-security-features.md)
- 対象リポジトリ: public / GitHub Pro（すべての標準機能が無料）

## 🔗 関連 Issue

Closes #91
