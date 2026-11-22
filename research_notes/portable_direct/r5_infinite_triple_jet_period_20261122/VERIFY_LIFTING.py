"""Independent exact small-field test of the R5 dual-number denominator-lifting lemma.
The general mathematical proof is in RESEARCH.md. This tests one nontrivial
8-factor denominator with a quadratic term, not all primes/parameters.
"""
P,D=113,7
W=next(x for x in range(2,P) if pow(x,D,P)==1 and all(pow(x,j,P)!=1 for j in range(1,D)))
factors=[(0,1),(216,1),(217,1),(218,1),(214,1),(215,1),(219,1),(214+215+219,2)]
def add(a,b):
    out=[0]*max(len(a),len(b))
    for i,v in enumerate(a): out[i]=(out[i]+v)%P
    for i,v in enumerate(b): out[i]=(out[i]+v)%P
    return out
def mul(a,b):
    z=[0]*(len(a)+len(b)-1)
    for i,v in enumerate(a):
        for j,w in enumerate(b): z[i+j]=(z[i+j]+v*w)%P
    return z
def divexact(A,B):
    R=A[:];Q=[0]*max(1,len(A)-len(B)+1); inverse=pow(B[-1],-1,P)
    for k in range(len(A)-len(B),-1,-1):
        c=R[k+len(B)-1]*inverse%P;Q[k]=c
        for j,b in enumerate(B):R[k+j]=(R[k+j]-c*b)%P
    assert all(x==0 for x in R[:len(B)-1])
    return Q
Q0=[1];Q1=[0]
for exponent,h in factors:
    a=pow(W,exponent,P)
    f0=[1]+[0]*(h-1)+[-a%P]
    f1=[0]*h+[-exponent*a%P]
    Q1=add(mul(Q1,f0),mul(Q0,f1));Q0=mul(Q0,f0)
H=[1]+[0]*(2*D*P-1)+[-1%P]
B0=divexact(H,Q0)
B1=[(-x)%P for x in divexact(mul(H,Q1),mul(Q0,Q0))]
assert mul(Q0,B0)==H
assert all(x%P==0 for x in add(mul(Q0,B1),mul(Q1,B0)))
print("ALL CHECKS PASS", "d",D,"prime",P,"root",W,"denominator degree",len(Q0)-1,"target degree",len(H)-1)
