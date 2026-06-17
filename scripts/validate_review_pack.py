#!/usr/bin/env python3
"""Validate a FinalSkill LaTeX review pack."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


REQUIRED_SECTIONS = [
    "材料分类确认",
    "材料分类与证据权重",
    "我是如何判断考点的",
    "考题模式总结",
    "考试地图",
    "核心考点复习",
    "考前速查表",
    "老师风格练习题",
    "答案与评分点",
    "错因诊断",
    "个性化复习路径",
]


def find_tex(pack: Path) -> Path | None:
    matches = sorted(pack.glob("FinalSkill - *.tex"))
    if matches:
        return matches[0]
    matches = sorted(pack.glob("*.tex"))
    return matches[0] if matches else None


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate a FinalSkill review pack.")
    parser.add_argument("pack", help="Path to a FinalSkill output folder")
    parser.add_argument("--require-pdf", action="store_true", help="Fail if PDF is missing")
    args = parser.parse_args()

    pack = Path(args.pack).expanduser().resolve()
    failures: list[str] = []

    if not pack.exists() or not pack.is_dir():
        print(f"FAIL: review pack folder does not exist: {pack}")
        return 1

    tex = find_tex(pack)
    if tex is None:
        failures.append("missing final .tex file")
        tex_text = ""
    else:
        tex_text = tex.read_text(encoding="utf-8")
        for section in REQUIRED_SECTIONS:
            if section not in tex_text:
                failures.append(f"missing required section: {section}")
        if "source pattern" not in tex_text:
            failures.append("missing mandatory question source pattern marker")

    sources = pack / "sources.md"
    if not sources.exists():
        failures.append("missing sources.md")
    else:
        source_text = sources.read_text(encoding="utf-8")
        if "Label" not in source_text:
            failures.append("sources.md must include a Label column")

    if args.require_pdf:
        if tex is None:
            failures.append("cannot infer PDF path because .tex is missing")
        elif not tex.with_suffix(".pdf").exists():
            failures.append(f"missing compiled PDF: {tex.with_suffix('.pdf').name}")

    if failures:
        print("FinalSkill review pack validation failed:")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print(f"FinalSkill review pack is valid: {pack}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
