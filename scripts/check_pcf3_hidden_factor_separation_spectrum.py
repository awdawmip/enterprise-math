#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, math, random
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path

SCHEMA='PCF3_HIDDEN_FACTOR_SEPARATION_SPECTRUM_V1'
TASK='RS-PRIME-COORD-FACTOR-HIDDEN-FACTOR-SEPARATION-SPECTRUM'
PUBLIC_SEEDS=tuple(range(64))
CORPUS_SEED=0x5A17C0DE
POLY_NAMES=('x^2+1','x^2+x+1','x^6-1','x^6+1')
STATES=('Z','C','B3','A4','D12')
SIG_TO_STATE={(0,0,0,0):'Z',(0,0,1,0):'C',(0,1,1,0):'B3',(1,0,0,1):'A4',(0,0,0,1):'D12'}
CLASS_NONZERO={1:{'C':4,'B3':2,'A4':2,'D12':4},5:{'C':2,'B3':0,'A4':2,'D12':0},7:{'C':4,'B3':2,'A4':0,'D12':0},11:{'C':2,'B3':0,'A4':0,'D12':0}}
CLASS_ROOTS={1:12,5:4,7:6,11:2}
DOT={a:{b:sum(CLASS_NONZERO[a][s]*CLASS_NONZERO[b][s] for s in ('C','B3','A4','D12')) for b in CLASS_NONZERO} for a in CLASS_NONZERO}

def poly_values(x:int)->tuple[int,int,int,int]: return (x*x+1,x*x+x+1,x**6-1,x**6+1)
def signature_mod(x:int,p:int)->tuple[int,int,int,int]: return tuple(int(z%p==0) for z in poly_values(x))
def predicted_counts(p:int)->dict[str,int]:
    if p==3:return {'Z':1,'C':1,'B3':1,'A4':0,'D12':0}
    c=p%12
    if c not in CLASS_NONZERO:raise AssertionError((p,c))
    return {'Z':p-CLASS_ROOTS[c],**CLASS_NONZERO[c]}
def direct_counts(p:int)->dict[str,int]:
    c=Counter(SIG_TO_STATE[signature_mod(x,p)] for x in range(p));return {s:c[s] for s in STATES}
def collision_count(p:int,q:int)->int:
    a=predicted_counts(p);b=predicted_counts(q);return sum(a[s]*b[s] for s in STATES)

def is_prime(n:int)->bool:
    if n<2:return False
    for p in (2,3,5,7,11,13,17,19,23,29,31,37):
        if n==p:return True
        if n%p==0:return False
    d=n-1;s=0
    while d%2==0:s+=1;d//=2
    for a in (2,325,9375,28178,450775,9780504,1795265022):
        if a%n==0:continue
        x=pow(a,d,n)
        if x in (1,n-1):continue
        for _ in range(s-1):
            x=x*x%n
            if x==n-1:break
        else:return False
    return True

def next_prime(n:int)->int:
    n=max(2,n)
    if n==2:return 2
    if n%2==0:n+=1
    while not is_prime(n):n+=2
    return n

def factor_small(n:int)->tuple[int,...]:
    out=[];x=n;d=2
    while d*d<=x:
        while x%d==0:out.append(d);x//=d
        d=3 if d==2 else d+2
    if x>1:out.append(x)
    return tuple(out)

def spsp2(n:int)->bool:
    if n<3 or n%2==0 or is_prime(n):return False
    d=n-1;s=0
    while d%2==0:s+=1;d//=2
    x=pow(2,d,n)
    if x in (1,n-1):return True
    for _ in range(s-1):
        x=x*x%n
        if x==n-1:return True
    return False

@dataclass(frozen=True)
class Case:
    n:int;family:str;factors:tuple[int,...]

def build_corpus()->list[Case]:
    rng=random.Random(CORPUS_SEED);out=[];seen=set()
    def add(n,fam,fac):
        if n in seen or n<=3 or len(fac)<2:return
        assert math.prod(fac)==n
        seen.add(n);out.append(Case(n,fam,tuple(sorted(fac))))
    for bits in (10,12,14,16,18,20):
        half=bits//2
        for k in range(4):
            base=(1<<(half-1))+rng.randrange(1,max(3,1<<max(1,half-2)))
            p=next_prime(base);q=next_prime(p+2+2*k)
            if p==q:q=next_prime(q+2)
            add(p*q,'balanced_semiprime',(p,q))
        for k in range(3):
            pb=max(3,bits//4);qb=max(4,bits-pb)
            p=next_prime((1<<(pb-1))+2*k+1);q=next_prime((1<<(qb-1))+rng.randrange(1,1<<max(1,qb-3)))
            if p==q:q=next_prime(q+2)
            add(p*q,'unbalanced_semiprime',(p,q))
        for _ in range(3):
            center=(1<<(half-1))+rng.randrange(5,max(7,1<<max(2,half-2)))
            p=next_prime(center);q=next_prime(p+2);add(p*q,'near_twin_semiprime',(p,q))
        p=next_prime((1<<max(2,bits//3-1))+1);e=2
        while (p**(e+1)).bit_length()<=bits:e+=1
        e=max(2,e);add(p**e,'prime_power',tuple([p]*e))
        p=next_prime((1<<max(2,bits//5-1))+1);q=next_prime(p+4);r=next_prime((1<<max(3,bits//2-1))+rng.randrange(1,8));add(p*q*r,'multi_prime',(p,q,r))
    for n in (561,1105,1729,2465,2821,6601,8911,10585,15841,29341):add(n,'carmichael',factor_small(n))
    for n in (2047,3277,4033,4681,8321,15841,29341,42799,49141,52633):
        if spsp2(n):add(n,'strong_pseudoprime_base2',factor_small(n))
    collision=[]
    for s in PUBLIC_SEEDS:
        if s<2:continue
        for v in poly_values(s):
            if v<=3:continue
            fac=factor_small(abs(v))
            if len(fac)>=2 and abs(v)%2==1 and abs(v).bit_length()<=22:collision.append(abs(v))
        if len(set(collision))>=12:break
    for n in sorted(set(collision))[:12]:add(n,'coordinate_collision',factor_small(n))
    assert len(out)==89
    return out

def first_split(n:int):
    for s in PUBLIC_SEEDS:
        gs=tuple(math.gcd(n,v) for v in poly_values(s))
        for i,d in enumerate(gs):
            if 1<d<n:return {'seed':s,'component':POLY_NAMES[i],'factor':d,'gcds':list(gs)}
    return None

def fixed_prefix_counterexample():
    M=max(abs(v) for s in PUBLIC_SEEDS for v in poly_values(s) if v!=0);p=next_prime(M+1);q=next_prime(p+2);N=p*q
    for s in PUBLIC_SEEDS:
        for v in poly_values(s):assert math.gcd(N,v) in (1,N)
    return {'seed_budget':[0,63],'max_nonzero_abs_value':M,'p':p,'q':q,'N':N}

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--out');args=ap.parse_args()
    primes=[p for p in range(3,300) if p%2 and is_prime(p)]
    for p in primes:assert direct_counts(p)==predicted_counts(p),(p,direct_counts(p),predicted_counts(p))
    pair_checks=0
    for i,p in enumerate(primes[:20]):
        for q in primes[i+1:20]:
            assert collision_count(p,q)==sum(direct_counts(p)[s]*direct_counts(q)[s] for s in STATES);pair_checks+=1
    crt_checks=0;small=[3,5,7,11,13,17,19,23,29,31]
    for i,p in enumerate(small):
        for q in small[i+1:]:
            N=p*q;split=0
            for x in range(N):
                local_diff=signature_mod(x,p)!=signature_mod(x,q);gcd_split=any(1<math.gcd(N,v)<N for v in poly_values(x));assert local_diff==gcd_split;split+=int(gcd_split);crt_checks+=1
            assert split==N-collision_count(p,q)
    corpus=build_corpus();fam=defaultdict(lambda:[0,0]);fails=[];sem=[0,0]
    for c in corpus:
        hit=first_split(c.n);fam[c.family][1]+=1
        if hit:fam[c.family][0]+=1
        else:fails.append({'n':c.n,'family':c.family})
        if c.family in ('balanced_semiprime','unbalanced_semiprime','near_twin_semiprime'):sem[1]+=1;sem[0]+=int(hit is not None)
    assert sum(v[0] for v in fam.values())==84 and sem==[43,48]
    ce=fixed_prefix_counterexample()
    report={'schema':SCHEMA,'task_id':TASK,'primary_verdict':'SEPARATOR_FOUND_WITH_EXACT_SCOPE','typed_vector':{'constructor_inputs':['N','independent public seed s','fixed public constants'],'polynomial_components':list(POLY_NAMES),'projection':'pi_l(f(s) mod N)=f(s) mod l for proof-side l|N','gcd_event':'component separates iff exactly one local projection vanishes'},'cyclotomic_signature':{'factorizations':{'x^2+1':'Phi_4','x^2+x+1':'Phi_3','x^6-1':'Phi_1 Phi_2 Phi_3 Phi_6','x^6+1':'Phi_4 Phi_12'},'states':{'Z':'no listed polynomial vanishes','C':'orders 1,2,6; only x^6-1 vanishes','B3':'order 3; x^2+x+1 and x^6-1 vanish','A4':'order 4; x^2+1 and x^6+1 vanish','D12':'order 12; only x^6+1 vanishes'},'prime_class_table':{'1':{'nonzero':CLASS_NONZERO[1],'root_union':12},'5':{'nonzero':CLASS_NONZERO[5],'root_union':4},'7':{'nonzero':CLASS_NONZERO[7],'root_union':6},'11':{'nonzero':CLASS_NONZERO[11],'root_union':2},'3_special':{'Z':1,'C':1,'B3':1,'A4':0,'D12':0}},'collision_dot_matrix':{str(a):{str(b):DOT[a][b] for b in DOT[a]} for a in DOT},'exact_formula':'For p,q>3, C=(p-r_p)(q-r_q)+d[c_p,c_q], S=pq-C, P=S/(pq), where c_l=l mod 12 and r={1:12,5:4,7:6,11:2}.'},'theorems':{'integer_residue_collapse':'Any N-only integer scalar a(N,s) is GCD-relevant only through divisibility by local prime ideals; gcd(N,a) splits iff p|a xor q|a for N=pq.','matrix_rank_bridge':'For an N-only square integer matrix M, a full-rank-vs-singular local asymmetry is integerized by det(M): gcd(N,det M) splits when exactly one local determinant vanishes.','universal_sixth_minus_separator':'For every distinct odd-prime semiprime N=pq, x^6-1 has r_l=gcd(6,l-1)>=2 roots mod each l, and a uniform public seed has exact proper-split probability r_p/p+r_q/q-2*r_p*r_q/(pq)>0.','fixed_prefix_no_go':'For any finite factor-independent seed set S and fixed finite integer-polynomial family F, choose distinct primes p,q larger than every nonzero |f(s)|. Then every probe is 0 modulo both factors or neither, so all GCDs are trivial; no fixed finite seed prefix is a universal splitter.','balanced_fixed_degree_barrier':'For the four-probe vector, exact P <= 12/p+12/q. Hence on balanced semiprimes one independent uniform seed succeeds only at O(N^-1/2), so constant-success iid repetition remains Omega(sqrt(N)) seeds within this fixed probe family.'},'benchmark_replay':{'source':'PCF2 deterministic corpus definition, Draft PR #740, used as finite evidence only','public_seeds':[0,63],'cases':89,'successes':84,'semiprime_cases':48,'semiprime_successes':43,'by_family':{k:{'successes':v[0],'cases':v[1]} for k,v in sorted(fam.items())},'failures':fails},'fixed_prefix_64_counterexample':ce,'verification':{'prime_signature_checks':len(primes),'prime_pair_formula_checks':pair_checks,'small_crt_seed_checks':crt_checks},'ranked_pcf4_handoff':[{'rank':1,'residue':'x^6-1','reason':'smallest admitted current component with all-semiprime positive exact split probability under uniform public seeds; still square-root-scale when balanced'},{'rank':2,'residue_pair':['x^6-1','x^6+1'],'reason':'separates opposite sixth-power phases that product aggregation would erase'},{'rank':3,'refinements':['x^2+x+1','x^2+1'],'reason':'cyclotomic Phi_3/Phi_4 refinements inside the two sixth-power branches; useful only when parent branch is synchronized'}],'unresolved_residue':'No admitted packet/path, shell, wall, or filament source currently supplies a proved N-only integer asymmetry with better balanced success scaling; any such future component must be reduced to an explicit integer residue/minor before claiming factor separation.'}
    text=json.dumps(report,indent=2,sort_keys=True)+'\n'
    if args.out:Path(args.out).write_text(text,encoding='utf-8')
    print(f"PCF3_SPECTRUM_CHECK_PASS primes={len(primes)} pairs={pair_checks} crt={crt_checks} corpus=84/89 semiprime=43/48 fixed64={ce['N']}")
if __name__=='__main__':main()
