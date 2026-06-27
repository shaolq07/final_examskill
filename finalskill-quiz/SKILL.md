---
name: finalskill-quiz
description: "Generate quizzes and practice tests from university course materials. Use when the user asks for quiz questions, mock tests, practice problems, self-tests, exam-style questions, multiple choice, short answer, calculation questions, model answers, answer keys, rubrics, or teacher-style practice from PDFs, slides, assignments, quizzes, past exams, or source-derived text. This skill is only for quiz generation; use finalskill-notes for notes and finalskill-flashcards for flashcards."
---

# FinalSkill Quiz

Generate focused quizzes and practice tests from course materials. The goal is retrieval practice and exam readiness, not generic summarization.

## Required Outcome

Default deliverables:

- an output folder named `Quiz - <source-or-course-stem>`;
- `quiz.tex` and compiled `quiz.pdf` as the main student-facing mock paper;
- `quiz.md` as an editable backup version;
- `answer-key.md` with model answers, scoring points, and explanations;
- optional `answer-key.tex` / `answer-key.pdf` if the user wants a printable answer key.

Do not generate notes or flashcards unless the user explicitly asks to switch tasks.

## Workflow

1. **Intake**
   - Determine source materials, topic scope, number of questions, difficulty, quiz format, and whether answers should be hidden.
   - If the user provides assignments, prior quizzes, or past exams, treat them as style evidence.
   - If only slides are provided, generate source-grounded study quizzes and mark exam-style claims as inferred.

2. **Read globally first**
   - Identify course structure and segment by lecture/topic.
   - Extract concepts, formulas, methods, examples, and likely misconceptions.
   - Preserve page/slide/question references.

3. **Build a quiz blueprint**
   - Decide question distribution by topic and difficulty.
   - Build the student-facing quiz like a real mock paper with sections, points, timing, and instructions.
   - Mix question types: multiple choice, fill-in-the-blank/cloze, true/false with correction, short answer, compare/contrast, calculation/data interpretation, application/case analysis, diagram/process ordering, proof/derive, debug/diagnose when relevant.
   - If assessment materials exist, imitate structure and difficulty without copying exact wording.

4. **Generate questions**
   - Each question should test a clear knowledge point.
   - Include realistic distractors for multiple-choice questions.
   - Include enough information for calculation/application questions.
   - Avoid trick questions unrelated to the course material.
   - The student-facing quiz must show only question numbers, point values, and question text. Do not show metadata such as `source pattern`, `tested knowledge point`, or `difficulty` in the student-facing quiz/PDF.

5. **Generate answer key**
   - Provide final answer, reasoning, grading points, and common wrong answer.
   - For calculation questions, include setup, units, intermediate steps, and final result.
   - For essays, include thesis expectations and evidence criteria.

6. **Verify**
   - Check coverage against the blueprint.
   - Check answers for consistency with the source.
   - Check difficulty labels.
   - Check that question wording is clear and unambiguous.

## Question Schema

Every question should include:

```text
id:
topic:
type:
difficulty:
source pattern:
question:
answer:
grading points:
common wrong answer:
follow-up drill:
```

`source pattern` is internal metadata for generation and the answer key. Do not print it in the student-facing quiz. It can be:

- `slide`: generated from lecture content;
- `assignment`: transformed from homework method;
- `quiz`: inspired by quiz wording or trap;
- `past_exam`: analogous to past-exam structure;
- `inferred`: generated from course structure when no assessment source exists.

## Quiz Formats

Support:

- quick check: 5-10 questions;
- topic quiz: one unit/topic;
- mixed review: balanced across units;
- mock exam: timed sections with marks and exam-style instructions;
- weak-point drill: focused on user mistakes.

## Mock Paper Layout

Default section design:

```text
Course / Topic
Time:
Total Points:
Instructions:

Section A: Multiple Choice
Section B: Fill-in-the-blank / True-False Correction
Section C: Short Answer and Concept Explanation
Section D: Application / Data / Diagram / Calculation
Section E: Integrated Challenge
```

Adapt sections to the course. Life science courses should include process ordering, mechanism explanation, compare/contrast, and application questions when appropriate.

## Anti-Copy Rule

Do not copy exact past-exam wording unless the user explicitly requests verbatim extraction. Generate analogous questions that preserve tested concept, structure, and difficulty.
