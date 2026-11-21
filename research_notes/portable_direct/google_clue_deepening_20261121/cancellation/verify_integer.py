import json
from pathlib import Path
from fractions import Fraction as F
import sympy as s
root=Path(__file__).parent
obj=json.loads((root/'derived.json').read_text())
q=s.Symbol('q');lam=s.Symbol('lam')
Cp=[s.Poly(s.sympify(t),q) for t in obj['C']]
Tp=[s.Poly(s.sympify(t),q) for t in obj['T']]
def coef(poly): return [F(int(t.p),int(t.q)) for t in poly.all_coeffs()]
C=list(map(coef,Cp));T=list(map(coef,Tp))
def ev(coeff,q):
    v=F(0)
    for c in coeff:v=v*q+c
    return v
def readout(r,l):
    bias=(-r**6+l*r**5)//25920
    obs=[]
    for q0 in range(r,r+7):
        p=F(q0**4,6)+F(q0**3,2)-F(115*q0*q0,36)+F(115*q0,6)-F(16315,108)
        obs.append(F(q0**3)*(ev(T[q0%6],q0)+bias)/ev(C[q0%6],q0)-p)
    z=[sum(w*obs[j+k] for k,w in enumerate((1,-4,6,-4,1))) for j in range(3)]
    return [(x+20)*r for x in z]
rows=[]
for l in (0,-39,-48,-69,5):
    for R in (600,6000,60000):
        err=F(0)
        for a in range(6):
            r=R+a
            expected=[s.sympify(t.replace('lambda','lam'),locals={'lam':lam}).subs(lam,l) for t in obj['phase_coefficients'][a]['r_inverse']]
            got=readout(r,l)
            err=max(err,*[abs(x-F(int(y.p),int(y.q))) for x,y in zip(got,expected)])
        rows.append({'lambda':l,'R':R,'max_error':str(err),'max_error_float':float(err)})
for l in (0,-39,-48,-69,5):
    seq=[x['max_error_float'] for x in rows if x['lambda']==l]
    assert seq[2]<seq[1]/5<seq[0]/25
print(json.dumps({'status':'PASS','integer_starts':90,'lambda_values':[0,-39,-48,-69,5],'checks':rows},indent=2))
(root/'integer_verification.json').write_text(json.dumps({'status':'PASS','integer_starts':90,'checks':rows},indent=2)+'\n')
