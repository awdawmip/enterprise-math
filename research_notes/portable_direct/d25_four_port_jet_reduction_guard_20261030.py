#!/usr/bin/env python3
"""D25 ORIGINAL-OBSERVER four-port p-adic residual; AUTHOR-SIDE, NOT NATIVE.

No new axioms, no network, stdlib exact residue arithmetic. Enumerates target primes,
independently checks original A216 and Gauss finite coefficient recurrences.
"""
from math import isqrt


def target_primes(limit):
    for p in range(7, limit):
        if p % 24 not in (13, 19):
            continue
        if all(p % d for d in range(2, isqrt(p) + 1)):
            yield p


def three_stratum_ports(p):
    assert p % 6 == 1 and p >= 7
    m = (p-1)//6
    q, q2 = p**3, p**2
    # Every denominator explicitly inverted below is a p-unit (index <p).
    f = [1] * p
    for j in range(1, p):
        f[j] = f[j-1] * j % q2
    H, H2 = [0]*p, [0]*p
    for j in range(1, p):
        u=pow(j,-1,q2)
        H[j]=(H[j-1]+u)%q2
        H2[j]=(H2[j-1]+u*u)%q2
    inv2=pow(2,-1,q)
    inv3,inv6=pow(3,-1,q2),pow(6,-1,q2)
    inv9,inv36=pow(9,-1,q2),pow(36,-1,q2)
    V0=V1=V2=W0=W1=0
    s0=s1=s2=0
    Yparts=[0,0,0]
    half=1
    B=1
    for n in range(p):
        if n<=m:
            L= (-(H[m]-H[m-n])*inv6-(H[2*m]-H[2*m-n])*inv3)%q2
            J= ((H2[m]-H2[m-n])*inv36+(H2[2*m]-H2[2*m-n])*inv9)%q2
            v0=B*half%q
            v1=(v0%q2)*L%q2
            v2=(v0%p)*((L*L-J)*pow(2,-1,p)%p)%p
            V0=(V0+v0)%q
            V1=(V1+v1)%q2
            V2=(V2+v2)%p
            Yparts[0]=(Yparts[0]+v2)%p
            W0=(W0+2*n*v0)%q2
            W1=(W1+2*n*v1)%p
            s0=(s0+v0+p*v1+p*p*v2)%q
            if n<m:
                B=B*(m-n)*(2*m-n)*pow((n+1)**2,-1,q)%q
        elif n<=2*m:
            numer=(-1 if (m+n)%2 else 1)*f[m]*f[n-m-1]*f[2*m]
            denom=6*f[2*m-n]*f[n]*f[n]
            T=numer*pow(denom,-1,q2)%q2
            K=((H[n-m-1]-H[m])*inv6-(H[2*m]-H[2*m-n])*inv3)%q2
            v1=T*half%q2
            v2=v1*K%p
            V1=(V1+v1)%q2
            V2=(V2+v2)%p
            Yparts[1]=(Yparts[1]+v2)%p
            W1=(W1+2*n*v1)%p
            s1=(s1+p*v1+p*p*v2)%q
        else:
            numer=(-1 if m%2 else 1)*f[m]*f[2*m]*f[n-m-1]*f[n-2*m-1]
            denom=18*f[n]*f[n]
            U=numer*pow(denom,-1,p)%p
            v2=U*half%p
            V2=(V2+v2)%p
            Yparts[2]=(Yparts[2]+v2)%p
            s2=(s2+p*p*v2)%q
        half=half*inv2%q
    assert V0%p==0,(p,'CM zero input violated')
    X=(V0//p+V1)%q2
    Y=V2%p
    g=(W0+p*W1)%q2
    h=(X+p*Y)%q2
    return {'p':p,'m':m,'V0':V0,'V1':V1,'V2':Y,'X':X,'W0':W0,'W1':W1,
            'h':h,'g':g,'Yparts':Yparts,'M':(s0+s1+s2)%q, 'S0':s0,'S1':s1,'S2':s2}


def independently_original(p):
    q=p**3
    # Original 216 a_n ratio, not three-stratum or Clausen construction.
    a=1; A=0
    for n in range(p):
        A=(A+(6*n+1)*a)%q
        if n<p-1:
            a=a*(2*n+1)*(3*n+1)*(3*n+2)*pow(36*(n+1)**3,-1,q)%q
    # Original Gauss c_n/2^n ratio, independent from stratum factorials/harmonics.
    M=g=0
    c=1
    for n in range(p):
        M=(M+c)%q
        g=(g+2*n*c)%q
        if n<p-1:
            c=c*(6*n+1)*(3*n+1)*pow(36*(n+1)**2,-1,q)%q
    return A,M,g


def original_signed_reflection_and_joint(p):
    """Independent original triangular R and new combined (i,a) signed strip."""
    m=(p-1)//6
    C=[0]*(4*m+1)
    C[1]=pow(10,-1,p)
    for a in range(1,4*m):
        C[a+1]=C[a]*36*a*a*pow((6*a+5)*(3*a+2),-1,p)%p
    P=[0]*(4*m+1); Q=[0]*(4*m+1)
    for a in range(1,4*m+1):
        P[a]=(P[a-1]+C[a])%p
        Q[a]=(Q[a-1]+(6*a-1)*C[a])%p
    F=P[4*m]
    R=J=0
    b=1
    for i in range(1,m+1):
        b=b*(m-i+1)*(2*m-i+1)*pow(2*i*i,-1,p)%p
        # This is the original uncollapsed signed triangular observer.
        T=sum((1+6*(i-a))*C[a] for a in range(1,i+1))%p
        R=(R+2*b*T)%p
        # Two original relation branches: a<=i, i<a<=4m.
        J=(J+2*b*(Q[i]+6*i*(F-P[i])))%p
    return R,F,J


def check_prime(p):
    t=three_stratum_ports(p)
    A,M,g=independently_original(p)
    R,F,J=original_signed_reflection_and_joint(p)
    q=p**3; q2=p*p
    assert t['M']==M,(p,'Gauss coefficient source mismatch')
    assert t['g']==g%q2,(p,'Gauss derivative mismatch')
    assert M%p==0,(p,'CM Gauss zero mismatch')
    assert t['h']==M//p%q2,(p,'normalized Gauss value mismatch')
    X,Y,W0,W1=t['X'],t['V2'],t['W0'],t['W1']
    assert F==t['Yparts'][2],(p,'high-tail reflection source mismatch')
    assert J==(6*F*W0-R)%p,(p,'joint signed strip kernel mismatch')
    assert (6*X*W0-1)%p==0,(p,'first digit premise mismatch')
    assert (A-p)%q2==0,(p,'original weighted first digit mismatch')
    K=((6*X*W0-1)%q2)//p
    parts=[K%p,6*X*W1%p,6*Y*W0%p,(X*X-R)%p]
    # Subtracting the actual frozen signed R, not a fitted constant.
    obstruction=sum(parts)%p
    joint_ports=[parts[0],parts[1],(6*(Y-F)*W0)%p,(X*X)%p,J]
    assert sum(joint_ports)%p==obstruction,(p,'joint-port obstruction mismatch')
    source_delta=((6*t['h']*t['g']+p*t['h']**2-1)%q2)//p
    assert (source_delta-R)%p==obstruction,(p,'original signed R port')
    assert ((A-p)%q)//q2==obstruction,(p,'independent original 216 bridge')
    return dict(p=p,m=t['m'],R=R,source_delta=source_delta,original_A=A,
                X_mod_p=X%p,W0_mod_p=W0%p,Y=Y,W1=W1,
                four_ports=parts,joint_ports=joint_ports,high_F=F,high_signed_joint=J,
                Yparts=t['Yparts'],obstruction=obstruction,
                original_source_strata=[t['S0'],t['S1'],t['S2']])


if __name__=='__main__':
    import json
    primes=list(target_primes(5000))
    records=[check_prime(p) for p in primes]
    assert len(primes)==166,len(primes)
    print('CHECKED',len(records),'TARGET_PRIMES_LT_5000')
    print('EXACT_216_SECOND_DIGIT_NONZERO',[(r['p'],r['obstruction']) for r in records if r['obstruction']])
    print('EVERY_PORT_NONZERO_COUNT',sum(all(r['four_ports']) for r in records))
    for p in [13,19,67,373]:
        print('WITNESS',json.dumps(next(r for r in records if r['p']==p),sort_keys=True))
    print('PASS_D25_ORIGINAL_SIGNED_FOUR_PORT_LIFT_REDUCTION')
