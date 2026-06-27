# FinalSkill Skill Pack

FinalSkill is now a small pack of three independent Codex/Claude Code skills for studying course materials:

```text
finalskill-notes/       Generate concise study notes from slides or PDFs.
finalskill-flashcards/  Generate NotebookLM-style active-recall flashcards.
finalskill-quiz/        Generate quizzes, practice tests, answers, and rubrics.
```

The old all-in-one workflow has been removed. Each skill is intentionally vertical, so the assistant can choose the right task from the user's intent:

- "整理这份课件 / make notes" -> `finalskill-notes`
- "生成 flashcards / Anki cards / 记忆卡片" -> `finalskill-flashcards`
- "出题 / generate quiz / mock test / practice questions" -> `finalskill-quiz`

## Install From GitHub

Clone the repository:

```bash
git clone https://github.com/shaolq07/final_examskill.git
```

Then copy or symlink the three skill folders into your local skills directory.

### Codex

Example on Windows:

```powershell
mkdir D:\Codex\.codex\skills\finalskill-notes
mkdir D:\Codex\.codex\skills\finalskill-flashcards
mkdir D:\Codex\.codex\skills\finalskill-quiz

Copy-Item -Recurse final_examskill\finalskill-notes\* D:\Codex\.codex\skills\finalskill-notes\
Copy-Item -Recurse final_examskill\finalskill-flashcards\* D:\Codex\.codex\skills\finalskill-flashcards\
Copy-Item -Recurse final_examskill\finalskill-quiz\* D:\Codex\.codex\skills\finalskill-quiz\
```

### Claude Code

Personal skills usually live under:

```bash
~/.claude/skills/
```

Install:

```bash
mkdir -p ~/.claude/skills
cp -R final_examskill/finalskill-notes ~/.claude/skills/
cp -R final_examskill/finalskill-flashcards ~/.claude/skills/
cp -R final_examskill/finalskill-quiz ~/.claude/skills/
```

## Skill 1: FinalSkill Notes

Use for:

- lecture notes;
- slide summaries;
- course PDF summaries;
- exam-oriented study notes;
- formula/concept cheat sheets.

Default output is a LaTeX/PDF study document when possible.

Example prompt:

```text
Use $finalskill-notes to turn Lecture 1-6 PDFs into Chinese-first study notes.
```

## Skill 2: FinalSkill Flashcards

Use for:

- NotebookLM-style flashcards;
- active recall cards;
- Anki/Quizlet-style CSV cards;
- printable flashcard PDF decks;
- cloze deletion cards;
- formula cards;
- misconception/trap cards.

Default outputs:

```text
flashcards.md
flashcards.csv
flashcards.tex
flashcards.pdf
```

Example prompt:

```text
Use $finalskill-flashcards to generate 80 active-recall flashcards from these slides.
```

## Skill 3: FinalSkill Quiz

Use for:

- quizzes;
- mock tests;
- practice questions;
- answer keys;
- grading points;
- teacher-style question generation.

Default outputs:

```text
quiz.pdf
quiz.tex
quiz.md
answer-key.pdf
answer-key.tex
answer-key.md
```

Example prompt:

```text
Use $finalskill-quiz to generate a 30-question mixed mock paper PDF with answers from these lecture PDFs.
```

## Design Principle

The three skills follow the same reliable document-processing pattern inspired by strong slide-summary workflows:

```text
1. read globally
2. segment by lecture/topic
3. extract task-specific material
4. generate the artifact
5. verify coverage and source references
6. write files, and compile PDF when requested/available
```

No task should include unnecessary meta-explanation. Notes should start with useful learning content; flashcards should start with cards; quizzes should start with questions.
