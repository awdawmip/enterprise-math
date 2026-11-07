"""Stage492-B exact finite oracle (stdlib; integer/word equality only)."""
from collections import Counter, defaultdict
from itertools import product
import json
D='ABCDEFGHIJKL' # +E1..+E6,-E1..-E6
V={c:tuple((1 if j==i else 0) if i<6 else (-1 if j==i-6 else 0) for j in range(6)) for i,c in enumerate(D)}
P='ABGABA';W='GH'; n=16; d=3
Q=lambda h:P+W+'A'+h+'A'
def edges(w): return Counter(zip(w,w[1:]))
def disp(w): return tuple(sum(V[c][j] for c in w) for j in range(6))
def obs(p,q): return len(p),len(q),disp(p),disp(q),tuple(edges(q).get((a,b),0) for a in D for b in D),sum(a==b for a,b in zip(p,q))
def tri(w,j): return w[j-2:j+1] # 1-based center
def moving(w,z):
    j=len(w)-d;assert 2<=j<len(w)
    return w[:j-1]+z+w[j:]
def delete(w,j):return w[:j-1]+w[j:]
q1=Q('ABAGGG');q2=Q('BAAGGG')
assert obs(P,q1)==obs(P,q2)
assert [tri(q1,j) for j in (13,14)]==[tri(q2,j) for j in (13,14)]
assert tri(q1,12)!=tri(q2,12)
base_checks=0
for pop,app in ((0,0),(1,0),(0,1),(1,1)):
    for order in (('POP','APPEND'),('APPEND','POP')) if pop and app else (('POP',) if pop else ('APPEND',) if app else (),):
        for z in D if app else ('',):
            def go(q):
                for op in order:q=q[:-1] if op=='POP' else q+z
                return q
            a,b=go(q1),go(q2)
            for p in [P,P[:-1]]+[P+c for c in D]+[P[:-1]+c for c in D]:
                assert obs(p,a)==obs(p,b);base_checks+=1
for appended in ('',)+tuple(D):
    for z in D:
        assert obs(P,moving(q1+appended,z))==obs(P,moving(q2+appended,z))
a,b=q1[:-1],q2[:-1]
assert obs(P,a)==obs(P,b) and obs(P,moving(a,'I'))!=obs(P,moving(b,'I'))
a,b=delete(q1,15),delete(q2,15)
assert obs(P,a)==obs(P,b) and obs(P,moving(a,'I'))!=obs(P,moving(b,'I'))
assert delete(q1,15)!=q1[:-1] and delete(q2,15)!=q2[:-1] # genuinely internal
fib=defaultdict(list)
for x in map(''.join,product('ABGH',repeat=6)):
    q=Q(x); key=tuple(edges(q).get((a,b),0) for a in D for b in D),q[-1]
    fib[key].append(q)
old=set();new=set()
for key,qs in fib.items():
    for q in qs:
        old.add((key,tri(q,13),tri(q,14)))
        new.add((key,tri(q,12),tri(q,13),tri(q,14)))
assert len(old)==3904 and len(new)==4096
out={'H_population':4096,'initial_fibers':len(fib),'old_classes':len(old),'pop_aware_classes':len(new),'base_PQ_observer_checks':base_checks,'pre_pop_set_symbol_checks':13*12,'witness':{'H1':'ABAGGG','H2':'BAAGGG','SET_from_end':3,'pop_then_set_center':12,'interior_delete_center':15,'replace_with':'I','post_edit_observable_different':True},'scope':'author-side finite exact verification, not native admission'}
print(json.dumps(out,sort_keys=True,indent=2))
