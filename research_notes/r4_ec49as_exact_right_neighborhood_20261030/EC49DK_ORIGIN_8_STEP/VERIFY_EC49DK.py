#!/usr/bin/env python3
"""EC49DK: exact native X6 / positive BRC finite future observer certificate.

Self-contained, Python 3 standard-library, exact integers and Fraction. Rebuilds
both entire h=2 D=0 future languages; checks all native words of lengths 0,2,4,6,
and verifies an explicit length-8 rational full-rank 18x18 minor.
"""
from __future__ import annotations
import hashlib
import itertools
import json
from collections import Counter
from fractions import Fraction
from pathlib import Path
from math import factorial

ROOT = Path(__file__).resolve().parent
P = (1000003, 1000033)
OPERATIONS = {
    'a':(-1,-1), 'b':(-2,-2), 'c':(1,2,-1,-2),
    'd':(2,1,-2,-1), 'e':(3,1,1,-3)
}
X = (2,3,1,2,3,4)
Y = tuple(2*t+1 for t in X)


def ep(word):
    return tuple(sum((1 if a>0 else -1) for a in word if abs(a)==j) for j in range(1,7))


def tags(word):
    aa = any(u==1 and v==2 for u,v in zip(word,word[1:]))
    bb = any(u==2 and v==1 for u,v in zip(word,word[1:]))
    return 2*int(aa)+int(bb)


def weight(word):
    a=b=1
    for j in word:
        if j>0:
            a*=X[j-1];b*=Y[j-1]
    return (a,b,1)


def suffix(word):
    return tuple(z for k in word for z in OPERATIONS[k])


def return_suffixes(h, cumulative):
    words=[]
    lengths=range(1,h+1) if cumulative else (h,)
    for m in lengths:
        for w in itertools.product(OPERATIONS,repeat=m):
            q=''.join(w)
            if ep(suffix(q))==(0,)*6:words.append(q)
    return tuple(words)


def feature(word):
    t=tags(word)
    f=[int(t==i) for i in range(4)]
    f.append(int((t&2)==0 and bool(word) and word[-1]==1))
    f.append(int((t&1)==0 and bool(word) and word[-1]==2))
    return tuple(f)


def feature_row(word):
    v=weight(word)
    return tuple(a*b for a in feature(word) for b in v)


def full_row(word, future):
    out=[]
    for s in future:
        path=tuple(word)+suffix(s)
        t=tags(path);ws=weight(path)
        for j in range(4):out.extend(ws if t==j else (0,0,0))
    return tuple(out)


def rank_rational(rows):
    pivots={}
    for row in rows:
        v=list(map(Fraction,row))
        for col,u in sorted(pivots.items()):
            c=v[col]
            if c:
                for j in range(col,len(v)):v[j]-=c*u[j]
        for col,z in enumerate(v):
            if z:
                pivots[col]=[t/z for t in v]
                break
    return len(pivots)


def det_exact(a):
    """Fraction-free Bareiss algorithm with exact integer divisions."""
    a=[list(map(int,r)) for r in a]
    n=len(a);assert n and all(len(r)==n for r in a)
    prev=1;sign=1
    for k in range(n-1):
        r=next((j for j in range(k,n) if a[j][k]),None)
        if r is None:return 0
        if r!=k:a[k],a[r]=a[r],a[k];sign*=-1
        p=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                num=a[i][j]*p-a[i][k]*a[k][j]
                assert num%prev==0
                a[i][j]=num//prev
            a[i][k]=0
        prev=p
    return sign*a[-1][-1]


def native_words(m):
    # Each zero-return native word has a unique six-axis positive multiset.
    if m==0:
        yield tuple();return
    for axes in itertools.combinations_with_replacement(range(1,7),m):
        steps=axes+tuple(-q for q in axes)
        yield from set(itertools.permutations(steps))


def native_aggregate(n, positive_weights):
    # Closed signed X6 path multinomial BRC aggregate, no floating point.
    m=n//2;total=0;mass=0
    for ks in itertools.product(range(m+1),repeat=6):
        if sum(ks)!=m:continue
        mult=factorial(n)
        for k in ks:mult//=1 # just keep integer until joint denominator constructed
        denom=1
        for k in ks:denom*=factorial(k)**2
        assert mult%denom==0
        term=mult//denom
        total+=term
        w=term
        for k,t in zip(ks,positive_weights):w*=t**k
        mass+=w
    return total,mass


def g_feature_row(word):
    # All odd-h zero-return suffixes contain at least one c or d.
    # Five response features: 1, B_absent, A_absent, seam_A, seam_B.
    f=feature(word); v=weight(word)
    g=(1,f[0]+f[2],f[0]+f[1],f[4],f[5])
    return tuple(a*b for a in g for b in v)


def matrix_from_witness(data):
    assert data['model']['native_signed_spatial_axes']==6
    assert data['model']['prefix_length']==8
    assert data['model']['prefix_endpoint']==[0]*6
    assert data['model']['operation_horizon']==2
    assert tuple(data['model']['positive_BRC_weights_x'])==X
    assert tuple(data['model']['positive_BRC_weights_y'])==Y
    assert data['model']['operators']=={k:list(v) for k,v in OPERATIONS.items()}
    future=return_suffixes(2,False)
    assert data['model']['returning_suffixes_exact']==list(future)
    paths=[tuple(p) for p in data['paths']]
    labels=data['rows']
    assert len(paths)==18 and len(set(paths))==18 and len(labels)==18
    assert len(set((x['operation_word'],x['joint_tag'],x['channel']) for x in labels))==18
    for p in paths:
        assert len(p)==8 and ep(p)==(0,)*6 and sum(z>0 for z in p)==4
        assert all(1<=abs(z)<=6 for z in p)
    assert all(r['operation_word'] in future and 0<=r['joint_tag']<=3 and 0<=r['channel']<=2 for r in labels)
    return [[weight(p+suffix(r['operation_word']))[r['channel']]
             if tags(p+suffix(r['operation_word']))==r['joint_tag'] else 0
             for r in labels] for p in paths]


def main():
    source_path=ROOT/'EC49DK_WITNESS.json'
    d=json.loads(source_path.read_text())
    exact=return_suffixes(2,False)
    cumul=return_suffixes(2,True)
    assert exact==('ae','cc','cd','dc','dd','ea'),exact
    assert cumul==('c','d','ae','cc','cd','dc','dd','ea'),cumul
    assert all(ep(suffix(z))==(0,)*6 for z in cumul)
    fdict={}
    for m in range(4):
        words=list(native_words(m)); n=2*m
        assert len(words)==len(set(words))
        assert all(ep(w)==(0,)*6 and len(w)==n for w in words)
        fr={feature_row(w) for w in words}
        er={full_row(w,exact) for w in words}
        cr={full_row(w,cumul) for w in words}
        rf=rank_rational(fr);re=rank_rational(er);rc=rank_rational(cr)
        assert rf==re==rc
        assert (rf,re,rc)=={0:(1,1,1),1:(4,4,4),2:(9,9,9),3:(15,15,15)}[m]
        gr={g_feature_row(w) for w in words}
        rg=rank_rational(gr)
        assert rg=={0:1,1:4,2:9,3:13}[m]
        count,wx=native_aggregate(n,X)
        count2,wy=native_aggregate(n,Y)
        assert count==count2==len(words)
        assert sum(weight(w)[0] for w in words)==wx
        assert sum(weight(w)[1] for w in words)==wy
        fdict[str(n)]={'complete_native_words':len(words),'distinct_feature_rows':len(fr),
          'exact_Q_rank_h2':re,'cumulative_Q_rank_h2':rc,
          'odd_h_upper_feature_Q_rank':rg,'native_return_mass':count,
          'BRC_x_return_mass':wx,'BRC_y_return_mass':wy}
    M=matrix_from_witness(d)
    det=det_exact(M)
    assert det==-26018196083657455104000000000000000000, det
    assert all(det%p==d['nonzero_modular_determinants'][str(p)]!=0 for p in P)
    assert rank_rational([feature_row(tuple(w)) for w in d['paths']])==18
    # The same 18 path rows have full rank for exact and cumulative future languages.
    assert rank_rational([full_row(tuple(w),exact) for w in d['paths']])==18
    assert rank_rational([full_row(tuple(w),cumul) for w in d['paths']])==18
    odd=d['odd_h3']
    odd_paths=[tuple(d['paths'][i]) for i in odd['prefix_path_indices']]
    assert len(odd_paths)==15 and len(set(odd_paths))==15
    assert all(len(r['operation_word'])==3 and ep(suffix(r['operation_word']))==(0,)*6 for r in odd['rows'])
    def submatrix(ps,rows,t=''):
        return [[weight(p+suffix(r['operation_word']+t))[r['channel']]
                 if tags(p+suffix(r['operation_word']+t))==r['joint_tag'] else 0
                 for r in rows] for p in ps]
    odd_det=det_exact(submatrix(odd_paths,odd['rows']))
    assert odd_det==int(odd['nonzero_exact_determinant'])==-3902729412548618265600000000000000000000
    assert all(odd_det%p==odd['nonzero_modular_determinants'][str(p)]!=0 for p in P)
    # Exact universal lift: append the tag-inert, zero-displacement 'ae'
    # to every suffix. Since each suffix ends negative, there is no seam tag.
    gate=weight(suffix('ae')); assert gate==(4,75,1) and ep(suffix('ae'))==(0,)*6
    lift_checked=0
    for h in range(2,10):
        if h%2==0:
            k=(h-2)//2; ps=[tuple(z) for z in d['paths']]; rows=d['rows']; baseline=det;size=18
        else:
            k=(h-3)//2; ps=odd_paths;rows=odd['rows'];baseline=odd_det;size=15
        trail='ae'*k
        mat=submatrix(ps,rows,trail)
        assert all(len(r['operation_word']+trail)==h for r in rows)
        assert all(ep(suffix(r['operation_word']+trail))==(0,)*6 for r in rows)
        # All groups carry all three instruments: (Wx,Wy,count).
        assert len(rows)%3==0 and all([r['channel'] for r in rows[i:i+3]]==[0,1,2] for i in range(0,len(rows),3))
        scale=pow(gate[0]*gate[1],k*(size//3))
        assert det_exact(mat)==baseline*scale
        lift_checked+=1
    c,x=native_aggregate(8,X)
    _,y=native_aggregate(8,Y)
    report={'status':'PASS','model':'native_six_signed_X6_positive_integer_BRC',
      'parameters':{'x':X,'y':Y,'affine_relation':'y_i=2*x_i+1','h':2,'D':[0]*6},
      'future_languages':{'exact_2':list(exact),'cumulative_1_to_2':list(cumul)},
      'exhaustive_short_lengths':fdict,
      'length_8_witness':{'native_path_count':18,'coordinate_count_even':18,
        'odd_h3_path_count':15,'odd_h3_coordinate_count':15,
        'odd_h3_determinant':str(odd_det),'odd_h3_mod':{str(p):odd_det%p for p in P},
        'universal_parity_lift_checks_h2_to_h9':lift_checked,
        'analytic_conclusion':'origin fibre saturated at n=8 for exact h>=2 (18 even / 15 odd) and cumulative 1..h (18); not global all-fibre saturation',
        'determinant':str(det),
        'det_mod':{str(p):det%p for p in P},'Q_rank_exact':18,'Q_rank_cumulative':18,
        'aggregate_X6_native_mass':c,'aggregate_BRC_x':x,'aggregate_BRC_y':y},
      'witness_sha256':hashlib.sha256(source_path.read_bytes()).hexdigest(),
      'limitation':'Author-side exact finite observer result, not full all-fibre/all-h or Source-admitted theorem.'}
    (ROOT/'EC49DK_EXECUTED.json').write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n')
    print(json.dumps(report,ensure_ascii=False,sort_keys=True))

if __name__=='__main__':main()
