"""Check provenance-bounded first/second-drop finite-field and exact CRT certificates."""
from math import isqrt,lcm,prod
import csv
from pathlib import Path
root=Path(__file__).parent
lam=814202665467037976682352800
main={32,54,25,49,11,13,17,19,23,29,62,37,41,43,47,59,61,73}
def prime(n):return n>1 and all(n%i for i in range(2,isqrt(n)+1))
def factors(n):
    a=[];i=2
    while i*i<=n:
        if n%i==0:
            a.append(i)
            while n%i==0:n//=i
        i+=1
    if n>1:a.append(n)
    return a
rows=list(csv.DictReader((root/"R5_M74_M78_HASSE.csv").open()))
assert len(rows)==95
v={}
for row in rows:
    m,d,nd,p,z,j,res=(int(row[k]) for k in ("m","d","nd","prime","root","first_nonzero_jet","jet_residue"))
    assert 74<=m<=78 and d in main|{27} and (m,d) not in v
    assert prime(p) and (p-1)%d==0 and pow(z,d,p)==1
    assert all(pow(z,d//r,p)!=1 for r in factors(d))
    assert nd==sum(price%d==0 for price in range(214,315))
    assert (0<=j<=min(2,nd-2) and 0<res<p) or (j==-1 and res==0)
    v[m,d]=row
for m in range(74,79):
    missing={d for d in main if int(v[m,d]["first_nonzero_jet"])<0}
    assert missing==({41} if m==78 else set())
    assert lcm(*(main-missing))==lam//(41 if m==78 else 1)
crt=list(csv.DictReader((root/"R5_M78_D41_CRT.csv").open()))
assert len(crt)==7
assert all(int(r["m"])==78 and int(r["primitive_zero_count"])==40 and int(r["total_primitive_roots"])==40 and int(r["first_failed_k"])==0 for r in crt)
ps=[int(r["prime"]) for r in crt]
assert len(set(ps))==7 and all(prime(p) and (p-1)%41==0 for p in ps)
P=prod(ps);B=7*2**8*78**8
assert P>2*B
assert {d for d in range(1,315) if d%41==0 and sum(price%d==0 for price in range(214,315))>=2}=={41}
print("PASS 95 Hasse lower-bound records m74..78")
print("PASS 280 primitive roots, CRT product",P,"> 2B",2*B)
print("PASS exact M78",lam//41)
