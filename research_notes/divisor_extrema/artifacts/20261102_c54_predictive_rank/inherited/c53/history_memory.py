"""C53: exact history diagnostics and a six-parameter finite inverse.

Population: all different factor words of 1260. The preparation remembers
only the most recent visible factor (2 or 3). The positive terminal weight
is q**(A+gamma*B)**2. All proof scopes are in RESEARCH_NOTE.md.
"""
from __future__ import annotations
from collections import defaultdict
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
from typing import Mapping, Sequence
import sys

ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'inherited'/'c52'))
import nonuniform_inverse as old

COUNTS=old.COUNTS
PRIMES=old.PRIMES
words=old.words
word=old.word
text=old.text
raw_scores=old.raw_scores
ALL_WORDS=old.ALL_WORDS
native=old.native
W0,W7,W2,W30,W3=old.PREP_WORDS
W37=word('322375')
WP,WM=old.WP,old.WM
PREP_WORDS=(W0,W7,W2,W30,W37,W3)
CALIBRATION_WORDS=PREP_WORDS+(WP,WM)


def last_visible(prefix:Sequence[int])->int:
    for p in reversed(prefix):
        if p==0:return 1
        if p==1:return -1
    return 0


def state_rates(rates:Sequence[F],theta:F,last:int)->tuple[F,...]:
    return rates[0],rates[1],rates[2]*theta**last,rates[3]


def memory_probability(w:Sequence[int],rates:Sequence[F],theta:F)->F:
    """Multiply reference transitions, retaining last-visible identity."""
    if len(rates)!=4 or any(x<=0 for x in rates) or theta<=0:
        raise ValueError('Four positive baseline rates and positive theta required')
    left=[w.count(i) for i in range(4)]
    answer=F(1);last=0
    for p in w:
        rr=state_rates(rates,theta,last)
        answer*=rr[p]*left[p]/sum(rr[i]*left[i] for i in range(4))
        left[p]-=1
        if p==0:last=1
        elif p==1:last=-1
    return answer


def reference(rates:Sequence[F],theta:F,counts=COUNTS)->dict[tuple[int,...],F]:
    return {w:memory_probability(w,rates,theta) for w in words(counts)}


def terminal_selected(base:Mapping[tuple[int,...],F],q:F,gamma:F,
                      use_brc=False):
    """Reuse the inherited exact positive weighting, common gamma^2 removed."""
    return old.selected(base,q,gamma,use_brc)


def cross_ratio(Q:Mapping[tuple[int,...],F])->F:
    """Four neutral words; arbitrary common positive W(A,B) cancels."""
    return Q[W0]*Q[W37]/(Q[W7]*Q[W30])


def recover_preparation(Q:Mapping[tuple[int,...],F])->dict:
    """Six neutral probabilities; strictly positive even terminal weight."""
    a=Q[W0]/Q[W7]          # rate of 5 after visible 2
    b=Q[W30]/Q[W37]        # rate of 5 after visible 3
    r2=Q[W0]/Q[W2]
    r3=Q[W30]/Q[W3]
    theta=old.rational_sqrt(a/b)
    z=old.rational_sqrt(a*b)
    x=(old.rational_sqrt(1+4*r2*b*(a+1)/a)-1)/2
    y=(old.rational_sqrt(1+4*r3*a*(b+1)/b)-1)/2
    return {'rates':(x,y,z,F(1)),'theta':theta,'a':a,'b':b}


def preparation_corrections(rates:Sequence[F],theta:F)->tuple[F,F]:
    x,y,z,one=rates
    if one!=1:raise ValueError('Normalize baseline rate of 7 to 1')
    a=z*theta;b=z/theta
    fu=a*(b+1)*(a+y+1)/(b*(a+1)*(x+b+1))
    fv=(2*x+y+b+1)*(x+y+a+1)/((x+y+b+1)*(x+2*y+a+1))
    return fu,fv


def infer(Q:Mapping[tuple[int,...],F])->dict:
    out=recover_preparation(Q)
    fu,fv=preparation_corrections(out['rates'],out['theta'])
    u=(Q[WP]/Q[W0])*fu;v=(Q[WM]/Q[W0])*fv
    if not 0<u*v<1:raise ValueError('Two odds do not support 0<q<1')
    out.update(u=u,v=v)
    return out


def predict_all(rates:Sequence[F],theta:F,u:F,v:F)->dict[tuple[int,...],F]:
    masses={}
    for w in ALL_WORDS:
        A,B=raw_scores(w);k=A//2
        ep=k*(k+B)//2;em=k*(k-B)//2
        masses[w]=memory_probability(w,rates,theta)*u**ep*v**em
    total=sum(masses.values())
    return {w:p/total for w,p in masses.items()}


def memory_histogram(counts:tuple[int,...],rates:Sequence[F],theta:F)->dict:
    """DP state (used counts, partial A, partial B, last visible).

    Future transitions and terminal joint scores factor through this state.
    The last-visible coordinate is retained before any positive aggregation.
    """
    delta={(0,1):1,(0,2):-1,(0,3):1,(1,2):1,(1,3):-1}
    states={((0,0,0,0),0,0,0):F(1)}
    for _ in range(sum(counts)):
        out=defaultdict(F)
        for (used,A,B,last),mass in states.items():
            remaining=[counts[i]-used[i] for i in range(4)]
            rr=state_rates(rates,theta,last)
            total=sum(rr[i]*remaining[i] for i in range(4))
            for p,n in enumerate(remaining):
                if not n:continue
                nxt=list(used);nxt[p]+=1
                da=2*sum(used[j]*delta.get((j,p),0) for j in range(p))
                db=2*used[2] if p==3 else 0
                newlast=1 if p==0 else -1 if p==1 else last
                out[(tuple(nxt),A+da,B+db,newlast)]+=mass*rr[p]*n/total
        states=dict(out)
    H=sum(counts[i]*counts[j]*d for (i,j),d in delta.items())
    hB=counts[2]*counts[3]
    out=defaultdict(F)
    for (used,A,B,last),mass in states.items():out[A-H,B-hB]+=mass
    return dict(out)


def scores_for_counts(w:Sequence[int])->tuple[int,int]:
    counts=tuple(w.count(i) for i in range(4))
    delta={(0,1):1,(0,2):-1,(0,3):1,(1,2):1,(1,3):-1}
    A=2*sum(d for i,p in enumerate(w) for z in w[i+1:]
            for (a,b),d in delta.items() if p==a and z==b)
    H=sum(counts[i]*counts[j]*d for (i,j),d in delta.items())
    B=2*sum(p==2 and z==3 for i,p in enumerate(w) for z in w[i+1:])
    return A-H,B-counts[2]*counts[3]


def reference_next(prefix:tuple[int,...],rates,theta,counts=COUNTS):
    remaining=[counts[i]-prefix.count(i) for i in range(4)]
    rr=state_rates(rates,theta,last_visible(prefix))
    total=sum(rr[i]*remaining[i] for i in range(4))
    return {p:rr[p]*n/total for p,n in enumerate(remaining) if n}


def prefix_state(prefix:tuple[int,...])->tuple:
    counts=tuple(prefix.count(i) for i in range(4))
    delta={(0,1):1,(0,2):-1,(0,3):1,(1,2):1,(1,3):-1}
    A=2*sum(d for i,p in enumerate(prefix) for z in prefix[i+1:]
            for (a,b),d in delta.items() if p==a and z==b)
    B=2*sum(p==2 and z==3 for i,p in enumerate(prefix) for z in prefix[i+1:])
    return counts,A,B,last_visible(prefix)


def completion_kernel(rates,theta,q,gamma,counts=COUNTS):
    """Exact positive h transform; returns conditional next probabilities.

    For half-integral gamma all relative terminal exponents below are integer.
    Negative relative exponents are harmless: q is strictly positive and the
    omitted common q^(gamma^2) cancels in every conditional probability.
    """
    delta={(0,1):1,(0,2):-1,(0,3):1,(1,2):1,(1,3):-1}
    H=sum(counts[i]*counts[j]*d for (i,j),d in delta.items())
    hB=counts[2]*counts[3]
    @lru_cache(None)
    def h(used,A,B,last):
        if used==counts:
            aa=A-H;bb=B-hB
            exponent=F(aa*aa)+2*gamma*aa*bb+gamma*gamma*(bb*bb-1)
            if exponent.denominator!=1:raise ValueError('Exact rational terminal exponent required')
            return q**int(exponent)
        rem=[counts[i]-used[i] for i in range(4)]
        rr=state_rates(rates,theta,last);den=sum(rr[i]*rem[i] for i in range(4))
        ans=F(0)
        for p,n in enumerate(rem):
            if not n:continue
            nxt=list(used);nxt[p]+=1
            da=2*sum(used[j]*delta.get((j,p),0) for j in range(p))
            db=2*used[2] if p==3 else 0
            nl=1 if p==0 else -1 if p==1 else last
            ans+=rr[p]*n/den*h(tuple(nxt),A+da,B+db,nl)
        return ans
    def next_prob(prefix):
        used,A,B,last=prefix_state(prefix)
        if used==counts:return {}
        pp=reference_next(prefix,rates,theta,counts);ans={}
        for p,prob in pp.items():
            nxt=prefix+(p,)
            ans[p]=prob*h(*prefix_state(nxt))/h(used,A,B,last)
        return ans
    return next_prob,h


# Interval formulas use inherited outward-rounded rational primitives.
I=old.I
point=old.point
add,sub,mul,div=old.iadd,old.isub,old.imul,old.idiv
sqrt_box=old.sqrt_box

def multiply_all(*args:I)->I:
    ans=point(1)
    for a in args:ans=mul(ans,a)
    return ans


def inverse_box(Q:Mapping[tuple[int,...],I])->dict:
    a=div(Q[W0],Q[W7]);b=div(Q[W30],Q[W37])
    r2=div(Q[W0],Q[W2]);r3=div(Q[W30],Q[W3])
    z=sqrt_box(mul(a,b));theta=sqrt_box(div(a,b))
    def root_from_odds(odds):return div(sub(sqrt_box(add(point(1),mul(point(4),odds))),point(1)),point(2))
    # b*(1+1/a) and a*(1+1/b), coordinate monotone.
    vx=(r2[0]*b[0]*(1+1/a[1]),r2[1]*b[1]*(1+1/a[0]))
    vy=(r3[0]*a[0]*(1+1/b[1]),r3[1]*a[1]*(1+1/b[0]))
    x=root_from_odds(vx);y=root_from_odds(vy)
    fu=div(multiply_all(a,add(b,point(1)),add(add(a,y),point(1))),
           multiply_all(b,add(a,point(1)),add(add(x,b),point(1))))
    fv=div(multiply_all(add(add(mul(point(2),x),y),add(b,point(1))),
                        add(add(x,y),add(a,point(1)))),
           multiply_all(add(add(x,y),add(b,point(1))),
                        add(add(x,mul(point(2),y)),add(a,point(1)))))
    u=mul(div(Q[WP],Q[W0]),fu);v=mul(div(Q[WM],Q[W0]),fv)
    lu=old.outward(old.previous.log_box(u));lv=old.outward(old.previous.log_box(v))
    total=add(lu,lv)
    if total[1]>=0:raise ValueError('Probability box does not ensure 0<q<1')
    prod=mul(u,v)
    qbox=(old.previous.root_interval(prod[0],8,100)[0],old.previous.root_interval(prod[1],8,100)[1])
    gamma=div(sub(lu,lv),total)
    return {'x':x,'y':y,'z':z,'theta':theta,'a':a,'b':b,'q':qbox,'gamma':gamma,'u':u,'v':v}


def serialise(obj):
    if isinstance(obj,F):return {'numerator':obj.numerator,'denominator':obj.denominator,'approx':float(obj)}
    if isinstance(obj,dict):return {str(k):serialise(v) for k,v in obj.items()}
    if isinstance(obj,(list,tuple)):return [serialise(v) for v in obj]
    return obj
