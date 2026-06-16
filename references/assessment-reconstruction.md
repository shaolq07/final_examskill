# Assessment Reconstruction

Use this reference when the user wants stronger question generation from labeled course materials, especially assignments, quizzes, and past exams.

## Core Principle

Good question generation depends on separating content sources from assessment sources.

- Slides and lecture notes explain what was taught.
- Assignments show what methods students were expected to practice.
- Quizzes show compact concepts and common traps.
- Past exams show final-exam structure, difficulty, and repeated patterns.
- Rubrics show how answers are scored.

Ask the user to label materials when labels are missing and filenames are ambiguous.

## Recommended User Input Format

```text
slides:
- Lecture 1.pdf
- Lecture 2.pdf

assignment:
- HW1.pdf
- HW2.pdf

quiz:
- Quiz 1.pdf
- Quiz 2.pdf

past_exam:
- 2023 Final.pdf
- 2024 Final.pdf

rubric:
- Final rubric.pdf
```

If the user provides unlabeled files, infer obvious labels from filenames. If assessment files are unclear, ask for classification before producing the final PDF.

## Evidence Weighting

| Source Type | Use | Weight |
| --- | --- | --- |
| past_exam | exam structure, recurring topics, difficulty, wording | highest |
| rubric | grading points, required answer components | highest |
| quiz | short concepts, traps, teacher wording | high |
| assignment | practiced methods, transformations, multi-step patterns | high |
| syllabus | official scope and learning outcomes | medium-high |
| slides | definitions, formulas, examples, concept coverage | medium |
| notes | personal weak points and extra context | low unless confirmed |

## Assessment Pattern Summary

Before generating questions, produce a concise pattern summary:

```latex
\section{考题模式总结}
\begin{itemize}
  \item \textbf{题型结构：} <sections, marks, question types>
  \item \textbf{高频问法：} <recurring stems or command verbs>
  \item \textbf{作业到考试的变形：} <how homework methods become exam tasks>
  \item \textbf{Quiz 常见陷阱：} <distractors or short-answer traps>
  \item \textbf{历年题重复模式：} <topic and reasoning patterns>
  \item \textbf{评分偏好：} <rubric-derived scoring expectations>
\end{itemize}
```

## Knowledge-Point Reproduction

For each S/A-level concept, generate at least one reproduction question that retests the knowledge point in an exam-like form.

Question layers:

1. `基础保分题`: direct recall, formula use, or one-step explanation.
2. `作业变形题`: structurally based on assignment methods, with changed numbers/context/conditions.
3. `Quiz 风格快测题`: short diagnostic questions with likely traps.
4. `历年题复现题`: similar topic, reasoning path, and difficulty to past exams without copying exact wording.

Each question should include:

- `source pattern`: assignment, quiz, past_exam, slide, or inferred
- `tested knowledge point`
- `difficulty`: easy, medium, hard, exam-hard
- `answer`
- `grading points`
- `common wrong answer`
- `follow-up drill`

## Anti-Copy Rule

Do not copy exact past exam wording unless the user explicitly asks for verbatim extraction. Generate analogous questions that preserve structure, tested concept, and difficulty.

## When Labels Are Missing

Use this fallback:

1. Infer labels from obvious filenames.
2. Put ambiguous files in `unknown`.
3. Ask the user to classify `unknown` files if they are likely assessments.
4. If the user cannot classify them, continue but mark all question-style conclusions from those files as low confidence.
