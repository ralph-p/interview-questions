function isPalindrome(s) {
    //sanitize the string
    s = s.toLowerCase().replace(/[\W_]/g,"");
    let leftPointer = 0;
    let rightPointer = s.length - 1;

    while (leftPointer < rightPointer) {
        if (s[leftPointer] !== s[rightPointer]){
            return false;
        }
    leftPointer ++;
    rightPointer --;
    }


    return true;
}