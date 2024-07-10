from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

premier_league_url = Request(
    url='https://www.whoscored.com/Regions/252/Tournaments/2/Seasons/9618/Stages/22076/PlayerStatistics/England-Premier-League-2023-2024#stage-top-player-stats-summary',
    headers={'User-Agent': 'Mozilla/5.0'}
)

page = urlopen(premier_league_url)
html = page.read().decode('utf-8')
soup = BeautifulSoup(html, 'html.parser')

print(soup)