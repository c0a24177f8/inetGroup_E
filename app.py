import streamlit as st
import data
import chart
import status

st.set_page_config(page_title="ほっとメーター", layout="centered")

with st.sidebar:
    st.subheader("ほっとメーター")
    scenario = st.radio("表示シナリオ", ["通常", "やや注意", "異常"])

d = data.get(scenario)

st.title("ほっとメーター")

status.render_status_card(scenario)

tab1, tab2, tab3 = st.tabs(["24時間", "7日間", "30日間"])
with tab1:
    st.plotly_chart(chart.build(d), use_container_width=True)
with tab2:
    st.write("準備中")
with tab3:
    st.write("準備中")

col1, col2 = st.columns(2)
col1.metric("電気 最終利用", d["last_electricity"])
col2.metric("ガス 最終利用", d["last_gas"])
if d["note"]:
    st.warning(d["note"])

st.link_button("今すぐ連絡する", "tel:09000000000", use_container_width=True)

with st.expander("お知らせ履歴（直近30日）"):
    st.write("準備中")