nums = [2,7,11,15]
target = 9
a=nums[0]
#print(a)

for i in range(len(nums)):
    for j in range(1+i,len(nums)):
        if(nums[i] + nums[j] == target):
            print (i,j)
