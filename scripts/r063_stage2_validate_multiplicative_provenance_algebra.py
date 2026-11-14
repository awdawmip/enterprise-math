#!/usr/bin/env python3
"""R063 Stage 2 exact multiplicative provenance/root/trace/path checker."""
from __future__ import annotations
import argparse, hashlib, json, runpy, subprocess, tempfile
from collections import Counter
from functools import lru_cache
from itertools import product
from math import comb, isqrt
from pathlib import Path

TASK="RS-R063-STAGE2-MULTIPLICATIVE-PATH-NORM-ROOT-PROVENANCE-ALGEBRA"
TASKBOOK="74cacc89ec09a8af7dd7ff01c10f2baf082daf81"
S1HEAD="65f4e98cd707c634d805f2a9ec7c41f24ab06185"
S1ACCEPT="fb2331b0602e74cae506ebac49c4582e7147479d"
RID="EM-R063S2-52118B"
BASE=(1,2,5,13,17,25,65); UNITS=((1,0),(0,1),(-1,0),(0,-1))
SPARSE=((1_000_000,1_000_000),(3_000_000,1_000_000),(3_000_000,3_000_000),
        (6_000_000,1_000_000),(5_000_000,2_000_000),(7_000_000,1_000_000))
FINAL="MULTIPLICATIVE_PATH_NORM_ROOT_PROVENANCE_TOWER_CLASSIFIED_WITH_UNIT_QUOTIENT_MONOID_ORIENTATION_CONDITIONAL_TRACE_PRODUCT_AND_CHOICE_FREE_PATH_LIFT_NO_GO"
S1=None

def cj(x): return json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=False)
def sh(x): return hashlib.sha256(cj(x).encode()).hexdigest()
def put(p,x): p.write_text(cj(x)+"\n",encoding="utf-8")

def load_s1(path):
    holder=None
    if path is None:
        q=Path(__file__).with_name("r063_stage1_validate_general_path_norm_root.py")
        if not q.exists():
            root=Path(__file__).resolve().parents[1]
            git=lambda *a: subprocess.check_output(["git","-C",str(root),*a],text=True)
            names=git("ls-tree","-r","--name-only",S1HEAD,"--","scripts/r063_stage1_validate_general_path_norm_root.py","scripts/r063_stage1_checker_parts").splitlines()
            holder=tempfile.TemporaryDirectory(prefix="r063s2-s1-"); td=Path(holder.name)
            for rel in names:
                if not (rel.endswith(".py") or rel.endswith(".inc")): continue
                t=td/rel; t.parent.mkdir(parents=True,exist_ok=True); t.write_text(git("show",f"{S1HEAD}:{rel}"),encoding="utf-8")
            q=td/"scripts/r063_stage1_validate_general_path_norm_root.py"
        path=q
    ns=runpy.run_path(str(path),run_name="r063_stage1_frozen_dependency")
    if holder: ns["_holder"]=holder
    need=("factor_integer","support_from_factors","gaussian_signed_root_channels","split_prime_gaussian","gmul","gconj","gpow","r2_from_factorization")
    miss=[k for k in need if k not in ns]
    if miss: raise RuntimeError(f"frozen Stage1 loader missing {miss}")
    return ns

@lru_cache(None)
def fac(n): return S1["factor_integer"](n)
@lru_cache(None)
def ok(n): return bool(S1["support_from_factors"](fac(n)))
@lru_cache(None)
def sroots(n): return tuple(sorted(S1["gaussian_signed_root_channels"](n,detailed=False)[0]))
@lru_cache(None)
def groot(n): return tuple(z for z in sroots(n) if z[0]>=0 and z[1]>=0)
def orb(z):
    a,b=z; return ((a,b),(-b,a),(-a,-b),(b,-a))
def okey(z): return min(orb(z))
@lru_cache(None)
def uroot(n): return tuple(sorted({okey(z) for z in sroots(n)}))
@lru_cache(None)
def splits(n): return tuple((p,e,S1["split_prime_gaussian"](p)) for p,e in sorted(fac(n).items()) if p%4==1)
def fstr(n): return "*".join(str(p) if e==1 else f"{p}^{e}" for p,e in sorted(fac(n).items())) or "1"

def umul(i,j): return UNITS.index(S1["gmul"](UNITS[i],UNITS[j]))
@lru_cache(None)
def prov(n):
    if not ok(n): return ()
    pe=[(p,e) for p,e,_ in splits(n)]; rr=[range(e+1) for _,e in pe]
    return tuple((u,tuple((p,t) for (p,e),t in zip(pe,a))) for a in (product(*rr) if rr else [()]) for u in range(4))

def evalp(n,P):
    u,a=P; am=dict(a); z=(1,0); gm,gp,gc=S1["gmul"],S1["gpow"],S1["gconj"]
    for p,e in sorted(fac(n).items()):
        if p==2: z=gm(z,gp((1,1),e))
        elif p%4==1:
            pi=S1["split_prime_gaussian"](p); t=am[p]; z=gm(gm(z,gp(pi,t)),gp(gc(pi),e-t))
        else: z=gm(z,(p**(e//2),0))
    return gm(UNITS[u],z)

def mulp(A,B,P,Q):
    u,a=P; v,b=Q; da,db=dict(a),dict(b)
    return umul(u,v),tuple((p,da.get(p,0)+db.get(p,0)) for p,e,pi in splits(A*B))

def mp(a,b,t): return max(0,min(a,t)-max(0,t-b)+1)
def pre(A,B,T,unit=True):
    x=4 if unit else 1
    for p,t in T[1]: x*=mp(fac(A).get(p,0),fac(B).get(p,0),t)
    return x

def star(r,s):
    a,b=r; c,d=s; x=a*c-b*d; y=a*d+b*c
    return (x,y) if x>=0 else (y,-x)
def sw(r): return r[1],r[0]
def starj(r,s): return sw(star(sw(r),sw(s)))
def pc(r): return comb(r[0]+r[1],r[0])

def brute(n):
    out=[]
    for a in range(isqrt(n)+1):
        b=isqrt(n-a*a)
        if b*b==n-a*a: out.append((a,b))
    return tuple(sorted(out))

def row(A,B,expand_path=True):
    T=prov(A*B); supported=ok(A) and ok(B)
    vals=[pre(A,B,t) for t in T] if supported else []
    GA,GB,GT=groot(A),groot(B),groot(A*B); idx={r:i for i,r in enumerate(GT)}
    tm=[idx[star(r,s)] for r in GA for s in GB] if supported else []
    path=-1
    if supported and expand_path:
        path=1 if all(pc(star(r,s))==pc(r)*pc(s) for r in GA for s in GB) else 0
    return [A,B,A*B,len(T) if supported else 0,len(T),min(vals) if vals else 0,max(vals) if vals else 0,
            sum(vals),len(prov(A))*len(prov(B)) if supported else 0,1 if supported else 0,path,tm]

def normrec(n):
    card=lambda r: pc(r) if r[0]+r[1]<=4096 else f"binom({r[0]+r[1]},{r[0]})"
    return [n,fstr(n),1 if ok(n) else 0,S1["r2_from_factorization"](n),[list(x) for x in uroot(n)],[[a,b,card((a,b))] for a,b in groot(n)]]

def run(args):
    global S1; S1=load_s1(args.stage1_loader); out=args.out; out.mkdir(parents=True,exist_ok=True)
    bad=[]; checks={}
    anchors=(1,2,5,13,17,25,65,2500)
    for n in anchors:
        if groot(n)!=brute(n) or len(sroots(n))!=S1["r2_from_factorization"](n): bad.append(["s1",n])
    checks["R063_STAGE1_FROZEN_DEPENDENCY_REPLAY_INTACT"]=not bad
    for n in set(BASE+anchors):
        if ok(n):
            vv=[evalp(n,p) for p in prov(n)]
            if len(vv)!=len(set(vv)) or set(vv)!=set(sroots(n)): bad.append(["evbij",n])
    checks["PROV_EVALUATION_BIJECTION_STAGE1"]=not any(x[0]=="evbij" for x in bad)
    uc=[sum(umul(i,j)==t for i in range(4) for j in range(4)) for t in range(4)]
    checks["SIGNED_TARGET_UNIT_PAIR_FACTOR_IS_FOUR"]=uc==[4]*4
    maxe=max([0]+[e for n in range(1,args.max_pair+1) for p,e in fac(n).items() if p%4==1]); lc=0
    for a in range(maxe+1):
      for b in range(maxe+1):
       for t in range(a+b+1):
        lc+=1; direct=sum(i+j==t for i in range(a+1) for j in range(b+1))
        if mp(a,b,t)!=direct: bad.append(["mp",a,b,t])
    checks["LOCAL_PREIMAGE_FORMULA_EXACT"]=not any(x[0]=="mp" for x in bad)
    base=[]
    for A in BASE:
      for B in BASE:
        rr=row(A,B); base.append(rr)
        if not(ok(A) and ok(B)): continue
        cnt=Counter()
        for P in prov(A):
          for Q in prov(B):
            T=mulp(A,B,P,Q); cnt[T]+=1
            if evalp(A*B,T)!=S1["gmul"](evalp(A,P),evalp(B,Q)): bad.append(["evalmul",A,B])
        if set(cnt)!=set(prov(A*B)): bad.append(["surj",A,B])
        if any(cnt[t]!=pre(A,B,t) for t in prov(A*B)): bad.append(["pre",A,B])
    checks["PROVENANCE_MULTIPLICATION_EVALUATION_SURJECTIVITY_BASE"]=not any(x[0] in("evalmul","surj") for x in bad)
    checks["GLOBAL_SIGNED_PREIMAGE_FORMULA_BASE"]=not any(x[0]=="pre" for x in bad)
    norms=sorted(set(range(1,args.max_pair+1))|{a*b for a in range(1,args.max_pair+1) for b in range(1,args.max_pair+1)})
    for n in norms:
        if not ok(n): continue
        fib=Counter(okey(r) for r in groot(n)); sq=isqrt(n)**2==n
        if len(groot(n))!=len(uroot(n))+(1 if sq else 0) or sum(v==2 for v in fib.values())!=(1 if sq else 0): bad.append(["orbit",n])
    checks["UNIT_ORBIT_TO_GROOT_FIBRE_CLASSIFIED"]=not any(x[0]=="orbit" for x in bad)
    for A in BASE:
      for B in BASE:
       if ok(A) and ok(B):
        for z in sroots(A):
         for w in sroots(B):
          k=okey(S1["gmul"](z,w))
          if any(okey(S1["gmul"](uz,uw))!=k for uz in orb(z) for uw in orb(w)): bad.append(["uq",A,B])
    checks["UNIT_QUOTIENT_PRODUCT_WELL_DEFINED"]=not any(x[0]=="uq" for x in bad)
    R=sorted({r for n in range(1,min(args.max_pair,32)+1) for r in groot(n)})
    for r in R:
      if star((1,0),r)!=r: bad.append(["starid",r])
      for s in R:
        if star(r,s)!=star(s,r) or okey(star(r,s))!=okey(S1["gmul"](r,s)): bad.append(["star2",r,s])
    for r in R:
      for s in R:
       for t in R:
        if star(star(r,s),t)!=star(r,star(s,t)): bad.append(["starassoc",r,s,t]); break
    checks["ORIENTED_COMPONENT_PRODUCT_MONOID_EXACT_BOUNDED"]=not any(x[0].startswith("star") for x in bad)
    oi,oj=star((1,1),(1,1)),starj((1,1),(1,1)); checks["MANDATORY_2X2_COMPONENT_DISCRIMINATOR"]=(oi==(0,2) and oj==(2,0))
    rows=[]; first_path=None
    for A in range(1,args.max_pair+1):
      for B in range(1,args.max_pair+1):
        rr=row(A,B); rows.append(rr)
        if rr[9] and (rr[3]!=rr[4] or rr[7]!=rr[8]): bad.append(["pair",A,B])
        if rr[9]:
          for r in groot(A):
           for s in groot(B):
            t=star(r,s)
            if t not in groot(A*B): bad.append(["closure",A,B,r,s])
            if first_path is None and pc(t)!=pc(r)*pc(s): first_path=[A,B,list(r),list(s),list(t),pc(t),pc(r)*pc(s)]
    checks["EXHAUSTIVE_PAIR_REGRESSION_PASS"]=not any(x[0] in("pair","closure") for x in bad)
    checks["NATIVE_PATH_MULTIPLICITY_IS_NOT_MULTIPLICATIVE_UNDER_ROOT_PRODUCT"]=(first_path[:5]==[2,2,[1,1],[1,1],[0,2]])
    sparse=[row(A,B,False) for A,B in SPARSE]; checks["SPARSE_10E12_SCALE_REACHED"]=max(x[2] for x in sparse)>=10**12
    for A in BASE:
      for B in BASE:
       for C in (1,2,5,13):
        for P in (prov(A)[0],prov(A)[-1]):
         for Q in (prov(B)[0],prov(B)[-1]):
          for R0 in (prov(C)[0],prov(C)[-1]):
           if mulp(A*B,C,mulp(A,B,P,Q),R0)!=mulp(A,B*C,P,mulp(B,C,Q,R0)): bad.append(["pa",A,B,C])
           if mulp(A,B,P,Q)!=mulp(B,A,Q,P): bad.append(["pc",A,B])
    checks["PROVENANCE_ASSOCIATIVE_COMMUTATIVE_IDENTITY"]=not any(x[0] in("pa","pc") for x in bad)
    perA=[[A,sh(rows[(A-1)*args.max_pair:A*args.max_pair])] for A in range(1,args.max_pair+1)]
    ncat=[normrec(n) for n in sorted(set(norms)|{x for A,B in SPARSE for x in(A,B,A*B)})]
    nblocks=[[ncat[i][0],ncat[min(i+127,len(ncat)-1)][0],sh(ncat[i:i+128])] for i in range(0,len(ncat),128)]
    reg={"schema":"R063_STAGE2_REGRESSION_V3_PROCEDURAL_EXACT_REPLAY","task_id":TASK,"max_pair":args.max_pair,
         "contract":"all ordered rows and norm records are materialized exactly by this checker; publication stores full and block hashes plus samples/sparse rows for exact replay",
         "pair_columns":["A","B","AB","prov_image","prov_target","pre_min","pre_max","pre_total","domain_pairs","supported_domain","path_mult_code","trace_target_indices"],
         "norm_columns":["N","factorization","support","signed_count","unit_orbit_roots","groot_with_path_cardinality"],
         "ordered_pair_count":len(rows),"rows_sha256":sh(rows),"per_A_128_row_sha256":perA,
         "norm_count":len(ncat),"norm_sha256":sh(ncat),"norm_128_block_sha256":nblocks,
         "samples":[rows[(A-1)*args.max_pair+B-1] for A,B in((1,1),(2,2),(3,3),(5,5),(13,17),(65,65))],"sparse":sparse,"checks":checks}
    p25=next(T for T in prov(25) if evalp(25,T)==(3,4))
    mult={"schema":"R063_STAGE2_MULTIPLICITY_SEPARATION_CERTIFICATE_V1",
          "mandatory_2x2":{"derivation_pairs":4,"source_path_pairs":4,"target_root":[0,2],"target_paths":1,"additive_trace_target":[2,2],"additive_target_paths":6},
          "witness_5x5":{"root":[2,1],"target":[3,4],"signed_target_preimages":pre(5,5,p25),"source_path_pairs":9,"target_paths":35},
          "smallest_path_counterexample":first_path,"orientation":{"star_i":[0,2],"star_j":[2,0],"same_unit_orbit":True},
          "uroot_bijection_minimal_counterexample":{"N":1,"GRoot":[[0,1],[1,0]],"URoot_count":1},
          "layers":["signed-root channel","fixed-target provenance preimage","unit orbit","ordered GRoot/trace","native path multiplicity","N_BRC","Boolean support"]}
    provc={"schema":"R063_STAGE2_PROVENANCE_FIBER_COUNT_CERTIFICATE_V1","local_formula":"max(0,min(alpha,t)-max(0,t-beta)+1)",
           "signed_target_formula":"4*product_p m_p","uroot_target_formula":"product_p m_p","unit_pair_counts":uc,"local_cases":lc,
           "base_pair_rows_sha256":sh(base),"supported_domain_only":True,"unrestricted_boundary":{"A":3,"B":3,"AB":9,"Prov_A":0,"Prov_B":0,"Prov_AB":4}}
    mism={"schema":"R063_STAGE2_MISMATCHES_V1","mismatch_count":len(bad),"smallest_mismatch":bad[0] if bad else None,"mismatches":bad[:100]}
    put(out/"R063_STAGE2_PROVENANCE_FIBER_COUNT_CERTIFICATE.json",provc); put(out/"R063_STAGE2_MULTIPLICITY_SEPARATION_CERTIFICATE.json",mult)
    put(out/"R063_STAGE2_REGRESSION.json",reg); put(out/"R063_STAGE2_MISMATCHES.json",mism)
    summary={"status":"PASS" if not bad else "FAIL","task_id":TASK,"researcher_id":RID,"taskbook_source":TASKBOOK,"stage1_frozen_head":S1HEAD,"stage1_driver_acceptance":S1ACCEPT,"mismatch_count":len(bad),"checks":checks,"final_classification":FINAL,"semantic_boundary":"sector-local CONDITIONAL_DERIVED; no global full-plane Gaussian multiplication claim"}
    print(cj(summary)); return 0 if not bad else 1

def main():
    p=argparse.ArgumentParser(); p.add_argument("--stage1-loader",type=Path); p.add_argument("--out",type=Path,default=Path(__file__).resolve().parents[1]/"research_results/R063_STAGE2"); p.add_argument("--max-pair",type=int,default=128)
    return run(p.parse_args())
if __name__=="__main__": raise SystemExit(main())
