import streamlit as st

# 웹페이지 탭 이름과 아이콘 설정
st.set_page_config(
    page_title="Gusan Highschool English Class",
    page_icon="🏫",
)

# 1. 귀여운 폰트(Google Fonts - Jua) 불러오기 & 환영 문구
# CSS 스타일을 추가하여 폰트를 동글동글하게 바꿉니다.
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Jua&display=swap');
    </style>
    
    <h1 style="text-align: center; font-family: 'Jua', 'Comic Sans MS', cursive;">
        🎈Welcome to Gusan Highschool English Class🎈
    </h1>
    """, 
    unsafe_allow_html=True
)

st.write("") # 약간의 빈칸 추가

# 2. 안내 문구 (이곳에도 같은 귀여운 폰트 적용)
st.markdown(
    """
    <p style="text-align: center; font-size: 20px; color: #555555; font-family: 'Jua', 'Comic Sans MS', cursive;">
        👈 왼쪽 사이드바를 열어서 필요한 학습 페이지로 이동해보세요!
    </p>
    """, 
    unsafe_allow_html=True
)
