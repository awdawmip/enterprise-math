"""Unit61, exact signed X6 two-step detour and native/P022 typing check.
Author-side new math: all operations exact Python integers; no imported project code.
"""
from __future__ import annotations
from collections import defaultdict
from functools import lru_cache
from math import factorial
import json

D=6

def require(condition, label):
    if not condition:
        raise AssertionError(label)

def paths_shortest(z):
    t=sum(abs(x) for x in z)
    out=factorial(t)
    for x in z: out//=factorial(abs(x))
    return out

def paths_excess2(z):
    """Independent direct M=T+2 factorial sum over the one backtrack axis."""
    a=[abs(x) for x in z]
    t=sum(a)
    f=factorial(t+2)
    den=1
    for x in a:den*=factorial(x)
    return sum(f//(den*(x+1)) for x in a) # each denominator divides f for these dimensions

def paths_excess2_rational(z):
    """Different exact recurrence via factorial multinomials and integer scaling."""
    a=[abs(x) for x in z]
    t=sum(a)
    n=paths_shortest(z)
    w=(t+2)*(t+1)*n
    # Avoid fractions by product of (a_i+1); same integer via common denominator.
    p=1
    for x in a:p*=x+1
    s=sum(p//(x+1) for x in a)
    require((w*s)%p==0, "detour division not integral")
    return w*s//p

def signed_G_shell(g):
    # Enumerate signed six-axis endpoints with quadratic readout g, no projected slice.
    def rec(prefix, rem):
        if len(prefix)==D:
            if rem==0: yield tuple(prefix)
            return
        for a in range(int(rem**0.5)+1):
            q=a*a
            for x in ((0,) if a==0 else (-a,a)):
                yield from rec(prefix+[x], rem-q)
    return rec([],g)

@lru_cache(None)
def recurrence(m,z):
    if m == 0: return int(all(v==0 for v in z))
    if sum(abs(v) for v in z)>m or (m-sum(abs(v) for v in z))%2:return 0
    total=0
    for i in range(D):
        for sign in (-1,1):
            zz=list(z); zz[i]-=sign
            total+=recurrence(m-1,tuple(zz))
    return total

def independent_orbit_g25():
    # Nondecreasing magnitude multisets (positive entries), independently embed axes.
    from collections import Counter
    from math import comb
    result=defaultdict(lambda:[0,0,0])
    def rec(mags, start, left):
        if left==0:
            support=len(mags); mult=Counter(mags)
            embeddings=1
            for i in range(support):embeddings*=D-i
            embeddings*=2**support
            for n in mult.values():embeddings//=factorial(n)
            z=tuple(mags)+(0,)*(D-support)
            t=sum(mags)
            v0=paths_shortest(z)
            v2=paths_excess2_rational(z)
            key=(t,support)
            result[key][0]+=embeddings
            result[key][1]+=embeddings*v0
            result[key][2]+=embeddings*v2
            return
        if len(mags)==D:return
        for a in range(start,int(left**0.5)+1):
            yield from rec(mags+[a],a,left-a*a)
    list(rec([],1,25))
    return {f'T{t}_s{s}': val for (t,s),val in sorted(result.items())}

def main():
    samples=[(0,)*6,(1,0,0,0,0,0),(1,1,0,0,0,0),(-1,0,0,1,0,0),
             (2,1,0,0,0,0),(1,1,1,0,0,0),(3,0,0,-4,0,0)]
    out_samples=[]
    for z in samples:
        t=sum(abs(v) for v in z)
        a=paths_excess2(z);b=paths_excess2_rational(z)
        require(a==b, f"detour formula mismatch {z} {a} {b}")
        if t+2<=6:
            c=recurrence(t+2,z)
            require(a==c, f"independent recursion mismatch {z} {a} {c}")
        out_samples.append({'z':list(z),'G':sum(v*v for v in z),'T':t,
                            'N_T':paths_shortest(z),'N_T_plus_2':a,
                            'independent_word_recurrence':recurrence(t+2,z) if t+2<=6 else None})
    agg=defaultdict(lambda:[0,0,0])
    for z in signed_G_shell(25):
        key=f'T{sum(abs(v) for v in z)}_s{sum(v!=0 for v in z)}'
        vals=agg[key]
        vals[0]+=1;vals[1]+=paths_shortest(z); vals[2]+=paths_excess2(z)
    agg=dict(sorted(agg.items()))
    independent=independent_orbit_g25()
    require(agg==independent, "signed endpoint and orbit census differ")
    total=[sum(z[i] for z in agg.values()) for i in range(3)]
    require(total[:2]==[7812,2538954612], "unit58 baseline mismatch")
    # Source-controlled formula S(5,k) from published P022 producer, checked algebraically.
    # P022 L1 shell at T=5, d=6: sum C(d,k)*2^k*k!*Stirling(5,k).
    from math import comb
    stirling={1:1,2:15,3:25,4:10,5:1}
    p022_l1=sum(comb(D,k)*2**k*factorial(k)*stirling[k] for k in range(1,6))
    require(p022_l1==106452, "P022 L1 baseline mismatch")
    data={'schema':'X6_LP019_UNIT61_TWO_STEP_DETOUR_EXACT_V1',
          'scientific_pin':'awdawmip/enterprise-math@59538f585d037d09ef687b28715c4bc1a3f9fe03',
          'P000_type':'signed X6 Cell displacement; pure coordinate adjacency',
          'claims':'N_{T+2}(z)=N_T(z)*(T+1)*(T+2)*sum_i 1/(|z_i|+1)',
          'source_api_names':['signed_brc.shortest_path_multiplicity','signed_brc.endpoint_multiplicity','p022_geodesic_multiplicity.sc_geodesic_path_count','p022_geodesic_multiplicity.sc_shell_total_geodesic_paths'],
          'source_api_executed':False,
          'samples':out_samples,
          'G25_by_T_support':agg,
          'G25_all':{'endpoints':total[0],'N_T_mass':total[1],'N_T_plus_2_mass':total[2]},
          'P022_T5_mass':p022_l1,
          'crosscheck':'enumerate all signed quadratic-shell endpoints and independent orbit-partition counting; direct factorial detour + common denominator + word recurrence on small cases',
          'project_admission':'UNREVIEWED_NOT_ADMITTED'}
    print(json.dumps(data,ensure_ascii=False,indent=2))

if __name__=='__main__':main()
