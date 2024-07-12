FOOTBALL_LEAGUES = {'Premier League': ["Man City", "Bournemouth", "Everton", "West Ham", "Newcastle",
                                       "Luton", "Aston Villa", "Tottenham", "Brentford", "Chelsea",
                                       "Nottingham Forest", "Liverpool", "Arsenal", "Crystal Palace", "Man Utd",
                                       "Wolves", "Fulham", "Brighton", "Sheff Utd", "Burnley"],
                    'LaLiga': ["Deportivo Alaves", "Athletic Club", "Atletico", "Barcelona", "Cadiz",
                               "Celta Vigo", "Getafe", "Girona", "Granada", "Las Palmas",
                               "Mallorca", "Osasuna", "Rayo Vallecano", "Real Betis", "Real Madrid",
                               "Real Sociedad", "Sevilla", "Valencia", "Villarreal", "Almeria"],
                    'Serie A': ["Atalanta", "Bologna", "Cagliari", "Empoli", "Fiorentina",
                                "Genoa", "Inter", "Juventus", "Lazio", "Lecce",
                                "AC Milan", "Monza", "Napoli", "Roma", "Salernitana",
                                "Sassuolo", "Torino", "Udinese", "Verona", "Frosinone"],
                    'Ligue 1': ["Clermont Foot", "Le Havre", "Lens", "Lille", "Lorient",
                                "Lyon", "Marseille", "Metz", "Monaco", "Montpellier",
                                "Nantes", "Nice", "PSG", "Reims", "Rennes",
                                "Strasbourg", "Toulouse", "Brest"],
                    'Bundesliga': ["Augsburg", "Leverkusen", "Bayern", "Borussia Dortmund",
                                   "Borussia M.Gladbach", "Darmstadt", "Eintracht Frankfurt", "Freiburg",
                                   "FC Heidenheim", "Hoffenheim", "FC Koln", "Mainz", "RBL",
                                   "Stuttgart", "Union Berlin", "Werder Bremen", "Wolfsburg", "Bochum"]
                    }

FOOTBALL_LEAGUES_MAPPING = {team: league for league, teams in FOOTBALL_LEAGUES.items() for team in teams}