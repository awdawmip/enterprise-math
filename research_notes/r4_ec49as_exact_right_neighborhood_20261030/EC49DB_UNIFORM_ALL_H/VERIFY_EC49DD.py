"""EC49DD: genuine signed-X6 positive BRC rank strata, exact mod-prime witnesses.
Python 3 standard library; run beside EC49DB_SEEDS.json.zlib.b64, or with
--seeds PATH. No scientific computation outside the declared positive BRC.
"""
import argparse
import base64
import json
import zlib
from pathlib import Path

MOD = 1000003
W = (2, 3, 3, 2, 1, 1)
OPS = {'a':(-1,-1),'b':(-2,-2),'c':(1,2,-1,-2),
       'd':(2,1,-2,-1),'e':(3,1,1,-3)}
GADGET = {0:('1111','3111'),1:('3211','2111'),
          2:('1112','1122'),3:('1211','2121')}

def word(ops):
    return tuple(step for symbol in ops for step in OPS[symbol])

def endpoint(path):
    out=[0]*6
    for step in path:
        assert isinstance(step,int) and step and abs(step)<=6
        out[abs(step)-1] += 1 if step>0 else -1
    return tuple(out)

def tag(path):
    pairs = set(zip(path,path[1:]))
    return 2*int((1,2) in pairs)+int((2,1) in pairs)

def weight(path):
    ans=1
    for step in path:
        if step>0: ans*=W[step-1]
    return ans

def rank_pivots(a):
    a=[[int(x)%MOD for x in row] for row in a]
    if not a:return 0,[]
    n=len(a);cols=len(a[0]);piv=[]
    assert all(len(row)==cols for row in a)
    for c in range(cols):
        r=len(piv)
        if r>=n:break
        k=next((i for i in range(r,n) if a[i][c]),None)
        if k is None:continue
        a[r],a[k]=a[k],a[r]
        z=pow(a[r][c],-1,MOD)
        a[r]=[(x*z)%MOD for x in a[r]]
        for i in range(r+1,n):
            if a[i][c]:
                z=a[i][c]
                a[i]=[(u-z*v)%MOD for u,v in zip(a[i],a[r])]
        piv.append(c)
    return len(piv),piv

def determinant(a):
    a=[[int(x)%MOD for x in row] for row in a]
    n=len(a);assert all(len(row)==n for row in a)
    out=1
    for c in range(n):
        k=next((i for i in range(c,n) if a[i][c]),None)
        if k is None:return 0
        if k!=c:a[k],a[c]=a[c],a[k];out=-out
        v=a[c][c];out=out*v%MOD
        inv=pow(v,-1,MOD)
        for i in range(c+1,n):
            if a[i][c]:
                scale=a[i][c]*inv%MOD
                for j in range(c+1,n):a[i][j]=(a[i][j]-scale*a[c][j])%MOD
                a[i][c]=0
    return out%MOD

def observation(paths,rows,mode):
    """One row per final-tag/complete suffix, with distinct positive-weight/count channels."""
    out=[]
    for symbols,target_tag in rows:
        suffix=word(symbols)
        entries=[(tag(tuple(p)+suffix)==target_tag, weight(tuple(p)+suffix)) for p in paths]
        if mode=='count':
            out.append([int(v) for v,_ in entries])
        elif mode=='weight_count':
            out.append([wt if valid else 0 for valid,wt in entries])
            out.append([int(valid) for valid,_ in entries])
        else:raise ValueError(mode)
    return out

def lift(seed,s,v,h):
    mode,h0,(x0,y0)=seed['language'],seed['h'],seed['target']
    q=x0//2
    assert v>=0 and abs(s)+v<h
    if q==1:
        assert s>=1; x=s-1;y=v;tail='a'*x+'b'*y
    elif q==-1:
        assert s<=-1;x=-s-1;y=v;tail='e'*x+'b'*y
    elif y0==2:
        assert s==0 and v>=1;x=0;y=v-1;tail='b'*y
    else:
        assert (x0,y0)==(0,0);x=abs(s);y=v
        tail=('a'*s if s>0 else 'e'*(-s))+'b'*v
    ax=(q if q else (1 if s>0 else -1))
    b1=[ax]*(2*x); b2=[2]*(2*y)
    dh=h-(h0+x+y)
    assert dh>=0 and (mode=='le' or dh%2==0)
    if mode=='eq':tail+='ae'*(dh//2)
    paths=[[-3,3]*dh+b1+[-3]+b2+[3]+p[2:] for p in seed['paths']]
    rows=[(w+tail,lab) for w,lab in seed['rows']]
    assert all(len(p)==2*h+8 and endpoint(p)==(2*s,2*v,0,0,0,0) for p in paths)
    assert all(endpoint(word(w))==(-2*s,-2*v,0,0,0,0) and
               (len(w)==h if mode=='eq' else 1<=len(w)<=h) for w,lab in rows)
    return paths,rows

def boundary_path(u,v,lab,variant):
    assert u>0 and v>0 and variant in (0,1)
    A=[1]*(2*u);B=[2]*(2*v)
    one1=[1,-1] if variant==1 else []
    filler=[3,-3]*(4-variant)
    if lab==0:p=A+one1+filler+B
    elif lab==1:p=B[:-1]+B[-1:]+A+one1+filler
    elif lab==2:p=A[:-1]+one1+A[-1:]+B+filler
    elif lab==3:p=A[:-2]+one1+A[-2:-1]+B[:-1]+[1,2]+filler
    else:raise ValueError(lab)
    assert len(p)==2*(u+v)+8 and endpoint(p)==(2*u,2*v,0,0,0,0) and tag(p)==lab
    return p

def boundary_family(s,v,h):
    assert abs(s)+v==h and v>=0
    out=[]
    if s>0 and v>0:
        for lab in range(4):
            for var in (0,1):out.append(boundary_path(s,v,lab,var))
        suffix='a'*s+'b'*v
    elif s<=0:
        u=-s
        suffix='e'*u+'b'*v
        for lab in range(4):
            for g in GADGET[lab]:
                core=[int(c) for c in g]
                out.append([-1]*(2*u)+core+[-c for c in core]+[2]*(2*v))
    else: # positive-E1 corner
        assert s==h and v==0
        suffix='a'*h
        for lab in range(4):
            for g in GADGET[lab]:
                core=[int(c) for c in g]
                out.append(core+[-c for c in core]+[1]*(2*h))
    assert all(len(p)==2*h+8 and endpoint(p)==(2*s,2*v,0,0,0,0)
               for p in out)
    assert [tag(p) for p in out] == [v for v in range(4) for _ in range(2)]
    assert endpoint(word(suffix))==(-2*s,-2*v,0,0,0,0)
    return out,[(suffix,lab) for lab in range(4)]

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--seeds',type=Path,default=Path(__file__).with_name('EC49DB_SEEDS.json.zlib.b64'))
    args=parser.parse_args()
    seeds=json.loads(zlib.decompress(base64.b64decode(args.seeds.read_text().strip(),validate=True)))
    assert len(seeds)==9
    data={};cert=[]
    for seed in seeds:
        mode,h0,target=seed['language'],seed['h'],tuple(seed['target'])
        k=(mode,h0,target);assert k not in data
        paths,rows=seed['paths'],seed['rows'];r=len(rows)
        assert len(paths)==3*r
        assert all(len(p)==2*h0+8 and endpoint(p)==(*target,0,0,0,0) for p in paths)
        assert all(endpoint(word(w))==(-target[0],-target[1],0,0,0,0) for w,_ in rows)
        T=observation(paths,rows,'count')
        M=observation(paths,rows,'weight_count')
        rt,pivot_t=rank_pivots(T)
        rw,pivot_w=rank_pivots(M)
        assert rt==r and rw==2*r,(k,rt,rw)
        d_t=determinant([[a[j] for j in pivot_t] for a in T])
        d_w=determinant([[a[j] for j in pivot_w] for a in M])
        assert d_t and d_w
        cert.append({'mode':mode,'h':h0,'target':list(target),'tag_rank':rt,
                     'weight_count_rank':rw,'tag_pivots_0based':pivot_t,
                     'weight_count_pivots_0based':pivot_w,
                     'tag_det_mod':d_t,'weight_count_det_mod':d_w})
        data[k]=seed
    tested_interior=0;tested_boundary=0;counts_by_h={}
    for h in range(2,13):
        per_h={'exact_rank_count':0,'cumulative_rank_count':0,
               'exact_rank_2channel':0,'cumulative_rank_2channel':0,
               'interior_fibers':0,'boundary_fibers':0}
        for s in range(-h,h+1):
            for v in range(h-abs(s)+1):
                defect=h-abs(s)-v
                if defect==0:
                    paths,rows=boundary_family(s,v,h)
                    T=observation(paths,rows,'count')
                    M=observation(paths,rows,'weight_count')
                    assert rank_pivots(T)[0]==4
                    assert determinant(M)!=0
                    tested_boundary+=1
                    for key in ('exact_rank_count','cumulative_rank_count'):per_h[key]+=4
                    for key in ('exact_rank_2channel','cumulative_rank_2channel'):per_h[key]+=8
                else:
                    per_h['interior_fibers']+=1
                    base=(2,0) if s>0 else (-2,0) if s<0 else (0,2) if v else (0,0)
                    for mode in ('eq','le'):
                        if mode=='le':key=('le',2,base)
                        elif defect%2==0:key=('eq',2,(0,0))
                        elif s==0 and v==0:key=('eq',3,(0,0))
                        else:key=('eq',2,base)
                        p,rr=lift(data[key],s,v,h)
                        T=observation(p,rr,'count')
                        M=observation(p,rr,'weight_count')
                        r=len(rr)
                        assert rank_pivots(T)[0]==r
                        assert rank_pivots(M)[0]==2*r
                        tested_interior+=1
                        if mode=='eq':per_h['exact_rank_count']+=r;per_h['exact_rank_2channel']+=2*r
                        else:per_h['cumulative_rank_count']+=r;per_h['cumulative_rank_2channel']+=2*r
        assert per_h['exact_rank_count']==(11*h*h+15*h+8)//2
        assert per_h['cumulative_rank_count']==6*h*h+8*h+4
        assert per_h['exact_rank_2channel']==11*h*h+15*h+8
        assert per_h['cumulative_rank_2channel']==12*h*h+16*h+8
        counts_by_h[str(h)]=per_h
    # Additional boundary-only h beyond interior finite-check range.
    for h in range(13,31):
        for s in range(-h,h+1):
            v=h-abs(s)
            paths,rows=boundary_family(s,v,h)
            M=observation(paths,rows,'weight_count')
            assert determinant(M)!=0
            tested_boundary+=1
    print(json.dumps({'status':'PASS','modulus':MOD,'weight_vector':W,
         'seed_certificate':cert,
         'checked_interior_mode_fibers_h2_to12':tested_interior,
         'checked_boundary_fibers_h2_to30':tested_boundary,
         'rank_formulas_checked_h2_to12':counts_by_h},sort_keys=True))
if __name__=='__main__':main()
