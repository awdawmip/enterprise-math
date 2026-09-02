#!/usr/bin/env python3
"""Exact standard-library verifier for the frozen Q27 n=11 certificate."""
from __future__ import annotations
import argparse,base64,hashlib,json,lzma,math
from collections import Counter
from functools import lru_cache
from pathlib import Path

TASK="RS-P000-PHILOSOPHY-FIRST-RETURN-PROFILE-1WL-N11-COLLISION-FRONTIER"
PUB="TP2-875D6C62E617BCC7CE63"; RESULT="RR-5F80FBDB98CAA0E43177"
RID="EM-P000-7A4951"; CLAIM="chatgpt-p000-q27-20260902-0920"
COUNTS={2:5050080,4:11476080,6:27213300,8:69824160,10:194934600}
REPS={2:23,4:197,6:536,8:482,10:114}; TOTAL=308498220; NREP=1352

def ck(x,msg):
    if not x: raise AssertionError(msg)

def g6(s):
    a=[ord(c)-63 for c in s]; ck(a and all(0<=x<=63 for x in a),'bad graph6'); n=a[0]; ck(n==11,'n drift')
    bits=[]
    for x in a[1:]: bits += [(x>>k)&1 for k in (5,4,3,2,1,0)]
    need=n*(n-1)//2; ck(len(bits)>=need and not any(bits[need:]),'graph6 payload')
    adj=[0]*n; k=0
    for j in range(1,n):
        for i in range(j):
            if bits[k]: adj[i]|=1<<j; adj[j]|=1<<i
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
                b=u&-u; u-=b; w=b.bit_length()-1; path.append(w); dfs(w,used|b); path.pop()
        dfs(s,1<<s)
    return tuple(tuple(x[3:]) for x in c)

def packet(a):
    n=len(a); p=profiles(a); leg0=tuple(sorted(set(p))); ids={x:i for i,x in enumerate(leg0)}; col=[ids[x] for x in p]
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
    ck(stab is not None,'no stabilization')
    return p,tuple(col),json.dumps((leg0,tuple(layers),tuple(sorted(col))),separators=(',',':'))

@lru_cache(None)
def simple(ds):
    seq=tuple(sorted((d for d in ds if d>0),reverse=True))
    if not seq:return 1
    n=len(seq); d=seq[0]
    if d>=n:return 0
    rest=list(seq[1:]); groups=[(v,rest.count(v)) for v in sorted(set(rest),reverse=True)]; ans=0
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
def total(c2,c3):return simple((2,)*c2+(3,)*c3)
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
    n=len(a); deg=[x.bit_count() for x in a]; keys=[(deg[v],p[v],col[v]) for v in range(n)]; buckets={}
    for w,k in enumerate(keys):buckets.setdefault(k,[]).append(w)
    cand=[buckets[k] for k in keys]; order=sorted(range(n),key=lambda v:(len(cand[v]),-deg[v],v)); mp=[-1]*n; out=0
    def rec(i,used):
        nonlocal out
        if i==n:out+=1;return
        v=order[i]
        for w in cand[v]:
            b=1<<w
            if used&b:continue
            if all(((a[v]>>order[j])&1)==((a[w]>>mp[order[j]])&1) for j in range(i)):
                mp[v]=w;rec(i+1,used|b);mp[v]=-1
    rec(0,0);ck(out>0,'missing identity');return out

def load(path):
    m=json.loads(path.read_text()); ck(m['schema']=='P000_Q27_RETURN_PROFILE_1WL_N11_EXACT_ORBIT_CERTIFICATE_V1','schema')
    ck((m['task_id'],m['publication_id'],m['result_id'],m['researcher_id'],m['claim_id'])==(TASK,PUB,RESULT,RID,CLAIM),'binding')
    ck(m['n']==11 and m['collision_fibers']==0 and m['total_representatives']==NREP and m['total_normalized_connected']==TOTAL,'totals')
    payload={}
    for s in m['payload_shards']:
        q=path.parent/s['file']; text=q.read_text(); ck(hashlib.sha256(text.encode()).hexdigest()==s['file_sha256'],'shard file hash')
        obj=json.loads(text); ck(obj['schema']=='P000_Q27_N11_REPRESENTATIVE_SHARD_V1' and obj['codec']=='lzma+base64','shard schema')
        raw=lzma.decompress(base64.b64decode(obj['payload_b64'])); h=hashlib.sha256(raw).hexdigest(); ck(h==obj['raw_sha256']==s['raw_sha256'],'shard raw hash')
        payload.update(json.loads(raw))
    return m,payload

def verify(path):
    m,payload=load(path); allenc=[]; seen=set(); nr=lab=0
    for r in (2,4,6,8,10):
        ck(connected(11-r,r)==COUNTS[r],f'count r={r}'); meta=m['sectors'][str(r)]; dat=payload[str(r)]; rows=dat['graph6']; autos=dat['aut_sizes']
        ck(len(rows)==len(autos)==REPS[r]==meta['representative_count'],'rep count'); ck(rows==sorted(rows),'sort')
        enc=[]; orbit=0; fac=math.factorial(r)*math.factorial(11-r)
        for s,fa in zip(rows,autos):
            ck(s not in seen,'duplicate g6');seen.add(s);a=g6(s);ck(conn(a),'disconnected');ck(Counter(x.bit_count() for x in a)==Counter({3:r,2:11-r}),'degree')
            p,c,e=packet(a);aa=aut(a,p,c);ck(aa==fa and fac%aa==0,'aut');orbit+=fac//aa;enc.append(e);allenc.append(e)
        ck(len(enc)==len(set(enc)),'packet collision');enc.sort();dig=hashlib.sha256(('\n'.join(enc)+'\n').encode()).hexdigest()
        ck(dig==meta['packet_image_sha256'],'sector digest');ck(orbit==COUNTS[r]==meta['normalized_label_orbit_sum']==meta['expected_normalized_connected'],'orbit cover')
        nr+=len(rows);lab+=orbit
    ck(nr==NREP and lab==TOTAL and len(allenc)==len(set(allenc))==NREP,'global cover/collision');allenc.sort();dig=hashlib.sha256(('\n'.join(allenc)+'\n').encode()).hexdigest();ck(dig==m['combined_packet_image_sha256'],'combined digest')
    return nr,lab,len(allenc),dig

def main():
    d=Path(__file__).resolve().parents[1]/'research_artifacts'/'P000_PHILOSOPHY_FIRST_RETURN_PROFILE_1WL_N11_COLLISION_FRONTIER'/'P000_Q27_RETURN_PROFILE_1WL_N11_EXACT_ORBIT_CERTIFICATE_V1.json'
    ap=argparse.ArgumentParser();ap.add_argument('--artifact',type=Path,default=d);a=ap.parse_args();nr,lab,np,_=verify(a.artifact);print(f'PASS Q27 n=11 exact orbit certificate: representatives={nr} normalized_connected={lab} stable_packets={np} collision=0 lower_bound=n<=11')
if __name__=='__main__':main()
