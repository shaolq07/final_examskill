# Study Materials Workflow

Use this reference when the user wants FinalSkill to directly create review materials from slides, PDFs, notes, quizzes, assignments, or past papers.

## Required Behavior

Do not stop at a chat-only summary unless the user explicitly asks for inline output only. Create a LaTeX source file and compiled PDF by default. Markdown may be used for internal working notes, but it is not the final deliverable unless the user explicitly requests Markdown.

Default output folder:

```text
FinalSkill - <course-or-source-stem>/
```

Keep all generated notes, drafts, extracted text, question banks, answer keys, PDFs, LaTeX files, and logs in that folder.

## Default Study Material Set

| File | Purpose |
| --- | --- |
| `FinalSkill - <stem>.tex` | Final LaTeX study document |
| `FinalSkill - <stem>.pdf` | Compiled PDF final deliverable |
| `working-notes.md` | Internal extraction notes and draft planning |
| `sources.md` | Source inventory and coverage map |

## Global Read and Segmentation

For every substantial course file:

1. Read enough to identify the macro-structure.
2. Segment by lecture, chapter, topic, page range, assignment, quiz, or past-paper section.
3. Create per-segment notes before merging.
4. Ensure every segment is represented or explicitly excluded.

Segment notes should contain:

- segment id
- source page/slide/question range
- main exam points
- formulas and methods
- key concepts with English terms
- examples or problem patterns
- traps and likely mistakes
- coverage uncertainty

If the segment is an assignment, quiz, or past exam, also extract:

- question type
- tested knowledge point
- command verb
- answer format
- mark allocation if available
- transformation opportunity for new practice questions

## Final Review Notes Template

```latex
\section{如何使用这份复习资料}
\begin{itemize}
  \item <highest priority action>
  \item <what to memorize>
  \item <what to practice>
\end{itemize}

\section{我是如何判断考点的}
\begin{itemize}
  \item \textbf{高频依据：} <repeated slides/topics with citations>
  \item \textbf{作业依据：} <assignments/labs with citations>
  \item \textbf{Quiz 依据：} <quiz evidence with citations>
  \item \textbf{往年题依据：} <past paper evidence with citations>
  \item \textbf{推测部分：} <inferred priorities and why>
  \item \textbf{不确定部分：} <gaps, weak evidence, or extraction uncertainty>
\end{itemize}

\section{考试地图}
<readable table or bullet list>

\section{<Unit or Topic>}
\subsection{核心考点}
\begin{itemize}
  \item \textbf{<point>}：<concise explanation>. 来源：<file/page/slide>.
\end{itemize}

\subsection{关键术语}
\begin{itemize}
  \item \textbf{Chinese term (English term)}：<definition and exam use>.
\end{itemize}

\subsection{公式 / 方法}
\begin{itemize}
  \item \textbf{<formula or method>}：<conditions, steps, and trap>. 来源：<file/page/slide>.
\end{itemize}
```

## Exam Cheat Sheet Template

```latex
\section{考前速查表}

\subsection{必背定义}
<compact list or table>

\subsection{公式与适用条件}
<compact list or table>

\subsection{解题流程}
<compact list or table>

\subsection{最后检查的易错点}
<compact list or table>
```

## Required Transparency Section

Every final `.tex` document must include:

```latex
\section{我是如何判断考点的}
\begin{itemize}
  \item \textbf{高频依据：}
  \item \textbf{作业依据：}
  \item \textbf{Quiz 依据：}
  \item \textbf{往年题依据：}
  \item \textbf{推测部分：}
  \item \textbf{不确定部分：}
\end{itemize}
```

If a category has no evidence, write `暂无明确材料支持` and explain the consequence.

## LaTeX Build Requirements

- Use `xelatex` by default.
- Use UTF-8 source.
- Include Chinese font support through `ctexart`.
- Keep layout readable; do not force dense two-column output unless requested.
- Escape LaTeX special characters from source text.
- Use citations like `来源：Lecture 3, p. 12` or `来源：Quiz 2, Q4`.

## Verification Gate

Before reporting completion, verify:

- all major segments are represented
- user-provided material labels are reflected in source analysis
- assessment-pattern summary is present when assignments, quizzes, or past exams are provided
- generated questions cite their source pattern
- citations exist for major points when source locations are available
- formulas are not missing from formula-heavy sections
- important English terms are present
- practice questions match course evidence
- the final `.tex` exists in the output folder
- the PDF exists if `xelatex` is available and compilation succeeds
- `我是如何判断考点的` is present and filled
- any uncertainty is reported explicitly

## PDF Output

PDF is default.

1. Write a `.tex` version of the review notes or cheat sheet.
2. Check that `xelatex` is available.
3. Compile with `xelatex`.
4. Verify the PDF exists and the compile command succeeded.

If `xelatex` is missing, report the blocker and provide the `.tex` file as the deliverable. Do not silently downgrade to Markdown.
