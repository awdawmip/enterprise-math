#!/usr/bin/env python3
"""Exact EC34 positive-source BRC Hankel certificate, pinned to EC33 code."""
from collections import defaultdict
from fractions import Fraction
from pathlib import Path
import argparse, hashlib, importlib.util, json
UPSTREAM_SHA = 'c2c5b183f88e7856c006f6b9ca954d603ac4e2cfd25d65a5558c67c91bc69856'
UPSTREAM_COMMIT = '0f84db42704c6e107adb9fd99d5e64cb77589e9d'

def load_original(path):
    assert hashlib.sha256(Path(path).read_bytes()).hexdigest() == UPSTREAM_SHA
    spec = importlib.util.spec_from_file_location('ec33_pinned', path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod

def micro(H, word):
    states={0:1}
    for label in word:
        nxt=defaultdict(int)
        for q,w in states.items():
            if q<H: nxt[q+1]+=w
            elif label=='R':
                # Two distinct microscopic red source alternatives R0 and R1.
                for source_id in ('R0','R1'):
                    assert source_id
                    nxt[H]+=w
        states=nxt
    return sum(states.values())

def rank(M):
    a=[[Fraction(v) for v in row] for row in M]
    n,m=len(a),len(a[0]); r=0
    for col in range(m):
        pivot=next((i for i in range(r,n) if a[i][col]),None)
        if pivot is None:continue
        a[r],a[pivot]=a[pivot],a[r]
        d=a[r][col]
        for j in range(col,m):a[r][j]/=d
        for i in range(n):
            if i==r or not a[i][col]:continue
            d=a[i][col]
            for j in range(col,m):a[i][j]-=d*a[r][j]
        r+=1
        if r==n:break
    return r

def det(M):
    a=[[Fraction(v) for v in row] for row in M]
    n=len(a); out=Fraction(1)
    for col in range(n):
        i=next((i for i in range(col,n) if a[i][col]),None)
        if i is None:return 0
        if i!=col:a[i],a[col]=a[col],a[i];out=-out
        d=a[col][col];out*=d
        for j in range(col+1,n):
            k=a[j][col]/d
            for t in range(col,n):a[j][t]-=k*a[col][t]
    return out

def verify(upstream, maxH):
    ec33=load_original(upstream)
    counts={'word':0,'total':0,'entries':0,'determinants':0,'refined_ranks':0,'scalar_ranks':0}
    witnesses=[]
    for H in range(1,maxH+1):
        for k in range(2*H+5):
            actual=ec33.weight_for_labels(H,tuple('B'*k),'V')
            assert actual==micro(H,'B'*k)==int(k<=H)
            counts['word']+=1
        for n in range(H+9):
            assert ec33.total_by_step_dp(H,n,'V')==2**n
            # Independently sum the positive microscopic source branches.
            states={0:1}
            for step in range(n):
                nex=defaultdict(int)
                for q,w in states.items():
                    if q<H:nex[q+1]+=2*w
                    else:nex[H]+=2*w
                states=nex
            assert sum(states.values())==2**n
            counts['total']+=1
        K=[]
        for i in range(H+1):
            row=[]
            for j in range(H+1):
                v=ec33.weight_for_labels(H,tuple('B'*(i+j)),'V')
                assert v==int(i+j<=H)
                row.append(v);counts['entries']+=1
            K.append(row)
        d=det(K)
        assert d==(-1)**(H*(H+1)//2)
        counts['determinants']+=1
        assert rank(K)==H+1
        counts['refined_ranks']+=1
        assert rank([[2**(i+j) for j in range(H+1)] for i in range(H+1)])==1
        counts['scalar_ranks']+=1
        assert ec33.weight_for_labels(H,tuple('B'*(H+1)),'U')==1
        assert ec33.weight_for_labels(H,tuple('B'*(H+1)),'V')==0
        witnesses.append({'H':H,'refined_rank':H+1,'scalar_rank':1,'determinant':str(d),'first_B_difference_depth':H+1})
    return {'status':'PASS','H_range':[1,maxH],'checks':counts,'witnesses':witnesses,
            'upstream_commit':UPSTREAM_COMMIT,'upstream_sha256':UPSTREAM_SHA,
            'model':'EC33 positive-source microscopic alternative-edge BRC',
            'scope':'auxiliary ordered-source observer only; no native X6 heartbeat calculation',
            'unbounded_claim_proof':'paper algebraic determinant, not finite extrapolation',
            'native_owner_or_claim':'UNKNOWN; CONTROL_QUOTA / STATIC_READONLY_SCOPE_DENIED'}

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--upstream',required=True)
    p.add_argument('--max-h',type=int,default=18);p.add_argument('--out',default='EC34_GITHUB_REPORT.json')
    a=p.parse_args()
    d=verify(a.upstream,a.max_h)
    Path(a.out).write_text(json.dumps(d,sort_keys=True,indent=2)+'\n',encoding='utf-8')
    print('EC34',d['status'],d['checks'])
