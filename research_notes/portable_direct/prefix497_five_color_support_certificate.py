#!/usr/bin/env python3
"""Exact five-color Parikh support certificate (PREFIX-497).

Model: native X6 signed five-axis path family, sixth axis unused.
Observer (n,y_a,...,y_e,V,W,q,t), with g in {'aab','aba'}.
This code executes integer/finite-state equalities only; no floating arithmetic.
"""
from collections import defaultdict
from math import comb
import json

GATES=('aab','aba')
LETTERS='aAbBcCdDeE'
COLORS='abBcx'              # x = A,d,D,e,E; c = c,C
V_COEFF=(0,1,0,2,1)
W_COEFF=(0,0,1,0,1)
MAX_N=9

def color(ch):
    if ch in 'abB': return ch
    if ch in 'cC': return 'c'
    return 'x'

def ctrl_next(q,t,ch,g):
    suf=g[:q]+ch
    nq=max(j for j in range(4) if suf.endswith(g[:j]))
    nt=t if t!='N' else ('B' if ch in 'bB' else 'C' if ch=='c' else 'N')
    return (nq,nt)

def raw_next(st,ch,g):
    y=st[:5]
    v,w,q,t=st[5:]
    i=LETTERS.index(ch)//2
    ep=1 if ch.islower() else -1
    delta=int(ep*y[i]<0)
    ny=list(y);ny[i]+=ep
    return tuple(ny)+(v+V_COEFF[i]*delta,w+W_COEFF[i]*delta)+ctrl_next(q,t,color(ch),g)

def color_tables(g,max_n):
    table={(0,0,0,0,0): {(0,'N')}}
    tables=[table]
    for n in range(max_n):
        nxt=defaultdict(set)
        for sig,cs in table.items():
            for i,ch in enumerate(COLORS):
                sig2=list(sig);sig2[i]+=1;sig2=tuple(sig2)
                nxt[sig2].update(ctrl_next(q,t,ch,g) for q,t in cs)
        table=dict(nxt)
        assert len(table)==comb(n+5,4)
        tables.append(table)
    return tables

def lattice_support(base, n, table):
    y=base[:5];v,w=base[5:]
    total_abs=sum(map(abs,y))
    if total_abs>n or (n-total_abs)%2: return frozenset()
    m=(n-total_abs)//2
    result=set()
    for e in range(max(0, w+1)):
        for d in range(max(0,(v-e)//2+1)):
            pb=v-2*d-e
            pc=w-e
            pa=m-v-w+d+e
            if min(pa,pb,pc,d,e)<0:continue
            sig=(pa+max(0,y[0]),pb+max(0,y[1]),pb+max(0,-y[1]),
                 2*pc+abs(y[2]),pa+max(0,-y[0])+2*(d+e)+abs(y[3])+abs(y[4]))
            assert sum(sig)==n
            assert sig in table, (n,base,sig)
            result.update(table[sig])
    return frozenset(result)

def raw_direct_obs(word,g):
    u=[word.count(ch) for ch in 'abcde']
    v=[word.count(ch) for ch in 'ABCDE']
    y=tuple(u[i]-v[i] for i in range(5))
    p=[min(u[i],v[i]) for i in range(5)]
    V=p[1]+2*p[3]+p[4]
    W=p[2]+p[4]
    q=max(j for j in range(4) if word.endswith(g[:j]))
    t='N'
    for ch in word:
        if ch in 'bB':t='B';break
        if ch in 'cC':t='C';break
    return y+(V,W,q,t)

def main():
    output={
      'status':'ALL_CHECKS_PASS', 'scope':'X6 five-axis signed path subfamily; sixth axis unused',
      'scientific_pin':'f42f2906d77f24085c123f3ccfe9667d41caa96d',
      'max_n':MAX_N,'gates':{},
      'five_colors': {'a':'a','b':'b','B':'B','c':'c/C','x':'A/d/D/e/E'}
    }
    for g in GATES:
        tables=color_tables(g,MAX_N)
        raw={(0,0,0,0,0,0,0,0,'N')}
        checks=[]
        words=['']
        for n in range(MAX_N+1):
            tb=tables[n]
            assert len(tb)==comb(n+4,4)
            assert all(len(v)<=11 for v in tb.values())
            groups=defaultdict(set)
            for st in raw: groups[st[:7]].add(st[7:])
            reconstructed=0
            for base,support in groups.items():
                calc=lattice_support(base,n,tb)
                assert calc==support, (g,n,base,calc,support)
                reconstructed+=len(calc)
            assert reconstructed==len(raw)
            if n<=4:
                raw_words={raw_direct_obs(word,g) for word in words}
                assert raw_words==raw,(g,n,len(raw_words),len(raw))
                words=[word+ch for word in words for ch in LETTERS]
            checks.append({
                'n':n,
                'five_color_signatures':len(tb),
                'ten_letter_occupancy_signatures':comb(n+9,9),
                'base_observation_fibers':len(groups),
                'full_joint_states':len(raw),
                'full_support_agreement':True,
            })
            if n<MAX_N:
                raw={raw_next(st,ch,g) for st in raw for ch in LETTERS}
        output['gates'][g]={'checks':checks,'ordered_word_verification':'n=0..4, exhaustive 11111 words'}
    print(json.dumps(output,sort_keys=True,indent=2,ensure_ascii=False))

if __name__=='__main__':main()
