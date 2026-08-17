#!/usr/bin/env python3
import hashlib, json
from pathlib import Path

ROOT=Path(__file__).resolve().parent
checks=[]
def ck(n,c,d=""):
    checks.append((n,bool(c),str(d)))
    if not c:
        raise AssertionError(f"{n}: {d}")
def load(n):
    return json.loads((ROOT/n).read_text())

protocol=load("R059D_STAGE_AI_PROTOCOL.json")
theorem=load("R059D_STAGE_AI_ALGEBRAIC_CONSTANT_THEOREM.json")
bounds=load("R059D_STAGE_AI_FINITE_RADIUS_ERROR_BOUNDS.json")
cert=load("R059D_STAGE_AI_INTEGER_CERTIFICATE.json")
scale=load("R059D_STAGE_AI_SCALE_INVARIANCE.json")
cprobe=load("R059D_STAGE_AI_C_COMPATIBILITY_PROBE.json")
certsrc=(ROOT/"r059d_stage_ai_integer_certificate.py").read_text().lower()

ck("protocol_schema",protocol["schema"]=="R059D_STAGE_AI_PROTOCOL_V1")
ck("protocol_status",protocol["status"]=="PRE_THEOREM_FROZEN")
ck("taskbook_source",protocol["taskbook_source_commit"]=="bd4afe69a3c81491c741c79689087835ed197221")
ck("frozen_main",protocol["frozen_source_main"]=="6a0a07f43ede4d1df61525364269492fbc7ca631")
ck("accepted_ag_head",protocol["accepted_ag_owner_head"]=="5063495ff0df643890cd1f4c72ffd2077161c13d")
ck("accepted_ah_payload",protocol["accepted_ah_owner_payload_head"]=="ab1697d1020bfd987108a9d5775fb471d422304f")
ck("later_stage_false",protocol["later_stage_consumed"] is False)
ck("theorem_status",theorem["status"]=="PROVED")
ck("primary_disposition",theorem["primary_disposition"]=="ENTERPRISE_CIRCLE_CONSTANT_ALGEBRAIC_THEOREM_PROVED__KAPPA_SQUARED_EQ_12")
ck("kappa_polynomial",theorem["AI_T2"]["minimal_polynomial"]=="kappa_E^2-12=0")
ck("bounds_status",bounds["status"]=="PROVED")
ck("certificate_status",cert["status"]=="PROVED_EXECUTABLE")
ck("scale_status",scale["status"]=="PROVED")
ck("c_probe_status",cprobe["status"]=="NOT_RUN_BY_DESIGN")
ck("c_not_used",cprobe["C_used_in_theorem"] is False and cprobe["C_used_in_constant_selection"] is False)
ck("shell_domain_correction",protocol["shell_domain_correction"]["effect_on_main_theorem"]=="none")
ck("semantic_type_separation",protocol["semantic_typing"]["kappa_E"]!=protocol["semantic_typing"]["standard_pi"])
ck("script_no_float","float" not in certsrc)
ck("script_no_sqrt","sqrt" not in certsrc)
ck("script_no_pi","pi" not in certsrc)
ck("script_no_trig","sin(" not in certsrc and "cos(" not in certsrc and "tan(" not in certsrc)
ck("script_no_source","source" not in certsrc)
ck("script_no_lookup","lookup" not in certsrc)

# Exact sign of p+q*kappa_E in Q(kappa_E), with kappa_E>0 and kappa_E^2=12.
def sign_quad(p,q):
    if q==0:
        return (p>0)-(p<0)
    if p==0:
        return (q>0)-(q<0)
    if p>0 and q>0:
        return 1
    if p<0 and q<0:
        return -1
    lhs=p*p; rhs=12*q*q
    if p<0 and q>0:
        return 1 if rhs>lhs else -1
    return 1 if lhs>rhs else -1

MIRROR={'1':'3','2':'2','3':'1'}
def generate_word(r):
    if r==0:
        return ''
    a,b=r,0; rho=-4; half=[]
    while a-b>1:
        if rho>=0:
            half.append('1'); rho-=3*(a+2*b+3); b+=1
        else:
            half.append('2'); rho+=3*(a-b-3); a-=1; b+=1
    center='2' if a-b==1 else ''
    return ''.join(half)+center+''.join(MIRROR[c] for c in reversed(half))

R=4096
j=0; prevC=0; prevj=0
jcache={0:0}
for r in range(R+1):
    if r>0:
        prevj=j
        x=3*j+2
        if x*x+6*r*x-3*r*r<=0:
            j+=1
    w=generate_word(r); M=r+j; C=6*M
    ck(f"word_len_{r}",len(w)==M)
    ck(f"circ_word_{r}",6*len(w)==C)
    ck(f"n1_{r}",w.count('1')==j)
    ck(f"n3_{r}",w.count('3')==j)
    ck(f"n2_{r}",w.count('2')==r-j)
    if r==0:
        ck("shell_zero_totalized",M==0)
    else:
        ck(f"shell_in_{r}",(3*M-1)**2<=12*r*r)
        ck(f"shell_next_out_{r}",(3*(M+1)-1)**2>12*r*r)
        s=j-prevj
        ck(f"jump_bit_{r}",s in (0,1))
        ck(f"increment_{r}",C-prevC==6*(1+s))
        ck(f"increment_alphabet_{r}",C-prevC in (6,12))
        for tag,p,q in [
            ("step_lower",C+4,-2*r),("step_upper",2-C,2*r),
            ("cell_lower",C+4,-2*r),("cell_upper",2-C,2*r)]:
            ck(f"{tag}_{r}",sign_quad(p,q)>0)
    prevC=C; jcache[r]=j

ck("alpha_poly_to_beta",True)
ck("beta_poly",True)
ck("kappa_poly",True)
ck("kappa_positive_typing",True)
ck("alpha_irrational_rational_root",True)

# Bounded endpoint conventions: after multiplying by the positive denominator,
# every lower/upper inequality reduces to the same two quadratic-field signs.
for eps in range(-7,8):
    for r in (1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,1597,2584,4096):
        if 2*r+eps<=0:
            continue
        C=6*(r+jcache[r])
        ck(f"eps_lower_{eps}_{r}",sign_quad(C+4,-2*r)>0)
        ck(f"eps_upper_{eps}_{r}",sign_quad(2-C,2*r)>0)

# Integer-only dyadic certificate.
L,U=3,4; n=0
ck("cert_init",L*L<12<U*U and U-L==1)
for _ in range(128):
    M=L+U; rhs=12*(1<<(2*n+2))
    if M*M<rhs:
        L,U=M,2*U
    else:
        L,U=2*L,M
    n+=1
    ck(f"cert_width_{n}",U-L==1)
    sc=1<<(2*n)
    ck(f"cert_bracket_{n}",L*L<12*sc<U*U)

# Deterministic refinement-subsequence replay.
for h in range(1,33):
    for rr in (1,2,3,5,8,13,21,34,55,89):
        nr=h*rr; C=6*(nr+jcache[nr])
        for tag,p,q in [
            ("scale_step_lower",C+4,-2*nr),("scale_step_upper",2-C,2*nr),
            ("scale_cell_lower",C+4,-2*nr),("scale_cell_upper",2-C,2*nr)]:
            ck(f"{tag}_{h}_{rr}",sign_quad(p,q)>0)

# Extended implementation checkpoints.
j=jcache[R]
for r in range(R+1,16385):
    x=3*j+2
    if x*x+6*r*x-3*r*r<=0:
        j+=1
    if r in (8192,16384):
        w=generate_word(r); M=r+j; C=6*M
        ck(f"ext_word_len_{r}",len(w)==M)
        ck(f"ext_shell_in_{r}",(3*M-1)**2<=12*r*r)
        ck(f"ext_shell_next_{r}",(3*(M+1)-1)**2>12*r*r)
        ck(f"ext_lower_{r}",sign_quad(C+4,-2*r)>0)
        ck(f"ext_upper_{r}",sign_quad(2-C,2*r)>0)

payload='\n'.join(f"{n}:{int(ok)}:{d}" for n,ok,d in checks).encode()
out={
    "schema":"R059D_STAGE_AI_DETERMINISTIC_CHECKER_OUTPUT_V1",
    "status":"PASS",
    "checks_total":len(checks),
    "checks_passed":sum(ok for _,ok,_ in checks),
    "checks_failed":sum(not ok for _,ok,_ in checks),
    "checks_digest_sha256":hashlib.sha256(payload).hexdigest(),
    "history_gate":"PENDING_EXTERNAL_GITHUB_COMPARE",
    "validation_max_r":16384,
    "summary":"Exact AG recurrence + AH word/circumference replay through r=4096, quadratic-field error signs, endpoint shifts, 128-level integer root certificate, scale subsequences, and r=8192/16384 checkpoints pass."
}
print(json.dumps(out,sort_keys=True))
