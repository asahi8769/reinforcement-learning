from utility_functions import subprocess_cmd, old_ver_directory
import os


class GitCommandLines():
    def __init__(self):
        self.repository = r'https://github.com/asahi8769/reinforcement-learning.git'
        subprocess_cmd (f'git config --global user.name Ilhee Lee')
        subprocess_cmd (f'git config --global user.email asahi8769@gmail.com')

    def push_rep(self):
        self.clone_rep()
        self.ask_overwrite()
        subprocess_cmd (f'git init')
        subprocess_cmd (f'git add .')
        subprocess_cmd (f'git config --global http.sslVerify false')
        subprocess_cmd (f'git commit -m "Apply all changes"')
        subprocess_cmd (f'git remote add origin {self.repository}')
        subprocess_cmd (f'git push --force origin master')
        subprocess_cmd (f'git remote remove origin')

    def clone_rep(self):
        rel_dir = os.path.relpath(old_ver_directory(), os.getcwd())
        subprocess_cmd (f'git clone {self.repository[:-4]} {rel_dir}')

    def history(self):
        subprocess_cmd (f'git log ')

    def ask_overwrite(self):
        if input('Overwrite current repository? (y/n, Default : n)').lower() != 'y':
            return


if __name__ == "__main__":
    GitCommandLines().push_rep()