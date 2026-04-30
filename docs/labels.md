# 🏷️ Repository Labels

This document defines the standard labels used in this repository. These labels are designed to support AI-assisted Scrum workflows and make it easy to filter, view, and manage issues in GitHub Projects.

---

## Issue Type Labels

| Label | Color | Purpose |
|-------|-------|---------|
| `pbi` | ![#0075ca](https://placehold.co/12x12/0075ca/0075ca.png) `#0075ca` | **Product Backlog Item** — A unit of work representing a specific feature, improvement, or change. Use for the `pbi` view in GitHub Projects. |
| `epic` | ![#6f42c1](https://placehold.co/12x12/6f42c1/6f42c1.png) `#6f42c1` | **Epic** — A large body of work that encompasses multiple PBIs toward a bigger business objective. Epics are the parent level of PBIs. |
| `bug` | ![#d73a4a](https://placehold.co/12x12/d73a4a/d73a4a.png) `#d73a4a` | **Bug** — Something isn't working as expected and needs to be investigated and fixed. |
| `task` | ![#a2eeef](https://placehold.co/12x12/a2eeef/a2eeef.png) `#a2eeef` | **Task** — A specific, actionable work item that doesn't directly deliver user value on its own (e.g., infrastructure, configuration). |

---

## AI-Assisted Labels

| Label | Color | Purpose |
|-------|-------|---------|
| `ai-review` | ![#5319e7](https://placehold.co/12x12/5319e7/5319e7.png) `#5319e7` | **AI Review** — Request an AI assistant to review and assess the quality, clarity, or completeness of this issue. Useful as a quality gate before sprint planning. |
| `prototype` | ![#e4e669](https://placehold.co/12x12/e4e669/e4e669.png) `#e4e669` | **Prototype** — This issue is for exploratory or prototyping purposes. Deep consideration of NFRs (non-functional requirements) and backend architecture is not required at this stage. |

---

## Management Labels

| Label | Color | Purpose |
|-------|-------|---------|
| `risk` | ![#e4700d](https://placehold.co/12x12/e4700d/e4700d.png) `#e4700d` | **Risk** — Identifies a risk item that the team needs to monitor or mitigate. Use for the `risk` view in GitHub Projects to manage the risk register. |
| `blocked` | ![#b60205](https://placehold.co/12x12/b60205/b60205.png) `#b60205` | **Blocked** — Progress on this issue is blocked by an unresolved dependency, external factor, or decision. Requires immediate attention. |
| `tech-debt` | ![#ededed](https://placehold.co/12x12/ededed/ededed.png) `#ededed` | **Technical Debt** — Tracks technical debt that has been deliberately taken on and needs to be addressed in a future sprint. |

---

## Workflow / Status Labels

| Label | Color | Purpose |
|-------|-------|---------|
| `sprint` | ![#006b75](https://placehold.co/12x12/006b75/006b75.png) `#006b75` | **Sprint** — This item is planned for or being tracked in the current sprint. Useful for filtering the active sprint board. |
| `in-progress` | ![#0e8a16](https://placehold.co/12x12/0e8a16/0e8a16.png) `#0e8a16` | **In Progress** — This issue is currently being actively worked on by a team member. |

---

## Other Labels

| Label | Color | Purpose |
|-------|-------|---------|
| `documentation` | ![#c5def5](https://placehold.co/12x12/c5def5/c5def5.png) `#c5def5` | **Documentation** — Improvements, additions, or corrections to documentation. |
| `question` | ![#d876e3](https://placehold.co/12x12/d876e3/d876e3.png) `#d876e3` | **Question** — Further information is needed or being requested before this issue can proceed. |

---

## Label Usage Guidelines

- **Multiple labels are encouraged.** For example, a PBI that is currently being worked on should have both `pbi` and `in-progress`.
- **`epic` issues should list related `pbi` issues** in their description as a checklist to track overall progress.
- **`ai-review`** can be applied to any issue — use it to trigger an AI-assisted quality check before the team commits to implementing the work.
- **`risk`** issues should follow the risk management view in GitHub Projects, and include a description of the risk, its likelihood, impact, and mitigation plan.
- **`prototype`** issues should clearly state what is being explored and what the expected output (e.g., a proof of concept, a demo, a decision) looks like.

---

## Setting Up Labels

Labels are automatically created when this template repository is first set up. See the [setup-labels workflow](../.github/workflows/setup-labels.yml) for details. If you need to recreate labels manually, you can re-run the disabled workflow from the **Actions** tab.
