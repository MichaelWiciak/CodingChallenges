Approach 1: Convert the list into a set and then back into a list
	Example Code:
		```uniqueNums = list(set(nums))
        k = len(uniqueNums)
        nums[:k] = uniqueNums
        return k
        ```
	Problem:
		The code fails for some cases such as [-1, 0, 0, 0, 0, 3, 3].
		This is because sets do not preserve the order of elements, so the order of the unique elements might not be the same as the original order.

Approach 2: Convert into an Ordered Dictionary and convert the keys back into the list
	Example Code:
		```uniqueNumsDict = OrderedDict.fromkeys(nums)
        uniqueNumsList = list(uniqueNumsDict.keys())
        k = len(uniqueNumsList)
        nums[:k] = uniqueNumsList
        return k```
	Works :)
	Time Taken
		![[Pasted image 20231003152859.png]]
	Space Taken
		![[Pasted image 20231003152933.png]]
	Remark
		It seems that the amount of time taken and space taken changes drastically with each execution as such this isn't too accurate. 