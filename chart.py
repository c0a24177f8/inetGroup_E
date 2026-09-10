import plotly.graph_objects as go

def build(d):
    x = d["hours"]
    fig = go.Figure()

    #ガス
    fig.add_trace(go.Bar(
        x=x, y=d["gas"], name="ガス (m³)",
        marker_color="#7EB6E8", yaxis="y2", opacity=0.85,
    ))

    #電気
    fig.add_trace(go.Scatter(
        x=x, y=d["electricity"], name="電気 (kWh)",
        line=dict(color="#F0A22E", width=2.5),
    ))

    fig.update_layout(
        height=320,
        margin=dict(l=10, r=10, t=10, b=10),
        yaxis=dict(title="電気 (kWh)", range=[0, 2.0]),
        yaxis2=dict(title="ガス (m³)", overlaying="y", side="right",
                    range=[0, 0.8], showgrid=False),
        xaxis=dict(tickmode="array",
                   tickvals=["0:00", "6:00", "12:00", "18:00", "23:00"]),
        legend=dict(orientation="h", y=1.12, x=0),
        plot_bgcolor="white",
    )
    return fig
