import numpy as np
from http_requests import http_requests
from src.common.moves import Moves


class GridWorld:
    # Initialise starting data
    def __init__(self, world_id):
        # Set information about the gridworld
        self.world_id = world_id
        self.height = 40
        self.width = 40
        self.grid = np.zeros((self.height, self.width)) - 1

        # Set random start location for the agent (need change to 0, 0)
        # self.current_location = (39, np.random.randint(0, 40))
        self.current_location = (0, 0)

        # Set available actions
        self.actions = [move.value for move in Moves]

    # Put methods here:
    def get_available_actions(self):
        """Returns possible actions"""
        available_actions = list(self.actions)
        if self.current_location[0] == 0:
            available_actions.remove(Moves.West.value)
        if self.current_location[1] == 0:
            available_actions.remove(Moves.South.value)
        if self.current_location[1] == self.height - 1:
            available_actions.remove(Moves.East.value)
        if self.current_location[0] == self.width - 1:
            available_actions.remove(Moves.North.value)
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
        return move_result.get("reward"), move_result.get("scoreIncrement")

    def check_action(self, old_state, new_state):
        vector = (new_state[0] - old_state[0], new_state[1] - new_state[1])
        real_action = None
        if vector[0] == 1:
            real_action = Moves.East.value
        elif vector[0] == -1:
            real_action = Moves.West.value
        elif vector[1] == 1:
            real_action = Moves.North.value
        elif vector[1] == -1:
            real_action = Moves.South.value
        return real_action

