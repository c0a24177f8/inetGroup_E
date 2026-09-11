import streamlit as st
import plotly.graph_objects as go

def render_chart(d):
    fig = go.Figure()
    
    # 電気のグラフ（黄色の線）
    fig.add_trace(go.Scatter(
        x=d["hours"], y=d["electricity"],
        mode='lines', name='電気 (kWh)', 
        line=dict(color='#ecc94b', width=3),
        fill='tozeroy', fillcolor='rgba(236, 201, 75, 0.1)' # 下を少し塗りつぶす
    ))
    
    # ガスのグラフ（青色の線）
    fig.add_trace(go.Scatter(
        x=d["hours"], y=d["gas"],
        mode='lines', name='ガス (m³)', 
        line=dict(color='#4299e1', width=3),
        fill='tozeroy', fillcolor='rgba(66, 153, 225, 0.1)',
        yaxis='y2' # 右側のメモリを使う設定
    ))
    
    # グラフの見た目の調整
    fig.update_layout(
        margin=dict(l=0, r=0, t=10, b=0),
        height=300,
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        yaxis=dict(title='電気 (kWh)', range=[0, 1.5], showgrid=True, gridcolor='#f0f0f0'),
        yaxis2=dict(title='ガス (m³)', range=[0, 0.6], overlaying='y', side='right', showgrid=False),
        plot_bgcolor='white'
    )
    
    # Streamlitに描画
    st.plotly_chart(fig, use_container_width=True)