from gen import F,MS,types
from collections import Counter
from math import comb
import csv,json
from pathlib import Path

def load_status():
    status={}
    for file in ['results.csv','results2.csv','results3.csv','symbolic_results.csv','cover_results.csv','fullrow_50000.csv','last8.csv']:
        for row in csv.reader(open(file)):
            i=int(row[0]); s=int(row[2]);
            if s:
                assert i not in status or status[i]==s
                status[i]=s
    return status

def remove(p,t):
    s,r=t; j=p.index(s); assert s>>r&1
    p[j]^=1<<r

def fibers(key):
    r,mask,other=key; p=(mask,*other)
    for u in F:
        if not (u>>r&1) or u&mask: continue
        b=sum(1<<j for j,s in enumerate(p) if s&u)
        if b.bit_count()>14: continue
        a=((1<<25)-1)^1
        if b.bit_count()==14:a=b
        yield u,b,a

def cert(f,k):
    tight=[]
    for u,b,a in f:
        p=(a^b).bit_count()
        if p>k:return False
        d=[v^u for v,c,e in f if v!=u and c&~b==0 and b&~e==0]
        if not d:
            if p==k:tight.append((u,b,a,0,0))
            continue
        rows=0
        for z in d:rows|=z
        best=k+1; extra=neg=0; z=rows
        while z:
            pos=(z&u).bit_count(); cost=max(p,pos)+(z&~u).bit_count()
            if cost<=best and cost<=k and all(z&q for q in d):
                if cost<best:best=cost;extra=neg=0
                if pos>p:extra|=z&u
                neg|=z&~u
            z=(z-1)&rows
        if best>k:return False
        if best==k:tight.append((u,b,a,extra,neg))
    if tight:
        return any(all((u>>r&1 and (a^b)>>j&1) or ((extra|neg)>>r&1 and not b>>j&1) for u,b,a,extra,neg in tight) for j in range(25) for r in range(10))
    return True

if __name__=='__main__':
    status=load_status(); cases=json.load(open('cases.json')); assert len(status)==len(cases)==348
    keys={}
    for i,(n,key,paths) in enumerate(cases):
        if status[i]!=1: continue
        for path in paths:
            p=MS.copy()
            for t in path:remove(p,t)
            for j,r in types(p):
                z=p.copy();z[j]^=1<<r
                key=(r,z[j],tuple(sorted(z[:j]+z[j+1:])))
                keys.setdefault(key,[]).append((path,(p[j],r)))
    print('ordered',sum(map(len,keys.values())),'unique',len(keys))
    out=[]
    for key,paths in keys.items():
        f=list(fibers(key)); n=sum(sum(comb((a^b).bit_count(),i) for i in range(min((a^b).bit_count(),14-b.bit_count())+1)) for u,b,a in f)
        label='TRIVIAL' if n<=1 else 'CAPACITY_NO' if n>2**15 else 'CERTIFICATE_NO' if not cert(f,15) else 'OPEN'
        out.append((n,key,paths,label))
    print(Counter(x[3] for x in out));print('ordered',Counter(x[3] for x in out for _ in x[2]));print('range',min(x[0] for x in out),max(x[0] for x in out));
    json.dump(sorted(out),open('fourth.json','w'),separators=(',',':'))
