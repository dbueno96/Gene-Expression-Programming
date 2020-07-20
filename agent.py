from env_wrapper import GymEnv
from expression_tree import TreeNode
import math
from tqdm import tqdm

class Agent():

    def __init__(self, config):
        self.conf=config
        self.env= GymEnv(config.env_name)
        self.total_reward=0
        self.played_steps=0

    @property
    def steps(self):
        return self.played_steps



    def truncate_action(self, tree_eval): 
        try: 
            angle = tree_eval * math.pi
            angle = angle * math.pi /180
            result= (self.env.max_actions-1)*abs(math.sin(angle))
        except OverflowError: 
            result = 0

        return int(result)


    def choose_action(self,head,tail, observation):
        self.expr_tree= TreeNode(self.conf,None, self.conf.operators[head[0]][0], self.conf.operators[head[0]][1] )
        head=head[1:]
        self.expr_tree.create_expression_tree(head,tail,observation)
        action= self.truncate_action(self.expr_tree.evaluate_tree())
        return action
    
    def play(self, limit_steps=999):
        self.env.new_game()
        self.played_steps=0
        t=0
        static_check= [75,125,175]
        static=True
        while not self.env.terminal:
            action= self.choose_action(self.head, self.tail, self.env.observation)
            self.total_reward+= self.env.env_step(action)
            t+=1
            
            if t in static_check:
                static= static and self.env.is_static()

            if self.env.terminal or t > limit_steps or (static and t >=175) : 
                tqdm.write(str(limit_steps))
                tqdm.write(str(self.env.terminal))
                tqdm.write(str(t))
                tqdm.write('\tFinished after {} timesteps'.format(t))
                self.played_steps=t
                break
        return self.total_reward


    def random_play(self, steps=100): 
        for t in range(steps): 
            self.env.env.render()
            action= self.env.env.action_space.sample()
            o,r,d,info= self.env.env.step(action) 
            if self.env.terminal: 
                # print('Finished after {} timesteps'.format(t))
                break

        self.env.close_env()