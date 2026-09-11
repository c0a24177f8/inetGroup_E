import streamlit as st

# ここが確実に4つの引数を受け取るようになっています
def render_recent_usage(elec_val, gas_val, elec_is_zero: bool, gas_is_zero: bool):
    
    # 電気がすべて0の場合の表示切替
    if elec_is_zero:
        elec_html = '<div style="color: #e53e3e; font-size: 14px; font-weight: bold;">最終利用：本日電気の利用がありません。</div>'
    else:
        elec_html = f'<div style="color: #4a5568; font-size: 14px;">最終利用 23:00 <strong style="font-size: 16px; color: #2d3748;">({elec_val} kWh)</strong></div>'
        
    # ガスがすべて0の場合の表示切替
    if gas_is_zero:
        gas_html = '<div style="color: #e53e3e; font-size: 14px; font-weight: bold;">最終利用：本日ガスの利用がありません。</div>'
    else:
        gas_html = f'<div style="color: #4a5568; font-size: 14px;">最終利用 23:00 <strong style="font-size: 16px; color: #2d3748;">({gas_val} m³)</strong></div>'

    html = f"""<div style="border: 1px solid #e2e8f0; border-radius: 12px; padding: 16px; margin-top: 10px; margin-bottom: 20px; background-color: #ffffff; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
<div style="font-weight: bold; color: #2c3e50; font-size: 16px; margin-bottom: 16px;">直近の利用時間</div>
<div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 12px; padding-bottom: 12px; border-bottom: 1px dashed #e2e8f0;">
<div style="display: flex; align-items: center; gap: 8px;">
<span style="font-size: 20px;">⚡</span>
<span style="font-weight: bold; color: #4a5568;">電気</span>
</div>
{elec_html}
</div>
<div style="display: flex; align-items: center; justify-content: space-between;">
<div style="display: flex; align-items: center; gap: 8px;">
<span style="font-size: 20px;">🔥</span>
<span style="font-weight: bold; color: #4a5568;">ガス</span>
</div>
{gas_html}
</div>
</div>"""
    st.markdown(html, unsafe_allow_html=True)