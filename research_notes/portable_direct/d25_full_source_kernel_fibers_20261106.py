"""D25 exact p-adic source-kernel fiber certificate, author-side only.

Run beside d25_outer_fiber_strata_20261106.py in research_notes/portable_direct.
Reuses its previously persisted integer jet recurrence; no native H0/B0.
"""
from collections import Counter
from d25_outer_fiber_strata_20261106 import jets, primes_to

def chart(p):
    M=p*p
    _,A,H=jets(p,M,True)
    t=[x%p for x in A]
    pivot=next(i for i in range(3) if t[i])
    other=[i for i in range(3) if i!=pivot]
    B=[]
    for i in other:
        v=[0,0,0]
        v[i]=1
        v[pivot]=-A[i]*pow(A[pivot],-1,M)%M
        assert sum(A[k]*v[k] for k in range(3))%M==0
        B.append(v)
    v0=[-pow(3,-1,p),-pow(2,-1,p),-2*pow(3,-1,p)]
    HB=[[sum(B[h][i]*H[i][j]*B[k][j] for i in range(3) for j in range(3))%p
         for k in range(2)] for h in range(2)]
    lin=[sum(v0[i]*H[i][j]*B[h][j] for i in range(3) for j in range(3))%p
         for h in range(2)]
    half=pow(2,-1,p)
    a,b,c=HB[0][0]*half%p,HB[0][1],HB[1][1]*half%p
    D=(b*b-4*a*c)%p
    chi=0 if D==0 else (1 if pow(D,(p-1)//2,p)==1 else -1)
    assert D!=0,(p,'degenerate binary Hessian: different count theorem')
    det=(4*a*c-b*b)%p
    cx=-(2*c*lin[0]-b*lin[1])*pow(det,-1,p)%p
    cy=-(2*a*lin[1]-b*lin[0])*pow(det,-1,p)%p
    tau=(a*cx*cx+b*cx*cy+c*cy*cy+lin[0]*cx+lin[1]*cy)%p
    return dict(p=p,A=A,pivot=pivot,B=B,abc=(a,b,c),linear=lin,
                discriminant=D,chi=chi,center=(cx,cy),tau=tau)

def Q(row,x,y):
    p=row['p'];a,b,c=row['abc'];l0,l1=row['linear']
    return (a*x*x+b*x*y+c*y*y+l0*x+l1*y)%p

def direct_sum(p,v):
    M=p**3
    s=((p-1)//3,(p-1)//2,2*(p-1)//3)
    B=[1,1,1];z=1;ans=0
    inv=[0]+[pow(i,-1,M) for i in range(1,p)]
    half=pow(-2,-1,M)
    for j in range(p):
        ans=(ans+(6*j+1)*z*B[0]*B[1]*B[2])%M
        if j==p-1: break
        for i in range(3):
            B[i]=B[i]*(s[i]+p*v[i]-j)*inv[j+1]%M
        z=z*half%M
    return ans

def input_at(row,x,y):
    p=row['p'];M=p*p;B=row['B']
    base=[-pow(3,-1,M),-pow(2,-1,M),-2*pow(3,-1,M)]
    delta=[(x*B[0][i]+y*B[1][i])%M for i in range(3)]
    return [(base[i]+delta[i])%M for i in range(3)],delta

def j1_source_diff(p,delta):
    s=((p-1)//3,(p-1)//2,2*(p-1)//3)
    return -pow(2,-1,p)*sum(s[(i+1)%3]*s[(i+2)%3]*delta[i] for i in range(3))%p

def main():
    for p in (13,19,211,373,1093,3511):
        r=chart(p);tau=r['tau']
        special=(2*p-1 if r['chi']==1 else 1)
        normal=(p-1 if r['chi']==1 else p+1)
        zero=special if tau==0 else normal
        print('P',p,'pivot',r['pivot'],'abc',r['abc'],'linear',r['linear'],
              'D',r['discriminant'],'chi',r['chi'],'center',r['center'],
              'tau',tau,'special_size',special,'other_size',normal,'zero_size',zero)
        if p<=373:
            hist=Counter(Q(r,x,y) for x in range(p) for y in range(p))
            assert hist[tau]==special
            assert all(hist[z]==normal for z in range(p) if z!=tau)
        c=r['abc'][2];l1=r['linear'][1]
        y=-l1*pow(c,-1,p)%p
        assert y and Q(r,0,y)==0
        base,_=input_at(r,0,0);nxt,delta=input_at(r,0,y)
        W0=direct_sum(p,base);W1=direct_sum(p,nxt)
        j1=j1_source_diff(p,delta)
        assert W1==W0 and j1!=0
        print('WITNESS',p,'x,y',(0,y),'delta',delta,'W0,W1',(W0,W1),
              'labelled_j1_change_over_p',j1)
        if p<=19:
            for x in range(p):
                for y in range(p):
                    inp,_=input_at(r,x,y)
                    assert (direct_sum(p,inp)-W0)%p**3==p*p*Q(r,x,y)
            print('EXHAUSTIVE_DIRECT',p,p*p,'PASS')
    ps=primes_to(5000)
    n_plus=n_minus=0
    for p in ps:
        row=chart(p)
        if row['chi']==1:n_plus+=1
        else:n_minus+=1
    assert len(ps)==330 and (n_plus,n_minus)==(177,153)
    print('SCAN',len(ps),'nondegenerate',n_plus,'split',n_minus,'nonsplit: PASS')

if __name__=='__main__':
    main()
