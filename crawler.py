import requests
import os
import datetime
from urllib.request import urlopen
from bs4 import BeautifulSoup

os.environ['DJANGO_SETTINGS_MODULE'] = 'lcks.settings'
import django
django.setup()
from api.models import Team, Match

def create_team():
    URL = 'https://lck.inven.co.kr/'
    html = urlopen(URL)
    soup = BeautifulSoup(html, "html.parser")
    for i in range(0, 10):
        name = soup.select_one(
            '#lckBody > div.commu-wrap > section > article > section.commu-left > section > div > div > nav> div.rankingListWrap > table > tbody > tr:nth-child(' + str(i + 1) + ') > td.total > a > div.team'
            ).get_text()
        rank = soup.select_one(
            '#lckBody > div.commu-wrap > section > article > section.commu-left > section > div > div > nav > div.rankingListWrap > table > tbody > tr:nth-child(' + str(i + 1) + ') > td.ranking'
            ).get_text()
        score = soup.select_one(
            '#lckBody > div.commu-wrap > section > article > section.commu-left > section > div > div > nav > div.rankingListWrap > table > tbody > tr:nth-child(' + str(i + 1) + ') > td.total > a > div.score'
            ).get_text().split()
        rank = int(''.join( x for x in rank if x not in '위'))
        win = int(''.join( x for x in score[0] if x not in '승'))
        defeat = int(''.join( x for x in score[1] if x not in '패'))
        v_point = int(''.join( x for x in score[2] if x not in '+'))
        info = ''
        info_url = 'https://lck.inven.co.kr/af/proteam'
        logo_url = ''
        
        if name == 'KWANGDONG FREECS':
            info_url = 'https://lck.inven.co.kr/af/proteam'
            logo_url = 'img/kwangdong_freecs.png'
        elif name == 'DRX':
            info_url = 'https://lck.inven.co.kr/drx/proteam'
            logo_url = 'img/drx.png'
        elif name == 'DWG KIA':
            info_url = 'https://lck.inven.co.kr/dk/proteam'
            logo_url = 'img/dwg_kia.png'
        elif name == 'Fredit BRION':
            info_url = 'https://lck.inven.co.kr/bro/proteam'
            logo_url = 'img/fredit_brion.png'
        elif name == 'Gen.G Esports':
            info_url = 'https://lck.inven.co.kr/gen/proteam'
            logo_url = 'img/geng.png'
        elif name == 'Hanwha Life Esports':
            info_url = 'https://lck.inven.co.kr/hle/proteam'
            logo_url = 'img/hanwha_life_esports.png'
        elif name == 'Liiv Sandbox':
            info_url = 'https://lck.inven.co.kr/lsb/proteam'
            logo_url = 'img/liiv_sandbox.png'
        elif name == 'NS RED FORCE':
            info_url = 'https://lck.inven.co.kr/ns/proteam'
            logo_url = 'img/ns_red_force.png'
        elif name == 'T1':
            info_url = 'https://lck.inven.co.kr/t1/proteam'
            logo_url = 'img/t1.png'
        elif name == 'kt rolster':
            info_url = 'https://lck.inven.co.kr/kt/proteam'
            logo_url = 'img/kt_rolster.png'
            
        info_html = urlopen(info_url)
        info_soup = BeautifulSoup(info_html, "html.parser")

        players = info_soup.select('#scriptorium > div.block.scriptorium_layout.clearfix > div.left_div > div.memberTable > table > tbody > tr')
        info += '소속 선수 :\n'
        for j in range(1, len(players)):
            info += '    '
            info += players[j].select_one('td:nth-child(2)').get_text()
            info += ' '
            info += players[j].select_one('td:nth-child(1)').get_text()
            info += '\n'

        try:
            team = Team.objects.get(name=name)
            team.name = name
            team.logo_url = logo_url
            team.rank = rank
            team.win = win
            team.defeat = defeat
            team.v_point = v_point
            team.info = info

            team.save()
        except Team.DoesNotExist:
            Team.objects.create(
            name = name,
            logo_url = logo_url,
            rank = rank,
            win = win,
            defeat = defeat,
            v_point = v_point,
            info = info
            )
            
    
def create_match():
    for i in range(1, 10):
        URL = 'https://lol.inven.co.kr/dataninfo/match/teamList.php?pg=' + str(i) + 'iskin=esports&category2=166'
        html = urlopen(URL)
        soup = BeautifulSoup(html, "html.parser")
        matches = soup.select('.listFrame')
        for match in matches:
            tx4 = match.select_one('div:nth-child(4) > div:nth-child(1) > span:nth-child(2)').get_text()
            tx4 = tx4.split(' ')
            team_1_score = tx4[0]
            team_2_score = tx4[2]
            team_1_name = match.select_one('div:nth-child(2) > div:nth-child(1) > a:nth-child(1)').get_text()
            team_2_name = match.select_one('div:nth-child(3) > div:nth-child(2) > a:nth-child(1)').get_text()
            match_set = match.select_one('div.listTop > div.stage').get_text().split()[2]
            match_set = int(''.join( x for x in match_set if x not in '세트'))
            
            if team_1_name == 'Gen.G eSports':
                team_1_name = 'Gen.G Esports'
            if team_2_name == 'Gen.G eSports':
                team_2_name = 'Gen.G Esports'
            if team_1_name == 'kt Rolster':
                team_1_name = 'kt rolster'
            if team_2_name == 'kt Rolster':
                team_2_name = 'kt rolster'
                
            try:
                team_1 = Team.objects.get(name=team_1_name)
            except:
                pass

            try:
                team_2 = Team.objects.get(name=team_2_name)
            except:
                pass
            
            match_date = match.select_one('div:nth-child(1) > div:nth-child(1)').get_text()
            match_date = match_date.replace('.', '-')
            match_date = datetime.datetime.strptime(match_date, '%Y-%m-%d').date()
            
            try:
                exist_match = Match.objects.get(team_1=team_1, team_2=team_2, match_date=match_date, match_set=match_set)
            except Match.DoesNotExist:
                Match.objects.create(
                    team_1 = team_1,
                    team_2 = team_2,
                    team_1_score = team_1_score,
                    team_2_score = team_2_score,
                    match_date = match_date,
                    match_set = match_set,
                )

if __name__=='__main__':
    create_team()
    create_match()