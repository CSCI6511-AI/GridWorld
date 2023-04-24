from src.grid_world import GridWorld
from src.q_agent import QAgent
from src.play import play
from http_requests import http_requests


def main():
    # Create environment
    environment = GridWorld()
    # Create agent
    agent = QAgent(environment)
    # Train agent by playing games
    play(environment, agent)


if __name__ == '__main__':
    res = http_requests.reset_team()
    print(res)
    res = http_requests.enter_a_world()
    print(res)
    # res = http_requests.get_location()
    # print(res)
    # res = http_requests.make_a_move("E")
    # print(res)
    main()