import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Activity Timer", layout="centered")

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Jua&display=swap');
    * { font-family: 'Jua', sans-serif !important; }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("⏱️ Activity Timer")
st.caption("조별 활동이나 문제 풀이 시간을 설정해 보세요! (최대 30분)")
st.markdown("---")

col1, col2 = st.columns(2)
with col1:
    set_mins = st.number_input("분 (Minutes)", min_value=0, max_value=30, value=5, step=1)
with col2:
    set_secs = st.number_input("초 (Seconds)", min_value=0, max_value=59, value=0, step=1)

total_seconds = set_mins * 60 + set_secs

html_code = f"""
<!DOCTYPE html>
<html>
<head>
    <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.6.0/dist/confetti.browser.min.js"></script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Jua&display=swap');
        body {{ font-family: 'Jua', sans-serif; display: flex; flex-direction: column; align-items: center; padding-top: 20px; }}
        .timer-wrapper {{ width: 280px; height: 280px; border-radius: 50%; background: #f0f2f6; display: flex; justify-content: center; align-items: center; box-shadow: 0px 4px 10px rgba(0,0,0,0.1); margin-bottom: 30px; position: relative; }}
        .bg-gradient {{ position: absolute; top: 0; left: 0; right: 0; bottom: 0; border-radius: 50%; background: conic-gradient(#FF85A2 100%, #f0f2f6 0); z-index: 1; }}
        .timer-inner {{ width: 240px; height: 240px; border-radius: 50%; background-color: white; display: flex; justify-content: center; align-items: center; font-size: 70px; color: #333; z-index: 2; }}
        .btn-group {{ display: flex; gap: 15px; }}
        button {{ font-family: 'Jua', sans-serif; font-size: 18px; padding: 10px 20px; border: 2px solid #FF85A2; border-radius: 8px; background-color: white; color: #FF85A2; cursor: pointer; transition: all 0.2s; }}
        button:hover {{ background-color: #FF85A2; color: white; }}
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
        
        // 효과음 파일 (웹에서 바로 재생 가능한 짧은 알림음)
        const alarmSound = new Audio('https://actions.google.com/sounds/v1/alarms/digital_watch_alarm_long.ogg');

        const display = document.getElementById('display');
        const bg = document.getElementById('bg');

        function updateDisplay() {{
            let m = Math.floor(timeLeft / 60);
            let s = timeLeft % 60;
            display.innerText = (m < 10 ? '0'+m : m) + ':' + (s < 10 ? '0'+s : s);
            let percent = totalTime > 0 ? (timeLeft / totalTime) * 100 : 0;
            bg.style.background = `conic-gradient(#FF85A2 ${{percent}}%, #f0f2f6 0)`;
        }}

        function startTimer() {{
            if (isRunning || timeLeft <= 0 || totalTime <= 0) return;
            isRunning = true;
            timerInterval = setInterval(() => {{
                timeLeft--;
                updateDisplay();
                if (timeLeft <= 0) {{
                    clearInterval(timerInterval);
                    isRunning = false;
                    // 효과음 재생
                    alarmSound.play();
                    // 폭죽 효과
                    confetti({{ particleCount: 150, spread: 70, origin: {{ y: 0.6 }} }});
                    alert("⏰ 시간이 다 되었습니다! 활동을 마무리해 주세요.");
                }}
            }}, 1000);
        }}

        function pauseTimer() {{ clearInterval(timerInterval); isRunning = false; }}
        function resetTimer() {{ clearInterval(timerInterval); isRunning = false; timeLeft = totalTime; updateDisplay(); }}

        updateDisplay();
    </script>
</body>
</html>
"""

components.html(html_code, height=450)
