from grid_world import GridWorld
from q_agent import Q_Agent


def play(environment, agent, max_steps_per_episode=1000, learn=False):
    """The play function runs iterations and updates Q-values if desired."""
    reward_per_episode = []  # Initialise performance log

    cumulative_reward = 0  # Initialise values of each game
    step = 0
    game_over = False
    while game_over != True:  # Run until max steps or until game is finished
        old_state = environment.current_location
        action = agent.choose_action(environment.actions)
        reward = environment.make_step(action)
        if reward == 0:
            game_over = True
        new_state = environment.current_location

        if learn == True:  # Update Q-values if learning is specified
            agent.learn(old_state, reward, new_state, action)

        cumulative_reward += reward
        step += 1

        # 获取当前位置和得分
        loc = get_location()
        print("当前位置：", loc["location"], "得分：", get_score())

        # 执行测试
        while True:
            # 进行一些操作
            # ...

            # 获取执行动作后的结果
            res = make_a_move(move, loc["world"])
            print("移动方向：", move, "得分增量：", res["scoreIncrement"], "新位置：", res["newState"])
            loc = get_location()
            print("当前位置：", loc["location"], "得分：", get_score())

            # 判断是否已到达终点
            if loc["location"] == "END":
                print("已到达终点！得分：", get_score())
                break

        # if environment.check_state() == 'TERMINAL':  # If game is in terminal state, game over and start next trial
        #     environment.__init__()
        #     game_over = True
        #
        # elif environment.check_state() == 'EXIT':  # 如果遇到了出口，则结束当前游戏并开始下一个试验
        #     environment.__init__()
        #     game_over = True

    reward_per_episode.append(cumulative_reward)  # Append reward for current trial to performance log


    return reward_per_episode  # Return performance log
