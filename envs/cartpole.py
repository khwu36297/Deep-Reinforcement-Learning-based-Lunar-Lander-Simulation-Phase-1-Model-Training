import gymnasium as gym
from stable_baselines3 import PPO
from stable_baselines3.common.env_util import make_vec_env

def train_cartpole(total_timesteps=200_000, save_path="ppo_cartpole"):
    env = make_vec_env("CartPole-v1", n_envs=8)
    model = PPO("MlpPolicy", env, verbose=1)
    model.learn(total_timesteps=total_timesteps)
    model.save(save_path)
    print(f"CartPole model saved to {save_path}")

if __name__ == "__main__":
    train_cartpole()
