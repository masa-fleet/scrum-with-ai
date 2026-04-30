# 🚀 Setting Up Your Repository

After creating a new repository from this template, follow the steps below to finish setting it up.

---

## Step 1 — Enable GitHub Actions

GitHub Actions are enabled by default on new repositories. If you disabled them, re-enable them via **Settings → Actions → General → Allow all actions**.

---

## Step 2 — Create Issue Labels

This template ships with a one-time workflow that creates all [standard labels](labels.md) for you.

1. Go to the **Actions** tab of your repository.
2. In the left sidebar, select **🏷️ Setup Repository Labels**.
3. Click **Run workflow → Run workflow** (leave the branch as `main`).

   [![Run workflow button](https://img.shields.io/badge/Actions-Run%20workflow-2088FF?logo=github-actions&logoColor=white)](../../actions/workflows/setup-labels.yml)

4. Wait for the run to complete (usually under 30 seconds). All labels will be created and the workflow will **disable itself automatically** so it won't run again by accident.

> **Want to recreate labels later?**  
> Go to **Actions → 🏷️ Setup Repository Labels**, click the three-dot menu on the workflow, select **Enable workflow**, then run it again.

---

## Step 3 — Configure GitHub Projects (optional)

The labels are designed to work well with GitHub Projects views:

| View name | Label filter |
|-----------|-------------|
| `pbi` | `pbi` |
| `epic` | `epic` |
| `risk` | `risk` |

See [labels.md](labels.md) for the full label reference and usage guidelines.
