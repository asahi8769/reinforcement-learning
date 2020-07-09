from DQN.main_dqn import *
import sys

sys.path.append(r'D:\devs\reinforce\venv\Lib\site-packages')
sys.path.append(r'D:\devs\reinforce\venv\Scripts')


class ReinforceMain:
    print('Start DQN Learning')
    dqn_train()


if __name__ == '__main__':
    ReinforceMain()