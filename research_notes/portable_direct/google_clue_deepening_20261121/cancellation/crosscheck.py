"""Author-side targeted check via rational generating functions and series division."""
import json
from pathlib import Path
from itertools import combinations
import sympy as s

root=Path(__file__).resolve().parent
obj=json.loads((root/'derived.json').read_text())
q,m,z,x,t,L=s.symbols('q m z x t lambda')
C=[s.sympify(v) for v in obj['C']]
T=[s.sympify(v) for v in obj['T']]
moments=[1/(1-x)]
for j in range(6): moments.append(s.cancel(x*s.diff(moments[-1],x)))

def gf(branches):
    total=0
    for a,p in enumerate(branches):
        pp=s.Poly(p.subs(q,6*m+a),m)
        total+=z**a*sum(c*moments[pow[0]].subs(x,z**6) for pow,c in pp.terms())
    return s.cancel(total)

assert s.cancel(gf(C)-z/((1-z)**3*(1-z**2)*(1-z**3)*(1-z**6)))==0
assert s.cancel(gf(T)-z**2/((1-z)**4*(1-z**2)*(1-z**3)*(1-z**6)))==0

stencil=(1,-4,6,-4,1)
Q=q**4/6+q**3/2-s.Rational(115,36)*q*q+s.Rational(115,6)*q-s.Rational(16315,108)
for a in range(6):
    coefficients=[]
    for j in range(7):
        D=s.Poly(s.expand(t**5*C[(a+j)%6].subs(q,1/t+j)),t)
        N=s.Poly(s.expand(t**9*(1/t+j)**3*(T[(a+j)%6].subs(q,1/t+j)-1/(25920*t**6)+L/(25920*t**5))),t)
        v=[]
        for ell in range(6):
            v.append(s.expand((N.nth(ell)-sum(D.nth(i)*v[ell-i] for i in range(1,min(ell,5)+1)))/D.nth(0)))
        baseline=s.Poly(s.expand(t**4*Q.subs(q,1/t+j)),t)
        coefficients.append([s.expand(v[ell]-baseline.nth(ell)) for ell in range(6)])
    for start in range(3):
        for ell in range(6):
            result=s.expand(sum(stencil[j]*coefficients[start+j][ell] for j in range(5)))
            expected=0 if ell<4 else (-20 if ell==4 else s.sympify(obj['phase_coefficients'][a]['r_inverse'][start].replace('lambda','L'),locals={'L':L}))
            assert s.expand(result-expected)==0,(a,start,ell,result,expected)

# Direct rank-based classification, independent of the original solve calls.
tables={
 'full':[[s.sympify(v.replace('lambda','L'),locals={'L':L}) for v in row['r_inverse']] for row in obj['phase_coefficients']],
 'shape':[[s.sympify(v.replace('lambda','L'),locals={'L':L}) for v in row['centered']] for row in obj['phase_coefficients']]
}
classification={}
for name,rows in tables.items():
    same=[];independent=[]
    for a,b in combinations(range(6),2):
        va=s.Matrix(rows[a]);vb=s.Matrix(rows[b]);one=s.Matrix([s.diff(v,L) for v in va]);two=s.Matrix([s.diff(v,L) for v in vb])
        rhs=vb.subs(L,0)-va.subs(L,0)
        for kind,M in [('same',one-two),('independent',s.Matrix.hstack(one,-two))]:
            if M.rank()==M.row_join(rhs).rank():
                ans=list(s.linsolve((M,rhs)))
                (same if kind=='same' else independent).append({'phases':[a,b],'solutions':str(ans)})
    classification[name]={'same':same,'independent':independent}

report={'status':'PASS','generating_function_identities':2,'series_coefficients_checked':6*3*6,'classification':classification,
        'review_kind':'AUTHOR_SIDE_CROSSCHECK_NOT_INDEPENDENT_PROJECT_ADMISSION'}
Path(__file__).with_name('crosscheck.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
