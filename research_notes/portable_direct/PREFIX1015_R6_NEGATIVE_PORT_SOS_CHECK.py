"""PREFIX-1015: exact BRC-derived negative-port Gram sum-of-squares certificate.

Pure integral Laurent-polynomial postprocessing of pinned PREFIX-1014 typed
signed Cell--terminal-port BRC amplitudes. No independent native propagation.
"""
from collections import defaultdict
from math import comb, factorial
from fractions import Fraction
import json, hashlib
D=6
ZERO=(0,)*D
def unit(i,a=1):return tuple(a if t==i else 0 for t in range(D))
def add(*args):
    d=defaultdict(int)
    for p in args:
        for k,v in p.items(): d[k]+=v
    return {k:v for k,v in d.items() if v}
def scale(p,c):return {k:v*c for k,v in p.items() if v*c}
def mult(a,b):
    d=defaultdict(int)
    for x,v in a.items():
        for y,w in b.items():d[tuple(u+t for u,t in zip(x,y))]+=v*w
    return {k:v for k,v in d.items() if v}
def star(p):return {tuple(-t for t in x):v for x,v in p.items()}
def sqnorm(p):return sum(v*v for v in p.values())
S={unit(i):1 for i in range(D)}
ONE={ZERO:1}
def power_s(m):
    out={ZERO:1}
    for _ in range(m):out=mult(out,S)
    return out
V=[add(S,scale({unit(i):1},-D)) for i in range(D)]
T=add(S,scale({unit(0):1},-1))
A=mult(V[0],star(V[0]))
B=mult(V[1],star(V[1]))
DELTA=add(A,scale(B,-1))

def gram(m,j):
    return sqnorm(mult(power_s(m+1),mult(T,V[j])))
def test_one(n):
    m=n-4
    g1=gram(m,0);g2=gram(m,1)
    raw=sqnorm(mult(power_s(m+1),DELTA))
    assert raw%12==0,(n,raw)
    assert g1-g2==raw//12,(n,g1,g2,raw)
    return {"n":n,"m":m,"qminus_distinguished":g1,"qminus_other_per_port":g2,"difference":g1-g2,"sos_norm":raw,"identity":"difference=sos_norm/12"}

def check_symmetry():
    # Laurent identity 6|T|^2 = 5|S|^2+|V_1|^2-30
    lhs=scale(mult(T,star(T)),6)
    rhs=add(scale(mult(S,star(S)),5),A,scale(ONE,-30))
    assert lhs==rhs
    assert DELTA==star(DELTA)
    return True

def main():
    check_symmetry()
    rows=[test_one(n) for n in range(5,15)]
    for r in rows[:4]:
        old={5:(16560,12384),6:(246870,191574),7:(4299380,3455060),8:(83992020,69575892)}
        assert (r['qminus_distinguished'],r['qminus_other_per_port'])==old[r['n']]
    return {"schema":"PREFIX1015_R6_NEGATIVE_PORT_SOS_V1","source":"PREFIX-1014@599f5d5306abae0101769432d6ff8da77517bf3e; frozen P000 V5 f42f2906d77f24085c123f3ccfe9667d41caa96d","scope":"n>=5, single bidirectionally blocked {0,e1}, grade k=1, signed BRC numerator, each final negative-direction port, chosen chart anchor; S5 class j>=2", "theorem":"Q^-_{n,1}-Q^-_{n,2}=(1/12)||S^(n-3)*(|S-6z1|^2-|S-6z2|^2)||_2^2>0", "laurent_identity_6T2":"6|S-z1|^2=5|S|^2+|S-6z1|^2-30", "exact_crosschecks":rows,"proof":"S6 symmetry of Haar/constant-term Gram bilinear functional with |S|^(2n-6); exchange axes 1,2 makes integral of (5|S|^2-30)(A-B) zero and integral A(A-B)=integral (A-B)^2/2. Strict because S^(n-3)(A-B) is a nonzero Laurent polynomial.","verification":"All integer arithmetic. No floating point. PREFIX-1014 native BRC independent values matched for n=5..8; this run verifies post-observer SOS identity for n=5..14. This is not an independent BRC trajectory replay nor formal review.","next_problem":"Prove or refute analogous uniform sign Q^+_{n,1}-Q^+_{n,*}; find difference's sum-of-squares or exact A6 shifts; generalize beyond grade k=1."}
if __name__=='__main__':
    result=main()
    data=json.dumps(result,ensure_ascii=False,sort_keys=True,indent=2)+'\n'
    with open('/mnt/data/PREFIX1015_R6_NEGATIVE_PORT_SOS_RESULTS.json','w') as f:f.write(data)
    print(json.dumps({'checks':len(result['exact_crosschecks']),'rows_first4':result['exact_crosschecks'][:4], 'last':result['exact_crosschecks'][-1], 'certificate_sha256':hashlib.sha256(data.encode()).hexdigest()},ensure_ascii=False,indent=2))
