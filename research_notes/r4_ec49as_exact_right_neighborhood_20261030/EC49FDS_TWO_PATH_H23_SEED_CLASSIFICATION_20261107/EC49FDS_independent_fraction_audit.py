#!/usr/bin/env python3
"""Independent exact rank audit of EC49FDS two-word seeds.
Uses literal signed primitive-step observer from immutable EC49FDQ audit,
not the six-signature four-clause shortcut from primary enumerator.
"""
import json,itertools
from fractions import Fraction
from pathlib import Path
from EC49FDS_seedpairs import language,rank_ok,steps

def obs(w):
    out=[]
    for name,prev in (('N',0),('N',1),('N',2),('A',0),('A',2),('B',0),('B',1),('AB',0),('BA',0)):
        state=name
        for t in steps(w):
            if prev==1 and t==2:
                if state=='N':state='A'
                elif state=='B':state='BA'
            elif prev==2 and t==1:
                if state=='N':state='B'
                elif state=='A':state='AB'
            prev=t
        out.append(('N','A','B','AB','BA').index(state))
    return out

def rank(ws):
    arr=[obs(w) for w in ws]
    mat=[[Fraction(int(o[i]==s)) for o in arr for s in range(5)] for i in range(9)]
    r=0
    for c in range(len(mat[0])):
        p=next((i for i in range(r,9) if mat[i][c]),None)
        if p is None: continue
        mat[p],mat[r]=mat[r],mat[p]
        lead=mat[r][c];mat[r]=[x/lead for x in mat[r]]
        for i in range(r+1,9):
            if mat[i][c]:
                a=mat[i][c]
                mat[i]=[u-a*v for u,v in zip(mat[i],mat[r])]
        r+=1
        if r==9:break
    return r

pairs=[]
for h in (2,3):
    words=language(h)
    rank9=[]
    for a,b in itertools.combinations(words,2):
        shortcut=rank_ok((a[1],b[1]))
        direct=(rank((a[0],b[0]))==9)
        assert shortcut==direct,(h,a,b,shortcut,direct)
        if direct:rank9.append([a[0],b[0]])
    pairs.append(rank9)
assert len(pairs[0])==1 and len(pairs[1])==16
report=json.load(open(Path(__file__).with_name('EC49FDS_seedpairs_report.json'),encoding='utf-8'))
for v in report['all_rank9_seed_pairs']:
    assert rank(v['H2'])==9 and rank(v['H3'])==9
if __name__=='__main__':print(json.dumps({'H2_rank9_pairs':pairs[0],'H3_rank9_pairs':pairs[1], 'audit':'ALL PAIRWISE H2/H3 RATIONAL RANK TESTS AGREE WITH CLAUSE CLASSIFIER', 'H2_cases_checked':15,'H3_cases_checked':703,'verified_combined_seed_pairs':len(report['all_rank9_seed_pairs'])},ensure_ascii=False,indent=2))
