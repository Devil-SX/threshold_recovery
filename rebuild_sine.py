import numpy as np
import matplotlib.pyplot as plt


def rebuild_sine(arr, value=1):
    """
    输入一个数组，判断数组是否全为0或全为1，如果是则返回全为0的数组，否则返回模拟重建。
    """
    is_all_zero = all(elem == 0 for elem in arr)  # 判断是否全为0
    is_all_one = all(elem == 1 for elem in arr)  # 判断是否全为1

    if is_all_zero or is_all_one:
        # 如果全为0或全为1，则返回全为0的数组
        # return [0 for _ in arr]
        return arr
    else:
        # 否则返回原数组
        diff_arr = np.diff(arr)
        index = np.where(diff_arr == -1)[0][0]
        index = index + 1
        # print(index)
        T = len(arr)
        # print(T)
        t = np.arange(0, T)
        A = value / np.cos(np.pi * index / T)
        # print(A)
        if np.abs(A) >= 2**15:
            A = (2**15 - 1) * np.sign(A)
        anology = A * np.cos(2 * np.pi * (t + index / 2) / T)
        return anology


if __name__ == "__main__":
    plt.plot(rebuild([1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0]))
    plt.plot(rebuild([0, 0, 0, 0]))
    plt.plot(rebuild([1, 1, 0]))
