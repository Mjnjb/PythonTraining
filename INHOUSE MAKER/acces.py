import requests
import settings


def get_nominvoc(game_name=None,tag_line=None,nb_match=None, region=settings.DEFAULT_REGION):
    
    if not game_name:
        game_name = input("Entrez le pseudo : ")
    if not tag_line:
        tag_line = input("Entrez le # : ")

    
    params = {
        "api_key" : settings.api_key
    }
    api_url = f"https://{region}.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{game_name}/{tag_line}"

    try: 
        response = requests.get(api_url,params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Information sur l'invocateur impossible depuis l'api : {e}")
        return None
    


def get_historique(summoner_puuid,nb_match,region=settings.DEFAULT_REGION):
    params = {
        "api_key" : settings.api_key
    }
    api_url = f"https://{region}.api.riotgames.com/lol/match/v5/matches/by-puuid/{summoner_puuid}/ids?start=0&count={nb_match}&"

    try: 
        response = requests.get(api_url,params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Information sur l'historiqe impossible depuis l'api : {e}")
        return None
    

def win_ou_lose(summoner_puuid, match_id, region=settings.DEFAULT_REGION):
    params = {
        "api_key": settings.api_key
    }
    api_url = f"https://{region}.api.riotgames.com/lol/match/v5/matches/{match_id}"

    try: 
        response = requests.get(api_url, params)
        response.raise_for_status()
        match_data = response.json()
    except requests.exceptions.RequestException as e:
        print(f"Information sur la game impossible depuis l'api : {e}")
        return None
    
    if summoner_puuid in match_data['metadata']['participants']:
        player_index = match_data['metadata']['participants'].index(summoner_puuid)
        player_info = match_data['info']['participants'][player_index]
    else:
        return None

    return player_info['win']

def role_joueur(summoner_puuid, match_id, region=settings.DEFAULT_REGION):
    params = {
    "api_key": settings.api_key
    }
    api_url = f"https://{region}.api.riotgames.com/lol/match/v5/matches/{match_id}"

    try: 
        response = requests.get(api_url,params)
        response.raise_for_status()
        match_data= response.json()
    except requests.exceptions.RequestException as e:
        print(f"Information sur le role impossible depuis l'api : {e}")
        return None
    
    if summoner_puuid in match_data['metadata']['participants']:
        player_index = match_data['metadata']['participants'].index(summoner_puuid)
        player_role = match_data['info']['participants'][player_index]
    else:
        return None

    return player_role['teamPosition']
