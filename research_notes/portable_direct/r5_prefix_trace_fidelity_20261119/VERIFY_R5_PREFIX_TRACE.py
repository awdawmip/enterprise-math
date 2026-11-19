#!/usr/bin/env python3
"""R5 prefix-trace experiment. Pure Python 3, exact exhaustive N=3."""
from itertools import product
from collections import deque,Counter
import json

def bfs(x,Y,act,L,kind):
    def match(u,v):
        return L[u]==L[v] if kind=='exact' else L[u]&~L[v]==0
    initial=(x,frozenset(Y if kind=='word' else (y for y in Y if match(x,y))))
    seen={initial}; q=deque([(initial,())])
    while q:
        (u,V),w=q.popleft()
        if not V or (kind=='word' and not any(match(u,v) for v in V)):
            return False,w
        for a,T in enumerate(act):
            v=T[u]
            W=frozenset(T[y] for y in V if kind=='word' or match(v,T[y]))
            z=(v,W)
            if z not in seen: seen.add(z);q.append((z,w+(a,)))
    return True,None

def mapcheck(x,Y,act,L,kind):
    n=len(L); I=tuple(range(n)); seen=set();q=deque([(I,(I,))])
    while q:
        f,h=q.popleft()
        valid=lambda y: all((L[p[x]]==L[p[y]] if kind=='exact' else L[p[x]]&~L[p[y]]==0) for p in (h if kind!='word' else (f,)))
        survivors=tuple(y for y in Y if valid(y))
        key=(f,survivors)
        if key in seen:continue
        seen.add(key)
        if not survivors:return False
        for T in act:
            g=tuple(T[f[i]] for i in range(n))
            q.append((g,h+(g,)))
    return True

def main():
    A=list(product(range(3),repeat=3));counts=Counter(); lengthmax=Counter(); example=None;total=0;checks=0
    for a in A:
      for b in A:
       for L in product(range(2),repeat=3):
        for m in range(8):
         S=tuple(i for i in range(3) if m>>i&1)
         if len(S)<2:continue
         for x in S:
          Y=tuple(i for i in S if i!=x); T=(a,b)
          outcome=[]
          for kind in ('word','positive','exact'):
           ok,w=bfs(x,Y,T,L,kind)
           assert ok==mapcheck(x,Y,T,L,kind)
           checks+=1;outcome.append(int(ok))
           if w is not None:lengthmax[kind]=max(lengthmax[kind],len(w))
          assert outcome[2]<=outcome[1]<=outcome[0]
          counts[''.join(map(str,outcome))]+=1;total+=1
          if outcome==[1,0,0] and example is None:
           example={'actions':[a,b],'labels':L,'x':x,'Y':Y}
    assert total==52488 and checks==157464
    # Three states, one action: WD1 true, positive trace false at word 'a'.
    x=0;Y=(1,2);L=(1,1,0);T=((0,2,0),)
    assert bfs(x,Y,T,L,'word')[0]
    assert bfs(x,Y,T,L,'positive')==(False,(0,))
    assert bfs(x,Y,T,L,'exact')==(False,(0,))
    assert dict(counts)=={'000':24831,'100':1092,'110':8043,'111':18522}
    out={'n':3,'ordered_actions':2,'binary_labels':1,'exhaustive_cases':total,'independent_semigroup_comparisons':checks,
         'counts_word_positive_exact':dict(sorted(counts.items())),'maximum_minimal_bad_word_length':dict(lengthmax),
         'one_action_counterexample':{'labels':[1,1,0],'T_a':[0,2,0],'x':0,'Y':[1,2],'word_safe':True,'positive_trace_safe':False,'exact_trace_safe':False},
         'first_two_action_gap_example':example,'arithmetic':'exact integer and boolean; complete finite domain',
         'status':'AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED'}
    print('PASS_R5_PREFIX_TRACE',total,checks,dict(sorted(counts.items())))
    with open('RESULT_R5_PREFIX_TRACE.json','w') as f:json.dump(out,f,indent=2,sort_keys=True)
if __name__=='__main__':main()
