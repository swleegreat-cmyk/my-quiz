import streamlit as st

# 페이지 제목 설정
st.set_page_config(page_title="Big-Seed 마케팅 마스터", page_icon="📝")

def main():
    st.title("📊 빅 시드 마케팅 7단계 퀴즈")
    st.write("지문의 핵심 내용을 7개의 문제로 완벽히 정복해보세요!")
    st.divider()

    # 7개의 문제 데이터
    questions = [
        {
            "q": "1. 바이럴 마케팅은 메시지를 전파하는 '이것'을 가진 개인들로부터 시작됩니다. 무엇일까요?",
            "options": ["백신(Vaccine)", "시드(Seed)", "엔진(Engine)", "타겟(Target)"],
            "answer": "시드(Seed)"
        },
        {
            "q": "2. 한 사람이 평균적으로 감염시키는 새 인원수를 뜻하는 용어는?",
            "options": ["성장률(G)", "전파력(P)", "재생산 지수(R)", "확산 속도(S)"],
            "answer": "재생산 지수(R)"
        },
        {
            "q": "3. 메시지가 기하급수적으로 성장(에피데믹)하려면 R의 값은 어떠해야 하나요?",
            "options": ["R < 0", "R < 1", "R = 1", "R > 1"],
            "answer": "R > 1"
        },
        {
            "q": "4. 지문에 따르면, 기업이나 정치 캠페인이 질병과 달리 직접 '조절'할 수 있는 것은?",
            "options": ["감염 속도", "시드(Seed)의 크기", "개인의 면역력", "바이러스의 종류"],
            "answer": "시드(Seed)의 크기"
        },
        {
            "q": "5. '빅 시드 마케팅'은 바이럴 마케팅의 힘과 무엇의 힘을 결합한 것인가요?",
            "options": ["SNS 광고", "전통 매체(Traditional media)", "입소문", "1대1 대면 마케팅"],
            "answer": "전통 매체(Traditional media)"
        },
        {
            "q": "6. 빅 시드 마케팅이 의존하지 않는 '두 가지' 요소로 언급된 것은?",
            "options": ["데이터와 분석", "운(Luck)과 유명인 지지", "자본과 기술", "시간과 노력"],
            "answer": "운(Luck)과 유명인 지지"
        },
        {
            "q": "7. 빅 시드 마케팅은 결국 누구의 힘을 활용하는 방식인가요?",
            "options": ["소수의 엘리트", "수많은 보통 사람들", "영향력 있는 유튜버", "전문 마케터 집단"],
            "answer": "수많은 보통 사람들"
        }
    ]

    # 퀴즈 시작
    with st.form("marketing_quiz"):
        user_answers = []
        for i, item in enumerate(questions):
            st.markdown(f"#### {item['q']}")
            ans = st.radio("정답을 선택하세요:", item['options'], key=f"ans_{i}")
            user_answers.append(ans)
            st.write("") # 간격 띄우기

        submitted = st.form_submit_button("결과 확인하기")

    if submitted:
        score = sum(1 for i, q in enumerate(questions) if user_answers[i] == q['answer'])
        
        if score == 7:
            st.balloons()
            st.success(f"7/7 만점입니다! 당신은 마케팅 전문가군요! 🏆")
        elif score >= 5:
            st.info(f"잘하셨습니다! {score}/7점을 맞히셨습니다. 👍")
        else:
            st.warning(f"조금 더 복습해볼까요? {score}/7점을 맞히셨습니다. 📖")

if __name__ == "__main__":
    main()
