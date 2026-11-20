#!/usr/bin/env python3
"""Stage413-B exact native-labelled Euler/K transfer and sharp safe-boundary witnesses.
All inputs are two labelled words in the +E1/-E1 subalphabet of the 12
signed native spatial directions. No floating-point arithmetic.
"""
from collections import Counter, defaultdict
from functools import lru_cache
from itertools import product
import json

D = tuple('ABCDEFGHIJKL') # (A,B)=(+E1,-E1), ..., (K,L)=(+E6,-E6)
PAIRS = ('AA','AB','BA')

def disp(word):
    z=[0]*6
    for a in word:
        ix=D.index(a); z[ix//2] += 1 if ix%2==0 else -1
    return tuple(z)

def hist(word):
    return tuple(sorted(Counter(a+b for a,b in zip(word,word[1:])).items()))

def k(p,q): return sum(x==y for x,y in zip(p,q))

def obs(p,q):
    return (len(p),len(q),disp(p),disp(q),hist(p),hist(q),k(p,q))

def take(pair,trace,pop_budget=2,cancel_budget=1):
    p,q=pair
    for step in trace:
        if step[0]=='POP_Q':
            assert pop_budget>0 and q
            pop_budget-=1;q=q[:-1]
        elif step[0]=='CANCEL':
            assert cancel_budget>0 and len(p)>=2 and len(q)>=2
            assert p[-2:] in ('AB','BA') and q[-2:] in ('AB','BA')
            cancel_budget-=1;p=p[:-2];q=q[:-2]
        else:
            assert step[0]=='APP' and step[1] in D and step[2] in D
            p+=step[1];q+=step[2]
    return [p,q],obs(p,q)

def family(n):
    for r in range(2,n-2):
        for s in range(r+2,n):
            q='A'*(r-1)+'B'+'A'*(s-r-1)+'B'+'A'*(n-s)
            for i in (r,s):
                p='A'*(i-1)+'B'+'A'*(n-i)
                yield p,q

def transfer(n,sP=4,sQ=5):
    # Exact residual directed-edge DP. Each edge TYPE is chosen once, not
    # multiplied by the number of copies, avoiding labelled-edge overcounting.
    initialP=(n-3,1,1);initialQ=(n-5,2,2);expectedK=n-1
    zP=(n-2,0,0,0,0,0);zQ=(n-4,0,0,0,0,0)
    @lru_cache(None)
    def walk(lastP,lastQ,edgesP,edgesQ,matches,endP,endQ):
        remains=sum(edgesP)
        if matches>expectedK or matches+remains<expectedK: return ()
        if remains==0:
            return (((endP,endQ,1),) if matches==expectedK and all(x==0 for x in edgesQ) else ())
        total=defaultdict(int)
        for u,edgeP in enumerate(PAIRS):
            if edgesP[u]==0 or edgeP[0]!=lastP:continue
            for v,edgeQ in enumerate(PAIRS):
                if edgesQ[v]==0 or edgeQ[0]!=lastQ:continue
                newP=list(edgesP);newP[u]-=1
                newQ=list(edgesQ);newQ[v]-=1
                a,b=edgeP[-1],edgeQ[-1]
                for suffixP,suffixQ,mass in walk(a,b,tuple(newP),tuple(newQ),matches+(a==b),(endP+a)[-sP:],(endQ+b)[-sQ:]):
                    total[(suffixP,suffixQ)]+=mass
        return tuple((a,b,c) for (a,b),c in total.items())
    out=defaultdict(int)
    starts=0
    for a,b in product(D,repeat=2):
        def endpoint_from(start,edge_types,counts):
            z=list(disp(start))
            for edge,c in zip(edge_types,counts):
                d=disp(edge[-1]);z=[v+c*w for v,w in zip(z,d)]
            return tuple(z)
        if endpoint_from(a,PAIRS,initialP)!=zP or endpoint_from(b,PAIRS,initialQ)!=zQ:continue
        starts+=1
        for p,q,m in walk(a,b,initialP,initialQ,int(a==b),a,b):out[(p,q)]+=m
    assert starts==1
    return dict(sorted(out.items())),walk.cache_info().currsize

# A fixed six-trace test battery. A disabled operation is itself observable.
TESTS=(
    (('POP_Q',),),
    (('POP_Q',),('POP_Q',)),
    (('POP_Q',),('POP_Q',),('CANCEL',)),
    (('POP_Q',),('POP_Q',),('APP','B','A'),('CANCEL',)),
    (('POP_Q',),('POP_Q',),('APP','B','B'),('CANCEL',)),
    (('POP_Q',),('CANCEL',),('POP_Q',)),
)

def signature(pair,trace):
    p,q=pair;pops=2;cancels=1;output=[]
    for op in trace:
        if op[0]=='POP_Q':
            if not pops or not q:return tuple(output)+(('DISABLED','POP_Q'),)
            pops-=1;q=q[:-1]
        elif op[0]=='CANCEL':
            if not cancels or len(p)<2 or len(q)<2 or p[-2:] not in ('AB','BA') or q[-2:] not in ('AB','BA'):
                return tuple(output)+(('DISABLED','CANCEL'),)
            cancels-=1;p=p[:-2];q=q[:-2]
        else:
            assert op[0]=='APP';p+=op[1];q+=op[2]
        output.append(obs(p,q))
    return tuple(output)

def nine_group(n,r,s,i):
    if s<=n-4:return 'G0'
    if s==n-3:return 'G1'
    if s==n-2:return 'G2' if i==r else 'G3'
    assert s==n-1
    if i==r:return 'G7' if r==n-3 else 'G4'
    return 'G5' if r<=n-5 else ('G6' if r==n-4 else 'G8')

def nine_certificate(n):
    observed=defaultdict(set);counts=Counter()
    for r in range(2,n-2):
        for s in range(r+2,n):
            q='A'*(r-1)+'B'+'A'*(s-r-1)+'B'+'A'*(n-s)
            for i in (r,s):
                p='A'*(i-1)+'B'+'A'*(n-i)
                group=nine_group(n,r,s,i)
                key=tuple(signature((p,q),t) for t in TESTS)
                observed[group].add(key)
                counts[group]+=1
    assert all(len(signatures)==1 for signatures in observed.values())
    assert len({next(iter(v)) for v in observed.values()})==len(observed)
    expected=[(n-6)*(n-7),2*(n-6),n-5,n-5,n-5,n-6,1,1,1]
    assert all(counts.get(f'G{i}',0)==expected[i] for i in range(9)),(n,counts,expected)
    return len(observed),[counts.get(f'G{i}',0) for i in range(9)]

def main():
    p1=('AABAAB','AAABAA');p2=('ABAAAB','AAABAA')
    q1=('AAAAAAB','AABABAA');q2=('AAAAAAB','ABAABAA')
    t=(('POP_Q',),('POP_Q',),('CANCEL',))
    assert obs(*p1)==obs(*p2) and p1[0][-3:]==p2[0][-3:] and p1[1]==p2[1]
    assert obs(*q1)==obs(*q2) and q1[0]==q2[0] and q1[1][-4:]==q2[1][-4:]
    assert p1[0][-2:] in ('AB','BA') and p1[1][-4:-2] in ('AB','BA')
    assert q1[0][-2:] in ('AB','BA') and q1[1][-4:-2] in ('AB','BA')
    p_out=[take(z,t) for z in (p1,p2)]
    q_out=[take(z,t) for z in (q1,q2)]
    assert p_out[0][1]!=p_out[1][1] and q_out[0][1]!=q_out[1][1]
    assert [s[1][-1] for s in p_out]==[2,1]
    assert q_out[0][1][5]!=q_out[1][1][5]
    rows=[]
    for n in [5,6,7,8,9,10,12,16,20]:
        direct=list(family(n)) if n<=10 else []
        transfer_counts,states=transfer(n)
        total=sum(transfer_counts.values())
        assert total==(n-3)*(n-4),n
        if direct:
            assert len(direct)==total
            assert len({obs(p,q) for p,q in direct})==1
            expected=Counter((p[-4:],q[-5:]) for p,q in direct)
            assert expected==transfer_counts,(n,expected,transfer_counts)
        test_classes,test_sizes=nine_certificate(n) if n>=6 else (2,[2])
        rows.append(dict(n=n,total=total,safe_suffix_4_5_states=len(transfer_counts),
                         six_trace_observable_classes=test_classes,six_trace_class_sizes=test_sizes,
                         dp_memo_states=states,
                         transfer_histogram={p+'|'+q:v for (p,q),v in transfer_counts.items()} if n==7 else None))
    return {'status':'STAGE413B_SHARP_ASYMMETRIC_BOUNDARY_PASS',
       'exact_input':'P000 native X6 D=12 signed directions, A=+E1 B=-E1; pure path-formal observer',
       'operation_trace':t,
       'P_four_necessary':{'initial_pairs':[p1,p2],'same_P_suffix3':p1[0][-3:],
                           'initial_K':obs(*p1)[-1], 'post_pairs':[s[0] for s in p_out],
                           'post_K':[s[1][-1] for s in p_out]},
       'Q_five_necessary':{'initial_pairs':[q1,q2],'same_Q_suffix4':q1[1][-4:],
                           'initial_K':obs(*q1)[-1], 'post_pairs':[s[0] for s in q_out],
                           'post_Q_histograms':[s[1][5] for s in q_out]},
       'F_n_transfer':rows,
       'six_trace_library':TESTS,
       'verification':'Exact integers; independent full path enumeration and Euler/K residual transfer for n=5..10; DP n=5,6,7,8,9,10,12,16,20. The generic all-horizon 4/5 sufficiency is a separate proof; computation only crosschecks particular witnesses/fibers.',
       'author_review_status':'UNREVIEWED_NOT_ADMITTED'}

if __name__=='__main__': print(json.dumps(main(),ensure_ascii=False,indent=2))
