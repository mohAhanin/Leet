nums = [1,2,2,1]
k = 1
temp = []
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if(abs(nums[i]-nums[j])==k):
            temp.append([i,j])
            print(i, j)
print(len(temp))
        
            