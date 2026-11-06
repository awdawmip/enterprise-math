"""D25 p=211 finite exact source-jet certificate, author-side portable, not native.

Only modular arithmetic and p-local inverses; no floating point or external libs.
"""
P=211
M=(P-1)//6
S=(2*M,3*M,4*M)


def source_jets(modulus, include_hessian=False):
    B=[1]*3; D=[0]*3; E=[0]*3
    base=0; A=[0]*3; H=[[0]*3 for _ in range(3)]
    factor=1; minus_half=pow(-2,-1,modulus)
    for j in range(P):
        w=(6*j+1)*factor%modulus
        base=(base+w*B[0]*B[1]*B[2])%modulus
        for i in range(3):
            A[i]=(A[i]+w*D[i]*B[(i+1)%3]*B[(i+2)%3])%modulus
            if include_hessian:
                H[i][i]=(H[i][i]+w*E[i]*B[(i+1)%3]*B[(i+2)%3])%modulus
        if include_hessian:
            for i in range(3):
                for k in range(i+1,3):
                    l=3-i-k
                    H[i][k]=(H[i][k]+w*D[i]*D[k]*B[l])%modulus
                    H[k][i]=H[i][k]
        if j==P-1: break
        iv=pow(j+1,-1,modulus)
        Bnew=[B[i]*(S[i]-j)*iv%modulus for i in range(3)]
        Dnew=[(D[i]*(S[i]-j)+B[i])*iv%modulus for i in range(3)]
        Enew=[(E[i]*(S[i]-j)+2*D[i])*iv%modulus for i in range(3)]
        B,D,E=Bnew,Dnew,Enew
        factor=factor*minus_half%modulus
    return base,A,H


def direct_weighted_source(delta):
    q=P**3
    tangent=[-pow(3,-1,q),-pow(2,-1,q),-2*pow(3,-1,q)]
    tangent=[(tangent[i]+delta[i])%q for i in range(3)]
    B=[1]*3; factor=1; value=0; minus_half=pow(-2,-1,q)
    for j in range(P):
        value=(value+(6*j+1)*factor*B[0]*B[1]*B[2])%q
        if j==P-1:break
        iv=pow(j+1,-1,q)
        B=[B[i]*(S[i]+P*tangent[i]-j)*iv%q for i in range(3)]
        factor=factor*minus_half%q
    return value


if __name__ == '__main__':
    _,A,_=source_jets(P**2)
    _,T,H=source_jets(P,True)
    assert T==[0,151,0],T
    assert A==[28696,10279,42622],A
    assert H==[[22,170,29],[170,4,71],[29,71,182]],H
    original=direct_weighted_source((0,0,0))
    assert original==P,original
    v=[-pow(3,-1,P),-pow(2,-1,P),-2*pow(3,-1,P)]
    for i,expected in ((0,176),(2,21)):
        assert A[i]%P==0
        q=(A[i]//P+sum(v[k]*H[k][i] for k in range(3))+H[i][i]*pow(2,-1,P))%P
        delta=tuple(int(k==i) for k in range(3))
        direct=(direct_weighted_source(delta)-original)%(P**3)
        assert q==expected,(i,q)
        assert direct==expected*P**2,(i,direct)
        print('outer_source',i+1,'Q_mod_p',q,'direct_difference_mod_p3',direct)
    print('PASS p=211 T=',T,'A=',A,'H=',H,'W_mod_p3=',original)
