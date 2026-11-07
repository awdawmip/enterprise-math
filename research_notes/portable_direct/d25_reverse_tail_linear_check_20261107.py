#!/usr/bin/env python3
"""D25 source-preserving reflected-tail + prefix-jet O(p) certificate.
Pure integer residues; no native H0/B0 experiment or admissions.
"""

def primes(n):
    a=bytearray(b'\1')*(n+1);a[:2]=b'\0\0'
    for k in range(2,int(n**.5)+1):
        if a[k]:a[k*k::k]=b'\0'*(((n-k*k)//k)+1)
    return [p for p in range(5,n+1) if a[p]]


def mod_inverses(p):
    """All nonzero inverses in O(p) F_p arithmetic operations."""
    inv=[0]*p;inv[1]=1
    for j in range(2,p):inv[j]=(-(p//j)*inv[p%j])%p
    return inv


def reflected_readout(p,which):
    """E=2((1+cD)Pi_p(C Q R))(alpha) in O(p) F_p operations."""
    inv=mod_inverses(p)
    if which=='A':
        assert p%6==1
        m=(p-1)//6
        qdeg=m;maxj=4*m-1;alpha=inv[2];inv_alpha=2
        qparams=(m,2*m)
        rparams=(m+1,2*m+1)
        r=inv[18%p]*inv[m+1]*inv[2*m+1]%p
    else:
        assert p%8 in (3,5)
        k=(p-3)//8 if p%8==3 else (p-5)//8
        qdeg=k;maxj=5*k+(0 if p%8==3 else 2)
        alpha=inv[9%p];inv_alpha=9
        qparams=(k,3*k+1)
        rparams=(k+1,3*k+2)
        r=3*inv[64%p]*inv[k+1]*inv[3*k+2]%p
    qlist=[1]*(qdeg+1)
    for i in range(qdeg):
        qlist[i+1]=qlist[i]*(qparams[0]-i)*(qparams[1]-i)*inv[i+1]**2%p
    s0=s1=ans=0
    ai=1
    aj=1
    beta_shift=64*alpha%p
    for j in range(maxj+1):
        if j<=qdeg:
            qq=qlist[j]*ai%p
            s0=(s0+qq)%p;s1=(s1+j*qq)%p
        rr=r*aj%p
        if which=='A':
            val=6*s1-(6*j+5)*s0
        elif p%8==3:
            val=8*s1-(8*j+7)*s0
        else:
            # C(z)=1-z: the i=j term in C QR has no z^(p) contribution.
            diag=qlist[j]*ai%p if j<=qdeg else 0
            val=beta_shift*(s1-(j+1)*s0)+alpha*diag
        ans=(ans+2*rr*val)%p
        if j<maxj:
            r=r*(j+1)**2*inv[rparams[0]+j+1]*inv[rparams[1]+j+1]%p
            ai=ai*alpha%p
            aj=aj*inv_alpha%p
    return ans


def euler_diagonal(p):
    """True cutoff i=j contribution from C=1-z when p=8k+5."""
    assert p%8==5
    inv=mod_inverses(p);k=(p-5)//8;beta=inv[9%p]
    q=1;r=3*inv[64%p]*inv[k+1]*inv[3*k+2]%p
    total=0
    for j in range(k+1):
        total=(total+2*beta*q*r)%p
        if j<k:
            q=q*(k-j)*(3*k+1-j)*inv[j+1]**2%p
            r=r*(j+1)**2*inv[k+j+2]*inv[3*k+j+3]%p
    return total


def direct_readout(p,which):
    """Independent p^3 3F2-versus-Gauss short-jet (no reflected factorials)."""
    M=p**3
    if which=='A':
        m=(p-1)//6;lim=2*m;alpha=pow(2,-1,M)
        aa=1; full=0; f=1;Q=DQ=0
        for n in range(p):
            full=(full+(6*n+1)*aa)%M
            if n<=lim:
                Q=(Q+f*pow(alpha,n,M))%M
                DQ=(DQ+n*f*pow(alpha,n,M))%M
            if n<p-1:
                aa=aa*(2*n+1)*(3*n+1)*(3*n+2)*pow(36*(n+1)**3,-1,M)%M
                f=f*(6*n+1)*(3*n+1)*pow(18*(n+1)**2,-1,M)%M
        G=(Q*Q+12*Q*DQ)%M
    else:
        k=(p-3)//8 if p%8==3 else (p-5)//8
        lim=3*k+1;alpha=pow(9,-1,M)
        x,y=(1,3) if p%8==3 else (5,7)
        bb=1;full=0;g=1;Q=DQ=0
        for n in range(p):
            full=(full+(8*n+1)*bb)%M
            if n<=lim:
                Q=(Q+g*pow(alpha,n,M))%M
                DQ=(DQ+n*g*pow(alpha,n,M))%M
            if n<p-1:
                bb=bb*(4*n+1)*(2*n+1)*(4*n+3)*pow(288*(n+1)**3,-1,M)%M
                g=g*(8*n+x)*(8*n+y)*pow(64*(n+1)**2,-1,M)%M
        if p%8==3:G=(Q*Q+16*Q*DQ)%M
        else:G=(128*pow(9,-1,M)*Q*DQ)%M
    diff=(full-G)%M
    assert diff%(p*p)==0,(p,which,full,G,diff)
    return diff//(p*p)%p


def main():
    allp=[p for p in primes(2500) if p%24 in (13,19)]
    for p in allp:
        for name in ('A','B'):
            x=reflected_readout(p,name)
            y=direct_readout(p,name)
            assert x==y,(p,name,x,y)
    cases={p:(reflected_readout(p,'A'),reflected_readout(p,'B')) for p in (13,19,43,67,373)}
    assert cases=={13:(9,0),19:(13,8),43:(31,33),67:(30,46),373:(1,220)},cases
    print('PASS',len(allp),'target primes p<=2500; independently checked both A and B readouts; operations O(p) per model')
    print('cases',cases)
    diagonal={p:euler_diagonal(p) for p in (13,37,373)}
    assert diagonal[13]==3 and diagonal[373]==289,diagonal
    nonzero=sum(1 for p in allp if p%8==5 and euler_diagonal(p)!=0)
    total=sum(p%8==5 for p in allp)
    print('Euler diagonal',diagonal,'nonzero',nonzero,'of',total,'p=8k+5 instances')

if __name__=='__main__':main()
