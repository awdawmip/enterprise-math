from pathlib import Path
import json
import sympy as s
r,q=s.symbols('r q')
lam=s.symbols('lambda')
N=100
v=[1]+[0]*N
for w in (1,1,1,2,3,6):
    for j in range(w,N+1): v[j]+=v[j-w]
C=[0]+v
T=[0]*len(C)
for j in range(1,len(C)):T[j]=T[j-1]+C[j-1]
cp=[];tp=[]
for a in range(6):
    cp.append(s.expand(s.interpolate([(6*m+a,C[6*m+a]) for m in range(6)],q)))
    tp.append(s.expand(s.interpolate([(6*m+a,T[6*m+a]) for m in range(7)],q)))
    assert all(cp[a].subs(q,t)==C[t] and tp[a].subs(q,t)==T[t] for t in range(a,96,6))
z=s.symbols('z')
CG=z/((1-z)**3*(1-z**2)*(1-z**3)*(1-z**6))
TG=z**2/((1-z)**4*(1-z**2)*(1-z**3)*(1-z**6))
CN=s.cancel(CG*(1-z**6)**6);TN=s.cancel(TG*(1-z**6)**7)
assert s.denom(CN)==1 and s.denom(TN)==1
assert s.degree(CN,z)<36 and s.degree(TN,z)<42
# The first 36/42 coefficients determine the numerators under the displayed denominator,
# proving the six polynomial branches, not merely testing an infinite extrapolation.
poly=q**4/s.Integer(6)+q**3/s.Integer(2)-115*q*q/s.Integer(36)+115*q/s.Integer(6)-s.Rational(16315,108)
weights=(1,-4,6,-4,1)
records=[]
for a in range(6):
    coeff=[];quo=[]
    for j in range(7):
        denom=s.expand(cp[(a+j)%6].subs(q,r+j))
        num=s.expand((r+j)**3*(tp[(a+j)%6].subs(q,r+j)-r**6/s.Integer(25920)+lam*r**5/s.Integer(25920)))
        div,rem=s.div(num,denom,r)
        quo.append(s.expand(div-poly.subs(q,r+j)))
        coeff.append(s.factor(s.Poly(rem,r).nth(4)/s.Poly(denom,r).nth(5)))
    D0=[s.simplify(sum(weights[k]*quo[j+k] for k in range(5))) for j in range(3)]
    D1=[s.factor(sum(weights[k]*coeff[j+k] for k in range(5))) for j in range(3)]
    assert D0==[-20]*3,(a,D0)
    records.append({'phase':a,'r_inverse':list(map(str,D1)),'centered':list(map(lambda t:str(s.factor(t-D1[0])),D1[1:])),'lambda0':list(map(lambda t:str(t.subs(lam,0)),D1))})
    print(a, D1, 'shape=',[s.factor(t-D1[0]) for t in D1[1:]])
print('C polys', cp)
print('T polys', tp)
Path(__file__).with_name('derived.json').write_text(json.dumps({'model':'v=0, u=-1+lambda/r','C':list(map(str,cp)),'T':list(map(str,tp)),'phase_coefficients':records},ensure_ascii=False,indent=2)+'\n')
