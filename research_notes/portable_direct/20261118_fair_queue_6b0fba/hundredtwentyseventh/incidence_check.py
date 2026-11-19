"""Exact equality-sensor and positive BRC checks. See incidence.md for the sensor contract."""
import argparse
from collections import Counter, defaultdict
from fractions import Fraction as F
from functools import lru_cache
import hashlib
from itertools import combinations, product
import json
from math import comb, isqrt
from pathlib import Path
import sys

HERE=Path(__file__).resolve().parent
BOOK='research_tasks/RS-EULER-RR-20261012-01.md'


def minimax(bounds,erased):
    @lru_cache(None)
    def visit(state,left):
        if len(state)<=1:
            return 0
        best=None
        for g in range(len(state)):
            costs=[]
            for bit in (0,1):
                nxt=tuple(sorted(t for i,q in enumerate(state)
                                 if (t:=q-int((i==g)!=bool(bit)))>=0))
                if nxt:
                    costs.append(visit(nxt,left))
            if left:
                costs.append(visit(state,left-1))
            worst=1+max(costs)
            if best is None or worst<best:
                best=worst
        return best
    return visit(tuple(sorted(bounds)),erased)


def schedules(bounds,e,adaptive):
    lo=(e+1)//2
    hi=e+1-lo
    plan=[i for i,t in enumerate(bounds) for _ in range(t+(lo if i==0 else hi))]
    def walk(d,remain,erase_left,questions,answers,flips):
        active=[i for i,v in enumerate(remain) if v>=0]
        if adaptive and len(active)==1:
            assert active==[d]
            yield questions,answers
            return
        if not adaptive and len(questions)==len(plan):
            assert active==[d]
            yield questions,answers
            return
        g=active[0] if adaptive else plan[len(questions)]
        for ans in (0,1,2):
            flip=int(ans!=2 and ans!=int(g==d))
            if (ans==2 and not erase_left) or flips+flip>bounds[d]:
                continue
            nxt=tuple(v-int(ans!=2 and ans!=int(g==i)) for i,v in enumerate(remain))
            yield from walk(d,nxt,erase_left-int(ans==2),questions+(g,),answers+(ans,),flips+flip)
    return [list(walk(i,tuple(bounds),e,(),(),0)) for i in range(len(bounds))]


def fixed_feasible(m,limits,e,budget):
    def comps(total,n):
        if n==1:
            yield (total,)
        else:
            for j in range(total+1):
                for tail in comps(total-j,n-1):
                    yield (j,)+tail
    return any(all(ns[i]+ns[j]>=limits[i]+limits[j]+e+1 for i,j in combinations(range(m),2))
               for ns in comps(budget,m))


def resource_grid():
    examples=0
    for m in range(2,6):
        for t in combinations(range(m+3),m):
            # Remove the strictly increasing offset to enumerate heterogeneous weakly increasing radii.
            limits=tuple(v-i for i,v in enumerate(t))
            for e in range(4):
                adaptive=sum(limits)+m-1+e
                fixed=adaptive+(m-2)*(e//2)
                assert minimax(limits,e)==adaptive
                assert fixed_feasible(m,limits,e,fixed) and not fixed_feasible(m,limits,e,fixed-1)
                examples+=1
    return examples


def weight_kernel(repo):
    data=(repo/BOOK).read_bytes()
    assert hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()=='f056caab0db2b7612317f996b1718dc8e8188d5d'
    a=HERE.parent/'fortyfifth'/'recorder_check.py'
    b=HERE.parent/'ninetieth'/'recorders_check.py'
    assert hashlib.sha256(a.read_bytes()).hexdigest()=='b31b79efc8989d66dae6f3e589995c9b16763043393e049f11ee7a09e53db725'
    assert hashlib.sha256(b.read_bytes()).hexdigest()=='f1af1e08c97d50ca1996796774fc6f1693fcc4ace1d9453837345a46a9d49f31'
    sys.path[:0]=[str(a.parent),str(b.parent)]
    from recorder_check import local_match,load_kernel
    from recorders_check import signed_unit_contact
    return load_kernel(repo),local_match,signed_unit_contact


def native(brc,match,contact,limits,e,adaptive):
    cases=schedules(limits,e,adaptive)
    if not adaptive:
        n=len(cases[0][0][0])
        expected=[sum(comb(n,b)*sum(comb(n-b,a) for a in range(min(t,n-b)+1)) for b in range(e+1)) for t in limits]
        assert expected==list(map(len,cases))
    count=Counter()
    before=defaultdict(lambda:brc.CWM_ZERO)
    after=defaultdict(lambda:brc.CWM_ZERO)
    histogram=Counter()
    for j,a,r,direction,sheet in product(range(3),range(3),range(3),(-1,1),(-1,1)):
        d=direction*(j-a)%3
        for queries,answers in cases[d]:
            mass=brc.cwm_edge(F(1,108*len(cases[d])))
            counts=list(limits)
            ref=a
            for g,answer in zip(queries,answers):
                dest=(a+direction*g)%3
                turns=direction*(dest-ref)%3
                for _ in range(turns):
                    ref=(ref+direction)%3
                    mass=brc.cwm_propagate(mass,brc.CWM_ONE)
                    count['reference_steps']+=1
                physical=match(j,ref)
                assert physical==int(g==d)
                count['comparison']+=1
                count['marked_erasure' if answer==2 else ('answer_flip' if physical!=answer else 'correct_answer')]+=1
                mass=brc.cwm_propagate(mass,brc.CWM_ONE)
                if answer!=2:
                    counts=[t-int(answer!=int(g==i)) for i,t in enumerate(counts)]
            for _ in range(direction*(a-ref)%3):
                ref=(ref+direction)%3
                count['reference_steps']+=1
                mass=brc.cwm_propagate(mass,brc.CWM_ONE)
            decoded=[i for i,t in enumerate(counts) if t>=0]
            assert len(decoded)==1 and ref==a
            ports=[j,ref,r]
            final=contact(ports,2,direction*decoded[0],(1,sheet),mass,brc,count)
            assert ports==[j,a,(r+j-a)%3]
            before[(r-a)%3]=brc.cwm_recoalesce(before[(r-a)%3],mass)
            after[(ports[2]-j)%3]=brc.cwm_recoalesce(after[(ports[2]-j)%3],final)
            histogram[len(queries)]+=1
    assert before==after and sum(v.total for v in after.values())==1
    return dict(limits=limits,erasures=e,adaptive=adaptive,transcripts_by_offset=list(map(len,cases)),
                source_states=27,frames_per_state=4,executed_branches=sum(histogram.values()),
                query_length_counts=dict(histogram),costs=dict(count),final_difference_masses=[str(after[i].total) for i in range(3)])


def distances(A,p):
    return [sum((i in A)!=((i+h)%p in A) for i in range(p)) for h in range(1,p)]


def determinant(matrix):
    x=[row[:] for row in matrix]
    last=1
    sign=1
    for i in range(len(x)-1):
        k=next(k for k in range(i,len(x)) if x[k][i])
        if i!=k: x[i],x[k]=x[k],x[i];sign=-sign
        pivot=x[i][i]
        for k in range(i+1,len(x)):
            for j in range(i+1,len(x)):
                t=pivot*x[k][j]-x[k][i]*x[i][j]
                assert t%last==0
                x[k][j]=t//last
        last=pivot
    return sign*x[-1][-1]


def modular_rank(rows, prime):
    matrix = [[v % prime for v in row] for row in rows]
    rank = 0
    for col in range(len(matrix[0])):
        pivot = next((r for r in range(rank, len(matrix)) if matrix[r][col]), None)
        if pivot is None:
            continue
        matrix[pivot], matrix[rank] = matrix[rank], matrix[pivot]
        inverse = pow(matrix[rank][col], -1, prime)
        for r in range(rank + 1, len(matrix)):
            coeff = matrix[r][col] * inverse % prime
            matrix[r] = [(a - coeff * b) % prime for a, b in zip(matrix[r], matrix[rank])]
        rank += 1
    return rank


def residue_masks():
    entries=[]
    for p in range(3,102,2):
        if any(p%i==0 for i in range(2,isqrt(p)+1)):continue
        A={i*i%p for i in range(1,p)}
        profile=distances(A,p)
        bound=(p+1)//2 if p%4==3 else (p-1)//2
        assert min(profile)==bound
        brute=None
        if p<=13:
            brute=max(min(distances({i for i in range(p) if mask>>i&1},p)) for mask in range(1<<p))
            assert brute==bound
        det=None
        normalized_ranks=None
        if p<=31:
            matrix=[[int((j-i)%p in A) for j in range(p)] for i in range(p)]
            det=abs(determinant(matrix))
            differences=[[row[j]-row[-1] for j in range(p-1)] for row in matrix[:-1]]
            normalized_ranks={ell:modular_rank(differences,ell) for ell in (2,3,5,7,11,13,p)}
            c=(p+1)//4 if p%4==3 else (p-1)//4
            assert all((rank==p-1)==(c%ell!=0) for ell,rank in normalized_ranks.items())
            assert det==len(A)*(((p+1)//4 if p%4==3 else (p-1)//4)**((p-1)//2))
        entries.append(dict(p=p,distance_multiplicities=dict(Counter(profile)),all_masks_best=brute,
                            absolute_incidence_determinant=det, fixed_total_modular_ranks=normalized_ranks))
    return entries


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--repo',required=True,type=Path)
    args=ap.parse_args()
    brc,match,contact=weight_kernel(args.repo)
    native_checks=[native(brc,match,contact,t,e,a) for t,e in [((0,0,0),0),((0,1,1),2),((1,1,1),1)]
                   for a in (False,True)]
    out=dict(exact_robust_budget_cases=resource_grid(),native_positive_recordings=native_checks,
             cyclic_incidence=residue_masks())
    print(json.dumps(out,indent=2,sort_keys=True))
if __name__=='__main__': main()
