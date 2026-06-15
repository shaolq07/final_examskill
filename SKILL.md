---
name: finalskill
description: "AI final-exam study system for university courses. Use when Codex needs to transform course PPTs, PDFs, lecture notes, assignments, quizzes, labs, syllabi, rubrics, and past papers into exam-focused study artifacts: structured knowledge maps, concept cards, instructor-style practice questions, model answers, grading rubrics, mistake diagnosis, weak-point remediation, and personalized review schedules. Trigger on requests about finals review, exam preparation, course revision, study packs, mock exams, past-paper analysis, quiz-to-practice conversion, or Chinese-language final review prompts such as qimo fuxi, kaodian zongjie, gainian kapian, wangnian ti, laoshi fengge lianxi ti, pingfen dian, cuoyin zhenduan, and personalized fuxi paths."
---

# FinalSkill

FinalSkill turns messy course material into an exam-oriented review system. Treat the task as building a course-specific exam model, not as summarizing files.

## Core Workflow

1. **Ingest course evidence**
   - Identify file types: syllabus, slides/PDFs, lecture notes, assignments, quizzes, labs, past papers, rubrics, textbook chapters, user notes.
   - Preserve source references by file name and page/slide/question number whenever available.
   - Separate instructor-provided evidence from student notes and model-generated inference.

2. **Build the course exam model**
   - Extract topics, concepts, formulas, methods, cases, definitions, proofs, algorithms, diagrams, and recurring examples.
   - Infer likely exam emphasis from frequency, recency, assignment coverage, quiz coverage, wording intensity, and past-paper recurrence.
   - Classify each item as `Must Know`, `Likely`, `Useful`, or `Low Yield`.

3. **Produce exam artifacts**
   - Make structured knowledge maps and topic dependency graphs.
   - Create concept cards with definition, intuition, conditions, common traps, example, and source.
   - Generate instructor-style practice questions with answers and grading points.
   - Provide scoring rubrics and partial-credit breakdowns.
   - Diagnose mistakes from user answers and map them to root causes.
   - Build a personalized review path by time budget, confidence, and exam date.

4. **Verify against source material**
   - Mark unsupported claims as inference.
   - Do not invent instructor preferences when evidence is absent.
   - If multiple sources conflict, report the conflict and prefer syllabus/rubric/past papers over generic slides.

5. **Deliver in exam-ready form**
   - Prefer compact, scannable outputs: tables, card sets, checklists, mock exams, answer keys.
   - Use bilingual Chinese/English output when the course material or user prompt mixes languages.
   - Include an "Immediate Next Study Action" section unless the user requests a pure artifact.

## Operating Modes

Choose the smallest mode that satisfies the request.

- **Course Pack Mode**: full transformation of course materials into a complete study package.
- **Exam Cram Mode**: high-yield review plan for limited time, usually 1-7 days.
- **Past Paper Mode**: analyze past papers to infer patterns and generate similar questions.
- **Question Factory Mode**: generate practice questions, model answers, and rubrics.
- **Diagnosis Mode**: evaluate user answers, identify root causes, and prescribe targeted drills.
- **Concept Card Mode**: produce concise exam-oriented cards.
- **Study Path Mode**: make a calendar or session-by-session plan.

## Output Standards

Every substantial output should include:

- Source basis: exact files/pages/slides/questions when available.
- Exam relevance: why the item matters for finals.
- Task type: recall, calculation, proof, explanation, comparison, application, case analysis, coding, lab interpretation, essay.
- Difficulty: easy, medium, hard, exam-hard.
- Confidence: high, medium, low, based on source evidence.
- Action: what the student should do next.

## Evidence Rules

- Use course-specific materials over general knowledge.
- Treat past papers, quizzes, assignments, and rubrics as strong evidence for exam style.
- Treat slides with repeated emphasis, learning objectives, boxed definitions, formulas, and summary slides as medium-strong evidence.
- Treat textbook-adjacent expansions as optional unless the instructor explicitly assigned them.
- When evidence is thin, ask for past papers, quizzes, or syllabus only if necessary; otherwise state assumptions and continue.

## Resource Files

Load these only when needed:

- `references/output-patterns.md`: templates for knowledge maps, concept cards, study packs, and mock exams.
- `references/question-design.md`: rules for instructor-style question generation, model answers, and grading rubrics.
- `references/diagnosis-and-planning.md`: mistake taxonomy, remediation drills, and personalized review planning.

Use `scripts/create_review_pack.py` when the user wants files created for a course review package. It creates a clean Markdown folder structure for notes, concept cards, practice questions, rubrics, diagnosis logs, and study plans.

## Default Deliverable Shape

When the user gives course materials and asks broadly for review help, produce:

1. Course exam map
2. High-yield topic table
3. Concept cards
4. Practice set by topic
5. Model answers and grading points
6. Mistake traps and diagnostic checklist
7. Personalized review path

If the user only asks for one artifact, produce only that artifact and keep source references.
