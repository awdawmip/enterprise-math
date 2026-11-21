"""Given the archived exhaustive inventory of 250 size-13 classes, exclude six within any 11-label partition."""
from collections import Counter
from itertools import permutations, product
import json
from cyclic11 import P,index,observations,setbits


def is_legal(s, bad):
    for i in setbits(s):
        for j in setbits(s & ~((1<<(i+1))-1)):
            if s&bad[i][j]:
                return False
    return True


def enumerate_classes(space, minimum, bad):
    result=[]
    def visit(chosen, size, candidates, forb):
        if size + candidates.bit_count() < minimum:
            return
        # Each greedily built group is a clique of pair incompatibilities
        # in the current chosen set, so an extension takes at most one per group.
        remaining=candidates
        order=[]
        bound=0
        while remaining:
            bound+=1
            clique=remaining
            while clique:
                bit=clique&-clique
                v=bit.bit_length()-1
                order.append((v,bound))
                remaining^=bit
                clique &= remaining & forb[v]
        for v,upper in reversed(order):
            if size+upper<minimum:
                return
            b=1<<v
            candidates ^= b
            nxt=candidates & ~forb[v]
            if size+1>=minimum:
                result.append(chosen|b)
            if size+1+nxt.bit_count()>=minimum:
                visit(chosen|b,size+1,nxt,{j:forb[j]|bad[v][j] for j in setbits(nxt)})
    visit(0,0,space,{i:0 for i in setbits(space)})
    return result


def count_completions(residual, bad):
    # Rows of size at least eight suffice in the actual nonterminal search.
    pool=sorted(enumerate_classes(residual,8,bad),key=lambda s:(-s.bit_count(),s))
    nodes=0
    covers=0
    minimum_threshold=125
    def visit(free, left, available, previous):
        nonlocal nodes,covers,minimum_threshold
        nodes+=1
        n=free.bit_count()
        if n<left:
            return
        if left==1:
            if (-n,free)>(-previous.bit_count(),previous) and is_legal(free,bad):
                covers+=1
            return
        threshold=(n+left-1)//left
        minimum_threshold=min(minimum_threshold,threshold)
        if threshold<8:
            # Never reached on the eleven residues. Explicitly fail if the
            # pre-enumerated catalogue would be too narrow for a nonterminal node.
            raise ValueError((free,left,threshold))
        for i,s in enumerate(available):
            if s.bit_count()<threshold:
                break
            visit(free^s,left-1,[t for t in available[i+1:] if not t&s],s)
    visit(residual,5,pool,0)
    return dict(nodes=nodes,covers=covers,smallest_next_size_bound=minimum_threshold,
                largest_row=max(s.bit_count()for s in pool))


def run():
    bad,_=observations()
    A={0}
    for u,v in product((1,-1),repeat=2):
        A.update([index((0,2*u%5,v%5)),index((u%5,0,2*v%5)),index((2*u%5,v%5,0))])
    base=sum(1<<i for i in A)
    transforms=set()
    for per in permutations(range(3)):
        for k in (1,2):
            for sg in product((-1,1),repeat=3):
                transforms.add(tuple(index(tuple(k*sg[j]*p[per[j]]%5 for j in range(3))) for p in P))
    orientations={tuple(sorted(t[i] for i in A))for t in transforms}
    all13=set()
    for shift in P:
        for row in orientations:
            all13.add(sum(1<<index(tuple((u+v)%5 for u,v in zip(P[i],shift)))for i in row))
    assert len(all13)==250 and all(is_legal(s,bad)for s in all13)
    # Orbit has the same size as the prior exhaustive all-class count.
    stabilizer=[t for t in transforms if {t[i]for i in A}==A]
    maps=[{s:sum(1<<t[i]for i in setbits(s))for s in all13}for t in stabilizer]
    hits=[]
    def packs(chosen,candidates):
        if len(chosen)==6:
            hits.append(tuple(sorted(chosen)))
            return
        for i,s in enumerate(candidates):
            packs(chosen+[s],[t for t in candidates[i+1:] if not s&t])
    packs([base],[s for s in sorted(all13) if not s&base])
    seen=set()
    reps=[]
    for p in hits:
        if p in seen:
            continue
        seen.update(tuple(sorted(m[s]for s in p)) for m in maps)
        reps.append(p)
    checks=[]
    for p in reps:
        r=(1<<125)-1
        for s in p:
            r^=s
        check=count_completions(r,bad)
        checks.append(check)
    assert not any(t['covers']for t in checks)
    return dict(size13_orbit=len(all13),linear_stabilizer_used=len(stabilizer),
                packings_through_base=len(hits),representatives=len(reps),
                full_partitions=sum(t['covers']for t in checks),total_nodes=sum(t['nodes']for t in checks),
                checks=checks)
if __name__=='__main__':
    print(json.dumps(run(),indent=2))
