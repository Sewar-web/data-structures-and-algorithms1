# Challenge Summary
write a business_trip function that take graph of trip and arr of city name and return cost of trip and true or false
## Whiteboard Process
![img](code37.png)

## Approach & Efficiency
o(n^2)

## Solution

```
    def business_trip(graph,Cname):
        cost=0
        flag=False

        for cn in range(len(Cname)-1):
            edge=graph.get_neighbors(Cname[cn])
            for e in edge:
                if Cname[cn+1]==e.node:
                    cost+=e.weight
                    flag=True
        
        if flag==False:
            cost=0
            flag=False
            return f'{flag},${cost}'


        return f'{flag},${cost}'

```
