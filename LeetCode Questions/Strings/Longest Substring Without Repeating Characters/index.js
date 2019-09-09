function lengthOfLS(s){
    let charMap = {};
    let winStart = 0;
    let maxLen = 0;

    for (let index = 0; index < s.length; index++) {
        const endChar = s[index];

        if (charMap[endChar] >= winStart){
            winStart = charMap[endChar] + 1;
        }   
        charMap[endChar] = index;  
        maxLen = Math.max(maxLen, index - winStart + 1);    
    }

    return maxLen;

}