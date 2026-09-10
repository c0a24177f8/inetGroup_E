import streamlit as st

def render_status_card(scenario: str):
    # シナリオごとの設定データ
    status_config = {
        "通常": {
            "bg_color": "#eef7ed",
            "border_color": "#c3e6cb",
            "text_color": "#1e6043",
            "icon_bg": "#a2d8a5",
            "icon": "💡",
            "title": "お元気です",
            "subtitle": "いつも通りの生活リズムです",
        },
        "やや注意": {
            "bg_color": "#fff8e6",
            "border_color": "#ffeba8",
            "text_color": "#8a6d3b",
            "icon_bg": "#fce18a",
            "icon": "⚠️",
            "title": "やや注意が必要です",
            "subtitle": "生活リズムに少し変化が見られます",
        },
        "異常": {
            "bg_color": "#fdf2f2",
            "border_color": "#f8b4b4",
            "text_color": "#9b1c1c",
            "icon_bg": "#f87171",
            "icon": "🚨",
            "title": "異常を検知しました",
            "subtitle": "確認または連絡を行ってください",
        },
    }

    # デフォルトは「通常」に設定
    config = status_config.get(scenario, status_config["通常"])

    # HTML/CSSでカード風UIを描画
    card_html = f"""
    <div style="
        background-color: {config['bg_color']};
        border: 1px solid {config['border_color']};
        border-radius: 16px;
        padding: 16px 20px;
        display: flex;
        align-items: center;
        gap: 16px;
        margin-bottom: 20px;
    ">
        <div style="
            background-color: {config['icon_bg']};
            width: 54px;
            height: 54px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 26px;
            flex-shrink: 0;
        ">
            {config['icon']}
        </div>
        <div style="flex-grow: 1;">
            <div style="
                color: {config['text_color']};
                font-size: 20px;
                font-weight: bold;
                margin-bottom: 4px;
            ">{config['title']}</div>
            <div style="
                color: {config['text_color']};
                font-size: 15px;
                font-weight: bold;
                opacity: 0.9;
                margin-bottom: 8px;
            ">{config['subtitle']}</div>
            <div style="
                color: #718096;
                font-size: 11px;
            ">最終更新 10/25 09:32</div>
        </div>
    </div>
    """
    st.markdown(card_html, unsafe_allow_html=True)