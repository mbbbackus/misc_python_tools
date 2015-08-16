#!/usr/bin/env python
import sys

if len(sys.argv) == 1:
    sys.exit(0)

def compileStats():
    statfile = open(sys.argv[1]).readlines()
    fstats = "player,team,GP,MPG,FGM,FGA,FG%,3PM,3PA,3P%,FTM,FTA,FT%,TOV,PF,ORB,DRB,RPG,APG,SPG,PPG\n"
    for line in statfile:
        n = line.replace(">","<").split("<")
        for i in range(0, len(n)-1):
            if "a href=" in n[i]:
                n = n[i+1:]
                break
        stats = []
        for s in n:
            if s != "":
                if not ('/' in s):
                    if s != 'td' and s != '\n':
                        stats.append(s)
        stats.pop(len(stats)-2)
        fstats +=  ",".join(stats) + "\n"

    newfile = open("nba_stats.csv", 'w+')
    newfile.write(fstats)
    newfile.close()

def findSimilarStrings(string, strings):
	ret = []
	for s in strings:
		for i in range(0, len(string)-5):
			part = string[i:i+4]
			if part in s:
				ret.append(s)
				break
	ret = list(set(ret))
	return ret

def statsToJson(file):
    sheet = open(file).readlines()
    index = sheet[0].replace('\n','').split(',')
    stats = sheet[1:]

    players = {}
    for line in stats:
        p_data = line.replace('\n','').split(',')
        p_name = p_data[0].lower()
        p_stats = {}
        for i in range(1, len(p_data)):
            p_stats[index[i]] = p_data[i]
        players[p_name] = p_stats

    #return json_tools.format(players, 0)
    return players

def getPlayerStats():
	jstats = statsToJson("nba_stats.csv")
	playername = sys.argv[1].lower()
	stats_req = sys.argv[2:]
	try:
		ret = playername
		for s in stats_req:
			ret += " - " + s + " : " + jstats[playername][s]
		return ret 
	except KeyError:
		players = []
		for player in jstats:
			players.append(player)
		similar_players = findSimilarStrings(playername, players)
		return "player not found, perhaps you meant: " + ", ".join(similar_players)		

print getPlayerStats()
