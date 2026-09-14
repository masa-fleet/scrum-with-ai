---
name: create-pbi
description: Create and register a GitHub Project PBI from a short request.
---

# Create PBI

Create a PBI from the user's request and register it in the linked GitHub Project.

## Instructions

1. Read `.github/ISSUE_TEMPLATE/pbi.yml` and use its field descriptions as the source of truth.
2. Read only the repository files needed to understand the request. Check existing Issues for duplicates.
3. Resolve the repository owner/name with `gh repo view --json nameWithOwner`.
4. Resolve the Project linked to the repository with GraphQL (`repository.projectsV2`). Do not hard-code Project IDs.
5. Ask only for missing information required to write a useful PBI. Otherwise, draft the title and body.
6. Show the draft and ask for one confirmation before creating anything.
7. After confirmation:
   - Create the Issue with `gh issue create --label pbi`.
   - Add it to the linked Project with `gh project item-add`.
   - Set the requested Sprint and `New` Status using Project field names and option values.
8. Report the Issue URL and the final Project fields. If a mutation fails, report the error and do not claim completion.

Keep the response and generated PBI concise. Do not copy the PBI field guidance into this Skill; maintain it in `.github/ISSUE_TEMPLATE/pbi.yml`.
