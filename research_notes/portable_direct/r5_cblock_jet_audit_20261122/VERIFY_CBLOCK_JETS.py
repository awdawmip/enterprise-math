#!/usr/bin/env python3
"""R5 correction: compute S4 failure numerator, not product(1-q**(m*p)).
Exact cyclic integer group-ring calculation; no floating point.
Run from this directory: python VERIFY_CBLOCK_JETS.py
Reads the pinned copied WITNESSES_ALL6.csv.gz.b64, writes corrected selected witnesses.
"""
import base64, csv, gzip, hashlib, io
from pathlib import Path
from collections import Counter, defaultdict
P=Path(__file__).resolve().parent
packed=(P/"WITNESSES_ALL6.csv.gz.b64").read_text().strip()
raw=gzip.decompress(base64.b64decode(packed))
assert hashlib.sha256(raw).hexdigest()=="fa987223acdeec3c310ef5e11122a924c290e0e3139e07e817a23b678eb997a2"
rows=list(csv.DictReader(io.StringIO(raw.decode())))
assert len(rows)==228
def shift(v,p,d):
    k=p%d
    return v[-k:]+v[:-k] if k else v[:]
def mul(a,b,d):
    c=[0]*d
    for i,x in enumerate(a):
        if x:
            for j,y in enumerate(b):
                if y:c[(i+j)%d]+=x*y
    return c
def Djet(d,scale=1):
    a=[1]+[0]*(d-1);da=[0]*d
    for p in range(296,313):
        q=shift(a,scale*p,d)
        dq=shift(da,scale*p,d)
        dq=[u+scale*p*v for u,v in zip(dq,q)]
        a=[u-v for u,v in zip(a,q)]
        da=[u-v for u,v in zip(da,dq)]
    return a,da
def true_cdot(d,M):
    # h_j for j=0,...,M-1; unbounded multiplicities in the 17-price S4 block.
    h=[[0]*d for _ in range(M)]
    h[0][0]=1
    for p in range(296,313):
        for j in range(1,M):
            z=shift(h[j-1],p,d)
            h[j]=[x+y for x,y in zip(h[j],z)]
    D,dD=Djet(d)
    assert len(set(D))==1
    res={};prefix=[0]*d
    for m in range(1,M+1):
        prefix=[x+y for x,y in zip(prefix,h[m-1])]
        res[m]=mul(dD,prefix,d)
    return res
def canon(a,d):
    if d==25:return [a[j]-a[20+j%5] for j in range(20)]
    if d==27:return [a[j]-a[18+j%9] for j in range(18)]
    return [a[j]-a[d-1] for j in range(d-1)]
def diffs(a):
    return (a[0],a[1]-a[0],a[2]-2*a[1]+a[0],a[3]-3*a[2]+3*a[1]-a[0])
out=[]
stats=defaultdict(Counter)
for d in sorted(set(int(r["d"]) for r in rows)):
    group=[r for r in rows if int(r["d"])==d]
    M=max(int(r["r"])+6*d for r in group)
    actual=true_cdot(d,M)
    fake={m:Djet(d,m)[1] for m in range(1,M+1)}
    for r in group:
        m0=int(r["r"]);j=int(r["coordinate"])
        u,v,w,x=(int(r[key]) for key in ("U","V","W","X"))
        if r["component"]=="Rdot":
            delta=[]
            for h in range(4):
                m=m0+2*d*h
                delta.append(canon(actual[m],d)[j]-canon(fake[m],d)[j])
            du,dv,dw,dx=diffs(delta)
            u+=du;v+=dv;w+=dw;x+=dx
        same_sign=(u!=0 and u*v>=0 and u*w>=0 and u*x>=0)
        out.append({**r, "new_U":u,"new_V":v,"new_W":w,"new_X":x,
                    "witness_valid":int(same_sign)})
        stats[d]["same_sign" if same_sign else "sign_rule_failed"]+=1
assert len(out)==228
fail=[(int(x["d"]),int(x["r"])) for x in out if not x["witness_valid"]]
assert fail==[(27,4),(27,5),(31,1),(31,4),(31,59)],fail
with (P/"CORRECTED_SELECTED_WITNESSES.csv").open("w",newline="") as f:
    writer=csv.DictWriter(f,fieldnames=list(rows[0])+["new_U","new_V","new_W","new_X","witness_valid"])
    writer.writeheader();writer.writerows(out)
for d in sorted(stats): print("order",d,dict(stats[d]))
for r in out:
    if not r["witness_valid"]:print("affected",r["d"],r["r"],r["new_U"],r["new_V"],r["new_W"],r["new_X"])
assert sum(r["witness_valid"] for r in out)==223
# Correct the five prior d=23 primitive-root coordinate-0 author values.
old={42:(-36685,-37881),43:(-165853,-175720),
     44:(-170315,-178687),45:(-88803,-89700),46:(4324,4324)}
actual23=true_cdot(23,46+46*2)
for r,(u,v) in old.items():
    shifts=[]
    for h in range(3):
        m=r+46*h
        shifts.append(canon(actual23[m],23)[0]-canon(Djet(23,m)[1],23)[0])
    U=u+shifts[0];V=v+shifts[1]-shifts[0]
    assert shifts[2]-2*shifts[1]+shifts[0]==0
    assert U==V!=0
    print("corrected_d23",r,U,V)
print("CORRECTION_PASS 228 original selected-coordinate rows; 223 sign witnesses remain; 5 require separate reasoning")
