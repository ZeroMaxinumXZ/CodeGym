#Please use gym environment at your own risk and preferably on a test computer.

from gym import core, spaces, Env
from gym.utils import seeding
import subprocess



def keys():
    key_list = []
    not_allowed = [33]
    for i in range(32, 127):
        if i not in not_allowed:

            key_list.append(chr(i))
    return key_list

class CodeEnv(Env):
    def __init__(self, debug):
        self.debug = debug
        self.num_actions = len(keys()) 
        self.observation_amount = 1024
        self.observation_space = []
        self.type_list = []
    def step(self, action, type=[]):
        action = min(action, self.num_actions) 
        key_action = keys()[action]
        self.observation_space.append(action)
        self.type_list.append(key_action)
        rewards = 0 #True rewards only happen at reset method.
        done = len(self.observation_space) > self.observation_amount #Done is when the amount in observation space exceeds obs amount. 
        return self.observation_space, rewards, done
    def reset(self, rewards=0.0, code_file_save = 'codefrom.cpp'):
        code = ''.join(self.type_list)
        with open(code_file_save, "w+") as code_out:
            #code_out.write("try: \n    ")
            code_out.write(code)
            #code_out.write("\nexcept: \n    pass")
        try:
            returned = subprocess.check_output(["g++", code_file_save]).decode('utf-8')
        except subprocess.CalledProcessError as e:
            returned = str(e)            
        print("Complete")
        if "error" not in returned: #RELIEF...
            reward = 1
        else:
            reward = 0
        self.observation_space = []
        self.type_list = []
        return self.observation_space, reward

if __name__ == '__main__':
    print(keys())
    r = CodeGym(debug=True)
    obs, _, done = r.step(action=1)
    obs, reward = r.reset()
