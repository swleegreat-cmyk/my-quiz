import streamlit as st
import pandas as pd
import numpy as np
import time

# 1. 페이지 설정
st.set_page_config(page_title="Marketing Strategy Lab", page_icon="🧪", layout="wide")

# 2. 사이드바: 학생 등록
with st.sidebar:
    st.header("👤 학생 등록")
    user_name = st.text_input("이름을 입력하세요:", value="")
    st.divider()
    st.info("💡 빅 시드 마케팅 vs 유명인 보증 마케팅의 차이를 시뮬레이션으로 확인해보세요.")

# 3. 메인 탭 구성
tab1, tab2 = st.tabs(["📊 성장 시뮬레이터 (비교)", "✍️ 7단계 핵심 퀴즈"])

# --- 탭 1: 두 가지 마케팅 전략 비교 시뮬레이터 ---
with tab1:
    st.header("📈 마케팅 전략별 확산 비교")
    st.write("초기 시드(Seed)의 크기와 재생산 지수(R)가 결과에 어떤 영향을 주는지 비교해보세요.")

    col1, col2 = st.columns([1, 2])

    with col1:
        st.subheader("설정 변경")
        st.markdown("**[방법 A] 빅 시드 마케팅**")
        a_seed = st.number_input("A 초기 시드 (보통 사람들 수):", value=1000, step=100)
        a_r = st.slider("A 재생산 지수 (R):", 0.5, 2.0, 1.1, 0.1, key="a_r")

        st.divider()

        st.markdown("**[방법 B] 유명인 보증 마케팅**")
        b_seed = st.number_input("B 초기 시드 (유명인 수):", value=1, step=1)
        b_r = st.slider("B 재생산 지수 (R):", 1.0, 10.0, 5.0, 0.5, key="b_r")
        
        steps = st.slider("확산 단계 (Generation):", 1, 10, 7)

    # 데이터 계산 로직
    gens = np.arange(steps + 1)
    a_growth = [int(a_seed * (a_r ** n)) for n in gens]
    b_growth = [int(b_seed * (b_r ** n)) for n in gens]

    df_compare = pd.DataFrame({
        "단계": gens,
        "빅 시드 (보통 사람들)": a_growth,
        "유명인 (소수 정예)": b_growth
    }).set_index("단계")

    with col2:
        st.subheader("확산 추이 그래프")
        st.line_chart(df_compare)
        
        m1, m2 = st.columns(2)
        m1.metric("빅 시드 최종 전파", f"{a_growth[-1]:,} 명", delta=f"{a_growth[-1] - a_seed} 증분")
        m2.metric("유명인 최종 전파", f"{b_growth[-1]:,} 명", delta=f"{b_growth[-1] - b_seed} 증분")
        
        st.info(f"**분석 결과:** {user_name}님, 보시다시피 유명인은 초반 폭발력은 크지만(높은 R), "
                f"빅 시드는 낮은 R값으로도 대규모 인원에게 안정적으로 도달하는 것을 볼 수 있습니다.")

# --- 탭 2: 퀴즈 세션 (기능 유지) ---
with tab2:
    st.title("🚀 빅 시드 마케팅 이해도 테스트")
    
    questions = [
        {"q": "1. 바이럴 마케팅에서 메시지를 전파하는 초기 인원 집단은?", "options": ["백신", "시드(Seed)", "엔진"], "answer": "시드(Seed)"},
        {"q": "2. 한 사람이 평균적으로 전파하는 인원수를 뜻하는 지수는?", "options": ["R", "G", "S"], "answer": "R"},
        {"q": "3. 메시지가 기하급수적으로 성장하려면 R의 값은?", "options": ["R < 1", "R = 1", "R > 1"], "answer": "R > 1"},
        {"q": "4. 빅 시드 마케팅은 바이럴의 힘과 어떤 매체의 힘을 결합했나요?", "options": ["개인 SNS", "전통 매체", "해외 언론"], "answer": "전통 매체"},
        {"q": "5. 기업이 질병과 달리 직접 '규모'를 조절할 수 있는 것은?", "options": ["시드(Seed)의 크기", "개인의 감정", "운(Luck)"], "answer": "시드(Seed)의 크기"},
        {"q": "6. 빅 시드 마케팅이 의존하지 않는 두 가지 요소는?", "options": ["자본과 기술", "시간과 노력", "운과 유명인 지지"], "answer": "운과 유명인 지지"},
        {"q": "7. 이 전략은 결국 누구의 힘을 이용하는 방식인가요?", "options": ["소수의 엘리트", "수많은 보통 사람들", "전문 마케터"], "answer": "수많은 보통 사람들"}
    ]

    with st.form("quiz_final"):
        user_answers = []
        for i, item in enumerate(questions):
            st.markdown(f"#### Q{i+1}. {item['q']}")
            ans = st.radio("정답 선택:", item['options'], key=f"q_{i}")
            user_answers.append(ans)
        
        submitted = st.form_submit_button("퀴즈 완료 및 성적표 생성")

    if submitted:
        if not user_name:
            st.error("⚠️ 사이드바에 이름을 입력해야 성적표가 생성됩니다!")
        else:
            score = sum(1 for i, q in enumerate(questions) if user_answers[i] == q['answer'])
            st.divider()
            st.balloons()
            st.subheader(f"📊 {user_name}님의 최종 성적표")
            
            result_text = f"--- 퀴즈 결과 리포트 ---\n이름: {user_name}\n점수: {score} / 7\n일시: {time.strftime('%Y-%m-%d %H:%M:%S')}\n------------------------"
            st.code(result_text)
            st.info("⬆️ 위 회색 박스 우측 상단의 복사 버튼을 눌러 선생님께 제출하세요!")
