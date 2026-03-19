import streamlit as st

st.set_page_config(page_title="Big-Seed 마케팅 퀴즈", page_icon="📈")

def main():
    st.title("🚀 빅 시드 마케팅 이해도 테스트")
    st.info("지문 내용을 바탕으로 퀴즈를 풀어보세요!")

    # 퀴즈 정의
    questions = [
        {
            "q": "바이럴 마케팅에서 '전염병' 같은 확산이 일어나기 위한 재생산 지수(R)의 값은?",
            "options": ["R < 1", "R = 1", "R > 1"],
            "answer": "R > 1"
        },
        {
            "q": "빅 시드 마케팅의 가장 큰 장점은 무엇인가요?",
            "options": ["유명 연예인에 의존한다", "운 좋게 퍼지길 기다린다", "초기 전파자(Seed)의 규모를 조절할 수 있다"],
            "answer": "초기 전파자(Seed)의 규모를 조절할 수 있다"
        }
    ]

    # 폼 생성
    with st.form("quiz_form"):
        score = 0
        user_choices = []
        for i, q in enumerate(questions):
            st.write(f"**Q{i+1}. {q['q']}**")
            choice = st.radio("보기 선택:", q['options'], key=f"q{i}")
            user_choices.append(choice)
            st.write("---")
        
        submitted = st.form_submit_button("제출하기")

        if submitted:
            for i, q in enumerate(questions):
                if user_choices[i] == q['answer']:
                    score += 1
            
            st.success(f"결과: {len(questions)}문제 중 {score}문제를 맞혔습니다!")
            if score == len(questions):
                st.balloons()

if __name__ == "__main__":
    main()