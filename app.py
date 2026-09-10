import streamlit as st

st.set_page_config(page_title="ホットメーター", layout="centered")

with st.sidebar:
    st.subheader("ホットメーター")
    scenario = st.radio("表示シナリオ", ["通常", "やや注意", "異常"])

st.title("ホットメーター")
st.caption("最終更新 2026/09/10 09:32")

st.info("ここにステータス帯")

tab1, tab2, tab3 = st.tabs(["24時間", "7日間", "30日間"])
with tab1:
    st.write("ここにグラフ")


st.link_button("今すぐ連絡する", "tel:09000000000", use_container_width=True)

with st.expander("お知らせ履歴"):
    st.write("準備中")