import bisect
class MyList(list):
    def __init__(self):
        self.prefixSums=[]
        self.prefixSum=0
    def Fx(self,prefixSum,index,cap):
        size = len(prefixSum)
        if 0==index:
            return (cap * size - prefixSum[-1])
        return (cap * size - prefixSum[-1]) - ( cap*(index) - prefixSum[index-1] )
    def append(self,x):
        super().append(x)
        self.prefixSum+=x
        self.prefixSums.append(self.prefixSum)
    def __getitem__(self,i):
        k=(len(self.prefixSums)-1)-i
        return self.Fx(self.prefixSums,k,super().__getitem__(-1))

class Solution(object):
    def maxFrequency(self, nums, k):
        nums.sort()
        diff=MyList()
        count = 0
        countMax = 0
        for i, n in enumerate(nums):
            diff.append(n)
            count = bisect.bisect_right(diff, k)
            if count > countMax:
                countMax = count
        return countMax

# ##############################################
myList = MyList()
myList.append(1)
myList.append(4)
myList.append(8)
myList.append(13)
assert  0 == myList[0]
assert  5 == myList[1]
assert 14 == myList[2]
assert 26 == myList[3]

assert 1==(bisect.bisect_right(myList,0))
assert 1==(bisect.bisect_right(myList,2))
assert 2==(bisect.bisect_right(myList,5))
assert 2==(bisect.bisect_right(myList,6))
assert 4==(bisect.bisect_right(myList,26))
# ##############################################
sln=Solution()
assert 3==sln.maxFrequency(nums = [1,2,4], k = 5)
assert 2==sln.maxFrequency(nums = [1,4,8,13], k = 5)
assert 1==sln.maxFrequency(nums = [3,9,6], k = 2)
# # ##############################################
