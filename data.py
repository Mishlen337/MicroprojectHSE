import json
import config
import plotly
import html
import plotly.graph_objects as go
from datetime import datetime
def get_jitsiusers_data(name:str)->int:
    count = 0
    strMe = name
    with open(config.jitsiusers_path,"r") as file:
        line = file.readline()
        while line:
            data = json.loads(line)
            line = file.readline()
            try:
                if data["username"] == strMe:
                    count+=1
            except KeyError:
                pass
    return count

def get_git_data(name:str)->bool:
    user = False
    with open(config.git_path,"r") as file:
        total_message_count = 0
        current_message_count = 0
        message_dict = {}
        line = file.read()
        data = json.loads(line)
        print(data[0].keys())
        print(data[1])
        try:
            for item in data:
                if item['name'] == name:
                    print(len(item['projects']))
                    #break
        except KeyError:
            pass
        return message_dict,total_message_count

def get_zulip_data(name:str):
    total_message_count = 0
    current_message_count = 0
    message_dict = {'2021-01-01': 0}
    with open(config.zulip_path,"r") as file:
        line = file.read()
        data = json.loads(line)       
        try:
            for item in data:
                if item['full_name'] == name:
                    total_message_count = len(item['messages'])
                    for message in item['messages']:
                        current_message_count += 1       
                        message_dict[message['timestamp']] = current_message_count
        except KeyError:
            pass
        message_dict[str(datetime.isoformat(datetime.now(), sep='T'))] = current_message_count
        return message_dict,total_message_count


fig = go.Figure()
fig.add_trace(go.Scatter(x = list(get_zulip_data('Михаил Исаков')[0].keys()), y=list(get_zulip_data('Михаил Исаков')[0].values()),
                     line_shape='hv',
                    name='lines'))

fig.update_layout(title='Activity in MIEM Services',
                   xaxis_title='Time',
                   yaxis_title='Amount')
plotly.offline.plot(fig, include_plotlyjs=False, output_type='div')
fig.show()

#get_jitsiusers_data("maisakov@miem.hse.ru")
#print(get_git_data("Михаил Исаков"))
print(get_zulip_data('Михаил Исаков'))

        

    

