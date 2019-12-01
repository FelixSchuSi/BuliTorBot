import praw
import secrets
from competition import Competition, Team
import telegram

buli = [['gladbach', 'mönchengladbach', 'monchengladbach'], ['leipzig'], ['bayern', 'münchen', 'munchen', 'munich'], ['freiburg'], ['hoffenheim'], ['dortmund'], ['schalke'], ['leverkusen', 'bayer'],
        ['frankfurt'], ['wolfsburg'], ['union'], ['hertha'], ['düsseldorf'], ['dusseldorf'], ['werder', 'bremen'], ['augsburg'], ['mainz'], ['köln', 'koln', 'cologne'], ['paderborn']]

clTeams = [['ajax', 'amsterdam'], ['atalanta'], ['atlético', 'atletico'], ['bayer', 'leverkusen'], ['bayern', 'münchen', 'munich', 'munchen'], ['dortmund'], ['chelsea'], ['brügge', 'brugge'], ['roter', 'stern', 'belgrad', 'red', 'star'], ['dinamo', 'zagreb', 'dynamo'], ['barcelona'], ['galatasaray'], ['inter'], ['juventus', 'turin', 'juve'], ['genk'], ['lille', 'osc'],
           ['liverpool'], ['lokomotiv', 'moskva', 'moscow'], ['city'], ['olympiakos', 'piräus', 'piraus', 'olympiacos'], ['olympique', 'lyon'], ['paris', 'saint', 'germain', 'psg'], ['leipzig'], ['salzburg'], ['real'], ['schachtar', 'donezk', 'shakhtar', 'donetsk'], ['benfica'], ['slavia', 'praha', 'prag'], ['ssc', 'neapel', 'napoli'], ['tottenham', 'hotspur'], ['valencia'], ['zenit', 'petersburg']]


def redditBot():
    reddit = praw.Reddit(
        user_agent=secrets.reddit_user_agent,
        client_id=secrets.reddit_client_id,
        client_secret=secrets.reddit_client_secret
    )
    subreddit = reddit.subreddit('soccer')
    return subreddit


def telegramBot():
    return telegram.Bot(token=secrets.telegram_token)


def competition(competition):
    teams = []
    if competition == 'buli':
        for team in buli:
            tempTeam = Team(team)
            teams.append(tempTeam)
            print(tempTeam.aliases)
        bundesliga = Competition(teams)
        return bundesliga
    elif competition == 'cl':
        for team in clTeams:
            tempTeam = Team(team)
            teams.append(tempTeam)
            print(tempTeam.aliases)
        cl = Competition(teams)
        return cl
    else:
        raise Exception
