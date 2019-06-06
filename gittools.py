# coding = utf-8
# using namespace std
from os import chdir, system
import typing
import json

# Fast Variables

__version__ = "alpha-0.1"
__author__ = "GiullianoRossi1987"
__github__ = __author__

__doc__ = """"""


class GitVars(object):

    __doc__ = """"""

    envvars = list()
    initalized = False

    class NotInitError(Exception):
        args = "The system have to be initalized to do this action!"

        def __init__(self): print(self.args)

    def __init__(self, file_vars="git-envvars.json"):
        with open(file_vars, "r") as envvars:
            self.envvars = json.loads(envvars.read())
        self.initalized = True
    
    @classmethod
    def check_initialized(cls): 
        if not cls.initalized: raise cls.NotInitError()

    @classmethod
    def check_envvar_exists(cls, var: str) -> bool: return var in cls.envvars



class InvalidHostTypeOption(Exception):
    args = "The address '%addr%'  to the repository is not compatible"

    def __init__(self, addr: str): print(self.args.replace("%addr%", addr))


class InvalidVarToGit(Exception):
    args = "'%var%' is not a valid variable to git command line!"

    def __init__(self, var: str): print(self.args.replace("%var%", var))


class InvalidFileMode(Exception):
    args = "'%filemode%' is not valid such as file mode to git command line!"

    def __init__(self, file_mode: str): print(self.args.replace("%filemode%", file_mode))


def clone_repo(addr: str, dir_to: typing.Optional[str] = "--pwd"):
    if dir_to != "--pwd":
        chdir(dir_to)
    system("git clone "+addr)


def init(dir_link="--pwd"):
    if dir_link != "--pwd": chdir(dir_link)
    system("git init")


def add(dir_to: typing.Optional[str] = "--pwd", data_to_push="--all"):
    if dir_to != "--pwd": chdir(dir_to)
    system("git add "+data_to_push)


def commit(message: str): system("git commit -m '"+message+"'")


def config(var: str, value, dir_to: str,mode: typing.Optional[str] = "--global", dir_pwd: typing.Optional[bool] = True):
    if not dir_pwd: chdir(dir_to)
    var_git_obj = GitVars()
    if var not in var_git_obj.envvars.keys(): raise InvalidVarToGit(var)
    system(f"git config {mode} {dir_to} {var} = '{value}'")


def gitmerge(remote: str, branch: typing.Optional[str]="master"):
    system("git merge "+remote+"\b"+branch)


def gitpush(remote: str, branch: typing.Optional[str]="master"):
    system("git merge "+remote+" "+branch)

def gitcheckrepo(dir_repo: str) -> bool:
    from os import listdir
    a = ".git" in listdir(dir_repo)
    del listdir
    return bool(a)











    
    






















