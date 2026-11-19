"""Exact reversible preparation and source-pinned ternary BRC checks."""
import argparse
import hashlib
import json
from collections import Counter
from fractions import Fraction as F
from itertools import permutations, product
from pathlib import Path
import runpy


def law(p,d,weights,length,table,shared=False):
    """Return integer counts in error-word order; a shared input supplies one raw digit."""
    result=Counter()
    for initial in range(d):
        for digits in product(range(p),repeat=1 if shared else length):
            digits=digits*length if shared else digits
            c, word=initial,0
            for u in digits:
                dest=table[p*c+u]
                c,z=divmod(dest,p)
                word=p*word+z
            result[word]+=weights[initial]
    return [result[i] for i in range(p**length)]


def radix_table(p,d):
    return [(i%d)*p+(i//d) for i in range(p*d)]


def block_sums(weights,p,d,k):
    ordered=sorted(weights,reverse=True)
    totals=[]
    for m in range(p**k+1):
        q,s=divmod(m*d,p**k)
        totals.append(p**k*sum(ordered[:q])+(s*ordered[q] if q<d else 0))
    return [y-x for x,y in zip(totals,totals[1:])]


def shared_table(p,d,k,weights):
    """One loop at the most likely digit; the other selected digits receive k disjoint states."""
    labels=sorted(range(p),key=weights.__getitem__,reverse=True)[:min(p,1+(d-1)//k)]
    table=[None]*(p*d)
    table[labels[0]]=0
    new=1
    for b in labels[1:]:
        current=0
        for _ in range(k):
            table[p*current+b]=p*new
            current,new=new,new+1
    # Extra unused states need incoming zero edges; loops at them do not meet the root.
    for x in range(new,d):
        table[p*x]=p*x
    unused=iter(sorted(set(range(p*d))-set(table)))
    return [next(unused) if x is None else x for x in table]


def shared_score(p,d,k,table,weights):
    score=0
    for b,mass in enumerate(weights):
        c=0
        for _ in range(k):
            c,z=divmod(table[p*c+b],p)
            if z:
                break
        else:
            score+=mass
    return score


def complete_permutations():
    reports=[]
    for p,d,weights in [(3,2,[5,2]),(2,3,[6,3,1])]:
        majorants={k:block_sums(weights,p,d,k) for k in range(1,4)}
        pi=list(range(p,0,-1))
        shared_bounds={k:sum(pi[:min(p,1+(d-1)//k)]) for k in range(1,4)}
        all_same=[True]*3
        largest=[0]*3
        tested=0
        for perm in permutations(range(p*d)):
            tested+=1
            for k in range(1,4):
                actual=sorted(law(p,d,weights,k,perm),reverse=True)
                diff=0
                for a,b in zip(majorants[k],actual):
                    diff+=a-b
                    assert diff>=0
                assert diff==0
                all_same[k-1]&=(majorants[k]==actual)
                largest[k-1]=max(largest[k-1],shared_score(p,d,k,perm,pi))
        for k in range(1,4):
            assert law(p,d,weights,k,radix_table(p,d))==majorants[k]
            assert largest[k-1]==shared_bounds[k]==shared_score(p,d,k,shared_table(p,d,k,pi),pi)
        reports.append(dict(p=p,d=d,all_permutations_tested=tested,rational_weights=weights,
                            best_full_word_masses=majorants,best_shared_pure_masses=largest,
                            all_tables_saturate=all_same))
    return reports


def finite_families():
    checks,shared_checks=0,0
    for p in (2,3,5,6):
        for d in (1,2,4,7):
            w=list(range(d,0,-1))
            for k in range(1,5):
                true=law(p,d,w,k,radix_table(p,d))
                assert true==block_sums(w,p,d,k) and true==sorted(true,reverse=True)
                checks+=1
                pi=[1+p-i for i in range(p)]
                P=shared_table(p,d,k,pi)
                assert sorted(P)==list(range(d*p))
                assert shared_score(p,d,k,P,pi)==sum(pi[:min(p,1+(d-1)//k)])
                shared_checks+=1
    p,d,k=3,5,2
    exact=[1]*p
    assert shared_score(p,d,k,radix_table(p,d),exact)==2
    assert shared_score(p,d,k,shared_table(p,d,k,exact),exact)==3
    return dict(general_radix_cases=checks,shared_cases=shared_checks,
                uniform_ternary_two_step_five_state_example={'fresh':'5/9','same_table_shared':'2/3','best_table_shared':'1'})


def real_ternary(root):
    previous=Path(__file__).resolve().parents[1]/'fiftieth'/'calibration_check.py'
    old=runpy.run_path(str(previous))
    brc=old['load'](root)
    frozen=root/'research_tasks'/'RS-EULER-RR-20261012-03.md'
    raw=frozen.read_bytes()
    sha=hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()
    assert sha=='d2963ebc88db6b5a7cda7251af453434b9117542'
    costs=Counter()
    data=[]
    for d in (1,2,3,5):
        p,k=3,2
        w=list(range(d,0,-1))
        denominator=sum(w)*p**k
        masses=law(p,d,w,k,radix_table(p,d))
        offsets={}
        for j in range(p):
            for n,m in enumerate(masses):
                if m:
                    offsets[(j,divmod(n,p))]=F(m,denominator*p)
        result=old['finite_kernel'](brc,costs,offsets)
        for j, row in enumerate(result['channel_by_source']):
            for labels,prob in zip(result['record_words'],row):
                errorword=tuple((v-j)%p for v in labels)
                index=errorword[0]*p+errorword[1]
                assert F(prob)==F(masses[index],denominator)
        for j in range(p):
            for a in range(p):
                for z in range(p):
                    assert (a+z+j-a)%p==(j+z)%p
        data.append(dict(memory_states=d,steps=k,output_joint=result,all_accurate=str(F(masses[0],denominator))))
    return dict(public_task_git_blob=sha,prior_adapter_sha256=hashlib.sha256(previous.read_bytes()).hexdigest(),
                public_native_blob_pins=old['PINS'],BRC_costs=dict(costs),replayed=data)


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--repo',type=Path,required=True)
    arg=parser.parse_args()
    out=dict(unrestricted_permutation_audits=complete_permutations(),larger_exact_checks=finite_families(),
             original_ternary_write=real_ternary(arg.repo))
    print(json.dumps(out,indent=2))


if __name__=='__main__':
    main()
