import plotly.graph_objects as go
from data import get_zulip_data, get_git_data, get_jitsiClasses_data, get_jitsiSession_data

def form_plot():
    #initilize figure object
    fig = go.Figure()
    zulip_data = get_zulip_data('Михаил Исаков')[0]
    git_data = get_git_data('Михаил Исаков')[0]
    jitsiClasses_data = get_jitsiClasses_data('maisakov@miem.hse.ru')[0]
    jitsiSession_data = get_jitsiSession_data('kkgaluzina@miem.hse.ru')[0]

    fig.add_trace(go.Bar(name = 'Zulip Activity', x = list(zulip_data.keys()), y = list(zulip_data.values()),text=list(zulip_data.values()), textposition='auto'))
    
    fig.add_trace(go.Bar(name = 'GitLab Activity', x = list(git_data.keys()), y = list(git_data.values()),text=list(git_data.values()), textposition='auto'))

    fig.add_trace(go.Bar(name = 'JitsiClasses Activity', x = list(jitsiClasses_data.keys()), y = list(jitsiClasses_data.values()),text=list(jitsiClasses_data.values()), textposition='auto'))

    fig.add_trace(go.Bar(name = 'JitsiSession Activity', x = list(jitsiSession_data.keys()), y = list(jitsiSession_data.values()),text=list(jitsiSession_data.values()), textposition='auto'))

    fig.update_layout(title='Activity in MIEM Services',
                    xaxis_title='Time',
                    
                    yaxis_title='Amount',
                    barmode = 'group'
                    )
    fig.update_xaxes(
    dtick="M1",
    tickformat="%b-%Y")
    #plotly.offline.plot(fig, include_plotlyjs=False, output_type='div')
    fig.show()

form_plot()
