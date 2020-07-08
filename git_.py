from utility_functions import subprocess_cmd, make_pulled_dir
import os


class GitCommandLines():
    def __init__(self):
        self.repository = r'https://github.com/asahi8769/reinforcement-learning.git'
        self.rel_dir = None
        subprocess_cmd (f'git config --global user.name Ilhee Lee')
        subprocess_cmd (f'git config --global user.email asahi8769@gmail.com')

    def push_rep(self):
        self.clone_rep()
        if self.ask_overwrite() is False:
            os.startfile(self.rel_dir)
            return
        subprocess_cmd (f'git init')
        subprocess_cmd (f'git add .')
        subprocess_cmd (f'git config --global http.sslVerify false')
        subprocess_cmd (f'git commit -m "Apply all changes"')
        subprocess_cmd (f'git remote add origin {self.repository}')
        subprocess_cmd (f'git push --force origin master')
        subprocess_cmd (f'git remote remove origin')

    def clone_rep(self):
        self.rel_dir = os.path.relpath(make_pulled_dir(), os.getcwd())
        subprocess_cmd (f'git clone {self.repository[:-4]} {self.rel_dir}')

    def history(self):
        subprocess_cmd (f'git log ')

    def ask_overwrite(self):
        if input('Overwrite current repository? (y/n, Default : n) :').lower() != 'y':
            return False


if __name__ == "__main__":
    GitCommandLines().push_rep()