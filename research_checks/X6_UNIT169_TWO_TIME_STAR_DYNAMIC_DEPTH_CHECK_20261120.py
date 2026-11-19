"""X6 Unit169: exact dynamic depth recovery from source-consistent K4 STAR observers.
Frozen science: 59538f585d037d09ef687b28715c4bc1a3f9fe03.
Frozen historical comparison: fd2bcff10ca6e147348b6c1236027fc0d2877df3.
This is an algebraic signed-coordinate graph automorphism, not a physical rotation.
"""
import itertools
import json
from collections import Counter
from math import factorial

EDGES = tuple(itertools.combinations(range(4),2))
STARS = tuple(tuple(i for i,e in enumerate(EDGES) if v in e) for v in range(4))
D = (1,)*6

def check(flag, msg):
    if not flag:
        raise AssertionError(msg)

def rotor(z):
    return (-z[-1],)+z[:-1]

def rotate(z,k):
    for _ in range(k%12): z=rotor(z)
    return z

def can(z):
    m=min(z)
    return tuple(v-m for v in z)

def star_obs(z,S):
    return can(tuple(z[i] for i in S))

def recover_three_stars(z,family):
    observations=[star_obs(z,S) for S in family]
    adj=[set() for _ in range(6)]
    for S,v in zip(family,observations):
        for i,j in itertools.combinations(range(3),2):
            a,b=S[i],S[j];delta=v[j]-v[i]
            adj[a].add((b,delta));adj[b].add((a,-delta))
    todo=[0];p={0:0}
    while todo:
        i=todo.pop()
        for j,delta in adj[i]:
            val=p[i]+delta
            if j in p:check(p[j]==val,'inconsistent three-star observations')
            else:p[j]=val;todo.append(j)
    check(len(p)==6,'three-star graph disconnected')
    return can(tuple(p[i] for i in range(6)))

def brc(z):
    v=sum(abs(a) for a in z)
    p=factorial(v)
    for a in z:p//=factorial(abs(a))
    return p

def observed_depth(r,k,S,actual_obs):
    ak=rotate(r,k);ad=rotate(D,k)
    indices=[(i,j) for i,j in itertools.combinations(range(3),2) if ad[S[i]]!=ad[S[j]]]
    if not indices:return None
    i,j=indices[0]
    numerator=actual_obs[i]-actual_obs[j]-(ak[S[i]]-ak[S[j]])
    denominator=ad[S[i]]-ad[S[j]]
    check(abs(denominator)==2,'rotor diagonal difference != 2')
    check(numerator%denominator==0,'second read does not admit integer depth')
    return numerator//denominator

def run():
    check(STARS==((0,1,2),(0,3,4),(1,3,5),(2,4,5)),'K4 star order')
    family=STARS[:3]
    cases=0; effective=Counter(); bad=0; native_mass=0
    all_configs=[]
    for k in range(12):
        ad=rotate(D,k)
        for si,S in enumerate(STARS):
            crossed=len({ad[i] for i in S})>1
            effective[(k,si)]=crossed
            all_configs.append({'k':k,'star':si,'depth_visible':crossed})
    for k in range(12):
        for si,S in enumerate(STARS):
            expected=effective[(k,si)]
            u0=star_obs((0,)*6,S)
            ud=star_obs(rotate(D,k),S)
            check((u0!=ud)==expected,'sharp zero/diagonal witness wrong')
    for z in itertools.product(range(-2,3),repeat=6):
        r=recover_three_stars(z,family)
        check(r==can(z),'initial three-star recovery')
        true_h=min(z)
        for k in range(12):
            actual=rotate(z,k)
            for si,S in enumerate(STARS):
                v=star_obs(actual,S)
                restored_h=observed_depth(r,k,S,v)
                visible=effective[(k,si)]
                check((restored_h is not None)==visible,'depth effect mismatch')
                if visible:
                    check(restored_h==true_h,'depth reconstruction mismatch')
                    restored=tuple(a+restored_h for a in r)
                    check(restored==z,'full signed Cell restoration mismatch')
                    check(brc(restored)==brc(z),'native BRC multiplicity mismatch')
                    native_mass+=1
                else:
                    check(star_obs(rotate(tuple(a+true_h+1 for a in r),k),S)==v,'hidden one-depth alias failure')
                cases+=1
    counts={str(k):sum(effective[(k,si)] for si in range(4)) for k in range(12)}
    check(counts=={'0':0,'1':2,'2':3,'3':3,'4':3,'5':2,'6':0,'7':2,'8':3,'9':3,'10':3,'11':2},'visibility table')
    return {'schema':'X6_UNIT169_TWO_TIME_K4_STAR_DYNAMIC_DEPTH_CERT_V1',
        'historical_pin':'fd2bcff10ca6e147348b6c1236027fc0d2877df3',
        'scientific_pin':'59538f585d037d09ef687b28715c4bc1a3f9fe03',
        'observer':'can3 of labeled signed X6 coordinate triple, three of four K4 STARs at time 0; one STAR after A^k',
        'rotor':'A(x1,..,x6)=(-x6,x1,..,x5), A^6=-I, A^12=I',
        'star_axis_subsets':[list(s) for s in STARS],
        'second_star_visibility_counts_by_k':counts,
        'distinct_second_star_cases':len(all_configs),
        'effective_cases':sum(effective.values()),
        'ineffective_cases':sum(not v for v in effective.values()),
        'tested_raw_vectors':5**6,
        'tested_dynamic_observation_instances':cases,
        'successful_full_depth_brc_restorations':native_mass,
        'violations':bad,
        'original_R063_benchmark_rerun':False,
        'independent_review':'UNREVIEWED_NOT_ADMITTED',
        'scope':'SIGNED_X6_CANDIDATE_GRAPH_AUTOMORPHISM_NOT_A_NATIVE_PHYSICAL_ROTATION'}

if __name__=='__main__':
    print(json.dumps(run(),ensure_ascii=False,sort_keys=True,separators=(',',':')))
