from fractions import Fraction as F
from itertools import product, permutations
Z, U = F(0), F(1)
L = (F(-1760,59), F(-1392,59), F(-400,59), F(328,59))

def O(p1,p2,q1,q2,qb,r,k1,k2,t):
    out = [Z,Z,Z,Z]
    def row(tm,ans,pm,qm):
        assert pm>=0 and qm>=0
        out[0] += pm if ans=='P' else Z
        out[1] += qm if ans=='Q' else Z
        out[2] += tm*pm
        out[3] += tm*qm
    for p,q,k in ((p1,q1,k1),(p2,q2,k2)):
        u=(1-p); v=(1-q)
        row(1,'P',p/8,p/8)
        row(2,'Q',u/16,3*u/32)
        row(2,'P',u*q/16,u*q/32)
        row(3,'P',u*v/40,u*v/64)
        row(3,'Q',3*u*v/80,u*v/64)
        # P-tail nature split routes fraction t to K=(3,8/5);
        # continuation at K moves the final P answer from t=3 to t=4.
        out[2] += t*(1-k)*u*v/40
        out[3] += t*(1-k)*u*v/64
    row(2,'P',qb/4,qb/8)
    row(3,'P',(1-qb)/4,(1-qb)/8)
    row(1,'Q',r/2,5*r/8)
    row(3,'P',(1-r)/2,5*(1-r)/8)
    return tuple(out)

def R(p,q,r,k,t): return O(p,p,q,q,q,r,k,k,t)
def minus(a,b): return tuple(x-y for x,y in zip(a,b))
def dot(a,b): return sum((x*y for x,y in zip(a,b)),Z)
def det(cols):
    a=[[cols[j][i] for j in range(4)] for i in range(4)]
    s=Z
    for perm in permutations(range(4)):
        inv=sum(perm[i]>perm[j] for i in range(4) for j in range(i+1,4))
        v=F(-1 if inv%2 else 1)
        for i in range(4):v*=a[i][perm[i]]
        s+=v
    return s
base=R(Z,Z,Z,U,Z)
def score(y): return dot(L,minus(y,base))

def main():
    # Every variable is degree <=1 along every path, so the identities
    # are multi-affine and all 32 Boolean corners prove all-real equality.
    for p,q,r,k,t in product((Z,U),repeat=5):
        old=R(p,q,r,U,Z)
        v=R(p,q,r,k,t)
        expected=tuple(old[i]+t*(1-k)*(1-p)*(1-q)*x for i,x in enumerate((Z,Z,F(1,20),F(1,32))))
        assert v==expected
        assert score(v)==p*q-F(39,236)*t*(1-p)*(1-q)*(1-k)
    b=minus(R(U,Z,Z,U,Z),base)
    c=minus(R(Z,U,Z,U,Z),base)
    d=tuple(x-y-z for x,y,z in zip(minus(R(U,U,Z,U,Z),base),b,c))
    e=minus(R(Z,Z,U,U,Z),base)
    assert det((b,c,d,e))==F(59,20480)
    w=O(Z,Z,U,Z,Z,U,U,U,F(1,4))
    assert w==(F(27,80),F(53,64),F(29,16),F(49,32))
    assert score(w)==-F(1,2) and sum(map(abs,L))==F(3880,59)
    checks=0
    for t in map(F,('1/8','1/4','1/2','7/8')):
        vals=[]
        for args in product((Z,U),repeat=4):
            vals.append(score(R(*args,t)));checks+=1
        assert min(vals)==-F(39,236)*t
        for args in product((Z,U),repeat=8):
            assert isinstance(O(*args,t)[0],F);checks+=1
        assert (min(vals)-score(w))/sum(map(abs,L))==(118-39*t)/15520
    print('keys=I(1,1);J(2,2);K(3,8/5); nature epsilon in (0,1)')
    print('multi_affine_corner_identities=32 PASS')
    print('LR_four_rank_determinant=59/20480')
    print('FULL_witness=',w,'score=',score(w))
    print('LR_exact_score_min=-(39/236)*epsilon')
    print('all_real_support_gap_lower=(118-39*epsilon)/236 >79/236')
    print('all_real_distance_lower=(118-39*epsilon)/15520 >79/15520')
    print('deterministic_exact_checks=',checks)
    print('PASS_EXACT_R5_THIRD_GENUINE_KEY_UNIFORM_NO_GO')
if __name__=='__main__':main()
