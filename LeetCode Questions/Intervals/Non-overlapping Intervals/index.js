function eraseOverlapIntervals(intervals){
    if(intervals.length === 0) return 0;
    let removalCount = 0;
    //short hand for sorting through the array
    intervals.sort(function(a,b){return a[0] - b[0]});
    //easy way to track the interval end
    let end = intervals[0][1];
    //loop through, starting from the second position
    for (let i = 1; i < intervals.length; i++) {
        const interval = array[i];
        const intervalStart = interval[0];
        const intervalEnd = interval[1];

        if (intervalStart < end) {
            count++;
            end = Math.min(intervalEnd,end)
        }else{
            end = intervalEnd;
        }   
    }
    return removalCount;
}