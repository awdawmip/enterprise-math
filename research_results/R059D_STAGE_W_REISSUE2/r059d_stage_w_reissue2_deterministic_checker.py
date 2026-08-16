#!/usr/bin/env python3
from pathlib import Path
from itertools import product
from collections import defaultdict
import json, hashlib, math

R=Path(__file__).resolve().parent
RID="EM-R059D-9C6B2A"
PARENT="a9929a5bd666e621cb1bd77adb464df0d35db399"
TASK_BLOB="7ddaa1422786a39e5baa9fc2498298db6a28fa06"
C=[]

def ck(name, cond):
    C.append(name)
    if not cond:
        raise AssertionError(name)

def load(name):
    return json.loads((R/name).read_text())

req=[
"CELL_ID_SCAFFOLD","INTEGER_COORDINATE_SEMANTICS","FIRST_SHELL_SYMMETRY_AUDIT",
"EVENT_COUNT_LEDGER_PROTOCOL","PREDECLARED_ROOT_MODEL_REGISTRY","PURE_AXIS_RAY_TABLE",
"PRECOLLAPSE_PATH_INDEPENDENCE","MIXED_CELL_COMPLETION_LEDGER","ROOT_ORDER_SURVIVAL_LEDGER",
"FIVE_TO_FOUR_OR_NINE_CONTROL","FIRST_ROUND_W_NEGATIVE_CONTROL","TRIVIALITY_LEAKAGE_LEDGER"]
O={}
for x in req:
    O[x]=load("R059D_STAGE_W_REISSUE2_"+x+".json")
    ck("meta-"+x,O[x]["researcher_id"]==RID and O[x]["frozen_parent"]==PARENT)
    ck("task-"+x,O[x]["taskbook"]["git_blob_sha1"]==TASK_BLOB)

moves={"+u":(1,0),"-w":(1,-1),"+v":(0,-1),"-u":(-1,0),"+w":(-1,1),"-v":(0,1)}
axes=("u","v","w")
def dist(c):
    a,b=c
    return max(abs(a),abs(b),abs(a+b))
def add(c,d): return (c[0]+d[0],c[1]+d[1])
def endpoint(path):
    c=(0,0)
    for z in path:c=add(c,moves[z])
    return c
def ledger(path):
    cnt={(a,s):0 for a in axes for s in (1,-1)}
    for lab in path:
        cnt[(lab[1],1 if lab[0]=="+" else -1)]+=1
    D=[]
    split={}
    for a in axes:
        d=cnt[(a,1)]-cnt[(a,-1)]
        others=[x for x in axes if x!=a]
        qp=sum(cnt[(x,-1)] for x in others)
        qm=sum(cnt[(x,1)] for x in others)
        D.append(d); split[a]=(d,qp,qm,qp-qm)
    return tuple(D),split
def normD(D):
    m=min(D);M=max(D);rho=M-m
    return tuple(d-m for d in D),rho
def root_floor(n,p):
    k=0
    while (k+1)**p<=n:k+=1
    return k
def qopts(cell,p):
    a,b=cell;D=(a,-b,0);N,rho=normD(D)
    A=[]
    for x in N:
        c=rho-x;k=root_floor(c,p)
        if k**p==c:A.append((x-k,))
        else:A.append((x-k-1,x-k))
    return set(product(*A))
def cyc_cell(c):
    a,b=c;return (b,-a-b)
def cyc_coord(t):return (t[2],t[0],t[1])
def cells(rad):
    return [(a,b) for a in range(-rad,rad+1) for b in range(-rad,rad+1) if dist((a,b))<=rad]
def posray(c):
    a,b=c
    if a>0 and b==0:return ("+u",a)
    if a==0 and b<0:return ("+v",-b)
    if a<0 and b==-a:return ("+w",-a)
    return None
def filter_ray(c,opts):
    r=posray(c)
    if not r:return opts
    lab,_=r;out=set()
    for t in opts:
        if lab=="+u" and t[1]==t[2]:out.add(t)
        if lab=="+v" and t[0]==t[2]:out.add(t)
        if lab=="+w" and t[0]==t[1]:out.add(t)
    return out
def orbits(rad):
    cs=set(cells(rad));seen=set();out=[]
    for c in sorted(cs):
        if c in seen:continue
        o=[];x=c
        for _ in range(3):
            if x not in o:o.append(x)
            x=cyc_cell(x)
        seen.update(o);out.append(tuple(o))
    return out
def orbit_options(o,p):
    rep=o[0];res=[]
    for t in filter_ray(rep,qopts(rep,p)):
        asn={};tt=t;ok=True
        for x in o:
            if tt not in filter_ray(x,qopts(x,p)):ok=False;break
            asn[x]=tt;tt=cyc_coord(tt)
        if ok and len(set(asn.values()))==len(asn):res.append(asn)
    return res
def find_assignment(rad,p,forced=None):
    forced=forced or {}
    Q=[]
    for o in orbits(rad):
        z=[a for a in orbit_options(o,p) if all(c not in forced or a[c]==forced[c] for c in a)]
        if not z:return None
        Q.append((o,z))
    Q.sort(key=lambda z:len(z[1]))
    used=set();asn={}
    def rec(k):
        if k==len(Q):return dict(asn)
        _,opts=Q[k]
        for q in opts:
            vs=list(q.values())
            if any(v in used for v in vs):continue
            for c,v in q.items():asn[c]=v;used.add(v)
            r=rec(k+1)
            if r:return r
            for c,v in q.items():del asn[c];used.remove(v)
        return None
    return rec(0)
def digest(asn):
    rows=[(a,b,*asn[(a,b)]) for a,b in sorted(asn)]
    return hashlib.sha256(json.dumps(rows,separators=(",",":")).encode()).hexdigest()

S=O["CELL_ID_SCAFFOLD"]
ck("scaffold-moves",S["moves"]=={k:list(v) for k,v in moves.items()})
ck("ball61",S["ball_count"]==61)
ck("shells",S["shell_counts"]=={"0":1,"1":6,"2":12,"3":18,"4":24})
ck("rays6",set(S["pure_axis_rays_0_to_36"])==set(moves))
for lab,rows in S["pure_axis_rays_0_to_36"].items():
    ck("raylen-"+lab,len(rows)==37)
    for row in rows:
        n=row["n"]; v=moves[lab]
        ck("rayid-"+lab+str(n),row["id_index"]==[n*v[0],n*v[1]])
for z in S["relation_controls"]:
    if "paths" in z:
        e=[endpoint(p) for p in z["paths"]]
        ck("relation-"+str(z),e[0]==e[1]==tuple(z["same_endpoint"]))
    else:
        ck("loop-"+str(z),endpoint(z["loop"])==tuple(z["endpoint"]))

M=O["INTEGER_COORDINATE_SEMANTICS"]
ck("integer-only",M["types"]["INTEGER_CELL_COORDINATE"].endswith("every stored component integer."))
ck("hard-u",M["hard_observations"]["+u"]["stored"]==[1,-1,-1])
F=O["FIRST_SHELL_SYMMETRY_AUDIT"]
ck("minimal-underdetermined","UNDETERMINED" in F["minimal_control"]["other_first_neighbors"])
sym=F["symmetric_subcase_declaration"]
exp={"+u":[1,-1,-1],"+v":[-1,1,-1],"+w":[-1,-1,1],"-u":[-1,1,1],"-v":[1,-1,1],"-w":[1,1,-1]}
for k,v in exp.items():
    src=sym["cyclic_axis_relabeling"] if k[0]=="+" else sym["global_sign_inverted_first_shell"]
    ck("first-"+k,src[k]["stored"]==v)

G=O["PREDECLARED_ROOT_MODEL_REGISTRY"]
ck("models",set(G["models"])=={"N","S","H","Q","O"})
ck("root-orders",G["root_orders"]==[1,2,3,4,5,6])
ck("additions",G["model_addition_limit"]=={"allowed":2,"used":2,"further_additions_forbidden":True})
ck("no-homog-positive","NEGATIVE_TRIVIAL_CONTROL_ONLY"==G["models"]["H"]["role"])

def model_N(path,p):
    D,L=ledger(path);out=[]
    for a,d in zip(axes,D):
        q=L[a][3]
        out.append(("I",d) if q==0 else ("N",d,1 if q>0 else -1,abs(q),p))
    return tuple(out)
def model_H(path):
    D,_=ledger(path);s=sum(D)
    return tuple(2*d-s for d in D)
def qstate(path):
    D,_=ledger(path);N,rho=normD(D);return (N,rho)
for p in range(1,7):
    ck("N-relfail-"+str(p),model_N(("-w",),p)!=model_N(("+u","+v"),p))
    ck("Q-state-relation-"+str(p),qstate(("-w",))==qstate(("+u","+v")))
    ck("Q-state-triloop-"+str(p),qstate(())==qstate(("+u","+v","+w")))
ck("H-relfail",model_H(("-w",))!=model_H(("+u","+v")))
D1,L1=ledger(("+u",));D2,L2=ledger(("+u","+v","-v"))
ck("S-net-same",D1==D2)
for p in range(2,7):
    ck("S-split-history-"+str(p),L1["w"][1:3]!=L2["w"][1:3])

for row in S["cells"]:
    c=tuple(row["id_index"])
    test=[tuple(x) for x in row["shortest_paths"]+row["selected_nonshortest_paths"]]
    states=[qstate(p) for p in test]
    ck("QO-path-"+row["cell_id"],all(x==states[0] for x in states))
    for p in test:ck("endpoint-"+row["cell_id"]+str(p),endpoint(p)==c)

MX=O["MIXED_CELL_COMPLETION_LEDGER"]
for p in range(1,7):
    a=find_assignment(4,p)
    ck("Q-exists-"+str(p),a is not None)
    ck("Q-injective-"+str(p),len(set(a.values()))==61)
    ck("Q-cyclic-"+str(p),all(a[cyc_cell(c)]==cyc_coord(a[c]) for c in a))
    ck("Q-digest-"+str(p),digest(a)==MX["radius4_witnesses"]["p"+str(p)])
for p in range(2,7):
    for n in (2,3):
        for t in sorted(filter_ray((n,0),qopts((n,0),p))):
            ck("branch-ext-"+str((p,n,t)),find_assignment(4,p,{(n,0):t}) is not None)
ck("p2-n4-exact",filter_ray((4,0),qopts((4,0),2))=={(4,-2,-2)})
for p in range(3,7):
    ck("pgt2-n4-two",filter_ray((4,0),qopts((4,0),p))=={(4,-1,-1),(4,-2,-2)})

mixedcells=[(1,-1),(1,1),(0,1),(2,-1)]
for p in range(2,7):
    for c in mixedcells:
        for t in qopts(c,p):
            ck("mixed-ext-"+str((p,c,t)),find_assignment(4,p,{c:t}) is not None)

for p in range(2,7):
    pos=filter_ray((3,0),qopts((3,0),p));neg=qopts((-3,0),p)
    ck("invfail-"+str(p),not any(tuple(-x for x in t) in neg for t in pos))
pos=filter_ray((3,0),qopts((3,0),1));neg=qopts((-3,0),1)
ck("inv-p1",any(tuple(-x for x in t) in neg for t in pos))

for p in range(2,7):
    k=root_floor(3,p);levels={k} if k**p==3 else {k,k+1}
    ck("O-primary-fail-"+str(p),3 not in levels)

def qpolicy(cell,p,pol):
    a,b=cell;D=(a,-b,0);N,rho=normD(D);out=[]
    for x in N:
        n=rho-x;k=root_floor(n,p)
        if k**p==n:r=k
        elif pol=="floor":r=k
        elif pol=="ceil":r=k+1
        elif pol=="nearest":
            r=k if (2**p)*n < (2*k+1)**p else k+1
        elif pol=="midpoint":
            r=k if 2*n < k**p+(k+1)**p else k+1
        elif pol=="parity":r=k if n%2==0 else k+1
        out.append(x-r)
    return tuple(out)
q0=qpolicy((0,0),1,"floor"); q_u=qpolicy((1,0),1,"floor")
q_v=qpolicy((0,-1),1,"floor"); q_vu=qpolicy((1,-1),1,"floor")
d0=tuple(q_u[i]-q0[i] for i in range(3)); d1=tuple(q_vu[i]-q_v[i] for i in range(3))
ck("Q-p1-not-fixed-increment",d0==(1,-1,-1) and d1==(2,0,0) and d0!=d1)
for p in range(2,7):
    for pol in ("floor","ceil","nearest","midpoint"):
        vals={c:qpolicy(c,p,pol) for c in cells(4)}
        ck("policy-inj-"+str((p,pol)),len(set(vals.values()))==61)
        ck("policy-cyc-"+str((p,pol)),all(vals[cyc_cell(c)]==cyc_coord(vals[c]) for c in vals))
vals={c:qpolicy(c,2,"parity") for c in cells(4)}
ck("parity-p2-survives",len(set(vals.values()))==61)
for p in range(3,7):
    vals={c:qpolicy(c,p,"parity") for c in cells(4)}
    ck("parity-collision-"+str(p),len(set(vals.values()))<61)

V=O["FIVE_TO_FOUR_OR_NINE_CONTROL"]
ck("five-result",V["result"]=="FIVE_TO_FOUR_OR_NINE_STILL_UNRESOLVED_AT_TEST_RADIUS")
ck("five-levels",V["sqrt5"]["adjacent_root_levels"]==[2,3])

SV=O["ROOT_ORDER_SURVIVAL_LEDGER"]
ck("square-survive",SV["models"]["Q"]["p2"].startswith("SURVIVES_NONHOMOGENEOUS"))
ck("multi-roots","MULTIPLE_ROOT_ORDERS_SURVIVE" in SV["freezes"])
L=O["TRIVIALITY_LEAKAGE_LEDGER"]
ck("parent-gate",L["status"]=="PASS" and L["gates"]["stage_u_and_earlier_immutable"]=="PASS_BY_GITHUB_COMPARE_PRE_MANIFEST")
for k,v in L["gates"].items():
    if k not in ("CELL_COORDINATES_ARE_INTEGER_ONLY","stage_u_and_earlier_immutable"):
        ck("fw-"+k,v is False)
ck("cell-int-gate",L["gates"]["CELL_COORDINATES_ARE_INTEGER_ONLY"] is True)

dig=hashlib.sha256("\n".join(C).encode()).hexdigest()
out={
 "schema":"R059D_STAGE_W_REISSUE2_DETERMINISTIC_CHECKER_OUTPUT_V1",
 "status":"PASS","researcher_id":RID,"frozen_parent":PARENT,"taskbook_blob_sha1":TASK_BLOB,
 "checks_total":len(C),"checks_passed":len(C),"checks_failed":0,"checks_digest_sha256":dig,
 "parent_immutability":"PASS_BY_GITHUB_COMPARE_PRE_MANIFEST",
 "methods":{"proof_core":"exact A2 cell-ID relations, integer event counts, common-shift quotient invariants, exact integer root intervals, finite cyclic/injective completion CSP","enumeration":"radius4/61-cell and p=1..6 finite oracle only"}
}
(R/"R059D_STAGE_W_REISSUE2_DETERMINISTIC_CHECKER_OUTPUT.json").write_text(json.dumps(out,sort_keys=True,separators=(",",":"))+"\n")
print(json.dumps(out,indent=2))
