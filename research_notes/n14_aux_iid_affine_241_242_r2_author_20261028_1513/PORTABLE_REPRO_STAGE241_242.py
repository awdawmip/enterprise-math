#!/usr/bin/env python3
"""Self-contained exact N=14 ternary IID certificates for Stage241 and Stage242.
Python 3 standard library only. Exact Fraction Bellman, independent integer
suffix DP, full ordered-history positive-branch DFS, and supporting lines.
No claim of native X6 dynamics or independent researcher review.
"""
from fractions import Fraction as F
from functools import lru_cache

N=14
PN=(3,1,20); QN=(2,2,20)
P=tuple(F(x,24) for x in PN)
DEN=24**N
STATES=[(n,a,b) for n in range(N+1) for a in range(n+1) for b in range(n-a+1)]
NEXT=lambda s,j:(s[0]+1,s[1]+(j==0),s[2]+(j==1))
DATA=[
 (241,F(452793624,8007455),F(483729408,8007455),
  F(265760568220237397,5229145980094464),11,1229,F(78125,57653676),
  F(362608860595,975198486528),F(2682386241371,365699432448),
  F(311522546135,835884417024),F(755943802981,104485552128),
  (5,2047),(2043,0),1064948),
 (242,F(2707386744,48435355),F(2902376448,48435355),
  F(1594127315973221257,31629967560566784),12,1228,F(390625,348734556),
  F(311522546135,835884417024),F(755943802981,104485552128),
  F(1092145237285,2925595459584),F(2619507545471,365699432448),
  (5,4095),(4091,0),1189882)]

def verify(entry):
    (stage,lp,lq,expected_H,expected_k,expected_gap_count,expected_min_gap,
     left_alpha,left_value,right_alpha,right_value,lower_pair,upper_pair,
     expected_nodes)=entry
    @lru_cache(None)
    def bell(s):
        n,a,b=s
        d={'P':lq*F(2**(a+b),3**a),'Q':lp}
        if n<N:
            d['C']=1+sum(P[j]*bell(NEXT(s,j))[0] for j in range(3))
        m=min(d.values())
        return m,tuple(k for k,v in d.items() if v==m),d
    H=bell((0,0,0))[0]
    assert H==expected_H and len(STATES)==680
    ties=[s for s in STATES if len(bell(s)[1])>1]
    assert len(ties)==expected_k and all(len(bell(s)[1])==2 for s in ties)
    gap=[v-bell(s)[0] for s in STATES for v in bell(s)[2].values() if v>bell(s)[0]]
    assert len(gap)==expected_gap_count and min(gap)==expected_min_gap
    idx={s:(i,bell(s)[1]) for i,s in enumerate(ties)}
    fixed={s:bell(s)[1][0] for s in STATES if s not in idx}
    points={}; nodes=0
    for bits in range(1<<len(ties)):
        actions=dict(fixed)
        actions.update({s:a[(bits>>i)&1] for s,(i,a) in idx.items()})
        # Independent suffix recurrence: at depth n, each component has
        # denominator 24^(14-n). The state can merge histories here.
        @lru_cache(None)
        def dp(s):
            n,_,_=s; a=actions[s]; base=24**(N-n)
            if a=='P':return 0,base,n*base,n*base
            if a=='Q':return base,0,n*base,n*base
            z=[dp(NEXT(s,j)) for j in range(3)]
            return (sum(PN[j]*z[j][0] for j in range(3)),
                    sum(QN[j]*z[j][1] for j in range(3)),
                    sum(PN[j]*z[j][2] for j in range(3)),
                    sum(QN[j]*z[j][3] for j in range(3)))
        d=dp((0,0,0))
        # Full ordered histories, with integer branch masses for both laws;
        # no state merging is allowed in this independent implementation.
        acc=[0,0,0,0]; stack=[(0,0,0,1,1)]
        while stack:
            n,x,y,p,q=stack.pop();nodes+=1
            a=actions[(n,x,y)]
            if a=='C':
                for j in range(3):
                    stack.append((n+1,x+(j==0),y+(j==1),p*PN[j],q*QN[j]))
            else:
                m=24**(N-n)
                if a=='Q':acc[0]+=p*m
                else:acc[1]+=q*m
                acc[2]+=n*p*m;acc[3]+=n*q*m
        assert tuple(acc)==d, ('DP_DFS_MISMATCH',stage,bits)
        ep,eq,tp,tq=d
        assert tp>tq
        assert F(tp,DEN)+lp*F(ep,DEN)+lq*F(eq,DEN)==H
        points[bits]=(ep-eq,ep)
    assert nodes==expected_nodes
    # Exact support-line certificate.  Each chosen line is specified by two
    # deterministic optimal policies with opposite error imbalance.  Checking
    # every optimal corner proves its inequality for their entire convex hull.
    def edge(pair):return sorted((points[pair[0]],points[pair[1]]))
    A,B=edge(lower_pair);C,D=edge(upper_pair)
    assert A[0]<0<B[0] and C[0]<0<D[0]
    def margin(p,a,b):
        x,y=p;x1,y1=a;x2,y2=b
        return (y-y1)*(x2-x1)-(y2-y1)*(x-x1)
    assert all(margin(p,A,B)>=0 and margin(p,C,D)<=0 for p in points.values())
    def cut(pair):
        x1,y1=points[pair[0]];x2,y2=points[pair[1]]
        w=F(-x2,x1-x2)
        assert 0<w<1
        alpha=F(w*y1+(1-w)*y2,DEN)
        return alpha,w
    al,wlo=cut(lower_pair); ar,whi=cut(upper_pair)
    assert al==left_alpha and ar==right_alpha and ar>al
    assert H-(lp+lq)*al==left_value
    assert H-(lp+lq)*ar==right_value
    print('STAGE%d_EXACT_PASS policies=%d ordered_nodes=%d gaps=%d'
          ' left=%s right=%s slope=%s' %
          (stage,len(points),nodes,len(gap),al,ar,-lp-lq))
    return nodes

if __name__=='__main__':
    assert sum(verify(entry) for entry in DATA)==2254830
    print('STAGE241_242_PORTABLE_EXACT_PASS 2254830')
