
function canAttendMeetings(intervals){
    const sArray = [];
    const eArray = [];
    //fill up the starts and ends array
    for (let i = 0; i < intervals.length; i++) {
        const subArray = intervals[i];
        sArray.push(subArray[0])
        eArray.push(subArray[1])
    }
    sArray.sort((a,b) => a - b);
    eArray.sort((a,b) => a - b);
    for (let i = 0; i < sArray.length; i++) {
        if (sArray[i + 1] < eArray[i]){
            return false;
        }
    }
    return true;
}