---
title: "[PBI] セキュリティ NFR を整理する"
labels:
  - pbi
  - setup
---

## 🎯 Goal

プロジェクトのセキュリティ要件を整理し、`docs/nfr/security.md` に保存する。

## 📖 Background & Context

セキュリティ要件を早期に明確化することで、設計・実装フェーズでの手戻りを防ぐ。
AI がここに保存された要件を参照してアーキテクチャ設計やコードレビューに活用できる。

## ✅ Acceptance Criteria

- [ ] [SE:01](https://learn.microsoft.com/ja-jp/azure/well-architected/security/establish-baseline) 準拠すべき法令・規制・業界標準（例: GDPR、PCI DSS、ISO 27001）が列挙されている
- [ ] [SE:02](https://learn.microsoft.com/ja-jp/azure/well-architected/security/secure-development-lifecycle) / [SE:11](https://learn.microsoft.com/ja-jp/azure/well-architected/security/test) 脆弱性管理方針（例: Dependabot、CodeQL、ペネトレーションテスト頻度）が決定されている
- [ ] [SE:05](https://learn.microsoft.com/ja-jp/azure/well-architected/security/identity-access) 認証・認可方式（例: OAuth 2.0 / OIDC、RBAC/ABAC）が決定されている
- [ ] [SE:07](https://learn.microsoft.com/ja-jp/azure/well-architected/security/encryption) 通信の暗号化要件（例: TLS 1.2+）が決定されている
- [ ] [SE:07](https://learn.microsoft.com/ja-jp/azure/well-architected/security/encryption) 保存データの暗号化要件（例: AES-256 at rest）が決定されている
- [ ] [SE:09](https://learn.microsoft.com/ja-jp/azure/well-architected/security/application-secrets) シークレット管理方式（例: Azure Key Vault、GitHub Secrets）が決定されている
- [ ] [SE:12](https://learn.microsoft.com/ja-jp/azure/well-architected/security/incident-response) セキュリティインシデント対応フロー（検知 → 通知 → 封じ込め → 回復）が定義されている
- [ ] 整理された内容が `docs/nfr/security.md` に保存されている

## 📝 参考

- [Azure Well-Architected Framework — セキュリティ](https://learn.microsoft.com/ja-jp/azure/well-architected/security/)
- [セキュリティ設計レビューチェックリスト](https://learn.microsoft.com/ja-jp/azure/well-architected/security/checklist)
- [OWASP Top 10](https://owasp.org/www-project-top-ten/)

まずはこの Issue のコメント欄に決定事項や未決事項を書き込んでください。最終的に Copilot がコメントをもとに `docs/nfr/security.md` を作成します。
