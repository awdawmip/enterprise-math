#!/usr/bin/env python3
"""Exact directed-Hausdorff center-set recourse via old-path max-plus frontier.
Frozen R5 derived observer, 954 events, radius 2; all effective cut masks,
K=214..221 and changed cuts 8,9. Python arbitrary-precision integers.
Run beside VERIFY_R5_LOW_BUDGET_UNIT_RECOURSE.py (existing PR #2427).
"""
import json,hashlib,random
from collections import defaultdict
from bisect import bisect_right
from VERIFY_R5_LOW_BUDGET_UNIT_RECOURSE import frozen,close,graph,paths_dp
PIN='435e77af0d180eac32bd1f9c4c464bc4010b7551'
BITS=(3,8,9,10,27)
NEG=-10**9

def optimizer(z):
    inc,out,pref,tail=graph(z)
    out2,C,D,J=paths_dp(z,221)
    assert out==out2
    return out,C,D,J

def language(dp,K):
    out,C,D,J=dp;best=J[K-1]
    levels=[{j for j in range(len(out)) if C[r][j]+D[K-1-r][j]==best} for r in range(K)]
    edges=[{i:tuple(j for j,w in out[i] if j in levels[r+1]
                    and C[r][i]+w==C[r+1][j]) for i in levels[r]}
           for r in range(K-1)]
    assert all(all(v for v in row.values()) for row in edges)
    return levels,edges,best

def insert_pareto(bucket,vec,path):
    # Minimize every old-optimizer score. Same new node implies identical suffix language.
    for a in bucket:
        if all(x<=y for x,y in zip(a,vec)):return
    for a in list(bucket):
        if all(x<=y for x,y in zip(vec,a)):del bucket[a]
    bucket[vec]=path

def exact_core(old,new,a,b,begin,end,keep_witness=True):
    OL,OE,_=old;NL,NE,_=new
    assert OL[a]==NL[a]=={begin} and OL[b]==NL[b]=={end}
    # Every edge in the optimizer languages increases the original event index.
    vertices=sorted((i,r) for r in range(a,b+1) for i in OL[r])
    ids={v:t for t,v in enumerate(vertices)}
    pos=[v[0] for v in vertices]
    preds=[[] for _ in vertices];last=[-1]*len(vertices)
    for r in range(a,b):
        for i in OL[r]:
            for j in OE[r][i]:
                p,q=ids[(i,r)],ids[(j,r+1)]
                assert i<j
                preds[q].append(p)
                last[p]=max(last[p],j)
    terminal=ids[(end,b)]
    last[terminal]=end
    def frontier(j):
        return tuple(t for t in range(bisect_right(pos,j))
                     if last[t]>j or (j==end and t==terminal))
    front={j:frontier(j) for r in range(a,b+1) for j in NL[r]}
    def advance(i,j,vec):
        mem=dict(zip(front[i],vec))
        for q in range(bisect_right(pos,i),bisect_right(pos,j)):
            v=max((mem.get(p,NEG) for p in preds[q]),default=NEG)
            mem[q]=v+(pos[q]==j and j!=end) if v!=NEG else NEG
        return tuple(mem.get(p,NEG) for p in front[j])
    assert len(front[begin])==1 and vertices[front[begin][0]]==(begin,a)
    state={begin:{(0,):()}}
    max_antichain=1; states_examined=0
    for r in range(a,b):
        nxt=defaultdict(dict)
        for i,values in state.items():
            for j in NE[r][i]:
                for vec,path in values.items():
                    v2=advance(i,j,vec)
                    insert_pareto(nxt[j],v2,path+((j,) if j!=end else ()))
                    states_examined+=1
        state=nxt
        max_antichain=max(max_antichain,sum(len(v) for v in state.values()))
    assert len(state)==1 and end in state and len(front[end])==1
    overlap=min(state[end]);assert len(overlap)==1 and overlap[0]>=0
    inner=b-a-1
    score=overlap[0]
    path=state[end][overlap] if keep_witness else ()
    if keep_witness:assert len(path)==inner
    return {'recourse':inner-score,'min_core_overlap':score,
            'core_witness':path,'max_nondominated_states':max_antichain,
            'state_transitions_examined':states_examined,
            'max_old_frontier_width':max(len(x) for x in front.values())}

def full_new_path(new,K,core,a,b,begin,end):
    NL,NE,_=new
    # All global optimum paths cross each common unique-rank anchor.
    prefix=[min(NL[0])]
    for r in range(a):prefix.append(min(NE[r][prefix[-1]]))
    assert prefix[-1]==begin
    suffix=[end]
    for r in range(b,K-1):suffix.append(min(NE[r][suffix[-1]]))
    S=prefix+list(core)+suffix
    assert len(S)==K and all(i<j for i,j in zip(S,S[1:]))
    return S

def independent_old_overlap(old,S):
    OL,OE,_=old
    chosen=set(S)
    v={i:int(i in chosen) for i in OL[0]}
    for r in range(len(OL)-1):
        new={j:-10**9 for j in OL[r+1]}
        for i in v:
            for j in OE[r][i]:new[j]=max(new[j],v[i]+int(j in chosen))
        v=new
    return max(v.values())

def direct_cost(z,S):
    ds=[min(abs(z[t]-z[j]) for j in S) for t in range(len(z))]
    return max(ds),sum(ds)

def random_toy_crosscheck(repetitions=200):
    rng=random.Random(202611150440)
    def paths(lang):
        L,E,_=lang
        s=[(i,) for i in L[0]]
        for r in range(len(E)):
            s=[p+(j,) for p in s for j in E[r][p[-1]]]
        return s
    for trial in range(repetitions):
        depth=rng.randrange(3,8);start=0;end=100
        canonical=[start]+[10*r for r in range(1,depth)]+[end]
        def make_lang():
            L=[{start}]
            for r in range(1,depth):
                vals={canonical[r]}
                for z in (canonical[r]-1,canonical[r]+1):
                    if rng.random()<0.7:vals.add(z)
                L.append(vals)
            L.append({end})
            E=[]
            for r in range(depth):
                row={}
                for i in L[r]:
                    choices=[j for j in L[r+1] if i<j and
                             (rng.random()<0.65 or (i==canonical[r] and j==canonical[r+1]))]
                    row[i]=tuple(sorted(choices))
                E.append(row)
            # Restrict to vertices/edges on at least one full path.
            reach=[{start}]
            for r in range(depth):reach.append({j for i in reach[-1] for j in E[r][i]})
            back=[None]*(depth+1);back[-1]={end}
            for r in range(depth-1,-1,-1):
                back[r]={i for i in L[r] if any(j in back[r+1] for j in E[r][i])}
            L=[reach[r]&back[r] for r in range(depth+1)]
            E=[{i:tuple(j for j in E[r][i] if j in L[r+1]) for i in L[r]}
               for r in range(depth)]
            return L,E,None
        old,new=make_lang(),make_lang()
        O,N=paths(old),paths(new)
        brute=max(min(len(set(s)-set(t)) for t in O) for s in N)
        dp=exact_core(old,new,0,depth,start,end,False)
        assert brute==dp['recourse'],(trial,brute,dp['recourse'])
    return repetitions

def main():
    x,cuts=frozen()
    toy=random_toy_crosscheck()
    z={}
    for mask in range(32):
        bits=sum((1<<bit) for p,bit in enumerate(BITS) if mask>>p&1)
        z[mask]=close(x,cuts,bits)
    dp={mask:optimizer(z[mask]) for mask in range(32)}
    all_rows=[];largest_frontier=0;largest_antichain=0;checks=0
    representative={}
    for K in range(214,222):
        langs={mask:language(dp[mask],K) for mask in range(32)}
        for bit in (8,9):
            flag=1<<BITS.index(bit)
            for newmask in range(32):
                if not newmask&flag:continue
                oldmask=newmask^flag
                old,new=langs[oldmask],langs[newmask]
                assert old[2]==new[2]==2134-5*K
                r=exact_core(old,new,3,K-85,16,536)
                S=full_new_path(new,K,r['core_witness'],3,K-85,16,536)
                assert direct_cost(z[newmask],S)==(2,new[2])
                assert independent_old_overlap(old,S)==K-r['recourse']
                rr={k:v for k,v in r.items() if k!='core_witness'}
                rr.update(K=K,cut=bit,old_effective_mask=oldmask,
                          new_effective_mask=newmask,
                          witness_sha256=hashlib.sha256(json.dumps(S,separators=(',',':')).encode()).hexdigest())
                all_rows.append(rr)
                key=(K,bit)
                if key not in representative or rr['recourse']>representative[key]['recourse']:
                    representative[key]={'recourse':rr['recourse'],'old_effective_mask':oldmask,
                                         'new_effective_mask':newmask,'full_witness_centers':S}
                largest_frontier=max(largest_frontier,rr['max_old_frontier_width'])
                largest_antichain=max(largest_antichain,rr['max_nondominated_states'])
                checks+=1
    summary=[]
    for K in range(214,222):
        for bit in (8,9):
            vals=[r['recourse'] for r in all_rows if r['K']==K and r['cut']==bit]
            summary.append({'K':K,'cut':bit,'min_over_backgrounds':min(vals),
                            'max_over_backgrounds':max(vals),
                            'histogram':{str(i):vals.count(i) for i in sorted(set(vals))}})
    assert checks==256
    print(json.dumps({'status':'PASS_EXACT_R5_OFFLINE_MAXMIN_RECOURSE',
                      'scientific_input_commit':PIN,'model':'derived 954-event 1D indexed-center radius-2',
                      'effective_cut_bits':BITS,'K_scope':[214,221],
                      'changed_cuts':[8,9],'all_background_checks':checks,
                      'toy_bruteforce_crosschecks':toy,
                      'greatest_old_frontier_width':largest_frontier,
                      'greatest_pareto_antichain':largest_antichain,
                      'results':summary,'representative_exact_witnesses':
                      {str(k[0])+'_'+str(k[1]):v for k,v in representative.items()},
                      'all_background_rows':all_rows,
                      'review':'AUTHOR_PROVED_EXACT_FINITE_CHECKED_NOT_REVIEWED'},
                     sort_keys=True,ensure_ascii=False,indent=2))
if __name__=='__main__':main()
