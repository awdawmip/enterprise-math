#!/usr/bin/env python3
"""Author-side exact R5 low-excess-425 certificate check.

Place SHA-matched frozen EXACT_R5_ALL_101_BUDGETS.json and prior
RESULT_R5_MIXED_ERASURE_RIGIDITY.json alongside this file.
No third-party modules or floats. Counts unordered multisets.
"""
from pathlib import Path
import hashlib, json
P=Path(__file__).resolve().parent
SHA='50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b'
assert hashlib.sha256((P/'EXACT_R5_ALL_101_BUDGETS.json').read_bytes()).hexdigest()==SHA
prev=json.loads((P/'RESULT_R5_MIXED_ERASURE_RIGIDITY.json').read_text())
sets=[set(x) for x in prev['minimal_sets']]
assert sets==[set(range(214,219)),{214,*range(216,222)},{215,*range(216,222)},set(range(223,291)),set(range(296,313))]
O=sorted(set(range(214,315))-set.union(*sets))
assert O==[222,291,292,293,294,295,313,314]
CAP=425
ZERO=[0]*(CAP+1)

def G(n,r):
    if n<0:return ZERO.copy()
    t=[[0]*(CAP+1) for _ in range(n+1)]
    t[0][0]=1
    for w in range(r+1):
        for k in range(1,n+1):
            for v in range(w,CAP+1):
                t[k][v]+=t[k-1][v-w]
    return t[n]
def add(x,y):return [a+b for a,b in zip(x,y)]
def sh(x,k):return [0]*k+x[:CAP+1-k] if k<=CAP else ZERO.copy()
def conv(x,y):
    z=[0]*(CAP+1)
    yy=[(i,v) for i,v in enumerate(y) if v]
    for i,a in enumerate(x):
        if not a:continue
        for j,b in yy:
            if i+j>CAP:break
            z[i+j]+=a*b
    return z

def theoretical(m):
    e,ep,em,emm=G(m,2),G(m+1,2),G(m-1,2),G(m-2,2)
    md,mp=G(m,67),G(m+1,67)
    ld,lp=G(m,16),G(m+1,16)
    ml=conv(md,ld)
    b=conv(e,ml)
    a=ZERO.copy()
    for k in (214,215,219,220,221):a=add(a,sh(e,k))
    a=add(a,sh(ep,216))
    for k in (213,217,218,218,219,219,220):a=add(a,sh(em,k))
    for k in (216,217,218):a=add(a,sh(emm,k))
    z=add(b,conv(a,ml))
    for k in O:z=add(z,sh(b,k))
    z=add(z,sh(conv(conv(e,mp),ld),223))
    z=add(z,sh(conv(conv(e,md),lp),296))
    return z,b

def vectors(total,dim):
    if dim==1:
        yield (total,)
    else:
        for x in range(total+1):
            for y in vectors(total-x,dim-1):yield (x,)+y

def independent_count(m):
    # Independently enumerate bounded partial-price multiplicity vectors,
    # checking all three early cover constraints. Bounds are generous:
    # omitted partial totals >=7 or central deficits >=6 imply cost >425.
    early=ZERO.copy()
    for n in range(7):
      for v in vectors(n,5):
        a,b,d0,d1,d2=v
        d=d0+d1+d2
        priced=sum(x*y for x,y in zip((214,215,219,220,221),v))
        for c in range(max(0,m-5),m+2):
            if min(a+b+c,a+d+c,b+d+c)<m:continue
            delta=priced+216*(c-m)
            if 0<=delta<=CAP:early=add(early,sh(G(c,2),delta))
    ans=ZERO.copy()
    for jm in (0,1):
      for jl in (0,1):
        ml=conv(G(m+jm,67),G(m+jl,16))
        val=conv(early,ml)
        for o in (0,*O):
            delta=223*jm+296*jl+o
            if delta<=CAP:ans=add(ans,sh(val,delta))
    return ans

out={'schema':'R5_NONADAPTIVE_EXACT_LOW_EXCESS_425_V1',
     'science_pin':'awdawmip/enterprise-math@435e77af0d180eac32bd1f9c4c464bc4010b7551',
     'frozen_input_sha256':SHA,'cost_excess_range':[0,425],
     'crosscheck':{},'review':'NOT_REVIEWED'}
for m in (1,2,3,4,8,17):
    z,b=theoretical(m)
    zz=independent_count(m)
    assert z==zz, [(k,x,y) for k,(x,y) in enumerate(zip(z,zz)) if x!=y][:5]
    assert z[:213]==b[:213] and z[213]==b[213]+1
    out['crosscheck'][str(m)]={
        'coefficient_213':str(z[213]),
        'new_off_three_block_at_213':str(z[213]-b[213]),
        'coefficient_425':str(z[425]),
        'total_0_to_425':str(sum(z)),
        'all_426_coefficients_agree':True}
    print('PASS m',m,'coefficient_213',z[213],'coefficient_425',z[425])
(P/'RESULT_R5_LOW_EXCESS_425.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS frozen SHA, five sets, all 426 coefficients for six values of m')
