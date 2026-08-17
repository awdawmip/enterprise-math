#!/usr/bin/env python3
from fractions import Fraction
from collections import defaultdict
from itertools import product
import hashlib, json, pathlib, sys
import sympy as sp

ROOT=pathlib.Path(__file__).resolve().parent
EXPECTED_RID="EM-HODGE-H0G-6F3A12"
EXPECTED_TASK="RS-HODGE-H0G-ALGEBRAIC-DERHAM-FILTRATION-REPAIR-ATTRIBUTED-R2"

checks=[]
def check(cond,label,detail=None):
    checks.append({"label":label,"pass":bool(cond),"detail":detail})
    if not cond:
        raise AssertionError(f"{label}: {detail}")

def load(name):
    return json.loads((ROOT/name).read_text(encoding="utf-8"))

def add_vec(a,b,scale=Fraction(1)):
    out=defaultdict(Fraction)
    for k,v in a.items(): out[k]+=v
    for k,v in b.items(): out[k]+=scale*v
    return {k:v for k,v in out.items() if v}

def wedge1(a,b):
    out=defaultdict(Fraction)
    for (ba,ra,sa),ca in a.items():
        for (bb,rb,sb),cb in b.items():
            if ba=="dx" and bb=="dy": out[("dxy",ra+rb,sa+sb)] += ca*cb
            elif ba=="dy" and bb=="dx": out[("dxy",ra+rb,sa+sb)] -= ca*cb
    return dict(out)

def multiply_scalar_form(scalar,form):
    out=defaultdict(Fraction)
    for (r,s),c in scalar.items():
        for (b,rb,sb),d in form.items():
            out[(b,r+rb,s+sb)] += c*d
    return dict(out)

charts=[(0,),(1,),(2,)]
pairs=[(0,1),(0,2),(1,2)]

def native_data(tag):
    if tag in [(0,), (0,1),(0,2),(0,1,2)]:
        def expmap(a,b): return {(a,b):Fraction(1)}
        return expmap,{("dx",0,0):Fraction(1)},{("dy",0,0):Fraction(1)}
    if tag in [(1,), (1,2)]:
        def expmap(a,b): return {(-(a+b),b):Fraction(1)}
        return expmap,{("dx",-2,0):Fraction(-1)},{
            ("dy",-1,0):Fraction(1),("dx",-2,1):Fraction(-1)}
    if tag==(2,):
        def expmap(a,b): return {(b,-(a+b)):Fraction(1)}
        return expmap,{("dy",0,-2):Fraction(-1)},{
            ("dx",0,-1):Fraction(1),("dy",1,-2):Fraction(-1)}
    raise ValueError(tag)

def native_exp_pairs(tag,B):
    if tag in charts: return list(product(range(B+1),repeat=2))
    if tag==(0,1): return [(a,b) for a in range(-B,B+1) for b in range(B+1)]
    if tag==(0,2): return [(a,b) for a in range(B+1) for b in range(-B,B+1)]
    if tag==(1,2): return [(a,b) for a in range(B+1) for b in range(-B,B+1)]
    if tag==(0,1,2): return list(product(range(-B,B+1),repeat=2))
    raise ValueError(tag)

def native_monomial_form(tag,a,b,q,basis_idx=0):
    expmap,d1,d2=native_data(tag)
    scalar=expmap(a,b)
    if q==0: return {("s",r,s):c for (r,s),c in scalar.items()}
    if q==1: return multiply_scalar_form(scalar,d1 if basis_idx==0 else d2)
    if q==2: return multiply_scalar_form(scalar,wedge1(d1,d2))
    return {}

def embed_component(p,tag,q,expr):
    return {(p,tag,q,b,r,s):c for (b,r,s),c in expr.items()}

def de_rham(expr):
    out=defaultdict(Fraction)
    for (b,r,s),c in expr.items():
        if b=="s":
            if r: out[("dx",r-1,s)] += c*r
            if s: out[("dy",r,s-1)] += c*s
        elif b=="dx":
            if s: out[("dxy",r,s-1)] -= c*s
        elif b=="dy":
            if r: out[("dxy",r-1,s)] += c*r
    return dict(out)

def delta_total_component(vec):
    out=defaultdict(Fraction)
    groups=defaultdict(lambda:defaultdict(Fraction))
    for (p,tag,q,b,r,s),c in vec.items(): groups[(p,tag,q)][(b,r,s)]+=c
    for (p,tag,q),expr in groups.items():
        if p==0:
            i=tag[0]
            for pair in pairs:
                if i in pair:
                    coeff=1 if i==pair[1] else -1
                    for (b,r,s),c in expr.items(): out[(1,pair,q,b,r,s)] += coeff*c
        elif p==1:
            coeff={(1,2):1,(0,2):-1,(0,1):1}[tag]
            for (b,r,s),c in expr.items(): out[(2,(0,1,2),q,b,r,s)] += coeff*c
    return {k:v for k,v in out.items() if v}

def d_total_component(vec):
    out=defaultdict(Fraction)
    groups=defaultdict(lambda:defaultdict(Fraction))
    for (p,tag,q,b,r,s),c in vec.items(): groups[(p,tag,q)][(b,r,s)]+=c
    for (p,tag,q),expr in groups.items():
        sign=Fraction(1 if p%2==0 else -1)
        for (b,r,s),c in de_rham(dict(expr)).items():
            out[(p,tag,q+1,b,r,s)] += sign*c
    return {k:v for k,v in out.items() if v}

def D(vec): return add_vec(delta_total_component(vec),d_total_component(vec))

def seed_vectors_total(n,B):
    seeds=[]
    for p in range(3):
        q=n-p
        if q<0 or q>2: continue
        tags={0:charts,1:pairs,2:[(0,1,2)]}[p]
        for tag in tags:
            for a,b in native_exp_pairs(tag,B):
                if q==0: seeds.append(embed_component(p,tag,0,native_monomial_form(tag,a,b,0)))
                elif q==1:
                    for bi in (0,1):
                        seeds.append(embed_component(p,tag,1,native_monomial_form(tag,a,b,1,bi)))
                elif q==2: seeds.append(embed_component(p,tag,2,native_monomial_form(tag,a,b,2)))
    return seeds

def canonical_span_basis(vecs):
    keys=sorted(set(k for v in vecs for k in v))
    if not vecs: return [],keys
    M=sp.Matrix([[sp.Rational(v.get(k,0).numerator,v.get(k,0).denominator)
                  for v in vecs] for k in keys])
    _,piv=M.rref()
    return [vecs[i] for i in piv],keys

def rank_vecs(vecs):
    return len(canonical_span_basis(vecs)[0])

def build_complex(B1,B2):
    K1,_=canonical_span_basis(seed_vectors_total(1,B1))
    D1=[D(v) for v in K1]
    K2,_=canonical_span_basis(seed_vectors_total(2,B2)+D1)
    D2=[D(v) for v in K2]
    k2keys=sorted(set(k for v in K2+D1 for k in v))
    lowkeys=[k for k in k2keys if k[0]==2 and k[2]==0]
    d2keys=sorted(set(k for v in D2 for k in v))
    M2=sp.Matrix([[sp.Rational(v.get(k,0).numerator,v.get(k,0).denominator)
                   for v in D2] for k in d2keys])
    ker=M2.nullspace()
    li={k:i for i,k in enumerate(lowkeys)}
    lowK=sp.zeros(len(lowkeys),len(K2)); lowD1=sp.zeros(len(lowkeys),len(K1))
    for j,v in enumerate(K2):
        for k,c in v.items():
            if k in li: lowK[li[k],j]=sp.Rational(c.numerator,c.denominator)
    for j,v in enumerate(D1):
        for k,c in v.items():
            if k in li: lowD1[li[k],j]=sp.Rational(c.numerator,c.denominator)
    Kerc=sp.Matrix.hstack(*ker) if ker else sp.zeros(len(K2),0)
    lowker=lowK*Kerc
    return dict(K1=K1,D1=D1,K2=K2,D2=D2,lowkeys=lowkeys,ker=ker,
                lowD1=lowD1,lowker=lowker,rankD2=M2.rank())

def key_to_str(k):
    p,tag,q,b,r,s=k
    return f"p{p}|I{''.join(map(str,tag))}|q{q}|{b}|{r}|{s}"

def vec_to_json(v):
    return [[key_to_str(k),f"{c.numerator}/{c.denominator}"]
            for k,c in sorted(v.items(),key=lambda kv:key_to_str(kv[0]))]

def hash_obj(obj):
    return hashlib.sha256(json.dumps(obj,sort_keys=True,separators=(",",":"),
                                     ensure_ascii=False).encode()).hexdigest()

def colspace_matrix(cols,nrows):
    if not cols: return sp.zeros(nrows,0)
    M=sp.Matrix.hstack(*cols)
    cs=M.columnspace()
    return sp.Matrix.hstack(*cs) if cs else sp.zeros(nrows,0)

def in_colspace(M,v):
    return M.rank()==sp.Matrix.hstack(M,v).rank()

def vec_in_span(vec,basis):
    keys=sorted(set(k for v in basis+[vec] for k in v))
    M=sp.Matrix([[sp.Rational(v.get(k,0).numerator,v.get(k,0).denominator)
                  for v in basis] for k in keys])
    x=sp.Matrix([sp.Rational(vec.get(k,0).numerator,vec.get(k,0).denominator) for k in keys])
    return M.rank()==sp.Matrix.hstack(M,x).rank()

# Exact algebraic automorphism pullbacks used only for D-equivariance stress.
def perm_sign(seq):
    inv=sum(1 for i in range(len(seq)) for j in range(i+1,len(seq)) if seq[i]>seq[j])
    return -1 if inv%2 else 1

def mapped_tag(tag,perm):
    vals=[perm[i] for i in tag]
    return tuple(sorted(vals)),perm_sign(vals)

def pullback_expr(expr,kind):
    if kind=="swap12":
        xexp=(0,1); yexp=(1,0)
        dxmap={("dy",0,0):Fraction(1)}
        dymap={("dx",0,0):Fraction(1)}
    elif kind=="cycle012":
        xexp=(-1,1); yexp=(-1,0)
        dxmap={("dy",-1,0):Fraction(1),("dx",-2,1):Fraction(-1)}
        dymap={("dx",-2,0):Fraction(-1)}
    else: raise ValueError(kind)
    out=defaultdict(Fraction)
    for (b,r,s),c in expr.items():
        rr=r*xexp[0]+s*yexp[0]; ss=r*xexp[1]+s*yexp[1]
        if b=="s": form={("s",0,0):Fraction(1)}
        elif b=="dx": form=dxmap
        elif b=="dy": form=dymap
        else: form=wedge1(dxmap,dymap)
        for (bb,a,b2),cf in form.items(): out[(bb,rr+a,ss+b2)] += c*cf
    return {k:v for k,v in out.items() if v}

def transform_total(vec,perm,kind):
    groups=defaultdict(lambda:defaultdict(Fraction))
    for (p,tag,q,b,r,s),c in vec.items(): groups[(p,tag,q)][(b,r,s)]+=c
    out=defaultdict(Fraction)
    for (p,tag,q),expr in groups.items():
        nt,sg=mapped_tag(tag,perm)
        for (b,r,s),c in pullback_expr(dict(expr),kind).items():
            out[(p,nt,q,b,r,s)] += Fraction(sg)*c
    return {k:v for k,v in out.items() if v}

def run():
    src=load("HODGE_H0G_CECH_DERHAM_SOURCE_SPEC.json")
    gen=load("HODGE_H0G_FINITE_SUBCOMPLEX_GENERATION.json")
    rep=load("HODGE_H0G_FILTRATION_REPAIR_REGISTRY.json")
    lang=load("HODGE_H0G_MULTISTEP_REPAIR_LANGUAGE.json")
    base=load("HODGE_H0G_SOURCE_BASELINE_SANDWICH.json")
    fq=load("HODGE_H0G_FUTURE_QUOTIENT_REGISTRY.json")
    obs=load("HODGE_H0G_OBSTRUCTION_REGISTRY.json")
    attr=load("HODGE_H0G_ATTRIBUTION_CERTIFICATE_REGISTRY.json")
    nat=load("HODGE_H0G_PRESENTATION_NATURALITY_LEDGER.json")
    rat=load("HODGE_H0G_RATIONAL_HODGE_BOUNDARY.json")
    r3=load("HODGE_H0G_R3_PRESEED.json")
    leak=load("HODGE_H0G_TARGET_LEAKAGE_LEDGER.json")
    clf=load("HODGE_H0G_CLASSIFICATION.json")

    check(src["researcher_id"]==EXPECTED_RID,"identity")
    check(src["task_id"]==EXPECTED_TASK,"task")
    check(src["finite_primary_window"]=={"repair_degree_window_B1":1,"state_degree_window_B2":2},
          "frozen-primary-window")

    eq=build_complex(1,1)
    P=build_complex(1,2)
    dim_eq=(len(eq["K1"]),len(eq["K2"]),rank_vecs(eq["D1"]),eq["rankD2"],
            len(eq["ker"]),eq["lowD1"].rank(),eq["lowker"].rank(),
            sp.Matrix.hstack(eq["lowD1"],eq["lowker"]).rank()-eq["lowD1"].rank())
    check(dim_eq==(42,76,33,42,34,9,9,0),"equal-window-source-control",dim_eq)

    dims=(len(P["K1"]),len(P["K2"]),rank_vecs(P["D1"]),P["rankD2"],len(P["ker"]),
          len(P["lowkeys"]),P["lowD1"].rank(),P["lowker"].rank(),
          sp.Matrix.hstack(P["lowD1"],P["lowker"]).rank()-P["lowD1"].rank())
    check(dims==(42,152,33,98,54,25,9,19,10),"primary-source-dimensions",dims)

    hashes={
      "K1_basis_sha256":hash_obj([vec_to_json(v) for v in P["K1"]]),
      "K2_basis_sha256":hash_obj([vec_to_json(v) for v in P["K2"]]),
      "D1_images_sha256":hash_obj([vec_to_json(v) for v in P["D1"]]),
      "D2_images_sha256":hash_obj([vec_to_json(v) for v in P["D2"]])
    }
    for k,v in hashes.items(): check(gen["digests"][k]==v,f"source-digest-{k}",v)

    for i,v in enumerate(P["K1"]): check(D(D(v))=={},f"D2-K1-{i}")
    for i,v in enumerate(P["K2"]): check(D(D(v))=={},f"D2-K2-{i}")

    # Low spaces.
    LZ=sp.Matrix.hstack(*P["lowker"].columnspace())
    low_exp=[(k[4],k[5]) for k in P["lowkeys"]]
    expected_lz=[tuple(x) for x in gen["low_closed_standard_monomial_exponents"]]
    expected_rep=[tuple(x) for x in gen["projected_repair_image_standard_monomial_exponents"]]
    expected_ob=[tuple(x) for x in gen["canonical_obstruction_complement_exponents"]]
    got_lz=[]; got_rep=[]
    Rall=sp.Matrix.hstack(*P["lowD1"].columnspace())
    for i,eexp in enumerate(low_exp):
        e=sp.zeros(25,1); e[i]=1
        if in_colspace(LZ,e): got_lz.append(eexp)
        if in_colspace(Rall,e): got_rep.append(eexp)
        check((eexp in expected_lz)==in_colspace(LZ,e),f"low-closed-membership-{eexp}")
        check((eexp in expected_rep)==in_colspace(Rall,e),f"repair-membership-{eexp}")
    check(got_lz==expected_lz,"low-closed-basis-list")
    check(got_rep==expected_rep,"repair-basis-list")
    check([e for e in got_lz if e not in got_rep]==expected_ob,"obstruction-complement-list")

    # Positive/negative controls.
    zplus={(2,(0,1,2),0,"s",0,0):Fraction(1)}
    bplus={(1,(1,2),0,"s",0,0):Fraction(-1)}
    zminus={(1,(1,2),1,"dx",-3,0):Fraction(2),(2,(0,1,2),0,"s",-2,0):Fraction(1)}
    check(vec_in_span(zplus,P["K2"]),"positive-control-in-K2")
    check(vec_in_span(bplus,P["K1"]),"positive-repair-in-K1")
    check(D(zplus)=={},"positive-control-closed")
    check(add_vec(zplus,D(bplus))=={},"positive-control-repaired-to-F1")
    check(vec_in_span(zminus,P["K2"]),"negative-control-in-K2")
    check(D(zminus)=={},"negative-control-closed")
    neg=sp.zeros(25,1); neg[low_exp.index((-2,0))]=1
    check(in_colspace(LZ,neg),"negative-low-is-closed-projection")
    check(not in_colspace(Rall,neg),"negative-low-not-repairable")

    # Repair blocks by pair.
    li={k:i for i,k in enumerate(P["lowkeys"])}
    def lowcol(v):
        col=sp.zeros(25,1)
        for k,c in v.items():
            if k in li: col[li[k]]=sp.Rational(c.numerator,c.denominator)
        return col
    repair={p:[] for p in pairs}
    for b,db in zip(P["K1"],P["D1"]):
        types={(k[0],k[1],k[2]) for k in b}
        if len(types)==1:
            p,tag,q=next(iter(types))
            if p==1 and q==0: repair[tag].append(lowcol(db))
    W={}
    for tag,cols in repair.items():
        W[tag]=colspace_matrix(cols,25)
        check(W[tag].rank()==6,f"repair-block-rank-{tag}")
    def span(*Ms):
        cols=[]
        for M in Ms: cols+=M.columnspace()
        return colspace_matrix(cols,25)
    Rs=[span(W[(1,2)],W[(0,1)],W[(0,2)]),span(W[(0,1)],W[(0,2)]),span(W[(0,2)])]
    check([M.rank() for M in Rs]==[9,8,6],"remaining-repair-ranks")
    check([19-M.rank() for M in Rs]==[10,11,13],"future-quotient-dims")
    check(sum([19,19,19])==fq["measure"]["source_total"],"raw-interface-measure")
    check(sum([10,11,13])==fq["measure"]["enterprise_total"],"quotient-interface-measure")
    for i,M in enumerate(Rs):
        check(M.rank()==lang["stage_records"][i]["remaining_repair_span_rank"],f"stage-source-rank-{i}")
        check(19-M.rank()==lang["stage_records"][i]["quotient_dim"],f"stage-quotient-rank-{i}")

    # Source normal form and attribution consistency.
    check(base["B_std_dR"]["independent_source_normal_form"]["obstruction_dim"]==10,"Bstd-obstruction-dim")
    check(base["B_std_dR"]["independent_source_normal_form"]["multistep_interfaces"]
          ==["L_Z/R0 dim10","L_Z/R1 dim11","L_Z/R2 dim13"],"Bstd-stage-quotients")
    for cert in attr["certificates"]:
        check(cert["attribution_status"]=="SOURCE_INHERITED_LEVERAGE",f"source-inherited-{cert['certificate_id']}")
        check(cert["R2_ATTRIBUTION_ADDENDUM_PASS"] is False,f"attribution-gate-false-{cert['certificate_id']}")

    # Algebraic P2 automorphism pullback commutes with D on ambient source formulas.
    for kind,perm in [("swap12",{0:0,1:2,2:1}),("cycle012",{0:1,1:2,2:0})]:
        for i,v in enumerate(P["K1"]):
            check(D(transform_total(v,perm,kind))==transform_total(D(v),perm,kind),
                  f"{kind}-D-equiv-K1-{i}")
        for i,v in enumerate(P["K2"]):
            check(D(transform_total(v,perm,kind))==transform_total(D(v),perm,kind),
                  f"{kind}-D-equiv-K2-{i}")
    check(nat["checks"][2]["result"]=="NOT_GLOBAL","finite-window-presentation-scope-warning")

    # Protocol/Hodge firewalls.
    check(rat["finite_carrier_to_C_H_map"]=="NOT_CONSTRUCTED","no-finite-C_H-map")
    check(rat["integral_substitution_forbidden"] is True,"no-integral-substitution")
    check(r3["status"]=="NO_R3_PRESEED","no-R3-preseed")
    check(r3["H1_admissible"] is False,"H1-blocked-r3")
    check(leak["status"]=="PASS","target-leakage-pass")
    check(clf["primary_disposition"]=="H0G_R1_SOURCE_COHOMOLOGICAL_NORMAL_FORM_ALREADY_COMPLETE",
          "final-disposition")
    check(clf["hard_target_result"]=="NOT_ESTABLISHED","hard-target-not-established")
    check(clf["R2_ATTRIBUTION_ADDENDUM_PASS"] is False,"classification-attribution-false")
    check(clf["R3_preseed"] is False and clf["H1_admissible"] is False and clf["Hodge_proved"] is False,
          "Hodge-firewall")
    check(clf["route_recommendation"]=="HODGE_FILTRATION_RECOGNITION_SOURCE_COMPLETE__PIVOT_TO_ALGEBRAIC_LIFTING",
          "route-decision")

    return {
      "schema":"HODGE_H0G_CHECKER_OUTPUT_V1",
      "researcher_id":EXPECTED_RID,
      "protocol_integrity":"PASS",
      "checks_total":len(checks),
      "checks_passed":sum(1 for c in checks if c["pass"]),
      "checks_failed":sum(1 for c in checks if not c["pass"]),
      "source_dimensions":{"K1":42,"K2":152,"rankD1":33,"rankD2":98,"Z2":54,
                           "low_closed":19,"repair_image":9,"obstruction":10},
      "future_interface":{"raw_total":57,"quotient_total":34,"stage_dims":[10,11,13]},
      "valid_meaning":"Protocol and exact finite-source consistency only; not a Hodge proof and not completeness of H_dR^2(P^2).",
      "CI":"CI_NOT_REQUIRED_FOR_RESEARCH"
    }

if __name__=="__main__":
    try:
        result=run()
        print(json.dumps(result,indent=2,sort_keys=True))
    except Exception as e:
        print(json.dumps({"schema":"HODGE_H0G_CHECKER_OUTPUT_V1","protocol_integrity":"FAIL",
                          "error":str(e),"checks_total":len(checks),
                          "checks_passed":sum(1 for c in checks if c["pass"])},
                         indent=2,sort_keys=True))
        sys.exit(1)
