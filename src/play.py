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

        # ��ȡ��ǰλ�ú͵÷�
        loc = get_location()
        print("��ǰλ�ã�", loc["location"], "�÷֣�", get_score())

        # ִ�в���
        while True:
            # ����һЩ����
            # ...

            # ��ȡִ�ж�����Ľ��
            res = make_a_move(move, loc["world"])
            print("�ƶ�����", move, "�÷�������", res["scoreIncrement"], "��λ�ã�", res["newState"])
            loc = get_location()
            print("��ǰλ�ã�", loc["location"], "�÷֣�", get_score())

            # �ж��Ƿ��ѵ����յ�
            if loc["location"] == "END":
                print("�ѵ����յ㣡�÷֣�", get_score())
                break

        # if environment.check_state() == 'TERMINAL':  # If game is in terminal state, game over and start next trial
        #     environment.__init__()
        #     game_over = True
        #
        # elif environment.check_state() == 'EXIT':  # ��������˳��ڣ��������ǰ��Ϸ����ʼ��һ������
        #     environment.__init__()
        #     game_over = True

    reward_per_episode.append(cumulative_reward)  # Append reward for current trial to performance log


    return reward_per_episode  # Return performance log
