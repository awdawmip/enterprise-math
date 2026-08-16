#!/usr/bin/env python3
import json,hashlib,zlib,base64
from pathlib import Path
from collections import Counter,defaultdict,deque
try:
    import numpy as np
except Exception:
    np=None
ROOT=Path(__file__).resolve().parent
checks=[]
def ck(n,c,d=""):
    checks.append((n,bool(c),str(d)))
    if not c: raise AssertionError(f"{n}: {d}")
def load(n):
    o=json.loads((ROOT/n).read_text())
    if isinstance(o,dict) and o.get("codec")=="zlib+base64":
        raw=zlib.decompress(base64.b64decode(o["compressed_payload_b64"]))
        ck(f"compressed_sha_{n}",hashlib.sha256(raw).hexdigest()==o["uncompressed_sha256"])
        return json.loads(raw)
    return o
def q(a,b): return a*a+a*b+b*b
def verts(c):
    o,a,b=c
    return ((a,b),(a+1,b),(a,b+1)) if o=="U" else ((a+1,b),(a,b+1),(a+1,b+1))
def cent(c):
    v=verts(c);return sum(x for x,y in v),sum(y for x,y in v)
def neigh(c):
    o,a,b=c
    return [("D",a,b),("D",a,b-1),("D",a-1,b)] if o=="U" else [("U",a,b),("U",a+1,b),("U",a,b+1)]
def cand(r):
    B=2*r+3; L=9*(r+1)**2
    return [(o,a,b) for a in range(-B,B+1) for b in range(-B,B+1) for o in ("U","D") if q(*cent((o,a,b)))<=L]
M={}
def micro(s):
    if s in M:return M[s]
    z=[(3*i+1,3*j+1) for i in range(s) for j in range(s-i)]
    z += [(3*i+2,3*j+2) for i in range(max(0,s-1)) for j in range(s-1-i)]
    ck(f"micro_{s}",len(z)==s*s,len(z))
    M[s]=np.asarray(z,dtype=np.int64) if np is not None else z
    return M[s]
def cov(c,r,s):
    P0,P1,P2=verts(c);D=3*s;rr=(r*D)**2
    uv=np.asarray(micro(s),dtype=np.int64) if np is not None else micro(s)
    if np is not None:
        U=uv[:,0];V=uv[:,1]
        x=D*P0[0]+U*(P1[0]-P0[0])+V*(P2[0]-P0[0])
        y=D*P0[1]+U*(P1[1]-P0[1])+V*(P2[1]-P0[1])
        w=x*x+x*y+y*y
        return int(np.count_nonzero(w<=rr)),s*s
    n=0
    for U,V in uv:
        x=D*P0[0]+U*(P1[0]-P0[0])+V*(P2[0]-P0[0])
        y=D*P0[1]+U*(P1[1]-P0[1])+V*(P2[1]-P0[1])
        n += q(x,y)<=rr
    return int(n),s*s
def occN(r):
    rr=9*r*r
    return {c for c in cand(r) if q(*cent(c))<=rr}
def cell_from_vertices(vs):
    A=min(a for a,b in vs);B=min(b for a,b in vs);st=set(vs)
    return ("U",A,B) if (A,B) in st else ("D",A,B)
def rot(p):
    a,b=p;return (-b,a+b)
def ref(p):
    a,b=p;return (a+b,-b)
def rotcell(c,k=1):
    vs=list(verts(c))
    for _ in range(k%6): vs=[rot(p) for p in vs]
    return cell_from_vertices(vs)
def occC(r,s):
    lo=9*max(r-1,0)**2;hi=9*(r+1)**2;B=2*r+3;sector=set()
    for a in range(-1,B+1):
      for b in range(-1,B+1):
       for o in ("U","D"):
        c=(o,a,b);A,Bc=cent(c)
        if A<0 or Bc<0: continue
        qc=q(A,Bc)
        if qc>hi: continue
        if qc<=lo: sector.add(c)
        else:
            k,t=cov(c,r,s)
            if 2*k>=t: sector.add(c)
    out=set()
    for c in sector:
        for k in range(6): out.add(rotcell(c,k))
    return out
def edge_supported(occ):
    S=set()
    for c in occ:
        vc=set(verts(c))
        for n in neigh(c):
            if n in occ: S |= (vc & set(verts(n)))
    return S
DIRS=[(1,0),(0,1),(-1,1),(-1,0),(0,-1),(1,-1)]
DIDX={d:i for i,d in enumerate(DIRS)}
def boundary(S): return {p for p in S if any((p[0]+da,p[1]+db) not in S for da,db in DIRS)}
def hexball(r): return {(a,b) for a in range(-r,r+1) for b in range(-r,r+1) if max(abs(a),abs(b),abs(a+b))<=r}
def path(S,r):
    B=boundary(S);g=defaultdict(set)
    for p in B:
        for da,db in DIRS:
            v=(p[0]+da,p[1]+db)
            if v in B:g[p].add(v)
    st=(r,0);en=(0,r);dq=deque([st]);pr={st:None}
    while dq:
        u=dq.popleft()
        if u==en:break
        for v in g[u]:
            if v in pr or v[0]<0 or v[1]<0:continue
            pr[v]=u;dq.append(v)
    ck(f"path_exists_{r}",en in pr)
    z=[];u=en
    while u is not None:z.append(u);u=pr[u]
    return z[::-1]
def normturn(i,j):
    x=(j-i)%6
    return x-6 if x>3 else x
def pathdata(P):
    ds=[DIDX[(v[0]-u[0],v[1]-u[1])] for u,v in zip(P,P[1:])]
    core=ds[1:-1] if len(ds)>2 else []
    turns=[normturn(a,b) for a,b in zip(core,core[1:]) if normturn(a,b)!=0]
    return "".join(map(str,ds)), ",".join(f"{x:+d}" for x in turns), (bool(turns) and all(x>0 for x in turns))
def cycle_status(S):
    B=boundary(S);g=defaultdict(set)
    for p in B:
        for da,db in DIRS:
            v=(p[0]+da,p[1]+db)
            if v in B:g[p].add(v)
    seen=set();comp=0
    for p in B:
        if p in seen:continue
        comp+=1;stack=[p];seen.add(p)
        while stack:
            u=stack.pop()
            for v in g[u]:
                if v not in seen:seen.add(v);stack.append(v)
    return comp==1 and all(len(g[p])==2 for p in B)
def tri_bulge(P,r):
    poly=P+[(i,r-i) for i in range(1,r)];s=0
    for a,b in zip(poly,poly[1:]+poly[:1]): s += a[0]*b[1]-b[0]*a[1]
    return s
rad=load("R059D_STAGE_AE_RADIUS_LEDGER.json");bul=load("R059D_STAGE_AE_BULGE_LEDGER.json")
cal=load("R059D_STAGE_AE_COUNT_SEMANTICS_CALIBRATION.json");crit=load("R059D_STAGE_AE_CRITICAL_RADIUS_CERTIFICATE.json")
inv=load("R059D_STAGE_AE_INVERSE_LAW_CANDIDATES.json");leak=load("R059D_STAGE_AE_TARGET_LEAKAGE_AUDIT.json")
rf=rad["fields"];bf=bul["fields"]
Rrows={arm:{row[0]:dict(zip(rf,row)) for row in rad[arm]} for arm in ("N","C")}
Brows={arm:{row[0]:dict(zip(bf,row)) for row in bul[arm]} for arm in ("N","C")}
for arm in ("N","C"):
    for r,D,C,V in [(1,3,6,7),(2,5,12,19),(3,7,18,37)]:
        row=Rrows[arm][r];ck(f"control_{arm}_{r}",(row["D"],row["C"],row["V"])==(D,C,V))
prevV={"N":1,"C":1};prevC={"N":0,"C":0};prevDV={"N":None,"C":None};C64_cache={}
for r in range(1,65):
    O={"N":occN(r),"C":occC(r,64)};C64_cache[r]=O["C"]
    for arm in ("N","C"):
        S=edge_supported(O[arm]);H=hexball(r);Bnd=boundary(S);P=path(S,r)
        D=sum(1 for a,b in S if b==0);C=len(Bnd);V=len(S);dV=V-prevV[arm];dC=C-prevC[arm]
        d2=None if prevDV[arm] is None else dV-prevDV[arm]
        Bout=sum(1 for a,b in S-H if a>0 and b>0)-sum(1 for a,b in H-S if a>0 and b>0)
        sw,tw,cv=pathdata(P);rr=Rrows[arm][r];br=Brows[arm][r]
        for k,v in [("D",D),("C",C),("V",V),("DeltaV",dV),("DeltaC",dC),("Delta2V",d2),("B",Bout)]: ck(f"row_{arm}_{r}_{k}",rr[k]==v,(rr[k],v))
        ck(f"step_{arm}_{r}",br["step_word"]==sw);ck(f"turn_{arm}_{r}",br["turn_word"]==tw)
        ck(f"conv_{arm}_{r}",br["strict_outward_convex"]==(Bout>0 and cv));ck(f"tri_bulge_{arm}_{r}",br["B_tri_control"]==tri_bulge(P,r))
        ck(f"H_subset_{arm}_{r}",not (H-S));ck(f"axis_extra_{arm}_{r}",all(a!=0 and b!=0 and a+b!=0 for a,b in S-H))
        ck(f"D6_{arm}_{r}",{rot(p) for p in S}==S and {ref(p) for p in S}==S);ck(f"cycle_{arm}_{r}",cycle_status(S))
        J=(C-6*r)//6;ck(f"C_identity_{arm}_{r}",C==6*r+6*J);ck(f"V_identity_{arm}_{r}",V==1+3*r*(r+1)+6*Bout)
        ck(f"B_inverse_{arm}_{r}",4*V-3*D*D-1==24*Bout)
        ck(f"dV_identity_{arm}_{r}",dV-C==6*((Bout-(Brows[arm][r-1]["B"] if r>1 else 0))-J))
        prevV[arm]=V;prevC[arm]=C;prevDV[arm]=dV
for r in range(1,65):
    c64=C64_cache[r];c128=occC(r,128);ck(f"C_precision_{r}",c64==c128,len(c64^c128))
ck("crit_N_zero",crit["N"]["LAST_ZERO_BULGE_RADIUS"]==4);ck("crit_C_zero",crit["C"]["LAST_ZERO_BULGE_RADIUS"]==4)
ck("crit_first_positive",crit["N"]["FIRST_POSITIVE_BULGE_RADIUS"]==5 and crit["C"]["FIRST_POSITIVE_BULGE_RADIUS"]==5)
ck("crit_no_stable",crit["N"]["FIRST_STABLE_OUTWARD_BULGE_RADIUS"] is None and crit["C"]["FIRST_STABLE_OUTWARD_BULGE_RADIUS"] is None)
ck("disp",crit["primary_disposition"]=="NO_OUTWARD_CONVEXITY_THRESHOLD_THROUGH_AUDIT_RANGE")
for arm in ("N","C"):
    for r in range(1,5):
        x=Rrows[arm][r];ck(f"zero_D_{arm}_{r}",x["D"]==2*r+1);ck(f"zero_C_{arm}_{r}",x["C"]==6*r);ck(f"zero_V_{arm}_{r}",x["V"]==3*r*(r+1)+1)
    x=Rrows[arm][5];ck(f"baseline_fails5_{arm}",x["C"]!=30 and x["V"]!=91)
for r in range(5,11):
    for arm in ("N","C"):
        x=Rrows[arm][r];ck(f"transient_{arm}_{r}",x["B"]==r-2 and x["C"]==6*(r+1) and x["V"]==3*r*r+9*r-11)
ck("transient_N_holdout_fail",Rrows["N"][11]["B"]!=9 or Rrows["N"][11]["C"]!=72 or Rrows["N"][11]["V"]!=451)
ck("transient_C_r11_pass",Rrows["C"][11]["B"]==9 and Rrows["C"][11]["C"]==72 and Rrows["C"][11]["V"]==451)
ck("transient_C_holdout_fail",Rrows["C"][12]["B"]!=10 or Rrows["C"][12]["C"]!=78 or Rrows["C"][12]["V"]!=565)
for k,v in leak["forbidden"].items(): ck(f"firewall_{k}",v is False)
ck("post_only",leak["candidate_formulas_used_only_post_generation"] is True)
payload="\n".join(f"{n}:{int(ok)}:{d}" for n,ok,d in checks).encode()
print(json.dumps({"schema":"R059D_STAGE_AE_DETERMINISTIC_CHECKER_OUTPUT_V1","status":"PASS","checks_total":len(checks),"checks_passed":sum(o for _,o,_ in checks),"checks_failed":sum(not o for _,o,_ in checks),"checks_digest_sha256":hashlib.sha256(payload).hexdigest(),"history_gate":"PENDING_EXTERNAL_GITHUB_COMPARE","summary":"Exact N/C replay r=1..64, count calibration, dual D6 decomposition, bulge/turn words, inverse identities, s64-vs-s128 C stability, transient holdout failures, and hard firewalls pass."},sort_keys=True))