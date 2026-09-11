import streamlit as st
from status import render_status_card
from recent_usage import render_recent_usage
from action_button import render_contact_button
import chart
import status
import base64
import data


st.set_page_config(page_title="ホットメーター", layout="centered")

def get_image_base64(path):
    with open(path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()
img_base64 = get_image_base64("static/ほっとメーター.png")

st.markdown("""
<style>
[data-testid="stMainBlockContainer"] {
    max-width: 420px;
    padding-top: 4rem;
    padding-bottom: 90px;
}

.app-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding-top: 1rem;
    padding-bottom: 12px;
    margin-bottom: 16px;
}
.header-left {
    display: flex;
    align-items: center;
    gap: 8px;
    color: #1e6043;
    font-weight: bold;
    font-size: 20px;
}
.header-left i {
    font-size: 22px;
}
.header-right i {
    color: #1e6043;
    font-size: 22px;
    cursor: pointer;
}

.bottom-nav {
    position: fixed;
    bottom: 0;
    left: 50%;
    transform: translateX(-50%);
    width: 100%;
    max-width: 420px;
    background-color: #ffffff;
    border-top: 1px solid #e2e8f0;
    padding: 8px 0;
    z-index: 999;
}

.nav-item {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    text-decoration: none;
    color: #718096;
    font-size: 11px;
}
.nav-item.active {
    color: #1e6043;
    font-weight: bold;
}
.nav-icon {
    font-size: 20px;
    line-height: 1.2;
}

.header-logo {
    height: 50px; /* ロゴの大きさ変えれる */
    width: auto;
    object-fit: contain;
}
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

st.markdown(f"""
<div class="app-header">
    <div class="header-left">
        <img src="data:image/png;base64,{img_base64}" class="header-logo" alt="ロゴ">
        <span>ほっとメーター</span>
    </div>
</div>
""", unsafe_allow_html=True)


# 1. ステータスカードの表示
render_status_card(d["status"]) 

# 2. ボタンの表示
render_contact_button(d["status"]) 

# 3. タブとグラフの表示
tabs = st.tabs(["24時間"])
with tabs[0]: 
    chart.render_chart(d)

# 4. 直近の利用時間の表示
render_recent_usage(
    d["electricity"][-1], d["gas"][-1],
    sum(d["electricity"]) == 0, sum(d["gas"]) == 0,
)

st.markdown("""
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">

<style>
.nav-item {
    color: #94a3b8 !important;
    text-decoration: none !important; 
}
.nav-item * {
    text-decoration: none !important; 
}

.nav-item.active {
    color: #1e6043 !important;
    font-weight: bold;
}

.nav-icon-fa {
    font-size: 22px;
    margin-bottom: 3px;
    display: block; 
}
</style>

<div class="bottom-nav">
    <div style="display: flex; justify-content: space-around; text-align: center;">
        <a href="#" class="nav-item active">
            <i class="fa-solid fa-house nav-icon-fa"></i>
            <span>ホーム</span>
        </a>
        <a href="#" class="nav-item">
            <i class="fa-solid fa-chart-simple nav-icon-fa"></i>
            <span>グラフ</span>
        </a>
        <a href="#" class="nav-item">
            <i class="fa-regular fa-bell nav-icon-fa"></i>
            <span>お知らせ</span>
        </a>
        <a href="#" class="nav-item">
            <i class="fa-solid fa-gear nav-icon-fa"></i>
            <span>設定</span>
        </a>
    </div>
</div>
""", unsafe_allow_html=True)
