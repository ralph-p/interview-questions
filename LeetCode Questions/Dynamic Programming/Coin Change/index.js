function coinChange(coins, amount){
    let dpMinCoins = new Array(amount + 1).fill(Infinity);
    dpMinCoins[0] = 0;

    for (let i = 1; i < dpMinCoins.length; i++) {
        for (let c = 0; c < coins.length; c++){
            const cValue = coins[c];
            if (cValue <= i){
                dpMinCoins[i] = Math.min(dpMinCoins[i - cValue] + 1, dpMinCoins[i]);
            }
        }
    }
    const ans = dpMinCoins[dpMinCoins.length - 1];
    //if it's not possible to reach the last element return -1
    return ans === Infinity ? -1 : ans;
}