from grid_world import GridWorld
from q_agent import Q_Agent

def play(environment, agent, trials=500, max_steps_per_episode=1000, learn=False):
    """The play function runs iterations and updates Q-values if desired."""
    reward_per_episode = []  # Initialise performance log

    for trial in range(trials):  # Run trials
        cumulative_reward = 0  # Initialise values of each game
        step = 0
        game_over = False
        while step < max_steps_per_episode and game_over != True:  # Run until max steps or until game is finished
            old_state = environment.current_location  # 获取当前状态
            action = agent.choose_action(environment.actions)  # 选择行动
            reward = environment.make_step(action)  # 执行行动并获取奖励
            new_state = environment.current_location  # 获取新状态

            if learn == True:  # 如果指定了学习，则更新 Q 值
                agent.learn(old_state, reward, new_state, action)

            cumulative_reward += reward  # 累计奖励
            step += 1

            if environment.check_state() == 'TERMINAL':  # 如果游戏已结束，则结束当前游戏并开始下一个试验
                environment.__init__()
                game_over = True


            elif environment.check_state() == 'EXIT':  # 如果遇到了出口，则结束当前游戏并开始下一个试验

                # 修改部分：在到达出口后，计算所有位置的得分并选择最佳路径行走
                scores = agent.get_scores(environment)
                best_action = agent.get_best_action(environment, scores)
                while best_action != None:
                    action = best_action
                    reward = environment.make_step(action)
                    cumulative_reward += reward
                    step += 1
                    if environment.check_state() == 'TERMINAL':
                        environment.__init__()
                        game_over = True
                        break
                    elif environment.check_state() == 'EXIT':
                        game_over = True
                        break
                    scores = agent.get_scores(environment)
                    best_action = agent.get_best_action(environment, scores)
                break

        reward_per_episode.append(cumulative_reward)  # 将当前试验的累计奖励记录到性能日志中

    return reward_per_episode  # 返回所有试验的累计奖励列表

