"""Cyclic shifts, character spectra, and blind finite receivers. Python 3.9+, stdlib."""
import json
from fractions import Fraction as F
from functools import lru_cache
from itertools import combinations, permutations
from math import gcd, prod

ZERO = (0,0)
ONE = (1,0)
I = (0,1)


def times(a,b):
    return a[0]*b[0]-a[1]*b[1], a[0]*b[1]+a[1]*b[0]


def conj(a):
    return a[0],-a[1]


def add(*terms):
    return sum(t[0] for t in terms),sum(t[1] for t in terms)


def energy(v):
    return F(sum(a*a+b*b for a,b in v),len(v))


def correlation(v,w,h):
    pairs=(times(v[(s+h)%len(v)],conj(x)) for s,x in enumerate(w))
    z=add(*pairs)
    return F(z[0],len(v)),F(z[1],len(v))


def apply(w,v):
    return [add(*(times(t,v[(s+j)%len(v)]) for j,t in enumerate(w))) for s in range(len(v))]


def sumstreams(v,w,h=0):
    return [add(t,w[(s+h)%len(v)]) for s,t in enumerate(v)]


def divisors(n):
    return [d for d in range(1,n+1) if n%d==0]


def primes(n):
    return [d for d in divisors(n) if d>1 and len(divisors(d))==2]


def phi(n):
    return sum(gcd(a,n)==1 for a in range(1,n+1))


def mobius(n):
    pp=primes(n)
    return 0 if any(n%(p*p)==0 for p in pp) else (-1)**len(pp)


def ram(n,h):
    return sum(d*mobius(n//d) for d in divisors(gcd(n,h)))


def trim(p):
    p=p[:]
    while len(p)>1 and p[-1]==0:
        p.pop()
    return p


def divmod_monic(a,b):
    a=trim(a)
    assert b[-1]==1
    quotient=[0]*max(1,len(a)-len(b)+1)
    while len(a)>=len(b) and any(a):
        degree=len(a)-len(b)
        c=a[-1]
        quotient[degree]=c
        for i,v in enumerate(b):
            a[degree+i]-=c*v
        a=trim(a)
    return trim(quotient),a


@lru_cache(None)
def cycl(n):
    p=[-1]+[0]*(n-1)+[1]
    for d in divisors(n)[:-1]:
        p,r=divmod_monic(p,cycl(d))
        assert not any(r)
    return p


def gcd_det(a):
    # Exact Bareiss determinant, with row swaps if a leading entry vanishes.
    a=[r[:] for r in a]
    sign=den=1
    for j in range(len(a)-1):
        k=next((i for i in range(j,len(a)) if a[i][j]),None)
        if k is None:return 0
        if k!=j:
            a[j],a[k]=a[k],a[j]
            sign=-sign
        pivot=a[j][j]
        for r in range(j+1,len(a)):
            for t in range(j+1,len(a)):
                val=a[r][t]*pivot-a[r][j]*a[j][t]
                assert val%den==0
                a[r][t]=val//den
        den=pivot
    return sign*a[-1][-1]


def rational_rank(rows):
    a=[list(map(F,row)) for row in rows]
    lead=0
    for j in range(len(a[0])):
        p=next((k for k in range(lead,len(a)) if a[k][j]),None)
        if p is None:continue
        a[lead],a[p]=a[p],a[lead]
        for k in range(lead+1,len(a)):
            if a[k][j]:
                t=a[k][j]/a[lead][j]
                a[k][j:]=[v-t*w for v,w in zip(a[k][j:],a[lead][j:])]
        lead+=1
    return lead


def shift_rank(channels,complex_weights=False):
    g=len(channels[0])
    rows=[]
    for s in range(g):
        z=[v[(s+j)%g] for v in channels for j in range(g)]
        if complex_weights:z=z+[times(I,x) for x in z]
        rows.extend(([x[0] for x in z],[x[1] for x in z]))
    rank=rational_rank(rows)
    if complex_weights:
        assert rank%2==0
        rank//=2
    return rank


def character(f,q,table):
    return [table.get(s%f,ZERO) if gcd(s,q)==1 else ZERO for s in range(q)]


def single(f,q,table):
    P=prod(p for p in primes(q) if f%p)
    g=f*P
    v=character(f,q,table); u=v[:g]
    assert all(z==u[s%g] for s,z in enumerate(v))
    weights={f*d:F(phi(P)**2,f*P*P*phi(d)**2) for d in divisors(P)}
    corr=[]; variances=[]
    for h in range(g):
        r,i=correlation(u,u,h)
        assert i==0 and r==sum(w*ram(n,h)for n,w in weights.items())
        assert r==F(ram(f,h),f)*prod(F(p-2+int(h%p==0),p) for p in primes(P))
        corr.append(r)
        w=energy(apply([ONE]*h,u))
        rhs=sum(wt*sum(mobius(n//e)*(h%e)*(e-h%e) for e in divisors(n))
                for n,wt in weights.items())
        assert rhs==w
        variances.append(w)
    for a in range(g):
        m=g//gcd(a,g)
        poly=[F(0)]*m
        for h,c in enumerate(corr):
            poly[(a//gcd(a,g)*h)%m]+=c/g
        assert divmod_monic(poly,cycl(m))[1]==[weights.get(m,0)]
    J=f*f*prod(F(p*p-1,p*p)for p in primes(f))
    period_mean=F(J,6*f)*prod(F(2*(p-1),p)for p in primes(P))
    assert sum(variances)/g==period_mean
    wt=[ZERO]*(P*(len(cycl(f))-1)+1)
    for j,c in enumerate(cycl(f)):wt[P*j]=(c,0)
    assert not energy(apply(wt,u))
    return {"modulus":q,"conductor":f,"true_period":g,"gcd_of_period_and_repetition":gcd(g,q//g),
            "order_to_energy_per_frequency":{str(n):str(w) for n,w in weights.items()},
            "variance_at_window_six":str(variances[6%g]),"mean_over_windows":str(period_mean)}


LEG3={1:ONE,2:(-1,0)}
LEG5={1:ONE,2:(-1,0),3:(-1,0),4:ONE}
QUART5={1:ONE,2:I,3:(0,-1),4:(-1,0)}
Q4={1:ONE,3:(-1,0)}
Q8={1:ONE,3:(-1,0),5:(-1,0),7:ONE}


def two_real():
    a,b=character(3,15,LEG3),character(5,15,LEG5)
    for h in range(15):
        c=times(LEG3.get(h%3,ZERO),LEG5.get((-h)%5,ZERO))
        assert correlation(a,b,h)==(F(c[0],15),0)
        assert correlation(a,b,h)[0]==-correlation(a,b,-h)[0]
    for m in range(1,16):
        assert correlation(apply([ONE]*m,a),apply([ONE]*m,b),0)==ZERO
    minor=[[v[(s+j)%15][0] for v in (a,b) for j in range(7)] for s in range(14)]
    assert gcd_det(minor)==-2560
    w1=[1,2,1,1,1,0,-1,-2]; w2=[-1,0,1,1,1,2,1,0]
    y=apply([(i,0)for i in w1],a); z=apply([(i,0)for i in w2],b)
    assert all(k==ZERO for k in sumstreams(y,z)) and energy(y)==energy(z)==F(34,15)
    independent=F(sum((i+k)**2+(j+l)**2 for i,j in y for k,l in z),225)
    assert independent==F(68,15)
    measurements=[energy(sumstreams(y,z,t)) for t in range(15)]
    assert min(measurements[1:])==F(22,15)
    gaps={}
    for shift in range(1,8):
        codes=[(measurements[t],measurements[(t+shift)%15]) for t in range(15)]
        gap,i,j=min((max(abs(x-y) for x,y in zip(codes[i],codes[j])),i,j)
                    for i,j in combinations(range(15),2))
        gaps[str(shift)]={"gap":str(gap),"distinct_pairs":len(set(codes)),"nearest_offsets":[i,j]}
    assert gaps["5"]["gap"]=="4/5" and max(F(x["gap"]) for x in gaps.values())==F(4,5)
    ranks=[shift_rank([a]),shift_rank([b]),shift_rank([a,b])]
    assert ranks==[10,12,14]
    offset_law=[F(1,15)+F(ram(3,t),30) for t in range(15)]
    assert sum(offset_law)==1 and min(offset_law)>0
    mixed=[sum(p*measurements[(s+t)%15] for t,p in enumerate(offset_law))for s in range(15)]
    assert set(mixed)=={independent}
    rank=rational_rank([[measurements[(s+t)%15]for t in range(15)]for s in range(15)])
    assert rank==9
    return {"full_cyclic_rational_ranks":ranks,"energy_scan_rank_including_mass":rank,
            "indistinguishable_nonuniform_offset_law":[str(p) for p in offset_law],
            "first_true_cancellation_max_delay":7,"delay6_minor":-2560,
            "weights":[w1,w2],"channel1_filtered_trace":[t[0] for t in y],
            "individual_energy":"34/15","independent_energy":str(independent),
            "common_offset_energies_times_15":[int(x*15) for x in measurements],
            "two_control_delay_gaps":gaps}


def complex_det_square(a):
    ans=ZERO
    for perm in permutations(range(len(a))):
        z=ONE
        for j,k in enumerate(perm):z=times(z,a[j][k])
        inv=sum(i>j for i,j in combinations(perm,2))
        ans=add(ans,times(((-1)**inv,0),z))
    return ans


def quartic():
    a=character(5,5,QUART5);b=list(map(conj,a))
    assert all(correlation(a,a,h)==correlation(b,b,h) for h in range(5))
    e1=F(sum(a[s]==ZERO and a[(s+2)%5]==I for s in range(5)),5)
    e2=F(sum(b[s]==ZERO and b[(s+2)%5]==I for s in range(5)),5)
    assert (e1,e2)==(F(1,5),0)
    mat=[[v[(s+j)%5]for v in (a,b) for j in range(2)]for s in range(4)]
    assert complex_det_square(mat)==(-4,0)
    v=apply([(-2,4),(-1,2),(-2,4)],a)
    w=apply([ZERO,(5,0),ZERO],b)
    assert energy(v)==energy(w)==20 and all(z==ZERO for z in sumstreams(v,w))
    rat=shift_rank([a,b]);comp=shift_rank([a,b],complex_weights=True)
    assert (rat,comp)==(8,4)
    return {"character":"chi(2)=i mod 5 and conjugate","delay1_complex_minor":-4,
            "shortest_complex_max_delay":2,"separate_filtered_energy":20,
            "rational_receiver_rank_mod_shifts":rat,"complex_receiver_rank_mod_shifts":comp,
            "calibrated_two_time_event_probability":[str(e1),str(e2)]}


if __name__=="__main__":
    cases=[single(4,288,Q4),single(5,2250,QUART5),single(8,1600,Q8)]
    print(json.dumps({"induced_checks":cases,"shared_mod_15":two_real(),"quartic_mod_5":quartic()},
                     ensure_ascii=False,indent=2))
