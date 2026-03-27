# AI Adoption Barriers & Non-Developer Support Priority Dashboard

An interactive Streamlit dashboard that visualizes the challenges non-developers face when adopting AI tools and helps Technical Operations teams identify support priorities.

## Overview

This dashboard synthesizes data from global AI research reports (McKinsey, Gartner, IBM, Deloitte, etc.) to provide actionable insights for organizations looking to improve AI adoption among non-technical employees.

## Key Features

### 1. AI Adoption Barriers
Horizontal bar chart showing the top 8 barriers to AI adoption with research sources (e.g., AI literacy gaps at 47%, data quality issues at 40%).

### 2. Employee AI Usage Types
Donut chart classifying employees into three categories:
- **Active Users** (22%) - Self-driven exploration and workflow automation
- **Passive Users** (51%) - Use when instructed, give up on failure
- **Skeptical Users** (27%) - Doubt AI necessity, distrust results

### 3. AI Adoption Rate vs. Actual Outcomes (2019-2025)
Dual-line trend chart highlighting the persistent gap between adoption rates and actual value creation.

### 4. Non-Developer Technical Support Request Categories
Bar chart breaking down support requests by category and resolution difficulty (prompt writing 28%, tool setup 22%, result interpretation 18%).

### 5. Pain Points - Impact x Frequency Matrix
Bubble chart with 4-quadrant analysis to prioritize pain point resolution.

### 6. AI Literacy Maturity Radar (by Department)
Radar chart comparing departments across 5 dimensions: prompt writing, data interpretation, tool usage, ethics/security understanding, and automation design.

### 7. Monthly Support Request Heatmap
Heatmap revealing seasonal patterns in support requests (spikes at quarter starts).

### 8. Skill Gap Priority Matrix
Scatter plot mapping skills by learning difficulty vs. business impact, categorized as hard skills and soft skills.

## Tech Stack

| Component | Technology |
|-----------|------------|
| Framework | Streamlit |
| Visualization | Plotly (Express + Graph Objects) |
| Data Processing | Pandas, NumPy |
| Language | Python 3.8+ |

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```bash
streamlit run app.py
```

The dashboard will open at `http://localhost:8501`.

## Sidebar Features

- **Data Sources**: Full list of research references
- **Action Guide**: Prioritized action items for Technical Operations
- **Filters**: Year range slider and department selector for interactive exploration

## Data Sources

All data is synthesized from the following global research reports:
- McKinsey Global AI Survey (2019-2025)
- Gartner Data Quality Report 2024
- IBM Global AI Adoption Index 2023
- Deloitte State of AI 2024
- Harvard Business Review 2024
- IDC FutureScape 2024
- World Economic Forum 2024
- Accenture Technology Vision 2024

## License

This project is for internal analysis and educational purposes.

---

# AI 도입 장벽 & 비개발자 지원 우선순위 대시보드

비개발자가 AI 도구를 도입할 때 겪는 어려움을 시각화하고, 테크니컬 오퍼레이션 담당자가 지원 우선순위를 파악할 수 있도록 돕는 인터랙티브 Streamlit 대시보드입니다.

## 개요

McKinsey, Gartner, IBM, Deloitte 등 글로벌 AI 리서치 보고서의 데이터를 종합하여, 비기술 직원의 AI 도입률을 높이기 위한 실행 가능한 인사이트를 제공합니다.

## 주요 기능

### 1. AI 도입 주요 장벽
리서치 출처와 함께 AI 도입의 8대 장벽을 수평 막대 차트로 시각화합니다 (예: AI 리터러시 부족 47%, 데이터 품질 문제 40%).

### 2. 직원 AI 활용 유형
직원을 세 가지 유형으로 분류한 도넛 차트:
- **능동적 사용자** (22%) - 자발적 탐색, 워크플로 자동화 시도
- **소극적 사용자** (51%) - 지시 시 사용, 실패 시 포기
- **회의적 사용자** (27%) - 필요성 회의, AI 결과 불신

### 3. AI 도입률 vs 실질 성과 추이 (2019-2025)
도입률과 실질 성과 간의 지속적인 갭을 보여주는 이중 라인 차트입니다.

### 4. 비개발자 기술 지원 요청 카테고리
카테고리별, 해결 난이도별 지원 요청 비중을 보여주는 막대 차트입니다 (프롬프트 작성법 28%, 도구 설정 22%, 결과 해석 18%).

### 5. 불만 포인트 - 영향도 x 빈도 매트릭스
4분면 분석을 통해 불만 포인트 해결 우선순위를 도출하는 버블 차트입니다.

### 6. 부서별 AI 리터러시 성숙도 레이더
5개 차원(프롬프트 작성, 데이터 해석, 도구 활용, 윤리/보안 이해, 자동화 설계)에 걸쳐 부서간 역량을 비교하는 레이더 차트입니다.

### 7. 월별 지원 요청 히트맵
지원 요청의 계절적 패턴을 보여주는 히트맵입니다 (분기 초에 급증하는 패턴 확인).

### 8. 스킬 갭 우선순위 매트릭스
학습 난이도 vs 업무 임팩트로 스킬을 매핑하고, 하드스킬/소프트스킬로 분류한 산점도입니다.

## 기술 스택

| 구성 요소 | 기술 |
|-----------|------|
| 프레임워크 | Streamlit |
| 시각화 | Plotly (Express + Graph Objects) |
| 데이터 처리 | Pandas, NumPy |
| 언어 | Python 3.8+ |

## 설치

```bash
pip install -r requirements.txt
```

## 실행

```bash
streamlit run app.py
```

대시보드가 `http://localhost:8501`에서 열립니다.

## 사이드바 기능

- **데이터 출처**: 리서치 참고 자료 전체 목록
- **액션 가이드**: 테크니컬 오퍼레이션 담당자를 위한 우선순위별 액션 아이템
- **필터**: 연도 범위 슬라이더 및 부서 선택으로 인터랙티브 탐색

## 데이터 출처

모든 데이터는 다음 글로벌 리서치 보고서를 기반으로 합성되었습니다:
- McKinsey Global AI Survey (2019-2025)
- Gartner Data Quality Report 2024
- IBM Global AI Adoption Index 2023
- Deloitte State of AI 2024
- Harvard Business Review 2024
- IDC FutureScape 2024
- World Economic Forum 2024
- Accenture Technology Vision 2024

## 라이선스

이 프로젝트는 내부 분석 및 교육 목적으로 제작되었습니다.
