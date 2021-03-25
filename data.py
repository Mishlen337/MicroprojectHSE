import json
import config
from datetime import datetime
def get_jitsiSession_data(email:str):
    total_visits_count = 0
    visits_dict = {}
    postern_date = '2021-01'
    with open(config.jitsiSession_path,"r") as file:
        line = file.read()
        data = json.loads(line)
        try:
            for item in data:
                if 'project' in item['room'] and item['username'] == email:
                    visits_dict.setdefault(postern_date, 0)
                    visits_dict[postern_date] += 1
                    total_visits_count +=1

        except KeyError:
            pass
    return visits_dict,total_visits_count

def get_jitsiClasses_data(email:str):
    total_visits_count = 0
    visits_dict = {}
    with open(config.jitsiClasses_path,"r") as file:
        line = file.read()
        data = json.loads(line)
        try:
            for item in data:
                for auditorium in item['auditoriums']:
                    for aclass in auditorium['classes']:
                        if ('Проектный семинар (1 курс) (рус)' == aclass['discipline']) and (email in aclass['members']):
                            visits_dict.setdefault(item['date'][0:7:], 0)
                            visits_dict[item['date'][0:7:]] += 1
                            total_visits_count += 1
        except KeyError:
            pass
    return visits_dict,total_visits_count

def get_git_data(name:str):
    total_commits_count = 0
    account_exists = False
    commits_dict = {}
    with open(config.git_path,"r") as file:
        line = file.read()
        data = json.loads(line)
        try:
            for item in data:
                if item['name'] == name:
                    account_exists = True
                    for commits_month in item['commits_stats']:
                        commits_dict[datetime.strptime(commits_month['endDate'][4:15], "%b %d %Y").strftime('%Y-%m')] = commits_month['commitCount']
                        total_commits_count += commits_month['commitCount']
        except KeyError:
            pass
        return commits_dict,total_commits_count,account_exists


def get_zulip_data(name:str):
    total_messages_count = 0
    account_exists = False
    messages_dict = {}
    with open(config.zulip_path,"r") as file:
        line = file.read()
        data = json.loads(line)       
        try:
            for item in data:
                if item['full_name'] == name:
                    account_exists = True
                    for messages_month in item['stats']:
                        messages_dict[datetime.strptime(messages_month['endDate'][4:15], "%b %d %Y").strftime('%Y-%m')] = messages_month['messageCount']
                        total_messages_count += messages_month['messageCount']
        except KeyError:
            pass
        return messages_dict,total_messages_count,account_exists

#get_jitsiusers_data("maisakov@miem.hse.ru")
#print(get_git_data("Михаил Исаков"))
#print(get_zulip_data('Михаил Исаков'))
#print(get_jitsiClasses_data('maisakov@miem.hse.ru'))

#print(get_jitsiSession_data('pdblinov@miem.hse.ru'))
        

    

