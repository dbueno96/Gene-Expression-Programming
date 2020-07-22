from utils.operators import OPERATORS

class Config(): 


    max_timesteps= 1e3
    head_mutation_rate= 0.3
    tail_mutation_rate= 0.2

    pop_size=5
    generations=30
    pool_size=2

    head_size=3
    tail_size=10
    
    ops_size= 18
    obs_size=128


    env_name='Adventure-ram-v4'

    operators=OPERATORS

    save_dir= './saved/'
    save_freq= 5 #in generations