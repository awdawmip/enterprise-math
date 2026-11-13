"""R54 integration: exact ranked-cut stream replaces sorting in finite S23 risk geometry."""
from fractions import Fraction
from bisect import bisect_right
from VERIFY_R54_PUBLISHED import order,bracket

A=262204504569236716045286;B=A+1;D=10**24
M=128;END=389

def compile_once(p,q,ranked):
    x=Fraction(p,q)
    hist=sorted(((z*p)%q,z) for z in range(M))
    hphase=[t for t,z in hist]
    risks=[]
    for n in range(M,END+1):
        if ranked:
            # R54 sorts 1..n-1 by decreasing ordinary fractional phase.
            right,(_,i,_,j),_=order(p,q,n-1,n-1)
            perm=[0]+right[::-1]
            assert len(set(perm))==n
            # Full-interval Farey certificate for frozen theta enclosure.
            a,i,c,j=bracket(A+B,2*D,n-1)[0]
            assert a*D<A*i and a*D<B*i and c*D>A*j and c*D>B*j
        else:
            perm=sorted(range(n),key=lambda s:(s*p)%q)
        grouped={z:[] for _,z in hist}
        for pos,t in enumerate(perm):
            nxt=perm[(pos+1)%n]
            z=hist[bisect_right(hphase,(t*p)%q)-1][1]
            coeff=(t*p//q-nxt*p//q+(pos==n-1),nxt-t)
            grouped[z].append(coeff)
        assert len(grouped)==M and all(grouped.values())
        maxima=[]
        for z,ls in grouped.items():
            maxima.append(max(ls,key=lambda v:v[0]*q+v[1]*p))
        risks.append((1-sum(a for a,b in maxima),-sum(b for a,b in maxima)))
    return risks

def run():
    for label,p,q in [('lower',A,D),('mid',A+B,2*D),('upper',B,D)]:
        by_rank=compile_once(p,q,True)
        independent=compile_once(p,q,False)
        assert by_rank==independent
        assert by_rank[0]==(0,0)
        assert by_rank[-1]==(-7551,28800)
        print('PASS_R54_RISK_PREFIX',label,'n',M,'..',END,'states',len(by_rank),'R_389',by_rank[-1])
    print('PASS_R54_RISK_PREFIX_TOTAL 786 matched exact affine risk states')
if __name__=='__main__':run()
