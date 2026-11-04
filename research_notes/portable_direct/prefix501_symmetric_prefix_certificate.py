#!/usr/bin/env python3
"""PREFIX-501: exact signed-symmetry quotient and dense weighted lexicographic rank certificate.

No floating point; independently constructs native (displacement,BRC,KMP,source)
states, then tests symmetry and a compressed-radix prefix index on all states.
The all-n algorithm obtains quotient K from the earlier constant-arithmetic source
oracle (PREFIX-500); this finite checker obtains K from independent native DP.
"""
from collections import defaultdict, Counter
from bisect import bisect_right
import json, sys

LETTERS='aAbBcCdDeE'
GATES=('aab','aba')
CV=(0,1,0,2,1)
CW=(0,0,1,0,1)
MAX_N=9

def advance(x,ch,g):
    ya=list(x[:5]);V,W,q,t=x[5:]
    axis=LETTERS.index(ch)//2
    eps=1 if ch.islower() else -1
    d=int(ya[axis]*eps<0)
    ya[axis]+=eps
    suffix=g[:q]+ch
    nq=max(j for j in range(4) if suffix.endswith(g[:j]))
    if t=='N':
        if ch in 'bB':t='B'
        elif ch in 'cC':t='C'
    return tuple(ya)+(V+CV[axis]*d,W+CW[axis]*d,nq,t)

def ckey(base):
    u,v,c,d,e,V,W=base
    return (u,v,abs(c),abs(d)+abs(e),W,V)

def mkrow(pairs):
    """Sorted nonzero choice list, prefix offsets, total; exact integer."""
    pairs=sorted((int(x),int(w)) for x,w in pairs if w)
    coords=[];starts=[];weights=[];lookup={};s=0
    for val,w in pairs:
        assert val not in lookup and w>0
        coords.append(val);starts.append(s);weights.append(w);lookup[val]=s;s+=w
    return (coords, starts, weights, lookup, s)

def prepare(n, native):
    """Symmetry-compressed oracle and weighted-prefix rows, no full native y index."""
    supports=defaultdict(set)
    base_supports=defaultdict(set)
    for state in native:
        base=state[:7];ctrl=state[7:]
        base_supports[base].add(ctrl)
        supports[ckey(base)].add(ctrl)
    # Check every decomposed base carries exactly the same control support set.
    for b,cs in base_supports.items():
        assert supports[ckey(b)]==cs,(n,b,cs,supports[ckey(b)])

    # K is the single shared support set indexed by (u,v,|yc|,|yd|+|ye|,W,V).
    K={k:tuple(sorted(t)) for k,t in supports.items()}
    v_by_w=defaultdict(list)
    w_by_aggregate=defaultdict(list)
    for (u,v,c,s,W,V),ctrls in K.items():
        v_by_w[(u,v,c,s,W)].append((V,len(ctrls)))
    rowV={p:mkrow(t) for p,t in v_by_w.items()}
    for (u,v,c,s,W),row in rowV.items():
        w_by_aggregate[(u,v,c,s)].append((W,row[-1]))
    rowW={p:mkrow(t) for p,t in w_by_aggregate.items()}
    A={p:row[-1] for p,row in rowW.items()}
    assert sum(len(v) for v in K.values())<=len(native)

    # Build lex rows for y, preserving exact actual signed order while reusing
    # only A(u,v,|yc|,|yd|+|ye|) instead of all base-fiber support rows.
    rowE={};rowD={};rowC={};rowB={}
    choices_u=[]
    for u in range(-n,n+1):
        choices_v=[]
        for v in range(-(n-abs(u)),n-abs(u)+1):
            choices_c=[]
            for yc in range(-(n-abs(u)-abs(v)),n-abs(u)-abs(v)+1):
                budget=n-abs(u)-abs(v)-abs(yc)
                choices_d=[]
                for yd in range(-budget,budget+1):
                    pairs=[]
                    for ye in range(-(budget-abs(yd)),budget-abs(yd)+1):
                        s=abs(yd)+abs(ye)
                        w=A.get((u,v,abs(yc),s),0)
                        if w:pairs.append((ye,w))
                    row=mkrow(pairs)
                    if row[-1]:
                        rowE[(u,v,yc,yd)]=row
                        choices_d.append((yd,row[-1]))
                row=mkrow(choices_d)
                if row[-1]:
                    rowD[(u,v,yc)]=row
                    choices_c.append((yc,row[-1]))
            row=mkrow(choices_c)
            if row[-1]:
                rowC[(u,v)]=row
                choices_v.append((v,row[-1]))
        row=mkrow(choices_v)
        if row[-1]:
            rowB[(u,)]=row
            choices_u.append((u,row[-1]))
    root=mkrow(choices_u)
    assert root[-1]==len(native),(n,root[-1],len(native))
    rowlist=({():root},rowB,rowC,rowD,rowE,rowW,rowV)
    return K,rowlist,base_supports,A

def rank(state, K, rows):
    u,v,yc,yd,ye,V,W,q,t=state
    choices=(u,v,yc,yd,ye,W,V)
    p=();r=0
    for level,val in enumerate(choices):
        if level==5: p=(u,v,abs(yc),abs(yd)+abs(ye))
        elif level==6: p=(u,v,abs(yc),abs(yd)+abs(ye),W)
        row=rows[level][p]
        r+=row[3][val]
        if level<5:p=p+(val,)
    ctrls=K[(u,v,abs(yc),abs(yd)+abs(ye),W,V)]
    return r+ctrls.index((q,t))

def unrank(j,K,rows):
    assert 0<=j<rows[0][()][-1]
    y=[];p=();res=j
    for level in range(7):
        if level==5:p=(y[0],y[1],abs(y[2]),abs(y[3])+abs(y[4]))
        elif level==6:p=(y[0],y[1],abs(y[2]),abs(y[3])+abs(y[4]),y[5])
        row=rows[level][p]
        pos=bisect_right(row[1],res)-1
        assert 0<=pos<len(row[0]) and res<row[1][pos]+row[2][pos]
        res-=row[1][pos]
        val=row[0][pos]
        y.append(val)
        if level<5:p=p+(val,)
    u,v,yc,yd,ye,W,V=y
    ctrls=K[(u,v,abs(yc),abs(yd)+abs(ye),W,V)]
    assert 0<=res<len(ctrls)
    return tuple(y[:5])+(V,W)+ctrls[res]

def standalone_total_from_K(n,K):
    # Symmetry weighted sum: two signs for yc>0, 4s decompositions for s>0.
    z=0
    for (u,v,c,s,W,V),cs in K.items():
        mult_c=1 if c==0 else 2
        mult_de=1 if s==0 else 4*s
        z+=mult_c*mult_de*len(cs)
    return z

def run(N):
    output={'scientific_pin':'f42f2906d77f24085c123f3ccfe9667d41caa96d',
            'status':'ALL_CHECKS_PASS','arithmetic':'exact Python integers',
            'model':'X6 5-axis subfamily, fixed sixth-axis zero; (n,y,V,W,q,t)',
            'gates':{}}
    for g in GATES:
        states={(0,0,0,0,0,0,0,0,'N')}
        checks=[]
        for n in range(N+1):
            K,rows,bs,A=prepare(n,states)
            assert standalone_total_from_K(n,K)==len(states)
            base_fibers=len(bs)
            # Independent direct sort uses no quotient, prefix sums, or K keys.
            direct=sorted(states,key=lambda x:(x[:5],x[6],x[5],x[7],x[8]))
            for j,x in enumerate(direct):
                rr=rank(x,K,rows)
                assert rr==j,(g,n,j,rr,x)
                inv=unrank(j,K,rows)
                assert inv==x,(g,n,j,x,inv)
            assert len({ckey(b) for b in bs})==len(K)
            cnt={}
            for b in bs:
                key=(b[0],b[1],abs(b[2]),abs(b[3])+abs(b[4]))
                cnt[key]=cnt.get(key,0)+1
            checks.append({'n':n,'full_joint_states':len(states),'base_fibers':base_fibers,
                'quotient_support_keys':len(K),'unique_group_coordinates':len(A),
                'rank_inverse_checked':len(direct),
                'index_entry_counts':{
                    'y_lex':sum(len(row[0]) for d in rows[:5] for row in d.values()),
                    'W_lex':sum(len(row[0]) for row in rows[5].values()),
                    'V_lex':sum(len(row[0]) for row in rows[6].values())}})
            if n<N:
                states={advance(x,ch,g) for x in states for ch in LETTERS}
        output['gates'][g]=checks
    return output

if __name__=='__main__':
    N=int(sys.argv[1]) if len(sys.argv)>1 else MAX_N
    print(json.dumps(run(N),sort_keys=True,ensure_ascii=False,separators=(',',':')))
