"""EC49CA: exact CRT native signed-X6 BRC, terminal DFA and co-reachability."""
import json
from pathlib import Path
from native_signed_brc import endpoint_weight, endpoint_multiplicity

S=tuple(range(1,7))+tuple(range(-1,-7,-1))
Z=(0,)*6
W=(2,3,3,2,1,1)
P=(101,103,107,109,113,127,131,137)
Q=tuple((u,v) for u in range(3) for v in range(3))
I={x:j for j,x in enumerate(Q)}

def sw(a):
    return (2 if a>0 else -2) if abs(a)==1 else ((1 if a>0 else -1) if abs(a)==2 else a)
def w(a):return W[a-1] if a>0 else 1
def dfa(q,a):return 2 if q==2 or (q==1 and a==2) else (1 if a==1 else 0)
def step(q,a):return I[(dfa(Q[q][0],a),dfa(Q[q][1],sw(a)))]
def atom(q):return '%d%d'%(Q[q][0]==2,Q[q][1]==2)

def dp(n,p=None,prune=True):
    layer={(Z,0):(1,1,1)};sizes=[1]
    for t in range(n):
        nxt={}
        for (x,q),v in layer.items():
            for a in S:
                y=list(x);k=abs(a)-1;y[k]+=1 if a>0 else -1
                if prune and sum(abs(z) for z in y)>n-t-1:continue
                key=(tuple(y),step(q,a));old=nxt.get(key,(0,0,0))
                u=(old[0]+v[0]*w(a),old[1]+v[1]*w(sw(a)),old[2]+v[2])
                nxt[key]=tuple(z%p for z in u) if p else u
        layer=nxt;sizes.append(len(layer))
    result={a:[0,0,0] for a in ('00','01','10','11')}
    for (x,q),v in layer.items():
        if x==Z:
            a=result[atom(q)]
            for i in range(3):a[i]=(a[i]+v[i])%p if p else a[i]+v[i]
    return result,sizes

def crt(residues,primes):
    x=0;m=1
    for r,p in zip(residues,primes):
        x+=m*(((r-x)*pow(m,-1,p))%p);m*=p
    return x

def words(n):
    """Direct literal word check; entirely independent of DFA transition DP."""
    pos=[0]*6;path=[];out={a:[0,0,0] for a in ('00','01','10','11')};count=0
    def rec(t,x,y):
        nonlocal count
        if t==n:
            if any(pos):return
            count+=1
            a=any(path[j:j+2]==[1,2] for j in range(n-1))
            b=any(path[j:j+2]==[2,1] for j in range(n-1))
            v=out['%d%d'%(a,b)];v[0]+=x;v[1]+=y;v[2]+=1
            return
        for s in S:
            k=abs(s)-1;inc=1 if s>0 else -1;pos[k]+=inc
            if sum(abs(z) for z in pos)<=n-t-1:
                path.append(s);rec(t+1,x*w(s),y*w(sw(s)));path.pop()
            pos[k]-=inc
    rec(0,1,1)
    return out,count

def main():
    cases=[]
    for n in (0,2,4,6,8):
        bound=int(endpoint_weight(n,Z,W,(1,)*6))
        count=endpoint_multiplicity(n,Z)
        pp=[];m=1
        for p in P:
            pp.append(p);m*=p
            if m>bound:break
        assert m>bound
        rr=[dp(n,p)[0] for p in pp]
        obs={a:[crt([r[a][i] for r in rr],pp) for i in range(3)] for a in ('00','01','10','11')}
        exact,pruned=dp(n)
        assert obs==exact
        assert [sum(v[i] for v in obs.values()) for i in range(3)]==[bound,bound,count]
        full=dp(n,prune=False)[1]
        if n<=6:
            literal,nwords=words(n)
            assert literal==obs and nwords==count
        else:nwords=None
        cases.append(dict(n=n,native_bound=bound,native_count=count,primes=pp,crt_product=m,
            atoms=obs,peak_pruned=max(pruned),peak_unpruned=max(full),
            literal_paths_checked=nwords))
    assert cases[2]['atoms']=={'00':[1488,1488,384],'01':[36,36,6],
        '10':[36,36,6],'11':[0,0,0]}
    assert cases[3]['atoms']=={'00':[139320,139320,18744],
        '01':[6480,6480,576],'10':[6480,6480,576],'11':[360,360,24]}
    assert cases[4]['atoms']=={'00':[16560120,16560120,1170120],
        '01':[1129320,1129320,53850],
        '10':[1129320,1129320,53850],'11':[102240,102240,3600]}
    return dict(schema='EC49CA_CRT_EXACT_AUDIT_V1',native_blob='300a96e3dc24bf6fff73743037a0347a8bc83176',cases=cases,
        scope='finite exact X6 return paths, H=(id,(1 2)), DFA detects ordered substrings (+E1,+E2),(+E2,+E1)')
if __name__=='__main__':
    result=main()
    (Path(__file__).parent/'EXACT_REPORT_EC49CA_MIN.json').write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
    print('EC49CA_MIN_PASS',[(v['n'],v['crt_product'],v['peak_pruned'],v['peak_unpruned']) for v in result['cases']])
