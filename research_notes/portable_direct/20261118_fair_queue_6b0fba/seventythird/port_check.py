"""Restricted public comparison automata. Python 3.10+, standard library."""
from collections import Counter, deque
from itertools import combinations, product
from pathlib import Path
import importlib.util
import json
from math import gcd


def load(relative):
    path = Path(__file__).resolve().parents[1] / relative
    spec = importlib.util.spec_from_file_location(path.stem, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


cyc = load('thirtyninth/cycle_check.py')
pair = load('thirtythird/pairing_check.py')
perms = pair.states(3)
a, b = (1, 0, 2), (0, 2, 1)
def sensor(pi):
    return (pair.mask(pi) & ((1<<5) + (1<<7))).bit_count() % 2


def factors(N):
    p = 2
    while p*p<=N:
        if N%p == 0:
            u=1
            while N%p==0:
                u*=p;N//=p
            yield p,u
        p+=1
    if N>1:yield N,N


def number_key(N,m,x,h):
    keys=[]
    for p,Q in factors(N):
        M=gcd(m,Q);g=gcd(x,M)
        if h%g:return None
        step=M//g; den=Q//M
        if step>1:
            n0=(-h//g * pow(x//g,-1,step))%step
        else:
            n0=0
        keys.append((step,n0,(x//g)%den,((h+n0*x)//M)%den))
    return tuple(keys)


def count_classes(N,m):
    live=1
    for p,Q in factors(N):
        M=gcd(Q,m)
        if M==Q:live*=(p*Q-1)//(p-1)
        else:live*=Q*Q//M
    return live+int(m>1)


def palette(rows):
    colors={}
    return [colors.setdefault(z,len(colors)) for z in rows]


def refine(obs,go):
    partition=palette(obs);layers=[partition]
    while True:
        nxt=palette((partition[i],partition[l],partition[r]) for i,(l,r) in enumerate(go))
        if max(nxt)==max(partition):
            return layers
        layers.append(nxt);partition=nxt


def minimal_word(i,j,layers,go):
    if layers[-1][i]==layers[-1][j]:return None
    d=next(k for k,row in enumerate(layers) if row[i]!=row[j])
    word=''
    while d:
        for k,letter in enumerate('UB'):
            x,y=go[i][k],go[j][k]
            if layers[d-1][x]!=layers[d-1][y]:
                word+=letter;i,j=x,y;break
        else:raise AssertionError('missing predecessor')
        d-=1
    return word


def distance(N,m,left,right,cost):
    x,h=left;y,z=right
    if (h==0)!=(z==0):return 0
    best=None
    for v in range(1,N+1):
        hv=h+v*x;zv=z+v*y
        if (hv-zv)%N==0:continue
        for t in (hv,zv):
            if t%m:continue
            k=(-t//m)%(N//m)
            length=v+cost*((k+v-1)//v)
            if best is None or length<best:best=length
    return best


def run(N,m):
    states=list(product(range(N),range(N),perms));idx={state:i for i,state in enumerate(states)}
    def succ(x,h,pi,k):
        return (idx[((x+k)%N,h,pair.compose(a,pi) if k%2 else pi)],
                idx[(x,(h+x)%N,pair.compose(b,pi))])
    micro=[succ(*s,1) for s in states]
    obs=[(h==0,sensor(pi)) for x,h,pi in states]
    go=[succ(*s,m) for s in states]
    reached={0}; queue=deque([0])
    while queue:
        for v in micro[queue.popleft()]:
            if v not in reached:reached.add(v);queue.append(v)
    assert len(reached)==len(states)
    layers=refine(obs,go)
    keys=[(number_key(N,m,x,h),
           pi if m%2 else (sensor(pi),sensor(pair.compose(b,pi)))) for x,h,pi in states]
    assert len(set(zip(layers[-1],keys)))==len(set(keys))==1+max(layers[-1])
    assert len(set(keys))==count_classes(N,m)*(6 if m%2 else 3)
    busy=None
    if N<=9:
        raw=len(states);colors=[];moves=[]
        for phase in range(m):
            for i,(left,right) in enumerate(micro):
                colors.append((phase,obs[i]) if phase==0 else (phase,None))
                dest=(phase+1)%m
                moves.append((dest*raw+left,right if phase==0 else phase*raw+i))
        full=refine(colors,moves)
        assert len(set(full[-1]))==m*len(set(keys))
        all_pair_probes=[(phase,obs[i] if phase==0 else sensor(states[i][2]))
                         for phase in range(m) for i in range(raw)]
        refined=refine(all_pair_probes,moves)
        assert 1+max(refined[-1])==m*6*count_classes(N,m)
        busy={'states':len(colors),'observable_classes':len(set(full[-1])),
              'classes_when_pair_probe_is_allowed_while_busy':1+max(refined[-1]),
              'greatest_minimum_accepted_or_rejected_prefix_steps':len(full)-1}
    sizes=[len(set(v)) for v in layers]
    # A maximal-depth witness is recovered from the first split at this depth.
    deep={}
    if len(layers)>1:
        first={}
        for i,old in enumerate(layers[-2]):
            j=first.setdefault(old,i)
            if layers[-1][i]!=layers[-1][j]:
                w=minimal_word(i,j,layers,go)
                x,y=i,j
                for c in w:x,y=go[x]['UB'.index(c)],go[y]['UB'.index(c)]
                assert obs[x]!=obs[y] and len(w)==len(layers)-1
                deep={'states':[states[i],states[j]],'word':w,'terminal_obs':[obs[x],obs[y]]};break
    return {'N':N,'m':m,'common_word_prepared_raw_states':len(reached),
            'arithmetic_classes':count_classes(N,m),'joint_partition_sizes':sizes,
            'greatest_minimum_macro_length':len(layers)-1,'attaining_pair_and_word':deep,'micro':busy}


def distance_tests(N,m):
    ss=list(product(range(N),repeat=2))
    # Reverse BFS in the pair graph, compressing a run of m A letters only for the unit-cost test.
    def dist(cost):
        from heapq import heappush,heappop
        data={};heap=[]
        for i,x in enumerate(ss):
            for y in ss[i+1:]:
                if (x[1]==0)!=(y[1]==0):
                    data[x,y]=0;heappush(heap,(0,x,y))
        while heap:
            d,x,y=heappop(heap)
            if data[x,y]!=d:continue
            l=lambda t:((t[0]-m)%N,t[1])
            r=lambda t:(t[0],(t[1]-t[0])%N)
            for step,back in ((cost,l),(1,r)):
                i,j=sorted((back(x),back(y)))
                if d+step<data.get((i,j),float('inf')):
                    data[i,j]=d+step;heappush(heap,(d+step,i,j))
        return data
    out=[]
    for cost in sorted({1,m}):
        comp=dist(cost)
        for x,y in combinations(ss,2):assert comp.get((x,y))==distance(N,m,x,y,cost)
        out.append(dict(U_cost=cost,pair_count=len(ss)*(len(ss)-1)//2,
                        distinct_pairs=len(comp),maximum=max(comp.values())))
    return {'N':N,'m':m,'costs':out}


def source_receipts():
    i=perms[0];n=edges=0
    for size in range(8):
        for ww in product('AB',repeat=size):
            w=''.join(ww);x=h=0;pi=i
            for c in w:
                if c=='A':x=(x+1)%6;pi=pair.compose(a,pi)
                else:h=(h+x)%6;pi=pair.compose(b,pi)
            (ac,bc,e),steps=cyc.replay(w,6,True)
            assert (x,h)==(ac%6,e) and bc==w.count('B') and len(steps)==2*len(w)
            n+=1;edges+=len(steps)
    initial=[i,b]
    zero=[[sensor(z),sensor(pair.compose(b,z))] for z in initial]
    mid=[sensor(pair.compose(a,z)) for z in initial]
    assert zero==[[0,0],[0,0]] and mid==[0,1]
    return {'unrestricted_source_words':n,'individual_source_edge_transitions':edges,
            'rejected_example':{'N':4,'m':2,'attempt':'AB','accepted':'A',
            'phase_after':1,'B_status':'refused with all coordinates unchanged'},
            'boundary_pair':initial,'boundary_codes':zero,'optional_first_A_probe':mid}


if __name__=='__main__':
    cases=[(4,2),(8,2),(8,4),(9,3),(16,4),(25,5),(27,9),(6,2),(6,3),(12,4),
           (12,6),(18,6),(4,1),(4,4),(12,12)]
    report={'source_receipts':source_receipts(),'cases':[run(N,m) for N,m in cases],
            'all_pair_distances':[distance_tests(N,m) for N,m in [(4,2),(6,2),(6,3),(8,4),(9,3)]]}
    print(json.dumps(report,indent=2))
