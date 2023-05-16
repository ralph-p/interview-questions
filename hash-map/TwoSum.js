/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
// Input: nums = [2,7,11,15], target = 9
// Output: [0,1]
// Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
var twoSum1 = function (nums, target) {
  for (let i = 0; i < nums.length - 1; i++) {
    const num1 = nums[i];
    for (let j = i + 1; j < nums.length; j++) {
      const num2 = nums[j];
      if ((num1 + num2) === target) return [i, j]
    }
  }

};
var twoSum2 = function (nums, target) {
  /*
      We use a hashmap to keep track of the differences between the target and each number in the array 
      e.g. nums = [2,7,11,15], target = 17

      i = 0
        numMap = {}

        diff = 17 - 2 = 15
        numMap[15] does not exist, if check failed 
        numMap = {2: 0}

      i = 1
        numMap = {2: 0}

        diff = 17 - 7 = 10
        numMap[10] does not exist, if check failed 
        numMap = {2: 0, 7: 1}
        
      i = 2
        numMap = {2: 0, 7: 1}

        diff = 17 - 11 = 6
        numMap[6] does not exist, if check failed 
        numMap = {2: 0, 7: 1, 11: 2}
        
        i = 3
        numMap = {2: 0, 7: 1, 11: 2}

        diff = 17 - 15 = 2
        numMap[2] does exist, return [value of numMap at 2, index]
        
  */
      const numMap = {}
      for (var i = 0; i < nums.length; i++) {
        const diff = target - nums[i]
        if (numMap[diff] >= 0) return [numMap[diff], i]
        numMap[nums[i]] = i
      }

};