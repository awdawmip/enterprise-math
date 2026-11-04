"""Exact Fraction certificates for bypass BRC terminal information threshold."""
from fractions import Fraction as F
from itertools import product

def experiments(a,b,w):
    A=[(1-a,F(1,2)),(1+a,F(1,2))]
    B=[(1-b,w),(F(1),1-2*w),(1+b,w)]
    for E in (A,B):
        assert sum((p for r,p in E),F(0))==1
        assert sum((r*p for r,p in E),F(0))==1
        assert all(r>0 and p>0 for r,p in E)
    return A,B

def v(r,alpha,beta):return max(alpha*r,beta)
def D(E,alpha,beta):
    return sum((p*v(r,alpha,beta) for r,p in E),F(0))-v(F(1),alpha,beta)
def call_gap(E,t):
    return sum((p*max(r-t,F(0)) for r,p in E),F(0))-max(1-t,F(0))
def dot(n,x):return sum((a*b for a,b in zip(n,x)),F(0))

def observe_LR(A,B,t1,t2,term):
    out=[F(0),F(0),F(0),F(0)]
    histories=[(F(1,4),A,'A1'),(F(1,4),A,'A2'),(F(1,2),B,'B')]
    def stop(m,r,t,act):
        if act=='Q':out[0]+=m*r
        else:out[1]+=m
        out[2]+=m*r*t;out[3]+=m*t
    for m,E,s in histories:
        if s!='B' and t1!='C':
            stop(m,F(1),1,t1);continue
        if t2!='C':
            stop(m,F(1),2,t2);continue
        for r,p in E:stop(m*p,r,3,term[r])
    return tuple(out)

def support_LR(A,B,n):
    keys=sorted(set(r for r,p in A+B))
    vals=[]
    for s1,s2 in product(('P','Q','C'),repeat=2):
        for labels in product(('P','Q'),repeat=len(keys)):
            observation=observe_LR(A,B,s1,s2,dict(zip(keys,labels)))
            vals.append((dot(n,observation),observation,(s1,s2,labels)))
    assert len(vals)==9*2**len(keys)
    return max(vals,key=lambda x:x[0]),len(vals)

def support_FULL(A,B,n):
    alpha,beta,cp,cq=n
    def stop(m,r,t):
        return m*(max(alpha*r,beta)+t*(cp*r+cq))
    def terminal(m,E):
        return sum((p*stop(m,r,3) for r,p in E),F(0))
    A_time2=max(stop(F(1,4),F(1),2),terminal(F(1,4),A))
    A_time1=max(stop(F(1,4),F(1),1),A_time2)
    B_time2=max(stop(F(1,2),F(1),2),terminal(F(1,2),B))
    return 2*A_time1+B_time2

def witness_A_only(A,B,n):
    out=[F(0)]*4
    for r,p in A:
        m=F(1,2)*p
        if n[0]*r>=n[1]:out[0]+=m*r
        else:out[1]+=m
        out[2]+=3*m*r;out[3]+=3*m
    out[1]+=F(1,2)
    out[2]+=F(1);out[3]+=F(1)
    return tuple(out)

def run():
    a,b=F(1,2),F(3,4)
    print('PARAMS a,b',a,b)
    for w in (F(1,5),F(1,6),F(1,8)):
        A,B=experiments(a,b,w)
        threshold=a/(4*b)
        print('CASE w',w,'threshold',threshold,'regime',('EQUALITY' if w>=threshold else 'SEPARATED'))
        knots=sorted({F(0),F(1),F(2),1-b,1-a,1+a,1+b})
        differences=[D(A,F(1),t)-2*D(B,F(1),t) for t in knots]
        print('KNOTS',[(str(t),str(d)) for t,d in zip(knots,differences)])
        assert (max(differences)<=0)==(w>=threshold)
        for alpha,beta in product([F(-3),F(-1),F(0),F(1),F(2)],[F(-2),F(0),F(1,2),F(1),F(3)]):
            DA,DB=D(A,alpha,beta),D(B,alpha,beta)
            assert DA>=0 and DB>=0
            if w>=threshold:assert DA<=2*DB
        if w<threshold:
            DA,DB=D(A,F(1),F(1)),D(B,F(1),F(1))
            assert DA==a/2 and DB==w*b
            tau=(DA+2*DB)/4
            n=(F(1),F(1),-tau,F(0))
            W=witness_A_only(A,B,n)
            hfull=support_FULL(A,B,n)
            (hlr,L,policy),count=support_LR(A,B,n)
            gap=(DA-2*DB)/8
            assert count==288 and dot(n,W)==hfull
            assert hfull-hlr==gap>0
            d_inf_lower=gap/sum(map(abs,n))
            print('SEPARATOR',n,'FULL_W',W,'hFULL',hfull,'hLR',hlr,'GAP',gap,'DIST_INF_LOWER',d_inf_lower,'LR_COUNT',count)
        else:
            for f in [F(0),F(1,3),F(1),F(3,2),F(2),F(3)]:
                x,y=(F(0),f) if f<=1 else ((f-1)/2,F(1))
                z=x*y
                assert x+z+y==f
                for alpha,beta in product([F(-1),F(1),F(3)],[F(-2),F(1),F(2)]):
                    DA,DB=D(A,alpha,beta),D(B,alpha,beta)
                    canonical=v(F(1),alpha,beta)+(z*DA+y*DB)/2
                    ys={max(F(0),f-2),min(f,F(1))}
                    for yy in ys:
                        zz=(f-yy)/2
                        assert canonical>=v(F(1),alpha,beta)+(zz*DA+yy*DB)/2
            print('ALL_REAL_EQUALITY_BY_PIECEWISE_LINEAR_CALL_GAP_AND_FIXED_TIME_POLYGON')
    A,B=experiments(a,b,F(1,5))
    assert call_gap(A,F(1))==F(1,4)>call_gap(B,F(1))==F(3,20)
    assert call_gap(A,F(3,8))==0<call_gap(B,F(3,8))==F(1,40)
    print('CROSSING_CALL_GAPS at t=1:',call_gap(A,F(1)),call_gap(B,F(1)))
    print('CROSSING_CALL_GAPS at t=3/8:',call_gap(A,F(3,8)),call_gap(B,F(3,8)))
    print('PASS_EXACT_R5_BYPASS_CROSSING_INFORMATION_ORDERS_PHASE_THRESHOLD')
if __name__=='__main__':run()
