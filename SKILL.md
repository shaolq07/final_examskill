---
name: finalskill
description: "AI final-exam study system for university courses. Use when Codex needs to transform course PPTs, PDFs, lecture notes, assignments, quizzes, labs, syllabi, rubrics, and past papers into concrete exam-focused LaTeX/PDF study materials: final review notes, cheat sheets, structured knowledge maps, concept cards, instructor-style practice questions, model answers, grading rubrics, mistake diagnosis, weak-point remediation, and personalized review schedules. Trigger on requests about finals review, exam preparation, course revision, study materials, study packs, review notes, cheat sheets, mock exams, past-paper analysis, quiz-to-practice conversion, or Chinese-language final review prompts such as qimo fuxi, fuxi ziliao, kaodian zongjie, gongshi suzha, gainian kapian, wangnian ti, laoshi fengge lianxi ti, pingfen dian, cuoyin zhenduan, and personalized fuxi paths."
---

# FinalSkill

FinalSkill turns messy course material into an exam-oriented review system. Treat the task as building a course-specific exam model, not as summarizing files.

## Default Outcome

When the user provides course materials and asks for review, summary, exam prep, or study materials, the successful default outcome is a saved LaTeX source file and compiled PDF study document, not only an inline chat answer and not Markdown as the final format.

Create a deterministic output folder named `FinalSkill - <course-or-source-stem>` unless the user specifies another location. Keep generated notes, extracted text, drafts, practice sets, answer keys, and logs inside that folder.

Default files:

- `FinalSkill - <course-or-source-stem>.tex`: final Chinese-first LaTeX study document.
- `FinalSkill - <course-or-source-stem>.pdf`: compiled PDF, required by default.
- `sources.md`: source inventory and coverage map.
- optional `working-notes.md`: internal extraction and planning notes, not the final deliverable.

Check that `xelatex` is available before promising the default PDF. If `xelatex` is unavailable, write the `.tex` file, report the PDF build blocker, and do not pretend the PDF was created. Only fall back to Markdown final output if the user explicitly asks for Markdown.

## Best User Input Protocol

For best results, ask the user to provide or confirm material labels before final generation:

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

If the user uploads unlabeled files, first produce a short `Material Classification Confirmation` summary and ask for confirmation only when important files are ambiguous. Do not proceed to final question generation from an ambiguous pile of files when assessment files may be mixed with slides.

## Core Workflow

1. **Ingest course evidence**
   - Identify file types: syllabus, slides/PDFs, lecture notes, assignments, quizzes, labs, past papers, rubrics, textbook chapters, user notes.
   - Ask the user to label materials as `slides`, `assignment`, `quiz`, `past_exam`, `rubric`, `syllabus`, or `notes` when labels are missing and filenames do not make the type obvious.
   - Treat user-provided labels as the primary source of truth for material type.
   - Produce a material classification confirmation pass before final generation whenever labels are inferred or ambiguous.
   - Preserve source references by file name and page/slide/question number whenever available.
   - Separate instructor-provided evidence from student notes and model-generated inference.
   - Do not mix slides and assessments into one generic source bucket; slides explain content, while assignments, quizzes, and past exams reveal question style.

2. **Read globally and segment**
   - For long slide decks or PDFs, first identify the global structure, then segment by lecture, chapter, topic, or page range.
   - Cover all provided material exactly once unless a section is intentionally excluded.
   - Create segment notes before writing the final merged study material.

3. **Build the course exam model**
   - Extract topics, concepts, formulas, methods, cases, definitions, proofs, algorithms, diagrams, and recurring examples.
   - Infer likely exam emphasis from frequency, recency, assignment coverage, quiz coverage, wording intensity, and past-paper recurrence.
   - Weight evidence by source type: past exams and rubrics strongest, quizzes and assignments strong, syllabus objectives medium-strong, slides medium, student notes weak unless confirmed.
   - Classify each item as `Must Know`, `Likely`, `Useful`, or `Low Yield`.
   - Build a question-pattern map from assignments, quizzes, and past exams before generating new questions.

4. **Produce exam artifacts**
   - Write a final LaTeX document and compile it to PDF by default.
   - Include final review notes, exam cheat sheet, concept cards, practice questions, answer key, rubrics, mistake diagnosis, and review path in the same PDF unless the user requests a smaller artifact.
   - Include an assessment-pattern summary: recurring question types, command verbs, mark allocation, topic combinations, and common transformations from homework to exam questions.
   - Generate questions in two stages: first write the assessment-pattern summary, then generate practice questions from that summary.
   - Generate knowledge-point reproduction questions that re-test important concepts in forms similar to assignments, quizzes, and past exams.
   - Every generated question must include a `source pattern`; do not include questions without a source pattern in the final PDF.
   - Make structured knowledge maps and topic dependency graphs.
   - Create concept cards with definition, intuition, conditions, common traps, example, and source.
   - Generate instructor-style practice questions with answers and grading points.
   - Provide scoring rubrics and partial-credit breakdowns.
   - Diagnose mistakes from user answers and map them to root causes.
   - Build a personalized review path by time budget, confidence, and exam date.

5. **Verify against source material**
   - Run a coverage pass before finalizing files.
   - Check that every major lecture/topic segment appears in the final materials.
   - Check that formulas, key examples, English technical terms, and page/slide citations are present where available.
   - Check that the document contains a section named `我是如何判断考点的`.
   - Mark unsupported claims as inference.
   - Do not invent instructor preferences when evidence is absent.
   - If multiple sources conflict, report the conflict and prefer syllabus/rubric/past papers over generic slides.

6. **Deliver in exam-ready form**
   - Prefer compact, scannable outputs: tables, card sets, checklists, mock exams, answer keys.
   - Use Chinese-first output by default for Chinese prompts, with important English terms in parentheses.
   - Include an "Immediate Next Study Action" section unless the user requests a pure artifact.

## Operating Modes

Choose the smallest mode that satisfies the request.

- **Course Pack Mode**: full transformation of course materials into a complete study package.
- **Study Materials Mode**: default mode for slides/PDFs; produce a compiled LaTeX/PDF final review document with citations.
- **Exam Cram Mode**: high-yield review plan for limited time, usually 1-7 days.
- **Past Paper Mode**: analyze past papers to infer patterns and generate similar questions.
- **Question Factory Mode**: generate practice questions, model answers, and rubrics.
- **Assessment Reconstruction Mode**: use labeled assignments, quizzes, and past exams to summarize question patterns and reproduce important knowledge points in exam-like practice.
- **Diagnosis Mode**: evaluate user answers, identify root causes, and prescribe targeted drills.
- **Concept Card Mode**: produce concise exam-oriented cards.
- **Study Path Mode**: make a calendar or session-by-session plan.

## Output Standards

Every substantial output should include:

- Source basis: exact files/pages/slides/questions when available.
- Material label: slides, assignment, quiz, past_exam, rubric, syllabus, notes, or inferred.
- Transparent priority rationale: include `我是如何判断考点的` with high-frequency evidence, assignment evidence, quiz evidence, past-paper evidence, inferred parts, and uncertainty.
- Exam relevance: why the item matters for finals.
- Task type: recall, calculation, proof, explanation, comparison, application, case analysis, coding, lab interpretation, essay.
- Difficulty: easy, medium, hard, exam-hard.
- Confidence: high, medium, low, based on source evidence.
- Action: what the student should do next.

## Study-Material Writing Rules

- Default to Chinese-first prose for Chinese users; keep important terms, distributions, theorems, formulas, methods, and named concepts in English parentheses.
- Do not produce a generic chapter summary when the request is exam review.
- Each major point should include source page, slide, or question references when available.
- Include formulas, key concepts, representative examples, problem-solving techniques, and common traps.
- Keep bullets concise and readable. Do not over-compress into an unreadable cheat-sheet layout.
- For long decks, do not write the final notes until global segmentation and per-segment extraction are done.
- If extraction quality is too poor to preserve formulas, symbols, or page mapping, report the uncertainty instead of inventing math.
- If source-derived diagrams are essential, describe or redraw the minimal conceptual diagram; do not add decorative visuals.

## Material Labeling Rules

For best results, encourage the user to separate or label inputs before generation:

```text
slides: Lecture 1.pdf, Lecture 2.pdf
assignment: HW1.pdf, HW2.pdf
quiz: Quiz1.pdf, Quiz2.pdf
past_exam: 2023-final.pdf, 2024-midterm.pdf
rubric: final-rubric.pdf
syllabus: syllabus.pdf
notes: my-notes.pdf
```

If labels are missing:

- Infer labels from filenames only when obvious, such as `HW`, `assignment`, `quiz`, `past paper`, `final`, `midterm`, `exam`, `lecture`, `slides`, or `syllabus`.
- If important files remain ambiguous, ask the user to identify them before generating final questions.
- Continue with explicit uncertainty only when the user cannot provide labels.

Use source types differently:

- **Slides**: extract concepts, formulas, definitions, examples, and scope.
- **Assignments**: identify practiced methods, multi-step procedures, common transformations, and teacher-preferred problem forms.
- **Quizzes**: identify concise testable concepts, distractors, and short-answer wording.
- **Past exams**: identify final-exam structure, recurring topics, difficulty, time pressure, and mark allocation.
- **Rubrics**: identify scoring points and partial-credit expectations.
- **Syllabus**: identify official learning outcomes and included/excluded units.

## Question-Reconstruction Rules

Use a two-stage workflow. Stage 1 summarizes the assessment evidence; Stage 2 generates questions from that summary.

Stage 1 must summarize:

- recurring question formats
- command verbs such as define, explain, calculate, compare, derive, prove, analyze, design
- topic combinations that appear together
- how homework problems are transformed into quiz or exam questions
- common answer length and mark allocation
- common traps or distractors

Stage 2 generates questions in four layers:

1. **基础保分题**: direct recall or one-step application from high-priority concepts.
2. **作业变形题**: modify homework structures while preserving the tested method.
3. **Quiz 风格快测题**: short, discriminative questions that expose concept gaps.
4. **历年题复现题**: exam-like questions that reproduce topic, reasoning path, and difficulty without copying exact past exam wording.

For each generated question, include:

- source pattern: assignment, quiz, past exam, slide, or inferred; this field is mandatory
- tested knowledge point
- difficulty
- model answer
- grading points
- common wrong answer
- remediation drill

If the source pattern cannot be identified, either mark it as `inferred` with a reason or omit the question from the final PDF.

## Transparency Section

Every final study document must include this section, even when evidence is sparse:

```markdown
## 我是如何判断考点的

- 高频依据：
- 作业依据：
- Quiz 依据：
- 往年题依据：
- 推测部分：
- 不确定部分：
```

For each bullet, fill in course-specific evidence with file/page/slide/question references when available. If a category has no evidence, write `暂无明确材料支持` and explain whether the priority is inferred from course structure.

## LaTeX/PDF Rules

- The final deliverable is LaTeX plus PDF by default.
- Use `xelatex` for Chinese text and math.
- Use a clean article-style layout, readable spacing, and sectioned structure.
- Keep Chinese as the main language for Chinese prompts and put important English terms in parentheses.
- Use LaTeX tables sparingly; prefer readable lists when tables become too wide.
- Escape LaTeX special characters in extracted text.
- Do not report completion until the `.tex` file exists and `xelatex` either succeeded or failed with a clearly reported blocker.
- If compilation fails, fix the `.tex` and retry when the failure is fixable.
- If `xelatex` is missing, deliver the `.tex` file and explicitly report that the PDF build is blocked by a missing LaTeX engine.
- If tables overflow or cause layout warnings, convert them to itemized lists before retrying.
- If Chinese font support fails, keep the `.tex`, report the font/engine issue, and do not downgrade to Markdown unless the user asks.
- If a formula causes compilation failure, preserve the original source formula in `working-notes.md`, repair the LaTeX expression if possible, and flag uncertain formulas in the final document.

## Evidence Rules

- Use course-specific materials over general knowledge.
- Treat past papers, quizzes, assignments, and rubrics as strong evidence for exam style.
- Treat slides with repeated emphasis, learning objectives, boxed definitions, formulas, and summary slides as medium-strong evidence.
- Treat textbook-adjacent expansions as optional unless the instructor explicitly assigned them.
- When evidence is thin, ask for past papers, quizzes, or syllabus only if necessary; otherwise state assumptions and continue.

## Resource Files

Load these only when needed:

- `references/output-patterns.md`: templates for knowledge maps, concept cards, study packs, and mock exams.
- `references/study-materials.md`: default file-producing workflow for final review notes and cheat sheets.
- `references/latex-output.md`: LaTeX/PDF layout, required sections, build steps, and completion gate.
- `references/question-design.md`: rules for instructor-style question generation, model answers, and grading rubrics.
- `references/assessment-reconstruction.md`: material labeling, assessment pattern extraction, and knowledge-point reproduction.
- `references/diagnosis-and-planning.md`: mistake taxonomy, remediation drills, and personalized review planning.

Use `scripts/create_review_pack.py` when the user wants files created for a course review package or when course materials are provided and no output folder exists yet. It creates a LaTeX-first review pack with a final `.tex` template, source inventory, and working-notes file.
Use `scripts/validate_review_pack.py` before final reporting when a review pack exists. It checks required LaTeX sections, source labels, source-pattern requirements, and PDF presence.

## Default Deliverable Shape

When the user gives course materials and asks broadly for review help, produce:

1. Saved LaTeX final review document
2. Compiled PDF final review document
3. Transparent `我是如何判断考点的` section
4. Course exam map
5. High-yield topic table
6. Concept cards
7. Practice set by topic
8. Model answers and grading points
9. Mistake traps and diagnostic checklist
10. Personalized review path

If the user only asks for one artifact, produce only that artifact as a LaTeX/PDF file and keep source references.
