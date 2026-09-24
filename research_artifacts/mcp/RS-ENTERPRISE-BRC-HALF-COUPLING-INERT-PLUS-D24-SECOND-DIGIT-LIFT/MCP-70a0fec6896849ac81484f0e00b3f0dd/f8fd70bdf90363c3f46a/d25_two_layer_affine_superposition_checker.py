from math import isqrt

def inv(a,m): return pow(a%m,-1,m)
def primes(n): return [x for x in range(2,n) if all(x%d for d in range(2,isqrt(x)+1))]

def Bseq(p):
    M=p**3; B=[1]; cur=1
    for k in range(p-1):
        cur=cur*((6*k+1)*(3*k+1)%M)*inv(36*(k+1)*(k+1),M)%M
        B.append(cur)
    return B

def lam(p,s):
    return s*s*(6*s+1)%p*inv((s+1)*(2*s+1)*(3*s+2),p)%p

def mu(p,s):
    num=(2*s+1)*(3*s+1)*(3*s+2)*(6*s+7)**2
    den=36*(s+1)*(6*s+1)*(s+2)*(2*s+3)*(3*s+5)
    return num%p*inv(den,p)%p

def q1(p,Gpart,Hpart):
    d=(Gpart%(p*p))*(Hpart%(p*p))-1
    d%=p*p; assert d%p==0
    return d//p%p

def q2(p,Gpart,Hpart):
    M=p**3
    d=(Gpart%(p*p))*(Hpart%M)-1
    d%=M; assert d%p==0
    return d//p%(p*p)

def Rm(p):
    m=(p-1)//6
    t=[1]; w=[1]
    cur=1
    for h in range(m):
        cur=cur*((2*h+1)*(3*h+1)*(3*h+2)%p)*inv(36*(h+1)**3,p)%p
        t.append(cur); w.append((6*(h+1)+1)*cur%p)
    P=0; d=1; R=0
    for s in range(1,m+1):
        P=(P+w[s-1])%p
        h=s-1
        d=d*((6*h+1)*(h+1)%p)*inv((2*h+1)*(3*h+2),p)%p
        c=d*inv(6*s*s,p)%p
        R=(R+c*P)%p
    return R

def check(p):
    m=(p-1)//6; M=p**3; B=Bseq(p)
    g=sum(B)%M
    h=sum(((12*k+1)%M)*B[k] for k in range(p))%M
    assert g%p==0
    G=(g//p)%(p*p); Gbar=G%p; hbar=h%p
    Delta=q1(p,G,h)
    QM=[]; QT=[]; QC=[]
    for s in range(m+1):
        rr=range(s+1,m+1)
        Mh=sum((12*(m+r)+1)*B[m+r] for r in rr)%M
        Tg=sum(B[p-r] for r in rr)%M
        Th=sum((12*(p-r)+1)*B[p-r] for r in rr)%M
        assert Mh%p==0 and Tg%(p*p)==0 and Th%(p*p)==0
        gp=(g-Tg)%M; assert gp%p==0
        Gp=(gp//p)%(p*p)
        qm=q1(p,G,(h-Mh)%M)
        qt=q1(p,Gp,(h-Th)%M)
        qc=q1(p,Gp,(h-Mh-Th)%M)
        QM.append(qm); QT.append(qt); QC.append(qc)
        assert (qc-qm-qt+Delta)%p==0
        Xi=((Tg//(p*p))%p)*((Mh//p)%p)%p
        qm2=q2(p,G,(h-Mh)%M); qt2=q2(p,Gp,(h-Th)%M)
        qc2=q2(p,Gp,(h-Mh-Th)%M); de2=q2(p,G,h)
        assert (qc2-qm2-qt2+de2)%(p*p)==p*Xi%(p*p)
    assert QM[m]==QT[m]==QC[m]==Delta

    def U(A): return [None]+[(A[s]-A[s-1])%p for s in range(1,m+1)]
    UM,UT,UC=U(QM),U(QT),U(QC)
    for s in range(1,m+1): assert UC[s]==(UM[s]+UT[s])%p

    def V(U):
        A=[None]*m
        for s in range(1,m): A[s]=(U[s+1]-lam(p,s)*U[s])%p
        return A
    VM,VT,VC=V(UM),V(UT),V(UC)
    for s in range(1,m): assert VC[s]==(VM[s]+VT[s])%p

    def D(V):
        A=[None]*(m-1)
        for s in range(1,m-1): A[s]=(V[s+1]-mu(p,s)*V[s])%p
        return A
    DM,DT,DC=D(VM),D(VT),D(VC)
    for s in range(1,m-1): assert DC[s]==(DM[s]+DT[s])%p

    terminal=None
    if m>=3:
        s=m-2
        xm=(B[2*m]//p)%p
        ym=(B[p-m]//(p*p))%p
        dm=(-42062*inv(343,p)*Gbar*xm)%p
        dt=(-8069*inv(9604,p)*hbar*ym)%p
        assert DM[s]==dm and DT[s]==dt and DC[s]==(dm+dt)%p
        terminal=(DC[s],dm,dt,Gbar,hbar,xm,ym)

    assert Delta==Rm(p)
    return terminal

def main():
    T=[p for p in primes(5000) if p%24 in (13,19)]
    assert len(T)==166 and sum(p%24==13 for p in T)==83 and sum(p%24==19 for p in T)==83
    zero=[]
    for p in T:
        z=check(p)
        if z is not None and z[0]==0: zero.append((p,z))
    assert len(zero)==1 and zero[0][0]==163
    assert zero[0][1]==(0,60,103,154,18,150,22)
    print('targets',len(T),'failures',0,'terminal_zero_witnesses',zero)

if __name__=='__main__': main()
