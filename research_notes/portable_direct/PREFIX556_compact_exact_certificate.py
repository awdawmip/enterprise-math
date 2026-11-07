#!/usr/bin/env python3
"""PREFIX-556 exact two-step/sign-block certificate. Requires published PREFIX550 and PREFIX553 beside this file."""
import json
from collections import Counter,defaultdict
import PREFIX550_shared_gauge_compact_certificate as x
import PREFIX553_batched_depth_stream_certificate as p

MOD=1000000007
QVAL=(2,3,5,7,11,13)
Z=17

def det(a):
    a=[row[:] for row in a]; n=len(a); v=1
    assert all(len(row)==n for row in a)
    for j in range(n):
        i=next((i for i in range(j,n) if a[i][j]%MOD),None)
        if i is None:return 0
        if i!=j:a[i],a[j]=a[j],a[i];v=-v
        h=a[j][j]%MOD;v=v*h%MOD;inv=pow(h,-1,MOD)
        for i in range(j+1,n):
            t=a[i][j]*inv%MOD
            if t:
                for k in range(j+1,n):a[i][k]=(a[i][k]-t*a[j][k])%MOD
                a[i][j]=0
    return v%MOD

def multiply(rows,F):
    out=[]
    for row in rows:
        d=defaultdict(int)
        for (j,w),n in row.items():
            for mon,v in F[j].items():
                d[tuple(a+b for a,b in zip(w,mon))]+=n*v
        out.append(dict(d))
    return out

def main(depth=8):
    assert 0<=depth<=10
    ids,ph,sig,rows,roots=p.prepare()
    neg=[c for c in range(51) if x.P[ph[c]][2]<0]
    pos=[c for c in range(51) if x.P[ph[c]][2]>0]
    assert (len(neg),len(pos))==(24,27)
    idx_neg={c:i for i,c in enumerate(neg)};idx_pos={c:i for i,c in enumerate(pos)}
    def mkrow(c,j,g,ix):
        w=[0]*6;a=abs(x.P[ph[c]][2])-1
        if a<5:w[a]=1
        w[5]=g
        return (ix[j],tuple(w))
    A=[Counter() for _ in neg];B=[Counter() for _ in pos]
    for i,c in enumerate(neg):
        for (j,g),n in rows[c].items():A[i][mkrow(c,j,g,idx_pos)]+=n
    for i,c in enumerate(pos):
        for (j,g),n in rows[c].items():B[i][mkrow(c,j,g,idx_neg)]+=n
    AB=[Counter() for _ in neg]
    for i,row in enumerate(A):
        for (j,w),a in row.items():
            for (k,v),b in B[j].items():
                AB[i][(k,tuple(s+t for s,t in zip(w,v)))]+=a*b
    assert all(sum(r.values())==36 for r in AB)
    assert sum(len(r) for r in AB)==225
    total_checks=0
    for root in (None,)+x.ROOTS:
        F=[{p.ZERO6:1} if root is None or sig[c]==root else {} for c in range(51)]
        u=[F[c] for c in neg];v=[F[c] for c in pos]
        a=u;b=multiply(A,v)
        for n in range(depth//2+1):
            expected=[None]*51
            for i,c in enumerate(neg):expected[c]=a[i]
            vp=v if n==0 else multiply(B,prev_b)
            for i,c in enumerate(pos):expected[c]=vp[i]
            assert expected==F,(root,2*n)
            total_checks+=51
            if 2*n<depth:
                F=p.step(F,rows,ph)
                odd=[None]*51
                for i,c in enumerate(neg):odd[c]=b[i]
                bv=multiply(B,a)
                for i,c in enumerate(pos):odd[c]=bv[i]
                assert odd==F,(root,2*n+1)
                total_checks+=51
                if 2*n+1<depth:F=p.step(F,rows,ph)
            prev_b=b
            if n<depth//2:a,b=multiply(AB,a),multiply(AB,b)
    M=[[0]*51 for _ in range(51)]
    for c in rows:
        for (j,g),v in rows[c].items():
            M[c][j]=(M[c][j]+v*QVAL[abs(x.P[ph[c]][2])-1]*Z**g)%MOD
    a=[[M[c][j] for j in pos] for c in neg]
    b=[[M[c][j] for j in neg] for c in pos]
    ab=[[sum(a[i][k]*b[k][j] for k in range(27))%MOD for j in range(24)] for i in range(24)]
    dab=det(ab);assert dab==641735106
    F=[1]*51;K=[]
    for _ in range(49):
        K.append(F)
        F=[sum(M[i][j]*F[j] for j in range(51))%MOD for i in range(51)]
    keep=[i for i in range(51) if i not in (16,18)]
    dk=det([[K[j][i] for j in range(49)] for i in keep]);assert dk==291645334
    return {'status':'ALL_CHECKS_PASS','science_pin':'f42f2906d77f24085c123f3ccfe9667d41caa96d',
            'classes':51,'sign_blocks':[24,27],'AB_terms':sum(len(r) for r in AB),
            'all_boundary_vectors':13,'depth_inclusive':depth,'exact_polynomial_entries_checked':total_checks,
            'modulus':MOD,'specialization':{'q':QVAL,'z':Z},
            'AB_24_determinant_mod':dab,'Krylov_49_minor_rows':keep,'Krylov_49_determinant_mod':dk,
            'generic_rank_Q0':48,'generic_Krylov_rank_Q0_ones':49}

if __name__=='__main__':
    print(json.dumps(main(),ensure_ascii=False,indent=2))
