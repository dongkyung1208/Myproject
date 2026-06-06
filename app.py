import streamlit as st

# 웹페이지 탭 이름과 아이콘 설정 (선택 사항)
st.set_page_config(
    page_title="Gusan Highschool English Class",
    page_icon="🏫",
)

# 1. 중앙 정렬된 환영 문구 (크고 굵게)
st.markdown(
    """
    <h1 style='text-align: center;'>
        Welcome to Gusan Highschool English Class
    </h1>
    """, 
    unsafe_allow_html=True
)

st.write("") # 약간의 빈칸 추가

# 2. 안내 문구 (이것도 가운데 정렬하면 깔끔합니다)
st.markdown(
    """
    <p style='text-align: center; font-size: 18px; color: #555555;'>
        👈 왼쪽 사이드바를 열어서 필요한 학습 페이지로 이동해보세요!
    </p>
    """, 
    unsafe_allow_html=True
)
