"""Reachability with two calibrated packet times; independent shared-slot transport."""
import json
from collections import Counter
from itertools import permutations,product
from math import comb,gcd

BASE=(0,1,2)
LOOPS=(((0,1,2),(0,1,3),(0,2,3)),((0,1,2),(0,2,3),(1,2,3)))


def update(state,loop):
    slots=dict(zip(BASE,state))
    for u,v in zip(loop,loop[1:]+loop[:1]):
        outgoing,=set(u)-set(v)
        incoming,=set(v)-set(u)
        slots[incoming]=slots.pop(outgoing)
    return tuple(slots[i] for i in BASE)


STATES=list(permutations(BASE))
ID=STATES.index(BASE)
STEP=[[STATES.index(update(p,loop)) for loop in LOOPS] for p in STATES]
SIGNS=[sum(p[i]>p[j] for i in range(3) for j in range(i+1,3))%2 for p in STATES]


def endpoint(word):
    st=ID
    for i in word:
        st=STEP[st][i]
    return st


def semigroup(n,A,B):
    if n<0:
        return False
    j=n*pow(B,-1,A)%A if A>1 else 0
    return j*B<=n


def reachable(n,u,v,A,B):
    return any((n-d)%2==0 and semigroup((n-d)//2,A,B) for d in (u,v))


def integer_model(a,b):
    g=gcd(a,b)
    A,B=a//g,b//g
    assert A<=B
    L=3*(A+B)
    arc={}
    cost=0;st=ID
    for k in range(6):
        arc[st]=(min(cost,L-cost),max(cost,L-cost))
        st=STEP[st][k%2]
        cost+=(A,B)[k%2]
    assert st==ID and len(arc)==6
    odd=(A+B)%2==0
    frontier=(B if A==1 else A*B+B-A) if odd else 2*A*B+A+B
    limit=max(6*(A+B), frontier+2*(A+B)+12)
    dp=[0]*(limit+1);dp[0]=1<<ID
    for t,mask in enumerate(dp):
        for h in range(6):
            if mask&(1<<h):
                for j,delta in enumerate((A,B)):
                    if t+delta<=limit:
                        dp[t+delta]|=1<<STEP[h][j]
    profiles=[]
    for h,(u,v) in sorted(arc.items()):
        direct=max((t for t in range(limit+1) if not dp[t]&(1<<h) and
                    (not odd or t%2==SIGNS[h])),default=(SIGNS[h]-2 if odd else -1))
        pred=[reachable(t,u,v,A,B) for t in range(limit+1)]
        assert all(p==bool(mask&(1<<h)) for p,mask in zip(pred,dp))
        if odd:
            D=(v-u)//2
            z=(D*pow(B,-1,A))%A if A>1 else 0
            s=(z*B-D)//A
            apery=[j*B-A*max(s,0)*(j>=z) for j in range(A)]
            gap=u+2*(max(apery)-A)
            if A>=3:
                ii,jj=next((i,j) for i,j in ((0,0),(1,0),(0,1),(1,1),(2,1))
                           if i*A+j*B==u)
                assert gap==A*B+max((ii-2)*A+(1-jj)*B,(1-ii)*A+(jj-2)*B)
        else:
            gap=v+2*(A*B-A-B)
        assert direct==gap,(A,B,h,direct,gap)
        profiles.append({"slots":STATES[h],"short_long_arcs":[g*u,g*v],
                         "last_missing_eligible_divided_by_g":gap})
    assert max(x["last_missing_eligible_divided_by_g"] for x in profiles)==frontier
    return {"weights":[a,b],"gcd":g,"identity_period":g*(2 if odd else 1),
            "saturation_in_tick_units":g*(frontier+1),"endpoints":profiles}


def counts():
    verified=0
    # Independent two-dimensional transfer DP, each occurrence contributes one ordered history.
    tables={(0,0):Counter({ID:1})}
    model={(0,0):ID}
    for L in range(1,3):
        for w in product((0,1),repeat=L):
            k=sum((1 if j%2==0 else -1)*i for j,i in enumerate(w))%3
            model[k,L%2]=endpoint(w)
    model[2,1]=endpoint((0,1,0))
    assert len(set(model.values()))==6
    for i in range(16):
        for j in range(16):
            L=i+j
            pred=Counter()
            if L:
                for u,v,x in ((i-1,j,0),(i,j-1,1)):
                    if u>=0 and v>=0:
                        for h,mass in tables[u,v].items():
                            pred[STEP[h][x]]+=mass
                tables[i,j]=pred
            p=(L+1)//2; q=L//2
            coeffs=Counter()
            for k in range(max(0,j-q),min(j,p)+1):
                coeffs[model[(2*k-j)%3,L%2]]+=comb(p,k)*comb(q,j-k)
            assert coeffs==tables[i,j] and len(coeffs)==1+min(2,i,j)
            if L%2==0:
                # Coefficients of (1+t+t^2)^(L/2), by direct integer multiplication.
                poly=[1]
                for _ in range(L//2):
                    new=[0]*(len(poly)+2)
                    for k,c in enumerate(poly):
                        for step in range(3):new[k+step]+=c
                    poly=new
                delta=(-1)**j*poly[j]
                assert 3*coeffs[ID]==comb(L,j)+2*delta
                assert all(3*coeffs[model[k,0]]==comb(L,j)-delta for k in (1,2))
            verified+=1
    return verified


def main():
    assert STATES[endpoint((0,1))]==(2,0,1) and STATES[endpoint((1,0))]==(1,2,0)
    tested=0
    for a in range(1,22):
        for b in range(a,32):
            integer_model(a,b);tested+=1
    cases=[integer_model(a,b) for a,b in [(3,3),(1,2),(2,3),(3,5),(5,7),(6,9)]]
    print(json.dumps({"actual_slots":{"A":STATES[STEP[ID][0]],"B":STATES[STEP[ID][1]],
                              "A_then_B":STATES[endpoint((0,1))],"B_then_A":STATES[endpoint((1,0))]},
                      "integer_weight_pairs_checked":tested,"fixed_current_pairs_checked":counts(),
                      "examples":cases},sort_keys=True,indent=2))


if __name__=="__main__":
    main()
