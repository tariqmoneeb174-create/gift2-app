import streamlit as st
import time

st.set_page_config(
    page_title="باقة ورد",
    page_icon="💙",
    layout="centered"
)

st.markdown("""
    <style>
    .stApp {
        background-color: #0d1b2a;
    }
    div.stButton > button {
        background-color: #1b263b;
        color: #64dfdf;
        border: 2px solid #415a77;
        border-radius: 12px;
        font-size: 18px;
        padding: 10px 24px;
        transition: 0.3s;
    }
    div.stButton > button:hover {
        background-color: #415a77;
        color: #72efdd;
        border-color: #77abb7;
    }
    .blue-text {
        color: #48cae4;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

if 'step1' not in st.session_state:
    st.session_state.step1 = False

if 'step2' not in st.session_state:
    st.session_state.step2 = False

st.markdown("<h1 class='blue-text'>💙 انت نور؟ 💙</h1>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.button("لا", use_container_width=True, disabled=True, key="disabled_no")

with col2:
    if st.button("نعم", use_container_width=True, key="enabled_yes"):
        st.session_state.step1 = True

if st.session_state.step1:
    st.balloons()
    st.snow()

    st.markdown("---")
    st.markdown("<h3 class='blue-text'>💙 هاي الهدية الج لان تعبتي</h3>", unsafe_allow_html=True)

    if st.button("دوسي هنا 🎁", use_container_width=True, key="gift_btn"):
        st.session_state.step2 = True

if st.session_state.step2:
    with st.spinner("جاري تحضير الباقة... 💙"):
        time.sleep(1)

    st.image("garden-rose-red-pink-56866(1).avif",
             caption="❤️ أحلى وردة لاحلى ورداية بحياتي يتعبج السادس واني افرحج", use_container_width=True)
