#!/usr/bin/env python3
"""EC49EL: exact seam-event quotient, fiber counts and q=0 cost theorem.

Python standard library only. The finite-state dynamic program counts all words via
six grammar letters without constructing exponential lists of ordered paths.
The path simulator below is independent of the quotient and checks all h<=6.
"""
from collections import defaultdict, Counter
from itertools import product
from math import factorial
import json

OP = {'a':(-1,-1), 'b':(-2,-2), 'c':(1,2,-1,-2),
      'd':(2,1,-2,-1), 'e':(3,1,1,-3), 'f':(1,-1), 'g':(2,-2)}
ATOMS = (('N',0),('N',1),('N',2),('A',0),('A',2),('B',0),('B',1),('AB',0),('BA',0))
BUCKETS = ('N','A','B','AB','BA')
BIDX = {s:i for i,s in enumerate(BUCKETS)}
TAGS = {'a':0,'e':0,'c':1,'f':1,'d':2,'g':2} # neutral, starts +E1, starts +E2


def step_event(s, ev):
    if ev == 'A': return {'N':'A','B':'BA'}.get(s,s)
    if ev == 'B': return {'N':'B','A':'AB'}.get(s,s)
    raise ValueError(ev)


def reduce_internal(state, op):
    if op == 'c': return step_event(state,'A')
    if op == 'd': return step_event(state,'B')
    return state


def quotient_transfer(tag, events):
    internal = {'N':'','A':'A','B':'B','AB':'AB','BA':'BA'}[events]
    out=[]
    for s,last in ATOMS:
        if tag==1 and last==2: s=step_event(s,'B')
        if tag==2 and last==1: s=step_event(s,'A')
        for ev in internal:s=step_event(s,ev)
        out.append(BIDX[s])
    return tuple(out)


def direct_transfer(word):
    s_last=list(ATOMS)
    for op in word:
        for v in OP[op]:
            new=[]
            for s,last in s_last:
                if last==1 and v==2:s=step_event(s,'A')
                elif last==2 and v==1:s=step_event(s,'B')
                new.append((s,v))
            s_last=new
    return tuple(BIDX[s] for s,_ in s_last)


def qstate(word):
    tag=0; events='N'
    for i,op in enumerate(word):
        if i==0:tag=TAGS[op]
        events=reduce_internal(events,op)
    return tag,events


def pos(word):
    native=tuple(x for ch in word for x in OP[ch])
    return (native.count(1),native.count(2),native.count(3),0,0,0)


def direct_return_words(h):
    for chars in product('acdefg',repeat=h):
        if chars.count('e')==chars.count('a')+1:yield ''.join(chars)


def modrank(vectors, prime=1000003):
    pivot={}
    for bits in vectors:
        row=[(bits>>i)&1 for i in range(9)]
        for i in range(9):
            if not row[i]:continue
            if i in pivot:
                t=row[i]; p=pivot[i]
                for k in range(i,9):row[k]=(row[k]-t*p[k])%prime
            else:
                t=pow(row[i],-1,prime)
                pivot[i]=[(x*t)%prime for x in row]
                break
    return len(pivot)


def rank_transfers(transfers):
    return modrank([sum(1<<i for i,v in enumerate(t) if v==b)
                    for t in transfers for b in range(5)])


def DP(h):
    # (a,e,c+d,f,g,initial_tag,internal_AB_state) -> exact word multiplicity.
    d={(0,0,0,0,0,0,'N'):1}
    for i in range(h):
        out=defaultdict(int)
        for (a,e,q,f,g,tag,ev),count in d.items():
            for op in 'acdefg':
                na=a+(op=='a');ne=e+(op=='e')
                nq=q+(op in 'cd');nf=f+(op=='f');ng=g+(op=='g')
                nt=TAGS[op] if i==0 else tag
                nev=reduce_internal(ev,op)
                out[(na,ne,nq,nf,ng,nt,nev)]+=count
        d=out
    ptypes=defaultdict(lambda:defaultdict(int))
    for (a,e,q,f,g,tag,ev),count in d.items():
        if e!=a+1:continue
        p=(2*e+q+f,q+g,e,0,0,0)
        ptypes[p][quotient_transfer(tag,ev)]+=count
    return ptypes, len(d)


def factorial_formula(h,p):
    p1,p2,p3,p4,p5,p6=p
    if (p4,p5,p6)!=(0,0,0):return 0
    r=p3-1; q=p1+p2-h-1
    u=h-p2-2*r-1;v=h+1-p1
    if min(r,q,u,v)<0:return 0
    if 2*r+1+q+u+v!=h:return 0
    return factorial(h)*2**q // (factorial(r)*factorial(r+1)*factorial(q)*factorial(u)*factorial(v))


def det(A):
    a=[row[:] for row in A];n=len(a);s=1;last=1
    for k in range(n-1):
        if a[k][k]==0:
            for i in range(k+1,n):
                if a[i][k]!=0:
                    a[k],a[i]=a[i],a[k];s=-s;break
            else:return 0
        piv=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                num=a[i][j]*piv-a[i][k]*a[k][j]
                assert num%last==0
                a[i][j]=num//last
        for i in range(k+1,n):a[i][k]=0
        last=piv
    return s*a[-1][-1]


def general_q_positive_minor():
    # Any fiber with at least one c/d and one e admits these four types.
    choices=((1,'A'),(2,'B'),(0,'A'),(0,'B'))
    transfers=[quotient_transfer(*pair) for pair in choices]
    assert rank_transfers(transfers)==9
    cols=[[int(t[i]==b) for i in range(9)] for t in transfers for b in range(5)]
    selected=[]
    for j in range(len(cols)):
        candidate=selected+[j]
        bits=[sum(cols[k][i]<<i for i in range(9)) for k in candidate]
        if modrank(bits)>len(selected):selected=candidate
        if len(selected)==9:break
    assert len(selected)==9
    D=det([[cols[j][i] for j in selected] for i in range(9)])
    assert abs(D)==1
    return {'pairs':[list(x) for x in choices], 'column_indices':selected,'det':D}


def witness_minor():
    t1=quotient_transfer(1,'N'); t2=quotient_transfer(2,'N')
    cols=[[int(t[i]==b) for i in range(9)] for t in (t1,t2) for b in range(5)]
    ans=[]
    for omit in range(10):
        keep=[j for j in range(10) if j!=omit]
        D=det([[cols[j][i] for j in keep] for i in range(9)])
        if D:ans.append({'omit_column':omit,'column_names':[('f_tag' if j<5 else 'g_tag')+'_'+BUCKETS[j%5] for j in keep],'det':D})
    assert ans and rank_transfers((t1,t2))==9
    return ans[0]


def verify(max_h=9,prior7=None,prior8=None):
    # Full primitive-signed path agreement on a separate, exhaustive finite range.
    direct_cases=0
    for h in range(1,7):
        seen=defaultdict(lambda:defaultdict(int))
        for w in direct_return_words(h):
            direct_cases+=1
            assert direct_transfer(w)==quotient_transfer(*qstate(w)), w
            seen[pos(w)][direct_transfer(w)]+=1
        reconstructed,_=DP(h)
        assert {p:dict(v) for p,v in seen.items()}=={p:dict(v) for p,v in reconstructed.items()}
    cert=[];rank_match=[]
    for h in range(1,max_h+1):
        ptypes,dp_states=DP(h)
        nr=sum(sum(g.values()) for g in ptypes.values())
        count_formula=sum(factorial(h)*4**(h-2*r-1)//(factorial(r)*factorial(r+1)*factorial(h-2*r-1))
                           for r in range((h-1)//2+1))
        assert nr==count_formula
        assert all(sum(g.values())==factorial_formula(h,p) for p,g in ptypes.items())
        n_fibers=sum((h-2*r)*(h-2*r+1)//2 for r in range((h-1)//2+1))
        assert n_fibers==len(ptypes)
        fullrank=sum(rank_transfers(g)==9 for g in ptypes.values())
        q0_count=0;q0_fullrank=0
        for p,g in ptypes.items():
            r=p[2]-1; q=p[0]+p[1]-h-1
            if q==0:
                q0_count+=1
                u=h-p[1]-2*r-1;v=h+1-p[0]
                predicted=(u>=1 and v>=1)
                assert (rank_transfers(g)==9)==predicted,(h,p)
                q0_fullrank+=predicted
            else:
                assert rank_transfers(g)==9, ('q_positive_rank',h,p)
        assert fullrank==len(ptypes)-h, ('exact_bad_fiber_count',h,fullrank,len(ptypes))
        expected_q0=sum(max(0,h-2*r) for r in range((h-1)//2+1))
        expected_q0_full=sum(max(0,h-2*r-2) for r in range((h-1)//2+1))
        assert q0_count==expected_q0 and q0_fullrank==expected_q0_full
        cert.append({'h':h,'return_words':nr,'positive_count_fibers':len(ptypes),
                     'full_rank_fibers':fullrank,'q0_fibers':q0_count,'q0_full_rank':q0_fullrank,'dp_states_after_h':dp_states})
        if h in (7,8) and (prior7 if h==7 else prior8):
            with open(prior7 if h==7 else prior8,encoding='utf-8') as f:record=json.load(f)['h'+str(h)]
            old={(tuple(x['p'])):(x['words'],x['types'],x.get('rank_max',9) if x['min_added'] is None else 9)
                 for x in record['per_fiber_exact_minima']}
            fresh={p:(sum(g.values()),len(g),rank_transfers(g)) for p,g in ptypes.items()}
            assert old==fresh, ('prior-comparison',h,[(k,old.get(k),v) for k,v in fresh.items() if old.get(k)!=v][:3])
            rank_match.append({'h':h,'all_fibers_match_prior_github_artifact':True})
    # Exact q=0 cost proof also checked against published H=7/H=8 per-fiber DP when available.
    q0_cost_verified=[]
    for h,path in ((7,prior7),(8,prior8)):
        if not path:continue
        with open(path,encoding='utf-8') as f:rows=json.load(f)['h'+str(h)]['per_fiber_exact_minima']
        test=[v for v in rows if v['p'][0]+v['p'][1]==h+1 and v['min_added'] is not None]
        for v in test:
            r=v['p'][2]-1
            assert v['min_added']==4*h+4*r+2, (h,v)
        q0_cost_verified.append({'h':h,'checked_q0_fullrank_fibers':len(test)})
    m=witness_minor()
    qminor=general_q_positive_minor()
    for h in range(3,max_h+1):
        fs='feg'+'f'*(h-3);gs='gef'+'f'*(h-3)
        assert len(fs)==h and len(gs)==h
        assert pos(fs)==pos(gs)
        assert quotient_transfer(*qstate(fs))==quotient_transfer(1,'N')
        assert quotient_transfer(*qstate(gs))==quotient_transfer(2,'N')
    return {'status':'PASS','new_unit':'EC49EL','max_h':max_h,
      'model':'signed-native X6, ordered A/B first-occurrence, two symbolic positive BRC monomials',
      'analytic_results':{'all_h_word_count_formula':'sum_{r=0..floor((h-1)/2)} h! 4^(h-2r-1)/(r!(r+1)!(h-2r-1)!)',
        'fiber_word_count_formula':'h! 2^q/(r!(r+1)!q!u!v!) where r=p3-1, q=p1+p2-h-1, u=h-p2-2r-1, v=h+1-p1',
        'q0_rank9_condition':'u>=1 AND v>=1',
        'all_h_rank9_condition':'q>=1 OR (q=0 AND u>=1 AND v>=1)',
        'all_h_rank9_fiber_count':'number_of_positive_fibers - h',
        'q0_min_extra_edges_relative_to_mandatory_h2':'4h+4r+2 for h>=3, r=p3-1, q=0 and u,v>=1',
        'universal_unrestricted_cost_at_H9':'OPEN; constructive upper bound 66'},
      'witness_minor':m,'q_positive_unimodular_minor':qminor,'direct_path_words_checked_h1_to6':direct_cases,
      'finite_state_horizon_results':cert,'prior_full_fiber_matches':rank_match,
      'prior_q0_min_cost_matches':q0_cost_verified}

if __name__=='__main__':
    import sys
    max_h=int(sys.argv[1]) if len(sys.argv)>1 else 9
    prior7=sys.argv[2] if len(sys.argv)>2 and sys.argv[2]!='-' else None
    prior8=sys.argv[3] if len(sys.argv)>3 and sys.argv[3]!='-' else None
    print(json.dumps(verify(max_h,prior7,prior8),ensure_ascii=False,sort_keys=True,indent=2))