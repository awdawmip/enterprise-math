#!/usr/bin/env python3
"""General named FF witness search for seven unresolved PREFIX-899 residues."""
import math,json
N=1<<32
rows={510001:[455881,477249,496471,504809],510195:[466453,509983,510499]}
def carry_witness(delta,i,j,si,sj):
    # x + delta = y on 32 unsigned bits, x_i source sign si, y_j sign sj.
    states={0:0} # carry -> minimum witness x low part
    for t in range(32):
        ns={}
        abit=(delta>>t)&1
        for carry,x in states.items():
            for xb in (0,1):
                if t==i and xb!=(0 if si==1 else 1):continue
                ytmp=xb+abit+carry
                yb=ytmp&1
                if t==j and yb!=(0 if sj==1 else 1):continue
                nc=ytmp>>1
                cand=x|(xb<<t)
                if nc not in ns or cand<ns[nc]:ns[nc]=cand
        states=ns
        if not states:return None
    return states.get(0)
def find(a,b):
    g=math.gcd(a,b);m=b//g;K=(N-1)//a
    assert m>K
    inv=pow(a//g,-1,m)
    for i in range(32):
        for j in range(32):
            for si in (1,-1):
                for sj in (1,-1):
                    diff=si*(1<<i)-sj*(1<<j)
                    if diff%g:continue
                    k=((diff//g)*inv)%m
                    if not 1<=k<=K:continue
                    delta=k*a
                    x=carry_witness(delta,i,j,si,sj)
                    if x is None:continue
                    y=x+delta
                    assert 0<=x<y<N and ((x>>i)&1)==(si<0) and ((y>>j)&1)==(sj<0)
                    assert x%a==y%a and (x^(1<<i))%b==(y^(1<<j))%b
                    return {'q1':a,'q2':b,'x':x,'y':y,'bit_i':i,'bit_j':j,'first_end':x^(1<<i),'second_end':y^(1<<j),'first_sign':si,'second_sign':sj,'k':k}
    return None
records=[]
for a,bs in rows.items():
    for b in bs:
        witness=find(a,b)
        records.append({'a':a,'b':b,'witness':witness})
print(json.dumps({'residuals':records,'all_closed':all(r['witness'] is not None for r in records)},indent=2))
