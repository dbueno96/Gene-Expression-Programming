from evoAlgorithm import EvoAlgorithm
from config import Config as conf
from utils.utils import *
import numpy as np
import argparse
import sys


def process_args(): 
    parser=argparse.ArgumentParser(description='Gene Expression Programming Based Algorithm')
    parser.add_argument('-r',default=False, help='Restore previuosly interrupted process')
    return parser.parse_known_args()

def main():

    args,_ = process_args()
    algorithm = EvoAlgorithm(conf)

    if args.r: 
        generation= algorithm.load_progress()
        algorithm.run(generation)
    else:
        create_save_dir(conf.save_dir)
        
        create_folder_in_saved(conf.env_name+'/')


        algorithm.run()
        # algorithm.show_result()



if __name__=='__main__':
    main()