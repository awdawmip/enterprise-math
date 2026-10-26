"""Exact finite-ring author check for affine-rank Ward seam; not native CM."""
from math import comb
from fractions import Fraction

def primes(n):
    return [v for v in range(2,n+1) if all(v%q for q in range(2,int(v**.5)+1))]

def poly(p):
    M=2*((p-1)//6)-1
    R,D=1,0
    for s in range(1,M+1):
        term=comb(2*s,s)*pow(8,-s,p)%p
        R,D=(R+term)%p,(D+s*term)%p
    return M,R,D,comb(2*M,M)*pow(8,-M,p)%p

def seam(p,A,B,digits=2):
    mod=p**digits; M=2*((p-1)//6)-1
    neg={}; prev=0
    for n in range(-M,0):
        w=(A+B*n)*pow(2,n,mod)%mod
        prev=(w+(p-2*n+1)*prev)*pow(p-2*n,-1,mod)%mod
        neg[n]=prev
    Xi=(A+(p+1)*prev)%mod
    pos={}; prev=0
    for n in range(1,M+1):
        w=(A+B*n)*pow(2,n,mod)%mod
        prev=(w+(p-2*n+1)*prev)*pow(p-2*n,-1,mod)%mod
        pos[n]=prev
    return Xi,neg,pos

def main():
    checks=0
    def ck(ok,tag):
        nonlocal checks
        checks+=1
        if not ok: raise AssertionError(tag)
    for M in range(1,9):
        t=lambda s: Fraction(comb(2*s,s),8**s)
        R=sum((t(s) for s in range(M+1)),Fraction())
        D=sum((s*t(s) for s in range(1,M+1)),Fraction())
        ck(2*D==R-(2*M+1)*t(M),f"rational {M}")
        ck(R+6*D==4*R-3*(2*M+1)*t(M),f"signed {M}")
    ps=[p for p in primes(997) if p%6==1]; resonances=[]
    for p in ps:
        M,R,D,tail=poly(p)
        ck((2*D-R+(2*M+1)*tail)%p==0,f"derivative {p}")
        ck(tail!=0,f"unit {p}")
        for A,B in ((1,0),(1,-6),(3,4)):
            Xi,neg,pos=seam(p,A,B)
            ck(Xi%p==(A*R-B*D)%p,f"residue {p} {A} {B}")
            mod=p*p
            Y={n:(n**3+7*n+11)%mod for n in range(-M,M+1)}
            Y[M+1]=0
            S={n:((p-2*n)*Y[n]-(p-2*n-1)*Y[n+1])%mod for n in range(-M,M+1)}
            lhs=sum((A+B*n)*pow(2,n,mod)*Y[n] for n in range(-M,M+1))%mod
            rhs=(sum(neg[n]*S[n] for n in range(-M,0))
                 +sum(pos[n]*S[n] for n in range(1,M+1))+Xi*Y[0])%mod
            ck(lhs==rhs,f"telescoping {p} {A} {B}")
            if Xi%p==0: ck(Xi//p<p,f"integral {p}")
        if R==0:
            resonances.append(p)
            ck(D!=0,f"nonzero derivative {p}")
            ck((R+6*D)%p!=0,f"signed nonzero {p}")
    ck(resonances==[733],f"bounded census {resonances}")
    ck(poly(733)==(243,0,522,40),"p733")
    ck(seam(733,1,0,3)[0]==137318021,"geometric third digit")
    ck(seam(733,1,-6,3)[0]==191840960,"signed third digit")
    ck(seam(733,1,-6,2)[0]==28787,"signed second digit")
    ck(poly(13)==(3,9,10,4),"p13 control")
    print(f"PASS {checks} exact assertions, {len(ps)} primes; geometric resonances in range: {resonances}")

if __name__=="__main__": main()
