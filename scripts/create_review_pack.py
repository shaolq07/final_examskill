#!/usr/bin/env python3
"""Create a FinalSkill review pack folder with Markdown placeholders."""

from __future__ import annotations

import argparse
from pathlib import Path


FILES = {
    "00-exam-brief.md": "# Exam Brief\n\n## Course Snapshot\n\n## Exam Assumptions\n\n## Immediate Priorities\n",
    "01-topic-map.md": "# Topic Map\n\n| Unit | Core Concepts | Exam Tasks | Evidence | Priority | Confidence |\n| --- | --- | --- | --- | --- | --- |\n",
    "02-concept-cards.md": "# Concept Cards\n\n## Unit 1\n\n### Concept: \n\n- **Exam role**: \n- **Definition**: \n- **Intuition**: \n- **Conditions**: \n- **Procedure/Formula**: \n- **Mini example**: \n- **Common trap**: \n- **Source**: \n- **Priority**: \n",
    "03-practice-bank.md": "# Practice Bank\n\n## Easy\n\n## Medium\n\n## Hard\n\n## Exam-hard\n",
    "04-answer-key-and-rubrics.md": "# Answer Key and Rubrics\n\n## Question 1\n\n### Answer\n\n### Key Grading Points\n",
    "05-mistake-log.md": "# Mistake Log\n\n| Date | Question | Lost Marks | Root Cause | Fix | Re-test |\n| --- | --- | --- | --- | --- | --- |\n",
    "06-review-path.md": "# Review Path\n\n## Inputs\n\n## Session Plan\n\n## Final 24 Hours\n",
    "sources.md": "# Sources\n\n| File | Pages/Slides/Questions Used | Notes |\n| --- | --- | --- |\n",
}


def slugify(value: str) -> str:
    cleaned = "".join(ch.lower() if ch.isalnum() else "-" for ch in value.strip())
    parts = [part for part in cleaned.split("-") if part]
    return "-".join(parts) or "course-review"


def main() -> None:
    parser = argparse.ArgumentParser(description="Create a FinalSkill review pack.")
    parser.add_argument("course", help="Course name, e.g. CS101")
    parser.add_argument("--output", "-o", default=".", help="Parent output directory")
    args = parser.parse_args()

    root = Path(args.output).expanduser().resolve() / f"{slugify(args.course)}-finalskill-pack"
    root.mkdir(parents=True, exist_ok=True)

    for filename, content in FILES.items():
        path = root / filename
        if not path.exists():
            path.write_text(content, encoding="utf-8")

    print(root)


if __name__ == "__main__":
    main()
