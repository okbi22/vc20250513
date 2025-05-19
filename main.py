import streamlit as st

# MBTI 데이터
mbti_data = {
    "INTJ": {
        "description": "🧠 전략가형 | 창의적이며 분석적인 완벽주의자입니다.",
        "best_match": "ENFP 🧡 자유로운 영혼",
        "worst_match": "ESFP ⚡ 즉흥적인 연예인",
        "color": "#9b59b6"
    },
    "INFP": {
        "description": "🌸 중재자형 | 조용하고 이상주의적인 감성파입니다.",
        "best_match": "ENFJ 💖 따뜻한 리더",
        "worst_match": "ESTJ 🔥 강한 리더형",
        "color": "#e84393"
    },
    "ENTP": {
        "description": "🚀 발명가형 | 창의적이고 토론을 즐기는 열정가입니다.",
        "best_match": "INFJ 🌌 신비로운 조력자",
        "worst_match": "ISFJ 🛡️ 헌신적인 수호자",
        "color": "#fdcb6e"
    },
    "ISFJ": {
        "description": "🛡️ 수호자형 | 조용하고 성실하며 책임감이 강합니다.",
        "best_match": "ESTP 🕶️ 액션파 실용주의자",
        "worst_match": "ENTP 🌪️ 변화무쌍한 도전자",
        "color": "#74b9ff"
    },
    # 추가 MBTI 유형도 여기에 계속...
}

st.set_page_config(page_title="🌟 MBTI 궁합 백과", page_icon="🔮", layout="centered")

st.title("🔮 MBTI 궁합 백과")
st.markdown("당신의 **MBTI 유형**을 선택하면, 그 유형의 성격 특징과 ❤️잘 맞는/⚡상극인 유형을 알려드릴게요!")
st.markdown("---")

selected_mbti = st.selectbox("🌟 당신의 MBTI는?", list(mbti_data.keys()))

if selected_mbti:
    data = mbti_data[selected_mbti]
    st.markdown(f"<div style='background-color:{data['color']}; padding:20px; border-radius:10px;'>"
                f"<h2 style='color:white;'>🧬 {selected_mbti}</h2>"
                f"<p style='color:white; font-size:18px;'>{data['description']}</p>"
                f"<p style='color:white; font-size:20px;'>✅ 잘 맞는 유형: <b>{data['best_match']}</b></p>"
                f"<p style='color:white; font-size:20px;'>❌ 상극 유형: <b>{data['worst_match']}</b></p>"
                f"</div>", unsafe_allow_html=True)
