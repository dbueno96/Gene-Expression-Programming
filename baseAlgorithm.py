import numpy as np
from utils.utils import remove_loaded_files
class BaseAlgorithm(): 

    def __init__(self,config):
        self.conf= config
        self.population_size= config.pop_size
        self.generations= config.generations
        self.pool_size= config.pool_size
        self.save_dir= config.save_dir+config.env_name+'/'
        self.solution_index =0
        self.max_fitness= np.zeros(shape=(self.population_size, 1))
        self.checked_agents= np.zeros(shape=(self.population_size, 1))
        self.played_steps=0
        self.population_heads, self.population_tails= self._init_population(self.conf)
        



    def _init_population(self, conf):
        heads=np.random.randint(conf.ops_size, size=(self.population_size, conf.head_size))
        tails=np.random.randint(conf.obs_size, size=(self.population_size, conf.tail_size))
        return heads,tails



    def save_solution(self,): 
        np.save(self.save_dir+'best_head.npy', self.population_heads[self.solution_index])
        np.save(self.save_dir+'best_tail.npy', self.population_tails[self.solution_index])

    def load_solution(self): 
        head= np.load(self.save_dir+'best_head.npy')
        tail= np.load(self.save_dir+'best_tail.npy')
        return head, tail


    def save_progress(self, generation): 
        try: 
            np.save(self.save_dir+'../env_list.npy', self.conf.env_list)
        except AttributeError:
            pass
        
        np.save(self.save_dir+'heads.npy', self.population_heads)
        np.save(self.save_dir+'tails.npy', self.population_tails)
        np.save(self.save_dir+'max_fitness.npy', self.max_fitness)
        np.save(self.save_dir+'gen_index.npy', np.array([[generation, self.solution_index,self.played_steps]]))

    def load_progress(self): 
        print('Loading progress')
        try: 
            self.conf.env_list=np.load(self.save_dir+'../env_list.npy')
            self.conf.env_name= self.conf.env_list[0][0]
            self.save_dir='./saved/'+ str(self.conf.env_name) + '/'
        except IOError: 
            pass
        self.population_heads= np.load(self.save_dir+'heads.npy')
        self.population_tails= np.load(self.save_dir+'tails.npy')
        self.max_fitness=np.load(self.save_dir+'max_fitness.npy')
        gen_solution_steps=np.load(self.save_dir+'gen_index.npy')
        gen, self.solution_index, self.played_steps= gen_solution_steps[0][0], gen_solution_steps[0][1], gen_solution_steps[0][2]
        # remove_loaded_files(self.save_dir)
        print('Done!')
        return gen
