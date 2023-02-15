/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
 var findMedianSortedArrays = function(nums1, nums2) {
    const mergedArray = [];
    const length = nums1.length + nums2.length;
    let pointer1 = 0
    let pointer2 = 0;

    while (mergedArray.length <= length/2) {
        if (nums1[pointer1] <= nums2[pointer2] || nums2[pointer2] === undefined) {
            mergedArray.push(nums1[pointer1]);
            pointer1++;
        } else {
            mergedArray.push(nums2[pointer2]);
            pointer2++;
        }
    }

    if (!!(length % 2)) return mergedArray[mergedArray.length-1];
    return (mergedArray[mergedArray.length-1] + mergedArray[mergedArray.length-2]) / 2;
};