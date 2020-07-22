import os
import argparse
from utils.env_list import envs

def valid_args(args): 
    if args.env in envs or args.env=='All' or  args.env=='ALL':
        if args.steps >0 :
            return True
        else:
            return False

def process_args(): 
    parser=argparse.ArgumentParser(description='Gene Expression Programming Based Algorithm')
    parser.add_argument('--restore',default=False, type=bool, help='Restore previuosly interrupted process')
    parser.add_argument('--steps', default=2000, type=int, help='Run algorithm for this amount of timesteps on environment(s)')
    parser.add_argument('--env', default=None, type=str, help='Run algorithm on this gym atari ram environments')
    parser.add_argument('--list_envs', default=False, type=bool, help='List all atari gym ram environments')
    parser.add_argument('--result', default=False, type=bool, help='View result on especified gym atari ram environment')
    return parser.parse_args()

def show_envs(): 
    for env in envs:
        print(env)

def create_save_dir(foldername='saved'): 
    path='./{}'.format(foldername)  
    if not os.path.exists(foldername):
        os.makedirs(path, exist_ok=True)


def create_folder_in_saved(foldername): 
    path='./saved/{}'.format(foldername)  
    if not os.path.exists(foldername):
        os.makedirs(path, exist_ok=True)

def remove_loaded_files(dir): 
    files= [f for f in os.listdir(dir) if f.endswith('.npy')] 
    for f in files:
        os.remove(dir+f)
    if os.path.exists(dir+'../env_list.npy'):
        os.remove(dir+'../env_list.npy')