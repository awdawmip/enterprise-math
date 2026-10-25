"""Exact EC27 diagonal/BRC kernel regression (stdlib only)."""
import json
N=120
J=N//2
Y=[0]*(J+1)
for i in range(4,J+1):
    Y[i]=(i==4)+2*Y[i-1]+Y[i-3]+sum(Y[a]*Y[i-1-a] for a in range(i))
R=Y[:]
R[0]=R[1]=1
H=[Y[i]-(Y[i-1] if i else 0) for i in range(J+1)]
assert H[:4]==[0]*4 and all(h>0 for h in H[4:])
def conv(a,b):
    c=[0]*(J+1)
    for i,x in enumerate(a):
        if x:
            for k,y in enumerate(b[:J+1-i]):
                c[i+k]+=x*y
    return c
r2=conv(R,R)
for i in range(J+1):
    assert R[i]+(2*R[i-2] if i>=2 else 0)-(R[i-3] if i>=3 else 0)-(r2[i-1] if i else 0)==(i==0)
B=[[0]*(J+1)]
power=[1]+[0]*J
for p in range(1,N+2):
    power=conv(power,R)
    B.append([power[j]-(power[j-1] if j else 0) for j in range(J+1)])
E=[]
for n in range(N+1):
    row=[0]*(n+1)
    if n==0: row[0]=1
    if n==2: row[1]-=1
    for lag,shift,weight in ((1,0,1),(1,1,1),(4,2,-2),(6,3,1)):
        if n>=lag:
            for j,x in enumerate(E[n-lag]): row[j+shift]+=weight*x
    E.append(row)
checks=positives=0
zeros=[]
for n,row in enumerate(E):
    assert row==row[::-1] and min(row)>=0
    for j in range(n//2+1):
        f=row[j]-(row[j-1] if j else 0)
        assert f==B[n-2*j+1][j]
        checks+=1
        if n>=10 and j>=1:
            assert f>=0
            positives+=1
            if f==0: zeros.append((n,j))
assert zeros==[(10,3),(12,4)]
assert B[6][:8]==[1,5,9,5,1,27,97,209]
print(json.dumps({'status':'PASS','exact_diagonal_pairs':checks,
    'unimodality_pairs':positives,'all_n_le':N,
    'equality_cases':zeros,'B6_first8':B[6][:8],
    'method':'integers only; finite regression, not unbounded proof'},sort_keys=True))
