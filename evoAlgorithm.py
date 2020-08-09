from tqdm import  tqdm,trange
from env_wrapper import GymEnv
from config import Config 
from baseAlgorithm import BaseAlgorithm
from agent import Agent
import numpy as np


class EvoAlgorithm(BaseAlgorithm): 

    def __init__(self, config): 
        super(EvoAlgorithm, self).__init__(config)
        self.head_size= config.head_size
        self.tail_size= config.tail_size
        self.head_mutation_rate= config.head_mutation_rate
        self.tail_mutation_rate= config.tail_mutation_rate
        self.obs_size= config.obs_size
        self.ops_size= config.ops_size
        self.max_steps=config.max_timesteps
        self.steps_per_episode
        self.gen_steps=0           

    
    def create_selection_matrix(self, index):
        selection_matrix= {
            'head': self.population_heads[index,:],
            'tail': self.population_tails[index,:]
        }
        return selection_matrix


    def _create_mutation_matrix(self, dim, rate):
        index=np.random.randint(low=0, high=dim, size=(1, int(dim*rate)+1))
        columns= np.random.randint(low=-10, high=10, size= (dim,index.shape[1]))
        mutation_matrix= np.identity(dim)
        mutation_matrix[:,index[0,:]]= columns
        return mutation_matrix

    def create_mutation_matrix(self):
        mutation_matrix= {
            'head': self._create_mutation_matrix(self.head_size, self.head_mutation_rate),
            'tail': self._create_mutation_matrix(self.tail_size, self.tail_mutation_rate)
        }
        return mutation_matrix

    def mutate(self, selected_index): 
        selected_mat= self.create_selection_matrix(selected_index)
        mutation_mat= self.create_mutation_matrix()
        self.population_heads[selected_index, :]= np.dot(selected_mat['head'], mutation_mat['head']) % self.ops_size
        self.population_tails[selected_index, :] = np.dot(selected_mat['tail'], mutation_mat['tail']) % self.obs_size
        self.mark_as_unchecked(selected_index)

    def compute_steps_to_play(self): 
        missing_steps= self.steps_per_episode
        dif = self.max_steps - self.played_steps
        if dif < missing_steps:
            missing_steps=dif
            return missing_steps
        else: 
            return missing_steps

    def compute_played_steps(self, steps): 
        self.played_steps+=steps

    def evaluate(self, index): 
        scores= []
        for i in index[0]: 
            agent = Agent(self.conf)
            agent.head, agent.tail= self.population_heads[i], self.population_tails[i]
            timesteps=self.compute_steps_to_play() 
            scores.append(agent.play(timesteps))
            self.compute_played_steps(agent.steps)
            self.gen_steps+=agent.steps
        return np.array([scores])

    def generate_index(self): 
        index= np.unique(np.random.randint(self.population_size, size= (1,self.pool_size)),axis=1)
        while index.shape[1] < self.pool_size:
            index= np.unique(np.random.randint(self.population_size, size= (1,self.pool_size)),axis=1)
        return index


    def update_max_fitness(self, index, fitness):
        self.max_fitness[index,:] = np.where(self.max_fitness[index,:][0] < fitness.T , fitness.T, self.max_fitness[index,:][0])

        
    def mark_as_checked(self, index): 
        self.checked_agents[index,:] = 1

    
    def mark_as_unchecked(self, index): 
        self.checked_agents[index,:] = 0

    
    def selection(self): 
        group1= self.generate_index()
        group2= self.generate_index()
        fitness_group1=  self.evaluate(group1)
        self.mark_as_checked(group1)
        fitness_group2= self.evaluate(group2)
        self.mark_as_checked(group2)

        selected_index= np.where(fitness_group1 > fitness_group2, group1, group2)
        self.update_max_fitness(group1, fitness_group1)
        self.update_max_fitness(group2, fitness_group2)
        self.update_solution()
        return np.unique(selected_index, axis=0 )

    

    def show_result(self): 
        head,tail =self.load_solution()
        print('Final Fitness:')
        print(self.max_fitness)
        print('Best Fitness: {}'.format(np.amax(self.max_fitness, axis=0)[0]))
        print('Best Head: {}'.format(head))
        print('Best Tail: {}'.format(tail))
    
    
    
    def update_solution(self): 
        max_index=np.argmax(self.max_fitness)
        if self.solution_index != max_index:
            self.solution_index= max_index
            self.save_solution()

    

    def run(self, initial=0): 
        with tqdm(self.max_steps, total=self.max_steps, initial=self.played_steps, unit=' steps', leave=False, desc=str(self.conf.env_name)) as bar:
            gen=initial
            while(1):
                # tqdm.write(str(gen))
                self.gen_steps=0
                selected_index= self.selection()
                self.mutate(selected_index)
                bar.update(self.gen_steps)
                
                gen+=1
                if self.played_steps >=self.max_steps:
                    self.save_solution()
                    break 
                if gen % self.conf.save_freq == 0: 
                    self.save_progress(gen)

    def solution(self, episodes=10, render=False):
        agent = Agent(self.conf)
        agent.head, agent.tail = self.load_solution()
        scores=[]
        for i in range(episodes):
            agent.total_reward=0
            score=agent.play(2*1e5, render=render)
            scores.append(score)
            print('Episode {} finished with {} points'.format(i+1,score))
        
        self.solution_scores= np.array(scores)
        self.solution_scores_mean= np.mean(self.solution_scores)

        print('Scores after {} episodes: {}'.format(episodes, self.solution_scores))
        print('Mean solution scores after {} episodes'.format(self.solution_scores_mean))
