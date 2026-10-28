"""Exact R5 rational cross-check. All-direction result is proved in PROOF.md."""
from fractions import Fraction as F
from itertools import product

P,Q,C="P","Q","C"

def tree(theta,d,a,b):
    theta,d,a,b=map(F,(theta,d,a,b))
    assert 0<theta<1 and 0<d<1 and 0<b<a<F(1,2)
    rows={}
    for root,sign,k in (("U",1,a),("V",-1,b)):
        ro=1+sign*d
        rows[root+"O"]=(F(1,2)*(1-theta)*ro,F(1,2)*(1-theta),2)
        for j,(r,z) in enumerate(zip((F(1,2),F(1),F(3,2)),(k,1-2*k,k))):
            qq=F(1,2)*theta*z
            rows[root+"C"+str(j)]=(qq*r,qq,3)
    assert len(rows)==8 and all(p>0 and q>0 for p,q,t in rows.values())
    assert sum((p for p,q,t in rows.values()),F(0))==1
    assert sum((q for p,q,t in rows.values()),F(0))==1
    return rows

def obs(rows,roots,cs,side,last):
    out=[F(0)]*4
    for i,root in enumerate(("U","V")):
        rr=[k for k in rows if k.startswith(root)]
        mp=sum((rows[k][0] for k in rr),F(0))
        mq=sum((rows[k][1] for k in rr),F(0))
        if roots[i]!=C:
            if roots[i]==Q:out[0]+=mp
            else:out[1]+=mq
            out[2]+=mp;out[3]+=mq
            continue
        po,qo,_=rows[root+"O"]
        if side[i]==Q:out[0]+=po
        else:out[1]+=qo
        out[2]+=2*po;out[3]+=2*qo
        ck=[root+"C"+str(j) for j in range(3)]
        pc=sum((rows[k][0] for k in ck),F(0))
        qc=sum((rows[k][1] for k in ck),F(0))
        if cs[i]!=C:
            if cs[i]==Q:out[0]+=pc
            else:out[1]+=qc
            out[2]+=2*pc;out[3]+=2*qc
        else:
            for j,key in enumerate(ck):
                p,q,_=rows[key]
                if last[3*i+j]==Q:out[0]+=p
                else:out[1]+=q
                out[2]+=3*p;out[3]+=3*q
    return tuple(out)

def score(o,L):
    return sum((x*y for x,y in zip(o,L)),F(0))

def enum(rows,L,lr):
    best=None;bestobs=None;unique=set();count=0
    for roots in product((P,Q,C),repeat=2):
        csoptions=((x,x) for x in (P,Q,C)) if lr else product((P,Q,C),repeat=2)
        for cs in csoptions:
            for side in product((P,Q),repeat=2):
                for bits in product((P,Q),repeat=(3 if lr else 6)):
                    last=bits*2 if lr else bits
                    o=obs(rows,roots,cs,side,last)
                    unique.add(o);count+=1
                    s=score(o,L)
                    if best is None or s<best:best=s;bestobs=o
    return best,bestobs,count,len(unique)

def bellman(theta,d,a,b,L):
    alpha,beta,gamma,delta=map(F,L)
    f=lambda r:min(alpha*r,beta)
    c=lambda r:gamma*r+delta
    D=2*f(1)-f(F(1,2))-f(F(3,2))
    S=[];B=[];g=[]
    for sign,k in ((1,a),(-1,b)):
        r=1+sign*(1-theta)*d;ro=1+sign*d
        S.append((f(r)+c(r))/2)
        B.append((2*c(r)+theta*f(1)+(1-theta)*f(ro))/2)
        g.append(k*D)
    full=sum((min(S[i],B[i]-theta*max(g[i]-c(1),F(0))/2) for i in range(2)),F(0))
    lr=min(sum((min(S[i],B[i]-theta*y*(g[i]-c(1))/2) for i in range(2)),F(0)) for y in (0,1))
    return full,lr

def main():
    theta,a,b=F(3,4),F(1,4),F(1,8)
    H=(2+theta)*b-theta*a
    dcrit=H/(2*(1-theta)*(theta+H))
    assert H==F(5,32) and dcrit==F(10,29)
    print("theta=3/4, a=1/4, b=1/8, H=",H,"d_critical=",dcrit)
    Ls=[tuple(map(F,x)) for x in ((400,440,220,-199),(1,1,0,0),(-3,5,7,-2),(12,19,-7,8),(20,23,10,-9),(7,-11,-9,17))]
    for d in (F(1,10),dcrit,F(2,5)):
        rows=tree(theta,d,a,b)
        print("d=",d,"leaf count=",len(rows),"P/Q exact normalized")
        for L in Ls:
            ff,fo,nf,uf=enum(rows,L,False)
            ll,lo,nl,ul=enum(rows,L,True)
            x,y=bellman(theta,d,a,b,L)
            assert (ff,ll)==(x,y) and (nf,nl)==(20736,864)
            if d<=dcrit:assert ff==ll
            if L==Ls[0]:
                print("  signed lambda=",L,"full=",ff,"compressed=",ll,"gap=",ll-ff,"distinct full/LR=",uf,ul)
            if d==F(2,5) and L==Ls[0]:
                O=(F(219,320),F(7,32),F(19,8),F(19,8))
                assert (ff,ll,ll-ff)==(F(3359,8),F(1681,4),F(3,8)) and score(O,L)==ff
                print("  exact witness O*=",O,"score=",score(O,L))
    print("ALL EXACT PHASE-GATE CHECKS PASSED")

if __name__=="__main__":main()
