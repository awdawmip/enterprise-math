"""D25 original 216/2304 signed-port p^5 carry; exact stdlib certificate."""
from math import comb, isqrt

LIMIT = 12000
FIXED = (5, 7, 13, 19, 71, 107, 137, 373, 1289)


def primes(bound):
    s = bytearray(b'\x01') * bound
    s[:2] = b'\x00\x00'
    for i in range(2, isqrt(bound - 1) + 1):
        if s[i]:
            s[i*i:bound:i] = b'\x00' * (1 + (bound - 1 - i*i)//i)
    return (p for p in range(5, bound) if s[p])


def ledger(p, direct=False):
    M=p**5
    a=b=u=v=1
    A=[0]*4; B=[0]*4
    inv36=pow(36,-1,M); inv576=pow(576,-1,M)
    d216=pow(216,-1,M); d2304=pow(2304,-1,M)
    for n in range(p):
        if direct:
            c=comb(2*n,n)**2
            a=c*comb(3*n,n)*u%M
            b=c*comb(4*n,2*n)*v%M
            u=u*d216%M; v=v*d2304%M
        ja=(2*n)//p+(3*n)//p
        jb=(4*n)//p
        A[ja]=(A[ja]+(6*n+1)*a)%M
        B[jb]=(B[jb]+(8*n+1)*b)%M
        if not direct and n+1<p:
            t=pow(n+1,-3,M)
            a=a*(2*n+1)*(3*n+1)*(3*n+2)*inv36*t%M
            b=b*(4*n+1)*(4*n+2)*(4*n+3)*inv576*t%M
    chi=1 if p%3==1 else -1
    T=[]; V=[]; e=0
    for j in range(4):
        e=(e+A[j]-2*B[j]+(p*chi if j==0 else 0))%M
        T.append(e)
        if e==0: V.append(5)
        else:
            k=0; z=e
            while z%p==0: k+=1; z//=p
            V.append(k)
    return (A,B,T,V)


def main():
    extra={j:[] for j in range(4)}
    short={j:[] for j in range(4)}
    count=target=0
    for p in primes(LIMIT):
        count+=1
        target+=(p%24 in (13,19))
        v=ledger(p)[-1]
        for j in range(4):
            if v[j] > j+1: extra[j].append(p)
            if v[j] < j+1: short[j].append(p)
    assert (count,target)==(1436,363)
    assert all(not x for x in short.values()), short
    assert extra=={0:[7,71,137],1:[],2:[107,1289],3:[5,7]},extra
    print('PRIMES',count,'FROZEN_CLASS_PRIMES',target)
    print('LOWER_BOUND_FAILURES',short)
    print('EXTRA_DIVISIBILITY',extra)
    for p in FIXED:
        r=ledger(p)
        assert r==ledger(p,direct=True),p
        print('P',p,'T_MOD_P5',r[2],'V_CAP5',r[3], 'RAW_BINOMIAL_PASS')
    assert ledger(7)[-1][:3]==[3,2,3]
    assert ledger(71)[-1][0]==2
    assert ledger(107)[-1][2]==4
    print('PASS_D25_ORIGINAL_SOURCE_PORT_EXCEPTIONAL_CARRIES')


if __name__=='__main__':
    main()
