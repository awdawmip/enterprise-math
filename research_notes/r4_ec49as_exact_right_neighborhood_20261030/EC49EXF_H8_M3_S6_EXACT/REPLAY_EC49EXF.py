#!/usr/bin/env python3
"""Finite exact H8 / three BRC keys / at most six history maps.

Input: all returning words and 465 immutable H7 predecessor cases.  Generates
14 exact integer-native-prefix DP instances and checks all minima against
112.  No floating point enters the proof kernel.

Sample:
  g++ -O3 -std=c++17 VERIFY_EC49EXF_OR_DP.cpp -o verify_dp
  g++ -O3 -std=c++17 ENUM_EC49EXF_WORDS.cpp -o enum_words
  ./enum_words > ALL_RETURN_WORDS_H2_H8.csv
  python REPLAY_EC49EXF.py ALL_RETURN_WORDS_H2_H8.csv \
      EC49EV_EXACT_EXECUTED.json.gz.b64 ./verify_dp ./evidence
"""
import base64
import collections
import csv
import gzip
import itertools
import json
import pathlib
import re
import subprocess
import sys

P=1000003
OPS={
'a':(-1,-1),'b':(-2,-2),'c':(1,2,-1,-2),'d':(2,1,-2,-1),
'e':(3,1,1,-3),'f':(1,-1),'g':(2,-2)}
HIST=(('N',0),('N',1),('N',2),('A',0),('A',2),('B',0),('B',1),('AB',0),('BA',0))
BASE=('ce','de','ec','ed')
K0=(3,1,1)
EXPECTED_COUNTS={2:8,3:51,4:304,5:1770,6:10224,7:58947,8:340064}
T4_EXPECTED={1836687,1867942,1872656,1873981}
T2_EXPECTED={1836425,1866380}


def rank(sigs):
    """Rank of stacked 9-to-5 deterministic transition matrices over F_1000003.
    A nonzero 9x9 0/1 determinant has abs value <=3^9 < P, so this detects
    rank-nine over Q exactly for the present matrix family.
    """
    sigs=sorted(sigs)
    a=[[int((s//5**i)%5==b) for s in sigs for b in range(5)] for i in range(9)]
    row=0
    for col in range(len(a[0])):
        pivot=next((i for i in range(row,9) if a[i][col]),None)
        if pivot is None: continue
        a[row],a[pivot]=a[pivot],a[row]
        v=pow(a[row][col],P-2,P)
        for c in range(col,len(a[0])):a[row][c]=(a[row][c]*v)%P
        for i in range(row+1,9):
            z=a[i][col]
            if z:
                for c in range(col,len(a[0])):
                    a[i][c]=(a[i][c]-z*a[row][c])%P
        row+=1
        if row==9:return 9
    return row


def independent_signature(steps):
    bucket={'N':0,'A':1,'B':2,'AB':3,'BA':4}
    packed=0;factor=1
    for ev0,last0 in HIST:
        ev=ev0;last=last0
        for step in steps:
            if last==1 and step==2:
                if ev=='N':ev='A'
                elif ev=='B':ev='BA'
            elif last==2 and step==1:
                if ev=='N':ev='B'
                elif ev=='A':ev='AB'
            last=step
        packed+=bucket[ev]*factor
        factor*=5
    return packed


def read_words(filename):
    fibers=collections.defaultdict(lambda:collections.defaultdict(list))
    counts=collections.Counter()
    with open(filename,encoding='utf-8',newline='') as f:
        for r in csv.DictReader(f):
            h=int(r['h']);u=int(r['u']);v=int(r['v']);w=int(r['w'])
            sig=int(r['sig']);word=r['word']
            assert len(word)==h and all(ch in OPS and ch!='b' for ch in word)
            # Recheck signed native six-axis return and positive key independently
            steps=tuple(x for ch in word for x in OPS[ch])
            pos=tuple(steps.count(i) for i in range(1,7))
            net=tuple(pos[i-1]-steps.count(-i) for i in range(1,7))
            assert net==(2,0,0,0,0,0) and pos==(u,v,w,0,0,0)
            assert independent_signature(steps)==sig,(h,word,sig)
            counts[h]+=1
            fibers[(h,(u,v,w))][sig].append(word)
    assert dict(counts)==EXPECTED_COUNTS,(counts,EXPECTED_COUNTS)
    return fibers


def read_predecessor(path):
    raw=pathlib.Path(path).read_bytes()
    if path.endswith('.b64'):
        data=json.loads(gzip.decompress(base64.b64decode(raw)))
    else:
        data=json.loads(raw)
    assert data['unit']=='EC49EV' and data['status']=='PASS'
    assert data['schedule_count']==465 and len(data['cases'])==465
    assert set(c['schedule_id'] for c in data['cases'])==set(range(465))
    assert data['exact_min']==86
    return data['cases']


def make_input(requirements,fibers,outfile):
    """One terminal color per horizon/signature; common 28-edge h2 core paid."""
    parent=[-1];baseline=[0];mask=[0];kids=[{}]
    def insert(word,paid=False,color=None):
        node=0
        for op in word:
            for s in OPS[op]:
                if s not in kids[node]:
                    kids[node][s]=len(parent)
                    parent.append(node);baseline.append(0);mask.append(0);kids.append({})
                node=kids[node][s]
                if paid:baseline[node]=1
        if color is not None:mask[node]|=1<<color
    for color,(h,k,sig) in enumerate(requirements):
        options=fibers[(h,k)].get(sig,[])
        assert options,(h,k,sig)
        for word in options:insert(word,color=color)
    for w in BASE:insert(w,paid=True)
    assert sum(baseline)==28
    with open(outfile,'w',encoding='utf-8') as f:
        f.write(f'{len(parent)} {len(requirements)}\n')
        for p,b,m in zip(parent,baseline,mask):f.write(f'{p} {b} {m}\n')
    return len(parent),len(requirements)


def main(words_source,predecessor_source,dp_binary,out_dir):
    out=pathlib.Path(out_dir);out.mkdir(parents=True,exist_ok=True)
    fibers=read_words(words_source)
    cases=read_predecessor(predecessor_source)
    signature_set={s for f in fibers.values() for s in f}
    assert len(signature_set)==11
    t4=set(fibers[(2,K0)])
    assert t4==T4_EXPECTED and rank(t4)==9
    extra=signature_set-t4
    rank9_extra_pairs=[set(z) for z in itertools.combinations(extra,2) if rank(z)==9]
    assert rank9_extra_pairs==[T2_EXPECTED] or rank9_extra_pairs==[set(T2_EXPECTED)]
    t2=T2_EXPECTED
    for extra_pair in itertools.combinations(extra,2):
        available=t4|set(extra_pair)
        for (h,k),sig_words in fibers.items():
            ss=set(sig_words)&available
            if rank(ss)==9:
                assert t4<=ss or (set(extra_pair)==t2 and t2<=ss),(extra_pair,h,k,ss)
    # Each earlier horizon already contributes its positive key, so an H8 M3
    # family uses exactly two or three keys through H7.
    extendible=[]
    for c in cases:
        keys={K0}|{tuple(k[:3]) for k in c['h3_to_h7_count_keys']}
        assert len(keys)==3
        choices=[]
        for k in keys:
            ss=set(fibers[(8,k)])
            if t2<=ss:choices.append((k,'2'))
            if t4<=ss:choices.append((k,'4'))
        if choices:
            bound=min(c['E']+(4 if typ=='2' else 8) for _,typ in choices)
            extendible.append((c,choices,bound))
    assert len(extendible)==270
    unresolved=[(c,choices,bound) for c,choices,bound in extendible if bound<112]
    assert len(unresolved)==14
    assert sorted(c['schedule_id'] for c,_,_ in unresolved)==sorted([47,50,9,11,159,163,76,79,83,119,191,195,200,232])
    executed=[]
    for c,choices,bound in unresolved:
        assert len(choices)==1 and choices[0][1]=='2'
        req=[]
        for h,(p,t) in enumerate(zip(c['h3_to_h7_count_keys'],c['signature_class']),3):
            req.extend((h,tuple(p[:3]),s) for s in sorted(t2 if t=='2' else t4))
        req.extend((8,choices[0][0],s) for s in sorted(t2))
        cid=c['schedule_id'];dp_file=out/f'H8_DP_CASE_{cid}.txt'
        n,k=make_input(req,fibers,dp_file)
        ret=subprocess.run([dp_binary],input=dp_file.read_bytes(),stdout=subprocess.PIPE,stderr=subprocess.PIPE,check=True)
        result=ret.stdout.decode('utf-8').strip()
        m=re.match(r'^PASS min_extra=(\d+) total=(\d+) nodes=(\d+) colors=(\d+) largest_states=(\d+) convolutions=(\d+)$',result)
        assert m,(cid,result)
        total=int(m.group(2))
        assert total>=112 and int(m.group(3))==n and int(m.group(4))==k
        executed.append(dict(id=cid,E7=c['E'],H8_optimistic_lower=bound,
                             E8_exact_fixed_schedule=total,dp_output=result,
                             H3toH7_keys=c['h3_to_h7_count_keys'],H3toH7_types=c['signature_class'],
                             H8_key=choices[0][0],H8_type=choices[0][1]))
    assert sorted(x['E8_exact_fixed_schedule'] for x in executed)[0]==112
    rows={int(x['id']):x['E8_exact_fixed_schedule'] for x in executed}
    assert rows=={47:112,50:112,9:114,11:114,159:114,163:114,
                 76:114,79:112,83:114,119:126,191:114,195:112,200:114,232:126}
    report=dict(status='PASS',unit='EC49EXF',H=8,M=3,S_at_most=6,
                complete_word_counts=EXPECTED_COUNTS,total_returning_words=sum(EXPECTED_COUNTS.values()),
                total_signatures=len(signature_set),tested_extra_pairs=21,
                H7_predecessor_schedules=465,H7_extendible_3key_schedules=len(extendible),
                low_cost_candidates_exact_DP=len(unresolved),
                full_model_global_minimum_E=112,
                classification_logic='H7 with <=2 keys >=116 (EC49ET), and H8 adds >=4 edges. If H7 uses 3 keys, H7 predecessor exact E7 plus >=4 (T2) or >=8 (T4) eliminates all but 14 checked cases. Other observer pairs require all T4, with >=116 H7 edges.',
                cases=sorted(executed,key=lambda t:t['id']))
    (out/'EC49EXF_FULL_EXACT_EXECUTED.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
    print('PASS exact H8 M3 S<=6 E=112; 14 native-prefix DP cases; 411368 returning words')
    return report

if __name__=='__main__':
    if len(sys.argv)!=5:
        raise SystemExit('usage: REPLAY_EC49EXF.py ALL_RETURN_WORDS.csv EC49EV_EXACT_EXECUTED.json.gz.b64 compiled_DP outdir')
    main(*sys.argv[1:])
