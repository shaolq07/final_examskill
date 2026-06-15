#!/usr/bin/env python3
"""Create a FinalSkill LaTeX-first review pack folder."""

from __future__ import annotations

import argparse
from pathlib import Path


FILES = {
    "working-notes.md": "# Working Notes\n\n## Segmentation Map\n\n## Extracted Exam Points\n\n## Coverage Concerns\n",
    "sources.md": "# Sources\n\n| File | Pages/Slides/Questions Used | Notes |\n| --- | --- | --- |\n",
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
  \item 先看“考试地图”和 S/A 级考点，再进入具体章节。
  \item 每个考点优先掌握定义、适用条件、典型问法和易错点。
  \item 做完练习题后，用“错因诊断”和“复习路径”安排下一轮复习。
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

\section{考试地图}
\begin{longtable}{p{0.16\textwidth}p{0.27\textwidth}p{0.2\textwidth}p{0.1\textwidth}p{0.12\textwidth}}
\toprule
单元 & 核心考点 & 可能题型 & 优先级 & 来源 \\
\midrule
待补充 & 待补充 & 待补充 & S & 待补充 \\
\bottomrule
\end{longtable}

\section{考点复习}
\subsection{考点名称}
\begin{itemize}
  \item \textbf{考试作用：} 待补充。
  \item \textbf{定义 / 直觉：} 待补充。
  \item \textbf{公式 / 方法：} 待补充。
  \item \textbf{典型问法：} 待补充。
  \item \textbf{易错点：} 待补充。
  \item \textbf{来源：} 待补充。
\end{itemize}

\section{考前速查表}
\subsection{必背定义}
待补充。

\subsection{公式与适用条件}
待补充。

\subsection{最后检查的易错点}
待补充。

\section{老师风格练习题}
\subsection{基础保分题}
待补充。

\subsection{高频变形题}
待补充。

\subsection{压轴综合题}
待补充。

\section{答案与评分点}
待补充。

\section{错因诊断}
\begin{longtable}{p{0.2\textwidth}p{0.25\textwidth}p{0.25\textwidth}p{0.2\textwidth}}
\toprule
错因 & 表现 & 修复方法 & 对应练习 \\
\midrule
概念缺口 & 待补充 & 待补充 & 待补充 \\
\bottomrule
\end{longtable}

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

    root = Path(args.output).expanduser().resolve() / f"FinalSkill - {slugify(args.course)}"
    root.mkdir(parents=True, exist_ok=True)

    tex_path = root / f"FinalSkill - {slugify(args.course)}.tex"
    if not tex_path.exists():
        tex_path.write_text(TEX_TEMPLATE.replace("__COURSE__", args.course), encoding="utf-8")

    for filename, content in FILES.items():
        path = root / filename
        if not path.exists():
            path.write_text(content, encoding="utf-8")

    print(root)


if __name__ == "__main__":
    main()
