import matplotlib.pyplot as plt
import numpy as np


def compareFragments(array1, array2, startArray, fragLength):
    # array1: 第一个数组
    # array2: 第二个数组
    # startArray: 起始数组
    # fragLength: 片段长度

    for i in range(len(startArray)):
        startIndex = startArray[i]
        endIndex = startIndex + fragLength

        plt.subplot(len(startArray), 3, 3 * i + 1)
        plt.plot(np.arange(startIndex, endIndex), array1[startIndex:endIndex], "r-")
        # plt.xlim(startIndex, endIndex - 1)
        # plt.axis("square")
        plt.gca().set_aspect("auto")

        plt.subplot(len(startArray), 3, 3 * i + 2)
        plt.plot(np.arange(startIndex, endIndex), array2[startIndex:endIndex], "b-")
        # plt.xlim(startIndex, endIndex - 1)
        # plt.axis("square")
        plt.gca().set_aspect("auto")

        plt.subplot(len(startArray), 3, 3 * i + 3)
        plt.plot(np.arange(startIndex, endIndex), array1[startIndex:endIndex], "r-")
        plt.plot(np.arange(startIndex, endIndex), array2[startIndex:endIndex], "b-")
        # plt.xlim(startIndex, endIndex - 1)
        # plt.axis("square")
        plt.gca().set_aspect("auto")

    plt.show()


# 测试
if __name__ == "__main__":
    array1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    array2 = [1, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    startArray = [1, 3, 6]
    fragLength = 3
    compareFragments(array1, array2, startArray, fragLength)
