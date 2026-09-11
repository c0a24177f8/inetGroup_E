import streamlit as st
import data
import chart
import status

st.set_page_config(page_title="ほっとメーター", layout="centered")

st.markdown("""
<style>
[data-testid="stMainBlockContainer"] {
    max-width: 420px;
    padding-top: 2rem;
}
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.subheader("ほっとメーター")
    scenario = st.radio("表示シナリオ", ["通常", "異常"])

d = data.get(scenario)

st.title("ほっとメーター")

status.render_status_card(d["status"])

st.subheader("24時間の生活リズム")
st.plotly_chart(chart.build(d), use_container_width=True)

col1, col2 = st.columns(2)
col1.metric("電気 最終利用", d["last_electricity"])
col2.metric("ガス 最終利用", d["last_gas"])
if d["note"]:
    st.warning(d["note"])

st.link_button("今すぐ連絡する", "tel:09000000000", use_container_width=True)
