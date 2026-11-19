"""Marked heat rates, real helical chain lifts, and rational Perron enclosures."""
import argparse
from fractions import Fraction
from hashlib import sha256
from itertools import product
from math import isqrt, sqrt
from pathlib import Path
from runpy import run_path
import json


K=(1,0,0)
SOURCE_FILE='research_notes/ns-causal-inverse-newton-basin-20260909/inherited_fourier.py'
SOURCE_HASH='ac6a0a34994c85832bde55e38e195e9552df308906f1a4c4460d3dbdafb1db59'


def dot(x,y):
    return sum(a*b for a,b in zip(x,y))


def cross(x,y):
    return (x[1]*y[2]-x[2]*y[1],x[2]*y[0]-x[0]*y[2],x[0]*y[1]-x[1]*y[0])


def subtract(x,y):
    return tuple(a-b for a,b in zip(x,y))


def conjugate(x):
    return tuple(a.conjugate() for a in x)


def scale(c,x):
    return tuple(c*a for a in x)


def feasible(k,n):
    if n<=0:
        return False
    t=sum(a%2 for a in k)
    axis=sum(a!=0 for a in k)==1
    if t==0:
        if n%4:
            return False
        m=n//4
        while m%4==0:
            m//=4
        return m%8!=7 and not(axis and m==1)
    if t==1:
        return n%4==1 and not(axis and n==1)
    if t==2:
        nonzero=[abs(a) for a in k if a]
        equal_pair=len(nonzero)==2 and nonzero[0]==nonzero[1]
        return n%4==2 and not(equal_pair and n==2)
    return n%8==3


def direct_parents(k,nmax):
    # Enumerate unordered pairs directly on the original two-parent lattice.
    rows={}
    r=isqrt(nmax)
    for p in product(*(range((a-r+1)//2,(a+r)//2+1) for a in k)):
        q=subtract(k,p)
        if p>=q or dot(p,p)==dot(q,q) or cross(p,q)==(0,0,0):
            continue
        n=dot(subtract(p,q),subtract(p,q))
        if n<=nmax:
            rows[n]=rows.get(n,0)+1
    return rows


def test_arithmetic():
    nmax=768
    tests=0
    samples={}
    for k in product(range(5),repeat=3):
        if not any(k):
            continue
        actual=direct_parents(k,nmax)
        assert set(actual)=={n for n in range(nmax+1) if feasible(k,n)}
        unique=[n for n,count in actual.items() if count==1]
        labelled_odds=[a for a in k if a%2]
        expected_single=[]
        if len(labelled_odds)==1 and sum(bool(a) for a in k)>1:
            expected_single=[1]
        if len(labelled_odds)==2 and labelled_odds[0]==labelled_odds[1] and all(k):
            expected_single=[2]
        assert unique==expected_single
        tests+=nmax+1
        if k in (K,(1,1,0),(1,1,1),(2,0,0),(2,2,0),(1,2,0),(1,3,0)):
            samples[str(k)]={'rate_count':len(actual),
                           'first_N_and_unordered_pairs':[[n,actual[n]] for n in sorted(actual)[:12]]}
        if k==K:
            assert min(actual.values())>=4
    return {'N_max':nmax,'outputs':124,'tested_output_and_N':tests,'samples':samples}


def helical(v):
    # Exactly the frozen phase-two basis on coordinate planes. A projected
    # real reference covers the remaining frequencies in our independent test.
    r=sqrt(dot(v,v))
    ref=next((j for j,a in enumerate(v) if a==0),min(range(3),key=lambda j:abs(v[j])))
    e=tuple((1 if i==ref else 0)-v[i]*v[ref]/(r*r) for i in range(3))
    e=scale(1/sqrt(dot(e,e)),e)
    return tuple(a+1j*b/r for a,b in zip(e,cross(v,e)))


def read(v):
    # Scalar coordinate along h_-(k)=(0,i,1), whose squared norm is 2.
    return (-1j*v[1]+v[2])/2


def edge_response(v,prev):
    c=read(cross(helical(v),conjugate(helical(prev))))*(sqrt(dot(v,v))-sqrt(dot(prev,prev)))
    assert abs(c)>1e-12
    return c


def prefix(max_rate):
    chains={}
    r=isqrt(max_rate)
    for y,z in product(range(-r,r+1),repeat=2):
        if not(y>0 or (y==0 and z>0)):
            continue
        starts=[]
        for j in range(-r,r+1):
            rate=j*j+(j-1)**2+2*(y*y+z*z)
            if rate<=max_rate:
                starts.append(j)
        if starts:
            assert starts==list(range(min(starts),max(starts)+1))
            chains[y,z]=starts
    return chains


def targets(labels, desired):
    per_rate={}
    for yz,indices in labels.items():
        for j in indices:
            rate=j*j+(j-1)**2+2*dot(yz,yz)
            per_rate.setdefault(rate,[]).append((yz,j))
    if set(desired)!=set(per_rate):
        raise ValueError("every attained rate must have a declared target, including zero")
    weights={}
    for rate,entries in per_rate.items():
        z=desired[rate]
        if len(entries)==1:
            assert z!=0
            weights[entries[0]]=z
        else:
            a=1 if z!=len(entries)-1 else 2
            for edge in entries[:-1]:
                weights[edge]=a
            weights[entries[-1]]=z-(len(entries)-1)*a
    assert all(weights.values())
    return weights


def lift(chains,weights):
    modes={}
    max_vertex=0
    for yz,indices in sorted(chains.items()):
        old=None
        for j in sorted(indices):
            v=(j,)+yz
            prev=(j-1,)+yz
            if old!=j-1:
                amplitude=1+0j
                modes[prev]=helical(prev)
            c=edge_response(v,prev)
            amplitude=weights[(yz,j)]/(c*amplitude.conjugate())
            modes[v]=scale(amplitude,helical(v))
            old=j
            max_vertex=max(max_vertex,abs(amplitude))
    for v,h in list(modes.items()):
        minus=tuple(-a for a in v)
        assert minus not in modes
        modes[minus]=conjugate(h)
    # Separate full ordered convolutions until after accumulating at (k,rate).
    raw={}
    count={}
    for p,a in modes.items():
        q=subtract(K,p)
        if q not in modes:
            continue
        rate=dot(p,p)+dot(q,q)
        ab=scale(-sqrt(dot(q,q)),cross(a,modes[q]))
        old=raw.get(rate,(0,0,0))
        raw[rate]=tuple(i+j for i,j in zip(old,ab))
        count[rate]=count.get(rate,0)+1
    return {r:read(b) for r,b in raw.items()},count,max_vertex


def sample_lifts():
    chains=prefix(35)
    rates=sorted({j*j+(j-1)**2+2*dot(yz,yz) for yz,items in chains.items() for j in items})
    assert rates==list(range(3,36,2))
    wanted={s: complex(s%5-2,s%3-1) if s%7 else 0j for s in rates}
    mixed=targets(chains,wanted)
    got,count,maximum=lift(chains,mixed)
    err=max(abs(got[r]-wanted[r]) for r in rates)
    assert err<1e-9
    # Fixed sparse support with two chosen edges and one unavoidable connector.
    samples=[]
    for power in (1,3,6):
        eps=10.**(-power)
        q={(1,0):[2,3,4]}
        values={((1,0),2):1+2j,((1,0),3):eps,((1,0),4):-2+1j}
        got2,_,maximum2=lift(q,values)
        assert max(abs(got2[r]-v) for r,v in ((7,1+2j),(15,eps),(27,-2+1j)))<2e-8
        samples.append({'epsilon':'1e-'+str(power),'connector_observed':format(abs(got2[15]),'.9g'),
                        'largest_vertex_amplitude':format(maximum2,'.7g')})
    return {'prefix_max_rate':35,'chain_count':len(chains),'target_and_ordered_pair_count':
            [[r,[int(wanted[r].real),int(wanted[r].imag)],count[r]] for r in rates],
            'prefix_absolute_tolerance':'1e-9','prefix_largest_vertex_amplitude':format(maximum,'.7g'),
            'single_chain_approximating_samples':samples}


def general_lift(k,max_rate):
    # A representative b for v+Zk has 0 <= b.k < k.k. Keep the
    # lexicographically first member of the two distinct noncollinear chains.
    n2=dot(k,k)
    def base(v):
        j=dot(k,v)//n2
        return subtract(v,scale(j,k)),j

    def vertex(b,j):
        return tuple(a+j*c for a,c in zip(b,k))

    receiver=conjugate(helical(k))
    def observe(raw):
        return dot(conjugate(receiver),raw)/2

    r=isqrt(max_rate)
    byrate={}
    for v in product(range(-r,r+1),repeat=3):
        b,j=base(v)
        if b>=base(scale(-1,v))[0] or cross(v,k)==(0,0,0):
            continue
        prev=subtract(v,k)
        nv,np=dot(v,v),dot(prev,prev)
        if nv==np or nv+np>max_rate:
            continue
        byrate.setdefault(nv+np,[]).append((b,j))
    desired={r:complex((r+1)%3-1,r%3-1) if r%5 else 0j for r in byrate}
    singleton=[r for r,edges in byrate.items() if len(edges)==1]
    assert len(singleton)==1
    r0=singleton[0]
    b,j=byrate[r0][0]
    desired[r0]=0j
    forbidden={(b,j),(b,j+1)}
    other=[r for r,edges in byrate.items() if (b,j+1) in edges]
    assert len(other)==1 and len(byrate[other[0]])>=3
    desired[other[0]]=0j
    weights={}
    for r,edges in byrate.items():
        available=sorted(set(edges)-forbidden)
        if not available:
            assert desired[r]==0
            continue
        assert len(available)>=2
        c=(2 if desired[r]==len(available)-1 else 1)
        for e in available[:-1]:
            weights[e]=c
        weights[available[-1]]=desired[r]-(len(available)-1)*c
    assert all(weights.values())
    modes={}
    for (b,j),requested in sorted(weights.items()):
        v,prev=vertex(b,j),vertex(b,j-1)
        if prev not in modes:
            modes[prev]=1
        c=observe(cross(helical(v),conjugate(helical(prev))))*(sqrt(dot(v,v))-sqrt(dot(prev,prev)))
        assert v not in modes and abs(c)>1e-12
        modes[v]=requested/(c*modes[prev].conjugate())
    modes={v:scale(z,helical(v)) for v,z in modes.items()}
    for v,h in list(modes.items()):
        assert scale(-1,v) not in modes
        modes[scale(-1,v)]=conjugate(h)
    got={}
    for p,h in modes.items():
        q=subtract(k,p)
        if q in modes:
            rate=dot(p,p)+dot(q,q)
            got[rate]=got.get(rate,0j)-sqrt(dot(q,q))*observe(cross(h,modes[q]))
    allrates=sorted(set(got)|set(desired))
    assert max(abs(got.get(r,0j)-desired.get(r,0j)) for r in allrates)<1e-8
    return {'k':k,'max_rate':max_rate,'forced_zero_single_edge_rate':r0,
            'zeroed_vertex':vertex(*byrate[r0][0]),
            'other_zero_target_rate':other[0],'other_rate_multiplicity_before_deletion':len(byrate[other[0]]),
            'exact_rule_verified_to_absolute_tolerance':'1e-8','number_of_native_modes':len(modes),
            'intended_table':[[r,int(z.real),int(z.imag)] for r,z in sorted(desired.items())]}


def native_source(repo):
    import sympy as s
    path=repo/SOURCE_FILE
    assert sha256(path.read_bytes()).hexdigest()==SOURCE_HASH
    fn=run_path(str(path))['helical_data']
    chains=[[(j,1,0) for j in range(1,5)],[(j,0,1) for j in range(1,5)]]
    vertices=[v for chain in chains for v in chain]
    field=fn(vertices,[s.Integer(2)]*len(vertices))
    receiver=s.Matrix([0,s.I,1])
    coeffs=[]
    for chain in chains:
        row=[]
        for prev,v in zip(chain,chain[1:]):
            q=tuple(-a for a in prev)
            av,b=field[v],field[q]
            left=s.sqrt(dot(v,v));right=s.sqrt(dot(q,q))
            raw=-av.cross(right*b)-b.cross(left*av)
            c=s.simplify(receiver.conjugate().dot(raw)/2)
            assert s.simplify(c*s.conjugate(c)).is_positive
            assert abs(complex(c.evalf(16))-edge_response(v,prev))<1e-12
            row.append(c)
        coeffs.append(row)
    # Actual frozen coefficient c multiplies z_i conjugate(z_(i-1)).
    # SymPy cancellation is done before summing the two independent chains.
    desired=[1+s.I,0,-2+s.I]
    sums=[0]*3
    for idx,row in enumerate(coeffs):
        amplitude=s.Integer(1)
        for j,c in enumerate(row):
            value=s.Integer(1) if idx==0 else desired[j]-1
            new=value/(c*s.conjugate(amplitude))
            actual=s.simplify(c*new*s.conjugate(amplitude))
            assert actual==value
            amplitude=new
            sums[j]+=actual
    assert sums==desired
    return {'pinned_sha256':SOURCE_HASH,'helical_data_positive_vertices':len(vertices),
            'true_exact_ordered_pair_coefficients':[[str(a) for a in row] for row in coeffs],
            'rates':[7,15,27],'two_chain_exact_target':[str(a) for a in sums]}


def rational_bounds(nodes,average):
    # B_ij=2*y_j/(x_i+y_j) is diagonally similar to the square-root matrix.
    denom=len(nodes) if average else 1
    vector=[1.]*len(nodes)
    matrix=[[2*y/(x+y)/denom for y in nodes] for x in nodes]
    for _ in range(8):
        nxt=[dot(row,vector) for row in matrix]
        vector=[v/max(nxt) for v in nxt]
    v=[max(1,round(z*10**10)) for z in vector]
    digits=10**12
    lo,hi=None,None
    for x,w in zip(nodes,v):
        base=sum(2*y*u*digits//(x+y) for y,u in zip(nodes,v))
        a=Fraction(base,w*denom*digits)
        b=Fraction(base+len(nodes),w*denom*digits)
        lo=a if lo is None else min(a,lo)
        hi=b if hi is None else max(b,hi)
    return lo,hi


def outward(lo,hi):
    q=10**10
    return [lo.numerator*q//lo.denominator,-((-hi.numerator*q)//hi.denominator)]


def perron():
    continuous={}
    for n in (128,256,512):
        nodes=[2*n+2*i+1 for i in range(n)]
        lo,hi=rational_bounds(nodes,True)
        error=Fraction(1,8*n*n)
        continuous[str(n)]={'midpoint_matrix':outward(lo,hi),'integral_operator':outward(lo-error,hi+error)}
    finite={}
    for k in (K,(2,0,0),(1,1,1)):
        table=[]
        for A in (32,64,128,256,512):
            rates=[r for r in range(A,2*A) if feasible(k,2*r-dot(k,k))]
            lo,hi=rational_bounds(rates,False)
            table.append({'A':A,'count':len(rates),'rho':outward(lo,hi),'rho_per_rate':outward(lo/len(rates),hi/len(rates))})
        finite[str(k)]=table
    return {'integer_interval_denominator':10**10,'continuous':continuous,'dyadic':finite}


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--repo',type=Path,required=True,help='enterprise-math checkout containing the pinned helical_data')
    ap.add_argument('--out',type=Path)
    args=ap.parse_args()
    result={'arithmetic':test_arithmetic(),'helical_lifts':sample_lifts(),
            'singleton_zero_edge_lifts':[general_lift(k,64) for k in ((1,2,0),(1,1,2))],'source':native_source(args.repo),'perron':perron()}
    content=json.dumps(result,indent=2,sort_keys=True)+'\n'
    if args.out:args.out.write_text(content)
    else:print(content,end='')


if __name__=='__main__':
    main()
