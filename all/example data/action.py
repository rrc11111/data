import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import PillowWriter

# 替换为 .trc 文件的路径
file_path = "Remotetake0125-Body25.trc"

# 加载 TRC 文件（跳过前 5 行头部信息）
data = pd.read_csv(file_path, sep='\t', skiprows=5, header=None)

# 提取关节名称
joint_names = [
    "HeadTop", "LHeadFront", "LHeadBack", "RHeadFront", "RHeadBack",
    "C7", "T10", "CLAV", "STRN", 
    "LShoulderFront", "LShoulderBack", "LUArmHigh", "LElbow", "LElbowIn", 
    "LForearm", "LWristIn", "LWristOut", "LHandIn", "LHandOut",
    "RShoulderFront", "RShoulderBack", "RUArmHigh", "RElbow", "RElbowIn", 
    "RForearm", "RWristIn", "RWristOut", "RHandIn", "RHandOut",
    "WaistFront", "WaistSide", "WaistBack", "WaistRFront", "WaistRSide", "WaistRBack",
    "LThigh", "LKnee", "LKneeIn", "LShin", "LAnkleout", "LHeel", "LMT5", "LMT1", "LToe",
    "RThigh", "RKnee", "RKneIn", "RShin", "RAnkleout", "RHeel", "RMT5", "RMT1", "RToe"
]

# 提取关节数据（假设前三列是元数据）
joint_data_columns = data.iloc[:, 3:162]  # 获取关节数据列
num_joints = joint_data_columns.shape[1] // 3  # 每个关节包含 X, Y, Z
print(num_joints)
# 检查是否关节数量与关节名称匹配
if num_joints > len(joint_names):
    print(f"警告：关节名称不足，仅使用前 {len(joint_names)} 个关节。")
    joint_names = joint_names[:num_joints]

# 准备每个关节的轨迹数据
all_joint_trajectories = [
    {
        "X": joint_data_columns.iloc[:, i * 3],
        "Y": joint_data_columns.iloc[:, i * 3 + 1],
        "Z": joint_data_columns.iloc[:, i * 3 + 2],
    }
    for i in range(num_joints)
]

# 创建 3D 动画
fig_all = plt.figure(figsize=(10, 7))
ax_all = fig_all.add_subplot(111, projection='3d')

# 初始化所有关节的散点图，并显示具体点名称作为图例
scatters_all = [
    ax_all.scatter([], [], [], label=joint_names[i]) for i in range(num_joints)
]

# 设置坐标轴范围
ax_all.set_xlim(joint_data_columns.min().min(), joint_data_columns.max().max())
ax_all.set_ylim(joint_data_columns.min().min(), joint_data_columns.max().max())
ax_all.set_zlim(joint_data_columns.min().min(), joint_data_columns.max().max())

# 设置坐标轴标签
ax_all.set_title("3D Animation of All Joints")
ax_all.set_xlabel("X Coordinate")
ax_all.set_ylabel("Y Coordinate")
ax_all.set_zlabel("Z Coordinate")
ax_all.legend(loc='upper right', bbox_to_anchor=(1.5, 1.0))

# 定义动画更新函数
def update_all(frame):
    for i, scatter in enumerate(scatters_all):
        scatter._offsets3d = (
            [all_joint_trajectories[i]["X"][frame]],
            [all_joint_trajectories[i]["Y"][frame]],
            [all_joint_trajectories[i]["Z"][frame]],
        )
    return scatters_all

# 动画帧数
num_frames = len(data)

# 创建动画
ani_all = FuncAnimation(fig_all, update_all, frames=100, interval=50, blit=False)

# 保存动画为 GIF
output_gif_path = "joint_trajectories_animation_with_names.gif"
ani_all.save(output_gif_path, writer=PillowWriter(fps=20))

print(f"动画已保存为 {output_gif_path}")
