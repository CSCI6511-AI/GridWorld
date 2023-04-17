import json
from src.common.moves import Moves
import requests

team_id = "1365"
game_url = "https://www.notexponential.com/aip2pgaming/api/rl/gw.php"
score_url = "https://www.notexponential.com/aip2pgaming/api/rl/score.php"
api_key = "d6fd7a080c148372b551"
headers = {"User-Agent": "PostmanRuntime/7.31.3",
           "Accept": "*/*",
           "Accept-Encoding": "gzip, deflate, br",
           "Connection": "close",
           "userId": "1135",
           "x-api-key": api_key}


def get_runs(count):
    """
    get {count} runs
    :param count: number of runs you want get
    :return: a list of run history, each element is a dictionary which contains
        runId, teamId, gworldId, createTs, score, moves
    """
    params = {
        "type": "runs",
        "teamId": team_id,
        "count": count,
    }
    response = requests.get(score_url, params=params, headers=headers)
    if response.status_code != 200:
        raise Exception(json.loads(response.text)["message"])
    return json.loads(response.text)["runs"]


def get_location():
    """
    get current location
    :return: return a dictionary which contains
        the world you in and the state you are
    """
    params = {
        "type": "location",
        "teamId": team_id,
    }
    response = requests.get(game_url, params=params, headers=headers)
    if response.status_code != 200:
        raise Exception(json.loads(response.text)["message"])
    return json.loads(response.text)


def enter_a_world(world_id):
    """
    enter a world you want to go
    :param world_id: the world id you want to enter
    :return: a dictionary which contains
        worldId, runId, state
        Tips: Fails if you are already in a world.
    """
    data = {
        "type": "enter",
        "worldId": world_id,
        "teamId": team_id,
    }
    response = requests.post(game_url, data=data, headers=headers)
    if response.status_code != 200:
        raise Exception(json.loads(response.text)["message"])
    return json.loads(response.text)


def make_a_move(move, word_id):
    """
    make a move in current world
    :param move: move direction, refer to moves.py
    :param word_id: world id
    :return: a dictionary which contains
        worldId, runId, reward, scoreIncrement, newState
        Tips: Fails if you are not already in a world
    """
    data = {
        "type": "move",
        "teamId": team_id,
        "move": move,
        "wordId": word_id,
    }
    response = requests.post(game_url, data=data, headers=headers)
    if response.status_code != 200:
        raise Exception(json.loads(response.text)["message"])
    return json.loads(response.text)


def get_score():
    """
    get score of current team
    :return: the score of current team
    """
    params = {
        "type": "score",
        "teamId": team_id,
    }
    response = requests.get(score_url, params=params, headers=headers)
    if response.status_code != 200:
        raise Exception(json.loads(response.text)["message"])
    return json.loads(response.text)["score"]


def reset_team():
    params = {
        "teamId": team_id,
        "otp": "5712768807",
    }
    response = requests.get(
        "https://www.notexponential.com/aip2pgaming/api/rl/reset.php",
        params=params,
        headers=headers
    )
    if response.status_code != 200:
        raise Exception(json.loads(response.text))
    return json.loads(response.text)


# if __name__ == '__main__':
    # reset team
    # res = reset_team()
    # print(res)
    # test enter a world
    # res = enter_a_world("0")
    # print(res)
    # test make a move
    # res = make_a_move("E", "0")
    # print(res)
    # test get runs
    # res = get_runs(2)
    # print(res)
    # test get location
    # res = get_location()
    # print(res)
    # test get_score
    # res = get_score()
    # print(res)
