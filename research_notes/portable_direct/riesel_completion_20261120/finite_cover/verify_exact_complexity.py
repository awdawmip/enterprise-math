"""Exact finite certificate for c_P(a)=5 and recursive covering skeletons.

The theorem for arbitrary refinement depth is proved in proof.md, using Bang's
primitive prime divisor theorem. Symbolic rows below are not numeric prime
certificates. Positive MILP search output is not used by this verifier.
"""
from __future__ import annotations

from fractions import Fraction
from hashlib import sha1, sha256
from itertools import combinations
from math import gcd, isqrt, lcm, prod
from pathlib import Path
import argparse
import json
import sys

HERE = Path(__file__).resolve().parent
BASE_RELATIVE = Path('research_notes/portable_direct/riesel_mixed_20261119/certificate.json')
ROOT = next(p for p in HERE.parents if (p/BASE_RELATIVE).is_file())
BASE = ROOT/BASE_RELATIVE
SOURCE_DEFAULT = next(p for p in (ROOT/'src',ROOT/'vendor_src')
                      if (p/'enterprise_math/brc_transport.py').is_file())
PATTERN = [(2,0,2), (3,0,15), (4,1,1), (8,3,11), (12,7,7), (24,23,23)]
Q0 = [
    {'p':5, 'ord2':4, 'period_u':2, 'phase_u':1, 'private_u':3},
    {'p':73, 'ord2':9, 'period_u':9, 'phase_u':1, 'private_u':10},
    {'p':13, 'ord2':12, 'period_u':6, 'phase_u':0, 'private_u':6},
    {'p':19, 'ord2':18, 'period_u':9, 'phase_u':4, 'private_u':76},
    {'p':109, 'ord2':36, 'period_u':18, 'phase_u':16, 'private_u':16},
]


def strip(value, prime_set):
    """Remove only known primes; no factorization of the remaining integer."""
    counts={}
    for p in sorted(prime_set):
        v=0
        while value % p == 0:
            value//=p
            v+=1
        if v:
            counts[str(p)]=v
    return value, counts


def crt_pair(a, mod, b, p):
    assert gcd(mod,p)==1
    return a+mod*(((b-a)*pow(mod,-1,p))%p), mod*p


def git_blob(data):
    return sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()


def build_skeleton(depth):
    rows=[dict(r) for r in Q0]
    used_orders={r['ord2'] for r in Q0}
    stages=[]
    for level in range(depth):
        largest=max(rows,key=lambda r:r['period_u'])
        d=largest['period_u']; c=largest['phase_u']; w=largest['private_u']
        L=35*d
        assert d==18*24**level and c==d-2
        assert lcm(105,*(r['period_u'] for r in rows))==L
        assert gcd(35,24)==1
        v0=(w-c)//d
        assert w==c+d*v0
        children=[]
        for m,phase,private in PATTERN:
            target_order=2*d*m
            assert target_order>max(used_orders) or target_order not in used_orders
            assert target_order>6
            # Every new order exceeds every order existing before this stage.
            assert target_order>2*d
            assert target_order not in used_orders
            used_orders.add(target_order)
            t=((private-v0)*pow(35,-1,24))%24
            child={
                'p':f'primitive_prime_order_{target_order}',
                'ord2':target_order,'period_u':d*m,
                'phase_u':(c+d*phase)%(d*m),
                'private_u':w+L*t,
                'existence':'Bang: target exponent > 6',
            }
            assert child['private_u']>0
            assert child['private_u']%child['period_u']==child['phase_u']
            children.append(child)
        rows=[r for r in rows if r is not largest]+children
        assert len(rows)==5+5*(level+1)
        assert max(r['period_u'] for r in rows)==24*d
        stages.append({'level':level+1,'replaced_period_u':d,
                       'new_period_u':24*d,'new_prime_orders':[r['ord2'] for r in children]})
    return rows,stages


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--source-dir',type=Path,default=SOURCE_DEFAULT)
    ap.add_argument('--output',type=Path,default=HERE/'exact_complexity_certificate.json')
    ap.add_argument('--skeleton-depth',type=int,default=6)
    args=ap.parse_args()
    sys.set_int_max_str_digits(0)
    bbytes=BASE.read_bytes(); old=json.loads(bbytes); base=old['optimized']
    assert old['project_source_commit']=='b1efc6c805661ed7b476e6e730107da6043176ee'
    source_checks={}
    for name,expected in old['project_source_blobs'].items():
        path=args.source_dir/'enterprise_math'/name
        observed=git_blob(path.read_bytes())
        assert observed==expected,(name,expected,observed)
        source_checks[name]={'expected_git_blob_sha1':expected,'observed_git_blob_sha1':observed,'matches':True}
    astar=int(base['a']); P=[r['p'] for r in base['rows']]
    M=prod(P); Pset=set(P); Q=[r['p'] for r in Q0]
    assert len(Pset)==20 and len(set(Q))==5 and not Pset.intersection(Q)
    assert all(p>2 and all(p%d for d in range(2,isqrt(p)+1)) for p in Q)
    assert all(all(pow(2,j,r['p'])!=1 for j in range(1,r['ord2'])) and
               pow(2,r['ord2'],r['p'])==1 for r in Q0)
    assert all(r['period_u']==r['ord2']//gcd(2,r['ord2']) for r in Q0)
    assert all(any(v%m==phase for m,phase,_ in PATTERN) for v in range(24))
    for i,(_,_,private) in enumerate(PATTERN):
        assert [j for j,(m,phase,_) in enumerate(PATTERN) if private%m==phase]==[i]
    # Old H_u is a period-105 observer predicate, inherited from the v4 proof.
    H=[u for u in range(105) if all((astar*astar*pow(2,2*u,p)-1)%p for p in P)]
    assert len(H)==36
    Hset=set(H)
    for u in range(630):
        assert u%105 not in Hset or any(u%r['period_u']==r['phase_u'] for r in Q0)
    for i,r in enumerate(Q0):
        u=r['private_u']
        assert u%105 in Hset
        assert [j for j,t in enumerate(Q0) if u%t['period_u']==t['phase_u']]==[i]

    # Pairwise-coprimality forcing plus the previous B=3,m=1 forcing.
    exponents=[2*r['private_u'] for r in Q0]
    diffs=sorted({abs(x-y) for x,y in combinations(exponents,2)})
    D=lcm(*(pow(2,d)-1 for d in diffs))
    E,removed=strip(D,Pset|set(Q))
    R=pow(2,210)
    T1,T1_removed=strip(R-1,Pset)
    T=lcm(E,T1)
    K=2*M
    b=astar
    for r in Q0:
        r['root_residue']=pow(pow(2,r['phase_u'],r['p']),-1,r['p'])
        b,K=crt_pair(b,K,r['root_residue'],r['p'])
    assert 0<b<K and K==2*M*prod(Q)
    assert gcd(T,K)==1
    a=T*((b*pow(T,-1,K))%K)
    assert a>max(P+Q) and a%2==1 and a%3==0
    assert a%(2*M)==astar and a%T==0
    assert all(a%r['p']==r['root_residue'] for r in Q0)
    assert all(a%p==astar%p for p in P)

    # Project-native singleton positive BRC: x -> 2x+1.
    sys.path.insert(0,str(args.source_dir))
    from enterprise_math.brc_transport import Affine,EffectHistogram
    step=EffectHistogram.from_terms(1,[(1,Affine(((2,),),(1,)),1)])
    twice=step.then(step)
    assert twice.entries==((Fraction(1),Affine(((4,),),(3,)),1),)
    def advance(packet,value):
        (point,weights),=packet.evaluate((value,)).items()
        assert weights.entries==((Fraction(1),1),)
        assert point[0].denominator==1
        return int(point[0])
    assert advance(step,-1)==-1 and advance(twice,-1)==-1
    x=a*a-1
    native_samples=[]
    for n in range(1,max(exponents)+1):
        x=advance(step,x)
        if n in exponents:
            assert x==(a*a<<n)-1
            native_samples.append({'n':n,'value':str(x),'decimal_sha256':sha256(str(x).encode()).hexdigest()})
    values={r['n']:int(r['value']) for r in native_samples}
    gcd_rows=[]
    for ni,nj in combinations(exponents,2):
        g=gcd(values[ni],values[nj])
        assert g==1
        gcd_rows.append({'n1':ni,'n2':nj,'gcd':g})
    for i,n in enumerate(exponents):
        assert all(values[n]%p for p in P)
        assert [j for j,q in enumerate(Q) if values[n]%q==0]==[i]

    # Complete numeric cover, with proper divisors, not a finite prefix test.
    full_period=lcm(*(r['order'] for r in base['rows']),*(r['ord2'] for r in Q0))
    assert full_period==20160
    allQ=P+Q
    for n in range(full_period):
        assert any((a*a*pow(2,n,q)-1)%q==0 for q in allQ)
    assert 2*a*a-1>max(allQ)

    # Symbolic recursive finite obligations. General depth is proved inductively.
    skeletons=[]
    for depth in range(args.skeleton_depth+1):
        rows,stages=build_skeleton(depth)
        assert len({r['p'] for r in rows})==len(rows)
        assert len(rows)==5+5*depth
        dmax=max(r['period_u'] for r in rows)
        assert lcm(105,*(r['period_u'] for r in rows))==35*dmax
        for i,r in enumerate(rows):
            u=r['private_u']
            assert u%105 in Hset
            assert [j for j,t in enumerate(rows) if u%t['period_u']==t['phase_u']]==[i]
            # If its order matches an old P order, this is an original numeric q.
            if isinstance(r['p'],str):
                assert r['ord2'] not in {t['order'] for t in base['rows']}
            assert 210%r['ord2']!=0
        if depth<=2:
            for u in range(35*dmax):
                assert u%105 not in Hset or any(u%r['period_u']==r['phase_u'] for r in rows)
        skeletons.append({'depth':depth,'additional_prime_count':len(rows),
                          'dmax':dmax,'period_u':35*dmax,'rows':rows,'stages':stages,
                          'full_period_checked':depth<=2,
                          'all_private_witnesses_checked':True})

    cert={
        'schema':'enterprise-math.riesel-exact-finite-cover-complexity.v1',
        'researcher_id':'EM-DIRECT-970E1C','research_activity_id':'RA-D2EC212845B63844081F9A14',
        'session_id':'LOCAL-RIESEL-a047cf12d55443c395589f6024246b16',
        'status':'new author derivation and exact finite checks; not independent project Review',
        'base_certificate_sha256':sha256(bbytes).hexdigest(),
        'project_source_commit':old['project_source_commit'],
        'project_source_blob_checks':source_checks,
        'a_star':str(astar),'P':P,'M':str(M),'Q0':Q0,'H_u':H,
        'D':str(D),'E':str(E),'D_removed_valuations':removed,'T1':str(T1),
        'T1_removed_valuations':T1_removed,'T':str(T),'crt_b':str(b),'crt_K':str(K),
        'root_a':str(a),'root_digits':len(str(a)),'k_digits':len(str(a*a)),
        'root_progression_modulus':str(T*K),
        'full_cover_period':full_period,'pairwise_gcd_checks':gcd_rows,
        'private_terms':native_samples,'exact_minimum_P_outside_cover_primes':5,
        'total_minimum_cover_size_interval':[5,25],
        'old_B3_m1_forcing_preserved':True,
        'native_brc':{'module':'enterprise_math.brc_transport',
                      'source_commit':'b1efc6c805661ed7b476e6e730107da6043176ee',
                      'one_step':'x -> 2x+1','even_step':'x -> 4x+3',
                      'positive_singleton_weight':1,'multiplicity':1},
        'general_theorem':'For every r >= 0 there are infinitely many odd a congruent to a_star modulo 2M, also divisible by T1 and hence by 3, with c_P(a)=5+5r, finite.',
        'primitive_prime_source':{'url':'https://people.math.sc.edu/filaseta/papers/SierpinskiEtCoPap5.pdf',
                                  'location':'Lemma 2; cites A. S. Bang (1886)',
                                  'used_statement':'For each integer t > 6, 2^t-1 has a prime of exact 2-order t.'},
        'recursive_pattern':[{'modulus':m,'phase':c,'private_residue':w} for m,c,w in PATTERN],
        'skeletons':skeletons,
        'not_claimed':['same root works for every depth','arbitrary high-lpf B,m family admits finite cover',
                       'all old-hole values avoid all primes up to arbitrary B',
                       'numeric primes or roots computed for symbolic depths above zero',
                       'literature priority','independent project Review']}
    args.output.write_text(json.dumps(cert,indent=2)+'\n')
    print(json.dumps({'root_digits':cert['root_digits'],'k_digits':cert['k_digits'],
                      'exact_minimum_P_outside_primes':5,'full_period':full_period,
                      'gcd_checks':len(gcd_rows),'skeleton_depth':args.skeleton_depth,
                      'output':str(args.output)}))


if __name__=='__main__': main()
