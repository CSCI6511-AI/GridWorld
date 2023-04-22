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
            old_state = environment.current_location  #   ȡ  ǰ״̬
            action = agent.choose_action(environment.actions)  # ѡ   ж
            reward = environment.make_step(action)  # ִ   ж     ȡ
            new_state = environment.current_location  #   ȡ  ״̬

            if learn == True:  #    ָ    ѧϰ        Q ֵ
                agent.learn(old_state, reward, new_state, action)

            cumulative_reward += reward  #  ۼƽ
            step += 1

            if environment.check_state() == 'TERMINAL':  #      Ϸ ѽ            ǰ  Ϸ    ʼ  һ
                environment.__init__()
                game_over = True


            elif environment.check_state() == 'EXIT':  #         ˳  ڣ        ǰ  Ϸ    ʼ  һ

                #  ޸Ĳ  ֣  ڵ     ں󣬼       λ õĵ÷ֲ ѡ     ·
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

        reward_per_episode.append(cumulative_reward)  #     ǰ      ۼƽ     ¼        ־

    return reward_per_episode  #               ۼƽ    б

