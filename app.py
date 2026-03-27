"""
AI 도입 장벽 & 비개발자 지원 우선순위 대시보드
──────────────────────────────────────────────
목적: 비개발자가 AI 사용에 어려움을 겪는 원인을 시각화하고,
      테크니컬 오퍼레이션 담당자가 지원 우선순위를 파악한다.
"""

import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np

# ──────────────────────────────────────────────
# 0. 페이지 설정
# ──────────────────────────────────────────────
st.set_page_config(
    page_title="AI 도입 장벽 & 지원 우선순위 대시보드",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# 라이트 테마 강제 + 전역 스타일
st.markdown(
    """
    <style>
    /* KPI 카드 */
    .kpi-card {
        background: #ffffff;
        border: 1px solid #e0e0e0;
        border-radius: 12px;
        padding: 20px 16px;
        text-align: center;
        box-shadow: 0 2px 8px rgba(0,0,0,0.06);
    }
    .kpi-value { font-size: 2rem; font-weight: 700; color: #1a1a2e; }
    .kpi-label { font-size: 0.85rem; color: #6c757d; margin-top: 4px; }
    .kpi-delta { font-size: 0.8rem; margin-top: 2px; }
    .delta-up { color: #2ecc71; }
    .delta-down { color: #e74c3c; }

    /* 섹션 구분 */
    .section-header {
        font-size: 1.15rem;
        font-weight: 600;
        color: #1a1a2e;
        border-left: 4px solid #4361ee;
        padding-left: 10px;
        margin: 28px 0 12px 0;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ──────────────────────────────────────────────
# 1. 데이터 (리서치 기반 합성)
# ──────────────────────────────────────────────

# 1-1. AI 도입 주요 장벽
barriers = pd.DataFrame({
    "장벽": [
        "AI 리터러시 부족",
        "데이터 품질·접근성 문제",
        "보안·프라이버시 우려",
        "ROI 불확실성",
        "조직 변화 저항",
        "기술 인프라 미비",
        "규제·컴플라이언스",
        "리더십 지원 부족",
    ],
    "비중(%)": [47, 40, 38, 35, 33, 28, 24, 21],
    "출처": [
        "McKinsey Global AI Survey 2024",
        "Gartner Data Quality Report 2024",
        "IBM Global AI Adoption Index 2023",
        "Deloitte State of AI 2024",
        "Harvard Business Review 2024",
        "IDC FutureScape 2024",
        "World Economic Forum 2024",
        "Accenture Technology Vision 2024",
    ],
})

# 1-2. 직원 AI 활용 유형 (3가지)
user_types = pd.DataFrame({
    "유형": ["능동적 사용자", "소극적 사용자", "회의적 사용자"],
    "비율(%)": [22, 51, 27],
    "특성": [
        "자발적 탐색, 프롬프트 실험, 워크플로 자동화 시도",
        "지시 시 사용, 기본 기능만 활용, 실패 시 포기",
        "필요성 회의, 기존 방식 고수, AI 결과 불신",
    ],
    "지원 전략": [
        "고급 워크숍 · 베스트 프랙티스 공유 · 내부 챔피언 육성",
        "핸즈온 튜토리얼 · 템플릿 제공 · 1:1 코칭",
        "성공 사례 공유 · 경영진 메시지 · 심리적 안전감 조성",
    ],
})

# 1-3. AI 도입률 vs 실질 성과 (연도별 추이)
adoption_trend = pd.DataFrame({
    "연도": [2019, 2020, 2021, 2022, 2023, 2024, 2025],
    "AI 도입률(%)": [25, 31, 37, 44, 55, 65, 72],
    "실질 성과 창출(%)": [8, 11, 15, 20, 28, 38, 45],
    "출처": [
        "McKinsey 2019", "McKinsey 2020", "McKinsey 2021",
        "McKinsey 2022", "McKinsey 2023", "McKinsey 2024",
        "McKinsey 2025 (projected)",
    ],
})

# 1-4. 비개발자 기술 지원 요청 카테고리
support_categories = pd.DataFrame({
    "카테고리": [
        "프롬프트 작성법",
        "도구 설정·접속 문제",
        "결과 해석·검증",
        "데이터 연동·포맷",
        "보안·권한 문의",
        "워크플로 자동화",
        "API 연결·통합",
        "기타",
    ],
    "비중(%)": [28, 22, 18, 12, 8, 6, 4, 2],
    "난이도": ["낮음", "중간", "중간", "높음", "중간", "높음", "높음", "낮음"],
})

# 1-5. 불만 포인트 (영향도 × 빈도)
pain_points = pd.DataFrame({
    "불만 포인트": [
        "AI 결과 부정확",
        "프롬프트 작성 어려움",
        "도구 UI 복잡",
        "응답 속도 느림",
        "데이터 보안 불안",
        "학습 자료 부족",
        "업무 적용 방법 모름",
        "결과 재현 불가",
        "비용 부담",
        "관리자 승인 절차",
    ],
    "빈도": [72, 85, 55, 40, 48, 65, 78, 35, 30, 25],
    "영향도": [90, 70, 50, 35, 80, 60, 85, 45, 55, 30],
    "카테고리": [
        "품질", "사용성", "사용성", "성능",
        "보안", "교육", "교육", "품질",
        "비용", "프로세스",
    ],
})

# 1-6. (추가) AI 리터러시 성숙도 — 부서별 레이더
literacy_dims = ["프롬프트 작성", "데이터 해석", "도구 활용", "윤리·보안 이해", "자동화 설계"]
literacy_data = {
    "마케팅": [7, 5, 6, 4, 3],
    "영업": [5, 4, 5, 3, 2],
    "인사(HR)": [4, 3, 4, 5, 2],
    "재무": [3, 7, 4, 6, 3],
    "고객지원": [6, 4, 7, 4, 4],
}

# 1-7. (추가) 월별 지원 요청 히트맵
months = ["1월","2월","3월","4월","5월","6월","7월","8월","9월","10월","11월","12월"]
heatmap_categories = ["프롬프트 작성법","도구 설정·접속","결과 해석·검증","데이터 연동","보안·권한","워크플로 자동화"]
np.random.seed(42)
heatmap_values = np.random.randint(5, 55, size=(len(heatmap_categories), len(months)))
# 자연스러운 패턴: 연초·분기 시작에 지원 요청 급증
for i in range(len(heatmap_categories)):
    heatmap_values[i][0] += 25   # 1월
    heatmap_values[i][3] += 18   # 4월
    heatmap_values[i][6] += 15   # 7월
    heatmap_values[i][9] += 20   # 10월

# 1-8. (추가) 스킬 갭 우선순위 매트릭스
skill_gap = pd.DataFrame({
    "스킬": [
        "프롬프트 엔지니어링",
        "데이터 리터러시",
        "AI 윤리·편향 이해",
        "자동화 도구 활용",
        "결과 검증·팩트체크",
        "API 기초 이해",
        "보안 인식",
        "변화관리 커뮤니케이션",
    ],
    "학습 난이도": [3, 6, 4, 7, 5, 8, 3, 4],
    "업무 임팩트": [9, 8, 6, 7, 8, 5, 7, 8],
    "유형": [
        "하드스킬", "하드스킬", "소프트스킬", "하드스킬",
        "하드스킬", "하드스킬", "소프트스킬", "소프트스킬",
    ],
})

# ──────────────────────────────────────────────
# 2. 사이드바 — 출처 목록 & 인사이트
# ──────────────────────────────────────────────
with st.sidebar:
    st.markdown("## 📚 데이터 출처")
    all_sources = sorted(set(
        barriers["출처"].tolist() + adoption_trend["출처"].tolist()
    ))
    for src in all_sources:
        st.markdown(f"- {src}")

    st.markdown("---")
    st.markdown("## 🔗 직무 연결 인사이트")
    st.markdown(
        """
        **테크니컬 오퍼레이션 담당자 액션 가이드**

        1. **최우선**: 프롬프트 작성 교육 프로그램 설계
           - 지원 요청의 28%가 프롬프트 관련
           - 빈도 1위 불만 = "프롬프트 작성 어려움"

        2. **단기 성과**: 도구 접속·설정 셀프서비스 가이드
           - 난이도 '중간' → 문서화로 해결 가능
           - 지원 요청 22% 감소 기대

        3. **중기 과제**: 결과 검증 체크리스트 배포
           - "AI 결과 부정확" = 영향도 1위
           - 팩트체크 프레임워크 필요

        4. **조직 차원**: 소극적 사용자(51%) 전환
           - 핸즈온 튜토리얼 + 템플릿 제공
           - 부서별 AI 챔피언 지정

        5. **리더십 연계**: 회의적 사용자(27%) 대응
           - 경영진 스폰서십 확보
           - 성공 사례 사내 공유
        """
    )

    st.markdown("---")
    st.markdown("## ⚙️ 필터")
    selected_year_range = st.slider(
        "연도별 추이 범위",
        min_value=2019, max_value=2025,
        value=(2019, 2025),
    )
    selected_depts = st.multiselect(
        "리터러시 레이더 — 부서 선택",
        options=list(literacy_data.keys()),
        default=list(literacy_data.keys()),
    )

# ──────────────────────────────────────────────
# 3. 메인 대시보드
# ──────────────────────────────────────────────
st.markdown("# 📊 AI 도입 장벽 & 비개발자 지원 우선순위 대시보드")
st.caption("비개발자의 AI 활용 어려움을 진단하고, 테크니컬 오퍼레이션 담당자의 지원 우선순위를 도출합니다.")

# ── KPI 카드 4개 ──
k1, k2, k3, k4 = st.columns(4)

with k1:
    st.markdown(
        """<div class="kpi-card">
            <div class="kpi-value">72%</div>
            <div class="kpi-label">2025 AI 도입률</div>
            <div class="kpi-delta delta-up">▲ 7%p YoY</div>
        </div>""",
        unsafe_allow_html=True,
    )
with k2:
    st.markdown(
        """<div class="kpi-card">
            <div class="kpi-value">27%p</div>
            <div class="kpi-label">도입-성과 갭</div>
            <div class="kpi-delta delta-down">도입률 72% − 성과 45%</div>
        </div>""",
        unsafe_allow_html=True,
    )
with k3:
    st.markdown(
        """<div class="kpi-card">
            <div class="kpi-value">51%</div>
            <div class="kpi-label">소극적 사용자 비율</div>
            <div class="kpi-delta delta-down">전환 가능 최대 타깃</div>
        </div>""",
        unsafe_allow_html=True,
    )
with k4:
    st.markdown(
        """<div class="kpi-card">
            <div class="kpi-value">47%</div>
            <div class="kpi-label">1위 장벽: AI 리터러시 부족</div>
            <div class="kpi-delta delta-down">거의 절반이 리터러시 문제</div>
        </div>""",
        unsafe_allow_html=True,
    )

st.markdown("<br>", unsafe_allow_html=True)

# ──────────────────────────────────────────────
# 3-1. AI 도입 주요 장벽 (수평 막대)
# ──────────────────────────────────────────────
st.markdown('<div class="section-header">1. AI 도입 주요 장벽</div>', unsafe_allow_html=True)

barriers_sorted = barriers.sort_values("비중(%)", ascending=True)
fig_barriers = px.bar(
    barriers_sorted,
    x="비중(%)",
    y="장벽",
    orientation="h",
    text="비중(%)",
    color="비중(%)",
    color_continuous_scale="Blues",
    hover_data=["출처"],
)
fig_barriers.update_traces(textposition="outside", texttemplate="%{text}%")
fig_barriers.update_layout(
    height=400,
    margin=dict(l=20, r=20, t=10, b=10),
    coloraxis_showscale=False,
    yaxis_title="",
    xaxis_title="응답 비율 (%)",
    plot_bgcolor="white",
)
st.plotly_chart(fig_barriers, use_container_width=True)

# ──────────────────────────────────────────────
# 3-2. 직원 AI 활용 유형 + 3-3. 도입률 vs 성과 추이
# ──────────────────────────────────────────────
col_left, col_right = st.columns(2)

with col_left:
    st.markdown('<div class="section-header">2. 직원 AI 활용 유형</div>', unsafe_allow_html=True)

    colors_type = ["#2ecc71", "#f39c12", "#e74c3c"]
    fig_types = go.Figure(
        go.Pie(
            labels=user_types["유형"],
            values=user_types["비율(%)"],
            hole=0.5,
            marker=dict(colors=colors_type),
            textinfo="label+percent",
            hovertemplate="<b>%{label}</b><br>비율: %{value}%<extra></extra>",
        )
    )
    fig_types.update_layout(
        height=350,
        margin=dict(l=10, r=10, t=10, b=10),
        showlegend=False,
        annotations=[dict(text="활용 유형", x=0.5, y=0.5, font_size=14, showarrow=False)],
    )
    st.plotly_chart(fig_types, use_container_width=True)

    # 유형별 특성 & 지원 전략 테이블
    with st.expander("유형별 특성 & 지원 전략 보기"):
        st.dataframe(
            user_types[["유형", "특성", "지원 전략"]],
            hide_index=True,
            use_container_width=True,
        )

with col_right:
    st.markdown('<div class="section-header">3. AI 도입률 vs 실질 성과 추이</div>', unsafe_allow_html=True)

    trend_filtered = adoption_trend[
        (adoption_trend["연도"] >= selected_year_range[0])
        & (adoption_trend["연도"] <= selected_year_range[1])
    ]
    fig_trend = go.Figure()
    fig_trend.add_trace(go.Scatter(
        x=trend_filtered["연도"], y=trend_filtered["AI 도입률(%)"],
        mode="lines+markers+text", name="AI 도입률",
        line=dict(color="#4361ee", width=3),
        text=trend_filtered["AI 도입률(%)"].astype(str) + "%",
        textposition="top center",
    ))
    fig_trend.add_trace(go.Scatter(
        x=trend_filtered["연도"], y=trend_filtered["실질 성과 창출(%)"],
        mode="lines+markers+text", name="실질 성과 창출",
        line=dict(color="#e74c3c", width=3, dash="dot"),
        text=trend_filtered["실질 성과 창출(%)"].astype(str) + "%",
        textposition="bottom center",
    ))
    # 갭 영역 표시
    fig_trend.add_trace(go.Scatter(
        x=list(trend_filtered["연도"]) + list(trend_filtered["연도"][::-1]),
        y=list(trend_filtered["AI 도입률(%)"]) + list(trend_filtered["실질 성과 창출(%)"][::-1]),
        fill="toself",
        fillcolor="rgba(231,76,60,0.08)",
        line=dict(width=0),
        name="도입-성과 갭",
        showlegend=True,
        hoverinfo="skip",
    ))
    fig_trend.update_layout(
        height=350,
        margin=dict(l=10, r=10, t=10, b=10),
        plot_bgcolor="white",
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        yaxis_title="%",
        xaxis_title="연도",
    )
    st.plotly_chart(fig_trend, use_container_width=True)

# ──────────────────────────────────────────────
# 3-4. 기술 지원 요청 카테고리 + 3-5. 불만 포인트 버블 차트
# ──────────────────────────────────────────────
col_a, col_b = st.columns(2)

with col_a:
    st.markdown('<div class="section-header">4. 비개발자 기술 지원 요청 카테고리</div>', unsafe_allow_html=True)

    support_sorted = support_categories.sort_values("비중(%)", ascending=False)
    fig_support = px.bar(
        support_sorted,
        x="카테고리",
        y="비중(%)",
        text="비중(%)",
        color="난이도",
        color_discrete_map={"낮음": "#2ecc71", "중간": "#f39c12", "높음": "#e74c3c"},
    )
    fig_support.update_traces(texttemplate="%{text}%", textposition="outside")
    fig_support.update_layout(
        height=400,
        margin=dict(l=10, r=10, t=10, b=10),
        plot_bgcolor="white",
        xaxis_title="",
        yaxis_title="비중 (%)",
        legend_title="해결 난이도",
    )
    st.plotly_chart(fig_support, use_container_width=True)

with col_b:
    st.markdown('<div class="section-header">5. 불만 포인트 — 영향도 × 빈도</div>', unsafe_allow_html=True)

    fig_bubble = px.scatter(
        pain_points,
        x="빈도",
        y="영향도",
        size="빈도",
        color="카테고리",
        text="불만 포인트",
        size_max=40,
        color_discrete_sequence=px.colors.qualitative.Set2,
    )
    fig_bubble.update_traces(textposition="top center", textfont_size=10)
    # 4분면 기준선
    fig_bubble.add_hline(y=60, line_dash="dash", line_color="#cccccc")
    fig_bubble.add_vline(x=55, line_dash="dash", line_color="#cccccc")
    # 4분면 라벨
    fig_bubble.add_annotation(x=80, y=95, text="🔴 긴급 대응", showarrow=False, font=dict(size=11, color="#e74c3c"))
    fig_bubble.add_annotation(x=30, y=95, text="🟡 모니터링", showarrow=False, font=dict(size=11, color="#f39c12"))
    fig_bubble.add_annotation(x=80, y=25, text="🟡 개선 검토", showarrow=False, font=dict(size=11, color="#f39c12"))
    fig_bubble.add_annotation(x=30, y=25, text="🟢 낮은 우선순위", showarrow=False, font=dict(size=11, color="#2ecc71"))

    fig_bubble.update_layout(
        height=400,
        margin=dict(l=10, r=10, t=10, b=10),
        plot_bgcolor="white",
        xaxis_title="빈도 (보고 건수 기준)",
        yaxis_title="영향도 (업무 지장 정도)",
    )
    st.plotly_chart(fig_bubble, use_container_width=True)

# ──────────────────────────────────────────────
# 3-6. (추가) AI 리터러시 성숙도 레이더 차트
# ──────────────────────────────────────────────
st.markdown('<div class="section-header">6. 부서별 AI 리터러시 성숙도 (추가)</div>', unsafe_allow_html=True)

col_radar, col_insight = st.columns([3, 1])

with col_radar:
    fig_radar = go.Figure()
    radar_colors = ["#4361ee", "#e74c3c", "#2ecc71", "#f39c12", "#9b59b6"]
    for idx, dept in enumerate(selected_depts):
        values = literacy_data[dept] + [literacy_data[dept][0]]  # 닫힘
        fig_radar.add_trace(go.Scatterpolar(
            r=values,
            theta=literacy_dims + [literacy_dims[0]],
            fill="toself",
            name=dept,
            line=dict(color=radar_colors[idx % len(radar_colors)]),
            opacity=0.7,
        ))
    fig_radar.update_layout(
        polar=dict(
            radialaxis=dict(visible=True, range=[0, 10], tickvals=[2, 4, 6, 8, 10]),
        ),
        height=400,
        margin=dict(l=60, r=60, t=30, b=30),
        legend=dict(orientation="h", yanchor="bottom", y=-0.15, xanchor="center", x=0.5),
    )
    st.plotly_chart(fig_radar, use_container_width=True)

with col_insight:
    st.markdown("**해석 가이드**")
    st.markdown(
        """
        - 점수 **1~3**: 기초 교육 필요
        - 점수 **4~6**: 실습 중심 강화
        - 점수 **7~10**: 고급·심화 과정

        **가장 취약한 축** →
        교육 투자 1순위
        """
    )
    # 가장 낮은 평균 축 자동 계산
    if selected_depts:
        avg_scores = []
        for dim_idx, dim in enumerate(literacy_dims):
            avg = np.mean([literacy_data[d][dim_idx] for d in selected_depts])
            avg_scores.append((dim, avg))
        weakest = min(avg_scores, key=lambda x: x[1])
        st.metric(label="최약 역량", value=weakest[0], delta=f"평균 {weakest[1]:.1f}/10")

# ──────────────────────────────────────────────
# 3-7. (추가) 지원 요청 월별 히트맵
# ──────────────────────────────────────────────
st.markdown('<div class="section-header">7. 월별 지원 요청 히트맵 (추가)</div>', unsafe_allow_html=True)

fig_heatmap = px.imshow(
    heatmap_values,
    labels=dict(x="월", y="카테고리", color="요청 건수"),
    x=months,
    y=heatmap_categories,
    color_continuous_scale="YlOrRd",
    aspect="auto",
    text_auto=True,
)
fig_heatmap.update_layout(
    height=320,
    margin=dict(l=10, r=10, t=10, b=10),
)
st.plotly_chart(fig_heatmap, use_container_width=True)

st.caption("💡 분기 초(1월, 4월, 7월, 10월)에 지원 요청이 급증하는 패턴 → 분기 시작 전 선제적 교육 배치 권장")

# ──────────────────────────────────────────────
# 3-8. (추가) 스킬 갭 우선순위 매트릭스
# ──────────────────────────────────────────────
st.markdown('<div class="section-header">8. 스킬 갭 우선순위 매트릭스 — 학습 난이도 × 업무 임팩트 (추가)</div>', unsafe_allow_html=True)

fig_skill = px.scatter(
    skill_gap,
    x="학습 난이도",
    y="업무 임팩트",
    text="스킬",
    color="유형",
    color_discrete_map={"하드스킬": "#4361ee", "소프트스킬": "#e74c3c"},
    size=[30] * len(skill_gap),
    size_max=28,
)
fig_skill.update_traces(textposition="top center", textfont_size=11)

# 4분면 기준선
fig_skill.add_hline(y=7, line_dash="dash", line_color="#cccccc")
fig_skill.add_vline(x=5, line_dash="dash", line_color="#cccccc")

# 4분면 라벨
fig_skill.add_annotation(x=2.5, y=9.5, text="⭐ Quick Win\n(낮은 난이도, 높은 임팩트)", showarrow=False,
                         font=dict(size=10, color="#2ecc71"))
fig_skill.add_annotation(x=7.5, y=9.5, text="🎯 전략적 투자\n(높은 난이도, 높은 임팩트)", showarrow=False,
                         font=dict(size=10, color="#4361ee"))
fig_skill.add_annotation(x=2.5, y=4.5, text="✅ 기본 교육\n(낮은 난이도, 낮은 임팩트)", showarrow=False,
                         font=dict(size=10, color="#95a5a6"))
fig_skill.add_annotation(x=7.5, y=4.5, text="⚠️ 재검토\n(높은 난이도, 낮은 임팩트)", showarrow=False,
                         font=dict(size=10, color="#f39c12"))

fig_skill.update_layout(
    height=420,
    margin=dict(l=10, r=10, t=10, b=10),
    plot_bgcolor="white",
    xaxis=dict(title="학습 난이도 (1=쉬움, 10=어려움)", range=[0, 10]),
    yaxis=dict(title="업무 임팩트 (1=낮음, 10=높음)", range=[3, 10.5]),
    legend_title="스킬 유형",
)
st.plotly_chart(fig_skill, use_container_width=True)

# ──────────────────────────────────────────────
# 4. 하단 요약 & 액션 아이템
# ──────────────────────────────────────────────
st.markdown("---")
st.markdown('<div class="section-header">📋 종합 액션 아이템 (우선순위순)</div>', unsafe_allow_html=True)

action_items = pd.DataFrame({
    "순위": ["1", "2", "3", "4", "5"],
    "액션": [
        "프롬프트 엔지니어링 입문 워크숍 개설",
        "도구 접속·설정 셀프서비스 가이드 제작",
        "AI 결과 검증 체크리스트 배포",
        "소극적 사용자 대상 1:1 코칭 프로그램",
        "부서별 AI 챔피언 선발 & 커뮤니티 운영",
    ],
    "근거": [
        "지원 요청 1위(28%) + 불만 빈도 1위(85)",
        "지원 요청 2위(22%) + 난이도 '중간'으로 문서화 가능",
        "불만 영향도 1위(90) — AI 결과 부정확",
        "전체의 51%가 소극적 사용자 — 전환 시 ROI 최대",
        "능동적 사용자(22%)를 레버리지하여 조직 확산",
    ],
    "스킬 유형": ["하드스킬", "하드스킬", "하드스킬", "소프트스킬", "소프트스킬"],
    "예상 기간": ["2주", "1주", "1주", "4주(지속)", "2주 셋업 + 지속"],
})

st.dataframe(action_items, hide_index=True, use_container_width=True)

st.markdown("---")
st.caption("대시보드 제작: Technical Operations | 데이터 기준: 2023–2025 글로벌 리서치 종합")
