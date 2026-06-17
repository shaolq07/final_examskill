# FinalSkill

FinalSkill is a Codex skill for university final-exam review. It turns labeled course materials into a Chinese-first LaTeX/PDF review pack with exam-point notes, assessment-pattern analysis, practice questions, model answers, grading points, mistake diagnosis, and a personalized review path.

It is not a generic PDF summarizer. FinalSkill separates **what was taught** from **how it is assessed**:

- `slides` / lecture notes explain concepts, formulas, definitions, and scope.
- `assignment` files reveal practiced methods and homework-to-exam transformations.
- `quiz` files reveal short-answer wording, traps, and common misconceptions.
- `past_exam` files reveal exam structure, repeated patterns, and difficulty.
- `rubric` files reveal scoring criteria and partial-credit expectations.
- `syllabus` files confirm official scope and learning outcomes.

## What It Generates

By default, FinalSkill creates a LaTeX-first review pack:

```text
FinalSkill - <course>/
  FinalSkill - <course>.tex
  FinalSkill - <course>.pdf
  sources.md
  working-notes.md
```

The final PDF is designed to include:

- how to use the review pack
- material classification and evidence weighting
- `我是如何判断考点的`
- assessment-pattern summary
- exam map
- core topic review notes
- exam cheat sheet
- teacher-style practice questions
- model answers and grading points
- mistake diagnosis
- personalized review path

## Recommended Input Format

For best results, label files before asking FinalSkill to generate the pack:

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

If labels are missing, FinalSkill can infer obvious labels from filenames, but ambiguous assessment files should be confirmed before final question generation.

## Question Generation

FinalSkill uses a two-stage question workflow:

1. **Assessment-pattern summary**
   - question structure
   - high-frequency prompts
   - homework-to-exam transformations
   - quiz traps
   - repeated past-exam patterns
   - grading preferences

2. **Practice-question generation**
   - 基础保分题
   - 作业变形题
   - Quiz 风格快测题
   - 历年题复现题

Every generated question should include:

- `source pattern`
- `tested knowledge point`
- `difficulty`
- `answer`
- `grading points`
- `common wrong answer`
- `follow-up drill`

## Skill Structure

```text
SKILL.md
agents/
  openai.yaml
references/
  study-materials.md
  assessment-reconstruction.md
  diagnosis-and-planning.md
  latex-output.md
scripts/
  create_review_pack.py
  validate_review_pack.py
```

### Key Files

- `SKILL.md`: lightweight entrypoint, trigger description, core workflow, completion standard.
- `references/study-materials.md`: review-pack content structure and writing rules.
- `references/assessment-reconstruction.md`: material labeling, assessment-pattern analysis, question generation, answers, and rubrics.
- `references/diagnosis-and-planning.md`: mistake taxonomy, remediation, and cram plans.
- `references/latex-output.md`: LaTeX/PDF build rules, fallback behavior, and completion gate.
- `scripts/create_review_pack.py`: creates a LaTeX-first review-pack folder.
- `scripts/validate_review_pack.py`: checks required sections, source labels, question source patterns, and optional PDF presence.

## Create a Review-Pack Skeleton

```bash
python scripts/create_review_pack.py "CS101" --output .
```

This creates:

```text
FinalSkill - cs101/
  FinalSkill - cs101.tex
  sources.md
  working-notes.md
```

## Validate a Review Pack

```bash
python scripts/validate_review_pack.py "FinalSkill - cs101"
```

Require the compiled PDF:

```bash
python scripts/validate_review_pack.py "FinalSkill - cs101" --require-pdf
```

## Compile the PDF

FinalSkill expects `xelatex` for Chinese text and math:

```bash
cd "FinalSkill - cs101"
xelatex -interaction=nonstopmode -halt-on-error "FinalSkill - cs101.tex"
```

If `xelatex` is missing, FinalSkill should still produce the `.tex` file and clearly report that PDF generation is blocked.

## Current Design Principle

FinalSkill follows this pipeline:

```text
1. classify materials
2. build content map from slides
3. build assessment map from assignments/quizzes/past exams
4. generate LaTeX review document and questions
5. verify coverage, citations, and source patterns
6. compile and validate PDF
```

The goal is not just to summarize course material, but to help students understand:

- what to review
- why it is likely important
- how the instructor may test it
- how to answer for marks
- what mistakes to avoid
