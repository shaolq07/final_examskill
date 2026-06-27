---
name: finalskill-notes
description: "Generate study notes from university course materials. Use when the user wants course PDFs, slides, lecture notes, or source-derived text turned into clean exam-oriented notes, review sheets, cheat sheets, formula/concept summaries, or a LaTeX/PDF learning document. This skill is only for note generation and content organization; use finalskill-flashcards for flashcards and finalskill-quiz for quizzes."
---

# FinalSkill Notes

Turn course materials into concise, source-cited study notes. Do not explain how priorities were judged unless the user asks. Start with useful learning content.

## Required Outcome

Default deliverables:

- a dedicated output folder named `Notes - <source-or-course-stem>`;
- `Notes - <source-or-course-stem>.tex`;
- compiled `Notes - <source-or-course-stem>.pdf` when `xelatex` is available;
- any extracted text, OCR dumps, verifier notes, or helper files kept inside the same output folder.

A chat-only summary is not a successful completion unless the user explicitly asks for inline output only.

## Workflow

1. **Intake**
   - Determine source path(s), output name, full deck vs subset, and language preference.
   - Default language is Chinese-first with important English terms in parentheses.
   - If source files are PDFs, use reliable PDF extraction/OCR workflows available in the environment.
   - Create the output folder before writing any intermediate files.

2. **Read globally first**
   - Identify document structure: lectures, chapters, topic separators, examples, summary pages, formula-heavy sections.
   - For long materials, build a segmentation map before detailed extraction.
   - Cover all pages/sections exactly once unless explicitly excluded.

3. **Segment extraction**
   - Process each lecture/topic segment independently.
   - Extract concepts, formulas, definitions, methods, examples, problem-solving techniques, diagrams that matter, and common traps.
   - Preserve source page/slide references.

4. **Merge into notes**
   - Organize by topic, not page-by-page narration.
   - Prefer short bullets, formula boxes, compact examples, and "when to use" cues.
   - Include formulas, conditions, representative examples, and practical solving hints when they matter.
   - Do not include filler such as "我是如何判断重点的" unless requested.

5. **Verify**
   - Check that every segment is represented or intentionally excluded.
   - Check page/slide citations on important points.
   - Check formulas, bilingual terminology, and readability.
   - If extraction quality is too poor for formulas or page mapping, report the uncertainty.

6. **Build**
   - Write LaTeX with `ctexart` and compile using `xelatex`.
   - If `xelatex` is missing, deliver `.tex` and report the blocker.
   - Do not claim PDF completion unless compilation succeeds and the PDF exists.

## Output Style

The notes should usually contain:

- quick usage guide;
- topic map;
- core concepts;
- formulas and conditions;
- representative examples;
- common traps;
- concise cheat sheet;
- source references.

Keep the document readable. Do not force dense two-column formatting unless the user asks.

## LaTeX Guidance

Use a clean preamble:

```latex
\documentclass[UTF8,12pt]{ctexart}
\usepackage[a4paper,margin=2cm]{geometry}
\usepackage{amsmath,amssymb}
\usepackage{booktabs,longtable,array}
\usepackage{enumitem}
\usepackage{hyperref}
\hypersetup{colorlinks=true,linkcolor=blue,urlcolor=blue}
```

Prefer lists over wide tables. Escape LaTeX special characters from source text.
