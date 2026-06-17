#!/usr/bin/env python3
"""Create a FinalSkill LaTeX-first review pack folder."""

from __future__ import annotations

import argparse
from pathlib import Path


FILES = {
    "working-notes.md": "# Working Notes\n\n## Segmentation Map\n\n## Extracted Evidence\n\n## Uncertainty\n",
    "sources.md": "# Sources\n\n| File | Label | Pages/Slides/Questions Used | Notes |\n| --- | --- | --- | --- |\n",
}


TEX_TEMPLATE = r"""\documentclass[UTF8,12pt]{ctexart}
\usepackage[a4paper,margin=2cm]{geometry}
\usepackage{amsmath,amssymb}
\usepackage{booktabs,longtable,array}
\usepackage{enumitem}
\usepackage{hyperref}
\hypersetup{colorlinks=true,linkcolor=blue,urlcolor=blue}
\setlength{\tabcolsep}{3pt}
\setlist[itemize]{leftmargin=2em,itemsep=0.2em}
\setlist[enumerate]{leftmargin=2em,itemsep=0.2em}

\title{FinalSkill 期末复习资料：__COURSE__}
\author{FinalSkill}
\date{\today}

\begin{document}
\maketitle
\tableofcontents
\newpage

\section{如何使用这份复习资料}
\begin{itemize}
  \item 先看材料分类、考点判断依据和考试地图，再进入具体考点。
  \item 对 S/A 级考点，优先掌握定义、条件、公式、典型问法和易错点。
  \item 做完练习题后，用答案与评分点自评，再进入错因诊断和复习路径。
\end{itemize}

\section{材料分类确认}
\begin{itemize}
  \item \textbf{课件 / slides：} 待补充。
  \item \textbf{作业 / assignment：} 待补充。
  \item \textbf{Quiz：} 待补充。
  \item \textbf{历年题 / past\_exam：} 待补充。
  \item \textbf{Rubric / syllabus / notes：} 待补充。
  \item \textbf{待确认：} 如有无法判断的文件，请先让用户确认分类。
\end{itemize}

\section{材料分类与证据权重}
\begin{itemize}
  \item \textbf{课件 / slides：} 用于提取概念、公式、定义、例题和课程范围。
  \item \textbf{作业 / assignment：} 用于识别练习过的方法、步骤和可变形题型。
  \item \textbf{Quiz：} 用于识别短题问法、概念陷阱和常见误区。
  \item \textbf{历年题 / past\_exam：} 用于识别考试结构、难度和重复题型。
  \item \textbf{Rubric / syllabus：} 用于确认评分点、考试范围和官方学习目标。
\end{itemize}

\section{我是如何判断考点的}
\begin{itemize}
  \item \textbf{高频依据：} 暂无明确材料支持。
  \item \textbf{作业依据：} 暂无明确材料支持。
  \item \textbf{Quiz 依据：} 暂无明确材料支持。
  \item \textbf{往年题依据：} 暂无明确材料支持。
  \item \textbf{推测部分：} 根据课程结构、概念依赖和常见期末题型推测。
  \item \textbf{不确定部分：} 待补充 syllabus、quiz、作业或往年题后更新。
\end{itemize}

\section{考题模式总结}
\begin{itemize}
  \item \textbf{题型结构：} 待补充。
  \item \textbf{高频问法：} 待补充。
  \item \textbf{作业到考试的变形：} 待补充。
  \item \textbf{Quiz 常见陷阱：} 待补充。
  \item \textbf{历年题重复模式：} 待补充。
  \item \textbf{评分偏好：} 待补充。
\end{itemize}

\section{考试地图}
\begin{itemize}
  \item \textbf{待补充考点：} priority: S；likely task: 待补充；source: 待补充。
\end{itemize}

\section{核心考点复习}
\subsection{考点名称 (English Term)}
\begin{itemize}
  \item \textbf{考试作用：} 待补充。
  \item \textbf{定义 / 直觉：} 待补充。
  \item \textbf{公式 / 方法：} 待补充。
  \item \textbf{典型问法：} 待补充。
  \item \textbf{易错点：} 待补充。
  \item \textbf{来源：} 待补充。
\end{itemize}

\section{考前速查表}
\begin{itemize}
  \item \textbf{必背定义：} 待补充。
  \item \textbf{公式与适用条件：} 待补充。
  \item \textbf{解题流程：} 待补充。
  \item \textbf{最后检查的易错点：} 待补充。
\end{itemize}

\section{老师风格练习题}
\subsection{基础保分题}
待补充。每题必须包含 source pattern、tested knowledge point、difficulty、answer、grading points、common wrong answer、follow-up drill。

\subsection{作业变形题}
待补充。

\subsection{Quiz 风格快测题}
待补充。

\subsection{历年题复现题}
待补充。

\section{答案与评分点}
待补充。

\section{错因诊断}
\begin{itemize}
  \item \textbf{概念缺口：} 待补充。
  \item \textbf{条件误用：} 待补充。
  \item \textbf{步骤缺失：} 待补充。
  \item \textbf{迁移困难：} 待补充。
\end{itemize}

\section{个性化复习路径}
待补充。

\end{document}
"""


def slugify(value: str) -> str:
    cleaned = "".join(ch.lower() if ch.isalnum() else "-" for ch in value.strip())
    parts = [part for part in cleaned.split("-") if part]
    return "-".join(parts) or "course-review"


def main() -> None:
    parser = argparse.ArgumentParser(description="Create a FinalSkill review pack.")
    parser.add_argument("course", help="Course name, e.g. CS101")
    parser.add_argument("--output", "-o", default=".", help="Parent output directory")
    args = parser.parse_args()

    stem = slugify(args.course)
    root = Path(args.output).expanduser().resolve() / f"FinalSkill - {stem}"
    root.mkdir(parents=True, exist_ok=True)

    tex_path = root / f"FinalSkill - {stem}.tex"
    if not tex_path.exists():
        tex_path.write_text(TEX_TEMPLATE.replace("__COURSE__", args.course), encoding="utf-8")

    for filename, content in FILES.items():
        path = root / filename
        if not path.exists():
            path.write_text(content, encoding="utf-8")

    print(root)


if __name__ == "__main__":
    main()
