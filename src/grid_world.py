import numpy as np
from http_requests import http_requests
from src.common.action import Actions


class GridWorld:
    # Initialise starting data
    def __init__(self, world_id):
        # set information about the gridworld
        self.world_id = world_id
        self.height = 40
        self.width = 40
        self.grid = np.zeros((self.height, self.width)) - 1
        # init location
        self.current_location = (0, 0)
        # set available actions
        self.actions = [action.value for action in Actions]
        self.visited = np.zeros((self.height, self.width)) - 1

    # Put methods here:
    def get_available_actions(self):
        """Returns possible actions"""
        available_actions = list(self.actions)
        c = self.current_location
        if c[0] == 0 or c[0] - 1 >= 0 and self.visited[c[0] - 1, c[1]] == 1:
            available_actions.remove(Actions.West.value)
        if c[1] == 0 or c[1] - 1 >= 0 and self.visited[c[0], c[1] - 1] == 1:
            available_actions.remove(Actions.South.value)
        if c[1] == self.height - 1 or c[0] + 1 < self.width and self.visited[c[0] + 1, c[1]] == 1:
            available_actions.remove(Actions.East.value)
        if c[0] == self.width - 1 or c[1] + 1 < self.height and self.visited[c[0], c[1] + 1] == 1:
            available_actions.remove(Actions.North.value)
        if len(available_actions) == 0:
            return list(self.actions)
        # print(available_actions)
        return available_actions

    def agent_on_map(self):
        """Prints out current location of the agent on the grid (used for debugging)"""
        grid = np.zeros((self.height, self.width))
        grid[self.current_location[0], self.current_location[1]] = 1
        return grid

    def make_step(self, action):
        # make a move and get the result
        move_result = http_requests.make_a_move(action)
        if move_result.get("code") == "FAIL" or move_result.get("newState") is None:
            print(move_result)
            return None, None
        # get the new state
        new_location = (int(move_result.get("newState").get("x")),
                        int(move_result.get("newState").get("y")))
        self.current_location = new_location
        self.visited[new_location[0], new_location[1]] = 1
        return move_result.get("reward"), move_result.get("scoreIncrement")

    def check_action(self, old_state, new_state):
        vector = (new_state[0] - old_state[0], new_state[1] - new_state[1])
        real_action = None
        if vector[0] == 1:
            real_action = Actions.East.value
        elif vector[0] == -1:
            real_action = Actions.West.value
        elif vector[1] == 1:
            real_action = Actions.North.value
        elif vector[1] == -1:
            real_action = Actions.South.value
        return real_action

