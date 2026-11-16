"""R518 independent exact 41st-order determinant checks using ballot-Catalan and SymPy Berkowitz."""
from math import comb
from sympy import Matrix
import json

R=41
def c(k): return comb(2*k,k)//(k+1)
def b(n,m): return comb(n,m) if 0<=m<=n else 0
def raw_signed(k,t):
    r=2*k+1
    if not 2<=t<=r: return 0
    return comb(r+t,2*t)*sum(comb(r-t,q)*(b(2*t,r-2*q)-b(2*t,r-2*q-1)) for q in range(r-t+1))
def ballot(k,t):
    r=2*k+1
    if not 2<=t<=r: return 0
    return comb(r+t,2*t)*sum(comb(t-1,2*q)*4**q*c(k-q) for q in range(min((t-1)//2,k)+1))
def recurrence(k,m=R):
    p=ballot(k,2)
    h=[ballot(k,j+3) for j in range(m)]
    d=[1]
    for n in range(1,m+1):
        d.append(sum((-1)**(a-1)*h[a-1]*p**(a-1)*d[n-a] for a in range(1,n+1)))
    return d[m]
Ks=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,20,28,29]
res=[]
for k in Ks:
    mat=Matrix(R,R,lambda i,j:ballot(k,3+i-j))
    det=int(mat.det(method='berkowitz'))
    assert det==recurrence(k),(k,'det!=rec')
    res.append({'k':k,'sign':('+' if det>0 else '-' if det<0 else '0')})
count=0
for k in range(1,21):
    for t in range(2,R+2):
        assert raw_signed(k,t)==ballot(k,t),(k,t)
        count+=1
expected={1:'+',2:'+',3:'+',4:'+',5:'+',6:'-',7:'-',8:'-',9:'-',10:'-',11:'-',12:'-',13:'-',14:'-',15:'+',16:'+',20:'+',28:'+',29:'+'}
assert {o['k']:o['sign'] for o in res}==expected
print(json.dumps({'status':'R518_INDEPENDENT_PASS','method':'Independent SymPy Berkowitz direct 41x41 ballot-Catalan Toeplitz determinants versus independent recurrence','tested':res,'raw_signed_vs_ballot':count,'precision':'exact Python integer/SymPy arbitrary-precision integer','independence_boundary':'independent implementation, same public mathematical definition; not independent Driver reviewer'},indent=2))
