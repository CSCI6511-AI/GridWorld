from http_requests import http_requests
import time

def play(environment, agent):
    # Initialise values of each game
    cumulative_reward = 0
    step = 0
    game_over = False
    score = 0
    while not game_over:
        old_state = environment.current_location
        # choose action
        action = agent.choose_action(environment.get_available_actions)
        # make move and get reward
        reward, score_increment = environment.make_step(action)
        # if reward is None means already exit current world --> game terminate
        if reward == 0:
            game_over = True
            score = http_requests.get_score()
        new_state = environment.current_location
        real_action = environment.check_action(old_state, new_state)
        if real_action is None:
            continue
        agent.learn(old_state, reward, new_state, real_action)

        cumulative_reward += reward
        step += 1

        print(f"old state: {old_state}")
        print(f"new state: {new_state}")
        print(f"current reward: {reward}")
        print(f"score_increment: {score_increment}")
        print(f"action: {action}")
        print(f"real action: {real_action}")

        time.sleep(5)

    print(f"cumulative_reward: {cumulative_reward}")
    print(f"step count: {step}")
    print(f"score: {score}")
