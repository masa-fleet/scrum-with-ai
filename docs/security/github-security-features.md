# GitHub標準セキュリティ機能の比較

- 調査日: 2026-07-04
- 対象: `masa-fleet/scrum-with-ai`
- 前提: public リポジトリ / 個人ユーザー `masa-fleet` / GitHub Pro
- 料金は GitHub 公式情報準拠。public リポジトリで無償利用できる機能は追加課金なしとして扱う。

| 機能 | 概要 | 料金 | public・private での可否 | 推奨度 |
| --- | --- | --- | --- | --- |
| Dependabot（alerts / security updates / version updates） | 依存脆弱性の検知、修正版PR、自動バージョン更新。version updates は `dependabot.yml` が必要。 | 追加料金なし。<br>出典: [About Dependabot alerts](https://docs.github.com/en/code-security/dependabot/dependabot-alerts/about-dependabot-alerts)、[About Dependabot security updates](https://docs.github.com/en/code-security/dependabot/dependabot-security-updates/about-dependabot-security-updates)、[About Dependabot version updates](https://docs.github.com/en/code-security/dependabot/dependabot-version-updates/about-dependabot-version-updates)、[GitHub's plans](https://docs.github.com/en/get-started/learning-about-github/githubs-plans)<br>調査日: 2026-07-04 | public: 可<br>private: 可 | 高 |
| Code scanning（CodeQL / GitHub Actionsベース） | CodeQL または SARIF 連携でコード脆弱性を検知。通常は GitHub Actions で実行。 | public: 無償。<br>private: GitHub Code Security が必要。$30 USD / active committer / month。private では Actions 分数も消費。<br>個人 Pro の private では購入前提を満たせず実質不可。<br>出典: [About code scanning](https://docs.github.com/en/code-security/code-scanning/introduction-to-code-scanning/about-code-scanning)、[About GitHub Advanced Security](https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security)、[About billing for GitHub Advanced Security](https://docs.github.com/en/billing/managing-billing-for-your-products/managing-billing-for-github-advanced-security/about-billing-for-github-advanced-security)、[GitHub security plans](https://github.com/security/plans)、[About billing for GitHub Actions](https://docs.github.com/en/billing/managing-billing-for-github-actions/about-billing-for-github-actions)<br>調査日: 2026-07-04 | public: 可<br>private: 組織 Team/Enterprise + GitHub Code Security で可。個人 Pro private は不可 | 高 |
| Secret scanning + push protection | 秘密情報の検知と push 時ブロック。漏えい予防の即効性が高い。 | public: 無償。<br>private: GitHub Secret Protection が必要。$19 USD / active committer / month。<br>個人 Pro の private では購入前提を満たせず実質不可。<br>出典: [About secret scanning](https://docs.github.com/en/code-security/secret-scanning/introduction/about-secret-scanning)、[GitHub security features](https://docs.github.com/en/code-security/getting-started/github-security-features)、[About GitHub Advanced Security](https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security)、[About billing for GitHub Advanced Security](https://docs.github.com/en/billing/managing-billing-for-your-products/managing-billing-for-github-advanced-security/about-billing-for-github-advanced-security)、[GitHub security plans](https://github.com/security/plans)<br>調査日: 2026-07-04 | public: 可<br>private: 組織 Team/Enterprise + GitHub Secret Protection で可。個人 Pro private は不可 | 高 |
| Private vulnerability reporting / Security advisories | 外部報告者からの非公開報告受付と、修正後の advisory 公開を支援。 | public: 無償。<br>private: GitHub.com の private リポジトリでは対象外。<br>出典: [Privately report a security vulnerability](https://docs.github.com/en/code-security/how-tos/report-and-fix-vulnerabilities/report-privately)、[About repository security advisories](https://docs.github.com/en/code-security/security-advisories/working-with-repository-security-advisories/about-repository-security-advisories)<br>調査日: 2026-07-04 | public: 可<br>private: 不可 | 中 |
| Branch protection / Rulesets | `main` への直接 push 防止、必須レビュー、必須チェック、署名コミット要求などを設定。 | public: 無償。<br>private: Protected branches は GitHub Pro 以上で可。Rulesets は public は Free でも可、private は Pro 以上で可。<br>出典: [About protected branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches)、[About rulesets](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets)、[GitHub's plans](https://docs.github.com/en/get-started/learning-about-github/githubs-plans)<br>調査日: 2026-07-04 | public: 可<br>private: GitHub Pro 以上で可 | 高 |
| Dependency review / Dependency graph | dependency graph で依存関係可視化。dependency review で PR に入る依存差分と脆弱性を確認。 | dependency graph: public/private とも追加料金なし。<br>dependency review: public は無償、private は GitHub Code Security が必要。$30 USD / active committer / month。<br>個人 Pro の private では dependency review は不可。<br>出典: [About the dependency graph](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/about-the-dependency-graph)、[About dependency review](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/about-dependency-review)、[About GitHub Advanced Security](https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security)、[GitHub security plans](https://github.com/security/plans)<br>調査日: 2026-07-04 | dependency graph: public/private 可<br>dependency review: public 可、private は組織 Team/Enterprise + GitHub Code Security で可 | 高 |
| GitHub Advanced Security（GHAS） | private リポジトリ向け有償枠の総称。現在は GitHub Secret Protection と GitHub Code Security に分かれる。public は主要機能の一部を無償利用可能。 | GitHub Secret Protection: $19 USD / active committer / month。<br>GitHub Code Security: $30 USD / active committer / month。<br>public リポジトリは主要機能を無償利用可。private はライセンス必須。<br>出典: [About GitHub Advanced Security](https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security)、[About billing for GitHub Advanced Security](https://docs.github.com/en/billing/managing-billing-for-your-products/managing-billing-for-github-advanced-security/about-billing-for-github-advanced-security)、[GitHub security plans](https://github.com/security/plans)<br>調査日: 2026-07-04 | public: 主要機能の一部を無償利用可<br>private: 組織 Team/Enterprise + 有償ライセンスで可 | 現状は低 |

## 選択基準

| リポジトリ条件 | 使うべき機能 | 判断 |
| --- | --- | --- |
| public / 個人 Pro / GHAS なし | Dependabot、code scanning、secret scanning、push protection、private vulnerability reporting、security advisories、dependency graph、dependency review、branch protection / rulesets | 今回の前提。無償で使える機能を漏れなく有効化するのが最適。 |
| private / 個人 Pro / GHAS なし | Dependabot、dependency graph、protected branches / rulesets | code scanning、secret scanning、dependency review は private の個人 Pro では使えない。private vulnerability reporting / security advisories も public 向け。 |
| private / 組織 Team / Secret Protection のみ | 上記 + secret scanning + push protection | 秘密情報漏えい対策を優先する場合の最小構成。 |
| private / 組織 Team / Code Security のみ | 上記 + code scanning + dependency review | アプリケーション脆弱性と依存差分の検査を優先する場合の最小構成。 |
| private / 組織 Team or Enterprise / Secret Protection + Code Security | 7カテゴリのうち public 専用機能を除くほぼ全機能 | private 化後も public 同等の守りを維持したい場合の本命。active committer 課金を前提に予算化する。 |

## private 化した場合の費用影響

- 現状の public では code scanning、secret scanning、dependency review などの主要機能は無償。
- private にすると、個人 Pro のままでは code scanning / secret scanning / dependency review を継続できない。
- private でも同等水準を維持するなら、組織 Team 以上へ移行し、必要に応じて以下を追加購入する。
  - GitHub Secret Protection: $19 USD / active committer / month
  - GitHub Code Security: $30 USD / active committer / month
- たとえば active committer が 3 人なら、両方導入時の概算は月額 `3 x (19 + 30) = 147 USD`。
- code scanning は private で GitHub-hosted runner を使うと Actions 分数も消費する。
- public の標準 GitHub-hosted runner は無料・無制限だが、private はプランごとの無料枠を超えると従量課金になる。
- 個人 Pro の無料枠は 3,000 分 / 月。

## 費用対効果ベースの優先度

1. Branch protection / Rulesets — 採用。事故防止の即効性が高く、現行 public / Pro で追加料金なし。
2. Dependabot alerts / security updates / version updates — 採用。依存脆弱性対策を継続運用しやすく、追加料金なし。
3. Secret scanning + push protection — 採用。漏えいを事後検知だけでなく push 前に止められ、public では無償。
4. Code scanning — 採用。CodeQL の検知価値が高く、public では無償。private 化時だけ追加コストを検討すればよい。
5. Dependency review / Dependency graph — 採用。PR 時点で危険な依存追加を止められ、supply chain 対策として費用対効果が高い。
6. Private vulnerability reporting / Security advisories — 採用。公開 OSS として報告窓口と開示フローを持つ価値が高い。
7. private 向け有償 GHAS 追加購入 — 現時点では不採用。現在は public で大半を無償利用でき、個人 Pro のまま private 化しても導入できないため、組織移管の要否と合わせて再評価する。

## 本PJで有効化する機能

- 有効化する
  - Branch protection または ruleset で `main` を保護する
  - Dependabot alerts を有効化する
  - Dependabot security updates を有効化する
  - Dependabot version updates を `dependabot.yml` で運用する
  - Dependency graph を有効化する
  - Dependency review を有効化する
  - Code scanning を default setup（CodeQL）で有効化する
  - Secret scanning と push protection を有効化する
  - Private vulnerability reporting を有効化する
  - Security advisories を運用する
- 有効化しない
  - private 向けの GitHub Secret Protection / GitHub Code Security の追加購入
- 結果費用
  - 追加費用は `0 USD / 月`。
  - 理由は、このPJで有効化する対象が public リポジトリで無償利用できる標準機能だけで、private 向け有償製品を追加購入しないため。
  - Code scanning を GitHub Actions ベースで動かしても、public リポジトリの標準 GitHub-hosted runner は無料・無制限のため追加費用は発生しない。
- 理由
  - このリポジトリは public なので、無償で使える標準機能を広く有効化するのが最も合理的。
  - private 向け有償製品は、private 化と組織移管が決まった時点で active committer 数を見て再見積もりすればよい。

## 参照した公式ドキュメント

- [GitHub security features](https://docs.github.com/en/code-security/getting-started/github-security-features)
- [About GitHub Advanced Security](https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security)
- [GitHub's plans](https://docs.github.com/en/get-started/learning-about-github/githubs-plans)
- [About billing for GitHub Advanced Security](https://docs.github.com/en/billing/managing-billing-for-your-products/managing-billing-for-github-advanced-security/about-billing-for-github-advanced-security)
- [GitHub security plans](https://github.com/security/plans)
- [About billing for GitHub Actions](https://docs.github.com/en/billing/managing-billing-for-github-actions/about-billing-for-github-actions)
- [Standard GitHub-hosted runners for public repositories](https://docs.github.com/en/actions/how-tos/write-workflows/choose-where-workflows-run/choose-the-runner-for-a-job#standard-github-hosted-runners-for-public-repositories)
- [About Dependabot alerts](https://docs.github.com/en/code-security/dependabot/dependabot-alerts/about-dependabot-alerts)
- [About Dependabot security updates](https://docs.github.com/en/code-security/dependabot/dependabot-security-updates/about-dependabot-security-updates)
- [About Dependabot version updates](https://docs.github.com/en/code-security/dependabot/dependabot-version-updates/about-dependabot-version-updates)
- [About code scanning](https://docs.github.com/en/code-security/code-scanning/introduction-to-code-scanning/about-code-scanning)
- [About secret scanning](https://docs.github.com/en/code-security/secret-scanning/introduction/about-secret-scanning)
- [Privately report a security vulnerability](https://docs.github.com/en/code-security/how-tos/report-and-fix-vulnerabilities/report-privately)
- [About repository security advisories](https://docs.github.com/en/code-security/security-advisories/working-with-repository-security-advisories/about-repository-security-advisories)
- [About protected branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches)
- [About rulesets](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets)
- [About the dependency graph](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/about-the-dependency-graph)
- [About dependency review](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/about-dependency-review)
