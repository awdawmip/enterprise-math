"""D25 portable author-side source-fiber structural certificate (not native Source evidence).

The integer jets are computed by an undivided polynomial recurrence; no division by
zero-valued binomial coefficients. A mod p^2, Hessian mod p.
"""
from math import isqrt

def primes_to(N):
    sieve=bytearray([1])*(N+1);sieve[:2]=b'\0\0'
    for a in range(2,isqrt(N)+1):
        if sieve[a]:sieve[a*a:N+1:a]=b'\0'*(((N-a*a)//a)+1)
    return [p for p in range(7,N+1) if sieve[p] and p%6==1]

def jets(p, modulus, second=True):
    m=(p-1)//6;s=(2*m,3*m,4*m)
    B=[1,1,1]; D=[0,0,0]; E=[0,0,0]
    A=[0,0,0]; H=[[0]*3 for _ in range(3)]; total=0; f=1
    neg_half=pow(-2,-1,modulus)
    for j in range(p):
        weight=(6*j+1)*f%modulus
        total=(total+weight*B[0]*B[1]*B[2])%modulus
        for i in range(3):
            u=(i+1)%3;v=(i+2)%3
            A[i]=(A[i]+weight*D[i]*B[u]*B[v])%modulus
            if second: H[i][i]=(H[i][i]+weight*E[i]*B[u]*B[v])%modulus
        if second:
            for i in range(3):
                for k in range(i+1,3):
                    l=3-i-k
                    H[i][k]=(H[i][k]+weight*D[i]*D[k]*B[l])%modulus
                    H[k][i]=H[i][k]
        if j==p-1:break
        iv=pow(j+1,-1,modulus)
        newB=[(B[i]*(s[i]-j)*iv)%modulus for i in range(3)]
        newD=[((D[i]*(s[i]-j)+B[i])*iv)%modulus for i in range(3)]
        newE=[((E[i]*(s[i]-j)+2*D[i])*iv)%modulus for i in range(3)]
        B,D,E=newB,newD,newE
        f=f*neg_half%modulus
    return total,A,H

def outer_values(p):
    _,A,_=jets(p,p*p,False); _,T,H=jets(p,p,True)
    v=[-pow(3,-1,p),-pow(2,-1,p),-2*pow(3,-1,p)]
    assert [a%p for a in A] ==T
    assert (T[0]+T[2])%p==0, ('outer sum conjecture failure',p,T)
    # Along d=(1,0,1), A_1+A_3 is divisible by p.
    k=((A[0]+A[2])//p+sum(v[i]*(H[i][0]+H[i][2]) for i in range(3)))%p
    c=((H[0][0]+2*H[0][2]+H[2][2])*pow(2,-1,p))%p
    # Coefficients of full outer-plane second digit only legitimate if T1=T3=0.
    q=None
    if T[0]==0 and T[2]==0:
        l0=(A[0]//p+sum(v[i]*H[i][0] for i in range(3)))%p
        l2=(A[2]//p+sum(v[i]*H[i][2] for i in range(3)))%p
        a=H[0][0]*pow(2,-1,p)%p;b=H[0][2];d=H[2][2]*pow(2,-1,p)%p
        disc=(b*b-4*a*d)%p
        q=dict(a=a,b=b,c=d,l0=l0,l2=l2,disc=disc,
               disc_type='zero' if disc==0 else 'square' if pow(disc,(p-1)//2,p)==1 else 'nonsquare')
    if T[0]: rank='nonzero-outer-first-digit'; collision_count=(2 if (k and c) else p if (not k and not c) else 1)
    else:rank='zero-outer-first-digit'; collision_count=None
    return {'p':p,'T':T,'A':A,'H':H,'rank':rank,'k':k,'c':c,'lambda2':((-k*pow(c,-1,p))%p if c else None),'line_zero_count':collision_count,'Q':q}

if __name__=='__main__':
    # Exact finite scan, not a general proof of these two congruences.
    ps=primes_to(5000)
    target_count=0
    errors=[]; qzero=[]; czero=[]; outerzero=[]; unitline=0; twoline=0
    for p in ps:
        o=outer_values(p)
        q2=(pow(2,p-1,p*p)-1)//p
        if (o['k']+3*q2)%p:
            errors.append((p,o['k'],q2))
        if p%24 in (13,19):target_count+=1
        if q2==0:qzero.append((p,o['k'],o['c']))
        if o['c']==0:czero.append(p)
        if o['T'][0]==0:outerzero.append((p,o['T']))
        if o['T'][0]:
            if o['line_zero_count']==1:unitline+=1
            elif o['line_zero_count']==2:twoline+=1
            else:raise AssertionError((p,'unexpected line type',o))
        if p in (13,19,211,373,1093,3511):
            print('SAMPLE',p,'mod24',p%24,'T',o['T'],
                  'k',o['k'],'c',o['c'],'q2',q2,
                  'lambda_nonzero',o['lambda2'],
                  'outer_first_digit_rank', 0 if o['T'][0]==0 else 1)
    assert not errors,errors
    assert len(ps)==330 and target_count==166
    assert qzero==[(1093,0,761),(3511,0,1757)],qzero
    assert not czero,czero
    assert [p for p,_ in outerzero]==[7,211],outerzero
    assert twoline==326 and unitline==2,(twoline,unitline)
    print('PASS p<=5000; 330 primes p=1(mod6), 166 target p=13/19(mod24)')
    print('k+3q_p(2)=0 all 330 finite instances; c!=0 in all; no universal proof asserted')
    print('Outer first-digit rank zero at p=7,211 only in scan')
    print('Along d=(1,0,1), 326 nonzero-rank cases with two collisions,')
    print('2 nonzero-rank cases with unique collision: p=1093,3511')
