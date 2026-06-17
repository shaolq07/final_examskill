# Assessment Reconstruction

Use this reference for material labeling, exam-pattern analysis, practice-question generation, model answers, and grading rubrics.

## Core Principle

Separate **content sources** from **assessment sources**:

- slides and lecture notes explain what was taught;
- assignments show practiced methods and transformable problem structures;
- quizzes show compact testable concepts, distractors, and wording traps;
- past exams show exam structure, difficulty, repeated patterns, and time pressure;
- rubrics show how points are awarded.

## Material Classification

Recommended user input:

```text
slides:
- Lecture 1.pdf

assignment:
- HW1.pdf

quiz:
- Quiz 1.pdf

past_exam:
- 2024 Final.pdf

rubric:
- Final rubric.pdf
```

If labels are inferred, produce a confirmation section:

```latex
\section{材料分类确认}
\begin{itemize}
  \item \textbf{课件 / slides：} ...
  \item \textbf{作业 / assignment：} ...
  \item \textbf{Quiz：} ...
  \item \textbf{历年题 / past\_exam：} ...
  \item \textbf{Rubric / syllabus / notes：} ...
  \item \textbf{待确认：} ...
\end{itemize}
```

Ask the user to classify ambiguous assessment files before final question generation.

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

## Stage 1: Assessment Pattern Summary

Before generating questions, write:

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

## Stage 2: Question Generation

Generate questions only after the assessment-pattern summary exists.

Question layers:

1. **基础保分题**: direct recall, formula use, or one-step explanation.
2. **作业变形题**: assignment-style methods with changed numbers, context, or conditions.
3. **Quiz 风格快测题**: short diagnostic questions with likely traps.
4. **历年题复现题**: analogous questions that preserve topic, reasoning path, and difficulty without copying exact wording.

Every question must include:

- `source pattern`: assignment, quiz, past_exam, slide, or inferred;
- `tested knowledge point`;
- `difficulty`: easy, medium, hard, exam-hard;
- `answer`;
- `grading points`;
- `common wrong answer`;
- `follow-up drill`.

If the source pattern is weak, write `source pattern: inferred from <evidence>` and explain why. Do not include unsupported questions in the final PDF.

## Question Types

| Type | Use When | Include |
| --- | --- | --- |
| Recall | definitions, formulas, classifications | precise expected wording |
| Explain | mechanisms, intuition, tradeoffs | key terms and causal links |
| Compare | similar concepts or methods | comparison dimensions |
| Calculate | numeric/formula tasks | givens, units, steps, final value |
| Prove/derive | math, algorithms, theory | assumptions and logical sequence |
| Apply | case/lab/design/coding scenario | constraints, data, expected reasoning |
| Debug/diagnose | code, labs, proofs, calculations | symptoms, cause, fix |
| Essay | humanities/social science/business | thesis, evidence, counterpoint |

## Model Answer and Rubric

Use this structure:

```latex
\paragraph{答案}
<solution>

\paragraph{评分点}
\begin{itemize}
  \item <mark allocation>: <criterion>
\end{itemize}

\paragraph{常见错误}
<mistake and why it loses marks>

\paragraph{补救练习}
<follow-up drill>
```

Rubric rules:

- grade observable reasoning, not vague quality;
- give partial credit for correct setup;
- separate conceptual, condition, arithmetic, wording, and notation errors;
- for essays, grade thesis, course concepts, evidence, reasoning, counterargument, and organization;
- for code, grade correctness, edge cases, complexity, readability, and explanation.

## Anti-Copy Rule

Do not copy exact past-exam wording unless the user explicitly asks for verbatim extraction. Generate analogous questions that preserve structure, tested concept, and difficulty.
