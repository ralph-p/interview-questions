

function isValid(s){
    let stack = [];
    let pairsMap = {"(" :")","[" :"]","{" :"}",};

    for (let i = 0; i < s.length; i++) {
        const char = s[i];

        if (pairsMap[char]){
            stack.push(char);
        } else if (pairsMap[stack.pop()] !== char) {
            return false;
        }
    }

    return stack.length === 0;
}