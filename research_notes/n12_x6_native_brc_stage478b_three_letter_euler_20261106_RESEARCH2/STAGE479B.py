"""Stage479-B: Q-POP=1 exact native X6 three-letter fiber refinement.
Import STAGE478B.py in same folder; uses its exact three-letter Euler count.
"""
from itertools import product
from collections import defaultdict
from functools import lru_cache
import json
import STAGE478B as em
ABC="ABC"
N = em.count_euler if hasattr(em,"count_euler") else em.N
EDGES = em.directed_edges if hasattr(em,"directed_edges") else em.edges
THETA = em.theta_for_blocks if hasattr(em,"theta_for_blocks") else em.theta
SUB = em.sub if hasattr(em,"sub") else em.minus
ADD = em.add
E = em.edge
BASE = em.base_edges if hasattr(em,"base_edges") else em.base
COMPOSITIONS = em.compositions_capped if hasattr(em,"compositions_capped") else em.compositions

@lru_cache(None)
def mass_end(s,t,ew,T,u,m,c):
    # After one original Q POP the revealed terminal is H[-1]=c.
    left=SUB(T,ADD(BASE(m),E("A",s),ew,E(t,"A"),E(c,"A")))
    if any(v<0 for v in left):return 0
    ans=0
    for a in ABC:
        h=SUB(left,E("A",a))
        if all(v>=0 for v in h):ans+=N(u,a,c,h)
    return ans

def summaries(k,u,T):
    m=2*k+2;tot=cnt=typ=0
    room=SUB(T,BASE(m))
    if any(z<0 for z in room):return dict(classes=0,population=0,supported_types=0)
    for ew in COMPOSITIONS(room,k-1):
        for s in ABC:
            for t in ABC:
                nw=N(k,s,t,ew)
                if not nw:continue
                for c in ABC:
                    mass=mass_end(s,t,ew,T,u,m,c)
                    if mass:
                        cnt+=nw;tot+=nw*mass;typ+=1
    return dict(classes=cnt,population=tot,supported_types=typ)

def verify_small(k,u):
    m=2*k+2;fibers=defaultdict(lambda:defaultdict(int))
    for W0 in product(ABC,repeat=k):
        W="".join(W0)
        for H0 in product(ABC,repeat=u):
            H="".join(H0);T=THETA(m,W,H)
            fibers[T][(W,H[-1])]+=1
    checked=0
    for T,cs in fibers.items():
        got=summaries(k,u,T)
        assert got["classes"]==len(cs)
        assert got["population"]==sum(cs.values())
        for (W,c),real in cs.items():
            assert mass_end(W[0],W[-1],EDGES(W),T,u,m,c)==real
            checked+=1
    return dict(k=k,u=u,fibers=len(fibers),class_mass_checks=checked)

def run():
    k,u=1,3;m=2*k+2;W="B";H1="BAC";H2="CAB"
    T1=THETA(m,W,H1);T2=THETA(m,W,H2)
    assert T1==T2
    after1=SUB(T1,E(H1[-1],"A"))
    after2=SUB(T2,E(H2[-1],"A"))
    assert after1!=after2
    witness={"k":k,"u":u,"P":"A"*m,"W":W,"H1":H1,"H2":H2,
             "Q1":"A"*m+W+"A"+H1+"A","Q2":"A"*m+W+"A"+H2+"A",
             "theta_before":list(T1),"Q_POP1_after_edges_1":list(after1),
             "Q_POP1_after_edges_2":list(after2)}
    small=[verify_small(k,u) for k,u in
           [(1,1),(1,2),(2,1),(2,2),(1,3),(3,1),(2,3),(3,2)]]
    k,u=24,18;m=2*k+2
    W=("ABCCABCAAB"*5)[:k];H=("BCAACBBC"*5)[:u]
    T=THETA(m,W,H)
    large=summaries(k,u,T)
    old=em.summarize(k,u,T)
    assert large["population"]==old["population"]
    assert large["classes"]>=old["classes"]
    return {"status":"ALL_ASSERTIONS_PASSED",
            "repair_key":"(W,H[-1]) for Q POP<=1, APPEND<=1",
            "strict_witness":witness,"small_brute":small,
            "large":{"k":k,"u":u,"theta":list(T),**large,
                     "old_classes":old["classes"]},
            "arithmetic":"exact integers, predecessor directed Euler count reused"}

if __name__=="__main__":
    print(json.dumps(run(),ensure_ascii=False,indent=2))
