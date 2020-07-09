import gym
import numpy as np
from dqn_agent import DQNAgent
from utils import plot_learning_curve, make_env
from utility_functions import *
import pickle


def dqn_train():
    env = make_env('PongNoFrameskip-v4')

    load_checkpoint = False
    save_checkpoint = True
    learning_enabled = True
    rendering_enabled = False

    n_games = 100
    agent = DQNAgent(gamma=0.99, epsilon=1.0, lr=0.0001, input_dims=(env.observation_space.shape),
                     n_actions=env.action_space.n, mem_size=50000, eps_min=0.1, batch_size=32, replace=1000,
                     eps_dec=1e-5, chkpt_dir='models/', algo='DQNAgent', env_name='PongNoFrameskip-v4')

    if load_checkpoint:
        agent.load_models()
        with open('models/best_score.pkl', 'rb') as file:
            best_score = pickle.load(file)
    else :
        best_score = -np.inf

    fname = agent.algo + '_' + agent.env_name + '_lr' + str(agent.lr) + '_' + str(n_games) + 'games'
    figure_file = 'plots/' + fname + '.png'

    n_steps = 0
    scores, eps_history, steps_array = [], [], []

    for i in range(n_games):
        done = False
        observation = env.reset()
        score = 0
        while not done:
            action = agent.choose_action(observation)
            observation_, reward, done, info = env.step(action)
            score += reward
            if learning_enabled:
                agent.store_transition(observation, action, reward, observation_, int(done))
                agent.learn()
            if rendering_enabled :
                env.render()
            observation = observation_
            n_steps += 1
        scores.append(score)
        steps_array.append(n_steps)

        avg_score = np.mean(scores[-100:])
        print('episode: ', i,'score: ', score, ' average score %.1f' % avg_score, 'best score %.2f' % best_score,
            'epsilon %.2f' % agent.epsilon, 'steps', n_steps)

        if avg_score > best_score:
            best_score = avg_score
            if save_checkpoint:
               agent.save_models()
               with open('models/best_score.pkl', 'wb') as file:
                   pickle.dump(best_score, file)

        eps_history.append(agent.epsilon)
        if load_checkpoint and n_steps >= 18000:
            break

    x = [i+1 for i in range(len(scores))]
    plot_learning_curve(steps_array, scores, eps_history, figure_file)


if __name__ == '__main__':
    dqn_train()