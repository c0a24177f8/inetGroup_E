import streamlit as st

@st.dialog("親に発信中")
def calling_parent():
    st.write("スマホだった場合実際にここで発信される")
    st.link_button("タップして接続", "tel:09000000000",use_container_width=True)

def render_contact_button(scenario: str):
    if scenario == "異常":
        st.markdown("""
        <style>
        div[data-testid="stButton"] button {
            background-color: #f05252;
            color: white;
            border: none;
            border-radius: 12px;
            padding: 16px;
            font-weight: bold;
            font-size: 20px;
            box-shadow: 0 4px 6px rgba(240, 82, 82, 0.3);
        }
        </style>
        """, unsafe_allow_html=True)
        if st.button("📞 今すぐ連絡する", use_container_width=True):
            calling_parent()