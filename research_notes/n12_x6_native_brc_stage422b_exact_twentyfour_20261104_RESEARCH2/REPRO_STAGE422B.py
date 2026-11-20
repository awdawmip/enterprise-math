#!/usr/bin/env python3
"""Stage422-B exact integer witness for the two-source 3-POP / 2-CANCEL quotient.
Universal assertions are proved in PROOF_STAGE422B.md; code checks finite instances/traces.
"""
from collections import Counter, defaultdict
from itertools import product
import json
A, B = 1, -1
D = tuple(range(1,7)) + tuple(range(-1,-7,-1))

def fiber(n):
    for r in range(2,n-2):
        for s in range(r+2,n):
            for i in (r,s):
                p = (A,)*(i-1)+(B,)+(A,)*(n-i)
                q = (A,)*(r-1)+(B,)+(A,)*(s-r-1)+(B,)+(A,)*(n-s)
                yield (r,s,i,p,q)

def observation(p,q):
    def one(w):
        z = tuple(w.count(i)-w.count(-i) for i in range(1,7))
        j = tuple(sorted(Counter(zip(w,w[1:])).items()))
        return len(w),z,j
    return one(p),one(q),sum(x==y for x,y in zip(p,q))

def cls(n,h):
    r,s,i,p,q=h
    if s==n-5: return ('B_cap',)
    if i<=n-3: return ('protected_P_run',p[-6:],q[-6:])
    # Here i=s is n-2 or n-1; P is fixed by its unique-B position.
    return ('fixed_P_Q_7',i,q[-7:])

def execute(h,trace):
    p,q=list(h[3]),list(h[4]); np,nc=3,2
    history=[]
    for op in trace:
        if op[0]=='POP':
            if np==0 or not q:
                history.append(('DENIED','POP')); break
            np-=1;q.pop()
        elif op[0]=='CANCEL':
            if nc==0 or min(len(p),len(q))<2 or p[-1]!=-p[-2] or q[-1]!=-q[-2]:
                history.append(('DENIED','CANCEL'));break
            nc-=1;del p[-2:];del q[-2:]
        else:
            p.append(op[1]);q.append(op[2])
        history.append(observation(p,q))
    return tuple(history)

def trace_words(max_apps, app_domain, max_depth):
    apps=tuple(('APP',x,y) for x in app_domain for y in app_domain)
    def rec(trace,np,nc,na):
        if trace: yield trace
        if len(trace)>=max_depth: return
        if np<3: yield from rec(trace+(('POP',),),np+1,nc,na)
        if nc<2: yield from rec(trace+(('CANCEL',),),np,nc+1,na)
        if na<max_apps:
            for app in apps:
                yield from rec(trace+(app,),np,nc,na+1)
    yield from rec((),0,0,0)

def verify():
    by_n={}; total_hist=0
    for n in range(11,41):
        histories=list(fiber(n)); total_hist+=len(histories)
        classes=defaultdict(list)
        for h in histories: classes[cls(n,h)].append(h)
        baseline=observation(histories[0][3],histories[0][4])
        assert all(observation(h[3],h[4])==baseline for h in histories)
        assert len(classes)==24,(n,len(classes))
        assert len([h for h in histories if h[1]==n-5])==2*(n-8)
        assert len([h for h in histories if h[1]<=n-6])==(n-8)*(n-9)
        by_n[n]={'history_count':len(histories),
                 'safe_7_8_key_count':len({(h[3][-7:],h[4][-8:]) for h in histories}),
                 'new_sufficient_classes':len(classes),
                 'b_capped_history_count':len(classes[('B_cap',)]),
                 'nonsingleton_classes':sum(len(x)>1 for x in classes.values())}
    P=('POP',);C=('CANCEL',);X=('APP',B,B);Y=('APP',B,A)
    probes=[(P,),(P,P),(P,P,P),(P,P,P,C),
            (P,P,P,Y,C),(P,P,P,Y,C,X,C),
            (P,P,P,X,C),(P,P,P,X,C,C),
            (P,P,P,X,C,Y,C),(P,P,P,X,C,X,C),
            (P,C,P,P,X,C),(P,X,C,C,P,P)]
    probe_cert={}
    for n in (11,12,16,30,40):
        reps={}
        for h in fiber(n):reps.setdefault(cls(n,h),h)
        fingerprint={k:tuple(execute(h,t) for t in probes) for k,h in reps.items()}
        assert len(reps)==len(set(fingerprint.values()))==24
        probe_cert[n]={'classes':len(reps),'distinct_12_trace_signatures':len(set(fingerprint.values()))}
    checks=0; trace_count=0
    groups=defaultdict(list)
    for h in fiber(11):groups[cls(11,h)].append(h)
    for max_apps,alphabet,max_depth in [(1,D,6),(2,(A,B),7)]:
        for trace in trace_words(max_apps,alphabet,max_depth):
            trace_count+=1
            for group in groups.values():
                rep=execute(group[0],trace)
                for h in group[1:]:
                    checks+=1
                    assert execute(h,trace)==rep,(h[:3],trace)
    return {'marker':'STAGE422B_EXACT_TWENTY_FOUR_COUPLED_STACK_PASS',
            'scope':'p=3 Q POP, c=2 paired inverse CANCEL, full directed J and absolute K, native six-axis D',
            'theorem':'q_(3,2)(F_n) = 24 for all n >= 11',
            'new_proof':['h_Q <= h_P for surviving paired-APP suffixes, without a P-tail premise',
                         'd_P <= c+1 = 3 and d_Q <= p+d_P <= 6 for one-B P; if P ends A^3 then d_P <= c=2 and d_Q <=5',
                         'common retained 6-label suffix bisimulation when P ends A^3',
                         'fixed-P, common Q-last-7 class lemma; B-capped s=n-5 class merge'],
            'frozen_global':'bf84bd7c61a2444b59b1da96be57df0e9ae47e53',
            'frozen_em':'2af3fc484eb11060b69e0afc1b562bcaf5ad1419',
            'p000_blob':'bcc2590d3168a28f72e8b9f0f9b1f76faadcd488',
            'finite_n_checked':[11,40], 'total_original_histories_checked':total_hist,
            'finite_trace_language':[{'max_APP':1,'APP_alphabet_size':12,'max_trace_steps':6},
                                     {'max_APP':2,'APP_alphabet_size':2,'max_trace_steps':7}],
            'traces_examined':trace_count,'same_group_trace_comparisons':checks,
            'lower_bound_12_explicit_probe_cert':{str(n):v for n,v in probe_cert.items()},
            'lower_bound_probe_traces':[list(map(list,t)) for t in probes],
            'snapshots': {str(n):by_n[n] for n in (11,12,16,30,40)},
            'statement_status':'AUTHOR_SIDE_PROOF_WITH_FINITE_REPRO; INDEPENDENT_REVIEW_PENDING'}

if __name__=='__main__':print(json.dumps(verify(),ensure_ascii=False,indent=2,sort_keys=True))
