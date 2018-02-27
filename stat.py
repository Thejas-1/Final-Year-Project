import requests
from bs4 import BeautifulSoup
import json
from pprint import pprint

player_template = {"pid":"0","name":"","team_name":"","out_by":"None","runs_scored":"-1","balls_faced":"0","fours":"0","sixes":"0","strike_rate":"0","overs":"0","maiden":"0","runs_given":"0","wickets":"0","no_balls":"0","wide_balls":"0","CROST":"0","extras":"0"}


#url = "http://www.howstat.com/cricket/Statistics/Matches/MatchScorecard_ODI.asp?MatchCode=3878"
#Scorecard = requests.get(url).text
Soup = BeautifulSoup(open("page.html"), "html.parser")
#print Soup
match_name = Soup.find('a',class_="LinkBlack2").get_text()
match_name=match_name.strip()
#print("Match Name :" + match_name)


match_date = Soup.find('td',class_="TextBlack8").get_text()
match_date=match_date.strip()
#print("Match Date :"match_date)
x=Soup.find('td',class_="TextBlack8").find_all_next("td")


for i in x:
	print(i.get_text().strip()) #To CSV file

j=1
for i in x:
	y = i.get_text().strip()
	if(j==3):
		match_venue=y
	if(j==10):
		match_result=y
	j=j+1
	if(j>10):
		break
		
#print(match_result)
	

'''
tds = Soup.find_all('td')
j=0
print(tds)
for td in tds:
    if(td=="Result"):
    	print("found")
    	j=1

if(j==0):
	print("Not Found!")
'''

'''
table = Soup.find('table')
rows = table.find_all('tr')
for tr in rows:
	cols = tr.find_all('td')
	text_data = []
	for ted in cols:
		text = ''.join(ted)
		utftext = str(text.encode('utf-8'))
		text_data.append(utftext) # EDIT
		text = date+','.join(text_data)

'''

'''
match_venue = Soup.find('td',class_="TextBlack8").get_text()
match_venue=match_venue.strip()
print(match_venue)
'''



'''
tds = Soup.find_all('td')

for td in tds:
    try:
        col = int(td["colspan"])
    except (ValueError, KeyError) as e:
        col = 0

    print(col)

'''

'''
i=3878

while i<4000:
	url = "http://www.howstat.com/cricket/Statistics/Matches/MatchScorecard_ODI.asp?MatchCode="+str(i)
	Scorecard = requests.get(url).text
	Soup = BeautifulSoup(Scorecard,"html.parser")
	i=i+1
	#print Soup
	match_name = Soup.find('a',class_="LinkBlack2").get_text()
	match_name=match_name.strip()
	print(str(i)+":"+match_name)

'''




#match_name = match_name[:match_name.find('- Live Cricket Score, Commentary')].strip()

'''
  for match in matches['match']:
    if match_name == match['match_name']:
      print "Match already exists..."
      return match

  match = {}
  match['match_name'] = match_name
  match['url'] = url[url.find('cricket-scorecard/')+18:]




  Inning1 = Soup.find_all('div',id="innings_1")[0]
  Inning1_batting = Inning1.find_all('div',class_="cb-col cb-col-100 cb-ltst-wgt-hdr")[0]
  Inning1_bowling = Inning1.find_all('div',class_="cb-col cb-col-100 cb-ltst-wgt-hdr")[1]
  Inning1_batting = Inning1_batting.find_all('div',class_="cb-col cb-col-100 cb-scrd-itms")
  Inning1_bowling = Inning1_bowling.find_all('div',class_="cb-col cb-col-100 cb-scrd-itms ")
  Score = Inning1.find_all('span',class_="pull-right")
  score = Score[0].get_text()
  if '-' in score:
    score = score[:score.find('-')]
  team_name = Inning1.find('span').get_text()
  if 'Innings' in team_name:
    team_name = team_name[:team_name.find(' Innings')]
  match['team1_name'] = team_name
  match['team1_score'] = score



  # Inning 1 Start

  Inning1_batting_info = []
  for b in Inning1_batting:
    # pprint(b)
    batsman = {}
    name = b.find('a',class_="cb-text-link")
    if name:
      pid = name['href'][10:]
      batsman['pid'] = str(pid[:pid.find('/')])
      batsman['name'] = str(name.get_text()).strip()
      if '(' in batsman['name']:
        batsman['name'] = batsman['name'][:batsman['name'].find('(')].strip()
    out_by = b.find('span',class_="text-gray")
    if out_by:
      batsman['out_by'] = str(out_by.get_text()).strip()
    runs = b.find('div',class_="cb-col cb-col-8 text-right text-bold")
    if runs:
      batsman['runs'] = str(runs.get_text()).strip()
    all_others = b.find_all('div',class_="cb-col cb-col-8 text-right")
    if len(all_others)>0:
      batsman['balls'] = str(all_others[0].get_text()).strip()
      batsman['fours'] = str(all_others[1].get_text()).strip()
      batsman['sixes'] = str(all_others[2].get_text()).strip()
      batsman['sr'] = str(all_others[3].get_text()).strip()

    # print all_other
    if len(batsman) > 0:
      Inning1_batting_info.append(batsman)



  Inning1_bowling_info = []
  for b in Inning1_bowling:
    bowler = {}
    name = b.find('a',class_="cb-text-link")
    if name:
      pid = name['href'][10:]
      bowler['pid'] = str(pid[:pid.find('/')])
      bowler['name'] = str(name.get_text()).strip()
      if '(' in bowler['name']:
        bowler['name'] = bowler['name'][:bowler['name'].find('(')].strip()
    wickets = b.find('div',class_="cb-col cb-col-8 text-right text-bold")
    if wickets:
      bowler['wickets'] = str(wickets.get_text()).strip()
    runs_given = b.find('div',class_="cb-col cb-col-10 text-right")
    if runs_given:
      bowler['runs_given'] = str(runs_given.get_text()).strip()
    all_others = b.find_all('div',class_="cb-col cb-col-8 text-right")
    # print all_others
    if len(all_others)>0:
      bowler['overs'] = str(all_others[0].get_text()).strip()
      bowler['maiden'] = str(all_others[1].get_text()).strip()
      bowler['no_balls'] = str(all_others[2].get_text()).strip()
      bowler['wide_balls'] = str(all_others[3].get_text()).strip()
      # bowler['economy'] = str(all_others[5].get_text()).strip()
    # print bowler
    if len(bowler) > 0:
      Inning1_bowling_info.append(bowler)



  # Inning 2 Start


  Inning2 = Soup.find_all('div',id="innings_2")[0]
  Inning2_batting = Inning2.find_all('div',class_="cb-col cb-col-100 cb-ltst-wgt-hdr")[0]
  Inning2_bowling = Inning2.find_all('div',class_="cb-col cb-col-100 cb-ltst-wgt-hdr")[1]
  Inning2_batting = Inning2_batting.find_all('div',class_="cb-col cb-col-100 cb-scrd-itms")
  Inning2_bowling = Inning2_bowling.find_all('div',class_="cb-col cb-col-100 cb-scrd-itms ")
  Score = Inning2.find_all('span',class_="pull-right")
  score = Score[0].get_text()
  if '-' in score:
    score = score[:score.find('-')]
  team_name = Inning2.find('span').get_text()
  if 'Innings' in team_name:
    team_name = team_name[:team_name.find(' Innings')]
  match['team2_name'] = team_name
  match['team2_score'] = score






  Inning2_batting_info = []
  for b in Inning2_batting:
    # pprint(b)
    batsman = {}
    name = b.find('a',class_="cb-text-link")
    if name:
      pid = name['href'][10:]
      batsman['pid'] = str(pid[:pid.find('/')])
      batsman['name'] = str(name.get_text()).strip()
      if '(' in batsman['name']:
        batsman['name'] = batsman['name'][:batsman['name'].find('(')].strip()
    out_by = b.find('span',class_="text-gray")
    if out_by:
      batsman['out_by'] = str(out_by.get_text()).strip()
    runs = b.find('div',class_="cb-col cb-col-8 text-right text-bold")
    if runs:
      batsman['runs'] = str(runs.get_text()).strip()
    all_others = b.find_all('div',class_="cb-col cb-col-8 text-right")
    if len(all_others)>0:
      batsman['balls'] = str(all_others[0].get_text()).strip()
      batsman['fours'] = str(all_others[1].get_text()).strip()
      batsman['sixes'] = str(all_others[2].get_text()).strip()
      batsman['sr'] = str(all_others[3].get_text()).strip()

    # print all_other
    if len(batsman) > 0:
      Inning2_batting_info.append(batsman)



  Inning2_bowling_info = []
  for b in Inning2_bowling:
    bowler = {}
    name = b.find('a',class_="cb-text-link")
    if name:
      pid = name['href'][10:]
      bowler['pid'] = str(pid[:pid.find('/')])
      bowler['name'] = str(name.get_text()).strip()
      if '(' in bowler['name']:
        bowler['name'] = bowler['name'][:bowler['name'].find('(')].strip()
    wickets = b.find('div',class_="cb-col cb-col-8 text-right text-bold")
    if wickets:
      bowler['wickets'] = str(wickets.get_text()).strip()
    runs_given = b.find('div',class_="cb-col cb-col-10 text-right")
    if runs_given:
      bowler['runs_given'] = str(runs_given.get_text()).strip()
    all_others = b.find_all('div',class_="cb-col cb-col-8 text-right")
    # print all_others
    if len(all_others)>0:
      bowler['overs'] = str(all_others[0].get_text()).strip()
      bowler['maiden'] = str(all_others[1].get_text()).strip()
      bowler['no_balls'] = str(all_others[2].get_text()).strip()
      bowler['wide_balls'] = str(all_others[3].get_text()).strip()
      # bowler['economy'] = str(all_others[5].get_text()).strip()
    # print bowler
    if len(bowler) > 0:
      Inning2_bowling_info.append(bowler)

  # print match
  # print json.dumps(matches,sort_keys=True,indent=4, separators=(',', ': '))
  players = {}
  Players = Soup.find_all('div',class_="cb-col cb-col-100 cb-minfo-tm-nm")
  Players1 = Players[1].find_all('a')
  Players2 = Players[3].find_all('a')
  # for p in Players1:
  #   print p
  # for p in Players2:
  #   print p
  for p in Players1:
    player = player_template.copy()
    pid = p['href'][10:]
    pid = str(pid[:pid.find('/')])
    players[pid] = player
  for p in Players2:
    player = player_template.copy()
    pid = p['href'][10:]
    pid = str(pid[:pid.find('/')])
    players[pid] = player


  # print players
  for p in Inning1_batting_info:
    if p['pid'] in players:
      players[p['pid']]['name'] = p['name']
      players[p['pid']]['balls_faced'] = p['balls']
      players[p['pid']]['fours'] = p['fours']
      players[p['pid']]['sixes'] = p['sixes']
      players[p['pid']]['runs_scored'] = p['runs']
      players[p['pid']]['out_by'] = p['out_by']
      players[p['pid']]['strike_rate'] = p['sr']
      players[p['pid']]['pid'] = p['pid']


  for p in Inning1_bowling_info:
    if p['pid'] in players:
      players[p['pid']]['name'] = p['name']
      players[p['pid']]['maiden'] = p['maiden']
      players[p['pid']]['overs'] = p['overs']
      players[p['pid']]['no_balls'] = p['no_balls']
      players[p['pid']]['runs_given'] = p['runs_given']
      players[p['pid']]['wickets'] = p['wickets']
      players[p['pid']]['wide_balls'] = p['wide_balls']
      players[p['pid']]['pid'] = p['pid']


  for p in Inning2_batting_info:
    if p['pid'] in players:
      players[p['pid']]['name'] = p['name']
      players[p['pid']]['balls_faced'] = p['balls']
      players[p['pid']]['fours'] = p['fours']
      players[p['pid']]['sixes'] = p['sixes']
      players[p['pid']]['runs_scored'] = p['runs']
      players[p['pid']]['out_by'] = p['out_by']
      players[p['pid']]['strike_rate'] = p['sr']
      players[p['pid']]['pid'] = p['pid']


  for p in Inning2_bowling_info:
    if p['pid'] in players:
      players[p['pid']]['name'] = p['name']
      players[p['pid']]['maiden'] = p['maiden']
      players[p['pid']]['overs'] = p['overs']
      players[p['pid']]['no_balls'] = p['no_balls']
      players[p['pid']]['runs_given'] = p['runs_given']
      players[p['pid']]['wickets'] = p['wickets']
      players[p['pid']]['wide_balls'] = p['wide_balls']
      players[p['pid']]['pid'] = p['pid']

  match['players'] = players
  matches["match"].append(match)


  with open('matches.json','w') as f:
    json.dump(matches,f)
  return match
# print json.dumps(matches,sort_keys=True,indent=4, separators=(',', ': '))

'''


