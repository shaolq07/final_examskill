# LaTeX Output

Use this reference for artifact creation, layout, compilation, and final validation.

## Default Artifact Contract

The final artifacts are:

- `FinalSkill - <stem>.tex`
- `FinalSkill - <stem>.pdf`, when `xelatex` is available
- `sources.md`
- optional `working-notes.md`

All generated files must live inside `FinalSkill - <stem>/`.

## Recommended Preamble

```latex
\documentclass[UTF8,12pt]{ctexart}
\usepackage[a4paper,margin=2cm]{geometry}
\usepackage{amsmath,amssymb}
\usepackage{booktabs,longtable,array}
\usepackage{enumitem}
\usepackage{hyperref}
\hypersetup{colorlinks=true,linkcolor=blue,urlcolor=blue}
\setlength{\tabcolsep}{3pt}
\setlist[itemize]{leftmargin=2em,itemsep=0.2em}
\setlist[enumerate]{leftmargin=2em,itemsep=0.2em}
```

Use Chinese-first text for Chinese prompts and include English terms in parentheses.

## Build Steps

1. Create the output folder before extraction or drafting.
2. Write working notes and source inventory inside that folder.
3. Write `FinalSkill - <stem>.tex`.
4. Check `xelatex` availability.
5. Run `xelatex -interaction=nonstopmode -halt-on-error "<tex-file>"` from the output folder.
6. Verify successful exit status and PDF existence.
7. Run `scripts/validate_review_pack.py`, using `--require-pdf` when PDF output is expected.

## Failure Fallbacks

- Missing `xelatex`: deliver `.tex`, report the missing engine, and do not claim PDF completion.
- Table overflow or layout warnings: convert wide tables to itemized lists or narrower columns, then retry.
- Chinese font failure: report the font/engine issue; do not silently downgrade to Markdown.
- Formula failure: preserve the raw expression in `working-notes.md`, repair if possible, and flag uncertain formulas in the final document.
- Nonzero compile exit: inspect the log, patch the `.tex`, and retry once when fixable.

## Completion Gate

Do not report completion unless:

- `.tex` exists;
- PDF exists or PDF build blocker is explicitly reported;
- `sources.md` exists and includes a `Label` column;
- `我是如何判断考点的` is present and filled;
- material labels are reflected;
- assessment questions include `source pattern`;
- validation has run, or the final response explains why validation could not run.
