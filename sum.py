class Solution:
    def __init__(self,lyst,target):
        self.nums=lyst
        self.target=target
        print(lyst)


    def twoSum(self):
        numsLen = len(self.nums)
        answerList = []
        print(numsLen)
        for i in  range(numsLen):
            isFind = False
            for j in range(i+1,numsLen):
                if j == i:
                    continue
                if self.nums[i] + self.nums[j] == self.target:
                    answerList.append(i)
                    answerList.append(j)
                    isFind = True
                    break
            if isFind == True:
                break
        return answerList

list1=[1,7,8,56,4,4,2,1,5]
a= Solution(list1,58).twoSum()
print(a)