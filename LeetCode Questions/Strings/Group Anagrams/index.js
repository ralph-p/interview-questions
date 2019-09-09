
function groupAnagrams(s){
    let grouped = {}

    for (let i = 0; i < s.length; i++) {
        const word = s[i];

        const key = word.split('').sort().join('');

        if (!grouped[key]){
            grouped[key] = [];
        }

        grouped[key].push(word);
        
    }
    // This will give us an array of objects, since each object is an array, this will return an array of arrays
    return Object.values(grouped);
}