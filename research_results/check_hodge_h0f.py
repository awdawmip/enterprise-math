#!/usr/bin/env python3
from fractions import Fraction
from dataclasses import dataclass
from itertools import product
from collections import defaultdict
from pathlib import Path
import json, hashlib, sys

ROOT=Path(__file__).resolve().parent
PASS=0; FAIL=[]
def check(cond,label):
    global PASS
    if cond: PASS+=1
    else: FAIL.append(label)

@dataclass(frozen=True)
class LP:
    terms: tuple
    @staticmethod
    def from_dict(d):
        dd={}
        for e,c in d.items():
            c=Fraction(c)
            if c: dd[tuple(e)]=dd.get(tuple(e),Fraction(0))+c
        dd={e:c for e,c in dd.items() if c}
        return LP(tuple(sorted((e[0],e[1],c.numerator,c.denominator) for e,c in dd.items())))
    @staticmethod
    def zero(): return LP(())
    @staticmethod
    def one(): return LP.from_dict({(0,0):1})
    @staticmethod
    def mon(a,b,c=1): return LP.from_dict({(a,b):c})
    def dict(self): return {(a,b):Fraction(n,d) for a,b,n,d in self.terms}
    def __add__(self,o):
        d=self.dict()
        for e,c in o.dict().items(): d[e]=d.get(e,Fraction(0))+c
        return LP.from_dict(d)
    def __neg__(self): return LP.from_dict({e:-c for e,c in self.dict().items()})
    def __sub__(self,o): return self+(-o)
    def __mul__(self,o):
        d={}
        for (a,b),c in self.dict().items():
            for (x,y),f in o.dict().items():
                e=(a+x,b+y); d[e]=d.get(e,Fraction(0))+c*f
        return LP.from_dict(d)
    def scale(self,c): return LP.from_dict({e:Fraction(c)*v for e,v in self.dict().items()})
    def pow_int(self,n):
        if n==0:return LP.one()
        if n<0:
            d=self.dict(); check(len(d)==1,"negative power only monomial")
            (e,c),=d.items(); return LP.mon(e[0]*n,e[1]*n,c**n)
        r=LP.one();b=self
        while n:
            if n&1:r=r*b
            b=b*b;n//=2
        return r
    def deriv(self,k):
        d={}
        for (a,b),c in self.dict().items():
            ex=[a,b]
            if ex[k]:
                coeff=c*ex[k];ex[k]-=1
                d[tuple(ex)]=d.get(tuple(ex),Fraction(0))+coeff
        return LP.from_dict(d)
    def regular(self): return all(a>=0 and b>=0 for a,b,_,_ in self.terms)

chart_coords={0:(1,2),1:(0,2),2:(0,1)}
SINK=("SINK",)
ACTIONS=("P","M")
PARAMS=((1,1),(1,2),(2,1),(2,2))

def ratio_X(k,base,target):
    tc=chart_coords[target]
    def xtoj(idx):
        if idx==target:return LP.one()
        if idx==tc[0]:return LP.mon(1,0)
        if idx==tc[1]:return LP.mon(0,1)
        raise RuntimeError
    return xtoj(k)*xtoj(base).pow_int(-1)

def sub(poly,src,target):
    sc=chart_coords[src]
    z1=ratio_X(sc[0],src,target);z2=ratio_X(sc[1],src,target)
    out=LP.zero()
    for (a,b),c in poly.dict().items():
        out=out+z1.pow_int(a)*z2.pow_int(b).scale(c)
    return out

def transport(form,src,target,m):
    if src==target:return form
    A,B=form;sc=chart_coords[src]
    zs=[ratio_X(sc[0],src,target),ratio_X(sc[1],src,target)]
    As=[sub(A,src,target),sub(B,src,target)]
    frame=ratio_X(src,target,target).pow_int(m)
    out=[]
    for q in (0,1):
        C=LP.zero()
        for Ai,zi in zip(As,zs): C=C+Ai*zi.deriv(q)
        out.append(frame*C)
    return tuple(out)

def seeds(B):
    out=[]
    for r in range(B+1):
        for s in range(B+1):
            M=LP.mon(r,s)
            out += [
              (f"dx_r{r}_s{s}",(M,LP.zero())),
              (f"dy_r{r}_s{s}",(LP.zero(),M)),
              (f"plus_r{r}_s{s}",(M,M)),
              (f"angular_r{r}_s{s}",(LP.mon(r,s+1),LP.mon(r+1,s,-1)))]
    return out

def skey(c,f): return (c,f[0].terms,f[1].terms)
def sdecode(st):
    if st==SINK:return None
    c,a,b=st;return c,(LP(a),LP(b))
def move(st,a,m):
    if st==SINK:return SINK
    c,f=sdecode(st);t=(c+1)%3 if a=="P" else (c-1)%3
    tf=transport(f,c,t,m)
    return skey(t,tf) if tf[0].regular() and tf[1].regular() else SINK
def layers(m,B):
    L=[set(skey(0,f) for _,f in seeds(B))]
    for _ in range(3):
        L.append(set(move(st,a,m) for st in L[-1] for a in ACTIONS))
    return L
def words(n): return [''.join(w) for w in product("PM",repeat=n)]
def exe(st,w,m):
    for a in w: st=move(st,a,m)
    return st
def sig(st,rem,m): return tuple(exe(st,w,m)!=SINK for w in words(rem))
def regsupp(form,c,m):
    return {j for j in range(3) if all(p.regular() for p in transport(form,c,j,m))}
def rho(st,m):
    if st==SINK:return (0,0)
    c,f=sdecode(st);R=regsupp(f,c,m)
    return (int((c+1)%3 in R),int((c-1)%3 in R))
def part(items,key):
    d=defaultdict(list)
    for x in items:d[key(x)].append(x)
    return d
def cmap(p): return {x:frozenset(v) for v in p.values() for x in v}
def serpoly(p): return [[a,b,n,d] for a,b,n,d in p.terms]
def serstate(st):
    if st==SINK:return {"sink":True}
    c,f=sdecode(st);return {"chart":f"U{c}","form":[serpoly(f[0]),serpoly(f[1])]}
def source_hash(m,B):
    L=layers(m,B)
    o={"m":m,"B":B,"depth":3,"actions":["P","M"],"stages":[],"transitions":[]}
    for lay in L:o["stages"].append([serstate(st) for st in sorted(lay,key=repr)])
    for i in range(3):
        rec=[]
        for st in sorted(L[i],key=repr):
            rec.append({"from":serstate(st),"P":serstate(move(st,"P",m)),"M":serstate(move(st,"M",m))})
        o["transitions"].append(rec)
    return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(",",":")).encode()).hexdigest()

# Artifact presence / protocol fields
required=[
"HODGE_H0F_ALGEBRAIC_SOURCE_SPEC.json","HODGE_H0F_PARAMETER_REGISTRY.json",
"HODGE_H0F_DIFFERENTIAL_TRANSITION_DERIVATION.json","HODGE_H0F_ALGEBRAIC_GENERATION_REPLAY.json",
"HODGE_H0F_MULTISTEP_SOURCE_REGISTRY.json","HODGE_H0F_ALGEBRAIC_BASELINE_SANDWICH.json",
"HODGE_H0F_SOURCE_NORMAL_FORM_REGISTRY.json","HODGE_H0F_SUFFIX_QUOTIENT_REGISTRY.json",
"HODGE_H0F_COMPARISON_THEOREM_REGISTRY.json","HODGE_H0F_PROOF_LEVERAGE_CERTIFICATE_REGISTRY.json",
"HODGE_H0F_ATTRIBUTION_CERTIFICATE_REGISTRY.json","HODGE_H0F_MIXING_CANCELLATION_CONTROLS.json",
"HODGE_H0F_BASELINE_GAMING_CONTROL.json","HODGE_H0F_PRESENTATION_NATURALITY_LEDGER.json",
"HODGE_H0F_PRIOR_ART_NOVELTY_LEDGER.json","HODGE_H0F_TARGET_LEAKAGE_LEDGER.json",
"HODGE_H0F_HODGE_R3_PREINTERFACE.json","HODGE_H0F_CLASSIFICATION.json","HODGE_H0F_SEMANTIC_CHECKPOINT.md"]
for f in required: check((ROOT/f).exists(),f"required {f}")

cls=json.loads((ROOT/"HODGE_H0F_CLASSIFICATION.json").read_text())
check(cls["primary_disposition"]=="H0F_R1_SOURCE_NORMAL_FORM_ALREADY_COMPLETE","disposition")
check(cls["hard_target_pass"] is False,"hard target false")
check(cls["actual_algebraic_source_generation"]=="PASS","source gen pass")
check(cls["non_diagonal_mixing"]=="PASS","mixing pass")
check(cls["R2_ATTRIBUTION_ADDENDUM_PASS"] is False,"attribution addendum false")
check(cls["H1_admissible"] is False and cls["Hodge_proved"] is False,"H1/Hodge firewall")

replay=json.loads((ROOT/"HODGE_H0F_ALGEBRAIC_GENERATION_REPLAY.json").read_text())
expected_hash={(x["m"],x["B"]):x["source_table_sha256"] for x in replay["parameter_replay"]}

total_suffix=0;total_qtrans=0
for m,B in PARAMS:
    L=layers(m,B)
    check(source_hash(m,B)==expected_hash[(m,B)],f"source hash m{m}B{B}")
    # composition and loops on seeds
    for sid,f in seeds(B):
        for i in range(3):
            fi=transport(f,0,i,m)
            for j in range(3):
                check(transport(fi,i,j,m)==transport(f,0,j,m),f"compose {m}{B}{sid}{i}{j}")
        for seq in ((1,2,0),(2,1,0)):
            cur=f;c=0
            for t in seq: cur=transport(cur,c,t,m);c=t
            check(cur==f,f"loop {m}{B}{sid}{seq}")
    # q and source rho equality; descended transitions; fine/q observation consistency
    qmaps=[];groups=[]
    for i in range(3):
        rem=3-i
        q=part(L[i],lambda st:sig(st,rem,m)); r=part(L[i],lambda st:rho(st,m))
        check(cmap(q)==cmap(r),f"q=rho {m}{B}s{i}")
        gs=sorted([sorted(v,key=repr) for v in q.values()],key=lambda g:repr(g[0]))
        mp={st:k for k,g in enumerate(gs) for st in g};qmaps.append(mp);groups.append(gs)
    induced=[]
    for i in range(2):
        td={}
        for qi,g in enumerate(groups[i]):
            for a in ACTIONS:
                tar={qmaps[i+1][move(st,a,m)] for st in g}
                check(len(tar)==1,f"q descend {m}{B}s{i}q{qi}{a}")
                td[(qi,a)]=next(iter(tar))
                total_qtrans+=len(g)
        induced.append(td)
    td={}
    for qi,g in enumerate(groups[2]):
        for a in ACTIONS:
            obs={move(st,a,m)!=SINK for st in g}
            check(len(obs)==1,f"q final {m}{B}q{qi}{a}")
            td[(qi,a)]=next(iter(obs));total_qtrans+=len(g)
    induced.append(td)
    for i in range(3):
        rem=3-i
        for st in L[i]:
            for w in words(rem):
                fine=exe(st,w,m)!=SINK
                cur=qmaps[i][st]
                for k,a in enumerate(w):
                    stage=i+k
                    if stage<2:cur=induced[stage][(cur,a)]
                    else:qobs=induced[2][(cur,a)]
                check(fine==qobs,f"q execute {m}{B}s{i}{w}")
                total_suffix+=1

# cancellation + weak summary
sd={sid:f for sid,f in seeds(1)}
ang=sd["angular_r0_s0"]; plus=sd["plus_r0_s1"]
a1=transport((ang[0],LP.zero()),0,1,2);a2=transport((LP.zero(),ang[1]),0,1,2);asm=transport(ang,0,1,2)
p1=transport((plus[0],LP.zero()),0,1,2);p2=transport((LP.zero(),plus[1]),0,1,2);psm=transport(plus,0,1,2)
check(not all(x.regular() for x in a1),"angular split1 nonregular")
check(not all(x.regular() for x in a2),"angular split2 nonregular")
check(all(x.regular() for x in asm),"angular sum regular")
check(asm==(LP.zero(),LP.mon(0,0,-1)),"angular exact -dv")
check(not all(x.regular() for x in psm),"plus nonregular")
check(regsupp(ang,0,2)=={0,1,2} and regsupp(plus,0,2)=={0},"control RegSupp differs")
check(sig(skey(0,ang),3,2)==(True,)*8 and sig(skey(0,plus),3,2)==(False,)*8,"control behavior differs")

# regular basis change
def bchange(f): return (f[0],f[1]-f[0])
for m,B in PARAMS:
    for sid,f in seeds(B):
        for c in range(3):
            fc=transport(f,0,c,m)
            check((all(x.regular() for x in fc))==(all(x.regular() for x in bchange(fc)),f"basis {m}{B}{sid}{c}")

# presentation permutations
def perm_form(form,c,perm):
    tc=perm[c]; old=chart_coords[c]; new=chart_coords[tc]
    vm=[new.index(perm[idx]) for idx in old]
    def vp(poly):
        d={}
        for (a,b),co in poly.dict().items():
            ex=[0,0];ex[vm[0]]+=a;ex[vm[1]]+=b
            d[tuple(ex)]=d.get(tuple(ex),0)+co
        return LP.from_dict(d)
    out=[LP.zero(),LP.zero()]
    for k,p in enumerate(form): out[vm[k]]=out[vm[k]]+vp(p)
    return tc,tuple(out)
def perm_state(st,perm):
    if st==SINK:return SINK
    c,f=sdecode(st);tc,tf=perm_form(f,c,perm);return skey(tc,tf)
def amap(perm,a):
    vals=[]
    for c in range(3):
        t=(c+1)%3 if a=="P" else (c-1)%3
        mc=perm[c];mt=perm[t]
        vals.append("P" if mt==(mc+1)%3 else "M")
    check(len(set(vals))==1,f"action map {perm}{a}")
    return vals[0]
perms=({0:1,1:0,2:2},{0:1,1:2,2:0})
for perm in perms:
    am={a:amap(perm,a) for a in ACTIONS}
    for m,B in PARAMS:
        L=layers(m,B)
        for i in range(3):
            for st in L[i]:
                for a in ACTIONS:
                    check(perm_state(move(st,a,m),perm)==move(perm_state(st,perm),am[a],m),f"perm trans {perm}{m}{B}{i}{a}")
                for w in words(3-i):
                    mw=''.join(am[a] for a in w)
                    check((exe(st,w,m)!=SINK)==(exe(perm_state(st,perm),mw,m)!=SINK),f"perm sig {perm}{m}{B}{i}{w}")

# Artifact semantics
mix=json.loads((ROOT/"HODGE_H0F_MIXING_CANCELLATION_CONTROLS.json").read_text())
check(mix["non_diagonal_transition_present"] is True,"mixing present artifact")
check(mix["negative_scalarized_control"]["verdict"]=="COMPONENTWISE_SPLIT_POLE_SUPPORT_INCOMPLETE","weak summary rejected")
nf=json.loads((ROOT/"HODGE_H0F_SOURCE_NORMAL_FORM_REGISTRY.json").read_text())
check(nf["conclusion"]=="WHOLE_FORM_REGSUPP_RELATIVE_MASK_ALREADY_COMPLETE","source NF conclusion")
lac=json.loads((ROOT/"HODGE_H0F_ATTRIBUTION_CERTIFICATE_REGISTRY.json").read_text())["certificates"][0]
check(lac["robust_transform_attributed"] is False,"no robust attribution")
check(lac["R2_ATTRIBUTION_ADDENDUM_PASS"] is False,"lac addendum false")
leak=json.loads((ROOT/"HODGE_H0F_TARGET_LEAKAGE_LEDGER.json").read_text())
check(leak["target_leakage_verdict"]=="PASS","target leakage pass")
r3=json.loads((ROOT/"HODGE_H0F_HODGE_R3_PREINTERFACE.json").read_text())
check(r3["H1_admissible"] is False and r3["Hodge_proved"] is False,"r3 firewall")

out={"schema":"HODGE_H0F_CHECKER_OUTPUT_V1","status":"PASS" if not FAIL else "FAIL",
     "passed":PASS,"failed":len(FAIL),"failures":FAIL,
     "recomputed_suffix_checks":total_suffix,"recomputed_q_transition_representative_checks":total_qtrans,
     "meaning":"protocol/exact finite algebraic source consistency only; PASS is not a Hodge proof and does not override classification"}
print(json.dumps(out,indent=2,sort_keys=True))
sys.exit(0 if not FAIL else 1)
