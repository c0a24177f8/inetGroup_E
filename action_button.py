import streamlit as st

def render_contact_button(scenario: str):
    # 異常シナリオの時のみボタンを表示
    if scenario == "異常":
        # divタグをspanとbr（改行）に変更して分裂を防ぐ
        html = """
        <a href="tel:09000000000" style="display: block; background-color: #f05252; color: white; text-align: center; padding: 16px; border-radius: 12px; text-decoration: none; margin-top: 10px; margin-bottom: 20px; box-shadow: 0 4px 6px rgba(240, 82, 82, 0.3);">
            <span style="font-weight: bold; font-size: 20px;">📞 今すぐ連絡する</span><br>
            <span style="font-size: 12px; opacity: 0.9;">電話・メッセージ・LINEなど</span>
        </a>
        """
        st.markdown(html, unsafe_allow_html=True)