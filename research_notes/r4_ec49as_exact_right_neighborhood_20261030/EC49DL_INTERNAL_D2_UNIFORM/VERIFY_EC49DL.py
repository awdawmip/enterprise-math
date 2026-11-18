#!/usr/bin/env python3
"""EC49DL: native signed-X6/BRC exact internal D=+2E1 local saturation.

This executable checks frozen literal path witnesses, independently rebuilds the
real full future-return observer, exact determinants, parity extensions, and a
finite *exhaustive* shorter-prefix bound. stdlib only.
"""
from __future__ import annotations
import itertools
import json
from fractions import Fraction
from math import factorial
from pathlib import Path
import native_signed_brc as native

HERE = Path(__file__).resolve().parent
OPS={'a':(-1,-1),'b':(-2,-2),'c':(1,2,-1,-2),'d':(2,1,-2,-1),'e':(3,1,1,-3)}
D=(2,0,0,0,0,0);ZERO=(0,)*6
X=(2,3,1,2,3,4);Y=(5,7,3,5,7,9)
P=(1000003,1000033)

def endpoint(word):
    return tuple(sum((1 if a>0 else -1) for a in word if abs(a)==j) for j in range(1,7))

def tags(word):
    return (2 if any(a==1 and b==2 for a,b in zip(word,word[1:])) else 0) | (1 if any(a==2 and b==1 for a,b in zip(word,word[1:])) else 0)

def weights(word):
    u=v=1
    for a in word:
        if a>0:u*=X[a-1];v*=Y[a-1]
    return (u,v,1)

def suffix(w):return tuple(z for c in w for z in OPS[c])

def future(h, cumulative=False):
    lengths=range(1,h+1) if cumulative else [h]
    return tuple(''.join(v) for k in lengths for v in itertools.product(OPS,repeat=k) if endpoint(suffix(''.join(v)))==tuple(-z for z in D))

def observable_row(word,coords):
    out=[]
    for z in coords:
        p=tuple(word)+suffix(z['suffix'])
        out.append(weights(p)[z['channel']] if tags(p)==z['tag'] else 0)
    return out

def feature(word):
    t=tags(word)
    ff=[int(t==k) for k in range(4)]
    ff.extend([int(not t&2 and word and word[-1]==1),int(not t&1 and word and word[-1]==2)])
    return tuple(ff)

def feature_row(word):
    ww=weights(word)
    return tuple(q*v for q in feature(word) for v in ww)

def rankQ(rows):
    piv={}
    for r in rows:
        v=list(map(Fraction,r))
        for j,w in sorted(piv.items()):
            if v[j]:
                f=v[j]
                for k in range(j,len(v)):v[k]-=f*w[k]
        for j,a in enumerate(v):
            if a:
                piv[j]=[b/a for b in v]
                break
    return len(piv)

def rankp(rows, p):
    piv={}
    for r in rows:
        v=[x%p for x in r]
        for j,w in sorted(piv.items()):
            if v[j]:
                f=v[j]
                for k in range(j,len(v)):v[k]=(v[k]-f*w[k])%p
        for j,a in enumerate(v):
            if a:
                inv=pow(a,-1,p)
                piv[j]=[b*inv%p for b in v]
                break
    return len(piv)

def detZ(rows):
    a=[list(map(int,row)) for row in rows]
    n=len(a); assert n and all(len(v)==n for v in a)
    sign=1;prev=1
    for k in range(n-1):
        q=next((i for i in range(k,n) if a[i][k]), None)
        if q is None:return 0
        if q!=k:a[k],a[q]=a[q],a[k];sign=-sign
        pivot=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                z=a[i][j]*pivot-a[i][k]*a[k][j]
                assert z%prev==0
                a[i][j]=z//prev
            a[i][k]=0
        prev=pivot
    return sign*a[-1][-1]

def pre8_words(m):
    # Unique exact 6-component endpoint D=+2E1; negatives use multiset N,
    # positive multiset N union {E1,E1}. Every word occurs exactly once.
    for neg in itertools.combinations_with_replacement(range(1,7),m):
        seq=neg+(1,1)+tuple(-i for i in neg)
        yield from set(itertools.permutations(seq))

def selected_matrix(cert, key):
    spec=cert['minors'][key]
    rows=[cert['paths'][idx] for idx in spec['path_indices']]
    coords=spec['coordinates']
    return [observable_row(w,coords) for w in rows]

def main():
    data=json.loads((HERE/'EC49DL_WITNESS.json').read_text())
    assert data['reference']['X']==list(X) and data['reference']['Y']==list(Y)
    assert data['reference']['D']==list(D) and data['reference']['prefix_length']==8
    assert data['reference']['operations']=={k:list(v) for k,v in OPS.items()}
    paths=[tuple(w) for w in data['paths']]
    assert len(paths)==18 and len(set(paths))==18
    assert all(len(w)==8 and endpoint(w)==D and all(1<=abs(a)<=2 for a in w) for w in paths)
    H=[(1,0,0,0,0,0),(0,1,0,0,0,0),(0,0,1,0,0,0),
       (0,0,0,1,0,0),(1,0,0,0,1,0),(1,0,0,0,0,1)]
    assert data['history_basis']==[list(v) for v in H]
    assert data['positive_E1_counts']==[2,3,4]*6
    assert all(feature(paths[3*i+j])==H[i] and sum(z==1 for z in paths[3*i+j])==j+2
               for i in range(6) for j in range(3))
    assert rankQ([feature_row(w) for w in paths])==18
    instr=[weights(paths[j]) for j in range(3)]
    det_gate=detZ(instr)
    assert det_gate!=0
    horizons={'even_h2':(2,False,15),'odd_h3':(3,False,18),'cumulative_h2':(2,True,18)}
    minor_report={}
    for name,(h,cumulative,expected) in horizons.items():
        spec=data['minors'][name]; rs=spec['coordinates']; ps=spec['path_indices']
        assert len(rs)==len(ps)==expected
        label_coordinates=[{'suffix':z['suffix'],'tag':z['tag'],'channel':2} for z in rs[::3]]
        label_matrix=[observable_row(paths[3*i],label_coordinates) for i in range(6)]
        assert rankQ(label_matrix)==expected//3
        assert len(set(ps))==expected and all(0<=j<len(paths) for j in ps)
        assert len(rs)%3==0
        fut=set(future(h,cumulative))
        for i in range(0,len(rs),3):
            g=rs[i:i+3]
            assert all(z['suffix'] in fut and z['tag'] in range(4) for z in g)
            assert len({(z['suffix'],z['tag']) for z in g})==1
            assert [z['channel'] for z in g]==[0,1,2]
        mat=selected_matrix(data,name)
        det=detZ(mat)
        assert det!=0 and str(det)==spec['determinant']
        assert all(det%p==spec['residues'][str(p)]!=0 for p in P)
        minor_report[name]={'rank_lower':expected,'determinant':str(det),'residues':{str(p):det%p for p in P},'columns':len(rs)}
    future_h2=future(2,False);future_h3=future(3,False);future_c2=future(2,True)
    assert future_h2==('ac','ad','ca','da')
    assert all(a in future_h3 for a in ('aae','aea','eaa'))
    assert set(future_c2)=={'a','ac','ad','ca','da'}
    below=[]
    for m in range(3):
        n=2+2*m
        ws=list(pre8_words(m))
        assert all(endpoint(w)==D and len(w)==n for w in ws)
        assert len(set(ws))==len(ws)
        assert len(ws)==native.endpoint_multiplicity(n,D)
        wx=sum(weights(w)[0] for w in ws)
        wy=sum(weights(w)[1] for w in ws)
        assert wx==native.endpoint_weight(n,D,X,(1,)*6)
        assert wy==native.endpoint_weight(n,D,Y,(1,)*6)
        unique={feature_row(w) for w in ws}
        rk=rankQ(unique)
        assert rk=={2:1,4:8,6:14}[n]
        below.append({'n':n,'all_paths':len(ws),'distinct_feature_rows':len(unique),
         'full_six_feature_rank_over_Q':rk,'aggregate_BRC_x':wx,'aggregate_BRC_y':wy})
    assert endpoint(suffix('ae'))==ZERO and tags(suffix('ae'))==0
    assert weights(suffix('ae'))==(4,75,1)
    lift=[]
    for h in range(2,10):
        name='even_h2' if h%2==0 else 'odd_h3'
        base=2 if h%2==0 else 3;k=(h-base)//2
        src=data['minors'][name]
        ps=[paths[idx] for idx in src['path_indices']]
        coords=[dict(z,suffix=z['suffix']+'ae'*k) for z in src['coordinates']]
        assert all(len(q['suffix'])==h and endpoint(suffix(q['suffix']))==tuple(-i for i in D) for q in coords)
        det=detZ([observable_row(w,coords) for w in ps])
        target=int(src['determinant'])*300**(k*(len(coords)//3))
        assert det==target and det!=0
        lift.append({'h':h,'rank_lower':len(coords),'determinant_scale_power_300':k*(len(coords)//3)})
    result={'id':'EC49DL','status':'PASS','weight_three_point_gate_det':str(det_gate),
     'exact_observer_minors':minor_report,
     'exhaustive_shorter_prefixes':below,'tested_analytic_lift_lengths':lift,
     'future_suffix_sizes':{'h2_exact':len(future_h2),'h3_exact':len(future_h3),'h2_cumulative':len(future_c2)},
     'proof_scope':'author-side native signed X6 / positive affine BRC reference at D=2E1; all h>=2 via analytic lift, exact prefix ranks for n=2/4/6',
     'admission':'PORTABLE_DRAFT / REGISTER_PENDING / UNREVIEWED / NOT_ADMITTED'}
    print(json.dumps(result,ensure_ascii=False,sort_keys=True,indent=2))
    if __name__=='__main__':(HERE/'EC49DL_EXECUTED.json').write_text(json.dumps(result,ensure_ascii=False,sort_keys=True,indent=2)+'\n')

if __name__=='__main__':main()
