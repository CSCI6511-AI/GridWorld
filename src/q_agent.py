import numpy as np
from src.common.moves import Moves


class QAgent:
    def __init__(self, environment, epsilon=0.05, alpha=0.1, gamma=1):
        self.environment = environment
        self.epsilon = epsilon
        self.alpha = alpha
        self.gamma = gamma
        # store q values
        self.q_table = dict()
        for x in range(environment.height):
            for y in range(environment.width):
                self.q_table[(x, y)] = {Moves.North.name: 0, Moves.South.name: 0, Moves.West.name: 0,
                                        Moves.East.name: 0}

    def choose_action(self, available_actions):
        # epsilon greedy
        # if np.random.uniform(0, 1) < self.epsilon:
        #     action = available_actions[np.random.randint(0, len(available_actions))]
        # else:
        #     q_values_of_state = self.q_table[self.environment.current_location]
        #     maxValue = max(q_values_of_state.values())
        #     action = np.random.choice([k for k, v in q_values_of_state.item() if v == maxValue])
        # max reward
        q_values_of_state = self.q_table[self.environment.current_location]
        max_value = max(q_values_of_state.values())
        action = np.random.choice([k for k, v in q_values_of_state.item() if v == max_value])
        return action

    def learn(self, old_state, reward, new_state, action):
        q_values_of_state = self.q_table[new_state]
        max_q_value_in_new_state = max(q_values_of_state.values())
        current_q_value = self.q_table[old_state][action]
        self.q_table[old_state][action] = (1 - self.alpha) * current_q_value \
                                          + self.alpha * (reward + self.gamma * max_q_value_in_new_state)


if __name__ == '__main__':
    a = dict()
    for x in range(4):
        for y in range(4):
            a[(x, y)] = {Moves.North.name: 0, Moves.South.name: 0, Moves.West.name: 0, Moves.East.name: 0}
    print(a)
