"""Independent phase-state BFS verification for the R284FD finite obstruction."""
from collections import deque
from itertools import permutations


def bfs_codes(words, n):
    seen={(0,words[0])}
    queue=deque(seen)
    while queue:
        phase,x=queue.popleft()
        j=(phase+1)&3
        delta=words[phase]^words[j]
        for omit in [-1]+[bit for bit in range(n) if (delta>>bit)&1]:
            z=x
            for k in range(n):
                if (delta>>k)&1 and k!=omit:
                    z=(z&~(1<<k))|(words[j]&(1<<k))
            v=(j,z)
            if v not in seen:
                seen.add(v)
                queue.append(v)
    cols=[set() for _ in range(4)]
    for i,x in seen:
        cols[i].add(x)
    return cols


def main():
    mi=999
    ok=0
    cases=0
    for a,b,c in permutations(range(1,32),3):
        ee=bfs_codes((0,a,b,c),5)
        collisions=sum(len(ee[i]&ee[j])
                       for i in range(4) for j in range(i+1,4))
        cases+=1
        ok += (collisions==0)
        mi=min(mi,collisions)
    sizes=list(map(len,bfs_codes((0,7,63,56),6)))
    assert (cases,ok,mi,sizes)==(26970,0,4,[16,16,16,16])
    print({'cases':cases,'disjoint':ok,'min_collision':mi,
           'six_bit_sizes':sizes})


if __name__=="__main__":
    main()
