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

TEAMS_RANKING = {'A-tier': ["Man City", "Real Madrid", "Bayern", "Barcelona", "Liverpool",
                            "Arsenal", "Man Utd", "Chelsea", "PSG", "Tottenham", "Inter",
                            "Juventus", "Atletico", "AC Milan", "Borussia Dortmund"],
                 'B-tier': ["Newcastle", "Leverkusen", "Aston Villa", "Brighton", "Napoli",
                            "Real Sociedad", "West Ham", "Atalanta", "RBL", "Roma", "Athletic Club",
                            "Girona", "Villarreal", "Lazio", "Lyon", "Marseille", "Everton", "Wolves",
                            "Sevilla", "Valencia", "Real Betis", "Fiorentina", "Nice", "Lille",
                            "Monaco", "Sassuolo", "Borussia M.Gladbach", "Eintracht Frankfurt",
                            "Stuttgart", "Union Berlin"],
                 'C-tier': ["Deportivo Alaves", "Cadiz", "Celta Vigo", "Getafe", "Granada", "Las Palmas",
                            "Mallorca", "Osasuna", "Rayo Vallecano", "Almeria", "Bologna", "Cagliari", "Empoli",
                            "Genoa", "Lecce", "Monza", "Salernitana", "Torino", "Udinese", "Verona", "Frosinone",
                            "Clermont Foot", "Le Havre", "Lens", "Lorient", "Metz", "Montpellier",
                            "Nantes", "Reims", "Rennes", "Strasbourg", "Toulouse", "Brest", "Augsburg",
                            "Darmstadt", "Freiburg", "FC Heidenheim", "Hoffenheim", "FC Koln", "Mainz",
                            "Werder Bremen", "Wolfsburg", "Bochum", "Bournemouth", "Luton", "Brentford",
                            "Nottingham Forest", "Fulham", "Sheff Utd", "Burnley", "Crystal Palace"]
                 }

TEAMS_RANKING_MAPPING = {team: rank for rank, teams in TEAMS_RANKING.items() for team in teams}

