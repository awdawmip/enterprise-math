"""Exact finite tests on named integer multiplicative shells. Python standard library."""
import argparse
from collections import Counter
from functools import cache
from hashlib import sha256
from itertools import combinations_with_replacement
import json
from math import gcd, prod
from pathlib import Path
import runpy

PRIMES = (2,3,5,7,11,13,17,19,23,29,31,37)


def bits(x):
    while x:
        bit = x & -x
        yield bit.bit_length()-1
        x -= bit


def shell(r,k,t):
    labels = []
    for seq in combinations_with_replacement(PRIMES[:r],k):
        if max(Counter(seq).values()) <= t:
            labels.append(prod(seq))
    return sorted(labels)


def volume(s,k,t):
    coeff = [1]+[0]*k
    for _ in range(s):
        coeff = [sum(coeff[max(0,i-t):i+1]) for i in range(k+1)]
    return coeff[k]


def graph(labels):
    g = [0]*len(labels)
    h = [0]*len(labels)
    for j,y in enumerate(labels):
        for i,x in enumerate(labels[:j]):
            a = gcd(x,y)
            if a > 1:
                h[i] |= 1<<j
                h[j] |= 1<<i
            if x//a in PRIMES and y//a in PRIMES:
                g[i] |= 1<<j
                g[j] |= 1<<i
    return g,h


def exact_power(g,h,k):
    for i in range(len(g)):
        seen = frontier = 1<<i
        for _ in range(k-1):
            following = 0
            for v in bits(frontier):
                following |= g[v]
            frontier = following & ~seen
            seen |= frontier
        assert seen == (h[i] | (1<<i))


def exact_widths(h):
    # Elimination order creates fill edge exactly across a path internal to eliminated vertices.
    n = len(h)
    size = 1<<n
    tw,pw,neighbors = bytearray(size),bytearray(size),[0]*size
    iso = [n]*(n+1)
    iso[0] = 0
    for s in range(1,size):
        bit = s & -s
        neighbors[s] = neighbors[s^bit] | h[bit.bit_length()-1]
        boundary = (neighbors[s] & ~s).bit_count()
        iso[s.bit_count()] = min(iso[s.bit_count()],boundary)
        pw[s] = max(boundary,min(pw[s^(1<<v)] for v in bits(s)))
        tw[s] = n
        for v in bits(s):
            smaller = s ^ (1<<v)
            reached = h[v]
            frontier = reached & smaller
            while frontier:
                following = neighbors[frontier] & ~reached
                reached |= following
                frontier = following & smaller
            degree = (reached & ~s).bit_count()
            tw[s] = min(tw[s],max(tw[smaller],degree))
    return iso,pw[-1],tw[-1]


def bandwidth(g,hamilton):
    # Exact prefix DFS. Each unplaced neighbor has a position deadline.
    n = len(g)
    all_vertices = (1<<n)-1
    for bound in range(n):
        def extend(seq,unused):
            if not unused: return seq
            allowed = unused
            if seq and hamilton: allowed &= g[seq[-1]]
            # Deadlines are nondecreasing along the prefix; Hall's interval capacity is necessary.
            required = 0
            for j,v in enumerate(seq):
                required |= g[v] & unused
                slots = j+bound-len(seq)+1
                if required and required.bit_count() > slots: return None
                if required and required.bit_count() == slots: allowed &= required
            for v in bits(allowed):
                done = extend(seq+[v],unused^(1<<v))
                if done is not None: return done
            return None
        witness = extend([],all_vertices)
        if witness is not None: return bound,witness


def minimum_sum(g,hamilton):
    # Sum of edge lengths equals the sum of the ordinary edge cuts after prefixes.
    n = len(g)
    full = (1<<n)-1
    cuts = [sum((g[i]&~s).bit_count() for i in bits(s)) for s in range(full+1)]
    inf = n**4+1
    @cache
    def val(s,last):
        old = s^(1<<last)
        if not old: return cuts[s]
        prev = old&g[last] if hamilton else old
        return cuts[s]+min((val(old,p) for p in bits(prev)),default=inf)
    s = full
    v = min(bits(s),key=lambda i:val(s,i))
    best = val(s,v)
    order = []
    while True:
        order.append(v)
        s ^= 1<<v
        if not s: break
        candidates = s&g[v] if hamilton else s
        v = min(bits(candidates),key=lambda i:val(s,i))
    return best,order[::-1]


def costs(order,g):
    pos = {v:j for j,v in enumerate(order)}
    lengths = [abs(pos[i]-pos[j]) for i,ns in enumerate(g) for j in bits(ns) if i<j]
    return max(lengths,default=0),sum(lengths)


def theoretical(r,k,t):
    n = volume(r,k,t)
    v = [volume(j,k,t) for j in range(r+1)]
    prof = [0]
    for a in range(1,n+1):
        s = next(s for s in range(r+1) if v[s] >= a)
        prof.append(n-v[r-s]-a)
    return prof


def tree_bags(labels,r):
    # Internal nodes 1..r-2; the three components at internal i contain i,1,r-i-1 labels.
    supports = [{i for i,p in enumerate(PRIMES[:r]) if n%p==0} for n in labels]
    bags = {}
    edges = []
    for i in range(r):
        leaf,stem = f"L{i}",f"I{min(max(1,i),r-2)}"
        bags[leaf] = {j for j,s in enumerate(supports) if i in s}
        edges.append((leaf,stem))
    for i in range(1,r-1):
        parts = [set(range(i)),{i},set(range(i+1,r))]
        bags[f"I{i}"] = {j for j,s in enumerate(supports) if sum(bool(s&p) for p in parts)>=2}
        if i>1: edges.append((f"I{i-1}",f"I{i}"))
    for j in range(len(labels)):
        sub = {b for b,v in bags.items() if j in v}
        assert sub and sum(a in sub and b in sub for a,b in edges)==len(sub)-1
    for j,row in enumerate(labels):
        for i,col in enumerate(labels[:j]):
            if gcd(row,col)>1: assert any(i in v and j in v for v in bags.values())
    return max(map(len,bags.values()))-1


def example(r,k,t,gray):
    nums = shell(r,k,t)
    n = len(nums)
    g,h = graph(nums)
    exact_power(g,h,k)
    # The earlier Gray order is used without changing the original integer vertices.
    previous = [prod(PRIMES[j-1] for j in seq) for seq in gray(r,k)]
    chosen = [x for x in previous if x in set(nums)]
    p = [nums.index(x) for x in chosen]
    if t==k: assert all((g[i]>>j)&1 for i,j in zip(p,p[1:]))
    prof = theoretical(r,k,t)
    prefix = union = 0
    for i,v in enumerate(p,1):
        union |= h[v]
        prefix |= 1<<v
        assert (union&~prefix).bit_count()==prof[i]
    W = max(prof)
    result = dict(r=r,k=k,cap=t,n=n,edges_G=sum(v.bit_count() for v in g)//2,
                  exact_profile=prof,pathwidth_H=W)
    if r>=3:
        tree = tree_bags(nums,r)
        formula = n-volume((r-1)//2,k,t)-volume(r//2,k,t)-1
        if t==k or r>=2*k:
            assert W==formula
            assert tree==W-int(t==k)
        result["caterpillar_width"]=tree
    if n<=15:
        ext,pw,tw = exact_widths(h)
        assert prof==ext and W==pw
        if r>=3 and (t==k or r>=2*k): assert tw==W-int(t==k)
        if r==2 and t==k: assert tw==pw==k-1
        result["subset_DP"]={"states":2**n,"pathwidth":pw,"treewidth":tw}
    if t==k and (n<=10 or (r,k)==(5,2)):
        opts = {}
        for ham in (False,True):
            b,bo = bandwidth(g,ham)
            s,so = minimum_sum(g,ham)
            assert costs(bo,g)[0]==b and costs(so,g)[1]==s
            if ham: assert all(g[i]&(1<<j) for seq in (bo,so) for i,j in zip(seq,seq[1:]))
            opts["Hamilton" if ham else "unrestricted"] = dict(bandwidth=b,total_stretch=s,
                          bw_order=[nums[i] for i in bo],sum_order=[nums[i] for i in so])
        result["optimized_G"]=opts
        result["older_Gray_costs"]=list(costs(p,g))
    return result


def arrange(items, first, last):
    if len(items)==1:
        assert first==last==items[0]
        return items
    assert first!=last and first in items and last in items
    return [first] + [x for x in items if x not in (first,last)] + [last]


def internal(count, splice=False):
    # Pairs use one-based local labels, and are put in increasing maximum blocks.
    words=[]
    for i in range(1,count+1):
        items=[(j,i) for j in range(1,i+1)]
        first=max(1,i-1)
        last=i
        if splice and i==count-1: last=1
        if splice and i==count: first,last=1,count-1
        words.extend(arrange(items,(first,i),(last,i)))
    return words


def hamilton_optimum(r):
    # For r=5,6 finite witnesses are also given as actual integer semiprimes in the paper.
    if r<7:
        witnesses={2:[4,6,9],3:[4,6,9,15,10,25],4:[4,6,9,15,10,14,21,49,35,25],
                   5:[4,6,9,15,10,14,21,33,22,55,25,35,49,77,121],
                   6:[4,6,9,15,10,25,35,14,21,33,22,26,39,65,55,77,49,91,169,143,121]}
        by_integer={x*y:(i+1,j+1) for i,x in enumerate(PRIMES[:r])
                     for j,y in enumerate(PRIMES[:r]) if i<=j}
        return [by_integer[z] for z in witnesses[r]]
    a,b=(r+1)//2,r//2
    low,high=[],[]
    for t in range(b):
        x,y=a-t,b-t
        # The column comes after allocating a whole row, hence it may be empty.
        length=x-1
        if length:
            col=[(j,a+y) for j in range(1,length+1)]
            low.extend(arrange(col,(length,a+y),(max(1,length-1),a+y)))
        row=[(x,a+j) for j in range(1,y+1)]
        high.append(arrange(row,(x,a+max(1,y-1)),(x,a+y)))
    tail=[(a+i,a+j) for i,j in reversed(internal(b))]
    return internal(a,True)+low+[pair for block in reversed(high) for pair in block]+tail


def construction_certificate(r):
    word=hamilton_optimum(r)
    assert len(set(word))==len(word)==r*(r+1)//2
    assert all(1<=i<=j<=r for i,j in word)
    assert all(set(p)&set(q) for p,q in zip(word,word[1:]))
    first,last={},{}
    for j,pair in enumerate(word):
        for i in pair:
            first.setdefault(i,j)
            last[i]=j
    bw=max(last[i]-first[i] for i in first)
    W=r*(r+1)//2-((r-1)//2)*(((r-1)//2)+1)//2-(r//2)*((r//2)+1)//2-1
    assert bw==W+int(r in (3,4))
    return bw


def hamilton_histogram(r):
    v=shell(r,2,2)
    g,_=graph(v)
    total=Counter()
    def extend(w,unused):
        if not unused:
            total[costs(w,g)[0]]+=1
            return
        allowed=unused&g[w[-1]] if w else unused
        for z in bits(allowed): extend(w+[z],unused^(1<<z))
    extend([],(1<<len(g))-1)
    return dict(sorted(total.items()))


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--previous",type=Path,default=Path(__file__).resolve().parents[1]/"nineteenth"/"adjacency_check.py")
    parser.add_argument("--out",type=Path)
    args=parser.parse_args()
    digest = sha256(args.previous.read_bytes()).hexdigest()
    assert digest == "f6da76cc32e1f2e9140f013551e3a1ccb68579c551d2c46c263ff7098c5ad428"
    gray = runpy.run_path(str(args.previous))["gray"]
    checks = [(2,2,2),(2,4,4),(3,2,2),(4,2,2),(5,2,2),(3,3,3),(4,3,3),
              (5,3,3),(6,4,4),(8,3,3),(4,2,1),(5,2,1),(6,2,1),
              (5,3,1),(6,3,1),(6,3,2),(8,4,3)]
    sequences={r:construction_certificate(r) for r in range(2,101)}
    hist={r:hamilton_histogram(r) for r in (3,4)}
    assert [min(hist[r]) for r in (3,4)]==[4,6]
    result = dict(old_Gray_sha256=digest,examples=[example(*s,gray) for s in checks],
                  exact_Hamilton_bandwidth_2_to_100=sequences,all_Hamilton_histograms=hist)
    text=json.dumps(result,indent=2,sort_keys=True)+"\n"
    if args.out: args.out.write_text(text)
    else: print(text,end="")


if __name__=="__main__":
    main()
