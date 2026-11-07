"""PREFIX570 exact integer certificate; inputs PREFIX565/PREFIX566, frozen pin f42f2906d77f24085c123f3ccfe9667d41caa96d."""
from collections import Counter
from PREFIX565_positive_marginal_certificate import SCIENCE_PIN,ZERO_ROOT,ROOTS,ACTIONS,edge,clean
from PREFIX566_gate_quotient_certificate import marginal_gate_rows,weighted_quotient,native_involution,symmetric_to_uvz
import json

def uv(p):
    assert all(p.get((y,x),0)==v for (x,y),v in p.items())
    return symmetric_to_uvz({(x,y,0):v for (x,y),v in p.items()})

def step(vec,Q):
    result=[]
    for row in Q:
        out=Counter()
        for (j,x,y,g),m in row.items():
            if not g:
                for (a,b),n in vec[j].items():out[a+x,b+y]+=m*n
        result.append(clean(out))
    return result

def check(excess=256):
    assert SCIENCE_PIN=='f42f2906d77f24085c123f3ccfe9667d41caa96d'
    native=marginal_gate_rows(ZERO_ROOT)
    assert all(marginal_gate_rows(root)==native for root in ROOTS)
    ids,Q,growth=weighted_quotient(native)
    assert len(Q)==37
    for i,row in enumerate(native):
        aggregate=Counter()
        for (j,x,y,g),m in row.items():aggregate[ids[j],x,y,g]+=m
        assert aggregate==Q[ids[i]]
    sigma=native_involution()
    fixed=sorted({ids[i] for i in range(96) if sigma[i]==i})
    assert len(fixed)==11 and sum(sigma[i]==i for i in range(96))==32
    for i in range(96):
        for a in ACTIONS:
            j,w=edge(i,a,ZERO_ROOT)
            expected=(sigma[j],w[:4]+(w[5],w[4])+w[6:])
            assert sum(edge(sigma[i],b,ZERO_ROOT)==expected for b in ACTIONS)==1
    gates={j for row in Q for (j,x,y,g),m in row.items() if g}
    assert gates=={5}
    assert all(x==y==0 for row in Q for (j,x,y,g),m in row.items() if g)
    U=[sum(m for (j,x,y,g),m in row.items() if g) for row in Q]
    assert [(i,n) for i,n in enumerate(U) if n]==[(4,1),(15,1),(17,1)]
    A=[{(0,0):n} if n else {} for n in U]
    B=[{(0,0):1} for _ in Q]
    count={'A':0,'K':0,'B':0};first={i:None for i in fixed};lead=None
    for d in range(excess+5):
        for i in fixed:
            p=uv(A[i]);assert all(z>=0 for z in p.values());count['A']+=len(p)
            if p and first[i] is None:first[i]=d
        k=uv(A[5]);b=uv(B[5]);assert all(z>=0 for z in k.values());assert all(z>=0 for z in b.values())
        count['K']+=len(k);count['B']+=len(b)
        if d==3:lead=k
        if d<excess+4:A,B=step(A,Q),step(B,Q)
    assert lead=={(0,0,0):4,(1,0,0):8}
    assert max(first.values())==4 and min(first.values())==0
    # Formal renewal: H[i,k,s]=[t^s]a_i(t)c(t)^(k-1)b(t), c(0)=4+8u.
    # Nonnegative factor coefficients through s=excess imply H>=0 for all k.
    # H[i,k+1,s]-(4+8u)H[i,k,s]>=0 follows by replacing c by c-c(0).
    return {'status':'ALL_CHECKS_PASS','science_pin':SCIENCE_PIN,'excess':[0,excess],
      'unbounded_gate_count':'all integers k>=1','fixed_classes':fixed,
      'delta_by_class':{str(i):first[i]+1 for i in fixed},
      'monotonic_factor':'4+8u','positive_positions':count,
      'total_positions':sum(count.values()),'factor_scan_depth':[0,excess+4],
      'native_edge_checks':len(ROOTS)*96*6,'native_involution_edge_checks':96*6,
      'theorems':['H[i,k,s] has nonnegative integer u,v coefficients for 0<=s<=256, k>=1',
                  'H[i,k+1,s]-(4+8u)H[i,k,s] has nonnegative integer u,v coefficients in same range']}

if __name__=='__main__':print(json.dumps(check(),ensure_ascii=False,indent=2))
