"""The 108 bounded-observer intervals on the frozen six-axis / hidden-field law."""
from collections import Counter
from fractions import Fraction as F
from functools import lru_cache
from itertools import product
from math import lcm
import json

MS=(8,32,128)
TS=(1,2,4)
RS=(2,4,8)


def mass(law,j):
    return F(1,2*j*(j+1)) if law==1 else F(2,j*(j+1)*(j+2))


def tail(law,M):
    return F(1,M+1) if law==1 else F(2,(M+1)*(M+2))


def complement_num(k,R,soft):
    if abs(k)>=R:
        return 0
    return R*R-k*k if soft else 1


def weight(law,M):
    denom=lcm(*(mass(law,j).denominator for j in range(1,M+1)))
    nums=[int(denom*mass(law,abs(j))) if j else 0 for j in range(-M,M+1)]
    assert F(sum(nums),denom)==1-tail(law,M)
    return nums,denom


def convolve(x,y):
    out=[0]*(len(x)+len(y)-1)
    for i,xi in enumerate(x):
        if xi:
            for j,yj in enumerate(y):
                out[i+j]+=xi*yj
    return out


@lru_cache(None)
def harmonic(n,order):
    return sum((F(1,j**order) for j in range(1,n+1)),F(0))


def exact_pair_tail(law,M,s):
    # Returns a+b*zeta(2) for S_2=s, max |A_i|>M.
    c=(F(1,2),-F(1,2)) if law==1 else (F(1),F(-2),F(1))
    a=b=F(0)
    for i,ci in enumerate(c):
        for l,cl in enumerate(c):
            j=l-abs(s)
            w=2*ci*cl
            if i==j:
                a-=w*harmonic(M+i,2)
                b+=w
            else:
                a+=w*(harmonic(M+j,1)-harmonic(M+i,1))/(j-i)
    return a,b


def gap_bound(law,M,t,R,soft):
    wden=R*R if soft else 1
    if t==1:
        return F(0)
    total=F(0)
    for s in range(1-R,R):
        J=(M+1-abs(s)+t-2)//(t-1)
        # Fix all but two jumps. One value is forced by the net sum.
        bound=min(mass(law,M+1)*tail(law,J-1),tail(law,M)*mass(law,J))
        total+=F(complement_num(s,R,soft),wden)*t*(t-1)*bound
    return total


def joint_check(law):
    # All 12^2 * 16^2 true joint update words, at M=8 and t=2.
    M=8
    weights,den=weight(law,M)
    increments=[]
    for i in range(6):
        for sign in (-1,1):
            v=[0]*6
            v[i]=sign
            increments.append(tuple(v))
    xyz=Counter()
    for x,y in product(increments,repeat=2):
        state=tuple(a+b for a,b in zip(x,y))
        for a in range(-M,M+1):
            if a:
                for b in range(-M,M+1):
                    if b:
                        xyz[state,a+b]+=weights[M+a]*weights[M+b]
    xm=Counter(tuple(a+b for a,b in zip(x,y)) for x,y in product(increments,repeat=2))
    hidden=convolve(weights,weights)
    assert sum(xyz.values())==12**2*sum(weights)**2
    for x,n in xm.items():
        for k,w in enumerate(hidden,-2*M):
            assert xyz[x,k]==n*w
    observers={}
    for R in RS:
        for soft in (False,True):
            wd=R*R if soft else 1
            obs=sum((wd-complement_num(k,R,soft))*n for (x,k),n in xyz.items())
            observers[R,soft]=F(obs,(12*den)**2*wd)
    return dict(retained_words=(12*2*M)**2,positive_joint_states=len(xyz),
                native_endpoints=len(xm)),observers


def second_order_law_two():
    weights,den=weight(2,8)
    dist=convolve(weights,weights)
    mass_pairs=[]
    for s in range(8):
        a,b=exact_pair_tail(2,8,s)
        mass_pairs.append((a+F(dist[16+s],den**2),b))
    a0,b0=mass_pairs[0]
    coeff={}
    for R in RS:
        for soft in (False,True):
            a=b=F(0)
            for s in range(R):
                w=F(complement_num(s,R,soft)*(1 if s==0 else 2),R*R if soft else 1)
                sa,sb=16+s*a0,-8+s*b0
                for j in range(1,s):
                    x,y=mass_pairs[j]
                    sa+=2*(s-j)*x
                    sb+=2*(s-j)*y
                a+=24*w*(sa-3)
                b+=24*w*sb
            coeff[f"{R}-{'soft' if soft else 'hard'}"]=[str(a),str(b)]
    assert coeff["2-hard"]==["0","0"] and coeff["2-soft"]==["78","-48"]
    return coeff


def pi_bounds():
    def atan_bounds(q,n):
        value=sum((F((-1)**j,(2*j+1)*q**(2*j+1)) for j in range(n)),F(0))
        other=value+F((-1)**n,(2*n+1)*q**(2*n+1))
        return min(value,other),max(value,other)
    a,b=atan_bounds(5,44)
    c,d=atan_bounds(239,16)
    return 16*a-4*d,16*b-4*c


def main():
    pi_lo,pi_hi=pi_bounds()
    rows=[]
    pairs={}
    joints={}
    for law in (1,2):
        joints[law],oracle=joint_check(law)
        for M in MS:
            nums,den=weight(law,M)
            dist=[1]
            for t in range(1,5):
                dist=convolve(dist,nums)
                if t not in TS:
                    continue
                kept,full=sum(dist),den**t
                delta=1-F(kept,full)
                assert delta==1-(1-tail(law,M))**t
                if M==128:
                    assert delta<=F(1,32)
                for R in RS:
                    for soft in (False,True):
                        wd=R*R if soft else 1
                        obs="soft" if soft else "hard"
                        denom=full*wd
                        missing=sum(complement_num(s,R,soft)*dist[t*M+s]
                                    for s in range(1-R,R))
                        lo=wd*kept-missing
                        up=lo+(full-kept)*wd
                        left,upper=F(lo,denom),F(up,denom)
                        gap=gap_bound(law,M,t,R,soft)
                        extra=max(left,upper-gap)
                        assert 0<=left<=extra<=upper<=1
                        if M==8 and t==2:
                            assert left==oracle[R,soft]
                        if t==2:
                            a=b=F(0)
                            for k in range(1-R,R):
                                da,db=exact_pair_tail(law,M,k)
                                w=F(complement_num(k,R,soft),wd)
                                a+=w*da
                                b+=w*db
                            target=(upper-a,-b)
                            key=f"{law}-{R}-{obs}"
                            if key in pairs:
                                assert pairs[key]==target
                            pairs[key]=target
                            v1=a+b*pi_lo**2/6
                            v2=a+b*pi_hi**2/6
                            assert 0<min(v1,v2)<=max(v1,v2)<=gap
                        rows.append(dict(law=law,M=M,t=t,R=R,observer=obs,
                                         common_denominator=str(denom),low_numerator=str(lo),
                                         upper_numerator=str(up),gap_upper=str(gap),
                                         tightened_low=str(extra)))
    assert len(rows)==108
    exact={k:[str(v) for v in ab] for k,ab in pairs.items()}
    assert sum(b!=0 for a,b in pairs.values())==4
    print(json.dumps(dict(description="Endpoints = numerator/common_denominator. "
                          "gap_upper bounds upper minus true; true >= tightened_low. "
                          "two_step_exact gives a,b for a+b*zeta(2).",
                          independent_joint_words=joints,two_step_exact=exact,
                          law_two_t4_Mminus6=second_order_law_two(),
                          maximum_M_width={law:str(1-(1-tail(law,128))**4) for law in (1,2)},
                          row_count=len(rows),intervals=rows),indent=2))


if __name__=="__main__":
    main()
