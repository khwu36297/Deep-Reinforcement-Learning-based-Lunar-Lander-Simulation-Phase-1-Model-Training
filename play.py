import gymnasium as gym
from stable_baselines3 import PPO
import pygame
import numpy as np
import matplotlib.pyplot as plt
import cv2
from utils import evaluate_agent, plot_dashboard

def play_and_record(model_path="ppo_lunarlander", episodes=100):
    env = gym.make("LunarLander-v3", render_mode="rgb_array")
    model = PPO.load(model_path)

    # เก็บข้อมูลจากการเล่น
    rewards, fuel_usage = evaluate_agent(env, model, episodes)

    # แสดงและบันทึกกราฟ dashboard
    plot_dashboard(rewards, fuel_usage)

    # เริ่ม pygame แสดงภาพ และบันทึกวิดีโอ
    pygame.init()
    screen = pygame.display.set_mode((600, 400))
    pygame.display.set_caption("LunarLander AI Visualization")
    clock = pygame.time.Clock()

    frame_width, frame_height = 600, 400
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter('lunarlander_playback.mp4', fourcc, 30.0, (frame_width, frame_height))

    obs, _ = env.reset()
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        action, _ = model.predict(obs)
        obs, reward, terminated, truncated, info = env.step(action)

        img = env.render()
        surf = pygame.surfarray.make_surface(np.flipud(np.rot90(img)))
        screen.blit(surf, (0, 0))
        pygame.display.flip()

        img_bgr = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
        img_bgr = cv2.resize(img_bgr, (frame_width, frame_height))
        out.write(img_bgr)

        clock.tick(30)

        if terminated or truncated:
            obs, _ = env.reset()

    env.close()
    pygame.quit()
    out.release()
    print("Video saved as lunarlander_playback.mp4")

if __name__ == "__main__":
    play_and_record()