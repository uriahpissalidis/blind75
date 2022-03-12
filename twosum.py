# Two-sum 
# https://leetcode.com/problems/two-sum/

class Solution:
	def twoSum(self, nums: List[int], target: int) -> List[int]:
		seen = {}
    	for i, value in enumerate(nums): #1
        	remaining = target - nums[i] #2
           
       		if remaining in seen: #3
            	return [i, seen[remaining]]  #4
        	else:
                seen[value] = i  #5

#1 lets you go through the array using enumerate which gives you
#both index and value of the elements in the array.

#eg nums = [2,3,1], let's say the index at i=0 and value=2
#so we need value 1, target - 2 = 1. 1 here is remaining.

#since remaining + value = target, you're done.
#So when going through the array, you calculate the remaining and
#check to see whether remaining is in the seen dictionary (#3)
#if yes, you're done

#current number and remaining from seen would give you the 
#output (#4)

#Otherwise, you add your current number to the dictionary (#5),
#since it is going to be a remaining for (probably) a number,
#you'll see in the future assuming that there is at least one
#instance of an answer