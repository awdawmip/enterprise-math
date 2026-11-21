#!/usr/bin/env python3
"""Exact R5 primitive-16 leading-pole audit: real event intersections vs union cap.
Only Python standard library. Run: python VERIFY_INTERSECTION.py
"""
import json

ZERO=(0,)*8
ONE=(1,)+(0,)*7
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def sc(a,c):return tuple(c*x for x in a)
def mon(k):
    k%=16
    return tuple(1 if k==i else (-1 if k==i+8 else 0) for i in range(8))
def mul(a,b):
    c=[0]*16
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            c[(i+j)%16]+=x*y
    return tuple(c[i]-c[i+8] for i in range(8))

S=[
    set(range(214,219)),
    {214,216,217,218,219,220,221},
    set(range(215,222))
]
S3=set(range(223,291))
S4=set(range(296,313))

def numerator(m,real):
    """Sum 7 exact inclusion-exclusion masks at a primitive 16th root."""
    ans=ZERO
    for mask in range(1,8):
        chosen=[S[j] for j in range(3) if mask>>j&1]
        U=sorted(set.union(*chosen))
        W=ONE
        for p in U:W=mul(W,add(ONE,sc(mon(p),-1)))
        total_poly=ZERO
        def rec(j,loads,cost,total):
            nonlocal total_poly
            if j==len(U):
                total_poly=add(total_poly,mon(cost));return
            p=U[j]
            for a in range(m):
                # The old error: a single cap on ALL p in the union.
                if not real and total+a>=m:break
                nxt=tuple(loads[k]+(a if p in chosen[k] else 0)
                          for k in range(len(chosen)))
                if all(v<m for v in nxt):
                    rec(j+1,nxt,cost+p*a,total+a)
        rec(0,(0,)*len(chosen),0,0)
        ans=add(ans,sc(mul(W,total_poly),1 if len(chosen)%2 else -1))
    return ans

EXPECTED_TRUE={
 1:(16,10,-4,-10,-16,-18,-20,-22),
 2:(-16,4,24,40,44,48,40,36),
 3:(-8,-14,-16,-14,-8,-2,0,6),
 4:(16,4,-8,-24,-32,-36,-32,-24),
 5:(24,8,-4,-12,-24,-28,-36,-32),
}
EXPECTED_OLD={
 1:(16,10,-4,-10,-16,-18,-20,-22),
 2:(-100,-76,-40,0,40,80,104,116),
 3:(280,266,216,130,24,-90,-184,-250),
 4:(-376,-444,-444,-372,-248,-84,92,252),
 5:(232,380,476,496,440,320,148,-44),
}

def main():
    all_sets=S+[S3,S4]
    div=[p for p in range(214,315) if p%16==0]
    assert div==[224,240,256,272,288,304]
    for mask in range(1,32):
        U=set.union(*(all_sets[j] for j in range(5) if mask>>j&1))
        assert (all(p not in U for p in div))==(mask<=7)
    a={215:1,219:1,223:2,296:2}
    events=[sum(a.get(p,0) for p in T)<2 for T in all_sets]
    assert events==[True,True,False,False,False]
    assert sum(p*v for p,v in a.items())==1472
    assert sum(events[:3])-2*int(sum(a.get(p,0) for p in set.union(*S))<2)==2
    assert any(events)==True
    table={}
    for m in range(1,6):
        good,old=numerator(m,True),numerator(m,False)
        assert good==EXPECTED_TRUE[m],(m,good)
        assert old==EXPECTED_OLD[m],(m,old)
        assert (good==old)==(m==1)
        table[str(m)]={"correct":list(good),"prior":list(old),
                       "correct_minus_prior":list(add(good,sc(old,-1)))}
    print(json.dumps({
      "status":"PASS",
      "method":"exact seven-mask enumeration in Z[z]/(z^8+1)",
      "m_range":[1,5],
      "witness":{"m":2,"N":1472,"counts":a,"events":events,
                 "true_union":1,"old_reduction":2},
      "coefficients":table,
      "interpretation":"finite exact falsification of old reduction; all-m replacement open",
      "review":"NOT_REVIEWED"
    },indent=2))
if __name__=="__main__":main()
