#!/usr/bin/env python3
"""R267 independent exact six-class priced zero-only observer verification.
Scientific pin: 43ec6098b1330ae86d0a7863be336c5d97f6ef34.
Derives all 63 source supports from exact seven-source rational model.
"""
import json
from collections import defaultdict
from fractions import Fraction as F
from itertools import permutations,combinations
from pathlib import Path

s=F(67,169);J=1184397599;T=989553240;K=3805974000
prime=13;period=2184
reps=(9,10,12,13,24,26)
w=(144,576,1440,4320,17280,86400,518400)

def times(poly,root):
    z=[F(0)]*(len(poly)+1)
    for i,v in enumerate(poly):z[i]-=v*root;z[i+1]+=v
    return z

def cp(ids,a,b):
    p=[F(1)]
    for i in ids:p=times(p,a[i])
    for i in ids:
        q=[F(1)]
        for j in ids:
            if j!=i:q=times(q,a[j])
        for j,v in enumerate(q):p[j]-=b[i]*v
    return p

def supports():
    t=(1691*s-2615)/(2615*s-3539)
    a=[F(1,5),F(1,4),F(3,10),F(9,20),s,F(2,3),t]
    b=[F(13,60)]+[F(5,18)*abs(F(1,2)-a[i]) for i in range(1,7)]
    pi=[b[i]/(1-a[i]) for i in range(7)]
    z=sum(b[i]/(1-a[i])**2 for i in range(7))
    rho=[b[i]/(z*(1-a[i])**2) for i in range(7)]
    assert sum(pi)==1
    profiles={};taps=0
    for m in range(63):
        ids=[0]+[i+1 for i in range(6) if (m>>i)&1]
        d=len(ids);taps+=d
        pol=[c*T**(d-i) for i,c in enumerate(cp(ids,a,b))]
        assert all(c.denominator==1 for c in pol)
        coeff=[int(c)%prime for c in pol]
        state=[F(1)]*d;seq=[]
        for k in range(3+d):
            if k>=3:
                q=F(J*T**k,K)*w[m.bit_count()]*sum(rho[i]*state[j] for j,i in enumerate(ids))
                assert q.denominator==1
                seq.append(int(q)%prime)
            total=sum(pi[i]*state[j] for j,i in enumerate(ids))
            state=[a[i]*state[j]+(1-a[i])*total for j,i in enumerate(ids)]
        for n in range(d,period+d):
            seq.append(-sum(coeff[j]*seq[n-d+j] for j in range(d))%prime)
        assert seq[:d]==seq[period:period+d]
        profiles[m]=sum(1<<i for i in range(period) if seq[i])
    assert taps==249
    groups=defaultdict(list)
    for m,b in profiles.items():groups[b].append(m)
    assert len(groups)==7 and len(groups[0])==39
    assert sorted(min(v) for k,v in groups.items() if k)==list(reps)
    return profiles,groups,taps

def paths(covers):
    union=0
    for c in covers.values():union|=c
    assert union.bit_count()==2182
    distinct={}
    for p in permutations(reps):
        remain=(1<<period)-1;vec=[0]*6;seq=[]
        for j in p:
            i=reps.index(j)
            vec[i]=remain.bit_count()
            seq.append(j)
            remain &=~covers[j]
            if (remain&union)==0:break
        key=tuple(vec)
        if key not in distinct or tuple(seq)<distinct[key]:distinct[key]=tuple(seq)
    items=list(distinct)
    nd=[]
    for u in items:
        if not any(v!=u and all(v[i]<=u[i] for i in range(6)) for v in items):nd.append(u)
    lines={}
    for vec in nd:
        a=sum(vec[i] for i in range(6) if i not in (0,5))
        b,c=vec[0],vec[5]
        key=(a,b,c)
        if key not in lines or distinct[vec]<lines[key]:lines[key]=distinct[vec]
    return distinct,nd,lines

def onecost_sanity(lines):
    for x,y,cost in [(F(1),F(1),2356),(F(169,168),F(1),F(172)+2184*F(169,168)),(F(15,14),F(1),F(2380)),(F(2),F(1),2380)]:
        assert min(a+b*x+c*y for a,b,c in lines)==cost

def solve_dp(covers,costs):
    u=0
    for k in reps:u|=covers[k]
    U=[0]*64
    for S in range(1,64):
        bit=S&-S;i=bit.bit_length()-1;U[S]=U[S^bit]|covers[reps[i]]
    Fv=[0]*64;choice=[None]*64
    for S in range(63,-1,-1):
        if U[S]==u:continue
        m=period-U[S].bit_count()
        arr=[(costs[i]*m+Fv[S|1<<i],reps[i]) for i in range(6) if not (S>>i)&1]
        Fv[S],choice[S]=min(arr)
    S=0;order=[]
    while choice[S] is not None:
        j=choice[S];order.append(j);S|=1<<reps.index(j)
    return Fv[0],order

def run():
    cov,groups,taps=supports()
    distinct,nd,lines=paths(cov)
    onecost_sanity(lines)
    grid=[F(1),F(101,100),F(169,168),F(21,20),F(15,14),F(6,5),F(3,2),F(2),F(3),F(5),F(10),F(100)]
    verified=0;sample=[]
    for x in grid:
        for y in grid:
            costs=(x,F(1),F(1),F(1),F(1),y)
            dval,order=solve_dp(cov,costs)
            rval=min(a+b*x+c*y for (a,b,c) in lines)
            aval=min(sum(vec[i]*costs[i] for i in range(6)) for vec in distinct)
            assert dval==rval==aval,(x,y,dval,rval,aval)
            verified+=1
            if x in [F(1),F(2),F(10)] and y in [F(1),F(2),F(10)]:sample.append([str(x),str(y),str(dval),order])
    firsts={}
    for i,m in enumerate(reps):
        costs=tuple(F(1) if j==i else F(10**6) for j in range(6))
        val,order=solve_dp(cov,costs)
        firsts[m]={'cost':str(val),'order':order}
    cert={
      'schema':'R267_SIX_CLASS_EXACT_POSITIVE_COST_CONE_V1',
      'scientific_pin':'43ec6098b1330ae86d0a7863be336c5d97f6ef34',
      's':'67/169','prime':13,'k_start':3,'period':period,
      'recurrence_shift_taps_verified':taps,
      'active_representatives':list(reps),
      'support_class_sizes':[len(groups[cov[m]]) for m in reps],
      'all_zero_events':period-sum(1 for i in range(period) if any(cov[m]&(1<<i) for m in reps)),
      'ordered_paths_total':720,'distinct_full_six_price_vectors':len(distinct),
      'pareto_minimal_cost_vectors':len(nd),'two_parameter_distinct_lines':len(lines),
      'two_parameter_grid_exact_crosschecks':verified,
      'two_parameter_samples':sample,
      'first_probe_under_one_cheap_class':firsts,
      'theorem':'For strictly positive six class costs c, exact F(c)=min_{v in ParetoVectors} dot(v,c); the recorded Pareto vectors are an exhaustive finite cost-coefficient certificate; every integer k>=3 inherits support period by monic recurrences.',
      'limits':'Boolean all-zero original-label oracle; no native signed BRC-port equivalence; no independent mathematical review.',
      'full_vectors':[{'counts':list(v),'order':list(distinct[v])} for v in sorted(nd)],
      'two_parameter_lines':[{'a':a,'b9':b,'b26':c,'order':list(o)} for (a,b,c),o in sorted(lines.items())],
    }
    dest=Path(__file__).with_name('R267_verification.json')
    dest.write_text(json.dumps(cert,ensure_ascii=False,sort_keys=True,indent=2)+'\n')
    print('PASS',{k:cert[k] for k in ['distinct_full_six_price_vectors','pareto_minimal_cost_vectors','two_parameter_distinct_lines','two_parameter_grid_exact_crosschecks','all_zero_events']})
    print('SAMPLES',sample)
    print('CHEAP',firsts)
    return cert

if __name__=='__main__':run()
