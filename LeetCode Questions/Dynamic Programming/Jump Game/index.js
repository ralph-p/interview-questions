
function canJump(nums){
    let dpPos = new Array(nums.length).fill(false);
    dpPos[0] = true;
    for (let j = 0; j < nums.length; j++) {
        for (let i = 0; i < j; i++) {
            if (dpPos[i] && i + nums[i] >= j) {
                dpPos[j] = true;
                break;
            }           
        }
    }
    return dpPos[dpPos.length - 1];
}