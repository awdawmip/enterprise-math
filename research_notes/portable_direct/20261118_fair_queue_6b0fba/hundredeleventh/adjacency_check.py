"""Exact finite certificates for semiprime prefix Hamilton paths and their costs."""
from collections import Counter
from itertools import combinations, permutations
from math import factorial, prod
import json


def triangular(r):
    return r*(r+1)//2


def primes(n):
    values=[]
    x=2
    while len(values)<n:
        if all(x%p for p in values if p*p<=x):
            values.append(x)
        x+=1
    return values


def graph(r):
    from math import gcd
    ps = primes(r)
    blocks = [[p*q for p in ps[:j+1]] for j,q in enumerate(ps)]
    vertices = sum(blocks,[])
    edges = [(a,b) for a,b in combinations(vertices,2) if gcd(a,b)>1]
    return blocks, vertices, edges


def cost_stats(path,edges):
    pos = {v:j for j,v in enumerate(path)}
    lengths=[abs(pos[v]-pos[w]) for v,w in edges]
    return max(lengths), sum(lengths)


def path_generator(blocks):
    from math import gcd
    def visit(j,path):
        if j==len(blocks):
            yield path
            return
        for perm in permutations(blocks[j]):
            if gcd(perm[0],path[-1])>1:
                yield from visit(j+1,path+perm)
    yield from visit(1,(blocks[0][0],))


def native_path(blocks):
    path=blocks[0][:]
    for j,b in enumerate(blocks[1:],2):
        path.extend([b[j-2]]+b[:j-2]+[b[j-1]])
    return path


def last_cost(r):
    return r*(r-1)*(r+1)*(r+2)*(3*r-1)//60


def improvement(r):
    if r%2==0:
        m=r//2
        return (m-2)*(m-1)*(2*m-3)//6
    m=r//2
    return m*(m-2)*(m-1)//3


def optimal_count(r):
    base=prod(factorial(j-2) for j in range(2,r+1))
    return base * 2**max(0,r//2-2)*((r-2) if r%2 else 1)


def prefix_optimal_path(r, want_minimax):
    # Predecessor's largest prime always survives in the terminal vertex.
    ps=primes(r)
    path=[4]
    for j0 in range(1,r):
        j=j0+1
        off=[ps[i]*ps[j0] for i in range(j0)]
        square=ps[j0]**2
        first=off[-1]
        if want_minimax and j==r:
            first=off[0]
        block=[first]+[v for v in off if v!=first]
        square_position=1 if 2*j<r+1 else j-1
        if want_minimax and j==r-1:
            block.remove(off[0])
            block.append(off[0])
            square_position=j-2
        block.insert(square_position,square)
        path+=block
    return path


def prefix_counts():
    records = {}
    for r in range(2,7):
        blocks,vertices,edge=graph(r)
        if r<=5:
            hist=Counter(cost_stats(path,edge) for path in path_generator(blocks))
            opt = min(s for m,s in hist)
            count = sum(v for (m,s),v in hist.items() if s==opt)
            assert opt==last_cost(r)-improvement(r)
            assert count==optimal_count(r)
            nondominated=[]; best=None
            for m in sorted({m for m,s in hist}):
                z=min(s for mm,s in hist if mm==m)
                if best is None or z<best:
                    best=z
                    nondominated.append([m,z])
            if r>=4:
                B=triangular(r-1)
                assert nondominated==[[B,opt+r-3],[B+1,opt]]
            records[r]={'complete_prefix_paths':sum(hist.values()),'minimum_paths':count,
                        'pareto':[list(x) for x in nondominated]}
        native=native_path(blocks)
        assert cost_stats(native,edge)==(1 if r==2 else triangular(r-1)+1,last_cost(r))
    return records


def unconstrained_dp(r):
    # Independent cut recurrence, permitting arbitrary prime-block interleavings.
    blocks,v,edges=graph(r)
    adjacency=[0]*len(v)
    for u,w in edges:
        i,j=v.index(u),v.index(w)
        adjacency[i]|=1<<j
        adjacency[j]|=1<<i
    total=1<<len(v)
    cuts=[0]*total
    best=[0]*total
    ends=[{} for _ in range(total)]
    for mask in range(1,total):
        lsb=mask&-mask
        first=lsb.bit_length()-1
        rest=mask^lsb
        cuts[mask]=cuts[rest]+adjacency[first].bit_count()-2*(adjacency[first]&rest).bit_count()
        best[mask]=min(best[mask^(1<<j)] for j in range(len(v)) if mask>>j&1)+cuts[mask]
        if mask==lsb:
            ends[mask][first]=cuts[mask]
            continue
        for j in range(len(v)):
            if not mask>>j&1:
                continue
            before=ends[mask^(1<<j)]
            options=[s for i,s in before.items() if adjacency[j]>>i&1]
            if options:
                ends[mask][j]=min(options)+cuts[mask]
    return {'vertices':len(v),'all_orderings_min_total':best[-1],
            'all_Hamilton_orderings_min_total':min(ends[-1].values()),
            'prefix_Hamilton_min_total':last_cost(r)-improvement(r)}


def main():
    from math import gcd
    prefix=prefix_counts()
    constructive={}
    exact=[]
    for r in range(4,101):
        best=last_cost(r)-improvement(r)
        if r<=28:
            blocks,v,edges=graph(r)
            for minimax in (False,True):
                path=prefix_optimal_path(r,minimax)
                assert all(gcd(a,b)>1 for a,b in zip(path,path[1:]))
                assert sorted(v)==sorted(path)
                maxval,total=cost_stats(path,edges)
                assert (maxval,total)==(triangular(r-1)+(not minimax),best+(r-3 if minimax else 0))
            constructive[r]=[triangular(r-1),best+r-3,triangular(r-1)+1,best]
        if r in (4,5,10,20,50,100):
            exact.append({'r':r,'vertices':triangular(r),'edges':r*r*(r-1)//2,
                          'minimum':best,'original':last_cost(r),'difference':improvement(r),
                          'minimizer_count':(optimal_count(r) if r<=20 else None),
                          'minimizer_count_bit_length':optimal_count(r).bit_length()})
        assert improvement(r)==sum((r+1-2*j)*(j-2) for j in range(2,(r+2)//2))
    off=[unconstrained_dp(r) for r in (3,4,5)]
    return {'model':'semiprime prefix Hamilton, one-based prime ranks; zero-based positions',
            'independent_exhaustive_prefix':prefix,
            'unrestricted_exact_cut_dynamic_program':off,
            'both_Pareto_frontiers_built_for_r_inclusive':[4,28],
            'selected_upper_bounds_and_counts':exact}


if __name__=='__main__':
    print(json.dumps(main(),ensure_ascii=False,indent=2))
