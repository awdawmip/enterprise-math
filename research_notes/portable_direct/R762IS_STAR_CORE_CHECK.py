"""R762IS: exact finite 6-star x 10-deletion core certificate (Python 3)."""
from itertools import combinations

PORTS=list(combinations(range(6),2))
SUPPORTS=list(combinations(range(6),3))
ix={p:i for i,p in enumerate(PORTS)}
TRIS=[tuple(ix[p] for p in combinations(s,2)) for s in SUPPORTS]
EXPECTED=[1023,64527,466033,746898,895652,971592]

def partition(tris):
    parent=list(range(15))
    def root(i):
        while parent[i]!=i:
            parent[i]=parent[parent[i]]
            i=parent[i]
        return i
    for t in tris:
        x,y,z=t
        parent[root(x)]=root(y)
        parent[root(y)]=root(z)
    return [root(x) for x in range(15)]

def main():
    tests=0
    for a in range(6):
        star=[s for s,t in enumerate(SUPPORTS) if a in t]
        assert len(star)==10
        assert sum(1<<s for s in star)==EXPECTED[a]
        for j in star:
            leaf=ix[tuple(x for x in SUPPORTS[j] if x!=a)]
            labels=partition(TRIS[s] for s in star if s!=j)
            others=[x for x in range(15) if x!=leaf]
            assert len({labels[x] for x in others})==1
            assert labels[leaf] not in {labels[x] for x in others}
            tests+=1
    assert tests==60
    print("PASS R762IS: six axis stars and 60 one-leaf deletions")
if __name__ == "__main__":
    main()
