"""Independent literal-path audit of EC49CM h=7 witness files.
No import of witness generator; DFA labels read from actual adjacent words.
Checks exact signed displacement, positive integer BRC weights, all selected minors,
complete independent suffix-pattern ranks, and native endpoint BRC totals.
"""
from __future__ import annotations
from collections import defaultdict
from itertools import product
from pathlib import Path
import json
from native_signed_brc import endpoint_multiplicity,endpoint_weight

ROOT=Path(__file__).resolve().parent
P=1_000_003
W=((2,3,3,2,1,1),(3,2,3,2,1,1))
OPS={'a':(-1,-1),'b':(-2,-2),'c':(1,2,-1,-2),'d':(2,1,-2,-1)}
Q=(0,1,2,3,5,6,7,8)

def mod_rank(x):
    a=[[v%P for v in row] for row in x]
    if not a:return 0
    nr=len(a);nc=len(a[0]);r=0
    for j in range(nc):
        z=next((t for t in range(r,nr) if a[t][j]),None)
        if z is None:continue
        a[r],a[z]=a[z],a[r]
        t=pow(a[r][j],-1,P)
        for i in range(r+1,nr):
            if a[i][j]:
                factor=a[i][j]*t%P
                for k in range(j+1,nc):a[i][k]=(a[i][k]-factor*a[r][k])%P
                a[i][j]=0
        r+=1
        if r==nc:break
    return r

def det_mod(matrix):
    a=[[x%P for x in row] for row in matrix];n=len(a);det=1
    assert all(len(row)==n for row in a)
    for j in range(n):
        i=next((k for k in range(j,n) if a[k][j]),None)
        if i is None:return 0
        if i!=j:a[i],a[j]=a[j],a[i];det=-det
        t=a[j][j];det=det*t%P;inv=pow(t,-1,P)
        for k in range(j+1,n):
            if a[k][j]:
                f=a[k][j]*inv%P
                for l in range(j+1,n):a[k][l]=(a[k][l]-f*a[j][l])%P
                a[k][j]=0
    return det%P

def disp(word):
    z=[0]*6
    for x in word:z[abs(x)-1]+=1 if x>0 else -1
    return tuple(z)

def weight(word):
    return (int(__import__('math').prod(w[abs(x)-1] for x in word if x>0)) for w in W)

def weights(word):
    return tuple(weight(word))+(1,)

def labels(word):
    a=any(x==1 and y==2 for x,y in zip(word,word[1:]))
    b=any(x==2 and y==1 for x,y in zip(word,word[1:]))
    return 2*int(a)+int(b)

def initial_flags(q):
    a,b=divmod(q,3)
    return a==2,b==2,(1 if a==1 else 2 if b==1 else None)

def future_label(q,word):
    a,b,last=initial_flags(q)
    for x in word:
        a=a or (last==1 and x==2)
        b=b or (last==2 and x==1)
        last=x
    return 2*int(a)+int(b)

def suffix_dict(h,upto):
    return {''.join(seq):sum((OPS[a] for a in seq),()) for l in range(1 if upto else h,h+1)
            for seq in product(OPS,repeat=l)}

def all_row_rank(sufs):
    per_target=defaultdict(list)
    for word in sufs.values():
        d=tuple(-x for x in disp(word))
        final=[future_label(q,word) for q in Q]
        for t in range(4):per_target[d].append([int(a==t) for a in final])
    return {d:mod_rank(rows) for d,rows in per_target.items()}

def audit_one(h,upto,n):
    name=f'EC49CM_CERT_h{h}_{"SLE" if upto else "S"}_n{n}.json'
    data=json.loads((ROOT/name).read_text())
    assert data['h']==h and data['n']==n and data['prime']==P
    sufs=suffix_dict(h,upto)
    form=all_row_rank(sufs)
    assert len(form)==(h+1)*(h+2)//2
    total=0;minors=0;fail=[]
    for block in data['blocks']:
        d=tuple(block['target']);rank=block['rank'];expected=block['dimension']
        assert expected==3*form[d],(name,d,expected,form[d])
        paths=[tuple(v) for v in block['paths']]
        assert len(paths)==rank
        assert all(len(p)==n and disp(p)==d and all(1<=abs(x)<=6 for x in p) for p in paths)
        rows=block['selected_rows'];idx=block['minor_row_indices']
        assert len(rows)==expected and len(idx)==rank and len(set(idx))==rank
        assert all(0<=x<expected for x in idx)
        row_reps=[]
        for key,tag,ch in rows:
            word=sufs[key]
            assert tuple(-x for x in disp(word))==d
            assert tag in (0,1,2,3) and ch in (0,1,2)
            row_reps.append([int(future_label(q,word)==tag) for q in Q])
        assert mod_rank([row_reps[k] for k in range(0,len(rows),3)])==form[d]
        m=[]
        for k in idx:
            key,tag,ch=rows[k]
            suffix=sufs[key]
            m.append([weights(p+suffix)[ch] if labels(p+suffix)==tag else 0 for p in paths])
        det=det_mod(m)
        assert det==block['minor_mod_p'] and det!=0,(name,d,det)
        total+=rank;minors+=1
        if rank!=expected:fail.append((d,expected-rank))
    assert total==data['real_mod_rank'] and sum(3*x for x in form.values())==data['formal_rank']
    assert total==data['formal_rank']-(12 if n==2*h+2 else 0)
    return {'file':name,'rank':total,'formal_rank':data['formal_rank'],'nonzero_literal_minors':minors,
            'deficits':[(list(d),v) for d,v in fail]}

def main():
    summary={'schema':'EC49CM_INDEPENDENT_LITERAL_AUDIT_V1','prime':P,'certificates':[],'native_brc':[]}
    for upto in (False,True):
        for n in (16,18):
            result=audit_one(7,upto,n)
            summary['certificates'].append(result)
            print('AUDIT',result,flush=True)
    for n in (16,18):
        z=(0,)*6
        values=[endpoint_weight(n,z,w,(1,)*6) for w in W]
        assert all(v.denominator==1 for v in values)
        total=[int(v) for v in values]+[endpoint_multiplicity(n,z)]
        if n==16:assert total==[14233765517623080,14233765517623080,72729762868620]
        summary['native_brc'].append({'n':n,'origin_weight0':str(total[0]),'origin_weight1':str(total[1]),'origin_count':str(total[2])})
        print('NATIVE',n,total,flush=True)
    (ROOT/'EC49CM_INDEPENDENT_AUDIT.json').write_text(json.dumps(summary,indent=2,ensure_ascii=False)+'\n')
    print('EC49CM INDEPENDENT RECHECK PASS',flush=True)
if __name__=='__main__':main()
