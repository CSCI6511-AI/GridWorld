import numpy as np
from src.common.action import Actions
import time
from src.grid_world import GridWorld
import os


class QAgent:
    def __init__(self, environment, file_name=None, epsilon=0.5, alpha=0.1, gamma=0.9):
        # grid world
        self.environment = environment
        self.epsilon = epsilon
        self.alpha = alpha
        self.gamma = gamma
        # store q values
        self.q_table = dict()
        if file_name is None:
            for x in range(environment.height):
                for y in range(environment.width):
                    self.q_table[(x, y)] = {Actions.North.value: 0,
                                            Actions.South.value: 0,
                                            Actions.West.value: 0,
                                            Actions.East.value: 0}
        else:
            self.init_q_table(file_name)

    def choose_action(self, available_actions):
        action = None
        # epsilon greedy
        if np.random.uniform(0, 1) < self.epsilon:
            action = available_actions[np.random.randint(0, len(available_actions))]
        else:
            q_values_of_state = self.q_table[self.environment.current_location]
            max_value = q_values_of_state.get(available_actions[0])
            for a in available_actions:
                if q_values_of_state.get(a) > max_value:
                    max_value = q_values_of_state.get(a)
                    action = a
        # max reward
        # q_values_of_state = self.q_table[self.environment.current_location]
        # max_value = max(q_values_of_state.values())
        # action = np.random.choice([k for k, v in q_values_of_state.items() if v == max_value])
        return action

    def learn(self, old_state, reward, new_state, action):
        q_values_of_state = self.q_table[new_state]
        max_q_value_in_new_state = max(q_values_of_state.values())
        # print(self.q_table)
        current_q_value = self.q_table[old_state][action]
        self.q_table[old_state][action] = (1 - self.alpha) * current_q_value \
                                          + self.alpha * (reward + self.gamma * max_q_value_in_new_state)

    def show_q_table(self):
        for x in range(self.environment.height):
            for y in range(self.environment.width):
                print("(", x, ",", y, ")")
                print(self.q_table[x, y])

    def download_q_table(self, version):
        write_file_name = f"{self.environment.world_id}-{version}.txt"
        fiw = open(write_file_name, mode='a')
        for x in range(self.environment.height):
            for y in range(self.environment.width):
                x_y_q_value = [str(v) for k, v in self.q_table[(x, y)].items()]
                q_table_str = " ".join(x_y_q_value)
                q_table_str += "\n"
                fiw.write(q_table_str)
        fiw.close()

    def init_q_table(self, file_name):
        fir = open(file_name, "r")
        if os.path.getsize(file_name) != 0:
            for x in range(self.environment.height):
                for y in range(self.environment.width):
                    state = fir.readline()
                    state = state.rstrip("\n")
                    [n, s, w, e] = state.split(" ")
                    self.q_table[(x, y)] = {
                        Actions.North.value: float(n),
                        Actions.South.value: float(s),
                        Actions.West.value: float(w),
                        Actions.East.value: float(e)
                    }
            fir.close()
        else:
            raise Exception("Fail Initialization! The file is empty!")


if __name__ == '__main__':
    g = GridWorld(1)
    q = QAgent(g)
    q.init_q_table(name)
    # q.download_q_table("0.1")
    q.show_q_table()
