import streamlit as st
import pandas as pd
import numpy as np
import time

# 1. 페이지 설정
st.set_page_config(page_title="Big-Seed 마케팅 마스터", page_icon="📈", layout="wide")

# 2. 사이드바: 이름 입력 (운영자 확인용)
with st.sidebar:
    st.header("👤 학생 등록")
    user_name = st.text_input("이름을 입력하세요:", value="")
    if user_name:
        st.success(f"반갑습니다, **{user_name}**님!")
    else:
        st.warning("이름을 입력해야 리포트가 생성됩니다.")
    st.divider()
    st.info("💡 팁: 지문의 내용을 떠올리며 7문제를 풀어보세요.")

# 3. 메인 화면 구성
tab1, tab2 = st.tabs(["✍️ 7단계 핵심 퀴즈", "📊 성장 시뮬레이터"])

# --- 탭 1: 퀴즈 세션 ---
with tab1:
    st.title("🚀 빅 시드 마케팅 이해도 테스트")
    st.markdown("---")

    # 7문제 데이터
    questions = [
        {"q": "1. 바이럴 마케팅에서 메시지를 전파하는 초기 인원 집단을 무엇이라 하나요?", "options": ["백신", "시드(Seed)", "엔진"], "answer": "시드(Seed)"},
        {"q": "2. 한 사람이 평균적으로 전파하는 인원수를 뜻하는 재생산 지수를 무엇이라 부르나요?", "options": ["R", "G", "S"], "answer": "R"},
        {"q": "3. 메시지가 기하급수적으로 성장(에피데믹)하려면 R의 값은 어떠해야 하나요?", "options": ["R < 1", "R = 1", "R > 1"], "answer": "R > 1"},
        {"q": "4. 빅 시드 마케팅은 바이럴의 힘과 어떤 매체의 힘을 결합한 것인가요?", "options": ["개인 SNS", "전통 매체", "해외 언론"], "answer": "전통 매체"},
        {"q": "5. 기업이 질병과 달리 직접 '규모'를 조절할 수 있는 것은?", "options": ["시드(Seed)의 크기", "개인의 감정", "운(Luck)"], "answer": "시드(Seed)의 크기"},
        {"q": "6. 빅 시드 마케팅이 의존하지 않는 두 가지 요소는?", "options": ["자본과 기술", "시간과 노력", "운과 유명인 지지"], "answer": "운과 유명인 지지"},
        {"q": "7. 이 전략은 결국 누구의 힘을 이용하는 방식인가요?", "options": ["소수의 엘리트", "수많은 보통 사람들", "전문 마케터"], "answer": "수많은 보통 사람들"}
    ]

    # 퀴즈 제출 폼
    with st.form("quiz_final"):
        user_answers = []
        for i, item in enumerate(questions):
            st.markdown(f"#### Q{i+1}. {item['q']}")
            ans = st.radio("정답 선택:", item['options'], key=f"q_{i}")
            user_answers.append(ans)
            st.write("")
        
        submitted = st.form_submit_button("퀴즈 완료 및 성적표 생성")

    # 제출 후 결과 로직
    if submitted:
        if not user_name:
            st.error("⚠️ 이름을 입력하지 않으면 성적표가 생성되지 않습니다. 사이드바를 확인하세요!")
        else:
            score = sum(1 for i, q in enumerate(questions) if user_answers[i] == q['answer'])
            
            st.divider()
            st.balloons()
            
            # 1) 시각적 피드백
            st.subheader(f"📊 {user_name}님의 최종 성적표")
            st.metric("최종 점수", f"{score} / 7")

            # 2) 요청하신 결과 요약 텍스트 생성 (st.code 활용)
            current_time = time.strftime('%Y-%m-%d %H:%M:%S')
            result_text = f"--- 퀴즈 결과 리포트 ---\n"
            result_text += f"이름: {user_name}\n"
            result_text += f"점수: {score} / 7\n"
            result_text += f"일시: {current_time}\n"
            result_text += f"상세: {' '.join(['O' if user_answers[i]==questions[i]['answer'] else 'X' for i in range(7)])}\n"
            result_text += "------------------------"

            st.code(result_text) # 학생들이 복사하기 쉽게 코드로 보여줌
            st.info("⬆️ 위 회색 박스 내용을 복사해서 운영자에게 제출하세요!")
            
            # 3) 복사 확인 버튼
            if st.button("📋 결과 복사 확인"):
                st.write("클립보드 기능을 사용하려면 위 박스의 우측 상단 아이콘을 클릭하거나 직접 드래그 복사해 주세요!")

# --- 탭 2: 시뮬레이터 세션 ---
with tab2:
    st.header("📈 지수적 성장 체험하기")
    c1, c2 = st.columns([1, 2])
    with c1:
        s_size = st.number_input("시드 크기:", value=100)
        r_val = st.slider("재생산 지수(R):", 0.0, 3.0, 1.2)
    
    gens = np.arange(6)
    vals = [s_size * (r_val ** n) for n in gens]
    with c2:
        st.line_chart(vals)
        st.caption("단계별 확산 인원 그래프")
