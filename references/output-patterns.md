# FinalSkill Output Patterns

Use these templates for exam-oriented artifacts. Adapt headings to the course language.

## Course Exam Map

| Unit | Core Concepts | Exam Task Types | Evidence | Priority | Confidence |
| --- | --- | --- | --- | --- | --- |
| Unit name | Key ideas, formulas, methods | Explain/calculate/prove/apply | file:page or slide | Must Know/Likely/Useful/Low Yield | High/Medium/Low |

After the table, add:

- **Dependency chain**: prerequisite concepts before later topics.
- **Exam bottlenecks**: topics where one misunderstanding damages many question types.
- **Fastest marks**: high-probability, low-time topics.

## Concept Card

Use one card per examinable concept.

```markdown
### Concept: <name>

- **Exam role**: Why this appears in finals.
- **Definition**: Precise definition in course wording.
- **Intuition**: One plain-language explanation.
- **Conditions**: When it applies and when it does not.
- **Procedure/Formula**: Steps, formula, or decision rule.
- **Mini example**: One short exam-style example.
- **Common trap**: Likely mistake and how to avoid it.
- **Source**: file/page/slide/question.
- **Priority**: Must Know/Likely/Useful/Low Yield.
```

## High-Yield Topic Table

| Topic | Why It Is High Yield | What To Memorize | What To Practice | Trap | Source |
| --- | --- | --- | --- | --- | --- |

Use "why" fields tied to evidence: repeated in slides, used in assignment, appears in quiz, highlighted in syllabus, or recurring in past papers.

## Complete Study Pack

Recommended structure:

1. **LaTeX/PDF final review document**: the main study material, organized by exam topic.
2. **Exam cheat sheet section**: formulas, definitions, procedures, traps, and citations.
3. **Executive exam brief**: 10-20 bullets, no fluff.
4. **Topic priority map**: table sorted by priority.
5. **Concept cards**: grouped by unit.
6. **Question bank**: easy -> medium -> exam-hard.
7. **Mock exam**: timed, with marks per question.
8. **Answer key**: final answers plus reasoning.
9. **Rubric**: partial-credit criteria.
10. **Mistake log**: root cause, fix, drill.
11. **Review path**: daily/session plan.

## Direct Review Notes

When the user asks for study materials from slides or PDFs, create a saved `.tex` file and compiled PDF by default.

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

\section{考试地图}
<high-yield table or list with source citations>

\section{<Topic>}
\begin{itemize}
  \item \textbf{考点：} <concise explanation>. 来源：<file/page/slide>.
  \item \textbf{公式 / 方法：} <conditions and steps>. 来源：<file/page/slide>.
  \item \textbf{典型问法：} <representative exam pattern>.
  \item \textbf{易错点：} <likely mistake and fix>.
\end{itemize}
```

## Mock Exam

```markdown
# Mock Exam: <course>

Time: <minutes>
Total: <marks>
Allowed materials: <if known, otherwise assumptions>

## Section A: Core Concepts
<short-answer questions>

## Section B: Application / Calculation / Proof
<multi-step questions>

## Section C: Integration
<case, essay, design, coding, or synthesis question>
```

Balance the mock exam according to evidence from past papers, quizzes, assignments, and stated learning outcomes.

## Source Confidence Labels

- **High**: directly supported by past papers, rubric, syllabus objective, quiz, assignment, or repeated instructor emphasis.
- **Medium**: supported by slides/notes and plausible exam relevance.
- **Low**: inferred from general course logic or adjacent material.
