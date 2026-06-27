---
name: finalskill-flashcards
description: "Generate NotebookLM-style flashcards from university course materials. Use when the user asks for flashcards, cards, memorization cards, active recall, spaced repetition, Anki-style cards, cloze cards, concept cards, term-definition cards, or quick review cards from PDFs, slides, lecture notes, or source-derived text. This skill is only for flashcard generation; use finalskill-notes for notes and finalskill-quiz for quizzes."
---

# FinalSkill Flashcards

Generate high-quality active-recall flashcards from course materials. The output should help students remember, distinguish, and apply concepts.

## Required Outcome

Default deliverables:

- an output folder named `Flashcards - <source-or-course-stem>`;
- `flashcards.md` as a readable study deck grouped by topic;
- `flashcards.csv` for import into Anki/Quizlet-like tools;
- `flashcards.tex` and compiled `flashcards.pdf` as a printable deck when `xelatex` is available;
- optional `flashcards.json` when structured downstream processing would help.

Do not produce generic notes. This skill creates cards.

## Workflow

1. **Intake**
   - Determine source files, topic scope, desired number of cards, language, and card style.
   - Default language is Chinese-first with English technical terms in parentheses.
   - Default card mix: term-definition, concept check, cloze deletion, comparison, formula use, and trap cards.

2. **Read globally first**
   - Identify course structure and segment by lecture/topic.
   - For long PDFs, segment before card generation to avoid missing later sections.
   - Keep page/slide references for card sources.

3. **Extract card-worthy knowledge**
   - Extract definitions, formulas, conditions, distinctions, methods, examples, and misconceptions.
   - Avoid cards for trivial slide headings or overly broad paragraphs.
   - Each card should test one atomic idea.

4. **Generate cards**
   - Produce a balanced deck by topic and difficulty.
   - Include easy recall, medium application, and hard discrimination cards.
   - Use cloze cards for formulas, definitions, sequences, conditions, and named theorems.
   - Use comparison cards for easily confused concepts.
   - Use trap cards for common mistakes.
   - Organize the readable deck by topic with short, scannable cards that students would actually review.
   - For printable output, make each card visually separated with front/back labels and enough whitespace for annotation.

5. **Verify deck quality**
   - Remove duplicates and near-duplicates.
   - Split cards that test multiple ideas.
   - Check that answers are concise but complete.
   - Check source citations where available.

## Card Schema

Every card should include:

```text
id:
topic:
type: basic | cloze | comparison | formula | application | trap
difficulty: easy | medium | hard
front:
back:
source:
tags:
```

For cloze cards, use this style:

```text
front: 中心极限定理 (Central Limit Theorem) 说明，当 n 足够大时，样本均值近似服从 {{c1::正态分布}}。
back: 条件、含义、常见误区。
```

## CSV Export

When writing `flashcards.csv`, use columns:

```text
id,topic,type,difficulty,front,back,source,tags
```

Escape commas, quotes, and newlines correctly. Keep the CSV UTF-8 encoded.

## Readable / Printable Output

`flashcards.md` should be pleasant to read:

```markdown
## Topic

### Card FC001 · basic · easy

**Front**
...

**Back**
...

**Source**
...
```

For `flashcards.tex` / `flashcards.pdf`, use a simple printable layout:

- grouped by topic;
- one card block per concept;
- visible `Front` and `Back`;
- optional difficulty/type labels;
- no dense tables;
- enough spacing for handwritten notes.

If PDF compilation is unavailable, still deliver Markdown and CSV.

## Output Rules

- Prefer active recall over passive summary.
- One card, one idea.
- Avoid vague fronts such as "Explain this slide".
- Include source page/slide references when available.
- Do not invent facts not supported by source material.
- If source extraction is uncertain, mark the card source as `uncertain` or omit the card.
