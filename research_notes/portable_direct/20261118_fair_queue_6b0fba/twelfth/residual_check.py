"""Exact integer finite-volume certificate. Python standard library only."""
from collections import Counter
from hashlib import sha256
from itertools import product
from math import comb
import argparse
import json
from pathlib import Path


def advance(q,r):
    n=len(q)
    # Split before adding the carry, even if q is the largest machine word.
    lo=[(v&7)+h for v,h in zip(q,r)]
    f=[(v>>3)+(b>>3) for v,b in zip(q,lo)]
    next_q=[(q[i]-f[i])+f[i-1] for i in range(n)]
    next_r=[b&7 for b in lo]
    assert sum(q)==sum(next_q) and min(next_q)>=0
    assert all(a*8+b==v+h for a,b,v,h in zip(f,next_r,q,r))
    return next_q,next_r,f


def project(q0,h):
    return [q0[i]+h[i]-(h[i]//8)+(h[i-1]//8) for i in range(len(h))]


def verify_case(q0,r0,T,budget):
    n=len(q0)
    full=list(q0);q=list(q0); rf=list(r0);r=list(r0)
    xf=[0]*n;x=[0]*n;y=list(r0);e=0
    max_q=max_face=max_region=0
    mass=sum(q0)
    for t in range(1,T+1):
        full,rf,ff=advance(full,rf);q,r,f=advance(q,r)
        xf=[u+v for u,v in zip(xf,ff)];x=[u+v for u,v in zip(x,f)]
        lost=[0]*n
        if e<budget and t%3!=0:
            for i in range(n):
                if (i+t)%3!=0 and 0<r[i]<=1+(t%7):
                    lost[i]=r[i]
                    r[i]=0
            e+=any(lost)
        y=[u-v for u,v in zip(project(q0,y),lost)]
        assert y==[8*u+v for u,v in zip(x,r)]
        yf=[8*u+v for u,v in zip(xf,rf)]
        assert all(0<=v-u<=8*e for v,u in zip(yf,y))
        df=[v-u for v,u in zip(xf,x)]
        dq=[v-u for v,u in zip(full,q)]
        assert all(0<=a<=e for a in df)
        assert dq==[df[i-1]-df[i] for i in range(n)]
        assert sum(q)==mass and max(q)<=max(q0)+t
        # Enumerate every oriented connected region, including wrap and full ring.
        region=max(abs(sum(dq[(a+k)%n] for k in range(length))) for a in range(n) for length in range(1,n+1))
        assert region<=e
        max_q=max(max_q,*map(abs,dq));max_face=max(max_face,*df);max_region=max(max_region,region)
    return [max_q,max_face,max_region,e]


def independent_sets(n):
    def visit(bits):
        if len(bits)==n:
            if not(bits[0] and bits[-1]): yield bits
            return
        yield from visit(bits+(0,))
        if not bits or not bits[-1]: yield from visit(bits+(1,))
    return visit(())


def collision(n,K=2):
    C=8*K+7
    counts=Counter(); observed=set(); histograms={}
    for mask in independent_sets(n):
        k=sum(mask); initial=[C+mask[i]-mask[i-1] for i in range(n)]
        flat,r,_=advance(initial,[0]*n)
        assert flat==[C]*n and r==[7-7*mask[i]-mask[i-1] for i in range(n)]
        expected=tuple(sorted(r))
        if k in histograms: assert histograms[k]==expected
        histograms[k]=expected
        next_q,_,_=advance(flat,r)
        assert next_q==initial and tuple(next_q) not in observed
        counts[k]+=1;observed.add(tuple(next_q))
    for k,value in counts.items():
        assert value==n*comb(n-k,k)//(n-k)
    return dict(n=n,total=len(observed),by_population=dict(sorted(counts.items())))


def block_view(mask,K=0):
    n=len(mask);c=8*K+7;q=[c+mask[i]-mask[i-1] for i in range(n)]
    flat,r,_=advance(q,[0]*n)
    after,_,_=advance(flat,r)
    assert after==q
    assert all(sorted(r[i:i+4])==[0,6,7,7] for i in range(0,n,4))
    return dict(q0=q,q1=flat,r1=r,q2=after)


def compositions(total,n):
    if n==1:
        yield (total,)
    else:
        for first in range(total+1):
            for tail in compositions(total-first,n-1):
                yield (first,)+tail


def flat_preimages():
    checked=0; counts=[]
    # Brute force all nonnegative inputs with the required conserved mass.
    for n,K in ((3,0),(3,1),(4,0),(4,1)):
        for s in range(8):
            c=8*K+s;actual=set()
            for q in compositions(n*c,n):
                checked+=1
                flux=tuple(v//8 for v in q)
                if all(q[i]+flux[i-1]-flux[i]==c for i in range(n)):
                    actual.add(q)
            if s==7 or (s==0 and K>0):
                sign=1 if s==7 else -1
                predicted={tuple(c+sign*(d[i]-d[i-1]) for i in range(n)) for d in independent_sets(n)}
            else:
                predicted={(c,)*n}
            assert actual==predicted
            counts.append([n,K,s,len(actual)])
    return dict(compositions_examined=checked,number_of_flat_targets=len(counts),counts=counts)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--output',type=Path)
    args=p.parse_args()
    checks=0;cases=[];largest=[0]*4
    for n,values,rs in [(2,(0,1,7,8),(0,1,6,7)),(3,(0,7,8),(0,7))]:
        for q0 in product(values,repeat=n):
            for r0 in product(rs,repeat=n):
                for budget in (0,1,2,4):
                    got=verify_case(q0,r0,8,budget)
                    largest=list(map(max,zip(largest,got)));cases.append(got);checks+=1
    for q0 in ((2**32-1,0,0),(0,1,2**32-2),(2**32-5,2,1),(0,2**64-1)):
        cases.append(verify_case(q0,(7,)*len(q0),24,3))
    collision_cases=[collision(n) for n in (4,8,12,16)]
    block=[]
    for n in (4,8,12,16):
        rows=[]
        for choice in product((1,2),repeat=n//4):
            code=[0]*n
            for i,b in enumerate(choice):code[4*i+b]=1
            rows.append((choice,block_view(code)['q2']))
        for c,v in rows:
            for d,w in rows:
                h=sum(x!=y for x,y in zip(c,d));delta=[a-b for a,b in zip(v,w)]
                assert max(map(abs,delta))==2*bool(h) and sum(u*u for u in delta)==6*h
        block.append([n,len(rows)])
    out={'entire_uniform_image_fibres':flat_preimages(),'systematic_seed_states_times_budgets':checks,'systematic_steps_per_case':8,
         'extra_machine_boundary_cases':4,'systematic_max_field_face_region_epochs':largest,
         'all_contract_cases_sha256':sha256(json.dumps(cases,separators=(',',':')).encode()).hexdigest(),
         'reachable_flat_profile_independent_sets':collision_cases,
         'fixed_each_block_histogram_counts':block,
         'four_cell_move_left':block_view((0,1,0,0)), 'four_cell_move_right':block_view((0,0,1,0))}
    content=json.dumps(out,indent=2,sort_keys=True)+'\n'
    print(content,end='')
    if args.output:args.output.write_text(content)


if __name__=='__main__':main()
