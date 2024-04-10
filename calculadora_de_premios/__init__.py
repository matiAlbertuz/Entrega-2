def combine_player_stats(names,goals,goals_avoided,assists):
    players_stats=[]
    for i in range(len(names)):
        players_stats.append((names[i],goals[i],goals_avoided[i],assists[i]))
    return players_stats

def get_top_scorer(players_stats):
    max_goals=-1
    for stats in players_stats:
        if(stats[1]>max_goals):
            top_scorer=stats[0]
            max_goals=stats[1]
    return top_scorer,max_goals

