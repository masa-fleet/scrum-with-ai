#!/usr/bin/env python3
"""Create GitHub issues from the Markdown files under .github/setup-issues/.

Each Markdown file has YAML frontmatter with a required `title` field. The
issue body is the remainder of the file after the frontmatter block.

By default all files in the setup-issues directory are processed. Use
--only to process a single file (basename), or --exclude to skip one or
more files (basename) while processing the rest.
"""

import argparse
import glob
import os
import re
import subprocess
import sys

try:
    import yaml
except ImportError:
    print("PyYAML not found, installing...")
    subprocess.run([sys.executable, "-m", "pip", "install", "pyyaml", "-q"], check=True)
    import yaml

ISSUES_DIR = ".github/setup-issues"


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--only",
        action="append",
        default=[],
        help="Only process this file (basename, e.g. github-project-board.md). "
             "May be given multiple times.",
    )
    parser.add_argument(
        "--exclude",
        action="append",
        default=[],
        help="Skip this file (basename, e.g. github-project-board.md). "
             "May be given multiple times.",
    )
    return parser.parse_args()


def select_files(only, exclude):
    files = sorted(glob.glob(os.path.join(ISSUES_DIR, "*.md")))

    if only:
        only_set = set(only)
        files = [f for f in files if os.path.basename(f) in only_set]
    if exclude:
        exclude_set = set(exclude)
        files = [f for f in files if os.path.basename(f) not in exclude_set]

    return files


def create_issues(files):
    if not files:
        print(f"No Markdown files to process in {ISSUES_DIR}, skipping.")
        return

    for filepath in files:
        print(f"Processing: {filepath}")
        content = open(filepath, encoding="utf-8").read()

        # Parse frontmatter
        fm_match = re.match(r"^---\s*\n(.*?)\n---\s*\n", content, re.DOTALL)
        if not fm_match:
            print(f"  Warning: No frontmatter found in {filepath}, skipping.")
            continue

        metadata = yaml.safe_load(fm_match.group(1))
        title = (metadata or {}).get("title", "").strip()
        if not title:
            print(f"  Warning: No title found in frontmatter of {filepath}, skipping.")
            continue

        body = content[fm_match.end():]
        body = expand_repository_placeholders(body)

        # Check for existing issue with the same title (open or closed)
        result = subprocess.run(
            ["gh", "issue", "list",
             "--search", f'"{title}" in:title',
             "--state", "all",
             "--json", "number",
             "--jq", ".[0].number // empty"],
            capture_output=True, text=True, check=True
        )
        if result.stdout.strip():
            print(f"  Issue already exists (#{result.stdout.strip()}): {title!r}, skipping.")
            continue

        # Create the issue
        create = subprocess.run(
            ["gh", "issue", "create",
             "--title", title,
             "--body", body,
             "--label", "pbi",
             "--label", "setup"],
            capture_output=True, text=True
        )
        if create.returncode == 0:
            print(f"  ✅ Created issue: {title!r}")
        else:
            print(f"  ❌ Failed to create issue: {title!r}")
            print(create.stderr)
            sys.exit(1)

    print("✅ All setup issues processed.")


def expand_repository_placeholders(body):
    server_url = os.environ.get("GITHUB_SERVER_URL", "https://github.com").rstrip("/")
    repository = os.environ.get("GITHUB_REPOSITORY", "").strip()
    if not repository:
        raise RuntimeError("GITHUB_REPOSITORY environment variable is not set")

    repo_blob_main = f"{server_url}/{repository}/blob/main"
    return body.replace("{{REPO_BLOB_MAIN}}", repo_blob_main)


def main():
    args = parse_args()
    files = select_files(args.only, args.exclude)
    if args.only and not files:
        print(f"No setup issue templates matched --only: {', '.join(args.only)}")
        sys.exit(1)
    create_issues(files)


if __name__ == "__main__":
    main()
