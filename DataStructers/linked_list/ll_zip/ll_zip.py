from linked_list.linked_list import LinkedList

def ll_zip(ll1, ll2):
    current = ll1.head
    current1 = ll2.head
    ll = LinkedList()
    while True:
        if current != None: 
            ll.append(current.value)
            current = current.next 
        if current1 != None:
            ll.append(current1.value)
            current1 = current1.next

        if current == None and current1 == None:
            break

    return ll.head.value

if __name__ == "__main__":
    ll1=LinkedList()
    ll1.append(1)
    ll1.append(2)
    ll2=LinkedList()
    ll2.append(3)
    ll2.append(4)
    print(ll_zip(ll1,ll2))
