import pandas as pd
import math
import numpy as np

# 计算多波束测深的覆盖宽度
def calculate_width(D, theta, alpha, distance, angle):
    # 当前的坡度角alpha_会随着angle 变化而变化
    alpha_ = math.atan(math.tan(15 * math.pi / 1800) * abs(math.sin(angle)))    
    # 当前的海水深度
    D = D + K * distance * math.tan(15 * math.pi / 1800) * math.cos(angle)
    # 覆盖的坡面长度
    W_D = D * (np.sin(math.pi / 3) / np.sin(math.pi / 6 + alpha_) + np.sin(math.pi / 3) / np.sin(math.pi / 6 - alpha_))
    # 投影后的覆盖宽度
    W = W_D * np.cos(alpha_)
    return W

# 测量船距海域中心点处的距离和角度数据
distances = [0, 0.3, 0.6, 0.9, 1.2, 1.5, 1.8, 2.1]
angles = [0, math.pi / 4, math.pi / 2, 3 * math.pi / 4, math.pi, math.pi * 5 / 4, math.pi * 3 / 2, math.pi * 7 / 4]

# 多波束测深系统的开角和坡度和海里与米的倍率和海域中心点处的海水深度
theta = math.pi * 2 / 3
alpha = math.pi * 15 / 1800
K = 1852
D = 120

# 创建一个空的二维列表来存储覆盖宽度
widths = []

# 计算并填充宽度数据
for angle in angles:
    row = [calculate_width(D, theta, alpha, distance, angle) for distance in distances]
    widths.append(row)

# 创建 DataFrame，不需要更改列 'angles' 的数据类型
result = pd.DataFrame(widths, columns=distances, index=angles)

# 将角度从弧度制转换为角度制
result.index = [math.degrees(angle) for angle in result.index]

# 设置 Pandas 显示选项，确保小数点均保留五位小数
pd.options.display.float_format = '{:.5f}'.format

# 打印计算结果
print(result)

# 尝试保存到Excel，但如果失败则显示错误信息，成功则result2.xlsx与当前python文件在一个文件夹里
try:
    result.to_excel('result2.xlsx', index=False)
except Exception as e:
    print("保存到Excel失败:", e)
