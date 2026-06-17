---
name: finalskill
description: "FinalSkill is an AI final-exam study system for university courses. Use when Codex needs to turn labeled course materials such as slides, lecture PDFs, assignments, quizzes, rubrics, syllabi, and past exams into a Chinese-first LaTeX/PDF final review pack with exam-point notes, assessment-pattern analysis, practice questions, model answers, grading points, mistake diagnosis, and a personalized review path. Trigger on finals review, exam preparation, study materials, review notes, cheat sheets, mock exams, past-paper analysis, quiz-to-practice conversion, assignment-to-exam transformations, or Chinese prompts such as qimo fuxi, fuxi ziliao, kaodian zongjie, gongshi suzha, laoshi fengge lianxi ti, pingfen dian, cuoyin zhenduan."
---

# FinalSkill

FinalSkill builds an exam-oriented review pack from course evidence. Treat the work as modeling both **what was taught** and **how it is assessed**, not as generic PDF summarization.

## Required Outcome

Default successful output:

- `FinalSkill - <stem>.tex`
- `FinalSkill - <stem>.pdf`, when `xelatex` is available
- `sources.md` with file labels and source coverage
- optional `working-notes.md` for extraction notes, uncertainty, and raw formulas

Place all generated files inside one folder named `FinalSkill - <course-or-source-stem>` unless the user specifies another location. A chat-only summary is not a successful completion unless the user explicitly requests inline output only.

## Best Input Format

For best results, ask the user to label materials:

```text
slides:
- Lecture 1.pdf
- Lecture 2.pdf

assignment:
- HW1.pdf
- HW2.pdf

quiz:
- Quiz 1.pdf

past_exam:
- 2023 Final.pdf
- 2024 Final.pdf

rubric:
- final-rubric.pdf

syllabus:
- syllabus.pdf
```

If labels are missing, infer only obvious labels from filenames. When important assessment files are ambiguous, ask for classification before final question generation.

## Core Workflow

1. **Intake and material classification**
   - Classify each file as `slides`, `assignment`, `quiz`, `past_exam`, `rubric`, `syllabus`, `notes`, or `unknown`.
   - Produce a material classification confirmation when labels are inferred.
   - Treat user labels as the primary source of truth.
   - Keep source references by file name, page, slide, and question number.

2. **Build the content map from teaching materials**
   - Use slides, lecture notes, syllabus, and textbook references to extract concepts, formulas, definitions, examples, methods, diagrams, and scope.
   - For long PDFs, read globally first, segment by lecture/topic/page range, then merge segment notes.
   - Do not drop later sections because of length.

3. **Build the assessment map from assessment materials**
   - Use assignments, quizzes, past exams, and rubrics to identify question structures, command verbs, mark allocation, recurring topic combinations, traps, and scoring preferences.
   - Weight evidence: past exams and rubrics strongest; quizzes and assignments strong; syllabus medium-strong; slides medium; personal notes low unless confirmed.
   - Summarize assessment patterns before generating questions.

4. **Generate the LaTeX review document**
   - Include: how to use the pack, material classification, `我是如何判断考点的`, assessment-pattern summary, exam map, core review notes, cheat sheet, practice questions, model answers, grading points, mistake diagnosis, and review path.
   - Default language is Chinese-first with important English terms in parentheses.
   - Every major point should include source citations when available.
   - Every generated question must include a `source pattern`; omit questions that have no evidence basis unless explicitly marked as inferred.

5. **Verify before building**
   - Check topic coverage, source citations, bilingual terminology, formula integrity, material labels, and question `source pattern` fields.
   - Mark unsupported claims as inference.
   - Report uncertainty instead of inventing instructor preferences.

6. **Build and validate**
   - Use `xelatex` to compile the PDF.
   - Run `scripts/validate_review_pack.py` when a review pack exists.
   - If `xelatex` is missing or compilation fails, deliver the `.tex` file and clearly report the blocker; do not claim PDF completion.

## Modes

- **Study Materials Mode**: default mode for slides/PDFs; produce a LaTeX/PDF review pack.
- **Assessment Reconstruction Mode**: use labeled assignments, quizzes, and past exams to summarize exam patterns and reproduce important knowledge points as practice questions.
- **Past Paper Mode**: analyze past papers to infer repeated structures and generate analogous questions without copying exact wording.
- **Question Factory Mode**: generate practice questions, model answers, grading points, and remediation drills.
- **Diagnosis Mode**: evaluate user answers and prescribe targeted remediation.
- **Cram Plan Mode**: create 1-day, 3-day, or 7-day review paths.

## Resource Files

Load only the needed reference:

- `references/study-materials.md`: final review pack content structure and writing rules.
- `references/assessment-reconstruction.md`: material labeling, assessment-pattern extraction, question generation, answer/rubric rules.
- `references/diagnosis-and-planning.md`: mistake taxonomy, diagnosis format, and review planning.
- `references/latex-output.md`: LaTeX layout, build procedure, failure fallbacks, and completion gate.

Use scripts:

- `scripts/create_review_pack.py`: create the LaTeX-first output folder and starter files.
- `scripts/validate_review_pack.py`: validate required sections, source labels, question source patterns, and optional PDF existence.

## Completion Standard

Do not report completion until:

- the `.tex` file exists;
- the PDF exists, or the missing/failed PDF build is explicitly reported;
- `sources.md` records file labels;
- `我是如何判断考点的` is filled;
- assessment questions include `source pattern`;
- validation has run or any inability to run validation is reported.
