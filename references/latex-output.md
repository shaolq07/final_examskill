# LaTeX Output Rules

Use this reference when producing the final FinalSkill study document.

## Default Artifact Contract

The default final artifacts are:

- `FinalSkill - <stem>.tex`
- `FinalSkill - <stem>.pdf`

The `.pdf` is required when `xelatex` is available. The `.tex` is always required.

## Build Steps

1. Create the output folder `FinalSkill - <stem>`.
2. Write all extraction and planning notes inside that folder.
3. Write `FinalSkill - <stem>.tex`.
4. Run `xelatex -interaction=nonstopmode -halt-on-error "<tex-file>"` from the output folder.
5. Verify the command exit status is success.
6. Verify the PDF exists.
7. If LaTeX fails, inspect the log, fix the source, and retry if the problem is fixable.

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

Use `ctexart` for Chinese-first review documents. Keep the layout single-column and readable by default.

## Required Sections

Every final document should include:

1. `如何使用这份复习资料`
2. `我是如何判断考点的`
3. `材料分类与证据权重`
4. `考题模式总结`
5. `考试地图`
6. `考点复习`
7. `考前速查表`
8. `老师风格练习题`
9. `答案与评分点`
10. `错因诊断`
11. `个性化复习路径`

If the user asks for a narrower artifact, include only relevant sections, but still include `我是如何判断考点的` unless the user explicitly excludes rationale.

When labels are inferred, include `材料分类确认` before `材料分类与证据权重`.

## Required Transparency Section

```latex
\section{我是如何判断考点的}
\begin{itemize}
  \item \textbf{高频依据：} <slides/pages/topics that repeat or receive emphasis>
  \item \textbf{作业依据：} <assignments/labs/problem sets tied to topics>
  \item \textbf{Quiz 依据：} <quiz questions or quiz patterns>
  \item \textbf{往年题依据：} <past-paper questions or recurring formats>
  \item \textbf{推测部分：} <reasonable inference from course structure>
  \item \textbf{不确定部分：} <missing sources, weak evidence, extraction uncertainty>
\end{itemize}
```

When evidence is absent for a category, write `暂无明确材料支持` instead of inventing support.

## Content Style

- Chinese-first for Chinese prompts.
- Put important English terms in parentheses: `中心极限定理 (Central Limit Theorem)`.
- Use source citations inline: `来源：Lecture 4, p. 18`.
- Prefer itemized lists over wide tables.
- Use tables only when they remain readable on A4.
- Keep formulas in math mode.
- Escape special characters from source text: `# $ % & _ { } ~ ^ \`.
- Do not copy large slide text verbatim.

## Completion Gate

Do not report completion unless:

- `.tex` exists.
- `我是如何判断考点的` is present and filled.
- source citations are present where source locations are available.
- material labels are reflected when the user provides or implies labels.
- assessment-pattern summaries are included when assignments, quizzes, or past exams are available.
- every generated question in the final PDF has a `source pattern` or is explicitly marked `inferred`.
- PDF exists, or a missing/failed `xelatex` build is explicitly reported.
- `scripts/validate_review_pack.py` has been run when available, or the final response explains why it could not be run.

## Failure Fallbacks

- Missing `xelatex`: deliver `.tex`, report the missing executable, and do not claim PDF completion.
- Table overflow: convert wide tables to lists or narrower `longtable` columns, then retry.
- Chinese font failure: keep `ctexart`, report the font issue, and avoid Markdown fallback unless requested.
- Formula failure: preserve the raw expression in `working-notes.md`, repair the LaTeX if possible, and mark uncertain formulas in the final document.
- Nonzero compile exit: inspect the log, patch the `.tex`, and retry once when the issue is fixable.
