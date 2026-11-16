#!/usr/bin/env python3
"""R402 exact sanity checks for the general signed BRC Catalan coefficient theorem.

All arithmetic is integer/Fraction; this program is *not* an independent
formal proof of the all-corank theorem (see PROOF.zh-CN.md).
"""
from fractions import Fraction as Q
from math import comb
import json, hashlib, sys
from pathlib import Path

ROOT=Path(__file__).resolve().parent

def C(n,k):
    return comb(n,k) if 0<=k<=n else 0

def mono(n,a,shift):
    return [0]*shift+[a*C(n,j) for j in range(n+1)] if n>=0 else [0]

def add(a,b):
    z=[0]*max(len(a),len(b))
    for j,x in enumerate(a): z[j]+=x
    for j,x in enumerate(b): z[j]+=x
    return z

def K(i):
    ds=(-C(4,i)+C(2,i-1), C(5,i-1)-C(5,i-2),C(7,i-2),-C(9,i-3))
    z=[0]
    for j,x in enumerate(ds,1):
        if x: z=add(z,mono(i+1-j,-x,i-1))
    return z

def J(s):
    z=[0]
    for x,n in ((-C(3,s-1),s),(-C(6,s-1),s-1),(C(8,s-2),s-2)):
        if x:z=add(z,mono(n,x,s))
    return z

def kernel_test(theta):
    laurent={}
    for i in range(1,13):
        arr=K(i)
        if i==3:
            assert arr[2]==-8
            arr[2]=-8*(1+theta)
        for q,c in enumerate(arr):
            if c:
                pair=(q,i-q)
                laurent[pair]=laurent.get(pair,0)+c
    assert all(-8<=e<=1 for _,e in laurent)
    coeff=lambda q:{e:v for (qq,e),v in laurent.items() if qq==q}
    assert coeff(0)=={1:2}
    assert coeff(1)=={0:3,1:-1}
    assert coeff(2)=={0:4,1:-8*(1+theta)}
    assert coeff(3)=={-1:4,0:-8,1:-11}
    assert coeff(4)=={-1:4,0:-29,1:6}
    # Hensel root of 1-K(z,u/z): zeta=1/2-5u/4+(-5/8+2theta)u².
    a,b=Q(-5,4),Q(-5,8)+2*theta
    # Expand the kernel through order u² at this root, exactly.
    # D0=1-2z, D1=-(3-z)u, D2=-(4-8(1+theta)z)u².
    assert -2*a-Q(5,2)==0
    assert -2*b+a+4*theta==0
    G0=-4*a
    G1=8*a*a-4*b
    assert G0==5 and G1==15-8*theta
    zeta=[Q(1,2),a,b,Q(-41,16)-4*theta,Q(-373,32)+Q(7,2)*theta+8*theta*theta]
    inv=[Q(2)]
    for n in range(1,5):
        inv.append(-2*sum(zeta[j]*inv[n-j] for j in range(1,n+1)))
    assert inv==[Q(2),Q(5),Q(15)-8*theta,Q(54)-24*theta,Q(226)-104*theta]
    # Coefficients of K(zeta(u),u/zeta(u)) through u^4 are exactly (1,0,0,0,0).
    # Every Laurent coefficient K_q is a linear combination of z, 1, 1/z up to q=4.
    for n in range(5):
        val=Q(0)
        for q in range(n+1):
            ce=coeff(q)
            assert all(e in (-1,0,1) for e in ce)
            val+=ce.get(0,0)*(1 if n==q else 0)
            val+=ce.get(1,0)*zeta[n-q]
            val+=ce.get(-1,0)*inv[n-q]
        assert val==(1 if n==0 else 0),('root Hensel coefficient',theta,n,val)
    # N(z,u)=1+(z^-1-2)u+O(u²) and D_z=-2+u+O(u²).
    # Therefore A(u)=-N(zeta,u)/(zeta*D_z(zeta,u))=1+3u+O(u²).
    assert inv[0]-2==0 and -2*a+Q(1,2)==3
    assert 20*inv[3]==1080-480*theta
    assert 200*inv[4]==45200-20800*theta
    return {'zeta_u0':'1/2','zeta_u1':str(a),'zeta_u2':str(b),
            'zeta_u3':str(zeta[3]),'zeta_u4':str(zeta[4]),
            'G_u0':str(G0),'G_u1':str(G1),
            'E_x1':str(2*G1),'E_x2':str(20*inv[3]),'E_x3':str(200*inv[4]),
            'A_x1':'30'}

def calc_L(max_r,max_k,theta):
    # Computes exact original signed B_s and raw-D coefficients, no polynomial interpolation.
    S=max_r+2*max_k+2; P=max_r+max_k+2
    kern=[None]+[K(i) for i in range(1,13)]
    assert kern[3][2]==-8
    kern[3][2]=-8*(1+theta)
    B=[[Q(0)]*(P+1) for _ in range(S+1)]
    B[0][0]=B[0][1]=1
    for s in range(1,S+1):
        for j,x in enumerate(J(s)[:P+1]):B[s][j]=x
        for i in range(1,min(s,12)+1):
            for j,x in enumerate(kern[i]):
                if not x: continue
                for p in range(j,P+1): B[s][p]+=x*B[s-i][p-j]
    def D(q,k):
        return sum((-1)**(k-w)*C(k,w)*Q(2)**(q-w)*B[q+w][q] for w in range(k+1))
    return [[Q(5)**(r-k)*D(r+k,k) for k in range(max_k+1)] for r in range(max_r+1)]

def delta(xs):
    return [xs[i+1]-xs[i] for i in range(len(xs)-1)]

def test_theta(theta,R=8):
    kern=kernel_test(theta)
    # All Q^r multipliers are exact, including theta=15/8 where the leading term vanishes.
    L=calc_L(R+1,2*R+2,theta)
    a=30-16*theta
    assert all(z==1 for z in L[0])
    rows=[]
    for r in range(1,R+1):
        d=L[r][:]
        for _ in range(r): d=delta(d)
        assert all(v==a**r for v in d), ('polynomial degree/leading coefficient',r,theta,d[:5],a**r)
        c=[]
        Qvals=[L[r][v+1]*L[r][v+2]-L[r-1][v+2]*L[r+1][v+1] for v in range(2*r+1)]
        f=Qvals[:]
        for _ in range(2*r):f=delta(f)
        top=f[0];expected=Q(C(2*r,r),r+1)*a**(2*r)
        assert top==expected, ('Catalan top term',r,theta,top,expected)
        rows.append({'r':r,'delta_r_Lr':str(d[0]),'c_2r':str(top),'catalan':str(C(2*r,r)//(r+1))})
    return {'theta':str(theta),'a':str(a),'kernel':kern,'rank_checks':rows}

def run():
    ths=[Q(-1,2),Q(0),Q(1,2),Q(15,8),Q(187,100)]
    data=[test_theta(th) for th in ths]
    jets=degeneracy_jets(8)
    record={'schema':'EM_R402_SIGNED_BRC_ALL_CORANK_CATALAN_SANITY_V1',
        'result':'R402_EXACT_FINITE_CROSSCHECK_PASS',
        'claim':'for every r>=1, c_{2r}=Cat_r*(30-16theta)^(2r); proof uses Laurent kernel + Hensel decomposition, not this finite check',
        'scope':'signed K/J raw D finite-sequence model; original twelve branches except K3[t²]=-8(1+theta)',
        'test_theta':[str(t) for t in ths],
        'coranks_tested':'1..8 each theta',
        'checks':{'laurent_kernel_low_orders':len(ths)*3,
                  'polynomial_rth_forward_differences':len(ths)*8,
                  'catalan_top_identities':len(ths)*8,
                  'degeneracy_coefficient_order_checks':sum(x['r'] for x in jets),
                  'turan_4s_divisibility_checks':sum(x['r']-1 for x in jets)},
        'results':data,'degeneracy_jet_results':jets,'scientific_limits':'finite tests support and crosscheck but do not prove all coranks; formal proof separately documented; no original-X6 physical transfer or admission'}
    path=ROOT/'EVIDENCE.json'
    path.write_text(json.dumps(record,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    print('R402_EXACT_FINITE_CROSSCHECK_PASS theta_cases=',len(ths),'ranks=',8,
          'catalan_identities=',len(ths)*8,
          'polynomial_differences=',len(ths)*8, 'degenerate_orders=',sum(x['r'] for x in jets), 'sha256=',hashlib.sha256(path.read_bytes()).hexdigest())
    for v in data:print('theta',v['theta'],'a',v['a'],'last_catalan',v['rank_checks'][-1]['c_2r'])
    return record


# A separate polynomial-jet route in the degeneracy variable a=30-16*theta.
# It is intentionally not needed for the universal proof: small-r independent
# checks may catch formula/index mistakes without changing the proof scope.

def jet_add(x,y): return [a+b for a,b in zip(x,y)]
def jet_mul(x,y):
    n=len(x); out=[Q(0)]*n
    for i,a in enumerate(x):
        if a:
            for j in range(n-i):
                if y[j]:out[i+j]+=a*y[j]
    return out

def degeneracy_jets(R=8):
    DMAX=2*R; N=DMAX+1; MK=2*R+2; MR=R+1
    S=MR+2*MK+2; P=MR+MK+2
    def scalar(v):return [Q(v)]+[Q(0)]*DMAX
    kk=[None]+[K(i) for i in range(1,13)]
    assert kk[3][2]==-8
    kk[3][2]=None
    B=[[[Q(0)]*N for _ in range(P+1)] for _ in range(S+1)]
    B[0][0][0]=B[0][1][0]=Q(1)
    for s in range(1,S+1):
        for j,x in enumerate(J(s)[:P+1]):B[s][j][0]=Q(x)
        for i in range(1,min(s,12)+1):
            for j,k in enumerate(kk[i]):
                if i==3 and j==2:
                    for p in range(j,P+1):
                        source=B[s-i][p-j];target=B[s][p]
                        for n in range(N):
                            target[n]+=-23*source[n]
                            if n>0:target[n]+=Q(1,2)*source[n-1]
                elif k:
                    for p in range(j,P+1):
                        source=B[s-i][p-j];target=B[s][p]
                        for n in range(N):target[n]+=k*source[n]
    def D(q,k):
        out=[Q(0)]*N
        for w in range(k+1):
            v=(-1)**(k-w)*C(k,w)*2**(q-w)
            source=B[q+w][q]
            for n in range(N):out[n]+=v*source[n]
        return out
    L={}
    for r in range(MR+1):
        for k in range(MK+1):
            fac=Q(5)**(r-k)
            L[r,k]=[z*fac for z in D(r+k,k)]
    def sub(a,b):return [x-y for x,y in zip(a,b)]
    def top_delta(r,s):
        def cc(p):
            return sum(C(r-s,j)*C(2*s,p-2*j) for j in range(r-s+1))
        return cc(r)-cc(r-1)
    records=[]
    cat=lambda n: Q(C(2*n,n),n+1)
    for r in range(1,R+1):
        Qvals=[sub(jet_mul(L[r,v+1],L[r,v+2]),jet_mul(L[r-1,v+2],L[r+1,v+1])) for v in range(2*r+1)]
        coeff=[]
        while Qvals:
            coeff.append(Qvals[0]);Qvals=[sub(Qvals[i+1],Qvals[i]) for i in range(len(Qvals)-1)]
        assert len(coeff)==2*r+1
        for s in range(1,r+1):
            j=r+s
            ord_a=next((i for i,x in enumerate(coeff[j]) if x),None)
            if (r%2==0 and s==1):
                expected_ord=3
                expected_val=Q(C(r+1,3))*Q(180)**(r-2)*cat(r//2-1)*(Q(60)+Q(r-2)*Q(6200,180))
            else:
                expected_ord=2*s
                expected_val=Q(C(r+s,2*s))*Q(180)**(r-s)*top_delta(r,s)
            assert ord_a==expected_ord,(r,s,ord_a,expected_ord)
            assert coeff[j][expected_ord]==expected_val,(r,s,coeff[j][expected_ord],expected_val)
        assert coeff[-1][2*r]==cat(r),('Catalan jet',r)
        # Verify the implied 4s-order lower bound for Turan defects exactly.
        for s in range(1,r):
            j=r+s
            tjet=sub(jet_mul(coeff[j],coeff[j]),jet_mul(coeff[j-1],coeff[j+1]))
            assert all(tjet[k]==0 for k in range(4*s) if k<N),(r,s,'T lower bound')
        records.append({'r':r,'all_coeff_orders':
                        {str(r+s):next(i for i,x in enumerate(coeff[r+s]) if x) for s in range(1,r+1)},
                        'highest_c2r_coeff_a2r':str(coeff[-1][-1]),
                        'turan_divisibility_checks':r-1})
    return records

if __name__=='__main__':run()
