"""Exact T08 shortest-arrival bridge; Python standard library plus the pinned U27 source."""
import argparse
import hashlib
import importlib.util
import json
from fractions import Fraction as F
from math import comb, gcd, isqrt, lcm
from pathlib import Path
import sys

PLAN_BYTES='{"version":"U27F09-two-axis-first-arrival-v1","prepare":"For each N>=2 and k=0,...,N set A=0, B=k*E1+(N-k)*E2, C=(N+1)*E3, D=(N+1)*E4; empty links; U21 original four labelled deposited IDs. Do not query prime labels, factors, residue tables or square shells.","read":"Full first A--B contact at proposal N with A stationary and side A paid at its original location. Retain positive branch count, total and dominant; use ratio to k=0 at same N. No retries or success conditioning.","tiers":[[2,12],[13,32]],"endpoints":"Exclude k=0,N from arithmetic interior; compare gcd progression and first k where N fails to divide coefficient. Compute classifications using independent trial division only after both sets of rows have been generated.","mix":"Check coeffwise gcd, unordered axis swap, uniform interior sum, integer-mixture fixed divisor, and known-budget reconstruction. Treat mixed initial laws as observers paid separately from dynamics.","control":"One fixed-distance preparation cannot stand for the remaining slices. An extension by E1 can distinguish previously reflected labelled states at the same N."}\n'
PLAN_SHA='ef7e522c73bfc5a4462eb7541e6cdcbcb70a9033eb688f606d6d51552d16dd50'
MANIFEST='e6a86c8ab44f674b126844358e893d893d0c58b6e16353c89660ff35adfafdb5'
ARCHIVE='a450cc3e235ca3d37211d31b2d4eb41dd2d4ac28b77c73d18d1b6e3ce45cc9a7'

def load(root):
    raw=(root/'PACKAGE_MANIFEST.json').read_bytes()
    assert hashlib.sha256(raw).hexdigest()==MANIFEST
    entries=json.loads(raw)['files']
    for name,data in entries.items():
        assert hashlib.sha256((root/name).read_bytes()).hexdigest()==data['sha256']
    path=root/'baseline/cell_u27/reuse/contact_network.py'
    spec=importlib.util.spec_from_file_location('bridge_u21',path)
    c=importlib.util.module_from_spec(spec)
    sys.modules[spec.name]=c
    spec.loader.exec_module(c)
    return c,len(entries)

def accept(K,s,label):
    found=[(y,w) for y,w,out in K.transition(s,label) if out=='ACCEPT']
    assert len(found)==1
    return found[0]

def point(*axis):return tuple(axis)+(0,)*(6-len(axis))

def line(c,K,N):
    # Only event paths can succeed at the earliest tick. The kernel still uses
    # its full original proposal weights, including the unobserved outcomes.
    r=c.r
    residual={}
    receipts=0
    for m in range(1,N+1):
        for i in range(m+1):
            j=m-i
            cells=(point(),point(i,j),point(0,0,N+1),point(0,0,0,N+1))
            state=c.m.make(cells,{})
            if m==1:
                y,weight=accept(K,state,('contact',(0,1),0))
                inv=c.ContactInventory.empty(cells)
                event=inv.toggle((0,1),0,0)
                assert event['birth'] and inv.state==y and event['token']==0
                receipts+=1
            else:
                paths=[]
                for axis,(a,b) in enumerate(((i-1,j),(i,j-1))):
                    if min(a,b)<0:continue
                    for grow in (False,True):
                        y,w=accept(K,state,('body',1,2*axis+1,grow))
                        assert y.cells[1]==point(a,b) and not y.links
                        paths.append(r.serial(w,residual[a,b]))
                weight=r.total(paths)
            residual[i,j]=weight
    edges=[residual[k,N-k] for k in range(N+1)]
    zero=edges[0]
    assert zero.total==F(1,2352)*F(1,192)**(N-1)
    assert zero.count==2**(N-1)
    vals=[]
    for w in edges:
        ratio=w.total/zero.total
        assert ratio.denominator==1 and w.count==zero.count*ratio and w.dominant==zero.dominant
        vals.append(int(ratio))
    bias_checks={}
    for t in (1,2):
        Z=sum(t**k for k in range(1,N))
        mix=r.total(r.serial(r.edge(F(t**k,Z)),edges[k]) for k in range(1,N))
        recovered=mix.total*Z/zero.total
        assert recovered==sum(vals[k]*t**k for k in range(1,N))
        bias_checks[str(t)]=dict(initial_weight_denominator=Z,recovered_integer=int(recovered))
    return vals,dict(base_count=zero.count,base_total=str(zero.total),one_label_dominant=str(zero.dominant),
                     positive_mixtures_replayed=bias_checks,
                     actual_terminal_receipts=receipts,computed_states=len(residual))

def prime(n):
    return n>=2 and not any(n%d==0 for d in range(2,isqrt(n)+1))

def mu(n):
    sign=1
    for p in range(2,isqrt(n)+1):
        if n%p==0:
            sign*=-1
            n//=p
            if n%p==0:return 0
    return -sign if n>1 else sign

def primitive(row,N,k):
    return sum(mu(d)*row[N//d][k//d] for d in range(1,gcd(N,k)+1) if N%d==0 and k%d==0)

def classify(all_rows):
    out=[]
    row={1:[1,1],**{v['N']:v['values'] for v in all_rows}}
    for source in all_rows:
        N=source['N']
        a=source['values']
        assert a==[comb(N,k) for k in range(N+1)] and a==list(reversed(a))
        g=0
        P=1
        profile=[]
        for k in range(1,N):
            g=gcd(g,a[k])
            P=lcm(P,k)
            assert g==N//gcd(N,P)
            profile.append(g)
        fullg=profile[-1]
        first_bad=next((k for k in range(1,N) if a[k]%N),None)
        labelled=prime(N)
        assert (first_bad is None)==labelled
        assert first_bad==next((i for i in range(2,N) if N%i==0),None)
        root=[a[k]-primitive(row,N,k) for k in range(1,N)]
        assert all(x>=0 and (a[k]-x)%N==0 for k,x in enumerate(root,1))
        assert (not any(root))==labelled
        fixed=0
        for t in range(1,N+1):
            value=sum(a[k]*t**k for k in range(1,N))
            assert value==(1+t)**N-t**N-1
            fixed=gcd(fixed,value)
        predicted=1
        for p in range(2,N+1):
            if prime(p) and (N-1)%(p-1)==0:predicted*=p
        assert fixed==predicted
        out.append(dict(**source,gcd_profile=profile,coefficient_content=fullg,
                        first_nondivisible_k=first_bad,root_residuals=root,
                        integer_mixture_fixed_divisor=fixed,trial_division_prime=labelled))
    return out

def blind_roots(rows):
    seen=0
    for entry in rows:
        N=entry['N']
        if N>12:continue
        direct=[0]*(N+1)
        for word in range(1,2**N-1):
            text=tuple((word>>j)&1 for j in range(N))
            if any(N%s==0 and text==text[:s]*(N//s) for s in range(1,N)):
                direct[word.bit_count()]+=1
        assert direct[1:-1]==entry['root_residuals']
        seen+=2**N-2
    return seen

def controls():
    examples={}
    for n,k in ((341,11),(561,3)):
        mixed=[(pow(1+t,n,n)-pow(t,n,n)-1)%n for t in range(n)]
        examples[n]=dict(first_raw_failure=[k,comb(n,k)%n],uniform_residue=mixed[1],
                         histogram={str(r):mixed.count(r) for r in sorted(set(mixed))},
                         every_integer_bias_passes=not any(mixed))
        assert prime(k) and n%k==0 and comb(n,k)%n==n//k
    assert examples[341]['uniform_residue']==0 and not examples[341]['every_integer_bias_passes']
    assert examples[561]['every_integer_bias_passes']
    return examples

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--bundle-dir',required=True,type=Path)
    root=parser.parse_args().bundle_dir
    assert hashlib.sha256(PLAN_BYTES.encode()).hexdigest()==PLAN_SHA
    c,count=load(root)
    K=c.Kernel()
    raw=[]
    for lo,hi in json.loads(PLAN_BYTES)['tiers']:
        for n in range(lo,hi+1):
            values,data=line(c,K,n)
            raw.append(dict(N=n,values=values,source=data))
    work=dict(c.r.CALLS)
    tested=classify(raw)
    witness=[row for row in tested if row['N']==12][0]
    assert witness['values'][6]==924 and 924%12==0 and witness['root_residuals'][5]>0
    result=dict(plan=json.loads(PLAN_BYTES),plan_byte_sha256=PLAN_SHA,source_manifest_sha256=MANIFEST,
                source_archive_sha256=ARCHIVE,verified_files=count,source_labels=len(K.proposals),
                rows=tested,source_brc_calls=work,exhaustive_raw_words_checked=blind_roots(tested),
                large_algebraic_controls=controls(),source_preparations=sum(n+1 for n in range(2,33)))
    print(json.dumps(result,indent=2,sort_keys=True))
if __name__=='__main__': main()
