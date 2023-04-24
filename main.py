from src.grid_world import GridWorld
from src.q_agent import QAgent
from src.play import play
from http_requests import http_requests


def main(world_id, file_name=None):
    # Create environment
    environment = GridWorld(world_id)
    # Create agent
    agent = QAgent(environment, file_name)
    # Train agent by playing games
    play(environment, agent, 100)


if __name__ == '__main__':
    res = http_requests.reset_team()
    print(res)
    http_requests.world_id = "1"
    res = http_requests.enter_a_world()
    print(res)
    # res = http_requests.get_location()
    # print(res)
    # res = http_requests.make_a_move("E")
    # print(res)
    file = "1-1682362721.txt"
    main(http_requests.world_id, file)
