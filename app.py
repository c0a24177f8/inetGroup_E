import streamlit as st
from status import render_status_card
from recent_usage import render_recent_usage
from action_button import render_contact_button
import chart
import data

st.set_page_config(page_title="ホットメーター", layout="centered")

st.markdown("""
<style>
    /* メイン画面をスマホサイズ（最大幅400px）に制限して中央寄せ */
    .block-container {
        max-width: 400px !important;
        padding-top: 2rem !important;
        padding-bottom: 2rem !important;
    }
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.subheader("ホットメーター")
    scenario = st.radio("表示シナリオ", ["通常", "異常"])

d = data.get(scenario)

st.title("ホットメーター")

# 1. ステータスカードの表示
render_status_card(d["status"]) 

# 2. タブとグラフの表示
tabs = st.tabs(["24時間"])
with tabs[0]: 
    chart.render_chart(d)

# 3. 直近の利用時間の表示
render_recent_usage(
    d["electricity"][-1], d["gas"][-1],
    sum(d["electricity"]) == 0, sum(d["gas"]) == 0,
)

# 4. ボタンの表示
render_contact_button(d["status"]) 