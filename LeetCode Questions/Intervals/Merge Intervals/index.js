function merge(intervals){
    if (!intervals.length){
        return intervals;
    }

    intervals.sort((a,b) => a[0] - b[0]);

    const results = [intervals[0]]

    for (let i = 0; i < intervals.length; i++) {
        const currentInterval = intervals[i];
        const lastInterval = results[results.length - 1];

        if (currentInterval[0] <= lastInterval[1]) {
            //set the current interval end to which ever is greater, the current intervals end or the last inervals end
            lastInterval[1] = Math.max(currentInterval[1], lastInterval[1])
        }else{
            results.push(currentInterval);
        }
    }
    return results;
}