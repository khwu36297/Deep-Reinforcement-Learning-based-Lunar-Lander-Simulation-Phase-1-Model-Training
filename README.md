# Deep Reinforcement Learning-based Lunar Lander Simulation: Phase 1 - Model Training

This project applies Proximal Policy Optimization (PPO) algorithm to train a deep reinforcement learning agent for the LunarLander-v3 environment. The simulation includes model training, evaluation, visualization, real-time playback, and report generation.

## 🧪 Phase 1 Scope
- LunarLander-v3 environment (Gymnasium)
- PPO-based agent (Stable-Baselines3)
- Model training with evaluation and performance metrics
- Dashboard visualization (matplotlib)
- Real-time video capture (pygame, OpenCV)
- Automatic report generation

## 📊 Results

- **Average Reward:** 218.00
- **Average Fuel Usage:** 67.00
- **Success Rate (Reward > 200):** 60%

Example dashboard output:

![Dashboard](outputs/lunarlander_dashboard.png)

## 🏗 Project Structure

- `train.py` — Model training using PPO
- `play.py` — Model evaluation with dashboard and real-time visualization
- `utils.py` — Utility functions (evaluation, plotting, video)
- `report.py` — Generate evaluation report
- `envs/` — Additional environment configurations
- `saved_model/` — Trained model files
- `outputs/` — Evaluation outputs and visualizations
- `paper/` — Full IEEE Research Paper for Phase 1

## ⚙️ Setup

```bash
# Clone repository
git clone https://github.com/yourusername/Deep-Reinforcement-Learning-based-Lunar-Lander-Simulation-Phase-1-Model-Training.git

cd Deep-Reinforcement-Learning-based-Lunar-Lander-Simulation-Phase-1-Model-Training

# Create virtual environment
python -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
