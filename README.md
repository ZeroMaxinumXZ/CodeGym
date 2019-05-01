# CodeGym
A programming Gym environment for RL agents.

# Goal
To create, and maintain a flexible OpenAI Gym environment that enables RL agents to learn to code. 

# Installation Instructions:
```
git clone https://github.com/ZeroMaxinumXZ/CodeGym
cd CodeGym
pip install -e .
```

# Instructions
```
import CodeGym
import gym

env = gym.make('CodeEnv-v0')

#Due to current limitations, env.reset() returns rewards as well as an observation.

rew, obs = env.reset()
obs, _, done = env.step(action=5)

```
# TODO:
Make more stable.
Add other programming languages.
Add other rewards.
Add in examples

# Contributions
Any and all contributions are welcome. This project is open-sourced under thehttps://github.com/ZeroMaxinumXZ/CodeGym/edit/master/README.md MIT License.

