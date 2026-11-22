"""Global exact primitive-root cancellation classes at d=54 and d=73.
Independent block evaluation; comparison against source R5_M1_M73_HASSE_WITNESSES.csv
from immutable prior source @882ac533.
"""
import csv,sys
from math import gcd
S0=list(range(214,219));S3=list(range(223,291));S4=list(range(296,313))
PRIME_ROOT={54:(109,36),73:(293,16)}
def block(m,prices,p,z):
    h=[0]*m;h[0]=1;factor=1
    for price in prices:
        w=pow(z,price,p)
        factor=factor*(1-w)%p
        for k in range(1,m):
            h[k]=(h[k]+w*h[k-1])%p
    return factor*sum(h)%p
def numerator(m,d):
    p,z=PRIME_ROOT[d]
    if d==54: return block(m,S4,p,z)
    a,b,c=(block(m,E,p,z) for E in (S0,S3,S4))
    return (1-(1-a)*(1-b)*(1-c))%p
for d,(p,z) in PRIME_ROOT.items():
    assert pow(z,d,p)==1 and all(pow(z,d//r,p)!=1 for r in range(2,d+1) if d%r==0 and all(r%t for t in range(2,int(r**.5)+1)))
    zeros=[m for m in range(1,d+1) if numerator(m,d)==0]
    assert zeros==(list(range(38,55)) if d==54 else list(range(69,74)))
    for m in range(1,4*d+1): assert numerator(m,d)==numerator(1+(m-1)%d,d)
    print("PASS",d,"zero classes",zeros,"nonzero",d-len(zeros),"four modular periods")
if len(sys.argv)>1:
    with open(sys.argv[1],newline="") as f:
        rows={(int(r["m"]),int(r["d"])):r for r in csv.DictReader(f)}
    for d,(p,z) in PRIME_ROOT.items():
        for m in range(1,d+1):
            r=rows[m,d];v=numerator(m,d)
            if v: assert (int(r["first_nonzero_jet"]),int(r["jet_residue"]),int(r["root"]))==(0,v,z)
            else: assert int(r["first_nonzero_jet"])==-1
    print("PASS archived full five-event finite-field residues agree")
