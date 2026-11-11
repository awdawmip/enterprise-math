#!/usr/bin/env python3
"""Exact independent modular certificates at p=101419; optional audit of 22042-row CSV."""
import csv,sys
P=101419; E=0; M=(P-1)//6; Q=P**4

def factorial_tables(N,m):
    f=[1]*(m+1)
    for j in range(1,m+1):f[j]=f[j-1]*j%N
    invf=[0]*(m+1); invf[m]=pow(f[m],-1,N)
    for j in range(m,0,-1):invf[j-1]=invf[j]*j%N
    return f,invf

def first_two_ports_by_factorials(N,p,e,m):
    f,iv=factorial_tables(N,2*m+e)
    C=lambda n,k:f[n]*iv[k]*iv[n-k]%N
    z=1; half=pow(2,-1,N); A=B=0
    for k in range(m+1):
        a=C(m,k)*C(2*m+e,k)*z%N
        A=(A+a)%N;B=(B+(1-6*e+12*k)*a)%N
        z=z*half%N
    return A,B

def first_two_ports_by_recurrence(N,p,e,m):
    term=1; A=1; B=(1-6*e)%N; half=pow(2,-1,N)
    for k in range(1,m+1):
        term=term*(m-k+1)*(2*m+e-k+1)*pow(k,-2,N)*half%N
        A=(A+term)%N;B=(B+(1-6*e+12*k)*term)%N
    return A,B

def original_W_by_factorial(N,p):
    f=[1]*(3*p-2)
    for j in range(1,len(f)): f[j]=f[j-1]*j%N
    _,iv=factorial_tables(N,p-1)
    d=pow(216,-1,N);z=1;W=0
    for k in range(p):
        a=f[2*k]*f[3*k]*pow(iv[k],5,N)*z%N
        W=(W+(6*k+1)*a)%N;z=z*d%N
    return W

def original_W_by_ratio(N,p):
    f,iv=factorial_tables(N,p-1)
    d=pow(216,-1,N);a=1;W=0
    for k in range(p):
        W=(W+(6*k+1)*a)%N
        if k+1<p:
            invk=f[k]*iv[k+1]%N
            a=a*(2*k+1)*(2*k+2)*(3*k+1)*(3*k+2)*(3*k+3)*d*pow(invk,5,N)%N
    return W

def audit_csv(path):
    lim=250000
    sieve=bytearray(b"\x01")*(lim+1);sieve[:2]=b"\x00\x00"
    for n in range(2,int(lim**0.5)+1):
        if sieve[n]:sieve[n*n:lim+1:n]=b"\x00"*((lim-n*n)//n+1)
    expected=[n for n in range(5,lim+1) if sieve[n]]
    with open(path,newline='') as f: rows=list(csv.DictReader(f))
    assert len(rows)==len(expected)==22042
    assert [int(row['p']) for row in rows]==expected
    counts={'A':0,'B':0};anomalies=[]
    for row in rows:
        p=int(row['p']);e=int(row['e']);m=int(row['m'])
        a=int(row['A_mod_p2']);b=int(row['B_mod_p2'])
        assert 6*m+1+4*e==p and e==(p%6==5)
        assert 0<=a<p*p and 0<=b<p*p
        port=row['zero_port'];counts[port]+=1
        assert (a%p==0)!=(b%p==0)
        assert (a%p==0)==(port=='A')
        chi=1 if pow((-6)%p,(p-1)//2,p)==1 else -1
        assert chi==int(row['chi_minus6'])
        assert (port=='A')==(chi==-1)
        vanished=(a if port=='A' else b)==0
        assert int(row['zero_port_order_at_least_2'])==int(vanished)
        if vanished:anomalies.append(p)
    assert counts=={'A':11055,'B':10987}
    assert anomalies==[149,211,101419]
    print('PASS complete 22042-prime CSV ledger and three exceptional ports')

if __name__=='__main__':
    assert P%24==19 and 6*M+1==P
    A,B=first_two_ports_by_factorials(Q,P,E,M)
    assert (A,B)==first_two_ports_by_recurrence(Q,P,E,M)
    assert (A,B)==(72047771727655493387,31417925454066666178)
    assert A%(P*P)==0 and A%(P**3)==757365024123552
    assert A%(P**3)!=0 and (A//P**2)%P==73632
    assert B%(P*P)==309350689 and B%P==22739
    W=original_W_by_factorial(Q,P)
    assert W==original_W_by_ratio(Q,P)
    assert W==58985396077906829515
    assert W%(P**3)==P and ((W-P)//P**3)%P==56544
    print('PASS p',P,'m',M,'e',E,'P²',P**2,'P³',P**3,'P⁴',Q)
    print('A mod P⁴',A,'B mod P⁴',B,'v_P(A)=2','A/P² mod P=73632','B mod P²=309350689')
    print('W mod P⁴',W,'(W-P)/P³ mod P=56544')
    if len(sys.argv)>1:audit_csv(sys.argv[1])
