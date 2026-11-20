"""Exact stabilizer and native legality of the eleven-label incumbent."""
from collections import Counter
from itertools import combinations


def verify(older, linear, translations, bad, pair, class_cost):
    labels=list(map(int,(older/'native/eleven.txt').read_text().split()))
    assert len(labels)==125 and set(labels)==set(range(11))
    partition=[tuple(i for i in range(125) if labels[i]==j) for j in range(11)]
    assert all(not (bad[a][b]>>c&1) for row in partition for a,b,c in combinations(row,3))
    costs=[class_cost(row,pair) for row in partition]
    assert sum(costs)==11292
    by_points={frozenset(row):i for i,row in enumerate(partition)}
    orders=Counter();observed=None
    for a in linear:
        for t in translations:
            g=bytes(t[i] for i in a)
            lifted=[by_points.get(frozenset(g[p] for p in row),-1) for row in partition]
            if -1 in lifted:
                continue
            u=g;order=1
            while u!=bytes(range(125)):
                u=bytes(g[p]for p in u);order+=1
            orders[order]+=1
            if [g[i] for i in (0,25,5,1)]==[0,4,100,5]:
                assert order==3
                observed=lifted
    assert orders=={1:1,2:1,3:2,6:2}
    assert observed==[0,1,2,3,4,7,8,9,10,5,6]
    return {'cost':sum(costs),'class_costs':costs,'stabilizer_by_order':dict(sorted(orders.items())),
            'order_three_label_map':observed,'order_three_point_map':'(-y,z,-x)'}
