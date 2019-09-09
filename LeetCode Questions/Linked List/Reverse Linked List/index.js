var reverseList = function(head) {
    let Prev = null;
    let current = head;

    while(current){
        let temp = current.next;
        //change direction
        current.next = Prev;
        //move them both up by one
        Prev = current;
        current = temp.next;
    }

    return Prev;
};