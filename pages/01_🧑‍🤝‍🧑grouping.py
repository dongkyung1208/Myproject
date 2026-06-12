import streamlit as st
import pandas as pd
import random
import os

st.set_page_config(page_title="Random Grouping", layout="centered")

st.title("👯‍♂️ Random Grouping (모둠 구성)")
st.caption("명단을 바탕으로 빠르고 공정하게 랜덤 조 편성을 진행합니다.")

# ---------------------------
# 1. 데이터 불러오기 함수
# ---------------------------
@st.cache_data
def load_data(file_path):
    # 위에서 2줄을 건너뛰면 '학번, 이름, 비고...'가 헤더(열 이름)가 됩니다.
    df = pd.read_csv(file_path, skiprows=2)
    classes_data = {}
    
    for i in range(1, 9):
        # 각 반의 '이름' 열 위치 찾기: 1반(1), 2반(4), 3반(7) ...
        col_idx = (i - 1) * 3 + 1
        
        # 결측치(빈칸)를 제외하고 학생 이름만 리스트로 추출
        students = df.iloc[:, col_idx].dropna().tolist()
        classes_data[f"{i}반"] = students
        
    return classes_data

# ---------------------------
# 2. 파일 업로드 및 데이터 처리
# ---------------------------
st.markdown("---")
uploaded_file = st.file_uploader("📂 1학년 학생 명단 CSV 파일을 업로드해주세요.", type=['csv'])

if uploaded_file is not None:
    try:
        # 데이터 로드
        class_students = load_data(uploaded_file)
        
        # ---------------------------
        # 3. 1반 ~ 8반 탭(Tab) 생성
        # ---------------------------
        tabs = st.tabs([f"{i}반" for i in range(1, 9)])
        
        for i, tab in enumerate(tabs):
            with tab:
                class_name = f"{i+1}반"
                students = class_students[class_name]
                
                st.subheader(f"🏫 {class_name} (총 {len(students)}명)")
                
                # ---------------------------
                # 4. 모둠 구성 옵션 (몇 개 조? OR 몇 명씩?)
                # ---------------------------
                col1, col2 = st.columns(2)
                with col1:
                    group_method = st.radio(
                        f"👉 {class_name} 모둠 기준 선택", 
                        ["조 개수로 나누기", "한 조당 인원으로 나누기"], 
                        key=f"method_{i}"
                    )
                with col2:
                    if group_method == "조 개수로 나누기":
                        num_val = st.number_input("몇 개의 조를 만들까요?", min_value=1, max_value=len(students), value=6, key=f"val_{i}")
                    else:
                        num_val = st.number_input("한 조에 몇 명씩 배정할까요?", min_value=1, max_value=len(students), value=4, key=f"val_{i}")
                
                # ---------------------------
                # 5. 모둠 구성 버튼 및 결과 출력
                # ---------------------------
                if st.button(f"🎲 {class_name} 모둠 구성하기", use_container_width=True, key=f"btn_{i}"):
                    
                    # 명단 섞기
                    shuffled_students = students.copy()
                    random.shuffle(shuffled_students)
                    
                    groups = []
                    
                    # 로직 A: 정해진 '조 개수'에 맞춰 골고루 분배
                    if group_method == "조 개수로 나누기":
                        groups = [[] for _ in range(num_val)]
                        for idx, student in enumerate(shuffled_students):
                            groups[idx % num_val].append(student)
                            
                    # 로직 B: 정해진 '인원수'만큼 끊어서 분배 (마지막 조는 인원이 적을 수 있음)
                    else:
                        for j in range(0, len(shuffled_students), num_val):
                            groups.append(shuffled_students[j:j + num_val])
                            
                    st.success(f"🎉 {class_name} 모둠 편성이 완료되었습니다!")
                    
                    # 결과를 보기 좋게 3열로 나누어 카드 형태로 출력
                    cols = st.columns(3)
                    for g_idx, group in enumerate(groups):
                        with cols[g_idx % 3]:
                            # 각 조의 명단을 깔끔한 텍스트 상자로 표시
                            group_text = "\n".join([f"- {name}" for name in group])
                            st.info(f"**{g_idx + 1}조** ({len(group)}명)\n\n{group_text}")

    except Exception as e:
        st.error(f"파일을 읽는 중 오류가 발생했습니다. 첨부해주신 명단 파일이 맞는지 확인해주세요.\n\n오류 내용: {e}")
else:
    st.info("👆 위쪽에 '2026. 구산고 학적 현황표.xlsx - 1학년.csv' 파일을 드래그해서 올려주세요.")
