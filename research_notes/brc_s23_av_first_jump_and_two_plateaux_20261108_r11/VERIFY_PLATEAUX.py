#!/usr/bin/env python3
"""Exact S23/AV first jump and second plateau certificate from compressed gap classes."""
import csv,sys,math,hashlib
from fractions import Fraction as F
Q=10**26; LO=545569623581288298975349314; HI=LO+1
P,D=2074774,380295; A,B=79,431; W=510
N0=2455069; N1=4530352; H0=380805; H1=380806; H2=649492

def atanh(z,n=45):
    result=F(0);term=z
    for i in range(n): result+=2*term/(2*i+1);term*=z*z
    return result,result+2*term/((2*n+1)*(1-z*z))

def common():
    a,b=atanh(F(1,3));c,d=atanh(F(1,15));e,f=atanh(F(1,9))
    assert F(LO,Q)<(3*a-d)/(f+d)<(3*b-c)/(e+c)<F(HI,Q)
    assert math.gcd(P,D)==1 and P*A-D*B==1 and N0==P+D
    alpha_low=P*Q-HI*D;alpha_high=P*Q-LO*D
    assert 0<alpha_low<alpha_high and H2*alpha_high<Q and H2<N0
    # Exceptional gap t(D+1,0)..t(D+1+A,B).
    L,K=760669,4149979
    assert (L+A)*alpha_high<2*Q
    assert (D+A)*alpha_high<Q
    assert (2*D+A)*alpha_low>Q
    assert K*Q>HI*L and (K+B)*Q<LO*(L+A)
    assert K+L-(D+1)==N1
    print('PASS_RATIONAL_LOG_KEY_AND_EXACT_FIRST_ENTRY',alpha_low,alpha_high)

def cover(dv,dj,V,J,S,budget):
    for L in range(V,V+300000):
        K=max(LO*L//Q+1,J)
        if (K>=J and K+L<=budget+S and K*Q>HI*L
                and (K+dj)*Q<LO*(L+dv)):
            return K+L-S
    raise ValueError('no witness '+str((dv,dj,V,J,S,budget)))

def endpoint(path,target):
    with open(path,newline='') as f:rows=list(csv.reader(f))
    assert rows[0][0]=='SUMMARY' and len(rows[0])==4
    H,M,C=map(int,rows[0][1:]);assert H==target
    assert M==(H+1)*(H+2)//2 and C==len(rows)-1
    assert H*(P*Q-LO*D)<Q and H<N0
    budget=N0 if H<=H1 else N1
    total=0;seen=set();nonw_max=0;wcount=0;data=[]
    for fields in rows[1:]:
        assert fields[0]=='CLASS' and len(fields)==7
        dv,dj,V,J,S,num=map(int,fields[1:]);total+=num
        assert (dv,dj) not in seen and num>0 and 0<=V<=H and 0<=J<=H and 0<=S<=H
        seen.add((dv,dj));data.append(','.join(fields[1:]))
        assert (LO if dv>=0 else HI)*dv>Q*dj
        if (dv,dj)==(A,B):
            wcount=num
            assert (V,J,S)==(H-W,H-W,0)
        else:nonw_max=max(nonw_max,cover(dv,dj,V,J,S,budget))
    assert len(seen)==C and total==M-1
    assert wcount==(H-509)*(H-508)//2
    assert M-wcount==510*H-129285  # exact number of w-orbits
    # All w-cells have left v+j<=H-W. For v<=D use (K,L)=(P,D).
    # For v>D use (K,L)=(4149979,760669) at length <=N1.
    if H==H0:assert H-W<=D
    else:
        assert H-W<=760669
        assert 4149979>=H-W and 760669>=H-W
        assert 4149979+760669-(D+1)==N1
    left=H*Q//LO+1;right=HI*H//Q+1
    assert LO*left>H*Q and right*Q>HI*H
    assert max(left,right,nonw_max)<=budget
    digest=hashlib.sha256('\n'.join(data).encode()).hexdigest()
    print('PASS_ENDPOINT',H,'M',M,'CHAINS',510*H-129285,'CLASSES',C,
          'NONW_MAX',nonw_max,'EXT',left,right,'ROW_SHA256',digest)

def main():
    common()
    for file,h in zip(sys.argv[1:],[H0,H1,H2]):endpoint(file,h)
    assert len(sys.argv)==4
    print('THEOREM_PLATEAU_1',510,H0,N0)
    print('THEOREM_FIRST_JUMP',H1,N1)
    print('THEOREM_PLATEAU_2',H1,H2,N1)
    print('PASS_S23_AV_TWO_PLATEAUX_FIRST_JUMP_CERTIFIED')

if __name__=='__main__':main()
