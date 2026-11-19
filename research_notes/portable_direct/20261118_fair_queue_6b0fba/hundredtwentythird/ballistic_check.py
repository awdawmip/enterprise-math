"""Exact conditional-axis enumeration for the frozen six-axis H4/H5 return kernel."""
from argparse import ArgumentParser
from collections import Counter
from fractions import Fraction as F
from functools import cache
from hashlib import sha256
import json
from math import comb, factorial
from pathlib import Path

SOURCE_SHA = "4931b82017d44ba1d6b3a1b4c91c0d7a8557739f15d065a455dbdf4a72f03436"
STEPS = (1, 2, 3, 4, 6, 8, 12, 16, 24, 32, 48, 64, 96, 128)
OLD = ("9daf668d407d59db0e0e19ed9bb0b2a0a5f6d66c771f9e5148fa77189ba3f928",
       "b609839e74a85efe80446b37409b9e43a86af6c535f6eb3d77c61ffbbfdf10be")
AXES = ((1, 0, 0, 0), (0, 1, 0, 0), (-1,-1,0,0),
        (0, 0, 1, 0), (0, 0, 0, 1), (0,0,-1,-1))


@cache
def group(plus, minus):
    """One three-axis block. Negative occupancies determine the positives."""
    if (plus-minus)%3: return 0
    a = (plus-minus)//3
    total = 0
    for i in range(max(0,-a), minus+1):
        if not 0 <= i+a <= plus: continue
        for j in range(max(0,-a), minus-i+1):
            k = minus-i-j
            if min(i+a,j+a,k+a)<0: continue
            total += (comb(minus,i)*comb(minus-i,j) *
                      comb(plus,i+a)*comb(plus-i-a,j+a))
    return total


def conditional_words(plus,minus):
    return sum(comb(plus,i)*comb(minus,j)*group(i,j)*group(plus-i,minus-j)
               for i in range(plus+1)
               for j in range(i%3,minus+1,3))


def finite(horizon):
    visits=[{0:1}]
    first=[{}]
    for n in range(1,horizon+1):
        row={}
        for m in range(n%2,n//3+1,2):
            p=(n+3*m)//2
            weight=comb(n,p)*conditional_words(p,n-p)
            assert weight>0
            row[m]=row[-m]=weight
        taboo=row.copy()
        for k in range(1,n):
            for l,u in first[k].items():
                for j,v in visits[n-k].items(): taboo[l+j]-=u*v
        assert all(a>0 for a in taboo.values())
        visits.append(row); first.append(taboo)
    return visits,first


def raw(horizon):
    """Original labelled steps; absorb when either group first regains equality with the other two members of that group."""
    state=Counter({(0,)*6:1}); rows=[{}]
    for _ in range(horizon):
        alive=Counter(); hit=Counter()
        for x,weight in state.items():
            for i in range(6):
                for e in (-1,1):
                    y=x[:i]+(x[i]+e,)+x[i+1:]
                    if y[0]==y[2]==y[4] and y[1]==y[3]==y[5]:
                        hit[y[0]-y[1]]+=weight
                    else: alive[y]+=weight
        assert sum(alive.values())+sum(hit.values())==12*sum(state.values())
        state=alive; rows.append(dict(hit))
    return rows


def digest(rows):
    return sha256((''.join(f'{i},{m},{n}\n' for i,r in enumerate(rows)
                          for m,n in sorted(r.items()))).encode()).hexdigest()


@cache
def franel(j):
    return sum(comb(j,r)**3 for r in range(j+1))


def counts_at_edge(M):
    v=[comb(3*m,m)*comb(2*m,m)*franel(m) for m in range(M+1)]
    k=[0]
    for m in range(1,M+1): k.append(v[m]-sum(k[i]*v[m-i] for i in range(1,m)))
    return v,k


def product(a,b,n,p):
    out=[0]*(n+1)
    for i,x in enumerate(a):
        if x:
            for j,y in enumerate(b[:n-i+1]): out[i+j]=(out[i+j]+x*y)%p
    return out


def digits_product(n,p,table):
    out=1
    while n:
        n,d=divmod(n,p)
        out=out*(table[d] if d<len(table) else 0)%p
    return out


def arithmetic(visit,first):
    N=len(visit)-1
    cases=[]
    for p in (5,7,11,13,17,19,23,29,31,37,41,43):
        poly=[x%p for x in visit[:(p-1)//3+1]]
        assert all(digits_product(i,p,poly)==x%p for i,x in enumerate(visit))
        base=[1]+[-x%p for x in first[1:]]
        power=[1]
        for _ in range(p-1): power=product(power,base,N,p)
        assert power==poly+[0]*(N+1-len(poly))
        cases.append([p,poly])
    # Independent truncated renewal inverse well beyond the exact-integer Franel table.
    p=5; top=p**6
    nonzero=[(m,digits_product(m,p,[1,2])) for m in range(1,top)
             if digits_product(m,p,[1,2])]
    K=[0]*top
    for m in range(1,top):
        K[m]=(digits_product(m,p,[1,2])-sum(d*K[m-j] for j,d in nonzero if j<m))%p
        u,d=divmod(m,p)
        expected=-pow(2,m,p)*comb(4,d)*digits_product(u,p,[1,3,3,1])%p
        assert K[m]==expected
    nnz=[sum(bool(v) for v in K[1:p**k]) for k in range(1,7)]
    assert nnz==[5*4**(k-1)-1 for k in range(1,7)]
    return dict(exact_integer_through=N,mod_p_identities=cases,mod5_upper_exclusive=top,
                mod5_nonzero_counts=nnz,visits_mod5_nonzero_counts=[2**k-1 for k in range(1,7)])


def enclosure(l,u):
    scale=10**8
    return [l.numerator*scale//l.denominator,-((-u.numerator*scale)//u.denominator)]


def moment_vectors():
    # Fourier orthogonality; constant terms over the original four integer differences.
    z=(0,0,0,0)
    pos=Counter(AXES)
    neg=Counter({tuple(-u for u in v):n for v,n in pos.items()})
    def ct3(P,Q,R):
        return sum(w*x*R[tuple(-i-j for i,j in zip(a,b))]
                   for a,w in P.items() for b,x in Q.items())
    assert sum(v==tuple(-u for u in w) for v in AXES for w in AXES)==0
    assert sum(v==w for v in AXES for w in AXES)==6
    assert ct3(pos,pos,pos)==12 and ct3(pos,pos,neg)==0
    return {"integral_B2":"1/12","integral_Re_phi_B2":"-1/72","positive_triples":12}


def main(source):
    visits,first=finite(128)
    assert raw(8)==first[:9]
    assert (digest(visits),digest(first))==OLD
    marginal=[F(sum(row.values()),12**n) for n,row in enumerate(visits)]
    frozen=sha256(('\n'.join(str(marginal[i]) for i in STEPS)+'\n').encode()).hexdigest()
    assert frozen=='5b0835054cce814727fedd4a10879eeef753616c29ca17f66c8a2ca8967ee1d9'
    if source:
        blob=source.read_bytes()
        assert sha256(blob).hexdigest()==SOURCE_SHA
        packet=json.loads(blob)
        assert packet['U']==[['1','0']*3,['0','1']*3]
        assert packet['routing_cases'][0]['axis_probabilities']==['1/6']*6
        fields=packet['hidden_returns']['rows']
        assert tuple(row['n'] for row in fields)==STEPS
        assert all(marginal[r['n']]==F(r['hidden_zero_probability']) for r in fields)
    ve,ke=counts_at_edge(240)
    assert all(visits[3*m][m]==ve[m] and first[3*m][m]==ke[m] for m in range(1,43))
    # Exactly one reversed sign; exact independent formula includes its time and the six possible negative axes.
    for m in range(43):
        factor=F(factorial(3*m+1),factorial(m)**3)
        expect=(3*m+2)*6*factor*sum(F(comb(m,j)**3,j+1) for j in range(m+1))
        assert expect==visits[3*m+2][m]
    g0=sum(marginal)
    r=F(133,144)
    g0up=g0+F(3,4*128)+r**129/(1-r)+F(1,2**128)
    limit=240
    edge_lo=sum(F(ve[m],216**m) for m in range(limit+1))
    tm=F(comb(3*limit,limit)*comb(2*limit,limit),27**limit)
    bm=F(comb(limit,limit//2),2**limit)
    edge_up=edge_lo+(limit+1)*tm*bm**2
    level=F(10,9)
    vl,vu=F(99,100),F(19999,20000)
    lower_vl=edge_lo+(1-vl**2)*(g0-edge_up)/(1+vl**2/3)
    upper_vu=edge_up+(1-vu**2)*(g0up-edge_lo)
    assert lower_vl>level>upper_vu>edge_up and g0>level
    samples=[]
    for n in (30,60,90,120):
        for m in sorted({0,n//3,max(0,n//3-2),2*(n//12)}):
            pp=(n+3*m)//2
            samples.append(dict(n=n,m=m,v=str(F(3*m,n)),
                               first_over_visit=str(F(first[n][m],visits[n][m])),
                               axis_return=str(F(visits[n][m],comb(n,pp)*6**n))))
    return dict(source_sha=SOURCE_SHA,source_marginal_digest=frozen,source_rows=list(STEPS),
                visits_and_first_integer_sha=list(OLD),legal_positive_cells=sum(map(len,visits[1:])),
                direct_signed_absorbing_walk_through=8,edge_exact_overlap=42,one_defect_overlap=43,
                green_interval_scale=10**8,G0=enclosure(g0,g0up),G1=enclosure(edge_lo,edge_up),
                source_0p9_escape_threshold=dict(lower=str(vl),upper=str(vu),
                    outward_G_at_lower=enclosure(lower_vl,g0up),
                    outward_G_at_upper=enclosure(edge_lo,upper_vu),
                    level=str(level)),exact_moment_checks=moment_vectors(),edge_moduli=arithmetic(ve,ke),samples=samples)


if __name__=='__main__':
    parser=ArgumentParser()
    parser.add_argument('--source',type=Path,help='optional pinned hidden_plane_results.json')
    args=parser.parse_args()
    print(json.dumps(main(args.source),indent=2,sort_keys=True))
