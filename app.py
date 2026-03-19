import streamlit as st
import pandas as pd
import numpy as np
import time

# 페이지 설정
st.set_page_config(page_title="Marketing Sim & Quiz", page_icon="📊", layout="wide")

# 사이드바: 사용자 정보 입력
with st.sidebar:
    st.header("👤 사용자 등록")
    user_name = st.text_input("이름을 입력하세요:", "마케팅 초보")
    st.write(f"반갑습니다, **{user_name}**님!")
    st.divider()
    st.info("💡 팁: 재생산 지수(R)가 1보다 커야 전염병처럼 번집니다.")

# 메인 탭 구성 (시뮬레이터와 퀴즈 분리)
tab1, tab2 = st.tabs(["📈 성장 시뮬레이터", "✍️ 마케팅 퀴즈"])

# --- 탭 1: 성장 시뮬레이터 (추가된 기능) ---
with tab1:
    st.header("바이럴 확산 시뮬레이터")
    st.write("지문에서 언급된 '시드 크기'와 'R'의 위력을 직접 확인해 보세요.")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        seed_size = st.number_input("초기 시드(Seed) 크기:", min_value=1, value=100)
        r_value = st.slider("재생산 지수 (R):", 0.0, 3.0, 1.2, 0.1)
        steps = st.slider("확산 단계 (Generation):", 1, 10, 5)
    
    # 계산 로직
    generations = np.arange(steps + 1)
    counts = [seed_size * (r_value ** n) for n in generations]
    df = pd.DataFrame({"단계": generations, "전파 인원": counts})
    
    with col2:
        st.line_chart(df.set_index("단계"))
        final_count = int(counts[-1])
        st.metric("최종 확산 인원", f"{final_count:,} 명", delta=f"{final_count - seed_size} 명 증가")

# --- 탭 2: 마케팅 퀴즈 (기능 강화) ---
with tab2:
    st.header(f"{user_name}님의 마케팅 실력 점검")
    
    questions = [
        {
            "q": "바이럴 마케팅에서 '기하급수적 성장'의 조건은?",
            "options": ["R < 1", "R = 1", "R > 1"],
            "answer": "R > 1",
            "why": "한 사람이 평균 1명보다 많이 퍼뜨려야 숫자가 계속 불어납니다."
        },
        {
            "q": "빅 시드 마케팅이 통제하는 핵심 변수는?",
            "options": ["운(Luck)", "유명인 섭외", "초기 시드 크기"],
            "answer": "초기 시드 크기",
            "why": "기업은 질병과 달리 초기 전파자의 숫자를 자본과 매체로 조절할 수 있습니다."
        },
        {
            "q": "빅 시드 마케팅은 누구의 힘을 활용하나요?",
            "options": ["소수 엘리트", "보통 사람들", "전문 마케터"],
            "answer": "보통 사람들",
            "why": "수많은 보통 사람들의 작은 전파력이 모여 큰 폭발을 만듭니다."
        }
    ]

    with st.form("quiz_advanced"):
        user_answers = []
        for i, item in enumerate(questions):
            st.markdown(f"**Q{i+1}. {item['q']}**")
            ans = st.radio("선택:", item['options'], key=f"adv_{i}")
            user_answers.append(ans)
            st.write("")
        
        submitted = st.form_submit_button("제출 및 해설 보기")

    if submitted:
        score = 0
        st.subheader("🧐 채점 결과 및 해설")
        
        for i, item in enumerate(questions):
            is_correct = user_answers[i] == item['answer']
            if is_correct:
                st.success(f"Q{i+1}: 정답입니다! ✅")
                score += 1
            else:
                st.error(f"Q{i+1}: 오답입니다. (선택: {user_answers[i]}) ❌")
            
            # 해설 상자 추가
            with st.expander("해설 보기"):
                st.write(f"**정답: {item['answer']}**")
                st.write(item['why'])
        
        st.divider()
        st.balloons()
        st.write(f"### {user_name}님의 최종 점수: {score} / {len(questions)}")
