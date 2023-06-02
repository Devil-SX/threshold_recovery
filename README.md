对音频信号进行门限判决，将阈值化后的数字信号恢复成模拟信号

# 问题分析

## 阈值化

会加强高频分量和低频分量

## 算法要求
1. （判决数学约束1）恢复后信号再次判决得到数组不变
2. （判决数学约束2）判决序列边界点恢复后为判决阈值
3. （幅度约束1）能恢复信号幅度平均值
4. （幅度约束2）能恢复信号幅度的变化
5. 信号连续
6. 能够恢复出主频率和叠加的子频率（子频率至少一个）


## 恢复率评价
- $e_{threshold} = ||f_t-f_0||_2$
- $e_{recover} = ||f_r-f_0||_2$
- $recover\_rate = \frac{e_{threshold}-e_{recover}}{e_{threshold}}*100\%$

## 算法迭代
- 插值算法-三角函数恢复法（满足要求：2,3）
- 插值算法-二次函数恢复法（满足要求：1,2,5）不能恢复，没有满足条件4
