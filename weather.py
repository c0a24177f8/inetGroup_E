import requests
import streamlit as st

@st.cache_data(ttl=3600)
def get_current_temperature():
    """
    Open-Meteo APIを使って現在の東京の気温を取得
    """
    url = "https://api.open-meteo.com/v1/forecast?latitude=35.6895&longitude=139.6917&current_weather=true"
    try:
        response = requests.get(url, timeout=5)
        data = response.json()
        return data['current_weather']['temperature']
    except:
        # ダミーの真夏日データを返す
        return 36.5 

def render_heatstroke_card(temp):
    html = f"""
    <div style="
        background-color: #fff5f5;
        border: 1px solid #feb2b2;
        border-radius: 16px;
        padding: 16px 20px;
        display: flex;
        align-items: center;
        gap: 16px;
        margin-bottom: 20px;
        box-shadow: 0 4px 6px rgba(254, 178, 178, 0.2);
    ">
        <div style="
            background-color: #fc8181;
            width: 54px;
            height: 54px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 26px;
            flex-shrink: 0;
        ">
            ☀️
        </div>
        <div style="flex-grow: 1;">
            <div style="color: #9b2c2c; font-size: 20px; font-weight: bold; margin-bottom: 4px;">
                熱中症のキケンがあります
            </div>
            <div style="color: #9b2c2c; font-size: 15px; font-weight: bold; opacity: 0.9; margin-bottom: 8px;">
            外気温が {temp}℃ ですが、電気がほとんど使われていません。<br>
            <span style="font-size: 12px; font-weight: normal;">（エアコン停止の可能性）</span>
        
    </div>
    """
    st.markdown(html, unsafe_allow_html=True)
