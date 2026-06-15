---
name: finalskill
description: "AI final-exam study system for university courses. Use when Codex needs to transform course PPTs, PDFs, lecture notes, assignments, quizzes, labs, syllabi, rubrics, and past papers into concrete exam-focused study materials and files: final review notes, cheat sheets, structured knowledge maps, concept cards, instructor-style practice questions, model answers, grading rubrics, mistake diagnosis, weak-point remediation, and personalized review schedules. Trigger on requests about finals review, exam preparation, course revision, study materials, study packs, review notes, cheat sheets, mock exams, past-paper analysis, quiz-to-practice conversion, or Chinese-language final review prompts such as qimo fuxi, fuxi ziliao, kaodian zongjie, gongshi suzha, gainian kapian, wangnian ti, laoshi fengge lianxi ti, pingfen dian, cuoyin zhenduan, and personalized fuxi paths."
---

# FinalSkill

FinalSkill turns messy course material into an exam-oriented review system. Treat the task as building a course-specific exam model, not as summarizing files.

## Default Outcome

When the user provides course materials and asks for review, summary, exam prep, or study materials, the successful default outcome is saved study-material files, not only an inline chat answer.

Create a deterministic output folder named `FinalSkill - <course-or-source-stem>` unless the user specifies another location. Keep generated notes, extracted text, drafts, practice sets, answer keys, and logs inside that folder.

Default files:

- `final-review-notes.md`: Chinese-first exam review notes with English terms in parentheses.
- `exam-cheat-sheet.md`: compact formulas, definitions, procedures, traps, and page/slide citations.
- `concept-cards.md`: exam-oriented concept cards.
- `practice-bank.md`: instructor-style questions by topic and difficulty.
- `answer-key-and-rubrics.md`: model answers and grading points.
- `mistake-log.md`: diagnosis table and remediation drills.
- `review-path.md`: personalized study sessions and cram plan.
- `sources.md`: source inventory and coverage map.

If the user explicitly asks for PDF output, write a `.tex` file and compile with `xelatex` when available. If `xelatex` is unavailable, report that blocker and still provide the Markdown study-material files unless the user required PDF only.

## Core Workflow

1. **Ingest course evidence**
   - Identify file types: syllabus, slides/PDFs, lecture notes, assignments, quizzes, labs, past papers, rubrics, textbook chapters, user notes.
   - Preserve source references by file name and page/slide/question number whenever available.
   - Separate instructor-provided evidence from student notes and model-generated inference.

2. **Read globally and segment**
   - For long slide decks or PDFs, first identify the global structure, then segment by lecture, chapter, topic, or page range.
   - Cover all provided material exactly once unless a section is intentionally excluded.
   - Create segment notes before writing the final merged study material.

3. **Build the course exam model**
   - Extract topics, concepts, formulas, methods, cases, definitions, proofs, algorithms, diagrams, and recurring examples.
   - Infer likely exam emphasis from frequency, recency, assignment coverage, quiz coverage, wording intensity, and past-paper recurrence.
   - Classify each item as `Must Know`, `Likely`, `Useful`, or `Low Yield`.

4. **Produce exam artifacts**
   - Write final review notes and cheat sheets as files by default.
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
- **Study Materials Mode**: default mode for slides/PDFs; produce saved final review notes and cheat sheets with citations.
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

## Study-Material Writing Rules

- Default to Chinese-first prose for Chinese users; keep important terms, distributions, theorems, formulas, methods, and named concepts in English parentheses.
- Do not produce a generic chapter summary when the request is exam review.
- Each major point should include source page, slide, or question references when available.
- Include formulas, key concepts, representative examples, problem-solving techniques, and common traps.
- Keep bullets concise and readable. Do not over-compress into an unreadable cheat-sheet layout.
- For long decks, do not write the final notes until global segmentation and per-segment extraction are done.
- If extraction quality is too poor to preserve formulas, symbols, or page mapping, report the uncertainty instead of inventing math.
- If source-derived diagrams are essential, describe or redraw the minimal conceptual diagram; do not add decorative visuals.

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
- `references/question-design.md`: rules for instructor-style question generation, model answers, and grading rubrics.
- `references/diagnosis-and-planning.md`: mistake taxonomy, remediation drills, and personalized review planning.

Use `scripts/create_review_pack.py` when the user wants files created for a course review package or when course materials are provided and no output folder exists yet. It creates a clean Markdown folder structure for final review notes, cheat sheets, concept cards, practice questions, rubrics, diagnosis logs, and study plans.

## Default Deliverable Shape

When the user gives course materials and asks broadly for review help, produce:

1. Saved final review notes
2. Saved exam cheat sheet
3. Course exam map
4. High-yield topic table
5. Concept cards
6. Practice set by topic
7. Model answers and grading points
8. Mistake traps and diagnostic checklist
9. Personalized review path

If the user only asks for one artifact, produce only that artifact as a saved file and keep source references.
