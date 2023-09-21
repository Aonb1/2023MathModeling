#Python
import math
import pandas as pd

def calculate_width(D, theta, alpha):
   #由正弦定理可知,设W为覆盖宽度，alpha为坡度角，theta为开角，D为当前的海水深度
   w1=(math.sin(math.radians(theta/2))/math.sin(math.radians(90+alpha-theta/2)))
   w2=(math.sin(math.radians(theta/2))/math.sin(math.radians(90-alpha-theta/2)))
   #抽象出覆盖宽度W和海水深度D的函数关系
   W=D*(w1+w2)*math.cos(math.radians(alpha))
   return W

#防止分母为0的情况
def calculate_overlap(d, W):
    """计算重叠率"""
    return 0 if W == 0 else 1 - d / W

# 数据初始化
distances = [-800, -600, -400, -200, 0, 200, 400, 600, 800]
#depth是根据D-x*tan(alpha)计算的，其中x为distances的距离
depths = [70 - math.tan(math.radians(1.5)) * d for d in distances]

descriptions = [f'距离中心点{abs(d)}米' for d in distances]
descriptions[4] = '中心点位置'

data = {
    '测线距中心点处的距离/m': distances,
    '海水深度/m': depths,
    '描述': descriptions
}
result = pd.DataFrame(data)

# 多波束测深系统参数
theta = 120
alpha = 1.5

# 使用Pandas的向量化计算来计算覆盖宽度
result['覆盖宽度/m'] = result['海水深度/m'].apply(calculate_width, args=(theta, alpha))

# 计算与前一条测线的重叠率
diff_values = result['测线距中心点处的距离/m'].diff()
result['与前一条测线的重叠率/%'] = ((1 - diff_values / result['覆盖宽度/m']) * 100).where(diff_values.notna(), other=None)

# 尝试保存到Excel，但如果失败则显示错误信息,成功则result1.xlsx与当前python文件在一个文件夹里
try:
    result.to_excel('result1.xlsx', index=False)
except Exception as e:
    print("保存到Excel失败:", e)

print(result)
