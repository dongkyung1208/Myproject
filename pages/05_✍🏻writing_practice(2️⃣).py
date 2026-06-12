import streamlit as st

st.set_page_config(page_title="Writing Practice", layout="centered")

# ---------------------------
# 세션 상태 초기화 (변수명에 _mid 추가하여 Low 단계와 분리)
# ---------------------------
if "wp_mid_stage" not in st.session_state:
    st.session_state.wp_mid_stage = 1
    st.session_state.wp_mid_wrongs = []

# ---------------------------
# 문제 데이터 세팅
# ---------------------------
step1_data = [
    {"q": "1. This shop mainly sells items (made / making) in Japan.", "trans": "이 가게는 주로 일본에서 만들어진 제품을 판매한다.", "options": ["made", "making"], "ans": "made"},
    {"q": "2. I have a dog (named / naming) Toto.", "trans": "나는 토토라는 이름을 가진 개가 있다.", "options": ["named", "naming"], "ans": "named"},
    {"q": "3. The boy (washes / washing) the dishes is my brother.", "trans": "설거지를 하고 있는 소년은 내 남동생이다.", "options": ["washes", "washing"], "ans": "washing"}
]

step2_data = [
    {"q": "1. 독성이 있다고 표시된 병을 만지지 마시오.", "base": "Don't _________________________.", "words": ["touch", "the bottles", "labeled", "poisonous"], "ans": ["touch", "the bottles", "labeled", "poisonous"]},
    {"q": "2. 사람들에게 사랑받는 그 배우는 곧 은퇴할 것이다.", "base": "The actor _________________________.", "words": ["is retiring soon", "loved by", "the people"], "ans": ["loved by", "the people", "is retiring soon"]},
    {"q": "3. 집에 남겨진 나의 개를 확인할 방법이 있나요?", "base": "Is there any way _________________________?", "words": ["left at home", "my dog", "to check on"], "ans": ["to check on", "my dog", "left at home"]},
    {"q": "4. 최고의 선수로 선정된 그 운동선수는 대학 장학금을 받았다.", "base": "The athlete _________________________ to university.", "words": ["won a scholarship", "selected as", "the best player"], "ans": ["selected as", "the best player", "won a scholarship"]}
]

step3_data = [
    {"q": "1. The advice ________ by my teacher was very helpful.", "trans": "(선생님께 받은 충고는 큰 도움이 되었다.)", "hint": "give", "ans": "given"},
    {"q": "2. This is the doctor ________ as the best in the country.", "trans": "(이 사람은 그 나라에서 최고라고 인정받는 의사이다.)", "hint": "recognize 또는 know", "ans": ["recognized", "known"]},
    {"q": "3. Many people ________ in Ireland eat potatoes as their staple food.", "trans": "(아일랜드에 사는 많은 사람들은 주식으로 감자를 먹는다.)", "hint": "live", "ans": "living"},
    {"q": "4. English is a language ________ in many countries.", "trans": "(영어는 많은 나라들에서 사용되는 언어이다.)", "hint": "speak", "ans": "spoken"},
    {"q": "5. The man ________ beside the door is my professor.", "trans": "(문 앞에 서 계시는 분은 우리 교수님이다.)", "hint": "stand", "ans": "standing"}
]

step4_data = [
    {"q": "The play writing by the French writer is very popular.", "prefix": "The play ", "suffix": " by the French writer is very popular.", "ans": "written"},
    {"q": "The boy runs around the playground is my nephew.", "prefix": "The boy ", "suffix": " around the playground is my nephew.", "ans": "running"},
    {"q": "We found the Easter egg hiding beneath the grass.", "prefix": "We found the Easter egg ", "suffix": " beneath the grass.", "ans": "hidden"},
    {"q": "He brought a basket filling with cookies.", "prefix": "He brought a basket ", "suffix": " with cookies.", "ans": "filled"},
    {"q": "The cat found a mouse catching in a trap.", "prefix": "The cat found a mouse ", "suffix": " in a trap.", "ans": "caught"}
]

# 다시 시작 버튼
if st.button("🔄 처음부터 다시 시작", key="reset_all_mid"):
    for key in list(st.session_state.keys()):
        if key.startswith("wp_mid") or key.startswith("s1_m") or key.startswith("s2_m") or key.startswith("s3_m") or key.startswith("s4_m"):
            del st.session_state[key]
    st.rerun()

st.title("✍️ Writing Practice (Step 1~4)")
st.progress(st.session_state.wp_mid_stage / 4.5)
st.markdown("---")

# ==========================================
# STEP 1
# ==========================================
if st.session_state.wp_mid_stage == 1:
    st.subheader("📌 STEP 1. 괄호 안에서 알맞은 말을 골라 봅시다.")
    for i, item in enumerate(step1_data):
        st.markdown(f"**{item['q']}**")
        st.caption(f"🇰🇷 해석: {item['trans']}")
        st.radio("정답:", item['options'], key=f"s1_m{i}", index=None, horizontal=True)
        st.markdown("---")
    if st.button("Step 1 채점하기"):
        for i, item in enumerate(step1_data):
            if st.session_state.get(f"s1_m{i}") != item['ans']:
                st.session_state.wp_mid_wrongs.append({"step": 1, "q": item['q'], "ans": item['ans']})
        st.session_state.wp_mid_stage = 1.5
        st.rerun()

elif st.session_state.wp_mid_stage == 1.5:
    st.subheader("🚨 Step 1 오답 확인")
    wrongs = [w for w in st.session_state.wp_mid_wrongs if w['step'] == 1]
    if not wrongs: st.success("대단해요! 모두 맞췄습니다. 🎉")
    else:
        for w in wrongs:
            st.write(f"❌ {w['q']}"); st.success(f"⭕ 정답: **{w['ans']}**"); st.markdown("---")
    if st.button("Step 2로 넘어가기"): st.session_state.wp_mid_stage = 2; st.rerun()

# ==========================================
# STEP 2
# ==========================================
elif st.session_state.wp_mid_stage == 2:
    st.subheader("📌 STEP 2. 괄호 안의 단어를 올바르게 배열해봅시다.")
    for i, item in enumerate(step2_data):
        st.write(f"**{item['q']}**"); st.write(item['base'])
        if f"s2_m_selected_{i}" not in st.session_state: st.session_state[f"s2_m_selected_{i}"] = []
        selected_words = st.session_state[f"s2_m_selected_{i}"]
        st.code(" ".join(selected_words) if selected_words else "(버튼을 눌러 단어를 채우세요)")
        cols = st.columns(len(item['words']))
        for j, word in enumerate(item['words']):
            with cols[j]:
                if st.button(word, key=f"btn_m_{i}_{j}", disabled=(word in selected_words)):
                    st.session_state[f"s2_m_selected_{i}"].append(word); st.rerun()
        if st.button("초기화", key=f"reset_m_{i}"): st.session_state[f"s2_m_selected_{i}"] = []; st.rerun()
        st.markdown("---")
    if st.button("Step 2 채점하기"):
        for i, item in enumerate(step2_data):
            if st.session_state.get(f"s2_m_selected_{i}", []) != item['ans']:
                st.session_state.wp_mid_wrongs.append({"step": 2, "q": item['q'], "ans": " ".join(item['ans'])})
        st.session_state.wp_mid_stage = 2.5; st.rerun()

elif st.session_state.wp_mid_stage == 2.5:
    st.subheader("🚨 Step 2 오답 확인")
    wrongs = [w for w in st.session_state.wp_mid_wrongs if w['step'] == 2]
    if not wrongs: st.success("완벽합니다! 모두 맞췄습니다. 🎉")
    else:
        for w in wrongs:
            st.write(f"❌ {w['q']}"); st.success(f"⭕ 정답: **{w['ans']}**"); st.markdown("---")
    if st.button("Step 3로 넘어가기"): st.session_state.wp_mid_stage = 3; st.rerun()

# ==========================================
# STEP 3
# ==========================================
elif st.session_state.wp_mid_stage == 3:
    st.subheader("📌 STEP 3. 빈칸에 알맞은 말을 써봅시다.")
    for i, item in enumerate(step3_data):
        st.markdown(f"**{item['q']}**"); st.caption(item['trans'])
        with st.expander("💡 동사 원형 힌트 보기"): st.write(f"👉 **{item['hint']}**")
        st.text_input("정답 입력:", key=f"s3_m{i}"); st.markdown("---")
    if st.button("Step 3 채점하기"):
        for i, item in enumerate(step3_data):
            user_ans = st.session_state.get(f"s3_m{i}", "").strip().lower()
            is_correct = (user_ans in item['ans']) if isinstance(item['ans'], list) else (user_ans == item['ans'])
            if not is_correct:
                correct_str = " / ".join(item['ans']) if isinstance(item['ans'], list) else item['ans']
                st.session_state.wp_mid_wrongs.append({"step": 3, "q": item['q'], "ans": correct_str})
        st.session_state.wp_mid_stage = 3.5; st.rerun()

elif st.session_state.wp_mid_stage == 3.5:
    st.subheader("🚨 Step 3 오답 확인")
    wrongs = [w for w in st.session_state.wp_mid_wrongs if w['step'] == 3]
    if not wrongs: st.success("훌륭해요! 모두 맞췄습니다. 🎉")
    else:
        for w in wrongs:
            st.write(f"❌ {w['q']}"); st.success(f"⭕ 정답: **{w['ans']}**"); st.markdown("---")
    if st.button("Step 4로 넘어가기"): st.session_state.wp_mid_stage = 4; st.rerun()

# ==========================================
# STEP 4 (전체 문장 볼드 피드백 적용)
# ==========================================
elif st.session_state.wp_mid_stage == 4:
    st.subheader("📌 STEP 4. 밑줄 친 부분을 어법상 바르게 고쳐 단어를 적어봅시다.")
    for i, item in enumerate(step4_data):
        st.markdown(f"**{item['q']}**")
        st.text_input("올바른 단어 입력:", key=f"s4_m{i}"); st.markdown("---")
    if st.button("최종 제출하기"):
        for i, item in enumerate(step4_data):
            if st.session_state.get(f"s4_m{i}", "").replace(" ", "").lower() != item['ans'].replace(" ", "").lower():
                st.session_state.wp_mid_wrongs.append({
                    "step": 4, 
                    "full_q": item['prefix'] + "**" + item['ans'] + "**" + item['suffix'], 
                    "ans": item['ans']
                })
        st.session_state.wp_mid_stage = 4.5; st.rerun()

elif st.session_state.wp_mid_stage == 4.5:
    st.subheader("🏆 최종 Review: 오답 복습")
    if not st.session_state.wp_mid_wrongs:
        st.balloons(); st.success("완벽해요! 🎉")
    else:
        for w in st.session_state.wp_mid_wrongs:
            if w['step'] == 4: st.write(f"❌ **{w['full_q']}**")
            else: st.write(f"**(Step {w['step']})** {w['q']} / 정답: **{w['ans']}**")
            st.markdown("---")
        hwp_content = "오답 노트\n"
        for w in st.session_state.wp_mid_wrongs:
            q = w['full_q'] if w['step'] == 4 else w['q']
            hwp_content += f"[Step {w['step']}] 문제: {q} / 정답: {w['ans']}\n"
        st.download_button("📄 틀린 문제 정리 파일 받기 (.hwp)", hwp_content.encode('utf-8'), "my_wrong_answers.hwp", "text/plain")
