import numpy as np


def infoCalculation(num):
    total = 0
    for i in num:
        total += i
    result = 0
    for i in num:
        if i == 0:
            return 0
        temp = i/total
        result -= temp * np.log2(temp)
    return result


def baseInfo(df, determineAttribute):
    keys = df[determineAttribute].unique()  # last column unique value
    numOfData = len(df)
    nums = list()
    for value in keys:
        nums.append(len(df[df[determineAttribute] == value]))
    return infoCalculation(nums)


def info(df, attribute, determineAttribute):
    numOfData = len(df)
    info = 0
    keys = df[attribute].unique()  # unique value
    for value in keys:
        occurrence = len(df[df[attribute] == value])
        probOfOccur = occurrence/numOfData
        info += probOfOccur * baseInfo(df[df[attribute] == value], determineAttribute)
    return info