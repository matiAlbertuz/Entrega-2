def combine_player_stats(names,goals,goals_avoided,assists): 
    """ 
    Combina las estadísticas de los jugadores en una lista de tuplas.

    Esta función combina las listas de nombres, goles, goles evitados y asistencias en una lista de tuplas, donde cada 
    tupla contiene el nombre de un jugador, sus goles, sus goles evitados y sus asistencias.

    Parámetros:
    names (list): Una lista de nombres de jugadores.
    goals (list): Una lista de números que representan los goles anotados por cada jugador.
    goals_avoided (list): Una lista de números que representan los goles evitados por cada jugador.
    assists (list): Una lista de números que representan las asistencias realizadas por cada jugador.

    Retorna:
    list: Una lista de tuplas donde cada tupla contiene el nombre de un jugador, sus goles,goles evitados y asistencias.
    """   
    
    players_stats=[]
    for i in range(len(names)):
        players_stats.append((names[i],goals[i],goals_avoided[i],assists[i]))
    return players_stats

def get_top_scorer(players_stats):
    """
    Encuentra al máximo goleador entre una lista de estadísticas de jugadores.

    Esta función toma una lista de estadísticas de jugadores, donde cada elemento es una tupla que contiene el nombre de 
    un jugador, su cantidad de goles, su cantidad de goles evitados y su cantidad de asistencias. Luego, encuentra al jugador con la
    mayor cantidad de goles y lo devuelve.

    Parámetros:
    players_stats (list): Una lista de tuplas donde cada tupla contiene el nombre de un jugador, su cantidad de goles, su 
    cantidad de goles evitados y su cantidad de asistencias.

    Retorna:
    tuple: Una tupla que contiene el nombre y la cantidad de goles del máximo goleador.
    """
    top_scorer=max(players_stats,key=lambda x: x[1])
    return top_scorer

def get_MVP(players_stats,points):
    """
    Encuentra al jugador mas influyente basado en las estadísticas de los jugadores y sus pesos.

    Esta función calcula el promedio de cada jugador utilizando sus estadísticas y el peso de ellas. Luego, determina al 
    jugador más influyente como aquel con el promedio más alto.

    Parámetros:
    players_stats (list): Una lista de tuplas donde cada tupla contiene el nombre de un jugador, sus goles, sus goles 
    evitados y sus asistencias.
    points (dict): Un diccionario que con el valor o puntaje de cada estadística.

    Retorna:
    str: El nombre del jugador más influyente basado en el promedio de sus estadísticas.
    """
    max_score=0
    for name, goals, goals_avoided, assists in players_stats:
      player_score=(goals*points["Goal"])+(goals_avoided*points["Goal avoid"])+(assists*points["Assist"])
      if(player_score>max_score):
        max_score=player_score
        mvp=name
    return mvp

def get_average(players_stats,total_matches):
    """
    Calcula el promedio de goles por partido basado en las estadísticas de los jugadores y la cantidad total de partidos.

    Esta función toma una lista de estadísticas de jugadores, donde cada elemento es una tupla que contiene el nombre de
    un jugador, su cantidad de goles, su cantidad de goles evitados y su cantidad de asistencias, y el número total de 
    partidos. Luego, calcula el total de goles marcados por todos los jugadores y divide este total por el número total 
    de partidos en la temporada para obtener el promedio de goles por partido.

    Parámetros:
    players_stats (list): Una lista de tuplas donde cada tupla contiene el nombre de un jugador y sus estadísticas.
    total_matches (int): El número total de partidos jugados en la temporada.

    Retorna:
    float: El promedio de goles por partido basado en las estadísticas de los jugadores y la cantidad total de partidos.
    """
    total=sum(map(lambda x:x[1],players_stats))
    return total/total_matches

def get_average_top_scorer(top_scorer,total_matches):
    """
    Calcula el promedio de goles por partido para el máximo goleador/goleadora.

    Toma la cantidad de goles anotados por el máximo goleador/goleadora y el número total de partidos jugados, y calcula
    su promedio de goles por partido.

    Parámetros:
    top_scorer (tuple): Una tupla que contiene el nombre del máximo goleador y la cantidad de goles que realizó.
    total_matches (int): El número total de partidos jugados.

    Retorna:
    float: El promedio de goles por partido para el máximo goleador/goleadora.
    """
    return top_scorer[1]/total_matches               