# AI Data with Copilot and Pencil

![Generate Dashboard Images](https://github.com/EltonDlamini97/ai-data-with-copilot-and-pencil/actions/workflows/generate-dashboard.yml/badge.svg)

This repository contains an experimental agent scaffold, research report, and visualization assets for "Prompt engineering and the future of robotics" along with an analysis of a student placement dataset and a dashboard.

Contents
- research/: research notes, markdown report, PDF/DOCX exports
- analysis/: CSV analysis scripts, summary outputs, charts, dashboard SVG and .epgz (Pencil project)
- auth-scaffold/: minimal Node.js auth scaffold (register/login + JWT middleware)

Quickstart
1. Clone the repo:
   `ash
   git clone https://github.com/EltonDlamini97/ai-data-with-copilot-and-pencil.git
   cd ai-data-with-copilot-and-pencil
   `
2. Review the research report in esearch/ and the dashboard in nalysis/dashboard.svg or open nalysis/dashboard.epgz with Pencil.

Run analysis (optional)
- The analysis script nalysis/analyze_csv.py expects a CSV at C:\Users\elton\Downloads\archive\Student_Placement_Skills_2025.csv.
- To regenerate charts locally, install Python 3 and dependencies, then run:
  `ash
  python -m pip install pandas matplotlib seaborn
  python analysis/analyze_csv.py
  `

Contributing
- Open issues or PRs. Add tests and update the README.

License
- MIT. See LICENSE file.

_Co-authored-by: Copilot <223556219+Copilot@users.noreply.github.com>_
