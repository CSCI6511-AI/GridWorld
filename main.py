from http_requests import http_requests
from src.common.moves import Moves

if __name__ == '__main__':
    world_id = "0"
    # enter a world
    # http_requests.enter_a_world("0")
    old_location = http_requests.get_location().get("state")
    move = Moves.East.value
    res = http_requests.make_a_move(move, world_id)
    print(res)
    cur_reward = res.get("reward")
    new_location = http_requests.get_location().get("state")
    print(f"move: {move}\nold location: {old_location}\nnew location: {new_location}\nreward: {cur_reward} points")
    score = http_requests.get_score()
    print(f"current score is {score}")
