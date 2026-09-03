#!/usr/bin/env python3
"""Exact standard-library verifier for P000 Q29 n=13 return-profile 1-WL certificate."""
from __future__ import annotations
import argparse,base64,hashlib,json,lzma,math
from collections import Counter
from functools import lru_cache
from pathlib import Path

TASK="RS-P000-PHILOSOPHY-FIRST-RETURN-PROFILE-1WL-N13-COLLISION-FRONTIER"
PUB="TP2-2BB590EA80230A7A7D4C"
EXEC="ER-B045187F5EDFF39075A8"
RID="EM-P000Q29N13-6C1B4E"
CLAIM="chatgpt-p000q29n13-20260902-2030-6c1b4e"
COUNTS={2:858211200,4:2430570240,6:6963440400,8:21063218400,10:68047938000,12:235189785600}
REPS={2:35,4:581,6:3159,8:6374,10:4541,12:839}
DIGESTS={
2:"c038bf95a0315e04e8bff7bafacd5dd3276295b446cc796c7b008f86a57d92c1",
4:"35776ac6c676164c5137d6ffd7262d3dbed7f9669fce891ed5c577f64e87cc38",
6:"9ec3a4c5cadf74b5e20a5bca26d9098139939dab7a841dbb3c488cb653e16168",
8:"d9bd46ae70d16a3424392f17f5b80dc1551ea764e30925047af1e289bf529cd2",
10:"6a35f902944152c785925454f6bd4e238c68bff641da0f464533708558859571",
12:"62988e4b43c090df2300b8e56bd32358f21442cc565194d7d08b6643660746c4"}
TOTAL=334553163840
NREP=15529
COMBINED="67cb46560ac86552b1ac0103de24a01192f5d85ccc6ec98e9e46e239308efbae"

def ck(x,msg):
    if not x: raise AssertionError(msg)

def g6(s):
    a=[ord(c)-63 for c in s]
    ck(a and all(0<=x<=63 for x in a),"bad graph6")
    n=a[0]; ck(n==13,"n drift")
    bits=[]
    for x in a[1:]: bits += [(x>>k)&1 for k in (5,4,3,2,1,0)]
    need=n*(n-1)//2
    ck(len(bits)>=need and not any(bits[need:]),"graph6 payload")
    adj=[0]*n; k=0
    for j in range(1,n):
        for i in range(j):
            if bits[k]:
                adj[i]|=1<<j; adj[j]|=1<<i
            k+=1
    return tuple(adj)

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
                for x in path: c[x][L]+=1
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
        if stab is None and len(leg)==cc: stab=t
        layers.append(leg); col=new; cc=len(leg)
    ck(stab is not None,"no stabilization")
    return p,tuple(col),json.dumps((leg0,tuple(layers),tuple(sorted(col))),separators=(',',':'))

@lru_cache(None)
def simple(ds):
    seq=tuple(sorted((d for d in ds if d>0),reverse=True))
    if not seq:return 1
    n=len(seq); d=seq[0]
    if d>=n:return 0
    rest=list(seq[1:])
    groups=[(v,rest.count(v)) for v in sorted(set(rest),reverse=True)]
    ans=0
    def rec(i,left,pick,mul):
        nonlocal ans
        if i==len(groups):
            if left:return
            nxt=[]
            for (v,c),k in zip(groups,pick): nxt += [v-1]*k+[v]*(c-k)
            if min(nxt,default=0)<0:return
            ans += mul*simple(tuple(nxt)); return
        v,c=groups[i]
        for k in range(min(c,left)+1):
            if v==0 and k:continue
            rec(i+1,left-k,pick+[k],mul*math.comb(c,k))
    rec(0,d,[],1); return ans

@lru_cache(None)
def total(c2,c3): return simple((2,)*c2+(3,)*c3)

@lru_cache(None)
def connected(c2,c3):
    n=c2+c3
    if n==0:return 0
    ans=total(c2,c3)
    if c3:
        for o3 in range(c3):
            for s2 in range(c2+1):
                s3=1+o3; size=s2+s3
                if size==n or size<=3:continue
                ans -= math.comb(c3-1,o3)*math.comb(c2,s2)*connected(s2,s3)*total(c2-s2,c3-s3)
    else:
        for o2 in range(c2):
            s2=1+o2
            if s2==n or s2<=2:continue
            ans -= math.comb(c2-1,o2)*connected(s2,0)*total(c2-s2,0)
    return ans

def aut(a,p,col):
    n=len(a); deg=[x.bit_count() for x in a]
    keys=[(deg[v],p[v],col[v]) for v in range(n)]; buckets={}
    for w,k in enumerate(keys):buckets.setdefault(k,[]).append(w)
    cand=[buckets[k] for k in keys]
    order=sorted(range(n),key=lambda v:(len(cand[v]),-deg[v],v))
    mp=[-1]*n; out=0
    def rec(i,used):
        nonlocal out
        if i==n: out+=1; return
        v=order[i]
        for w in cand[v]:
            b=1<<w
            if used&b:continue
            if all(((a[v]>>order[j])&1)==((a[w]>>mp[order[j]])&1) for j in range(i)):
                mp[v]=w; rec(i+1,used|b); mp[v]=-1
    rec(0,0); ck(out>0,"missing identity"); return out

def load(path):
    m=json.loads(path.read_text())
    ck(m["schema"]=="P000_Q29_RETURN_PROFILE_1WL_N13_EXACT_ORBIT_CERTIFICATE_V1","schema")
    ck((m["task_id"],m["publication_id"],m["execution_record_id"],m["researcher_id"],m["claim_id"])==
       (TASK,PUB,EXEC,RID,CLAIM),"binding")
    ck(m["n"]==13 and m["collision_fibers"]==0 and
       m["total_representatives"]==NREP and m["total_normalized_connected"]==TOTAL,"totals")
    payload={}
    for s in m["payload_shards"]:
        q=path.parent/s["file"]; text=q.read_text()
        ck(hashlib.sha256(text.encode()).hexdigest()==s["file_sha256"],"shard file hash")
        obj=json.loads(text)
        ck(obj["schema"]=="P000_Q29_N13_REPRESENTATIVE_SHARD_V1" and obj["codec"]=="lzma+base64","shard schema")
        raw=lzma.decompress(base64.b64decode(obj["payload_b64"]))
        ck(hashlib.sha256(raw).hexdigest()==obj["raw_sha256"]==s["raw_sha256"],"shard raw hash")
        payload.update(json.loads(raw))
    return m,payload

def verify(path):
    m,payload=load(path); allenc=[]; seen=set(); nr=lab=0
    for r in (2,4,6,8,10,12):
        ck(connected(13-r,r)==COUNTS[r],f"count r={r}")
        meta=m["sectors"][str(r)]; dat=payload[str(r)]
        rows=dat["graph6"]; autos=dat["aut_sizes"]
        ck(len(rows)==len(autos)==REPS[r]==meta["representative_count"],f"rep count r={r}")
        ck(rows==sorted(rows),f"sort r={r}")
        enc=[]; orbit=0; fac=math.factorial(r)*math.factorial(13-r)
        for s,fa in zip(rows,autos):
            ck(s not in seen,"duplicate g6"); seen.add(s)
            a=g6(s); ck(conn(a),"disconnected")
            ck(Counter(x.bit_count() for x in a)==Counter({3:r,2:13-r}),f"degree r={r}")
            p,c,e=packet(a); aa=aut(a,p,c)
            ck(aa==fa and fac%aa==0,f"aut r={r}")
            orbit += fac//aa; enc.append(e); allenc.append(e)
        ck(len(enc)==len(set(enc)),f"packet collision r={r}")
        dig=hashlib.sha256(("\n".join(sorted(enc))+"\n").encode()).hexdigest()
        ck(dig==DIGESTS[r]==meta["packet_image_sha256"],f"sector digest r={r}")
        ck(orbit==COUNTS[r]==meta["normalized_label_orbit_sum"]==meta["expected_normalized_connected"],f"orbit cover r={r}")
        nr+=len(rows); lab+=orbit
    ck(nr==NREP and lab==TOTAL and len(allenc)==len(set(allenc))==NREP,"global cover/collision")
    dig=hashlib.sha256(("\n".join(sorted(allenc))+"\n").encode()).hexdigest()
    ck(dig==COMBINED==m["combined_packet_image_sha256"],"combined digest")
    return nr,lab,len(allenc),dig

def main():
    root=Path(__file__).resolve().parents[1]
    d=root/"research_artifacts"/"P000_PHILOSOPHY_FIRST_RETURN_PROFILE_1WL_N13_COLLISION_FRONTIER"/"P000_Q29_RETURN_PROFILE_1WL_N13_EXACT_ORBIT_CERTIFICATE_V1.json"
    ap=argparse.ArgumentParser(); ap.add_argument("--artifact",type=Path,default=d)
    a=ap.parse_args(); nr,lab,np,_=verify(a.artifact)
    print(f"PASS Q29 n=13 exact orbit certificate: representatives={nr} normalized_connected={lab} stable_packets={np} collision=0 lower_bound=n<=13")
if __name__=="__main__": main()
