from matplotlib import pyplot as plt

from environment import WingEnv
from stable_baselines3.common.env_checker import check_env
from stable_baselines3 import PPO


env = WingEnv()
check_env(env)

# #%% train PPO model
# model = PPO("MlpPolicy", env)
# model.learn(total_timesteps=10_000)
# obs = env.reset()
#
# # %% run the model
# R, S, A = [], [], []
# for i in range(1000):
#     action, _states = model.predict(obs, deterministic=True)
#     obs, reward, done, info = env.step(action)
#     R.append(reward)
#     S.append(obs)
#     A.append(action)
#     print(f"a={action},s={obs},r={reward}")
#     # env.render()
#     if done:
#         obs = env.reset()
#
# env.close()
# # %% plot results
# plt.scatter(range(1000),R,s=0.3)
# plt.title("Reward")
# plt.show()
#
# plt.scatter(range(1000),A,s=0.3)
# plt.title("Action")
# plt.show()
#
# plt.scatter(range(1000),S,s=0.3)
# plt.title("State")
# plt.show()
