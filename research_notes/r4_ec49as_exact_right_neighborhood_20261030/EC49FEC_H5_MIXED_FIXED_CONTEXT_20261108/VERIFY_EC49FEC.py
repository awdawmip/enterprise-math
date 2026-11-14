#!/usr/bin/env python3
"""Independent EC49FEC exact verifier. Python standard library, no external physics.
Run in the same directory: python VERIFY_EC49FEC.py
It checks every fixed-outside H5 optimum and the explicit 109-edge system.
Science frozen at fc0f038e7bfd12c886b4d37f900bfb770c0f61ab.
"""
import json, itertools, collections, functools
from pathlib import Path

C = (6,4,1)
OPS = {'a':(-1,-1), 'c':(1,2,-1,-2), 'd':(2,1,-2,-1),
       'e':(3,1,1,-3), 'f':(1,-1), 'g':(2,-2)}
ORDER = 'acdefg'
TRANS = ((1,2,3,1,4,5),(1,6,7,1,1,1),(2,2,8,2,2,2),
         (3,8,3,3,3,3),(4,2,7,4,4,4),(5,6,3,5,5,5),
         (6,6,8,6,6,6),(7,8,7,7,7,7),(8,8,8,8,8,8))
SIG = (0,0,4,1,16,32,8,2,0)
Q = {2:4,3:2,4:2,5:4,6:2,7:4,8:4,9:2}
CLAUSES = (18,20,33,40)

def steps(w): return tuple(z for ch in w for z in OPS[ch])
def key(w):
    counts=collections.Counter(v for v in steps(w) if v>0)
    return tuple(counts.get(j,0) for j in (1,2,3))
def signature(w):
    q=0
    for ch in w: q=TRANS[q][ORDER.index(ch)]
    return SIG[q]
def prefix_set(w):
    ns=steps(w)
    return {ns[:i] for i in range(1,len(ns)+1)}
def check_system(paths):
    assert {int(h):len(v) for h,v in paths.items()}==Q
    allkeys=set(); covered=set()
    for h,words in paths.items():
        assert len(words)==len(set(words))
        bits=0
        for w in words:
            assert len(w)==int(h) and signature(w)
            st=steps(w)
            assert tuple(st.count(j)-st.count(-j) for j in range(1,7))==(2,0,0,0,0,0)
            k=key(w); allkeys.add(k)
            assert len(st)==2*sum(k)-2
            covered.update(prefix_set(w));bits |= signature(w)
        assert all(bits & cl for cl in CLAUSES)
    assert sum(map(len,paths.values()))==24 and len(allkeys)==5
    return len(covered)

@functools.lru_cache(None)
def pool(h,k):
    x,y,z=k
    na=z-1;ndc=x+y-h-1;nf=h+1-y-2*z;ng=h+1-x
    assert min(na,ndc,nf,ng)>=0
    answer=[]
    for nc in range(ndc+1):
        left=[na,nc,ndc-nc,z,nf,ng]
        def walk(q,w,todo):
            if not todo:
                if SIG[q]: answer.append((''.join(w),SIG[q]))
                return
            for i in range(6):
                if left[i]:
                    left[i]-=1;w.append(ORDER[i])
                    walk(TRANS[q][i],w,todo-1)
                    w.pop();left[i]+=1
        walk(0,[],h)
    assert len(answer)==len(set(answer))
    return tuple(answer)

def fixed_optima(fixed,b):
    bwords=pool(5,b); cwords=pool(5,C)
    assert set(s for _,s in bwords)=={1,2,4,8}
    assert set(s for _,s in cwords)=={1,2,4,8}
    outer=set().union(*(prefix_set(w) for ws in fixed.values() for w in ws))
    candidates=bwords+cwords
    active=sorted(set().union(*(prefix_set(w)-outer for w,s in candidates)))
    index={p:i for i,p in enumerate(active)}
    masks={w:sum(1<<index[p] for p in prefix_set(w)-outer) for w,s in candidates}
    groups=[]
    for target in (1,2,4,8):
        groups.append([(w,masks[w],0) for w,s in bwords if s==target]+
                      [(w,masks[w],1) for w,s in cwords if s==target])
    best=[10**9,10**9];counts=[0,0]
    for w0,m0,c0 in groups[0]:
      for w1,m1,c1 in groups[1]:
       mm=m0|m1;cc=c0+c1
       for w2,m2,c2 in groups[2]:
        mmm=mm|m2;ccc=cc+c2
        for w3,m3,c3 in groups[3]:
         n=ccc+c3
         if n==4: continue  # all-C, not a genuine B/C mix
         kind=0 if n==0 else 1
         counts[kind]+=1
         val=len(outer)+(mmm|m3).bit_count()
         if val<best[kind]:best[kind]=val
    return best,counts

CERT=json.loads(Path('EC49FEC_FIXED_CONTEXT_CERTIFICATES.json').read_text())
assert CERT['science_pin']=='fc0f038e7bfd12c886b4d37f900bfb770c0f61ab'
rows=CERT['rows']
assert len(rows)==12
record=[]
for index,row in enumerate(rows):
    a=tuple(row['a']); b=tuple(row['b'])
    assert tuple(CERT['C'])==C
    fixed={str(h):v for h,v in row['fixed'].items()}
    all_b={**fixed,'5':row['pure_h5']}
    mixed={**fixed,'5':row['mixed_h5']}
    assert check_system(all_b)==row['pure']
    assert check_system(mixed)==row['mixed']
    assert all(key(w)==b for w in row['pure_h5'])
    assert 0<sum(key(w)==C for w in row['mixed_h5'])<4
    minima,number=fixed_optima(fixed,b)
    assert minima==[row['pure'],row['mixed']],(index,minima,row)
    assert number==[row['np'],row['nm']],(index,number,row)
    record.append({'a':a,'b':b,'all_B':minima[0],'mixed':minima[1],
                   'mixed_minus_all_B':minima[1]-minima[0],
                   'literal_H5_choice_count':sum(number)})

BEST109={
 '2':['ce','ed','ge','ec'],
 '3':['feg','gef'],
 '4':['fegg','gefg'],
 '5':['gefgd','feggd','feggc','gefgc'],
 '6':['feggfg','gefgfg'],
 '7':['gefgdfd','feggddf','feggcfc','gefgccf'],
 '8':['gefgdfgf','feggfgfd','feggcffg','gefgfgfc'],
 '9':['feggfgfgf','gefgfgffg']
}
assert check_system(BEST109)==109
result={'science_pin':CERT['science_pin'],'fixed_contexts':len(record),
        'exact_H5_minima_checked':2*len(record),'valid_full_witnesses':2*len(record)+1,
        'mixed_penalties_positive':all(z['mixed_minus_all_B']>0 for z in record),
        'joint_complete_witness_cost':109,'rows':record}
Path('EC49FEC_VERIFICATION_REPORT.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='rows'},indent=2))
