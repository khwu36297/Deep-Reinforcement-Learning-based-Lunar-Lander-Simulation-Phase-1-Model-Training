import matplotlib.pyplot as plt
import numpy as np
import cv2

def evaluate_agent(env, model, episodes=100):
    rewards = []
    fuel_usage = []
    for ep in range(episodes):
        obs, _ = env.reset()
        total_reward, fuel, done = 0, 0, False
        while not done:
            action, _ = model.predict(obs)
            if action != 0:
                fuel += 1
            obs, reward, terminated, truncated, _ = env.step(action)
            total_reward += reward
            done = terminated or truncated
        rewards.append(total_reward)
        fuel_usage.append(fuel)
    return rewards, fuel_usage

def plot_dashboard(rewards, fuel_usage, filename="lunarlander_dashboard.png"):
    plt.figure(figsize=(18, 5))

    plt.subplot(1, 2, 1)
    plt.plot(rewards, label="Reward per Episode")
    plt.xlabel("Episode")
    plt.ylabel("Reward")
    plt.title("Reward per Episode")
    plt.grid(True)
    plt.legend()

    plt.subplot(1, 2, 2)
    plt.plot(fuel_usage, color='orange', label="Fuel Usage per Episode")
    plt.xlabel("Episode")
    plt.ylabel("Fuel Usage (steps firing thruster)")
    plt.title("Fuel Usage per Episode")
    plt.grid(True)
    plt.legend()

    plt.tight_layout()
    plt.savefig(filename)
    plt.show()
    print(f"Dashboard saved as {filename}")

def save_video(frames, filename="output.mp4", fps=30):
    if not frames:
        print("No frames to save.")
        return
    height, width, layers = frames[0].shape
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    video = cv2.VideoWriter(filename, fourcc, fps, (width, height))

    for frame in frames:
        video.write(frame)

    video.release()
    print(f"Video saved as {filename}")