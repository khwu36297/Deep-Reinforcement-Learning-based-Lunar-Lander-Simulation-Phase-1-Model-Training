import matplotlib.pyplot as plt
import numpy as np

def generate_report(rewards, fuel_usage, filename="report_summary.txt"):
    avg_reward = np.mean(rewards)
    avg_fuel = np.mean(fuel_usage)
    success_rate = sum(r > 200 for r in rewards) / len(rewards) * 100

    report = f"""
    LunarLander AI Training Report
    =============================

    Average Reward: {avg_reward:.2f}
    Average Fuel Usage: {avg_fuel:.2f}
    Success Rate (Reward > 200): {success_rate:.2f} %

    Recommendations:
    - Adjust training parameters if success rate is low.
    - Monitor fuel usage to improve efficiency.
    """

    with open(filename, "w") as f:
        f.write(report)
    print(f"Report saved to {filename}")

if __name__ == "__main__":
    # ตัวอย่างเรียกใช้ (ปรับตามข้อมูลจริง)
    sample_rewards = [250, 150, 210, 300, 180]
    sample_fuel = [50, 80, 60, 55, 90]
    generate_report(sample_rewards, sample_fuel)