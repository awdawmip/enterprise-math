#!/usr/bin/env python3
"""GH-88/GH-89 exact finite-field coefficient checks; author evidence, no native admission."""

def primes():
    for p in range(7,2000,4):
        if all(p%q for q in range(2,int(p**0.5)+1)):
            yield p

def cut(a):
    while len(a)>1 and a[-1]==0:a.pop()
    return a

def add(a,b,p):
    return cut([((a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0))%p for i in range(max(len(a),len(b)))])

def mul(a,b,p):
    v=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):v[i+j]=(v[i+j]+x*y)%p
    return cut(v)

def sc(a,k,p):return cut([k*x%p for x in a])
def sub(a,b,p):return add(a,sc(b,-1,p),p)
def sh(a,k):return [0]*k+a
def th(a,p):return cut([i*x%p for i,x in enumerate(a)])
def ev(a,z,p):
    o=0
    for x in a[::-1]:o=(o*z+x)%p
    return o

def coeff(p,d,t):
    v=[1]
    for j in range(d):
        num=(4*j+t)**3
        den=(4*j+t+1)*(4*j+t+2)*(4*j+t+3)
        assert den%p
        v.append(v[-1]*num*pow(den,-1,p)%p)
    return v

def check(p):
    d=(p-3)//4;s=(p-1)//2
    A=coeff(p,d,1);U=coeff(p,d,3)
    D=th(A,p);E=th(D,p);UD=th(U,p);UE=th(UD,p)
    inv=lambda k:pow(k,-1,p)
    P=lambda a,b:mul(a,b,p)
    # Original GH-84 signed bilinear source B(S,U).
    B=P([1,-1],add(sub(P(U,E),P(UD,D),p),P(UE,A),p))
    B=add(B,sc(P([-3,1],P(U,D)),inv(4),p),p)
    B=add(B,sc(P([3,-5],P(UD,A)),inv(4),p),p)
    B=add(B,sc(P([2,-7],P(U,A)),inv(16),p),p)
    # GH-88 intrinsic quadratic source Q(S).
    Q=P([1,-1],sub(sc(P(A,E),2,p),P(D,D),p))
    Q=sub(Q,sc(P([1,1],P(A,D)),inv(2),p),p)
    Q=sub(Q,sc(sh(P(A,A),1),inv(16),p),p)
    rhs=sh(sc(A,A[-1]*inv(4),p),d+1)
    assert add(th(Q,p),sc(Q,s,p),p)==rhs
    qref=[0]*(2*d+2)
    for j,x in enumerate(A):
        n=d+1+j;qref[n]=A[-1]*x*inv(4)*inv((n+s)%p)%p
    assert Q==cut(qref)
    T=add(sc(D,8,p),A,p);H=add(sc(UD,8,p),sc(U,5,p),p);J=th(H,p)
    # GH-88 full signed-source polynomial syzygy: arbitrary S,U.
    left=sub(sub(sc(P(U,Q),8,p),P(U,P(T,T)),p),sc(P(A,B),16,p),p)
    right=P([-72,8],P(U,P(D,D)))
    right=add(right,P(add(P([-18,2],U),P([2,-2],H),p),P(A,D)),p)
    final=add(add(sc(P([-7,1],U),inv(4),p),sc(P([-1,5],H),inv(4),p),p),P([-2,2],J),p)
    right=add(right,P(final,P(A,A)),p)
    assert left==right
    v={k:ev(x,9,p) for k,x in [('S',A),('U',U),('T',T),('H',H),('J',J),('B',B),('Q',Q),('D',D),('E',E)]}
    a,u,t,h,j,b,q=v['S'],v['U'],v['T'],v['H'],v['J'],v['B'],v['Q']
    assert (u*t*t-2*h*a*t+(13*h+16*j+u*inv(2))*a*a+16*a*b-8*u*q)%p==0
    # Distinguish observed roots/zeros from the new proven identities.
    assert h==0 and t==0
    if u==0:
        assert a!=0 and b==(-j*a)%p
        y=(v['D']+1)%p
        e=(8*y*y-5*a*y-9*inv(16)*a*a-q)*inv(16*a%p)%p
        assert (-16*a*e+8*y*y-5*a*y-9*inv(16)*a*a)%p==q
        assert (8*y+a)%p !=t
    return v

if __name__=='__main__':
    out={p:check(p) for p in primes()}
    assert len(out)==154
    assert sum(v['U']==0 for v in out.values())==74
    p23=out[23]
    assert (p23['S'],p23['U'],p23['H'],p23['J'],p23['B'],p23['Q'],p23['D'],p23['E'],p23['T'])==(20,0,0,15,22,6,9,0,0)
    print('PASS_GH88_FULL_POLYNOMIAL_154_PRIMES')
    print('PASS_GH88_TARGET_9_QUADRATIC_154_PRIMES')
    print('PASS_GH89_74_SIGNED_JET_FIBER_WITNESSES')
