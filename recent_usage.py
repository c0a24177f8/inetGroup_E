import streamlit as st

def _detail_html(last, unit):
    """最終利用の右側に出す文言。last は {"time":..., "value":...} か None"""
    if last is None:
        return (
            '<div style="color: #e53e3e; font-size: 14px; font-weight: bold;">'
            '本日の利用がありません</div>'
        )
    return (
        f'<div style="color: #4a5568; font-size: 14px;">最終利用 {last["time"]} '
        f'<strong style="font-size: 16px; color: #2d3748;">'
        f'({last["value"]:g} {unit})</strong></div>'
    )


def render_recent_usage(last_electricity, last_gas):
    elec_html = _detail_html(last_electricity, "kWh")
    gas_html = _detail_html(last_gas, "m³")
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