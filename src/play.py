def play(environment, agent):
    """The play function runs iterations and updates Q-values if desired."""
    cumulative_reward = 0  # Initialise values of each game
    step = 0
    game_over = False
    while not game_over:  # Run until max steps or until game is finished
        old_state = environment.current_location
        action = agent.choose_action(environment.get_available_actions)
        reward = environment.make_step(action)
        if reward == 0:
            game_over = True
        new_state = environment.current_location
        real_action = environment.check_action(old_state, new_state)
        agent.learn(old_state, reward, new_state, real_action)

        cumulative_reward += reward
        step += 1
        print(f"old state: {old_state}")
        print(f"new state: {new_state}")
        print(f"current reward: {reward}")
        print(f"action: {action}")
        print(f"real action: {real_action}")
