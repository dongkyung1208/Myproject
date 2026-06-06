import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Activity Timer", layout="centered")

# Streamlit 기본 텍스트에 귀여운 폰트(Jua) 적용
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Jua&display=swap');
    * {
        font-family: 'Jua', sans-serif !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("⏱️ Activity Timer")
st.caption("조별 활동/문제 풀이 시간을 설정해 보세요! (최대 30분)")

st.markdown("---")

# 1. 원하는 분과 초 설정창
col1, col2 = st.columns(2)
with col1:
    set_mins = st.number_input("분 (Minutes)", min_value=0, max_value=30, value=5, step=1)
with col2:
    set_secs = st.number_input("초 (Seconds)", min_value=0, max_value=59, value=0, step=1)

total_seconds = set_mins * 60 + set_secs

# 2. HTML과 JavaScript를 이용한 완벽한 타이머 (일시정지, 리셋 지원)
html_code = f"""
<!DOCTYPE html>
<html>
<head>
    <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.6.0/dist/confetti.browser.min.js"></script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Jua&display=swap');
        body {{
            font-family: 'Jua', sans-serif;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            margin: 0;
            padding-top: 20px;
        }}
        /* 동그란 타이머 바깥쪽 테두리 (회색 배경) */
        .timer-wrapper {{
            width: 280px; height: 280px;
            border-radius: 50%;
            background: #f0f2f6;
            display: flex; justify-content: center; align-items: center;
            box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
            margin-bottom: 30px;
            position: relative;
        }}
        /* 줄어드는 분홍색 테두리 */
        .bg-gradient {{
            position: absolute;
            top: 0; left: 0; right: 0; bottom: 0;
            border-radius: 50%;
            background: conic-gradient(#FF85A2 100%, #f0f2f6 0);
            z-index: 1;
        }}
        /* 타이머 안쪽 (하얀색 원) */
        .timer-inner {{
            width: 240px; height: 240px;
            border-radius: 50%;
            background-color: white;
            display: flex; justify-content: center; align-items: center;
            font-size: 70px; color: #333;
            z-index: 2;
        }}
        /* 버튼 디자인 */
        .btn-group {{
            display: flex; gap: 15px;
        }}
        button {{
            font-family: 'Jua', sans-serif;
            font-size: 18px;
            padding: 10px 20px;
            border: 2px solid #FF85A2;
            border-radius: 8px;
            background-color: white;
            color: #FF85A2;
            cursor: pointer;
            transition: all 0.2s;
            box-shadow: 0px 2px 5px rgba(0,0,0,0.05);
        }}
        button:hover {{
            background-color: #FF85A2;
            color: white;
            transform: translateY(-2px);
        }}
    </style>
</head>
<body>
    <div class="timer-wrapper">
        <div class="bg-gradient" id="bg"></div>
        <div class="timer-inner" id="display"></div>
    </div>
    
    <div class="btn-group">
        <button onclick="startTimer()">▶ 시작</button>
        <button onclick="pauseTimer()">⏸ 일시정지</button>
        <button onclick="resetTimer()">🔄 리셋</button>
    </div>

    <script>
        let totalTime = {total_seconds};
        let timeLeft = totalTime;
        let timerInterval = null;
        let isRunning = false;

        const display = document.getElementById('display');
        const bg = document.getElementById('bg');

        // 화면 업데이트 함수
        function updateDisplay() {{
            let m = Math.floor(timeLeft / 60);
            let s = timeLeft % 60;
            // 05:00 처럼 두 자리로 맞춤
            display.innerText = (m < 10 ? '0'+m : m) + ':' + (s < 10 ? '0'+s : s);
            
            // 남은 비율에 따라 분홍색 테두리 각도 계산
            let percent = totalTime > 0 ? (timeLeft / totalTime) * 100 : 0;
            bg.style.background = `conic-gradient(#FF85A2 ${{percent}}%, #f0f2f6 0)`;
        }}

        // 시작 버튼
        function startTimer() {{
            if (isRunning || timeLeft <= 0 || totalTime <= 0) return;
            isRunning = true;
            timerInterval = setInterval(() => {{
                timeLeft--;
                updateDisplay();
                
                // 시간이 0이 되었을 때
                if (timeLeft <= 0) {{
                    clearInterval(timerInterval);
                    isRunning = false;
                    setTimeout(() => {{
                        confetti({{ particleCount: 150, spread: 70, origin: {{ y: 0.6 }} }});
                        alert("⏰ 시간이 다 되었습니다! 활동을 마무리해 주세요.");
                    }}, 100);
                }}
            }}, 1000); // 1초마다 실행
        }}

        // 일시정지 버튼
        function pauseTimer() {{
            if (!isRunning) return;
            clearInterval(timerInterval);
            isRunning = false;
        }}

        // 리셋 버튼
        function resetTimer() {{
            clearInterval(timerInterval);
            isRunning = false;
            timeLeft = totalTime;
            updateDisplay();
        }}

        // 처음 화면 로딩 시 시계 표시
        updateDisplay();
    </script>
</body>
</html>
"""

# HTML 컴포넌트를 Streamlit 화면에 삽입 (높이를 넉넉하게 450으로 설정)
components.html(html_code, height=450)
