#!/usr/bin/env python3
"""Exact standard-library verifier for P000 Q30 n=14 r=14 reconstruction replay supplement."""
from __future__ import annotations
import argparse,base64,hashlib,json,math
from collections import Counter
from functools import lru_cache
from pathlib import Path

TASK="RS-P000-PHILOSOPHY-FIRST-RETURN-PROFILE-1WL-N14-COLLISION-FRONTIER"
PUB="TP2-8969646E7FF5FB8A9F5D"
RID="EM-P000Q30N14-536310"
CLAIM="chatgpt-p000q30n14-20260904-2106-536310"
N=14
COUNT=19491385914000
NREP=509
COMBINED_CODES="d7524b05f148fec867f77270c6fce71e33b4be5d9e78d15a6f729a68825c3505"
PACKET_IMAGE="3f51237fff86d43bd33ede65c412a4aa92ecbdb008bc770180cbc1aca3c82b80"
AUT_HIST={1:103,2:159,4:117,6:4,8:62,12:7,14:1,16:35,24:2,28:2,32:11,48:1,64:2,96:1,128:1,336:1}
PARTS=[
(1,105,"37d0e7b14195368bcb5121553a0dd3a94dfff3defec123b0f75a6f706473e7e8","bf2fec6fc272300dfbc9c5eb8f43bc4a69bfcfa05382fb190335ef6890657c06"),
(2,105,"8073826e5a029e3d090cc5e48a4c9317ed43744b4f02d18316b48fef3a030adf","70804fc1527cf5fadb6b59d180dd719ed5b1e90b1f6e0fc418096b3e5998f6ac"),
(3,105,"1429274e269cc494079c983765b8f367427f6e19acb1b41f6a6c4d50def1d041","5c871358798ee8c3bd3b03eefe8be0fefbd2eefe25020ebe8906c17fd29d9e5c"),
(4,105,"30d5ae650e3632d0d8c951c7422e27369b629784ac54c106b1cb24cc7e9349ad","37a4126e3cde9a15817c927469b35d186261e0fc0bd86d2b25342257fbc305b9"),
(5,89,"b8fdc7c2b7c3b5efa6216e85f692c2119eab7f3a08c4b2b1687af40605c397ed","d319bb4ab05351d7c81534d1cc5594ee8d29592ae520e2d55a95df98cc4179f5")]

def ck(x,msg):
    if not x: raise AssertionError(msg)

def decode(s):
    raw=base64.b64decode(s+"="*((4-len(s)%4)%4))
    bits="".join(f"{b:08b}" for b in raw)
    need=N*(N+1)//2*2
    ck(len(bits)>=need and set(bits[need:])<=set("0"),"kernel padding")
    vals=[int(bits[i:i+2],2) for i in range(0,need,2)]
    a=[0]*N; k=0
    for i in range(N):
        for j in range(i,N):
            v=vals[k]; k+=1
            ck(v in (0,1),"non-simple multiplicity")
            if i==j: ck(v==0,"loop in simple cubic sector")
            elif v:
                a[i]|=1<<j; a[j]|=1<<i
    return tuple(a)

def conn(a):
    seen=1; st=[0]
    while st:
        v=st.pop(); u=a[v]&~seen
        while u:
            b=u&-u; u-=b; seen|=b; st.append(b.bit_length()-1)
    return seen==(1<<len(a))-1

def profiles(a):
    n=len(a); c=[[0]*(n+1) for _ in range(n)]
    for s in range(n):
        path=[s]; high=~((1<<(s+1))-1)
        def dfs(v,used):
            if len(path)>=3 and ((a[v]>>s)&1) and path[1]<path[-1]:
                L=len(path)
                for x in path:c[x][L]+=1
            u=a[v]&~used&high
            while u:
                b=u&-u; u-=b; w=b.bit_length()-1
                path.append(w); dfs(w,used|b); path.pop()
        dfs(s,1<<s)
    return tuple(tuple(x[3:]) for x in c)

def packet(a):
    n=len(a); p=profiles(a)
    leg0=tuple(sorted(set(p))); ids={x:i for i,x in enumerate(leg0)}; col=[ids[x] for x in p]
    layers=[]; cc=len(leg0); stab=None
    for t in range(n):
        sig=[]
        for v in range(n):
            ns=[]; u=a[v]
            while u:
                b=u&-u; u-=b; ns.append(col[b.bit_length()-1])
            sig.append((col[v],tuple(sorted(ns))))
        leg=tuple(sorted(set(sig))); ids={x:i for i,x in enumerate(leg)}; new=[ids[x] for x in sig]
        if stab is None and len(leg)==cc:stab=t
        layers.append(leg); col=new; cc=len(leg)
    ck(stab is not None,"no stabilization")
    return p,tuple(col),json.dumps((leg0,tuple(layers),tuple(sorted(col))),separators=(",",":"))

def aut(a,p,col):
    n=len(a); deg=[x.bit_count() for x in a]
    keys=[(deg[v],p[v],col[v]) for v in range(n)]; buckets={}
    for w,k in enumerate(keys):buckets.setdefault(k,[]).append(w)
    cand=[buckets[k] for k in keys]
    order=sorted(range(n),key=lambda v:(len(cand[v]),-deg[v],v))
    mp=[-1]*n; out=0
    def rec(i,used):
        nonlocal out
        if i==n:out+=1;return
        v=order[i]
        for w in cand[v]:
            b=1<<w
            if used&b:continue
            if all(((a[v]>>order[j])&1)==((a[w]>>mp[order[j]])&1) for j in range(i)):
                mp[v]=w;rec(i+1,used|b);mp[v]=-1
    rec(0,0);ck(out>0,"missing identity");return out

@lru_cache(None)
def simple(ds):
    seq=tuple(sorted((d for d in ds if d>0),reverse=True))
    if not seq:return 1
    n=len(seq);d=seq[0]
    if d>=n:return 0
    rest=list(seq[1:]); groups=[(v,rest.count(v)) for v in sorted(set(rest),reverse=True)]
    ans=0
    def rec(i,left,pick,mul):
        nonlocal ans
        if i==len(groups):
            if left:return
            nxt=[]
            for (v,c),k in zip(groups,pick):nxt += [v-1]*k+[v]*(c-k)
            if min(nxt,default=0)<0:return
            ans += mul*simple(tuple(nxt));return
        v,c=groups[i]
        for k in range(min(c,left)+1):
            if v==0 and k:continue
            rec(i+1,left-k,pick+[k],mul*math.comb(c,k))
    rec(0,d,[],1);return ans

@lru_cache(None)
def total(c3):return simple((3,)*c3)

@lru_cache(None)
def connected(c3):
    if c3==0:return 0
    ans=total(c3)
    for o3 in range(c3):
        s3=1+o3
        if s3==c3 or s3<=3:continue
        ans -= math.comb(c3-1,o3)*connected(s3)*total(c3-s3)
    return ans

def verify(root):
    art=root/"research_artifacts"/"P000_PHILOSOPHY_FIRST_RETURN_PROFILE_1WL_N14_COLLISION_FRONTIER"
    codes=[]
    for part,count,dig,fh in PARTS:
        q=art/f"P000_Q30_N14_KERNELS_R14_RECON_P{part}_V1.json"
        text=q.read_text()
        ck(hashlib.sha256(text.encode()).hexdigest()==fh,f"file sha p{part}")
        obj=json.loads(text)
        ck((obj["schema"],obj["task_id"],obj["publication_id"],obj["researcher_id"],obj["claim_id"])==
           ("P000_Q30_N14_KERNEL_SHARD_V1",TASK,PUB,RID,CLAIM),f"binding p{part}")
        ck((obj["r"],obj["part"],obj["part_count"],obj["kernel_type_count"])==(14,part,5,count),f"meta p{part}")
        rows=obj["kernel_codes"]
        ck(rows==sorted(rows) and len(rows)==count,f"rows p{part}")
        got=hashlib.sha256(("\n".join(rows)+"\n").encode()).hexdigest()
        ck(got==dig==obj["kernel_codes_sha256"],f"code digest p{part}")
        codes += rows
    ck(len(codes)==len(set(codes))==NREP and codes==sorted(codes),"global codes")
    ck(hashlib.sha256(("\n".join(codes)+"\n").encode()).hexdigest()==COMBINED_CODES,"combined codes")
    ck(connected(14)==COUNT,"independent labeled count")
    enc=[]; autos=[]
    for s in codes:
        a=decode(s)
        ck(conn(a) and all(x.bit_count()==3 for x in a),"not connected simple cubic")
        p,c,e=packet(a);enc.append(e);autos.append(aut(a,p,c))
    ck(len(enc)==len(set(enc))==NREP,"stable packet collision")
    dig=hashlib.sha256(("\n".join(sorted(enc))+"\n").encode()).hexdigest()
    ck(dig==PACKET_IMAGE,"packet image digest")
    hist=dict(sorted(Counter(autos).items()))
    ck(hist==AUT_HIST,"automorphism histogram")
    orbit=sum(math.factorial(N)//a for a in autos)
    ck(orbit==COUNT,"orbit cover")
    return len(codes),len(enc),orbit,dig

def main():
    root=Path(__file__).resolve().parents[1]
    ap=argparse.ArgumentParser();ap.add_argument("--root",type=Path,default=root)
    a=ap.parse_args();nr,np,orbit,_=verify(a.root)
    print(f"PASS Q30 n=14 r14 reconstruction replay: representatives={nr} stable_packets={np} orbit_sum={orbit} collision=0")

if __name__=="__main__":main()
