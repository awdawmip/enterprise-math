#!/usr/bin/env python3
"""Exact finite evidence for the complete irredundant zero-W nine-cover theorem.

The all-prime reductions are proved in proof.md. This standard-library checker
verifies complete order inventories, finite geometries and their full periods,
counts, and exact-cost-nine CRT examples. It makes no native BRC execution claim.
"""
from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction as F
from functools import lru_cache
from itertools import combinations
import json
from math import gcd,isqrt,lcm,prod
from pathlib import Path

HERE=Path(__file__).resolve().parent
A={1,2,10,11,12,16,17,22,25,26,30,31,32}
ROWS=(1,2,3,4,5)
Z=(29,43,1429,5419)
J=(3361,15790321,88959882481)
K=(92737,649657,77158673929,40388473189,118750098349)
T=(61681,4562284561)
L=(2017,5153,25629623713,54410972897,1538595959564161)
V=(127681,1130641,755667361,84179842077657862011867889681,
   54169520413224311136354324156824071681)
U=(211,421,86171,106681,122921,152041,664441,1564921,
   7416361,47392381,146919792181,1041815865690181)
S=T+V
GROUPS={'Z':Z,'J':J,'K':K,'T':T,'L':L,'V':V,'U':U,'S':S}
PERIOD={q:f for group,f in ((Z,7),(J,14),(K,21),(T,10),(L,28),(V,70),(U,35)) for q in group}
P=(7,17,31,41,71,97,113,127,151,241,257,281,337,641,673,1321,14449,29191,65537,6700417)
A3=191972202303719298729928918311723396431844443114656289541489997722900148740095048143165366560585581706728525286370671799498153425353200109163
S3=398569978187125493241348981737346491702787412670647652655838012662365320990659421311257378134104419105098635600781280382381386713746554859390
B8=(193,1153,6337,22253377,38941695937,278452876033)
D6=(33975937,138991501037953)
C10=(61681,4562284561,168692292721,469775495062434961)
T8=tuple(sorted(set(B8+D6+C10+Z+J+U)))


def prime_trial(n):
    return n>=2 and all(n%d for d in range(2,isqrt(n)+1))


def factors(n):
    out=[];p=2
    while p*p<=n:
        if n%p==0:
            out.append(p)
            while n%p==0:n//=p
        p+=1
    if n>1:out.append(n)
    return out


def exact_order(q,d):
    return pow(2,d,q)==1 and all(pow(2,d//p,q)!=1 for p in factors(d))


@lru_cache(None)
def phi2(d):
    x=(1<<d)-1
    for e in range(1,d):
        if d%e==0:x//=phi2(e)
    return x


def verify_inventory():
    data=json.loads((HERE/'prime_inventory.json').read_text())
    certs=data['certificates'];verified=set()
    def verify(q):
        if q in verified:return
        c=certs[str(q)]
        if c['kind']=='trial':assert prime_trial(q)
        else:
            assert c['kind']=='lucas_n_minus_one'
            fac={int(p):int(e) for p,e in c.get('factorization',c.get('factors')).items()}
            assert prod(p**e for p,e in fac.items())==q-1
            for p in fac:verify(p)
            w=c['witness']
            assert pow(w,q-1,q)==1
            assert all(gcd(pow(w,(q-1)//p,q)-1,q)==1 for p in fac)
        verified.add(q)
    actual={f:set() for f in (7,8,10,14,21,28,35,70)}
    rows=data['complete_effective_order_factorizations']
    for row in rows:
        d=row['order'];f=row['effective_v_period']
        fac={int(p):int(e) for p,e in row['factors'].items()}
        assert phi2(d)==int(row['value'])==prod(p**e for p,e in fac.items())
        assert d//gcd(d,12)==f
        for q in fac:
            verify(q)
            if exact_order(q,d) and gcd(q,S3)==1:actual[f].add(q)
    expected={7:set(Z),8:{193,22253377},10:set(T),14:set(J),21:set(K),28:set(L),35:set(U),70:set(V)}
    assert actual==expected
    for f in actual:
        orders={f*g for g in (1,2,3,4,6,12) if gcd(f*g,12)==g}
        assert orders=={r['order'] for r in rows if r['effective_v_period']==f}
    return {'verified_prime_nodes':len(verified),'cyclotomic_values':len(rows),
            'effective_order_inventories':{str(k):sorted(v) for k,v in actual.items()}}


def falling(n,k):return prod(range(n-k+1,n+1))


def phase_count(slots):
    count=Counter(g for g,b in slots)
    return prod(falling(len(GROUPS[g]),k) for g,k in count.items())


def cube_matchings():
    vertices={v for v in range(70) if v%35 in A and v%7 in (1,5)}
    assert len(vertices)==8
    edges=[]
    for group,f in (('T',10),('J',14),('U',35)):
        for b in range(f):
            points=frozenset(v for v in vertices if v%f==b)
            if len(points)==2:edges.append((group,b,points))
    found=[]
    def visit(left,chosen):
        if not left:
            found.append(tuple(sorted((g,b) for g,b,_ in chosen)));return
        v=min(left)
        for edge in edges:
            if v in edge[2] and edge[2]<=left:visit(left-edge[2],chosen+[edge])
    visit(vertices,[])
    found=sorted(set(found));assert len(found)==9
    accepted=[x for x in found if all(Counter(g for g,b in x)[g]<=len(GROUPS[g]) for g in ('T','J','U'))]
    assert len(accepted)==7
    return found,accepted


def patterns():
    out=[]
    def add(kind,slots,**metadata):
        assert len(slots)==7
        out.append({'type':kind,'slots':slots,**metadata})
    for c in ROWS:
        zz=[('Z',b) for b in ROWS if b!=c]
        add('I',zz+[('K',c),('K',c+7),('K',c+14)],remaining_row=c)
    for big in (2,3,4):
        for small in (1,5):
            zz=[('Z',b) for b in ROWS if b not in (big,small)]
            pp=sorted(v for v in A if v%7==small)
            add('II',zz+[('J',big),('J',big+7)]+[('U',v) for v in pp],remaining_rows=[big,small])
    all_cube,good_cube=cube_matchings()
    for matching in good_cube:add('III',[('Z',b) for b in (2,3,4)]+list(matching),cube_matching=matching)
    for c in ROWS:
        zz=[('Z',b) for b in ROWS if b!=c]
        for half in (c,c+7):
            other=c+7 if half==c else c
            add('IV',zz+[('J',half),('L',other),('L',other+14)],remaining_row=c)
    for c in (2,3,4):
        zz=[('Z',b) for b in ROWS if b!=c]
        add('V',zz+[('U',v) for v in sorted(A) if v%7==c],remaining_row=c)
    for c in (1,5):
        zz=[('Z',b) for b in ROWS if b!=c]
        pp=sorted(v for v in A if v%7==c)
        for half in (c,c+7):
            opposite={v:next(t for t in (v,v+35) if t%14!=half) for v in pp}
            add('VI',zz+[('J',half)]+[('S',opposite[v]) for v in pp],remaining_row=c)
            for whole in pp:
                other=next(v for v in pp if v!=whole)
                add('VII',zz+[('J',half),('U',whole),('S',opposite[other])],remaining_row=c)
        for whole in pp:
            other=next(v for v in pp if v!=whole)
            add('VIII',zz+[('U',whole),('S',other),('S',other+35)],remaining_row=c)
    assert len(out)==47
    return out


def assignments_for_shape(slots):
    used=set();assign=[]
    for group,b in slots:
        q=next(q for q in GROUPS[group] if q not in used)
        used.add(q);assign.append((q,b%PERIOD[q]))
    return assign


def check_shape(assign):
    period=lcm(35,*(PERIOD[q] for q,b in assign))
    relevant=[v for v in range(period) if v%35 in A]
    private={q:[] for q,b in assign}
    for v in relevant:
        hits=[q for q,b in assign if v%PERIOD[q]==b]
        assert hits
        if len(hits)==1:private[hits[0]].append(v)
    assert all(private.values())
    return {'period':period,'residual_positions':len(relevant),'private_positions':{str(q):v for q,v in private.items()}}


def has_phase(a,q,b,coordinate='v'):
    n=8+12*b if coordinate=='v' else 32+36*b
    return (a*a*pow(2,n,q)-1)%q==0


def eight_predicate(a):
    for primes,phases in ((B8,(0,4)),(D6,(0,2)),(C10,(0,6,8))):
        if all(any(has_phase(a,q,b,'w') for q in primes) for b in phases):return True
    active=[]
    for q in Z:
        pp=[b for b in ROWS if has_phase(a,q,b)]
        if len(pp)!=1:return False
        active.append(pp[0])
    if len(set(active))!=4:return False
    c=next(b for b in ROWS if b not in active)
    if all(any(has_phase(a,q,b) for q in J) for b in (c,c+7)):return True
    if c in (1,5):
        pp=[v for v in A if v%7==c]
        if all(any(has_phase(a,q,b) for q in U) for b in pp):return True
    return False


def crt_append(a,m,r,q):
    assert gcd(m,q)==1
    return a+m*((r-a)*pow(m,-1,q)%q),m*q


def exact_nine_example(pattern):
    assign=assignments_for_shape(pattern['slots'])
    a,m=A3,S3
    for q,b in assign:
        residue=pow(pow(2,4+6*b,q),-1,q)
        a,m=crt_append(a,m,residue,q)
    selected={q for q,b in assign}
    for q in T8:
        if q not in selected:a,m=crt_append(a,m,0,q)
    assert a%S3==A3 and all(has_phase(a,q,b) for q,b in assign)
    assert not eight_predicate(a)
    assert 2*a*a-1>max(selected)
    return {'type':pattern['type'],'root':str(a),'progression_modulus':str(m),
            'tail_v_phases':{str(q):b for q,b in assign},'supplementary_minimum':9,
            'unrestricted_total_upper_bound':29,'complete_eight_predicate':False}


def capacity_checks():
    results=[]
    assert 2*F(5,2)+2*F(13,8)+3*F(3,2)==F(51,4)<13
    for c in ROWS:
        d={v for v in A if v%7!=c};r=len(d)
        bound=F(17,2)+F(r,8)
        assert bound<r
        results.append({'m':1,'removed':[c],'size':r,'bound':str(bound)})
    for cc in combinations(ROWS,2):
        d={v for v in A if v%7 not in cc};r=len(d)
        if r>7:assert 5*F(3,2)<r
        else:
            big=next(c for c in ROWS if c not in cc and len([v for v in d if v%7==c])==3)
            rest={v for v in d if v%7!=big}
            assert len(rest)==4 and max(Counter(v%5 for v in rest).values())==2
            assert 1+1+1<4
        results.append({'m':2,'removed':cc,'size':r,'excluded_by':'mass' if r>7 else 'opposite_f14_pair_then_residual_mass'})
    return results


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,default=HERE/'zero_nine_certificate.json')
    args=parser.parse_args()
    inventory=verify_inventory();shapes=[];counts=Counter();examples=[];seen_types=set()
    for p in patterns():
        count=phase_count(p['slots']);counts[p['type']]+=count
        shape=check_shape(assignments_for_shape(p['slots']))
        # S has two possible periods; all of its T/V choices have the same
        # restriction to the remaining row, checked directly in this loop.
        for i,(g,b) in enumerate(p['slots']):
            if g!='S':continue
            assign=assignments_for_shape(p['slots'])
            for q in S:
                if q in {x for j,(x,_) in enumerate(assign) if j!=i}:continue
                altered=assign[:];altered[i]=(q,b%PERIOD[q]);check_shape(altered)
        shapes.append({**p,'phase_count':count,'geometry':shape})
        if p['type'] not in seen_types:examples.append(exact_nine_example(p));seen_types.add(p['type'])
    expected={'I':7200,'II':114048,'III':336384,'IV':14400,'V':95040,'VI':12096,'VII':48384,'VIII':48384}
    assert dict(counts)==expected
    assert sum(counts.values())==675936
    result={'schema':'RIESEL_ZERO_W_NINE_V15','status':'PASS','inventory':inventory,
            'capacity_cases':capacity_checks(),'geometric_patterns':shapes,
            'phase_dictionary_counts':dict(counts),'phase_dictionary_total':sum(counts.values()),
            'signed_CRT_descriptions':128*sum(counts.values()),'cube_perfect_matchings':cube_matchings()[0],
            'exact_nine_examples':examples,'all_prime_completeness_basis':'proof.md',
            'native_BRC_execution':False,'independent_project_review':False}
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':'PASS','patterns':len(shapes),'phase_count':sum(counts.values()),
                      'signed_count':128*sum(counts.values()),'exact_nine_examples':len(examples),
                      'inventory':inventory,'output':str(args.output)},indent=2))


if __name__=='__main__':main()
