var hasCycle = function(head) {
    let slow = head;
    let fast = head;

    while( fast && fast.next){
        slow = slow.next;
        fast = fast.next.next;

        if (slow === fast){
            return true;
        }
    }
    //if the while loop reaches an end it's not a circular linked list
    return false;
};