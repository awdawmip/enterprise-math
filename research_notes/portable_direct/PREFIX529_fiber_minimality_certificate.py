#!/usr/bin/env python3
"""PREFIX-529: exact 51-state phase-resolving BRC/gate transducer certificate.

Frozen science: enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d.
This uses the typed signed-X6 BRC pair observer and branch-resolved native paths;
combinatorial arithmetic only; no trigonometry or physical residual attribution.
"""
from collections import defaultdict, Counter
import json

STARS=((0,2,5),(0,3,4),(1,2,4),(1,3,5))  # L1..L6, indices 0..5

def nearby(j,c):
    return [-(1 if c>0 else -1)*(a+1) for a in STARS[j] if a!=abs(c)-1]

def successor(s):
    j,p,c=s
    k=next(i for i,star in enumerate(STARS) if i!=j and abs(c)-1 in star)
    return [(j,c,v) for v in nearby(j,c) if v!=p]+[(k,c,v) for v in nearby(k,c)]

PHASES=tuple((j,p,sgn*(a+1)) for j in range(4) for a in STARS[j]
             for sgn in (-1,1) for p in nearby(j,sgn*(a+1)))
IDX={p:i for i,p in enumerate(PHASES)}
NEXT=tuple(tuple(IDX[v] for v in successor(s)) for s in PHASES)
T=IDX[(0,1,-3)]
PREDS=frozenset(i for i,n in enumerate(NEXT) if T in n)
assert len(PHASES)==48 and all(len(n)==3 for n in NEXT)
assert all(sum(i in succ for succ in NEXT)==3 for i in range(48))
assert len(PREDS)==3

def color(c):
    return 'a' if c==1 else 'A' if c==-1 else 'c' if abs(c)==3 else '_'

def encode_pair(src,dst,branch):
    a,b=-PHASES[src][2],PHASES[dst][2]
    return (a,b) if branch==0 else (b,a)  # INNER=0, OUTER=1

def gate(prev_inner,src,dst,branch):
    return int(prev_inner and branch==0 and dst==T)

def bit_after(phase,branch):
    return branch if phase in PREDS else None

VIRTUAL=tuple((i,b) for i in range(48) for b in ((0,1) if i in PREDS else (None,)))
assert len(VIRTUAL)==51
assert sum(len(NEXT[i])*2 for i,b in VIRTUAL)==306

# A local suffix distinguishes the two branch memories iff the phase can reach T.
for e in range(48):
    diff=[]
    for r in NEXT[e]:
        for branch in (0,1):
            if gate(True,e,r,branch)!=gate(False,e,r,branch):
                diff.append((r,branch))
    assert bool(diff)==(e in PREDS)
    if diff:
        assert diff==[(T,0)]

# Explicit same-start/end/visit/BRC/H prefixes separated by a common legal suffix.
w_start=IDX[(0,3,-6)]; w_mid=IDX[(0,-6,1)]
assert T in NEXT[w_mid] and w_mid in NEXT[w_start]
inner=encode_pair(w_start,w_mid,0)
outer=encode_pair(w_start,w_mid,1)
suffix=encode_pair(w_mid,T,0)
assert inner==(6,1) and outer==(1,6) and suffix==(-1,-3)
word_i=inner+suffix; word_o=outer+suffix
assert ''.join(map(color,word_i))=='_aAc'
assert ''.join(map(color,word_o))=='a_Ac'
assert sum(''.join(map(color,word_i))[n:n+3]=='aAc' for n in (0,1))==1
assert sum(''.join(map(color,word_o))[n:n+3]=='aAc' for n in (0,1))==0

def pairs(word):
    plus=Counter(x for x in word if x>0)
    minus=Counter(-x for x in word if x<0)
    return tuple(min(plus[a],minus[a]) for a in range(1,7))
assert pairs(inner)==pairs(outer)==(0,0,0,0,0,0)
assert pairs(word_i)==pairs(word_o)==(1,0,0,0,0,0)

# Exhaustive native-word scan with independent online 51-state and six BRC calculations.
actual_paths=0
per_depth={}
for s in range(48):
    frontier=[(s,(),0,False,tuple([0]*6),tuple([0]*6),bit_after(s,1))]
    for d in range(5):
        per_depth[d]=per_depth.get(d,0)+len(frontier)
        next_frontier=[]
        for e,word,H,last_inner,K,prevB,m in frontier:
            actual_paths+=1
            txt=''.join(map(color,word))
            hits=sum(txt[k:k+3]=='aAc' for k in range(len(txt)-2))
            assert hits==H
            assert m==bit_after(e,0 if last_inner else 1)
            start=s
            for ax in range(1,7):
                sigma=lambda ix: (1 if PHASES[ix][2]>0 else -1) if abs(PHASES[ix][2])==ax else 0
                delta=abs(sigma(e)-sigma(start))
                assert K[ax-1]>=delta and (K[ax-1]-delta)%2==0
                assert pairs(word)[ax-1]==(K[ax-1]-delta)//2
            if d==4:continue
            for dst in NEXT[e]:
                for br in (0,1):
                    new_word=word+encode_pair(e,dst,br)
                    inc=gate(last_inner,e,dst,br)
                    inc_compressed=gate(m==0,e,dst,br)
                    assert inc==inc_compressed
                    newK=list(K)
                    newK[abs(PHASES[e][2])-1]+=1
                    newK[abs(PHASES[dst][2])-1]+=1
                    newprev=bit_after(dst,br)
                    next_frontier.append((dst,new_word,H+inc,br==0,tuple(newK),prevB,newprev))
        frontier=next_frontier
assert per_depth=={d:48*6**d for d in range(5)}

# Independent whole-history weighted dynamic programs of the 96/51 memory variants.
full={(s,s,1,0,0):1 for s in range(48)}  # start/end, last branch, unsigned L1 visits, hits
compressed={(s,s,bit_after(s,1),0,0):1 for s in range(48)}
dp_results={}
for d in range(10):
    def reduce(table):
        obs=Counter()
        for (s,e,m,k,h),n in table.items():
            sig=lambda ix: (1 if PHASES[ix][2]>0 else -1) if abs(PHASES[ix][2])==1 else 0
            delta=abs(sig(e)-sig(s))
            assert k>=delta and (k-delta)%2==0
            obs[(h,(k-delta)//2)]+=n
        return obs
    obs1=reduce(full);obs2=reduce(compressed)
    assert obs1==obs2 and sum(obs1.values())==48*6**d
    dp_results[str(d)]={"history_count":str(sum(obs1.values())),
                         "distinct_H_p1_coefficients":len(obs1),
                         "full_DP_keys":len(full),"compressed_DP_keys":len(compressed)}
    if d==9:break
    n1=defaultdict(int); n2=defaultdict(int)
    for (s,e,last,k,h),n in full.items():
        for dst in NEXT[e]:
            for br in (0,1):
                inc=int(last==0 and br==0 and dst==T)
                kk=k+int(abs(PHASES[e][2])==1)+int(abs(PHASES[dst][2])==1)
                n1[(s,dst,br,kk,h+inc)]+=n
    for (s,e,last,k,h),n in compressed.items():
        for dst in NEXT[e]:
            for br in (0,1):
                inc=int(last==0 and br==0 and dst==T)
                kk=k+int(abs(PHASES[e][2])==1)+int(abs(PHASES[dst][2])==1)
                n2[(s,dst,bit_after(dst,br),kk,h+inc)]+=n
    full=n1;compressed=n2

results={
  "verdict":"ALL_CHECKS_PASS",
  "line":"PREFIX-529",
  "science_input":"enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d",
  "observer":"all six signed native-X6 BRC pair counts, aAc gate H, current phase; legal branch-labelled future macrosteps",
  "phase_count":48,"target_state":list(PHASES[T]),
  "target_predecessor_states":[list(PHASES[i]) for i in sorted(PREDS)],
  "minimal_conditional_phase_memory_states":51,
  "original_phase_last_branch_states":96,
  "compressed_labeled_transitions":306,"original_labeled_transitions":576,
  "witness":{"initial_phase":list(PHASES[w_start]),"common_end_phase":list(PHASES[w_mid]),
             "target_phase":list(PHASES[T]),"first_prefix_INNER":list(inner),
             "first_prefix_OUTER":list(outer),"common_suffix_INNER":list(suffix),
             "native_words":[list(word_i),list(word_o)],
             "colors":["_aAc","a_Ac"],"initial_p6":list(pairs(inner)),
             "final_p6":list(pairs(word_i)),"H_before":[0,0],"H_after":[1,0]},
  "native_word_checks":actual_paths,"enumeration_by_macro_depth":per_depth,
  "joint_p1_H_integer_DP_depth":9,"joint_DP_results":dp_results,
  "mathematical_scope":"exact 51 state online control for phase-resolving gate/BRC observer; exact six-axis BRC via visit counters and start/end correction. Separate Cell and path provenance retained in raw input; independent review pending."
}
print(json.dumps(results,ensure_ascii=False,indent=2))
