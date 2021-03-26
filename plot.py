import plotly.graph_objects as go
from data import get_zulip_data, get_git_data, get_jitsiClasses_data, get_jitsiSession_data
import config
from cult_grade import cult_grade


import plotly.offline
import plot 
from airium import Airium
import config
from datetime import datetime

def form_html_plot():
    #initilize figure object
    fig = go.Figure()
    zulip_data = get_zulip_data(config.name)
    git_data = get_git_data(config.name)
    jitsiClasses_data = get_jitsiClasses_data(config.email)
    jitsiSession_data = get_jitsiSession_data(config.email)

    

    fig.add_trace(go.Bar(name = 'Zulip Activity',  x = list(zulip_data[0].keys()), y = list(zulip_data[0].values()),text=list(zulip_data[0].values()), textposition='auto'))
    
    fig.add_trace(go.Bar(name = 'GitLab Activity', x = list(git_data[0].keys()), y = list(git_data[0].values()),text=list(git_data[0].values()), textposition='auto'))

    fig.add_trace(go.Bar(name = 'JitsiClasses Activity', x = list(jitsiClasses_data[0].keys()), y = list(jitsiClasses_data[0].values()),text=list(jitsiClasses_data[0].values()), textposition='auto'))

    fig.add_trace(go.Bar(name = 'JitsiSession Activity', x = list(jitsiSession_data[0].keys()), y = list(jitsiSession_data[0].values()),text=list(jitsiSession_data[0].values()), textposition='auto'))

    fig.update_layout(title=f'Activity in MIEM Services. Name  - {config.name}',
                    
                    xaxis_title='Time',
                    yaxis_title='Amount',
                    barmode = 'group'
                    )
    fig.update_xaxes(
    dtick="M1",
    tickformat="%b-%Y")

    #Form html file
    a = Airium()
    a('<!DOCTYPE html>')
    

    with a.html():
        with a.head():
            with a.html(lang='en'):
                a.meta(charset='utf-8')
                a.title(_t=config.name)
                a.link(href='style.css', rel='stylesheet', type='text/css')
                a.script(src='https://cdn.plot.ly/plotly-latest.min.js')
                a.font('Courier New, monospace')
                #a.style()

        with a.body():
            a.append(plotly.offline.plot(fig, include_plotlyjs=False, output_type='div'))
            with a.font(size  = '3', face="Courier New, monospace", color = '#2a3f5f'):
                with a.table( align = 'center',  style = 'border-spacing: 100px 0px'):
                    with a.tr(klass='header_row'):
                        a.th(_t='Name of the service')
                        a.th(_t='Total action amount')
                        a.th(_t='Profile existence')

                    with a.tr():
                        a.td(_t='Zulip', align = 'center')
                        a.td(_t=zulip_data[1], align = 'center')
                        a.td(_t=zulip_data[2], align = 'center')

                    with a.tr():
                        a.td(_t='GitLab', align = 'center')
                        a.td(_t=git_data[1], align = 'center')
                        a.td(_t=git_data[2], align = 'center')

                    with a.tr():
                        a.td(_t='JitsiClasses', align = 'center')
                        a.td(_t=jitsiClasses_data[1], align = 'center')
                        a.td(_t= '-', align = 'center')  # can use _t or text

                    with a.tr():
                        a.td(_t='JitsiSession', align = 'center')
                        a.td(_t=jitsiSession_data[1], align = 'center')
                        a.td(_t='-', align = 'center')
                with a.h3(klass='main_header', align = 'center'):
                    a(f"Activity grade:  {cult_grade(zulip_data, git_data,jitsiClasses_data,jitsiSession_data)}" )
                with a.div(align = 'center'):
                    a(f"Данные актуальны на {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
                    
    html = str(a)
    with open(config.html_path, 'w') as f:
        f.write(str(html))