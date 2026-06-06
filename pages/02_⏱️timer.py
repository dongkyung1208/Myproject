import streamlit as st
import time

st.set_page_config(page_title="Activity Timer", layout="centered")

# 귀여운 폰트 적용 (Jua)
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Jua&display=swap');
    * {
        font-family: 'Jua', sans-serif;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("⏱️ Activity Timer")
st.caption("조별 활동/문제 풀이 시간을 설정해 보세요! (최대 30분)")

st.markdown("---")

# 1. 원하는 분과 초 설정창 (좌우로 배치)
col1, col2 = st.columns(2)
with col1:
    set_mins = st.number_input("분 (Minutes)", min_value=0, max_value=30, value=5, step=1)
with col2:
    set_secs = st.number_input("초 (Seconds)", min_value=0, max_value=59, value=0, step=1)

total_seconds = set_mins * 60 + set_secs

# 2. 타이머가 그려질 빈 공간(Placeholder) 마련
timer_placeholder = st.empty()

# 동그란 타이머를 그려주는 함수 (HTML/CSS 활용)
def draw_timer(time_left, total_time):
    # 남은 시간의 비율(%) 계산
    if total_time == 0:
        percent = 0
    else:
        percent = (time_left / total_time) * 100
        
    mins, secs = divmod(time_left, 60)
    time_format = f"{mins:02d}:{secs:02d}"  # 05:00 형태로 맞춤
    
    # 분홍색(#FF85A2) 테두리가 줄어드는 원형 시계 CSS
    html_code = f"""
    <div style="display: flex; justify-content: center; margin-top: 20px; margin-bottom: 30px;">
        <div style="
            width: 280px; height: 280px; 
            border-radius: 50%; 
            background: conic-gradient(#FF85A2 {percent}%, #f0f2f6 0);
            display: flex; justify-content: center; align-items: center;
            box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
        ">
            <div style="
                width: 240px; height: 240px; 
                border-radius: 50%; 
                background-color: white; 
                display: flex; justify-content: center; align-items: center;
                font-size: 70px; color: #333;
            ">
                {time_format}
            </div>
        </div>
    </div>
    """
    return html_code

# 시작 전에는 기본 설정된 시간을 화면에 띄워둠
timer_placeholder.markdown(draw_timer(total_seconds, total_seconds), unsafe_allow_html=True)

# 3. 타이머 시작 버튼
col_btn1, col_btn2, col_btn3 = st.columns([1, 1, 1])
with col_btn2:
    start_button = st.button("🚀 타이머 시작!", use_container_width=True)

# 버튼을 누르면 타이머 작동
if start_button:
    if total_seconds > 0:
        for i in range(total_seconds, -1, -1):
            # 1초마다 빈 공간의 HTML(시간 및 테두리 비율)을 새롭게 업데이트
            timer_placeholder.markdown(draw_timer(i, total_seconds), unsafe_allow_html=True)
            time.sleep(1) # 1초 대기
        
        # 타이머가 0이 되면 축하 효과와 메시지 출력
        st.balloons()
        st.success("⏰ 시간이 다 되었습니다! 활동을 마무리하고 선생님을 봐주세요👀")
    else:
        st.error("시간을 1초 이상 설정해 주세요!")
