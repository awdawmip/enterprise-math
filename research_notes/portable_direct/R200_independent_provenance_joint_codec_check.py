#!/usr/bin/env python3
"""Exact-integer reference checker for R200 independent provenance joint codec.

Run: python R200_independent_provenance_joint_codec_check.py
Generates R200_verification.json next to the script. No external packages.
"""
from __future__ import annotations
from itertools import permutations, product
from math import factorial
import json
from pathlib import Path
import random

def p(n,j):
    return factorial(n)//factorial(n-j)

def nstates(k):
    return sum(p(k,j) for j in range(k+1))

def source_last(word, labels):
    s=()
    for x in word:
        v=labels[x]
        if v is not None:
            s=tuple(t for t in s if t!=v)+(v,)
    return s

def partials(available):
    return (u for j in range(len(available)+1) for u in permutations(available,j))

def rank_partial(u, available):
    n=len(available); j=len(u)
    z=sum(p(n,h) for h in range(j))
    left=list(available)
    for i,x in enumerate(u):
        z+=left.index(x)*p(n-i-1,j-i-1)
        left.remove(x)
    return z

def unrank_partial(z, available):
    n=len(available)
    j=next(j for j in range(n+1) if z<sum(p(n,h) for h in range(j+1)))
    z-=sum(p(n,h) for h in range(j))
    left=list(available); out=[]
    for i in range(j):
        weight=p(n-i-1,j-i-1)
        c,z=divmod(z,weight)
        out.append(left.pop(c))
    assert z==0
    return tuple(out)

class JointCodec:
    def __init__(self, labels, k, L):
        assert len(labels)>0 and k>=0 and L>=0
        assert all(x is None or 0<=x<k for x in labels)
        assert set(x for x in labels if x is not None)==set(range(k))
        self.labels=tuple(labels); self.k=k; self.L=L; self.a=len(labels)
        self.d=tuple(labels.count(i) for i in range(k))
        self.d0=labels.count(None)
        self.w=[[0]*(1<<k) for _ in range(L+1)]
        for mask in range(1<<k):
            self.w[0][mask]=nstates(k-mask.bit_count())
        for q in range(1,L+1):
            for mask in range(1<<k):
                cur=(self.d0+sum(self.d[i] for i in range(k) if mask&(1<<i)))*self.w[q-1][mask]
                for i in range(k):
                    if not mask&(1<<i):
                        cur+=self.d[i]*self.w[q-1][mask|(1<<i)]
                self.w[q][mask]=cur
        self.short=sum(self.a**h for h in range(L))
        self.count=self.short+self.w[L][0]
        self.bits=(self.count-1).bit_length()

    def _mask(self,mask,ch):
        lab=self.labels[ch]
        return mask if lab is None else mask|(1<<lab)

    def rank(self,state):
        s,t=state
        assert len(t)<=self.L
        if len(t)<self.L:
            assert s==source_last(t,self.labels)
            val=0
            for x in t: val=val*self.a+x
            return sum(self.a**h for h in range(len(t)))+val
        z=self.short; mask=0
        for idx,ch in enumerate(t):
            q=self.L-idx-1
            for x in range(ch):
                z+=self.w[q][self._mask(mask,x)]
            mask=self._mask(mask,ch)
        v=source_last(t,self.labels)
        assert s[-len(v):]==v if v else True
        u=s[:len(s)-len(v)] if v else s
        assert len(set(s))==len(s) and all(x not in v for x in u)
        avail=tuple(i for i in range(self.k) if not mask&(1<<i))
        return z+rank_partial(u,avail)

    def unrank(self,z):
        assert 0<=z<self.count
        if z<self.short:
            h=0
            while z>=self.a**h:
                z-=self.a**h; h+=1
            digits=[0]*h
            for i in range(h-1,-1,-1):
                digits[i]=z%self.a;z//=self.a
            t=tuple(digits)
            return source_last(t,self.labels),t
        z-=self.short;mask=0;out=[]
        for i in range(self.L):
            q=self.L-i-1
            for ch in range(self.a):
                nxt=self._mask(mask,ch)
                block=self.w[q][nxt]
                if z<block:
                    out.append(ch);mask=nxt
                    break
                z-=block
            else:
                raise AssertionError("invalid full-tail rank")
        t=tuple(out);v=source_last(t,self.labels)
        avail=tuple(i for i in range(self.k) if not mask&(1<<i))
        return unrank_partial(z,avail)+v,t

    def analytic_count(self):
        z=self.short
        for u in partials(tuple(range(self.k))):
            z+=(self.a-sum(self.d[i] for i in u))**self.L
        return z

def compose(x,y,L):
    s,t=x;v,u=y
    return tuple(x for x in s if x not in v)+v, (t+u)[-L:] if L else ()

def count_direction_only(m,k,L):
    v=lambda h:sum(p(k,j) for j in range(min(k,h)+1))
    return m**L*nstates(k)+sum(m**h*v(h) for h in range(L))

def reachable_states(c):
    for h in range(c.L):
        for tail in product(range(c.a),repeat=h):
            yield source_last(tail,c.labels),tail
    for tail in product(range(c.a),repeat=c.L):
        v=source_last(tail,c.labels)
        avail=tuple(i for i in range(c.k) if i not in v)
        for u in partials(avail):
            yield u+v,tail

def witness(state,c):
    s,tail=state
    if len(tail)<c.L: return tail
    v=source_last(tail,c.labels)
    u=s[:len(s)-len(v)] if v else s
    return tuple(c.labels.index(i) for i in u)+tail

def check():
    ran=random.Random(200)
    stats={"models":0,"exhaustive_states":0,"random_compositions":0,
           "analytic_count_checks":0,"uneven_multiplicity_models":0}
    cases=[(tuple(s for d in range(m) for s in (None,*range(k))),k,L,f"paired_{m}_{k}_{L}")
           for m in range(1,4) for k in range(4) for L in range(4)]
    cases += [((None,0,1,1),2,L,f"nonuniform_{L}") for L in range(5)]
    cases += [((0,1,2,2,2,None,0),3,L,f"nonuniform2_{L}") for L in range(4)]
    for labels,k,L,name in cases:
        c=JointCodec(labels,k,L)
        stats["models"]+=1
        if name.startswith("nonuniform"):stats["uneven_multiplicity_models"]+=1
        assert c.count==c.analytic_count()
        stats["analytic_count_checks"]+=1
        if c.count<=40000:
            states=list(reachable_states(c))
            assert len(states)==c.count and len(set(states))==len(states)
            assert {c.rank(s) for s in states}==set(range(c.count))
            for i,s in enumerate(states):
                assert c.rank(s)==i
                assert c.unrank(i)==s
            stats["exhaustive_states"]+=len(states)
        else:
            states=[c.unrank(ran.randrange(c.count)) for _ in range(300)]
            for s in states: assert c.unrank(c.rank(s))==s
        for _ in range(100):
            a,b=ran.choice(states),ran.choice(states)
            z=compose(a,b,L)
            wa,wb=witness(a,c),witness(b,c)
            assert source_last(wa+wb,c.labels)==z[0]
            assert (wa+wb)[-L:]==z[1] if L else z[1]==()
            assert c.unrank(c.rank(z))==z
            stats["random_compositions"]+=1
    examples={}
    for L in range(5):
        m=12;k=6
        c=JointCodec(tuple(s for d in range(m) for s in (None,*range(k))),k,L)
        v=count_direction_only(m,k,L)
        examples[f"L{L}"]={"paired_events_count":c.count,"paired_bits":c.bits,
                          "direction_only_count":v,"direction_only_bits":(v-1).bit_length()}
    labels=(None,0)
    words=((1,0),(0,1))
    assert source_last(words[0],labels)==source_last(words[1],labels)==(0,)
    result={"schema":"EM_R200_EXACT_REFERENCE_V1","status":"PASS",
            "parameters":{"small_uniform_m":"1..3","small_uniform_k":"0..3",
                          "small_L":"0..3","uniform_alphabet_size":"m(k+1)",
                          "additional_nonuniform_L":"0..4"},
            "counts":stats,"native_m12_k6":examples,
            "collision":{"event_alphabet":"0=(direction0,none);1=(direction0,source0)",
                         "word_a":list(words[0]),"word_b":list(words[1]),
                         "common_source_order":[0],"common_direction_tail":[0],
                         "distinct_paired_tail":[0,1]},
            "notes":"Integer-exact independent reference; not native package integration or independent theorem review."}
    Path(__file__).with_name("R200_verification.json").write_text(
        json.dumps(result,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(result,ensure_ascii=False,indent=2))

if __name__=="__main__":
    check()
