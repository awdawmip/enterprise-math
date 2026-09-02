#!/usr/bin/env python3
"""Control-valid exact verifier for the Q28 n=12 frozen certificate.

Reuses the accepted Q27 exact primitive-cycle / ordinary-1-WL / degree-count /
automorphism implementation. Q28 contributes only n=12 graph6 decoding,
certificate binding, and the sector/global orbit-cover checks.
"""
from __future__ import annotations
import argparse,base64,hashlib,importlib.util,json,lzma,math
from collections import Counter
from pathlib import Path

TASK="RS-P000-PHILOSOPHY-FIRST-RETURN-PROFILE-1WL-N12-COLLISION-FRONTIER"
PUB="TP2-C74E704488CBF01A602D"
RESULT="RR-D277A62E967320225132"
EXECUTION="ER-AED46EF41615532B2F46"
RID="EM-P000-AED46E"
CLAIM="chatgpt-p000q28-reexec-20260902-1920-8c7a2d"
COUNTS={2:63504000,4:161965440,6:423705600,8:1183502880,10:3561440400,12:11543439600}
REPS={2:29,4:351,6:1373,8:1892,10:835,12:85}
DIGESTS={
2:"ed91e3ff2a67244632fb7c85b06b4f99f04d90e6e41f18728677a92af498ab6a",
4:"a883a730d51d50cadd0ec89615c1ea88a5a4077a7de24ccba9aeeeef84a8d3b1",
6:"65390b31b86c6a4c8a3833603045ec8310e05e6fd8a101746ebc0e15ec6c80fb",
8:"1f9d61310be9c5dffeff5d0c4d496537c2c4b8bbcee0afd49fcfc80b94f006f9",
10:"7de0d6a3d5371fe4994ee41ea38d2dde7540c1bbebc862567ecdd50eaee54922",
12:"9c0c68896bb50488c16d2805920c75b46dcb6ddaa18bae43217366ffcf0b8c47",
}
TOTAL=16937557920; NREP=4565
COMBINED="0503bb2767926a155c8ceb09c15ebffdf4d5750fe1584b214108cc74c99ff814"

def ck(x,msg):
    if not x: raise AssertionError(msg)

def load_q27():
    root=Path(__file__).resolve().parents[1]
    p=root/"research_checks"/"P000_PHILOSOPHY_FIRST_RETURN_PROFILE_1WL_N11_COLLISION_FRONTIER_CHECK_20260902.py"
    spec=importlib.util.spec_from_file_location("p000_q27_exact_core",p)
    ck(spec is not None and spec.loader is not None,"q27 core import")
    m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    return m

def g6(s):
    a=[ord(c)-63 for c in s]
    ck(a and all(0<=x<=63 for x in a),"bad graph6")
    n=a[0]; ck(n==12,"n drift")
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

def load(path):
    m=json.loads(path.read_text())
    ck(m["schema"]=="P000_Q28_RETURN_PROFILE_1WL_N12_EXACT_ORBIT_CERTIFICATE_V1","schema")
    ck((m["task_id"],m["publication_id"],m["result_id"],m["execution_record_id"],m["researcher_id"],m["claim_id"])==
       (TASK,PUB,RESULT,EXECUTION,RID,CLAIM),"binding")
    ck(m["n"]==12 and m["collision_fibers"]==0 and m["total_representatives"]==NREP and m["total_normalized_connected"]==TOTAL,"totals")
    payload={}
    for s in m["payload_shards"]:
        q=path.parent/s["file"]; text=q.read_text()
        ck(hashlib.sha256(text.encode()).hexdigest()==s["file_sha256"],"shard file hash")
        obj=json.loads(text)
        ck(obj["schema"]=="P000_Q28_N12_REPRESENTATIVE_SHARD_V1" and obj["codec"]=="lzma+base64","shard schema")
        raw=lzma.decompress(base64.b64decode(obj["payload_b64"]))
        ck(hashlib.sha256(raw).hexdigest()==obj["raw_sha256"]==s["raw_sha256"],"shard raw hash")
        payload.update(json.loads(raw))
    return m,payload

def verify(path):
    q27=load_q27()
    m,payload=load(path)
    allenc=[]; seen=set(); nr=lab=0
    for r in (2,4,6,8,10,12):
        ck(q27.connected(12-r,r)==COUNTS[r],f"count r={r}")
        meta=m["sectors"][str(r)]; dat=payload[str(r)]
        rows=dat["graph6"]; autos=dat["aut_sizes"]
        ck(len(rows)==len(autos)==REPS[r]==meta["representative_count"],f"rep count r={r}")
        ck(rows==sorted(rows),f"sort r={r}")
        enc=[]; orbit=0; fac=math.factorial(r)*math.factorial(12-r)
        for s,fa in zip(rows,autos):
            ck(s not in seen,"duplicate g6"); seen.add(s)
            a=g6(s); ck(conn(a),"disconnected")
            ck(Counter(x.bit_count() for x in a)==Counter({3:r,2:12-r}),f"degree r={r}")
            p,c,e=q27.packet(a)
            aa=q27.aut(a,p,c); ck(aa==fa and fac%aa==0,f"aut r={r}")
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
    d=root/"research_artifacts"/"P000_PHILOSOPHY_FIRST_RETURN_PROFILE_1WL_N12_COLLISION_FRONTIER"/"P000_Q28_RETURN_PROFILE_1WL_N12_EXACT_ORBIT_CERTIFICATE_REEXEC_AED46E_V1.json"
    ap=argparse.ArgumentParser(); ap.add_argument("--artifact",type=Path,default=d)
    a=ap.parse_args(); nr,lab,np,_=verify(a.artifact)
    print(f"PASS Q28 n=12 exact orbit certificate: representatives={nr} normalized_connected={lab} stable_packets={np} collision=0 lower_bound=n<=12")

if __name__=="__main__": main()
