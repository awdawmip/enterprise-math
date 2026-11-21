"""Classify unordered pairs of maximal parents under the native cost isometries."""
from itertools import permutations,product

def build(parents,centers):
    coords=list(product(range(5),repeat=3))
    def encode(a):
        x,y,z=a
        return 25*(x%5)+5*(y%5)+(z%5)
    # Every map taking a specified parent to parent 0 must send its unique center to center 0.
    linear=[[tuple(k*v*x[j] for j,v in zip(p,sign))for x in coords]
             for p,sign,k in product(permutations(range(3)),product((1,-1),repeat=3),(1,2))]
    lookup={p:i for i,p in enumerate(parents)}
    sets=[[j for j in range(125)if p>>j&1]for p in parents]
    base=sets[0];cx=coords[centers[0]]
    def to_base(i):
        maps=[]
        for act in linear:
            shift=[cx[j]-act[centers[i]][j]for j in range(3)]
            def image(j):
                u=act[j]
                return encode((u[0]+shift[0],u[1]+shift[1],u[2]+shift[2]))
            if sum(1<<image(j) for j in sets[i])==parents[0]:
                maps.append([image(j) for j in range(125)])
        assert len(maps)==48
        return maps
    def key(pts,maps):
        return min(lookup[sum(1<<a[j]for j in pts)]for a in maps)
    fix=to_base(0)
    rank={i:min(key(sets[i],fix),key(base,to_base(i)))for i in range(1,250)}
    labels=sorted(set(rank.values()))
    assert len(labels)==12
    return [(j,[k for k in range(1,250)if rank[k]>=j])for j in labels]
