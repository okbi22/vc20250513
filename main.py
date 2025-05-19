import streamlit as st

mbti_data = {
    "INTJ": {
        "description": "🧠 전략가형 | 창의적이며 분석적인 완벽주의자입니다.",
        "best_match": "ENFP 🧡 자유로운 영혼",
        "worst_match": "ESFP ⚡ 즉흥적인 연예인",
        "color": "#9b59b6"
    },
    "INTP": {
        "description": "🔍 논리사색형 | 호기심 많고 이론적인 분석가입니다.",
        "best_match": "ENTJ 👩‍🚀 결단력 있는 리더",
        "worst_match": "ESFJ 🎭 감정 우선 사교가",
        "color": "#1abc9c"
    },
    "ENTJ": {
        "description": "🚀 지도자형 | 야망 있고 체계적인 리더입니다.",
        "best_match": "INFP 🌸 이상주의 중재자",
        "worst_match": "ISFP 🌿 자유로운 영혼",
        "color": "#e74c3c"
    },
    "ENTP": {
        "description": "🌪️ 발명가형 | 창의적이고 논쟁을 즐기는 도전자입니다.",
        "best_match": "INFJ 🌌 조용한 비전가",
        "worst_match": "ISFJ 🛡️ 헌신적 수호자",
        "color": "#f1c40f"
    },
    "INFJ": {
        "description": "🌌 선의의 옹호자형 | 통찰력 있고 깊이 있는 이상주의자입니다.",
        "best_match": "ENFP 🎨 감성적 낙천가",
        "worst_match": "ESTP 🏍️ 모험가 현실주의자",
        "color": "#8e44ad"
    },
    "INFP": {
        "description": "🌸 중재자형 | 조용하고 이상주의적인 감성파입니다.",
        "best_match": "ENFJ 💖 따뜻한 리더",
        "worst_match": "ESTJ 🔥 강한 리더형",
        "color": "#e84393"
    },
    "ENFJ": {
        "description": "🌞 정의로운 사회운동가형 | 타인을 이끄는 감성적 리더입니다.",
        "best_match": "INFP 💫 감성적 중재자",
        "worst_match": "ISTP 🔧 무심한 관찰자",
        "color": "#ff7675"
    },
    "ENFP": {
        "description": "🎨 재기발랄한 활동가형 | 열정적이고 창의적인 낙천주의자입니다.",
        "best_match": "INFJ 🌌 깊이 있는 직관가",
        "worst_match": "ISTJ 📋 현실적 관리자",
        "color": "#fab1a0"
    },
    "ISTJ": {
        "description": "📋 관리자형 | 현실적이고 신뢰할 수 있는 책임자입니다.",
        "best_match": "ESFP 🎤 사교적 연예인",
        "worst_match": "ENFP 🎨 감성적 낙천가",
        "color": "#34495e"
    },
    "ISFJ": {
        "description": "🛡️ 수호자형 | 조용하고 성실하며 책임감이 강합니다.",
        "best_match": "ESTP 🕶️ 액션파 실용주의자",
        "worst_match": "ENTP 🌪️ 변화무쌍한 도전자",
        "color": "#74b9ff"
    },
    "ESTJ": {
        "description": "⚖️ 경영자형 | 체계적이고 통솔력이 강한 지도자입니다.",
        "best_match": "ISFP 🌿 조용한 예술가",
        "worst_match": "INFP 🌸 감성적 이상주의자",
        "color": "#d35400"
    },
    "ESFJ": {
        "description": "🎭 사교적 외교관형 | 따뜻하고 타인을 잘 챙기는 유형입니다.",
        "best_match": "ISFP 🌱 자유로운 감성형",
        "worst_match": "INTP 🔍 분석적 논리형",
        "color": "#f39c12"
    },
    "ISTP": {
        "description": "🔧 장인형 | 냉철하고 문제 해결에 능한 실용주의자입니다.",
        "best_match": "ESFJ 🎭 외향적 돌봄형",
        "worst_match": "ENFJ 🌞 감성 리더",
        "color": "#2c3e50"
    },
    "ISFP": {
        "description": "🌿 예술가형 | 조용하고 감성적인 자연인입니다.",
        "best_match": "ESTJ ⚖️ 현실적 리더",
        "worst_match": "ENTJ 🚀 통솔형",
        "color": "#16a085"
    },
    "ESTP": {
        "description": "🏍️ 사업가형 | 에너지 넘치고 현실적인 실행자입니다.",
        "best_match": "ISFJ 🛡️ 조용한 보호자",
        "worst_match": "INFJ 🌌 직관적 이상가",
        "color": "#e67e22"
    },
    "ESFP": {
        "description": "🎤 연예인형 | 사교적이고 삶을 즐기는 낙천주의자입니다.",
        "best_match": "ISTJ 📋 현실적 계획가",
        "worst_match": "INTJ 🧠 전략가",
        "color": "#f368e0"
    }
}

st.set_page_config(page_title="🌟 MBTI 궁합 백과", page_icon="🔮", layout="centered")

st.title("🔮 MBTI 궁합 백과")
st.markdown("당신의 **MBTI 유형**을 선택하면, 그 유형의 성격 특징과 ❤️잘 맞는/⚡상극인 유형을 알려드릴게요!")
st.markdown("---")

selected_mbti = st.selectbox("🌟 당신의 MBTI는?", list(mbti_data.keys()))

if selected_mbti:
    data = mbti_data[selected_mbti]
    st.markdown(
        f"<div style='background-color:{data['color']}; padding:20px; border-radius:10px;'>"
        f"<h2 style='color:white;'>🧬 {selected_mbti}</h2>"
        f"<p style='color:white; font-size:18px;'>{data['description']}</p>"
        f"<p style='color:white; font-size:20px;'>✅ 잘 맞는 유형: <b>{data['best_match']}</b></p>"
        f"<p style='color:white; font-size:20px;'>❌ 상극 유형: <b>{data['worst_match']}</b></p>"
        f"</div>",
        unsafe_allow_html=True
    )
