"""One-crossing and permanent-order certificates for canonical-cut H suffixes.
Use --model to point to the inherited C64 checks directory containing suffix_limits.py.
Only the Python standard library is required. Positive rational arithmetic is exact.
"""
import argparse
from dataclasses import dataclass
from fractions import Fraction
from functools import lru_cache
import json
from math import comb, gcd, lcm
from pathlib import Path
import sys


def reduced_affine(slope, origin):
    multiple = lcm(slope.denominator, origin.denominator)
    p, b = int(slope*multiple), int(origin*multiple)
    if b < 0:
        p, b = -p, -b
    g = gcd(p,b)
    assert b>0 and p+b>0
    return p//g,b//g


@dataclass(frozen=True)
class Odds:
    p:tuple
    q:tuple
    det:int

    @staticmethod
    def from_forms(first,second):
        p,q=reduced_affine(*first),reduced_affine(*second)
        det=p[0]*q[1]-p[1]*q[0]
        assert det!=0
        return Odds(p,q,det) if det>0 else Odds(q,p,-det)

    def slope(self,u):
        n,d=u.numerator,u.denominator
        return Fraction(self.det*d*d,(self.p[0]*n+self.p[1]*d)*(self.q[0]*n+self.q[1]*d))

    def secant(self,x,y):
        # Exactly (H-1)/(y-x), even when the input interval is microscopic.
        return Fraction(self.det*x.denominator*y.denominator,
                    (self.p[0]*x.numerator+self.p[1]*x.denominator)
                    *(self.q[0]*y.numerator+self.q[1]*y.denominator))


def all_suffixes(q,model,terminal):
    """All C(2q-1,q) gap suffixes from stock c=q+1."""
    block=lru_cache(None)(model.block)
    def recur(r,c,path,matrix):
        if r:
            for m in range(c-1):
                a,b,h,t=block(r,c,m)
                p,n,s,v=matrix
                z=(a*p+b*s, a*n+b*v, h*p+t*s, h*n+t*v)
                g=gcd(*z)
                yield from recur(r-1,c-m,path+(m,),tuple(i//g for i in z))
        else:
            def pull(form):
                a,b=form
                p,n,s,v=matrix
                return a*p+b*s,a*n+b*v
            slot=c-2
            rows=terminal(c)
            yield path+(slot,),Odds.from_forms(pull(rows[0]),pull(rows[1 if slot<=1 else 2]))
    yield from recur(q,q+1,(),(1,0,0,1))


def inversion_count(old,new):
    """Count strict inversions between tie-free orders on the same IDs."""
    n=len(old)
    idx=[0]*n
    tree=[0]*(n+1)
    for j,key in enumerate(old): idx[key]=j+1
    total=0
    for j,key in enumerate(new):
        p=idx[key]; before=0
        k=p
        while k:
            before+=tree[k]; k-=k & -k
        total+=j-before
        while p<=n:
            tree[p]+=1; p+=p & -p
    return total


def sorted_ids(values):
    ans=sorted(range(len(values)),key=values.__getitem__)
    assert all(values[i]<values[j] for i,j in zip(ans,ans[1:])), 'tie in requested finite test'
    return ans


def checked_cut(q,model,terminal):
    paths,odds=zip(*all_suffixes(q,model,terminal))
    assert len(paths)==comb(2*q-1,q)
    assert len(set(odds))==len(odds)
    matrix=(1,0,0,1)
    prev_order=None
    changes=[]
    first=None
    for k in range(q+1,q+9):
        if k>q+1:
            matrix=model.compose(matrix,model.block(k-1,k,1))
        x,y=model.interval_image(matrix,(Fraction(0),Fraction(1)))
        if k>=q+2:
            assert Fraction(4,5)<x<y<Fraction(9,10) and y-x<Fraction(1,900)
        order=sorted_ids([v.secant(x,y) for v in odds])
        if prev_order is not None:
            inversions=inversion_count(prev_order,order)
            changes.append([k-1,k,inversions])
            if inversions and k>q+2 and first is None:
                new_position={i:j for j,i in enumerate(order)}
                i,j=next((i,j) for i,j in zip(prev_order,prev_order[1:]) if new_position[i]>new_position[j])
                first={'k_from':k-1,'k_to':k,'suffixes':[paths[i],paths[j]],
                       'before':str(odds[i].secant(last_x,last_y)/odds[j].secant(last_x,last_y)),
                       'after':str(odds[i].secant(x,y)/odds[j].secant(x,y))}
        if k>=q+2:
            # Since the slope difference has at most one simple zero, matching
            # endpoint signs for each adjacent pair certify all future intervals.
            left_order=sorted_ids([v.slope(x) for v in odds])
            right_order=sorted_ids([v.slope(y) for v in odds])
            if left_order==right_order==order:
                return dict(q=q,count=len(paths),pairs=comb(len(paths),2),permanent_from=k,
                            inversions=changes,first_late_inversion=first)
        prev_order=order; last_x,last_y=x,y
    raise ValueError(f"certificate search exhausted at cut {q}")


def equal_score_test():
    # A precise constructed simple contact at z=6/7, both positive odds.
    # Prescribing local affine logarithmic slopes (1,0),(2,1) would put
    # zeros in [0,1]. Use (1/4,0) and (1/2,1/4) instead.
    z=Fraction(6,7)
    def form(v):
        return v,1-v*z
    a=Odds.from_forms(form(Fraction(1,4)),form(Fraction(0)))
    b=Odds.from_forms(form(Fraction(1,2)),form(Fraction(1,4)))
    assert a.slope(z)==b.slope(z)==Fraction(1,4)
    assert a.slope(z-Fraction(1,1000))<b.slope(z-Fraction(1,1000))
    assert a.slope(z+Fraction(1,1000))>b.slope(z+Fraction(1,1000))
    assert a!=b
    # The exact Taylor coefficient controls true intervals with center skew 56/65.
    eps=Fraction(1,10**8);x=z-Fraction(56,65)*eps;y=x+eps
    assert a.secant(x,y)<b.secant(x,y)
    return dict(contact=str(z),score='1/4',left_order='A<B',right_order='A>B',
                biased_interval_order='A<B',scope='synthetic positive affine odds')


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--model',type=Path,required=True)
    parser.add_argument('--max-cut',type=int,default=9)
    args=parser.parse_args()
    sys.path.insert(0,str(args.model.resolve()))
    import suffix_limits as model
    from observed_four import tail_forms
    terminal=lru_cache(None)(tail_forms)
    assert (1+Fraction(10,900))**5<2
    assert Fraction(4,5)*Fraction(5,6)==Fraction(2,3)
    cuts=[checked_cut(q,model,terminal) for q in range(2,args.max_cut+1)]
    print(json.dumps(dict(cuts=cuts,synthetic=equal_score_test()),indent=2))


if __name__=='__main__':
    main()
