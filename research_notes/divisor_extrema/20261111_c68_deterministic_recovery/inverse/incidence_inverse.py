"""Exact incidence inverse for the native three-tail scalar at a specified size."""
from argparse import ArgumentParser
from bisect import bisect_left, bisect_right
from collections import defaultdict
from dataclasses import dataclass
from fractions import Fraction as Q
from functools import lru_cache
from itertools import combinations
from math import isqrt
from pathlib import Path
import json
import sys

@dataclass(frozen=True)
class Arc:
    p:Q
    q:Q
    s:Q
    t:Q
    cutoff:Q

    def value(self,x):
        if x>self.cutoff:return Q(2)
        return (self.p*x+self.q)/(self.s*x+self.t)

def arc(a,b,h):
    assert a>b>-1 and h>1
    top=(1+a)/(1+b)/h
    cutoff=(top-1)/(a-b*top) if top>=1 else Q(-1)
    return Arc(h*a-b,h-1,(1-h)*a*b,a-h*b,cutoff)

def words(length,blocks):
    for pos in combinations(range(length),blocks):
        letters=['5']*length
        for i in pos:letters[i]='B'
        yield ''.join(letters)

def slope(c):
    return Q(c[1]-c[0],c[0])

def sweep(points,arcs):
    """Report IDs of all incidences. Intersections in sorted x can skip/touch exact ties."""
    if not points or not arcs:return []
    by_x=defaultdict(list)
    for pid,(x,y) in enumerate(points):by_x[x].append((y,pid))
    xs=sorted(by_x);n=len(xs)
    active=[bisect_right(xs,v.cutoff) for v in arcs]
    answer=[]
    chunk=1+isqrt(len(points)-1)
    for first in range(0,len(arcs),chunk):
        ids=list(range(first,min(first+chunk,len(arcs))))
        events=defaultdict(list)
        for i,j in combinations(ids,2):
            a,b=arcs[i],arcs[j]
            A=a.p*b.s-b.p*a.s
            B=a.p*b.t+a.q*b.s-b.p*a.t-b.q*a.s
            cuts={0,n,active[i],active[j]}
            if A:
                vertex=-B/(2*A)
                cuts.update((bisect_left(xs,vertex),bisect_right(xs,vertex)))
            cuts=sorted(cuts)
            def follows(t):
                # Pair IDs have i<j, hence equality always ranks i first.
                return a.value(xs[t])>b.value(xs[t])
            def record(at,follows_after):
                events[at].append((i,j,1 if follows_after else -1))
            for lo,hi in zip(cuts,cuts[1:]):
                if lo==hi:continue
                start,end=follows(lo),follows(hi-1)
                if lo and start!=follows(lo-1):record(lo,start)
                if start==end:continue
                low,high=lo+1,hi-1
                while low<high:
                    mid=(low+high)//2
                    if follows(mid)==start:low=mid+1
                    else:high=mid
                record(low,end)
        order=sorted(ids,key=lambda i:(arcs[i].value(xs[0]),i))
        ranks={i:t for t,i in enumerate(order)}
        for t,x in enumerate(xs):
            if t in events:
                delta=defaultdict(int)
                for i,j,s in events[t]:delta[i]+=s;delta[j]-=s
                for i,s in delta.items():ranks[i]+=s;order[ranks[i]]=i
            def bound(y,right):
                lo,hi=0,len(order)
                while lo<hi:
                    mid=(lo+hi)//2
                    v=arcs[order[mid]].value(x)
                    if v<y or (right and v==y):lo=mid+1
                    else:hi=mid
                return lo
            for y,pid in by_x[x]:
                lo=bound(y,False)
                if lo<len(order) and arcs[order[lo]].value(x)==y:
                    answer.extend((pid,i) for i in order[lo:bound(y,True)])
    return answer

def inverse(k,h,maps,terminal):
    from upper_frontier import lift,terminal_forms
    @lru_cache(None)
    def edges(r,c):return tuple(maps(r,c))
    @lru_cache(None)
    def child(r,c,gaps):
        if not r:
            assert gaps==(c-2,)
            return terminal_forms(c,terminal)
        m=gaps[0]
        return lift(edges(r,c)[m],child(r-1,c-m,gaps[1:]),m)
    prefixes=defaultdict(list)
    for j in range(1,k+1):
        for w in words(k,j):
            gaps=tuple(map(len,w.split('B')))
            c=k+1-gaps[0]
            x,y=Q(0),Q(1)
            for z,m in enumerate(gaps[1:-1],1):
                a,b,h0=edges(k-z,c)[m]
                x=Q(a)/(a+h0+(b-h0)*x)
                y=Q(a)/(a+h0+(b-h0)*y)
                c-=m
            ell=gaps[-1]
            assert c==k+1-(k-j-ell)
            prefixes[j,ell].append((w,min(x,y),max(x,y)))
    matches=[]
    for (j,ell),pr in prefixes.items():
        r=k-j;c=k+1-(k-j-ell)
        suffixes=list(words(k-1,r))
        arcs=[]
        for w in suffixes:
            gaps=tuple(map(len,('5'*ell+w).split('B')))
            p,q=child(r,c,gaps).columns
            arcs.append(arc(slope(p),slope(q),h))
        for i,t in sweep([(x,y) for _,x,y in pr],arcs):
            matches.append(tuple(map(len,(pr[i][0]+suffixes[t]).split('B'))))
    return sorted(matches)

def test_sweep():
    arcs=[arc(a,b,Q(5,4)) for a,b in [(Q(2),Q(0)),(Q(2),Q(0)),(Q(3),Q(1,3)),
          (Q(1,2),Q(-1,2)),(Q(-1,4),Q(-3,4)),(Q(1,5),Q(0)),(Q(1,4),Q(0))]]
    xs=sorted({Q(j,40) for j in range(41)}|{a.cutoff for a in arcs if a.cutoff>=0})
    points=[(x,y) for x in xs for y in [Q(1),Q(1),Q(2,3),*(a.value(x) for a in arcs if x<=a.cutoff)]]
    expected=[(i,j) for i,(x,y) in enumerate(points) for j,a in enumerate(arcs) if a.value(x)==y]
    assert sorted(sweep(points,arcs))==expected
    return len(points),len(expected)
if __name__=='__main__':
    p=ArgumentParser(description=__doc__)
    p.add_argument('--checks',type=Path,required=True)
    p.add_argument('--inherited',type=Path,required=True)
    p.add_argument('--prior',type=Path,required=True,help='C67/inverse')
    p.add_argument('--output',type=Path)
    p.add_argument('--k',type=int)
    p.add_argument('--H',type=Q)
    args=p.parse_args()
    sys.path[:0]=[str(v.resolve()) for v in (args.checks,args.inherited,args.prior)]
    from observed_four import tail_forms
    from certify_schedules import block_maps
    if args.H is not None:
        if args.H<=1:
            result=[]
        elif args.k is not None:
            assert args.k>=2
            result=inverse(args.k,args.H,block_maps,tail_forms)
        else:
            k=2
            result=[]
            num,den=args.H.numerator,args.H.denominator
            while 5**k*(num-den)**2<144*num*num:
                result.extend(dict(k=k,gaps=w) for w in inverse(k,args.H,block_maps,tail_forms))
                k+=1
    else:
        assert args.k is None
        from functools import lru_cache
        from suffix_limits import block
        from inverse_grid import scalar
        def tails(c):
            r=sorted(tail_forms(c),key=lambda x:x[0]/x[1])
            return r[0],r[-1]
        rows=[]
        for k in [2,5,8,10]:
            row=json.loads((args.prior/'upper_frontier.json').read_text())['records'][k-2]
            for w in [tuple(row['gaps']),tuple([1]*(k-1)+[0,0])]:
                h=scalar(k,w,lru_cache(None)(block),tails)
                actual=inverse(k,h,block_maps,tail_forms)
                assert actual==[w]
                rows.append(dict(k=k,target=str(h),preimages=actual))
        assert inverse(8,Q(100),block_maps,tail_forms)==[]
        all_checked=0
        for k in range(2,6):
            groups=defaultdict(list)
            for encoded in words(2*k-1,k):
                w=tuple(map(len,encoded.split('B')))
                groups[scalar(k,w,lru_cache(None)(block),tails)].append(tuple(w))
            for val,ws in groups.items():
                assert inverse(k,val,block_maps,tail_forms)==sorted(ws)
                all_checked+=1
        result=dict(synthetic_points_and_incidences=test_sweep(),native_exact_queries=rows,
                    exhaustive_targets_through_k5=all_checked,absent_at_8='100')
    out=json.dumps(result,indent=2)+'\n'
    if args.output:args.output.write_text(out)
    else:print(out,end='')
