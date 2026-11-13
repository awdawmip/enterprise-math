"""Stage511-B: exact D_h-safe gap saturation tests, Python stdlib only.
This is an independently implemented finite oracle, not a native MCP Result.
"""
from itertools import product
from functools import lru_cache
import json

def disp(a):
    v=[0]*6
    v[a//2] = 1 if a%2==0 else -1
    return tuple(v)

@lru_cache(None)
def F(word):
    D=[0]*6; E=[0]*144
    for i,(a,_,_) in enumerate(word):
        d=disp(a)
        for j in range(6): D[j]+=d[j]
        if i: E[word[i-1][0]*12+a]+=1
    return (len(word),tuple(D),tuple(E))

def commands(w,R,S,directions):
    n=len(w)
    for k in ('POP','DELETE2','INSERT2'):
        if k=='POP' and n: yield ((k,),n-1)
        if k=='DELETE2' and n>=3: yield ((k,),n-3)
        if k=='INSERT2' and n>=2:
            for a in directions: yield ((k,a),None)
    for r in R:
        if r<n:
            for a in directions: yield (('SET_END',r,a), n-1-r)
    for k in S:
        pos=[i for i,t in enumerate(w) if t[1]]
        if len(pos)>=k: yield (('DELETE_KTH_PUBLIC',k),pos[-k])

def apply(w,op,index):
    name=op[0]
    if name=='INSERT2':
        return w[:-2]+((op[1],1,-1),)+w[-2:]
    if name=='SET_END':
        arr=list(w); a,p,ident=arr[index]; arr[index]=(op[2],p,ident);return tuple(arr)
    return w[:index]+w[index+1:]

def reachable_originals(word,h,R,S,directions):
    assert all(t[2]>=0 for t in word)
    seen={word}; frontier={word}; touched=set(); nodes=0; edges=0
    for t in range(h):
        nxt=set()
        for w in frontier:
            nodes+=1
            for op,i in commands(w,R,S,directions):
                edges+=1
                if i is not None and w[i][2]>=0: touched.add(w[i][2])
                state=apply(w,op,i)
                if state not in seen:
                    seen.add(state);nxt.add(state)
        frontier=nxt
    return touched,nodes,edges

def compressed(word,h,R,S,directions,cap):
    D,_,_=reachable_originals(word,h,R,S,directions)
    pieces=[];gap=[]
    def flush():
        if gap:
            pieces.append(('g',F(tuple(gap)),min(cap,sum(t[1] for t in gap))));gap.clear()
    for a,p,i in word:
        if i in D:
            flush();pieces.append(('x',a,p))
        else: gap.append((a,p,i))
    flush()
    return tuple(pieces),D

def future_signature(word,h,R,S,directions):
    ops=(('POP',),('DELETE2',))+tuple(('INSERT2',a) for a in directions)+tuple(('SET_END',r,a) for r in R for a in directions)+tuple(('DELETE_KTH_PUBLIC',k) for k in S)
    @lru_cache(None)
    def walk(w,depth):
        if not depth:return ()
        legal={op:(i) for op,i in commands(w,R,S,directions)}
        return tuple((op, None if op not in legal else (F(apply(w,op,legal[op])),walk(apply(w,op,legal[op]),depth-1))) for op in ops)
    return F(word),walk(word,h)

def counterexample(K):
    assert K>=2
    g=max(K,4);suffix=5
    base=((0,1,0),(2,1,1))
    gapA=tuple((4,1 if j<K-2 else 0,2+j) for j in range(g))
    gapB=tuple((4,1 if j<K-1 else 0,2+j) for j in range(g))
    end=tuple((6,0,2+g+j) for j in range(suffix))
    a=base+gapA+end;b=base+gapB+end;n=len(a)
    R=(n-2,n-1);S=(K,);h=1
    D1,x1,y1=reachable_originals(a,h,R,S,(0,2,4,6))
    D2,x2,y2=reachable_originals(b,h,R,S,(0,2,4,6))
    cap=K-2
    sig1,_=compressed(a,h,R,S,(0,2,4,6),cap)
    sig2,_=compressed(b,h,R,S,(0,2,4,6),cap)
    assert D1==D2 and sig1==sig2
    ranks=[(op,i) for op,i in commands(a,R,S,(0,2,4,6)) if op[0]=='DELETE_KTH_PUBLIC']
    ranks2=[(op,i) for op,i in commands(b,R,S,(0,2,4,6)) if op[0]=='DELETE_KTH_PUBLIC']
    _,i=ranks[0];_,j=ranks2[0]
    assert i==0 and j==1
    fa=F(apply(a,('DELETE_KTH_PUBLIC',K),i));fb=F(apply(b,('DELETE_KTH_PUBLIC',K),j))
    assert fa!=fb
    sig_a=compressed(a,h,R,S,(0,2,4,6),K-1)[0]
    sig_b=compressed(b,h,R,S,(0,2,4,6),K-1)[0]
    assert sig_a!=sig_b
    return {'K':K,'word_length':n,'D_count':len(D1),'exposed_positions':sorted(D1),'opaque_P_counts':[K-2,K-1], 'same_cap_K_minus_2':sig1==sig2, 'distinguished_by_cap_K_minus_1':sig_a!=sig_b,'deleted_origins':[i,j],'displacement_after_delete':[fa[1],fb[1]],'edge_counts_differ':fa[2]!=fb[2]}

def exhaustive():
    roots=0;cross_pairs=0;state_nodes=0;transitions=0
    directions=(0,2)
    for n in range(2,6):
      for symbols in product(range(4),repeat=n):
        word=tuple((directions[x//2],x%2,i) for i,x in enumerate(symbols))
        for h,S,R in [(1,(1,),(0,)),(1,(2,),(n-1,n-2)),(1,(3,),(n-1,n-2)),(1,(1,3),(n-1,n-2)),(2,(1,3),(0,n-1))]:
          roots+=1
          cap=max(S)-1
          sig,D=compressed(word,h,R,S,directions,cap)
          dd,nn,tt=reachable_originals(word,h,R,S,directions)
          assert D==dd
          state_nodes+=nn;transitions+=tt
          sig_key=(h,S,R,sig)
          truth=future_signature(word,h,R,S,directions)
          prev=group.get(sig_key)
          if prev is None: group[sig_key]=truth
          else:
            cross_pairs+=1
            if prev!=truth:
              raise AssertionError(('false collision',n,h,S,R,sig))
    return {'roots':roots,'future_tree_crosschecks':cross_pairs,'reachability_preaction_nodes':state_nodes,'reachability_transitions':transitions,'unique_compressed_states':len(group)}

if __name__=='__main__':
    group={}
    examples=[counterexample(k) for k in range(2,7)]
    checks=exhaustive()
    r={'schema':'EM_STAGE511B_LOCAL_EXACT_CHECK_V1','cap_theorem':'max(0,K-1)','examples':examples,'exhaustive_2_direction_tagged_words_up_to_n5':checks,'assertions':'PASS','bounds':'Finite oracle over two X6 signed primitive directions (0,+E1;2,+E2); general proof independent of enumeration.'}
    print(json.dumps(r,indent=2,ensure_ascii=False))