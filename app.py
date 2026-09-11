import streamlit as st
import pandas as pd
from status import render_status_card
from recent_usage import render_recent_usage
from action_button import render_contact_button
import chart # ← ここでグラフ用のファイルを読み込む

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

st.title("ホットメーター")
#st.caption("最終更新 2026/09/10 09:32")

# 1. ステータスカードの表示
render_status_card(scenario)

# --- データの読み込み ---
if scenario == "通常":
    df = pd.read_csv("data/normal_data.csv")
else:
    df = pd.read_csv("data/abnormal_data.csv")

last_row = df.iloc[-1]
elec_23 = last_row['Electricity_kWh']
gas_23 = last_row['Gas_m3']
elec_is_zero = (df['Electricity_kWh'].sum() == 0)
gas_is_zero = (df['Gas_m3'].sum() == 0)

# 2. タブとグラフの表示
tabs = st.tabs(["24時間"])
with tabs[0]: 
    chart.render_chart(df)

# 3. 直近の利用時間の表示
render_recent_usage(elec_23, gas_23, elec_is_zero, gas_is_zero)

# 4. ボタンの表示
render_contact_button(scenario)

with st.expander("お知らせ履歴"):
    st.write("準備中")