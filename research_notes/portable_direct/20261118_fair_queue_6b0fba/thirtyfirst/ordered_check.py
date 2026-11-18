"""Independent integer expansion of the public three-port model and binary collision criteria."""
import json
from collections import Counter,defaultdict
from itertools import product
from math import gcd


def record_paths(T):
    """Expand all port words into (record, complete final key) BEFORE taking squares."""
    v=defaultdict(Counter)
    for word in product(range(3),repeat=T):
        count=[0]*3
        prev=0;q=0; amp=1
        for j,p in enumerate(word):
            count[p]+=1
            q|=(p==1)<<j
            amp*=(-1 if p==prev else 2)
            prev=p
        v[q][(*count,prev)]+=amp
    return v


def full_model(N,a,T):
    """Independent work-aware update, without a trigger register."""
    states={(0,0,0,0,1):1}
    mod=a%N
    for _ in range(T):
        nxt=Counter()
        for (c0,c1,c2,i,w),amp in states.items():
            for p in range(3):
                key=(c0+(p==0),c1+(p==1),c2+(p==2),p,w*mod%N if p==1 else w)
                nxt[key]+=amp*(-1 if p==i else 2)
        states=nxt
        mod=mod*mod%N
    out=Counter()
    for (*b,w),v in states.items():out[tuple(b)]+=v*v
    return out


def order(N,a):
    assert N>=2 and gcd(a,N)==1
    x=a%N;n=1
    while x!=1:x=x*a%N;n+=1
    return n


def split_order(d):
    v=(d&-d).bit_length()-1
    return v,d>>v


def first(d):
    v,e=split_order(d)
    k=e.bit_length()
    return v+k+int((1<<k)-1-e < (1<<e.bit_count()))


def collisions(d,m):
    seen=Counter((x%d,x.bit_count()) for x in range(1<<m))
    return sum(v*(v-1) for v in seen.values())


def count_by_polynomial(d,m):
    p={(0,0):1}
    for t in range(m):
        new=Counter()
        for (r,z),c in p.items():
            new[r,z]+=2*c
            for s in (-1,1):new[(r+s*(1<<t))%d,z+s]+=c
        p=new
    return p[0,0]-(1<<m)


def boundary_excess(d,T):
    """On no-port-2 all amplitudes for a given terminal key have one common sign."""
    hits=defaultdict(lambda:[0,0])
    for q in range(1<<T):
        last=q>>(T-1)
        c=(q^(q<<1)).bit_count()-last
        m=1<<c
        key=(q.bit_count(),last,q%d)
        hits[key][0]+=m
        hits[key][1]+=m*m
    assert sum(a[1] for a in hits.values())==5**T
    return sum(x*x-y for x,y in hits.values())


def compare(N,T,paths,a=2):
    d=order(N,a)
    exact=full_model(N,a,T)
    joint=defaultdict(list);fresh=Counter()
    for q,vs in paths.items():
        for b,v in vs.items():
            joint[b,pow(a,q,N)].append(v);fresh[b]+=v*v
    delta=Counter()
    upper=0
    for (b,w),vs in joint.items():
        ordered=sum(x*y for k,x in enumerate(vs) for l,y in enumerate(vs) if k!=l)
        assert ordered==sum(vs)**2-sum(v*v for v in vs)
        delta[b]+=ordered
        upper+=sum(abs(v) for v in vs)**2-sum(v*v for v in vs)
    assert all(fresh[b]+delta[b]==exact[b] for b in set(fresh)|set(exact))
    assert sum(fresh.values())==sum(exact.values())==9**T and sum(delta.values())==0
    boundary=sum(v for b,v in delta.items() if b[2]==0)
    assert boundary==boundary_excess(d,T)
    tv=sum(abs(x) for x in delta.values())//2
    C=collisions(d,T-1)
    assert (tv>0)==(C>0)==(boundary>0) and boundary>=32*C
    return {"N":N,"T":T,"order":d,"first_nonzero_T":first(d)+1,"ordered_prefix_pairs":C,
            "TV_numerator_over_9T":tv,"absolute_bound_numerator_over_9T":upper//2,
            "no_port2_excess_numerator_over_9T":boundary}


def main():
    example=record_paths(3)
    assert example[0][2,0,1,0]==-8
    checks=[]; arithmetic=0
    for T in (4,5,6,7):
        paths=record_paths(T)
        for N in (21,35,77):
            checks.append(compare(N,T,paths))
    T6=[(r["TV_numerator_over_9T"],r["absolute_bound_numerator_over_9T"]) for r in checks if r["T"]==6]
    assert T6==[(80576,122112),(33280,39296),(0,0)]
    sharp=compare(3,3,example,a=1)
    assert sharp["no_port2_excess_numerator_over_9T"]==64 and sharp["ordered_prefix_pairs"]==2
    for d in range(1,1025):
        m=first(d)
        assert not collisions(d,m-1) and collisions(d,m)>0
        v,e=split_order(d)
        assert collisions(d,m)==(1<<v)*collisions(e,m-v)
        arithmetic+=1
    for d in range(1,31):
        for m in range(9):
            assert collisions(d,m)==count_by_polynomial(d,m)
    exceptional=[];f0,f1=0,1
    for k in range(1,17):
        num=sum(first(e)==k+1 for e in range((1<<(k-1))|1,1<<k,2))
        assert num==f1
        exceptional.append(num);f0,f1=f1,f0+f1
    families=[]
    for sign,start in [(-1,2),(1,3)]:
        for k in range(start,9):
            for v in range(3):
                e=(1<<k)+sign;d=e<<v;m=k+1+v
                assert first(d)==m
                n=(1<<(k-1)) if sign==-1 else (1<<(k-3))
                value=128*5**(k-2) if sign==-1 else (64 if k==3 else 512*5**(k-4))
                assert collisions(d,m)==2*(1<<v)*n
                assert boundary_excess(d,m+1)==value*5**v
                families.append((d,m+1,n*(1<<v),value*5**v))
    print(json.dumps({"regressions":checks,"same_record_T3_amplitude":-8,"boundary_lower_bound_equality":sharp,
                      "first_collisions_by_direct_enumeration_orders_through":arithmetic,
                      "delayed_odd_orders_by_bit_length":exceptional,
                      "near_power_family_samples":len(families),"group_ring_count_checks":30*9},
                     sort_keys=True,indent=2))


if __name__=="__main__":
    main()
