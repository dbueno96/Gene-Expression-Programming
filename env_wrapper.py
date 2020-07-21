import gym
from gym import wrappers
import time
from tqdm import tqdm

class GymEnv(): 

    def __init__(self, name): 
        self.env = gym.make(name)
        self.max_actions= self.env.action_space.n
        self.info={'ale.lives': 0}
        self.observation=self.env.reset()
        self.initial_obs=self.env.reset()
        self.reward=0
        self.terminal=False
        self.record_game=False

    @property
    def lives(self):
        return self.info['ale.lives']


    def env_step(self, action):
        lives_before= self.lives 
        self.env.render()
        time.sleep(0.05)
        self.observation, reward, self.terminal, self.info= self.env.step(action)
        self.reward +=reward
        lives_now= self.lives
        if lives_now < lives_before: 
            self.terminal=True
            tqdm.write('yaper')
        return reward
        

    def new_game(self): 
        if self.terminal: 
            self.observation=self.env.reset()  
        if self.record_game: 
            self.record_game()
        self.reward=0
        self.terminal=False

    def is_static(self): 
            return self.reward==0


    def close_env(self): 
        self.env.close()

    def record_game(self): 
        self.env = wrappers.Monitor(self.env , './GymMonitor/')
