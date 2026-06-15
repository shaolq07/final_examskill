# Study Materials Workflow

Use this reference when the user wants FinalSkill to directly create review materials from slides, PDFs, notes, quizzes, assignments, or past papers.

## Required Behavior

Do not stop at a chat-only summary unless the user explicitly asks for inline output only. Create saved study-material files by default.

Default output folder:

```text
FinalSkill - <course-or-source-stem>/
```

Keep all generated notes, drafts, extracted text, question banks, answer keys, and logs in that folder.

## Default Study Material Set

| File | Purpose |
| --- | --- |
| `final-review-notes.md` | Main exam-oriented review notes, Chinese-first when appropriate |
| `exam-cheat-sheet.md` | Fast lookup sheet for formulas, definitions, procedures, traps |
| `concept-cards.md` | One card per examinable concept |
| `practice-bank.md` | Instructor-style questions by topic and difficulty |
| `answer-key-and-rubrics.md` | Model answers, marking points, partial credit |
| `mistake-log.md` | Root-cause diagnosis and remediation |
| `review-path.md` | Personalized study sessions |
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

## Final Review Notes Template

```markdown
# Final Review Notes: <course>

## How To Use This

- <highest priority action>
- <what to memorize>
- <what to practice>

## Exam Map

| Unit | Must Know | Likely Tasks | Source | Priority |
| --- | --- | --- | --- | --- |

## <Unit or Topic>

### Core Exam Points

- **<point>**: <concise explanation>. Source: <file/page/slide>.

### Key Terms

- **Chinese term (English term)**: <definition and exam use>.

### Formulas / Procedures

- **<formula or method>**: <conditions, steps, and trap>. Source: <file/page/slide>.

### Representative Examples

- **Pattern**: <what the exam may ask>.
- **Solution idea**: <how to approach it>.

### Common Traps

- <trap>: <how to avoid it>.
```

## Exam Cheat Sheet Template

```markdown
# Exam Cheat Sheet: <course>

## Must-Memorize Definitions

| Concept | Exam wording | Trap | Source |
| --- | --- | --- | --- |

## Formulas and Conditions

| Formula | Use When | Do Not Use When | Source |
| --- | --- | --- | --- |

## Procedures

| Task | Steps | Check | Source |
| --- | --- | --- | --- |

## Last-Minute Traps

| Trap | Symptom | Fix |
| --- | --- | --- |
```

## Verification Gate

Before reporting completion, verify:

- all major segments are represented
- citations exist for major points when source locations are available
- formulas are not missing from formula-heavy sections
- important English terms are present
- practice questions match course evidence
- generated files exist in the output folder
- any uncertainty is reported explicitly

## Optional PDF Output

If the user asks for PDF:

1. Write a `.tex` version of the review notes or cheat sheet.
2. Check that `xelatex` is available.
3. Compile with `xelatex`.
4. Verify the PDF exists and the compile command succeeded.

If `xelatex` is missing, report the blocker and keep the Markdown files as the completed fallback unless the user required PDF only.
