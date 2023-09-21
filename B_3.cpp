#include <iostream>
#include <cmath>

using namespace std;

// ��������
const double theta = M_PI * 2 / 3;    // �ȵĶ��壬��λΪ����
const double alpha = M_PI * 15 / 1800; // ���Ķ��壬��λΪ����
const double K = 1852;                // K�ĳ���ֵ
const double D = 120;                 // D�ĳ���ֵ
const double C = sin(M_PI / 3) / (sin(M_PI / 6 + alpha)) + sin(M_PI / 3) / (sin(M_PI / 6 - alpha)); 
const double x = 1 + 0.9 * C * sin(15.0 / 1800 * M_PI);

// �ٽ�ֵ�ļ���
//206.9927�Ǹ������ĺ���㺣ˮ��ȼ���õ������߽��ϵĺ�ˮ���
const double hmax = (206.9927 / sin(M_PI / 6)) * (sin(M_PI * 285 / 1800) / sin(M_PI * 915 / 1800)); // hmax�ļ��㹫ʽ
const double hmin = (2 * 1852 * tan(15.0 / 1800 * M_PI)) + 110 - (1852 * 4 * tan(15.0 / 1800 * M_PI)); // hmin�ļ��㹫ʽ

int main() {
    cout<<"�ϱ�����Ϊ��ѵĲ��߷����串�ǿ�����ȶ�"<<endl;
    double a = hmax; // ��ʼ��aΪhmaxֵ
    const double b = 206.9927 / (1.0 - sin(M_PI / 3) * sin(15.0 / 1800 * M_PI) / sin(M_PI / 6 + 15.0 / 1800 * M_PI)); // b�ļ��㹫ʽ
    double length = 1; // ����������ʼ��Ϊ1������һ����

    // ��b��a֮�����1e-5ʱ����ѭ��
    while (b - a >= 1e-5) {
        // ���ݸ�����������length��ֵ
        while ((a / hmin - pow(x, length)) >= 1e-5) {
            length++;
        }// �����ǰ��ˮ���ֵ�Ͳ���length�����Ͳ����ܳ���
        length=length+1;
        cout << "h: " << a << "    length: " << length <<"  Lsum(/N mile):"<<length*2<<endl;
        a += 0.1; // a����0.1,ģ�⺣ˮ������������ȡ�����п���ֵ
        length = 1; // ����lengthΪ1
    }

    return 0;
}
