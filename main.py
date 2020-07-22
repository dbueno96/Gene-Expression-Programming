from evoAlgorithm import EvoAlgorithm
from config import Config as conf
from utils.utils import *
from utils.env_list import envs 
from tqdm import tqdm 
import numpy as np
import sys



def main():

    args = process_args()
    if valid_args(args):
        
        if args.restore: 
            if args.env== 'all' or args.env=='ALL' or args.env=='All':
                conf.max_timesteps=args.steps
                algorithm = EvoAlgorithm(conf)
                generation= algorithm.load_progress()
                
                 
                with tqdm(range(62),initial=(62-len(algorithm.conf.env_list[0])+1), total=62, unit=' envs', desc='Envs Progress' ) as bar:
                    algorithm.run(generation)
                    conf.env_list= np.delete(algorithm.conf.env_list, 0,1)
                    # print(algorithm.conf.env_list)
                    for env in algorithm.conf.env_list[0]:
                        # tqdm.write(env)
                        conf.env_name=env
                        conf.max_timesteps=args.steps
                        algorithm= EvoAlgorithm(conf)
                        create_folder_in_saved(conf.env_name+'/')
                        algorithm.run()
                        algorithm.conf.env_list= np.delete(algorithm.conf.env_list, 0,1)
                        bar.update()


            else: 
                conf.env_name=args.env
                conf.max_timesteps=args.steps
                algorithm = EvoAlgorithm(conf)
                create_save_dir(conf.save_dir)        
                create_folder_in_saved(conf.env_name+'/')
                algorithm.run()
    
        elif args.env== 'all' or args.env=='ALL' or args.env=='All':
            
            conf.env_list = np.array([envs[1:]])
            create_save_dir(conf.save_dir)
            with tqdm(62,initial=len(conf.env_list), total=62, unit=' envs', desc='Envs Progress' ) as bar:
                for env in conf.env_list[0]:
                    conf.env_name= env
                    conf.max_timesteps=args.steps

                    algorithm= EvoAlgorithm(conf)
                    create_folder_in_saved(conf.env_name+'/')
                    algorithm.run()
                    conf.env_list= np.delete(conf.env_list, 0,1)
                    bar.update()
        else:
            conf.env_name=args.env
            conf.max_timesteps=args.steps

            algorithm = EvoAlgorithm(conf)
            create_save_dir(conf.save_dir)        
            create_folder_in_saved(conf.env_name+'/')
            algorithm.run()



if __name__=='__main__':
    main()