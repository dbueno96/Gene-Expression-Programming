from evoAlgorithm import EvoAlgorithm
from config import Config as conf
from utils.utils import *
from utils.env_list import envs 
import numpy as np
import sys



def main():

    args = process_args()
    if valid_args(args):
        if args.restore: 
            algorithm = EvoAlgorithm(conf)
            generation= algorithm.load_progress()
            algorithm.run(generation)
    
        elif args.env== 'all' or args.env=='ALL' or args.env=='All':
            
            conf.env_list = np.array([envs[1:]])
            create_save_dir(conf.save_dir)
            for env in conf.env_list[0]:
                conf.env_name= env
                conf.max_timesteps=args.steps
                conf.env_list= np.delete(conf.env_list, 0,1)

                algorithm= EvoAlgorithm(conf)
                create_folder_in_saved(conf.env_name+'/')
                algorithm.run()
        else:
            conf.env_name=args.env
            conf.max_timesteps=args.steps

            algorithm = EvoAlgorithm(conf)
            create_save_dir(conf.save_dir)        
            create_folder_in_saved(conf.env_name+'/')
            algorithm.run()



if __name__=='__main__':
    main()