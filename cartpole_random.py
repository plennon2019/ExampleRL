import gymnasium as gym
import matplotlib.pyplot as plt

# Create the environment (no GUI)
env = gym.make("CartPole-v1", render_mode=None)

obs, info = env.reset()
done = False
step_num = 0

# Track pole angle over time
angles = []

while not done:
    action = env.action_space.sample()  # Random action (0 or 1)
    obs, reward, terminated, truncated, info = env.step(action)
    done = terminated or truncated

    pole_angle = obs[2]  # Index 2 = pole angle in radians
    angles.append(pole_angle)

    step_num += 1
    print(f"Step {step_num}: Angle = {pole_angle:.4f} radians")

env.close()

# Plot the angle history
plt.plot(angles, label="Pole Angle (radians)")
plt.axhline(y=0.0, color='gray', linestyle='--')
plt.xlabel("Time Step")
plt.ylabel("Pole Angle (radians)")
plt.title("Pole Angle Over Time in CartPole-v1")
plt.grid(True)
plt.legend()
plt.show()
