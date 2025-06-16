import gymnasium as gym
from stable_baselines3 import PPO
from stable_baselines3.common.env_util import make_vec_env

def train_agent(env_id="LunarLander-v3", total_timesteps=500_000, save_path="ppo_lunarlander"):
    env = make_vec_env(env_id, n_envs=8)
    model = PPO("MlpPolicy", env, verbose=1)
    model.learn(total_timesteps=total_timesteps)
    model.save(save_path)
    print(f"Model saved to {save_path}")

if __name__ == "__main__":
    train_agent()