#!/usr/bin/env python3
"""Deterministic checker for P000 G15 Pareto-minimal S4 packages V16.

Consumes the frozen G15 grammar, enumerates every dependency-closed package,
applies the frozen fixed-sort definitional quotient, checks the universal
classification partition and Pareto frontiers, and re-runs the mandatory
finite symmetry / extension regressions. No external packages.
"""
from __future__ import annotations
import argparse, hashlib, json
from collections import Counter, defaultdict
from itertools import combinations, permutations, product
from pathlib import Path

TASK_ID="RS-P000-L1-NATIVE-CARRIER-CONTACT-BRIDGE"
PUBLICATION_ID="TP2-6C18F4A93D705BE21642"
TERMINAL="G15_PARETO_MINIMAL_FAITHFUL_AND_CANONICAL_S4_PACKAGES_CLASSIFIED"
G15_CERT_SHA256="50ef864f0713d1f19ddf918dae2486a05a7e1d52bf538f1603b2d1c6c655281e"

R=("I_CA","I_HC","I_HA","ADD_H")
C=("K4_ADJ","TETRA_CA","H_C3X3","PROJECTIVE_HC","PAIR_AXIS_HA")
RM={"I_CA":(2,False),"I_HC":(2,True),"I_HA":(2,True),"ADD_H":(3,True)}
REQ={
 "K4_ADJ":(set(),set()),
 "TETRA_CA":({"I_CA"},set()),
 "H_C3X3":({"ADD_H"},set()),
 "PROJECTIVE_HC":({"ADD_H","I_HC"},{"H_C3X3"}),
 "PAIR_AXIS_HA":({"ADD_H","I_HC","I_HA"},{"H_C3X3","PROJECTIVE_HC"}),
}
SPEC_COUNTS={
 "NO_LIFT_P4":30,
 "UNIVERSAL_SPLIT_CANONICAL_FIXED_POINT":12,
 "NO_LIFT_UNCONSTRAINED_I_CA":6,
 "NO_LIFT_UNCONSTRAINED_I_HC":24,
 "NO_LIFT_UNCONSTRAINED_I_HA_ON_TETRA_AXIS":6,
 "SURJECTIVE_NONSPLIT_GL23":12,
}
CLASS_COUNTS={
 "NO_LIFT_P4":30,
 "UNIVERSAL_SPLIT_CANONICAL_FIXED_POINT":9,
 "NO_LIFT_UNCONSTRAINED_I_CA":6,
 "NO_LIFT_UNCONSTRAINED_I_HC":18,
 "NO_LIFT_UNCONSTRAINED_I_HA_ON_TETRA_AXIS":3,
 "SURJECTIVE_NONSPLIT_GL23":9,
}
def A(x,m):
    if not x: raise AssertionError(m)
def valid(rs,cs):
    return all(rr<=rs and cc<=cs for c in cs for rr,cc in [REQ[c]])
def packages():
    out=[]
    for rm in range(16):
        rs=frozenset(R[i] for i in range(4) if rm>>i&1)
        for cm in range(32):
            cs=frozenset(C[i] for i in range(5) if cm>>i&1)
            if valid(set(rs),set(cs)): out.append((rm,cm,rs,cs))
    return out
def key(rs,cs):
    # Frozen G15 D1: TETRA_CA parameter-free defines complete K4 adjacency.
    cs=set(cs)
    if "TETRA_CA" in cs: cs.discard("K4_ADJ")
    return tuple(x for x in R if x in rs),tuple(x for x in C if x in cs)
def cost(rs,cs):
    h=any(RM[x][1] for x in rs); a={1:0,2:0,3:0}
    for x in rs:a[RM[x][0]]+=1
    return (int(h),len(rs),a[1],a[2],a[3],int(h),len(cs),0)
def classify(rs,cs):
    rs,cs=set(rs),set(cs)
    base=("K4_ADJ" in cs) or ("TETRA_CA" in cs)
    if not base:
        return "NO_LIFT_P4","GEN13_P4_NO_LIFT",False,False
    if "PROJECTIVE_HC" in cs:
        return "SURJECTIVE_NONSPLIT_GL23","GEN13_GL23_SURJECTIVE_NONSPLIT",False,False
    if "I_HC" in rs:
        return "NO_LIFT_UNCONSTRAINED_I_HC","SINGLETON_I_HC_CELL_STABILIZER",False,False
    if "I_CA" in rs and "TETRA_CA" not in cs:
        return "NO_LIFT_UNCONSTRAINED_I_CA","SINGLETON_I_CA_CELL_STABILIZER",False,False
    if "TETRA_CA" in cs and "I_HA" in rs:
        return "NO_LIFT_UNCONSTRAINED_I_HA_ON_TETRA_AXIS","SINGLETON_I_HA_AXIS_STABILIZER",False,False
    return "UNIVERSAL_SPLIT_CANONICAL_FIXED_POINT","DIRECT_TYPED_FACTOR_SECTION",True,True
def dom(a,b): return a!=b and all(x<=y for x,y in zip(a,b))
def comp(p,q):return tuple(p[q[i]] for i in range(len(p)))
def inv(p):
    q=[0]*len(p)
    for i,j in enumerate(p):q[j]=i
    return tuple(q)
def auts(n,edges):
    E={tuple(sorted(e)) for e in edges}
    return [p for p in permutations(range(n))
            if {tuple(sorted((p[i],p[j]))) for i,j in E}==E]
def k4():return set(combinations(range(4),2))
def p4():return {(0,1),(1,2),(2,3)}
def k2222():
    f=(0,0,1,1,2,2,3,3)
    return {(i,j) for i,j in combinations(range(8),2) if f[i]!=f[j]}
def tetra():
    pairs=list(combinations(range(4),2)); idx={p:i for i,p in enumerate(pairs)}
    inc={(c,a) for a,p in enumerate(pairs) for c in p}; aa=[]
    for pc in permutations(range(4)):
        pa=tuple(idx[tuple(sorted((pc[i],pc[j])))] for i,j in pairs)
        aa.append((pc,pa))
    return pairs,inc,aa

# Exact GL(2,3)->PGL(2,3) residue regression.
MOD=3; MI=((1,0),(0,1)); MN=((2,0),(0,2))
LINES=((1,0),(0,1),(1,1),(1,2)); LIDX={v:i for i,v in enumerate(LINES)}
PID=tuple(range(4)); AP=(0,2,3,1); BP=(1,0,2,3)
def det(M):return (M[0][0]*M[1][1]-M[0][1]*M[1][0])%MOD
def mm(A_,B_):
    return tuple(tuple(sum(A_[i][k]*B_[k][j] for k in range(2))%MOD for j in range(2)) for i in range(2))
def mp(A_,n):
    z=MI
    for _ in range(n):z=mm(z,A_)
    return z
def GL():
    z=[]
    for v in product(range(3),repeat=4):
        M=((v[0],v[1]),(v[2],v[3]))
        if det(M):z.append(M)
    return z
def cl(v):
    x,y=v[0]%3,v[1]%3
    if x==0:return (0,1)
    return (1,y*(1 if x==1 else 2)%3)
def pact(M):
    return tuple(LIDX[cl(((M[0][0]*x+M[0][1]*y)%3,(M[1][0]*x+M[1][1]*y)%3))] for x,y in LINES)

# Exact C2 wr S4 section/fixed-point regression.
ZERO=(0,0,0,0)
def av(p,w):
    pi=inv(p);return tuple(w[pi[i]] for i in range(4))
def xv(a,b):return tuple(x^y for x,y in zip(a,b))
def wm(g,h):
    v,p=g;w,q=h;return xv(v,av(p,w)),comp(p,q)
WE=(ZERO,PID)
def wp(g,n):
    z=WE
    for _ in range(n):z=wm(z,g)
    return z
def wi(g):
    v,p=g;pi=inv(p);return av(pi,v),pi
def wc(k,g):return wm(wm(k,g),wi(k))
def wreath():
    la=[(v,AP) for v in product((0,1),repeat=4)]
    lb=[(v,BP) for v in product((0,1),repeat=4)]
    pairs=[];res=set()
    for a in la:
        for b in lb:
            res.add((wp(a,3)[0],wp(b,2)[0],wp(wm(a,b),4)[0]))
            if wp(a,3)==WE and wp(b,2)==WE and wp(wm(a,b),4)==WE:pairs.append((a,b))
    K=[(v,PID) for v in product((0,1),repeat=4)]; idx={p:i for i,p in enumerate(pairs)}
    unseen=set(range(len(pairs))); os=[]
    while unseen:
        i=next(iter(unseen));a,b=pairs[i]
        o={idx[(wc(k,a),wc(k,b))] for k in K if (wc(k,a),wc(k,b)) in idx}
        os.append(len(o));unseen-=o
    fx=sum(1 for a,b in pairs if all(wc(k,a)==a and wc(k,b)==b for k in K))
    return len(res),len(pairs),sorted(os),fx

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--selftest-no-repo",action="store_true")
    x=ap.parse_args();checks=0
    root=Path(__file__).resolve().parents[1]
    if not x.selftest_no_repo:
        g=root/"research_artifacts/P000_S4_RELATIONAL_MINIMALITY_GRAMMAR_V15/GRAMMAR_CERTIFICATE.json"
        art=root/"research_artifacts/P000_G15_PARETO_MINIMAL_S4_PACKAGES_V16/CLASSIFICATION_CERTIFICATE.json"
        A(g.exists(),"missing G15 cert")
        A(hashlib.sha256(g.read_bytes()).hexdigest()==G15_CERT_SHA256,"G15 hash drift")
        checks+=2
    P=packages();A(len(P)==90,"package count");checks+=1
    keys=sorted({key(rs,cs) for _,_,rs,cs in P});A(len(keys)==75,"quotient count")
    ids={k:f"G15C{i+1:03d}" for i,k in enumerate(keys)}
    A(ids[((),("K4_ADJ",))]=="G15C002","K4 class id");checks+=2
    T=[p for p in P if "TETRA_CA" in p[3]]
    A(len(T)==30 and sum("K4_ADJ" in p[3] for p in T)==15,"tetra/K4 redundancy");checks+=1
    A(Counter(classify(rs,cs)[0] for _,_,rs,cs in P)==Counter(SPEC_COUNTS),"raw partition");checks+=1
    G=defaultdict(list)
    for p in P:G[key(p[2],p[3])].append(p)
    lab={};mc={}
    for k,ms in G.items():
        ls={classify(p[2],p[3])[0] for p in ms};A(len(ls)==1,"class invariance")
        lab[k]=next(iter(ls));cc=[cost(p[2],p[3]) for p in ms];m=min(cc)
        A(all(all(a<=b for a,b in zip(m,c)) for c in cc),"class minimal rep");mc[k]=m
    A(Counter(lab.values())==Counter(CLASS_COUNTS),"class partition");checks+=2+2*len(G)
    pos=[k for k,v in lab.items() if v=="UNIVERSAL_SPLIT_CANONICAL_FIXED_POINT"];A(len(pos)==9,"positive classes")
    fr=[k for k in pos if not any(dom(mc[j],mc[k]) for j in pos if j!=k)]
    A(fr==[((),("K4_ADJ",))],"frontier");A(mc[fr[0]]==(0,0,0,0,0,0,1,0),"frontier cost");checks+=3
    # deletion and positive finite regressions
    A(valid(set(),set()) and len(auts(4,p4()))==2,"K4 deletion/P4");A(len(auts(4,k4()))==24,"K4 Aut");checks+=2
    pairs,inc,ta=tetra();A(len(ta)==24,"tetra Aut")
    ind={(c,d) for c,d in combinations(range(4),2) if any((c,a) in inc and (d,a) in inc for a in range(6))}
    A(ind==k4(),"tetra=>K4");checks+=2
    # singleton relation symmetry-breaks
    cellfix=[p for p in permutations(range(4)) if p[0]==0];A(len(cellfix)==6,"cell singleton stabilizer")
    A(len([pc for pc,pa in ta if pa[0]==0])==4,"axis singleton stabilizer");checks+=2
    # GL23 nonsplit
    gl=GL();acts={pact(M) for M in gl};ker=[M for M in gl if pact(M)==PID]
    la=[M for M in gl if pact(M)==AP];lb=[M for M in gl if pact(M)==BP]
    A(len(gl)==48 and len(acts)==24 and set(ker)=={MI,MN},"GL/PGL")
    A(len(la)==len(lb)==2 and all(mp(mm(a,b),4)==MN for a in la for b in lb),"GL23 residue");checks+=2
    # C2 wr S4 regression
    A(len(auts(8,k2222()))==384,"wreath Aut");A(wreath()==(16,16,[8,8],0),"wreath sections");checks+=2
    if not x.selftest_no_repo:
        d=json.loads(art.read_text())
        A(d["task_id"]==TASK_ID and d["publication_id"]==PUBLICATION_ID,"artifact identity")
        A(d["terminal_class"]==TERMINAL,"artifact terminal")
        A(d["enumeration"]=={"raw_packages":90,"definitional_classes":75,"positive_raw_packages":12,"positive_classes":9},"artifact counts")
        A(d["classification_spec_counts"]==SPEC_COUNTS and d["classification_class_counts"]==CLASS_COUNTS,"artifact partitions")
        A(d["faithful_pareto_frontier"]==[{"class_id":"G15C002","relations":[],"constraints":["K4_ADJ"],"cost":[0,0,0,0,0,0,1,0]}],"artifact faithful frontier")
        A(d["canonical_fixed_point_pareto_frontier"]==d["faithful_pareto_frontier"],"artifact canonical frontier")
        checks+=6
    print("PASS")
    print(f"task={TASK_ID}")
    print(f"publication={PUBLICATION_ID}")
    print(f"terminal={TERMINAL}")
    print("raw_packages=90")
    print("definitional_classes=75")
    print("universal_split_specs=12")
    print("universal_split_classes=9")
    print("faithful_pareto_frontier=G15C002:{K4_ADJ}")
    print("canonical_fixed_point_pareto_frontier=G15C002:{K4_ADJ}")
    print(f"checks={checks}")
if __name__=="__main__":main()
