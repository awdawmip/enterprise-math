#!/usr/bin/env python3
"""Stage332-B: exact integer cover and algebraic tagged-sign census.
Scope: auxiliary three-visit Bernoulli/BRC observer, not native X6 dynamics.
"""
from fractions import Fraction as F
from collections import Counter
from hashlib import sha256

D=2**20
D3=D**3
M=(61,21,9,9)
W=(1,3,3,1)
LIMIT=F(61,10000)
BOX=(F(21,100),F(6,25),F(1,2),F(2,3))

def B(k,z): return z**k*(1-z)**(3-k)
def residual(k,x,y): return (4*B(k,x)+B(k,y))/5-F(M[k],160)
def b(x,y): return F(5,32)*sum(W[k]*abs(residual(k,x,y)) for k in range(4))

def exact_int_extrema(k,a,d):
    v1=27*a**k*(D-a)**(3-k)
    v2=27*d**k*(D-d)**(3-k)
    lo,hi=min(v1,v2),max(v1,v2)
    if k==1 and 3*a<=D<=3*d: hi=max(hi,4*D3)
    if k==2 and 3*a<=2*D<=3*d: hi=max(hi,4*D3)
    return lo,hi

def lower_b_num(rect):
    a,d,c,e=rect
    ans=0
    for k in range(4):
        xl,xu=exact_int_extrema(k,a,d)
        yl,yu=exact_int_extrema(k,c,e)
        L=32*(4*xl+yl)-27*M[k]*D3
        U=32*(4*xu+yu)-27*M[k]*D3
        assert L<=U
        ans+=W[k]*(L if L>0 else -U if U<0 else 0)
    return ans # b>=ans/(1024*27*D**3)

def label(rect):
    a,d,c,e=rect
    if F(a,D)>=BOX[0] and F(d,D)<=BOX[1] and F(c,D)>=BOX[2] and F(e,D)<=BOX[3]:
        return 'INSIDE_BOX'
    if 10000*lower_b_num(rect)>61*1024*27*D3:
        return 'OUTSIDE_LOW_B'
    return None

def exact_cover():
    stack=[(0,D,0,D,0)]; leaves=[]
    while stack:
        a,d,c,e,depth=stack.pop()
        cl=label((a,d,c,e))
        if cl:
            leaves.append((a,d,c,e,cl,depth))
            continue
        assert depth<75
        if d-a>1 and (e-c<=1 or 4*(d-a)>=e-c):
            mid=(a+d)//2
            stack.extend(((mid,d,c,e,depth+1),(a,mid,c,e,depth+1)))
        else:
            assert e-c>1
            mid=(c+e)//2
            stack.extend(((a,d,mid,e,depth+1),(a,d,c,mid,depth+1)))
    assert all(a<d and c<e and label((a,d,c,e))==cl for a,d,c,e,cl,depth in leaves)
    assert sum((d-a)*(e-c) for a,d,c,e,cl,depth in leaves)==D**2
    assert len(leaves)==127
    assert Counter(q[4] for q in leaves)==Counter({'OUTSIDE_LOW_B':112,'INSIDE_BOX':15})
    return leaves

def exact_rational_extrema(k,lo,hi):
    z=[B(k,lo),B(k,hi)]
    if k==1 and lo<=F(1,3)<=hi:z.append(F(4,27))
    if k==2 and lo<=F(2,3)<=hi:z.append(F(4,27))
    return min(z),max(z)

def upper_b_on_y_segment(x,lo,hi):
    upper=F(0)
    for k in range(4):
        yl,yu=exact_rational_extrema(k,lo,hi)
        L=(4*B(k,x)+yl)/5-F(M[k],160)
        U=(4*B(k,x)+yu)/5-F(M[k],160)
        upper+=W[k]*max(abs(L),abs(U))
    return F(5,32)*upper

def quadratic_root_checks():
    # All nontrivial roots of Bk(a)-Bk(z) for anchors a=1/4 or 3/4.
    # Exact checks of sqrt13 in (89/25,91/25), sqrt21 in (113/25,23/5).
    assert F(89,25)**2<13<F(91,25)**2
    assert F(113,25)**2<21<F(23,5)**2
    # Roots are: B1(1/4): (7-sqrt13)/8 in (.42,.43),
    # B1(3/4): (5-sqrt21)/8 in (.05,.06),
    # B2(1/4): (3+sqrt21)/8 in (.94,.95),
    # B2(3/4): (1+sqrt13)/8 in (.57,.58).
    # Each root isolation follows by affine rearrangement of the exact square bounds.
    assert F(21,50)>BOX[1] and F(43,100)<BOX[2]
    assert F(3,50)<BOX[0] and F(47,50)>BOX[3]
    # Explicitly verify the quadratic factorizations by coefficient equality:
    # B1(a)-B1(z)=-(z-a)*(z*z+(a-2)*z+(1-a)**2)
    # B2(a)-B2(z)= (z-a)*(z*z+(a-1)*z+a*(a-1))
    for a in (F(1,4),F(3,4)):
        for z in (F(0),F(1,5),F(23,100),F(11,20),F(3,5),F(1)):
            assert B(1,a)-B(1,z)==-(z-a)*(z*z+(a-2)*z+(1-a)**2)
            assert B(2,a)-B(2,z)== (z-a)*(z*z+(a-1)*z+a*(a-1))
    # All 16 tagged signs are fixed except y against anchor 3/4 at k=2.
    # Enumerated in k order 0,1,2,3.
    signs={
        ('x',F(1,4)):'-+++',
        ('x',F(3,4)):'--++',
        ('y',F(1,4)):'++--',
        ('y',F(3,4)):'--?+',
    }
    for typ,z in [('x',F(23,100)),('y',F(11,20))]:
        for a in (F(1,4),F(3,4)):
            got=''.join('+' if B(k,a)-B(k,z)>0 else '-' if B(k,a)-B(k,z)<0 else '0' for k in range(4))
            assert all(u=='?' or u==v for u,v in zip(signs[(typ,a)],got))
    y2=F(3,5)
    assert B(2,F(3,4))-B(2,F(11,20))>0
    assert B(2,F(3,4))-B(2,y2)<0
    assert b(F(23,100),F(57,100))<LIMIT
    assert b(F(23,100),F(58,100))<LIMIT
    upper=upper_b_on_y_segment(F(23,100),F(57,100),F(58,100))
    assert upper==F(147739,32000000) and upper<LIMIT
    return signs,upper

if __name__=='__main__':
    leaves=exact_cover()
    data='\n'.join(','.join(map(str,t)) for t in leaves)+'\n'
    print('COVER_D',D,'LEAVES',len(leaves),'COUNTS',dict(Counter(t[4] for t in leaves)))
    print('MAX_DEPTH',max(t[5] for t in leaves),'AREA',sum((v-u)*(z-y) for u,v,y,z,cl,depth in leaves))
    print('CERTIFICATE_MANIFEST_SHA256',sha256(data.encode()).hexdigest())
    print('RATIONAL_FEASIBLE_BOX',tuple(map(str,BOX)))
    signs,upper=quadratic_root_checks()
    print('FIXED_15_TAGS_AND_ONE_ALGEBRAIC_SWITCH',[(str(t),str(a),s) for (t,a),s in signs.items()])
    print('EXACT_CUSP_ROOT',(str(F(1,1)), 'sqrt(13)', '8'), 'ISOLATION',(str(F(57,100)),str(F(58,100))))
    print('CUSP_SEGMENT_PUBLIC_COST_UPPER',str(upper))
    q=b(F(231,1000),F(5,9))
    assert q==F(2768189461,729000000000) and q<F(19,5000)
    print('RATIONAL_BETA_UPPER_WITNESS',str(q),'<' ,str(F(19,5000)))
    print('STAGE332B_15_FIXED_TAGS_AND_ONE_EXACT_CUSP_GLOBAL_PASS')
