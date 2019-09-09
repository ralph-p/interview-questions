var mergeTwoLists = function(l1, l2) {
    const tempHead = {next: null};
    let tail = tempHead;

    while(l1 && l2){
        if (l1.val < l2.val){
            tail.next = l1
            tail = tail.next;
            l1 = l1.next;
        } else{
            tail.next = l2;
            l2 = l2.next;
            tail = tail.next;
        }
    }
    tail.next = l1 || l2;

    return tempHead.next;
};