"""Exact finite-field verifier for D25 GH-29/GH-30 (author evidence only)."""
from math import comb

def primes_under(limit):
    for p in range(11, limit):
        if p % 8 != 3: continue
        if all(p % d for d in range(2,int(p**0.5)+1)):
            yield p

def character(a,p):
    v = pow(a % p,(p-1)//2,p)
    return 0 if v==0 else 1 if v==1 else -1

def laurent_c(n):
    c=[1,-8]
    for k in range(1,n):
        numerator=-8*(2*k+1)*c[k]-72*k*c[k-1]
        assert numerator % (k+1)==0
        c.append(numerator//(k+1))
    return c

def check(p, verbose=False):
    m=(p-3)//8
    if m<2: return None
    cc=laurent_c(2*m)
    D=comb(3*m+1,m)%p
    targetF=sum(comb(3*m+1,m-r)*comb(m,r)*pow(9,r,p) for r in range(m+1))%p
    targetG=sum((16*r+5)*comb(3*m+1,m-r)*comb(m,r)*pow(9,r,p) for r in range(m+1))%p
    U={}; S_F=S_G=0; B_direct=0
    for x in range(p):
        hf=character(x,p)*pow(x*(1+x),3*m+1,p)*pow(1+9*x,m,p)%p
        hg=character(x,p)*pow(x*(1+x),3*m+1,p)*pow(1+9*x,m-1,p)*(5-9*x)%p
        S_F=(S_F+hf)%p; S_G=(S_G+hg)%p
        if (x*(x+1)*(1+9*x))%p==0:
            assert hf==hg==0, (p,x,hf,hg)
            continue
        v=(1+9*x)*pow(9*x*(x+1),-1,p)%p
        U.setdefault(v,[]).append((x,1+x,hf,hg))
        if character(v,p)==1:
            B_direct=(B_direct+hg)%p
    assert S_F == (-targetF)%p and S_G==(-targetG)%p,(p,S_F,S_G,targetF,targetG)
    M0=M1=0; B_sqrt=0; B_discriminant=0
    for v, roots in U.items():
        chis=[character(t,p) for x,t,hf,hg in roots]
        d=(9*v*v-14*v+9)%p
        assert len(roots)==(1+character(d,p)), (p,v,roots,d)
        if len(roots)==2:
            assert (roots[0][1]*roots[1][1]*9*v-8)%p==0
        if character(v,p)==1:
            assert len(roots)==2 and chis[0]==-chis[1] and sum(z[2] for z in roots)%p==0, (p,v,roots,chis)
            # The branch orientation is fixed by listed root, but the product is root-independent.
            t1,t2=roots[0][1],roots[1][1]
            bs=pow(9,m,p)*pow(v,m,p)*character(t1,p)*(t1-t2)*27*pow(4,-1,p)
            assert bs%p==sum(z[3] for z in roots)%p,(p,v,roots,bs)
            B_sqrt=(B_sqrt+bs)%p
            # Independently reconstruct both roots directly from D(v).
            assert character(d,p)==1
            sqrt_d=pow(d,(p+1)//4,p)
            assert sqrt_d*sqrt_d%p==d
            tplus=(3*(v+1)+sqrt_d)*pow(6*v,-1,p)%p
            tminus=(3*(v+1)-sqrt_d)*pow(6*v,-1,p)%p
            assert {tplus,tminus}=={t1%p,t2%p}
            bdisc=pow(9,m+1,p)*pow(v,m-1,p)*character(tplus,p)*sqrt_d*pow(4,-1,p)
            B_discriminant=(B_discriminant+bdisc)%p
        else:
            assert len(set(chis))==1
            Rbar=(13*v-27)*pow(8*v,-1,p)%p
            hf=sum(z[2] for z in roots)%p
            hg=sum(z[3] for z in roots)%p
            assert hg==hf*Rbar%p,(p,v,roots,hg,hf,Rbar)
            M0=(M0+pow(v,m,p)*sum(chis))%p
            M1=(M1+pow(v,m-1,p)*sum(chis))%p
    assert B_direct==B_sqrt==B_discriminant
    assert M0==(-pow(72,-m,p)*cc[2*m])%p,(p,'Mm',M0,cc[2*m])
    assert M1==(-pow(72,1-m,p)*cc[2*m-2])%p,(p,'Mm-1',M1,cc[2*m-2])
    S_G_non=(pow(9,m,p)*pow(8,-1,p)*(13*M0-27*M1))%p
    G_nonsq=(-S_G_non)%p
    G_closed=pow(2,-3*m-3,p)*(13*cc[2*m]-1944*cc[2*m-2])%p
    F_closed=pow(2,-3*m,p)*cc[2*m]%p
    assert G_nonsq==G_closed,(p,G_nonsq,G_closed)
    assert targetF==F_closed,(p,'F',targetF,F_closed)
    assert targetG==(G_closed-B_direct)%p,(p,'G',targetG,G_closed,B_direct)
    if verbose:print(f'p={p},m={m},D*F={targetF},D*G={targetG},G_nonsq={G_closed},B_square={B_direct},c_2m={cc[2*m]%p},c_2m-2={cc[2*m-2]%p}')
    return (p,targetF,targetG,G_closed,B_direct)

if __name__=='__main__':
    out=[]
    for p in primes_under(2001):
        r=check(p,verbose=p in (19,43,67,83,107,139,163))
        if r:out.append(r)
    print('PASS_GH29_SIGNED_SQUARE_FIBER_DECOMPOSITION',len(out))
    print('PASS_GH30_TWO_MOMENT_LAURENT_AND_G_PORT_REPAIR',len(out))
    print('nonzero_square_residual_count',sum(z[4]!=0 for z in out),'of',len(out))
    print('class19',sum(z[0]%24==19 for z in out),'class11',sum(z[0]%24==11 for z in out))
