# R4-EC10 exact symbolic and modular reproduction. Auxiliary positive BRC, not native X6.
import json
import sympy as s

x,z=s.symbols('x z',nonzero=True)
p=1000003
fine=[(q,r,e) for q,r in [(0,0),(0,2),(1,1),(1,2),(2,0),(2,1),(2,2)] for e in (1,-1)]
outs=[(q,c,e) for q in range(3) for c in (0,1) for e in (1,-1)]
id={a:i for i,a in enumerate(fine)}
def edge(q,a):
    if q==0:return [(2,-1,-1),(2,1,-1)][a]
    if q==1:return [(0,-1,-1),(0,1,-1)][a]
    return [(1,1,1),(2,1,-1)][a]
T=s.zeros(14);C=s.zeros(12,14)
for j,(q,r,e) in enumerate(fine):
    C[outs.index((q,int(r==2),e)),j]=1
    for a in (0,1):
        nq,eta,b=edge(q,a)
        nr=2 if r==2 else (0 if a else (1 if r==0 else 2))
        ne=e*eta
        T[id[(nq,nr,ne)],j]+=z**(ne*b)
v=s.zeros(14,1);v[id[(0,0,1)]]=1
S=z+1/z
P=s.expand((1+x*x)*(1-x*S+2*x**4-x**6)*(1-x*S)*(1+x*x-x**3*S))
ps=[s.cancel(P.coeff(x,j)) for j in range(13)]
assert ps[0]==1
powers=[v]
for n in range(13): powers.append(T*powers[-1])
assert all(s.cancel(sum(ps[j]*powers[13-j][k] for j in range(13)))==0 for k in range(14))
defect=C*sum((ps[j]*powers[12-j] for j in range(13)),s.zeros(14,1))
for k,o in enumerate(outs):
    target=(-(z*z+1) if o==(0,1,1) else z*z+1 if o==(0,1,-1) else 0)
    assert s.cancel(defect[k]-target)==0
# Specialize exact Laurent polynomials at z=2 and reduce mod 1,000,003.
T2=[[s.Rational(T[i,j].subs(z,2)) for j in range(14)] for i in range(14)]
T2=[[int(a.p)*pow(int(a.q),-1,p)%p for a in row] for row in T2]
u=[int(j==id[(0,0,1)]) for j in range(14)]
ys=[]
for n in range(14):
    ys.append([sum(u[j] for j,(q,r,e) in enumerate(fine) if (q,int(r==2),e)==o)%p for o in outs])
    u=[sum(T2[i][j]*u[j] for j in range(14))%p for i in range(14)]
def det(A):
    A=[row[:] for row in A];d=1
    for j in range(len(A)):
        k=next((k for k in range(j,len(A)) if A[k][j]%p),None)
        if k is None:return 0
        if k!=j:A[k],A[j]=A[j],A[k];d=-d%p
        b=A[j][j];d=d*b%p;inv=pow(b,-1,p)
        for i in range(j+1,len(A)):
            a=A[i][j]*inv%p
            for m in range(j+1,len(A)):A[i][m]=(A[i][m]-a*A[j][m])%p
            A[i][j]=0
    return d
r13=[(0,j) for j in range(11)]+[(1,4),(1,5)]
r12=[(0,j) for j in [0,1,2,4,5,6,7,8,9,10]]+[(1,4),(1,5)]
d13=det([[ys[lag+j][o] for j in range(13)] for lag,o in r13])
d12=det([[ys[1+lag+j][o] for j in range(12)] for lag,o in r12])
assert d13==739682 and d12==684922,(d13,d12)
print(json.dumps({'proof':'PASS','exact_identity':'R(T)v=0','defect':'dirty q0 +/- = -/+(z^2+1)','field_prime':p,'specialized_z':2,'full_hankel_minor':d13,'shifted_hankel_minor':d12,'joint_minimum_dim':13,'shifted_minimum_dim':12},sort_keys=True))
