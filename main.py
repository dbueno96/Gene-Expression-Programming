from evoAlgorithm import EvoAlgorithm
from config import Config as conf
from utils.utils import *
from utils.env_list import envs 
import numpy as np
import argparse
import sys


def process_args(): 
    parser=argparse.ArgumentParser(description='Gene Expression Programming Based Algorithm')
    parser.add_argument('--restore',default=False, type=bool, help='Restore previuosly interrupted process')
    parser.add_argument('--steps', default=conf.max_timesteps, type=int, help='Run algorithm for this amount of timesteps on environment(s)')
    parser.add_argument('--env', default=None, type=str, help='Run algorithm on this gym atari ram environments')
    parser.add_argument('--list-envs', default=False, type=bool, help='List all atari gym ram environments')
    return parser.parse_args()


def main():

    args = process_args()
    if valid_args(args):
        if args.restore: 
            algorithm = EvoAlgorithm(conf)
            generation= algorithm.load_progress()
            algorithm.run(generation)
    
        elif args.env== 'all' or args.env=='ALL' or args.env=='All':
            
            conf.env_list = np.array([envs[1:]])
            for env in conf.env_list[0]:
                conf.env_name= env
                conf.env_list= np.delete(conf.env_list, 0,1)

        else:
            conf.env_name=args.env
            conf.max_timesteps=args.steps

            algorithm = EvoAlgorithm(conf)
            create_save_dir(conf.save_dir)        
            create_folder_in_saved(conf.env_name+'/')
            algorithm.run()
            # algorithm.show_result()



if __name__=='__main__':
    main()