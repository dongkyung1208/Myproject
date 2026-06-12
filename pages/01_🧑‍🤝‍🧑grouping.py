import streamlit as st
import pandas as pd
import random

st.set_page_config(page_title="Random Grouping", layout="centered")

st.title("👯‍♂️ Random Grouping (모둠 구성)")
st.caption("명단을 바탕으로 빠르고 공정하게 랜덤 조 편성을 진행합니다.")

# ---------------------------
# 1. 파일 구조에 맞춘 데이터 불러오기 함수
# ---------------------------
@st.cache_data
def load_data(file_path):
    # 파일 확장자에 따라 다르게 읽기 (CSV, Excel 모두 지원)
    if file_path.name.endswith('.csv'):
        df = pd.read_csv(file_path, skiprows=1) # 두 번째 줄(1반, 2반...)을 열 이름으로 지정
    else:
        df = pd.read_excel(file_path, skiprows=1)
        
    classes_data = {}
    
    # 1반부터 8반까지 (데이터프레임의 0번째~7번째 열)
    for i in range(8):
        class_name = f"{i+1}반"
        
        # i번째 열 추출 -> 첫 번째 행('이름' 글자) 제외 -> 빈칸(NaN) 제거 -> 리스트 변환
        students = df.iloc[1:, i].dropna().astype(str).tolist()
        
        # 이름 중에 진짜 빈칸이거나 'nan'이라는 글자로 인식된 쓰레기값을 완벽하게 필터링
        clean_students = [name.strip() for name in students if name.strip() and name.strip().lower() != 'nan']
        
        classes_data[class_name] = clean_students
        
    return classes_data

# ---------------------------
# 2. 파일 업로드 및 데이터 처리
# ---------------------------
st.markdown("---")
# CSV와 Excel 파일을 모두 업로드할 수 있도록 허용
uploaded_file = st.file_uploader("📂 1학년 학생 명단 파일(Excel 또는 CSV)을 업로드해주세요.", type=['xlsx', 'xls', 'csv'])

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
                
                # 빈칸이 완벽히 제거된 실제 총원 출력
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
                        num_val = st.number_input("몇 개의 조를 만들까요?", min_value=1, max_value=len(students) if len(students) > 0 else 1, value=6, key=f"val_{i}")
                    else:
                        num_val = st.number_input("한 조에 몇 명씩 배정할까요?", min_value=1, max_value=len(students) if len(students) > 0 else 1, value=4, key=f"val_{i}")
                
                # ---------------------------
                # 5. 모둠 구성 버튼 및 결과 출력
                # ---------------------------
                if st.button(f"🎲 {class_name} 모둠 구성하기", use_container_width=True, key=f"btn_{i}"):
                    
                    if len(students) == 0:
                        st.warning(f"{class_name}의 학생 명단이 비어있습니다. 파일을 확인해주세요.")
                    else:
                        # 명단 섞기
                        shuffled_students = students.copy()
                        random.shuffle(shuffled_students)
                        
                        groups = []
                        
                        # 로직 A: 정해진 '조 개수'에 맞춰 골고루 분배
                        if group_method == "조 개수로 나누기":
                            groups = [[] for _ in range(num_val)]
                            for idx, student in enumerate(shuffled_students):
                                groups[idx % num_val].append(student)
                                
                        # 로직 B: 정해진 '인원수'만큼 끊어서 분배
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
    st.info("👆 위쪽에 학생 명단 파일을 드래그해서 올려주세요.")
