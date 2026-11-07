"""EC49CB: exact X6 signed-word BRC, block CRT and finite-field root filter.
No external packages; requires the unchanged EC49CA native_signed_brc.py.
This checks finite combinatorial BRC, not physical heartbeat propagation.
"""
import itertools
import json
import sys
from pathlib import Path

source = Path(__file__).resolve().parents[1] / 'EC49CA_CRT'
if not source.exists():
    source = Path(__file__).resolve().parent / 'EC49CA_CRT'  # local evidence bundle
sys.path.insert(0, str(source))
from native_signed_brc import endpoint_weight, endpoint_multiplicity

S = tuple(range(1,7)) + tuple(range(-1,-7,-1))
W = (2,3,3,2,1,1)
Z = (0,)*6
Q = tuple((a,b) for a in range(3) for b in range(3))
QID = {s:i for i,s in enumerate(Q)}
LABELS = ('00','01','10','11')

def swap(a):
    if abs(a)==1: return 2 if a>0 else -2
    if abs(a)==2: return 1 if a>0 else -1
    return a

def step(q,a):
    return 2 if q==2 or (q==1 and a==2) else (1 if a==1 else 0)

NEXT = tuple(tuple(QID[(step(u,a),step(v,swap(a)))] for a in S) for u,v in Q)
ATOMS = tuple('%d%d'%(u==2,v==2) for u,v in Q)

def prime(p):
    return p>=2 and all(p%d for d in range(2,int(p**.5)+1))

def spectral(n,L,p):
    # The identity also computes aliased sums when L does not meet the bound.
    assert n%2==0 and prime(p) and (p-1)%L==0
    if L==1: omega=1
    else:
        assert L in (2,3,5)  # verified prime-period cases in this certificate
        omega=next(pow(x,(p-1)//L,p) for x in range(2,100)
                   if pow(x,(p-1)//L,p)!=1)
        assert pow(omega,L,p)==1
    roots=[pow(omega,j,p) for j in range(L)]
    sums={a:[0,0,0] for a in LABELS}
    for es in itertools.product(range(L),repeat=6):
        x=[roots[e] for e in es]
        y=[roots[(-e)%L] for e in es]
        c0=[x[j]*W[j]%p for j in range(6)]+y
        c1=[x[j]*W[abs(swap(j+1))-1]%p for j in range(6)]+y
        c2=x+y
        v=[[0,0,0] for _ in Q];v[0]=[1,1,1]
        for _ in range(n):
            nxt=[[0,0,0] for _ in Q]
            for q,(a,b,c) in enumerate(v):
                if (a,b,c)==(0,0,0): continue
                for j,dst in enumerate(NEXT[q]):
                    row=nxt[dst]
                    row[0]=(row[0]+a*c0[j])%p
                    row[1]=(row[1]+b*c1[j])%p
                    row[2]=(row[2]+c*c2[j])%p
            v=nxt
        for i,vec in enumerate(v):
            row=sums[ATOMS[i]]
            for j in range(3): row[j]=(row[j]+vec[j])%p
    inv=pow(pow(L,6,p),-1,p)
    return {a:[v*inv%p for v in sums[a]] for a in LABELS},omega

def block(n,ps):
    k=len(ps)
    layer={(Z,0):[1]*(3*k)}
    peak=1
    for t in range(n):
        nxt={}
        for (z,q),v in layer.items():
            for i,a in enumerate(S):
                axis=abs(a)-1
                zz=z[:axis]+(z[axis]+(1 if a>0 else -1),)+z[axis+1:]
                if sum(abs(x) for x in zz)>n-t-1: continue
                key=(zz,NEXT[q][i]);dst=nxt.setdefault(key,[0]*(3*k))
                wa=W[a-1] if a>0 else 1
                wb=W[abs(swap(a))-1] if a>0 else 1
                for j,p in enumerate(ps):
                    h=3*j
                    dst[h]=(dst[h]+wa*v[h])%p
                    dst[h+1]=(dst[h+1]+wb*v[h+1])%p
                    dst[h+2]=(dst[h+2]+v[h+2])%p
        layer=nxt;peak=max(peak,len(layer))
    residues=[{a:[0,0,0] for a in LABELS} for _ in ps]
    for (z,q),v in layer.items():
        if z!=Z:continue
        for j,p in enumerate(ps):
            dst=residues[j][ATOMS[q]]
            for c in range(3):dst[c]=(dst[c]+v[3*j+c])%p
    return residues,peak

def lift(rs,ps):
    x=0;M=1
    for r,p in zip(rs,ps):
        x+=M*(((r-x)*pow(M,-1,p))%p);M*=p
    return x

def check():
    expected={
      0: [[1,1,1],[0,0,0],[0,0,0],[0,0,0]],
      2: [[24,24,12],[0,0,0],[0,0,0],[0,0,0]],
      4: [[1488,1488,384],[36,36,6],[36,36,6],[0,0,0]],
      6: [[139320,139320,18744],[6480,6480,576],[6480,6480,576],[360,360,24]],
      8: [[16560120,16560120,1170120],[1129320,1129320,53850],
          [1129320,1129320,53850],[102240,102240,3600]]}
    cases=[]
    for n,L,ps in [(0,1,[100000081]),(2,3,[100000081]),
                   (4,3,[7,13,19]),(6,5,[100000081]),(8,5,[100000081])]:
        M=1
        for p in ps:M*=p
        weighted=int(endpoint_weight(n,Z,W,(1,)*6))
        count=endpoint_multiplicity(n,Z)
        assert M>weighted
        per_mod=[spectral(n,L,p)[0] for p in ps]
        atom={a:[lift([row[a][j] for row in per_mod],ps) for j in range(3)] for a in LABELS}
        assert [atom[a] for a in LABELS]==expected[n]
        assert [sum(atom[a][j] for a in LABELS) for j in range(3)]==[weighted,weighted,count]
        if n>=4:
            res,peak=block(n,ps)
            assert res==per_mod
        else:peak=None
        cases.append(dict(n=n,L=L,primes=ps,modulus_product=M,native_weight=weighted,
                          native_count=count,root_points=L**6,peak_block_states=peak,atoms=atom))
    alias=[]
    for n,L in [(4,2),(6,3)]:
        p=100000081
        atom,_=spectral(n,L,p)
        actual=[int(endpoint_weight(n,Z,W,(1,)*6))]*2+[endpoint_multiplicity(n,Z)]
        observed=[sum(atom[a][j] for a in LABELS) for j in range(3)]
        assert 18**n<p and all(observed[j]>actual[j] for j in range(3))
        alias.append(dict(n=n,L=L,modulus=p,aliased_totals=observed,
                          native_totals=actual,excess=[observed[j]-actual[j] for j in range(3)]))
    result=dict(schema='EC49CB_EXACT_PORTABLE_V1',
        scope='ordered signed X6 closed paths, H={id,(1 2)}, joint DFA of substrings (+E1,+E2) and (+E2,+E1)',
        native_source_git_blob='300a96e3dc24bf6fff73743037a0347a8bc83176',
        theory='for even n: no period-L alias iff odd L and 2L>n, or even L and L>n',
        status='AUTHOR_EXACT_FINITE_AUDIT; UNREVIEWED; NOT_ADMITTED',
        cases=cases,aliases=alias)
    Path(__file__).with_name('EXACT_REPORT_EC49CB.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print('EC49CB_EXACT_PASS',[(r['n'],r['L'],r['native_weight']) for r in cases])
    return result

if __name__=='__main__':check()
