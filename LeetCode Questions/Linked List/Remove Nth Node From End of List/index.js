var removeNthFromEnd = function(head, n) {
    //used to check if the linked list is only one or null 
    let tempHead = {next: head};
    let slow = tempHead;
    let fast = tempHead;

    //move fast N nodes ahead of slow

    for (let i = 0; i <= n; i++) {
        fast = fastn.next;
    }
    //Move slow and fast one node at a time until fast is last node

    while(fast.next){
        slow = slow.next;
        fast = fast.next;
    }
    //slow now points to two nodes ahead of it
    slow.next = slow.next.next;

    return tempHead.next;
};