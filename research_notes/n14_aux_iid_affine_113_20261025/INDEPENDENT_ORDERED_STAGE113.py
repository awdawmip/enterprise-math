# Independent author-side exact checker for Stage113.
# Enumerates literal ordered histories using integer branch weights (not a
# count-state forward mass recursion), normalizing only at terminal events.
from fractions import Fraction as F
from collections import Counter
P=(F(1,8),F(1,24),F(5,6))
K=F(814106972531223,875100809116)
L=F(189992854025880,218775202279)
N=14;A=(10,3,0);C=(5,2,3)
alpha0=F(13084629132464364707,37682150988866125824)
V0=F(1930486644885404154985,150728603955464503296)
u0=F(66372737348901,70438400000000)
def ratio(n,a,b):return F(2**(a+b),3**a)

def policy():
    dp={};acts={};ties={};slacks=[]
    for n in range(N,-1,-1):
        for a in range(n+1):
            for b in range(n-a+1):
                s=n,a,b
                opts={'P':K*ratio(*s),'Q':L}
                if n<N:
                    opts['C']=1+P[0]*dp[n+1,a+1,b]+P[1]*dp[n+1,a,b+1]+P[2]*dp[n+1,a,b]
                best=min(opts.values())
                minimizers=tuple(t for t in opts if opts[t]==best)
                dp[s]=best;acts[s]=minimizers[0]
                if len(minimizers)>1:ties[s]=minimizers
                for t,v in opts.items():
                    if t!=minimizers[0]:slacks.append(v-best)
    assert len(dp)==680 and len(slacks)==1240
    assert sum(v>0 for v in slacks)==1238 and sum(v==0 for v in slacks)==2
    assert min(v for v in slacks if v>0)==F(3797211181,1312651213674)
    assert ties=={C:('Q','C'),A:('P','C')}
    return acts,dp[0,0,0]

def literal_DFS(acts,a_stop,c_stop):
    pscale=[24**(14-n) for n in range(15)]
    qscale=[12**(14-n) for n in range(15)]
    stack=[(0,0,0,1,1,0)]
    hits=Counter();massP=Counter();massQ=Counter()
    accum=dict(eP=0,eQ=0,tP=0,tQ=0)
    visited=0
    while stack:
        n,a,b,p,q,mask=stack.pop();visited+=1
        s=n,a,b
        if s==A:
            assert not(mask&2)
            hits['A']+=1;massP['A']+=p*pscale[n];massQ['A']+=q*qscale[n]
            mask|=1;tag='P' if a_stop else 'C'
        elif s==C:
            assert not(mask&1)
            hits['C']+=1;massP['C']+=p*pscale[n];massQ['C']+=q*qscale[n]
            mask|=2;tag='Q' if c_stop else 'C'
        else:tag=acts[s]
        if tag=='C':
            stack.append((n+1,a,b,p*20,q*10,mask))
            stack.append((n+1,a,b+1,p,q,mask))
            stack.append((n+1,a+1,b,p*3,q,mask))
        else:
            pw=p*pscale[n];qw=q*qscale[n]
            if tag=='Q':accum['eP']+=pw
            else:
                assert tag=='P'
                accum['eQ']+=qw
            accum['tP']+=n*pw;accum['tQ']+=n*qw
    ans={k:F(v,24**14 if k in ('eP','tP') else 12**14) for k,v in accum.items()}
    ans['hits']=dict(hits)
    ans['hitP']={k:F(v,24**14) for k,v in massP.items()}
    ans['hitQ']={k:F(v,12**14) for k,v in massQ.items()}
    ans['visited']=visited
    return ans

def main():
    acts,h=policy()
    x00=literal_DFS(acts,False,False)
    x10=literal_DFS(acts,True,False)
    x01=literal_DFS(acts,False,True)
    x11=literal_DFS(acts,True,True)
    fields=('eP','eQ','tP','tQ')
    du={x:x10[x]-x00[x] for x in fields}
    dw={x:x01[x]-x00[x] for x in fields}
    assert all(x11[x]-x10[x]-x01[x]+x00[x]==0 for x in fields)
    assert x00['hits']=={'A':120,'C':6}
    assert x00['hitP']=={'A':F(390625,5971968),'C':F(1,147456)}
    assert x00['hitQ']=={'A':F(390625,20155392),'C':F(1,41472)}
    slope=-(dw['eP']-dw['eQ'])/(du['eP']-du['eQ'])
    assert slope==F(123866061659,986137600000000)
    eta=F(218775202279,19538893105337991168)
    start={x:x00[x]+u0*du[x] for x in fields}
    end={x:x00[x]+(u0+slope)*du[x]+dw[x] for x in fields}
    assert (start['eP'],start['eQ'],start['tP'])==(alpha0,alpha0,V0)
    assert end['eP']==end['eQ']==alpha0+eta
    assert end['tP']==V0-(K+L)*eta
    assert h==V0+(K+L)*alpha0
    assert start['tP']>start['tQ'] and end['tP']>end['tQ']
    assert 0<u0<u0+slope<1
    assert [x['visited'] for x in (x00,x10,x01,x11)]==[889909,886309,884347,880747]
    print('INDEPENDENT_EXACT_ORDERED_PASS',end['eP'],end['tP'])
if __name__=='__main__':main()
