This is a simple problem
Can't you just for loop through the list and write that element into another list of the same size with its index + k but if index + k > len(list) then minus it. 

Approach 1: Create a second list
	Example Code:
		```if (len(nums)) == 1 or len(nums)==k:
            return
        while k>len(nums):
            k=k-len(nums)
        newIndex = -1
        aList = []
        for i in range(len(nums)):
            aList.append(-1)
        for i in range(len(nums)):
            newIndex = k+i
            if newIndex > len(nums)-1:
                newIndex-= len(nums)
            aList[newIndex] = nums[i]
	    nums[:] = aList[:]```
	Time:
		![[Pasted image 20231005143814.png]]
	Space:
		![[Pasted image 20231005143836.png]]
	Remark:
		This is a pretty long approach but it deals with a few test cases to speed up the algorithm. 
		
Approach 2: inverse the list
	Example Code:
		```n=len(nums) 
		k%=n 
		nums[:]=nums[-k:]+nums[:-k]```
	Time:
		![[Pasted image 20231005144653.png]]
	Space:
		![[Pasted image 20231005144707.png]]
	Remark:
		This approach works by splitting the list and inversing it. 