from utility_functions import *
import os


dir_venv_64 = os.path.join(os.getcwd(), 'venv', 'Scripts')


def install(lib):
    return f'pip --trusted-host pypi.python.org --trusted-host files.pythonhosted.org --trusted-host pypi.org install {lib}'


""" https://download.pytorch.org/whl/torch_stable.html """
# subprocess_cmd(f'cd {dir_venv_64} & {install(r"C:/Users/glovis-laptop/Downloads/torch-1.5.0+cpu-cp37-cp37m-win_amd64.whl")}')
# subprocess_cmd(f'cd {dir_venv_64} & {install(r"C:/Users/glovis-laptop/Downloads/torchvision-0.6.1+cpu-cp37-cp37m-win_amd64.whl")}')
subprocess_cmd(f'cd {dir_venv_64} & {install(os.path.join(os.getcwd(),"wheels", r"torch-1.5.0+cpu-cp37-cp37m-win_amd64.whl"))}')
subprocess_cmd(f'cd {dir_venv_64} & {install(os.path.join(os.getcwd(),"wheels", r"torchvision-0.6.1+cpu-cp37-cp37m-win_amd64.whl"))}')
# subprocess_cmd(f'cd {dir_venv_64} & {install(r"torch==1.5.1+cpu torchvision==0.6.1+cpu -f https://download.pytorch.org/whl/torch_stable.html")}')


""" https://stackoverflow.com/questions/42605769/openai-gym-atari-on-windows """
""" https://github.com/Kojoley/atari-py/releases """
# subprocess_cmd(f'cd {dir_venv_64} & {install("--no-index -f https://github.com/Kojoley/atari-py/releases atari_py")}')
# subprocess_cmd(f'cd {dir_venv_64} & {install(r"C:/Users/glovis-laptop/Downloads/atari_py-1.2.0-cp37-cp37m-win_amd64.whl")}')
subprocess_cmd(f'cd {dir_venv_64} & {install(os.path.join(os.getcwd(),"wheels", r"atari_py-1.2.0-cp37-cp37m-win_amd64.whl"))}')
subprocess_cmd(f'cd {dir_venv_64} & {install("matplotlib")} & {install("opencv-python")} & {install("gym")}')
# subprocess_cmd(f'cd {dir_venv_64} & {install("gym")}')
