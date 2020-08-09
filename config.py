from utils.operators import OPERATORS

class Config(): 


    max_timesteps= 1e8
    steps_per_episode= 5000
    head_mutation_rate= 0.3
    tail_mutation_rate= 0.2

    pop_size=15
    generations=1e6
    pool_size=2

    head_size=24
    tail_size=head_size*3 +1
    
    ops_size= 18
    obs_size=128


    env_name='Adventure-ram-v4'

    operators=OPERATORS

    save_dir= './saved/'
    save_freq= 50 #in generations