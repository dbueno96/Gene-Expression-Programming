import os


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