import os
from utils.env_list import envs

def valid_args(args): 
    if args.env in envs or args.env=='All' or  args.env=='ALL':
        if args.steps >0 :
            return True
        else:
            return False



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