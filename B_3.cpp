#include <iostream>
#include <cmath>

using namespace std;

// 常量定义
const double theta = M_PI * 2 / 3;    // θ的定义，单位为弧度
const double alpha = M_PI * 15 / 1800; // α的定义，单位为弧度
const double K = 1852;                // K的常数值
const double D = 120;                 // D的常数值
const double C = sin(M_PI / 3) / (sin(M_PI / 6 + alpha)) + sin(M_PI / 3) / (sin(M_PI / 6 - alpha)); 
const double x = 1 + 0.9 * C * sin(15.0 / 1800 * M_PI);

// 临界值的计算
//206.9927是根据中心海域点海水深度计算得到的西边界上的海水深度
const double hmax = (206.9927 / sin(M_PI / 6)) * (sin(M_PI * 285 / 1800) / sin(M_PI * 915 / 1800)); // hmax的计算公式
const double hmin = (2 * 1852 * tan(15.0 / 1800 * M_PI)) + 110 - (1852 * 4 * tan(15.0 / 1800 * M_PI)); // hmin的计算公式

int main() {
    cout<<"南北走向为最佳的测线方向，其覆盖宽度最稳定"<<endl;
    double a = hmax; // 初始化a为hmax值
    const double b = 206.9927 / (1.0 - sin(M_PI / 3) * sin(15.0 / 1800 * M_PI) / sin(M_PI / 6 + 15.0 / 1800 * M_PI)); // b的计算公式
    double length = 1; // 测量条数初始化为1（至少一条）

    // 当b与a之差大于1e-5时继续循环
    while (b - a >= 1e-5) {
        // 根据给定条件调整length的值
        while ((a / hmin - pow(x, length)) >= 1e-5) {
            length++;
        }// 输出当前海水深度值和测线length条数和测线总长度
        length=length+1;
        cout << "h: " << a << "    length: " << length <<"  Lsum(/N mile):"<<length*2<<endl;
        a += 0.1; // a增加0.1,模拟海水深度在起点区间取到所有可能值
        length = 1; // 重置length为1
    }

    return 0;
}
