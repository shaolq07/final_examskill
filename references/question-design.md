# Question Design, Answers, and Rubrics

Use this reference when generating practice questions, mock exams, answer keys, or grading points.

## Instructor-Style Generation

Infer style from:

- Past paper wording and section structure.
- Quiz question stems and distractors.
- Assignment tasks and marking schemes.
- Repeated verbs in learning objectives: define, compare, derive, compute, prove, analyze, critique, design, implement.
- The instructor's preferred examples, diagrams, datasets, cases, or code patterns.

If no past assessments exist, generate standard university final-style questions and clearly mark style as inferred.

## Assessment-Aware Question Generation

When labeled assignments, quizzes, and past exams are available, do not generate questions directly from slides alone. First create an assessment-pattern map:

- past exams: section structure, repeated topics, difficulty, time pressure, mark allocation
- assignments: method templates, multi-step procedures, transformation opportunities
- quizzes: short-answer wording, distractors, common misconceptions
- rubrics: scoring requirements and partial-credit rules

Then generate questions that reproduce important knowledge points through assessment-like formats:

- `基础保分题`: direct concept checks
- `作业变形题`: homework-style method transformations
- `Quiz 风格快测题`: concise diagnostic questions
- `历年题复现题`: exam-like problems preserving structure and difficulty without copying exact wording

Every generated question should state its `source pattern`, such as `based on HW2 Q3 method`, `similar to Quiz 1 conceptual trap`, or `past_exam pattern inferred from 2024 Final Q2`.

## Question Types

| Type | Use When | Include |
| --- | --- | --- |
| Recall | Definitions, formulas, classifications | precise expected wording |
| Explain | Mechanisms, intuition, tradeoffs | key terms and causal links |
| Compare | Similar concepts or methods | dimensions of comparison |
| Calculate | Formulas, numerical methods, finance, stats, physics | givens, units, steps, final value |
| Prove/derive | Math, algorithms, theory | assumptions, logical sequence |
| Apply | Case/lab/design/coding scenario | constraints, data, expected reasoning |
| Debug/diagnose | Code, lab reports, proofs, calculations | symptoms, likely cause, fix |
| Essay | Humanities/social science/business | thesis, evidence, counterpoint |

## Difficulty Calibration

- **Easy**: one concept, direct recall or one-step application.
- **Medium**: combines two concepts or requires method selection.
- **Hard**: multi-step reasoning, edge cases, or distractors.
- **Exam-hard**: integrates units, mimics past-paper complexity, includes partial-credit opportunities.

## Model Answer Format

Use this shape:

```markdown
### Answer

1. <Step or claim>
2. <Step or claim>
3. <Final result or conclusion>

**Key grading points**
- <mark allocation>: <criterion>
- <mark allocation>: <criterion>

**Common wrong answer**
- <mistake>: <why it loses marks>
```

## Rubric Rules

- Allocate marks to observable reasoning, not vague quality.
- Include partial credit for correct setup even if final answer is wrong.
- Penalize missing assumptions, wrong units, invalid theorem conditions, unsupported claims, and arithmetic/coding errors separately.
- For essays, grade thesis, course concept use, evidence, reasoning, counterargument, and organization.
- For code, grade correctness, edge cases, complexity, readability, and explanation if required.

## Distractor Design

Good distractors should correspond to real student mistakes:

- Confusing similar definitions.
- Applying a formula outside its conditions.
- Reversing cause and effect.
- Dropping a boundary case.
- Using memorized wording without the required reasoning.
- Making a common algebra, unit, sign, indexing, or probability error.

Do not create trick questions unrelated to course emphasis.
