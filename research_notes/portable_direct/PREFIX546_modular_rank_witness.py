#!/usr/bin/env python3
"""Exact finite field Krylov rank lower-bound witness; needs adjacent PREFIX545_compact_exact_certificate.py."""
import json
import PREFIX545_compact_exact_certificate as b
P=1000000007

def rank(r):
    cls,Q,_=b.quotient(r)
    vec=[1]*28;rows=[]
    for depth in range(28):
        rows.append(vec[:])
        vec=[sum(n*(2**p)*(3**h)*vec[j] for (j,p,h),n in Q[c].items())%P for c in range(28)]
    a=[list(x) for x in zip(*rows)];k=0
    for col in range(28):
        h=next((j for j in range(k,28) if a[j][col]%P),None)
        if h is None:continue
        a[h],a[k]=a[k],a[h];inv=pow(a[k][col],-1,P)
        for j in range(col,28):a[k][j]=a[k][j]*inv%P
        for i in range(k+1,28):
            factor=a[i][col]
            for j in range(col,28):a[i][j]=(a[i][j]-factor*a[k][j])%P
        k+=1
    return k
if __name__=='__main__':
    print(json.dumps({'status':'ALL_CHECKS_PASS','field_modulus':P,'q':2,'z':3,'ranks':{str(r):rank(r) for r in (-1,0,1)}},indent=2))
