from linked_list.linked_list import Node, LinkedList


def zipLists(ll1, ll2):
    current1 = ll1.head
    current2 = ll2.head

    if current1 == None or current2 == None:
        if current1:
            return ll1.__str__()
        elif current2:
            return ll2.__str__()
        else:
         return "Both of the linked list is empty"

    valuelist = []
    while current1 or current2:
        if(current1):
            valuelist+=[current1.value]
            current1 = current1.next
        if(current2):
            valuelist+=[current2.value]
            current2 = current2.next
    x=''
    for i in valuelist:
      x+=f'( {i} ) -> '
    x+='None'
    return x



if __name__ == "__main__":
    ll1 = LinkedList()
    ll1.append(1)
    ll1.append(3)
    ll1.append(5)
    ll2 = LinkedList()
    ll2.append(2)
    ll2.append(4)
    ll2.append(6)
    print(ll1.__str__())
    print(ll2.__str__())
    print(zipLists(ll1, ll2))