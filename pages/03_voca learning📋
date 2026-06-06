import streamlit as st
import random
import pandas as pd

st.set_page_config(page_title="Lesson3의 Grammar Point 과거분사 마스터", layout="centered")

# ---------------------------
# 1. 단어 데이터 (제공된 PDF 기반)
# ---------------------------
raw_verb_data = [
    {"base": "begin", "past": "began", "pp": "begun", "mean": "시작하다"},
    {"base": "bear", "past": "bore", "pp": "born", "mean": "~을 낳다"},
    {"base": "bite", "past": "bit", "pp": "bitten", "mean": "물다"},
    {"base": "break", "past": "broke", "pp": "broken", "mean": "부수다"},
    {"base": "blow", "past": "blew", "pp": "blown", "mean": "불다"},
    {"base": "choose", "past": "chose", "pp": "chosen", "mean": "선택하다"},
    {"base": "do", "past": "did", "pp": "done", "mean": "하다"},
    {"base": "draw", "past": "drew", "pp": "drawn", "mean": "그리다"},
    {"base": "drink", "past": "drank", "pp": "drunk", "mean": "마시다"},
    {"base": "drive", "past": "drove", "pp": "driven", "mean": "운전하다"},
    {"base": "eat", "past": "ate", "pp": "eaten", "mean": "먹다"},
    {"base": "fall", "past": "fell", "pp": "fallen", "mean": "떨어지다"},
    {"base": "fly", "past": "flew", "pp": "flown", "mean": "날다"},
    {"base": "forgive", "past": "forgave", "pp": "forgiven", "mean": "용서하다"},
    {"base": "forget", "past": "forgot", "pp": "forgotten", "mean": "잊다"},
    {"base": "freeze", "past": "froze", "pp": "frozen", "mean": "얼다"},
    {"base": "give", "past": "gave", "pp": "given", "mean": "주다"},
    {"base": "get", "past": "got", "pp": "gotten", "mean": "얻다"},
    {"base": "go", "past": "went", "pp": "gone", "mean": "가다"},
    {"base": "grow", "past": "grew", "pp": "grown", "mean": "자라다"},
    {"base": "hide", "past": "hid", "pp": "hidden", "mean": "숨다"},
    {"base": "know", "past": "knew", "pp": "known", "mean": "알다"},
    {"base": "ride", "past": "rode", "pp": "ridden", "mean": "(말을)타다"},
    {"base": "ring", "past": "rang", "pp": "rung", "mean": "울리다"},
    {"base": "rise", "past": "rose", "pp": "risen", "mean": "오르다"},
    {"base": "see", "past": "saw", "pp": "seen", "mean": "보다"},
    {"base": "shake", "past": "shook", "pp": "shaken", "mean": "흔들다"},
    {"base": "show", "past": "showed", "pp": "shown", "mean": "보여주다"},
    {"base": "sing", "past": "sang", "pp": "sung", "mean": "노래하다"},
    {"base": "speak", "past": "spoke", "pp": "spoken", "mean": "말하다"},
    {"base": "steal", "past": "stole", "pp": "stolen", "mean": "훔치다"},
    {"base": "take", "past": "took", "pp": "taken", "mean": "가지다"},
    {"base": "throw", "past": "threw", "pp": "thrown", "mean": "던지다"},
    {"base": "write", "past": "wrote", "pp": "written", "mean": "쓰다"},
    {"base": "bring", "past": "brought", "pp": "brought", "mean": "가져오다"},
    {"base": "buy", "past": "bought", "pp": "bought", "mean": "사다"},
    {"base": "build", "past": "built", "pp": "built", "mean": "짓다"},
    {"base": "catch", "past": "caught", "pp": "caught", "mean": "잡다"},
    {"base": "feel", "past": "felt", "pp": "felt", "mean": "느끼다"},
    {"base": "fight", "past": "fought", "pp": "fought", "mean": "싸우다"},
    {"base": "find", "past": "found", "pp": "found", "mean": "발견하다"},
    {"base": "keep", "past": "kept", "pp": "kept", "mean": "간직하다"},
    {"base": "leave", "past": "left", "pp": "left", "mean": "떠나다"},
    {"base": "make", "past": "made", "pp": "made", "mean": "만들다"},
    {"base": "meet", "past": "met", "pp": "met", "mean": "만나다"},
    {"base": "sell", "past": "sold", "pp": "sold", "mean": "팔다"},
    {"base": "send", "past": "sent", "pp": "sent", "mean": "보내다"},
    {"base": "sit", "past": "sat", "pp": "sat", "mean": "앉다"},
    {"base": "sleep", "past": "slept", "pp": "slept", "mean": "자다"},
    {"base": "spend", "past": "spent", "pp": "spent", "mean": "소비하다"},
    {"base": "stand", "past": "stood", "pp": "stood", "mean": "서다"},
    {"base": "teach", "past": "taught", "pp": "taught", "mean": "가르치다"},
    {"base": "tell", "past": "told", "pp": "told", "mean": "말하다"},
    {"base": "think", "past": "thought", "pp": "thought", "mean": "생각하다"},
    {"base": "understand", "past": "understood", "pp": "understood", "mean": "이해하다"},
    {"base": "win", "past": "won", "pp": "won", "mean": "이기다"}
]

# ---------------------------
# 2. 세션 상태 초기화 및 문제 세팅
# ---------------------------
if "stage" not in st.session_state:
    st.session_state.stage = 1
    
    # 1단계, 2단계 문제를 위해 40개를 뽑고 반으로 나눔
    random.shuffle(raw_verb_data)
    st.session_state.step1_qs = raw_verb_data[:20]
    st.session_state.step2_qs = raw_verb_data[20:40]
    st.session_state.wrong_words = []  # 틀린 단어들 저장용
    
    # Step 1 보기(객관식) 생성
    all_pps = [v["pp"] for v in raw_verb_data]
    for q in st.session_state.step1_qs:
        wrong_choices = random.sample([p for p in all_pps if p != q["pp"]], 3)
        choices = wrong_choices + [q["pp"]]
        random.shuffle(choices)
        q["choices"] = choices

# ---------------------------
# 힌트 생성 함수 (Step 2용)
# ---------------------------
def get_hint(word):
    if len(word) <= 3:
        return word[0] + ("_" * (len(word) - 1))
    else:
        return word[:2] + ("_" * (len(word) - 2))

# ---------------------------
# 화면 타이틀
# ---------------------------
st.title("🏆 과거분사 마스터가 되는 그날까지!")
st.caption("🔥Step 1부터 차근차근 풀면서 과거분사를 외워봅시다🔥")

# 다시 시작 버튼
if st.button("🔄 처음부터 다시 시작"):
    for key in list(st.session_state.keys()):
        del st.session_state[key]
    st.rerun()

st.markdown("---")

# ---------------------------
# Step 1: 객관식 (20문제)
# ---------------------------
if st.session_state.stage == 1:
    st.subheader("📌 Step 1: 알맞은 과거분사 고르기")
    st.info("주어진 동사 원형의 '과거분사(p.p)' 형태를 4개의 보기 중 골라주세요.")
    
    for i, q in enumerate(st.session_state.step1_qs):
        st.write(f"**{i+1}. {q['base']} ({q['mean']})**")
        st.radio("정답 선택", q["choices"], key=f"s1_{i}", index=None, label_visibility="collapsed")
        st.markdown("---")
        
    if st.button("Step 1 제출하기"):
        wrong_list = []
        for i, q in enumerate(st.session_state.step1_qs):
            if st.session_state.get(f"s1_{i}") != q["pp"]:
                wrong_list.append(q)
                
        st.session_state.wrong_words.extend(wrong_list)
        st.session_state.stage = 2
        st.rerun()

# ---------------------------
# Step 2: 일부 주관식 (20문제)
# ---------------------------
elif st.session_state.stage == 2:
    st.subheader("📌 Step 2: 빈칸 채워 넣기")
    st.info("제시된 힌트를 보고 알맞은 과거분사를 직접 타이핑해 보세요.")
    
    for i, q in enumerate(st.session_state.step2_qs):
        hint = get_hint(q["pp"])
        st.write(f"**{i+1}. {q['base']} ({q['mean']})**")
        st.write(f"👉 힌트: `{hint}` (총 {len(q['pp'])}글자)")
        st.text_input("정답 입력", key=f"s2_{i}", label_visibility="collapsed")
        st.markdown("---")
        
    if st.button("Step 2 제출하기"):
        wrong_list = []
        for i, q in enumerate(st.session_state.step2_qs):
            ans = st.session_state.get(f"s2_{i}", "").strip().lower()
            if ans != q["pp"]:
                wrong_list.append(q)
                
        st.session_state.wrong_words.extend(wrong_list)
        st.session_state.stage = 2.5
        st.rerun()

# ---------------------------
# Pre-Step 3: 오답 복습
# ---------------------------
elif st.session_state.stage == 2.5:
    st.subheader("🚨 잠깐! Step 3로 가기 전에 복습해요")
    
    if len(st.session_state.wrong_words) == 0:
        st.balloons()
        st.success("Perfect! Step 1, 2에서 틀린 문제가 하나도 없습니다! 바로 전체 복습으로 넘어갑니다💯")
        if st.button("전체 단어 리스트 보기"):
            st.session_state.stage = 4
            st.rerun()
    else:
        st.warning(f"Step 1과 Step 2에서 총 **{len(st.session_state.wrong_words)}개**의 단어를 틀렸습니다. 아래 리스트를 보고 확실히 외운 뒤 다음으로 넘어가세요!")
        
        for idx, w in enumerate(st.session_state.wrong_words):
            st.write(f"{idx+1}. **{w['base']}** ➡️ **{w['pp']}** ({w['mean']})")
            
        if st.button("다 외웠습니다! Step 3(재시험) 도전"):
            st.session_state.stage = 3
            st.rerun()

# ---------------------------
# Step 3: 오답 주관식 재시험
# ---------------------------
elif st.session_state.stage == 3:
    st.subheader("📌 Step 3: 내가 틀린 단어 완벽 정복")
    st.info("앞서 틀렸던 단어들입니다. 힌트 없이 완벽하게 과거분사를 적어보세요!")
    
    for i, q in enumerate(st.session_state.wrong_words):
        st.write(f"**{i+1}. {q['base']} ({q['mean']})**")
        st.text_input("정답 입력", key=f"s3_{i}", label_visibility="collapsed")
        st.markdown("---")
        
    if st.button("최종 제출하기"):
        final_wrong = 0
        for i, q in enumerate(st.session_state.wrong_words):
            ans = st.session_state.get(f"s3_{i}", "").strip().lower()
            if ans != q["pp"]:
                final_wrong += 1
                
        if final_wrong > 0:
            st.error(f"아직 {final_wrong}개를 틀렸네요! 😭 결과를 확인하고 전체 리스트에서 다시 복습하세요.")
        else:
            st.balloons()
            st.success("Perfect! 틀린 단어를 모두 맞췄어요! 🎉")
            
        if st.button("마지막 전체 Review로 넘어가기"):
            st.session_state.stage = 4
            st.rerun()

# ---------------------------
# Review: 전체 리스트 보기
# ---------------------------
elif st.session_state.stage == 4:
    st.subheader("📚 Review: 과거분사 전체 리스트")
    st.caption("제시되었던 동사들의 3단 변화와 뜻을 전체적으로 확인해 보세요.")
    
    # 데이터를 표 형식(DataFrame)으로 예쁘게 보여줌
    df = pd.DataFrame(raw_verb_data)
    df.columns = ["동사 원형(Base)", "과거(Past)", "과거분사(P.P)", "뜻(Meaning)"]
    
    # 인덱스 숨기고 테이블 출력
    st.dataframe(df, use_container_width=True, hide_index=True)
    
    st.success("수고하셨습니다! 과거분사 학습을 모두 마쳤습니다.")
