# 参数
w = 1  # 测量带的宽度，单位为海里
o = 0.2 * w  # 重叠，即宽度的20%
east_boundary = 4  # 待测海域的东边界，单位为海里

# 初始化起始位置和用于存储选定位置的列表
current_position = 0
selected_positions = []

# 贪婪算法来放置测量带
while current_position < east_boundary:
    selected_positions.append(current_position)
    current_position += w - o  # 移动到下一个位置，考虑到重叠

# 计算相关指标
total_length_greedy = 5 * len(selected_positions)  # 测量带的总长度
missed_percentage_greedy = 0  # 漏测海区的百分比
excess_overlap_length_greedy = 0  # 超过20%的重叠长度

# 打印结果
print("选定的测量带位置:", selected_positions)
print("测量带的总长度:", total_length_greedy, "海里")
print("漏测海区百分比:", missed_percentage_greedy, "%")
print("超过20%的重叠长度:", excess_overlap_length_greedy, "海里")
