"""EC49DF, true Q=0 three-channel signed-X6 positive-BRC witnesses.
Requires VERIFY_EC49DD.py, VERIFY_EC49DE_COMPACT.py beside this file.
Python 3 standard library, no mock sign/semantic placement.
"""
from collections import defaultdict
from itertools import combinations
import VERIFY_EC49DD as E
import VERIFY_EC49DE_COMPACT as Tag

MOD=1000003
X=(2,3,5,2,4,1)
Y=(4,5,7,3,9,1)

def positive_weight(path, w):
    v=1
    for a in path:
        if a>0:v*=w[a-1]
    return v

def det_mod(square):
    n=len(square)
    assert all(len(row)==n for row in square)
    z=[[int(a)%MOD for a in row] for row in square]
    ans=1
    for j in range(n):
        q=next((i for i in range(j,n) if z[i][j]),None)
        if q is None:return 0
        if q!=j:z[j],z[q]=z[q],z[j];ans=-ans
        v=z[j][j];ans=ans*v%MOD
        inv=pow(v,-1,MOD)
        for i in range(j+1,n):
            if z[i][j]:
                factor=z[i][j]*inv%MOD
                for k in range(j+1,n):z[i][k]=(z[i][k]-factor*z[j][k])%MOD
                z[i][j]=0
    return ans%MOD

def independent_rows(paths, suffixes):
    rows=[];coeff=[];basis={}
    for future in suffixes:
        v=[E.tag(tuple(p)+future) for p in paths]
        for lab in range(4):
            arr=[int(t==lab) for t in v]
            q=[a%MOD for a in arr]
            for j,b in sorted(basis.items()):
                if q[j]:
                    t=q[j];q=[(a-t*c)%MOD for a,c in zip(q,b)]
            j=next((j for j,a in enumerate(q) if a),None)
            if j is None:continue
            inv=pow(q[j],-1,MOD)
            q=[a*inv%MOD for a in q]
            basis[j]=q
            for i,b in list(basis.items()):
                if i!=j and b[j]:
                    t=b[j];basis[i]=[(a-t*c)%MOD for a,c in zip(b,q)]
            rows.append((future,lab));coeff.append(arr)
            if len(basis)==len(paths):return rows,coeff
    return rows,coeff

def check():
    q=(X[0]-X[2])*(Y[1]-Y[2])-(X[1]-X[2])*(Y[0]-Y[2])
    Gdet=det_mod([X[2:5],Y[2:5],[1,1,1]])
    assert q==0 and Gdet==MOD-10
    assert all(v>0 for v in X+Y)
    assert not all(X[j]*Y[0]==Y[j]*X[0] for j in range(6))
    group={j:Tag.suffixes(j) for j in range(1,8)}
    tested={};count=0;seen=0
    for h in range(2,8):
        cum=defaultdict(list)
        for j in range(1,h+1):
            for d,L in group[j].items():cum[d].extend(L)
        sums=[0,0]; by_h=0
        for s in range(-h,h+1):
            for v in range(h-abs(s)+1):
                start=Tag.paths(h,s,v)
                for mode,language in enumerate((group[h],cum)):
                    suffixes=language[(-2*s,-2*v)]
                    assert suffixes
                    future_rows,count_rows=independent_rows(start,suffixes)
                    delta=h-abs(s)-v
                    expected=4 if delta==0 else 6 if mode==1 or delta%2==0 else 5
                    assert len(future_rows)==expected,(h,s,v,mode,len(future_rows),expected)
                    chosen=None
                    for inds in combinations(range(len(start)),expected):
                        A=[[row[i] for i in inds] for row in count_rows]
                        if det_mod(A):chosen=inds;break
                    assert chosen is not None
                    b=[start[j] for j in chosen]
                    full=[(-ax,ax)+tuple(p) for p in b for ax in (3,4,5)]
                    assert len(full)==3*expected
                    assert all(len(p)==2*h+8 and E.endpoint(p)==(2*s,2*v,0,0,0,0) for p in full)
                    M=[]
                    for suffix,lab in future_rows:
                        sx=positive_weight(suffix,X);sy=positive_weight(suffix,Y)
                        valid=[E.tag(p+suffix)==lab for p in full]
                        M.extend([
                            [int(t)*positive_weight(p,X)*sx for p,t in zip(full,valid)],
                            [int(t)*positive_weight(p,Y)*sy for p,t in zip(full,valid)],
                            [int(t) for t in valid]
                        ])
                    assert det_mod(M)!=0,(h,s,v,mode)
                    by_h+=1;count+=1;sums[mode]+=3*expected
        assert sums==[(3*(11*h*h+15*h+8))//2,18*h*h+24*h+12]
        tested[h]={'exact_dim':sums[0],'cumulative_dim':sums[1],'full_rank_minors':by_h}
    print({'status':'PASS','prime':MOD,'X':X,'Y':Y,'Q':q,'neutral_axis_gadget_det_mod':Gdet,
           'h_range':'2..7','checked_full_rank_minors':count,'dimensions':tested})
if __name__=='__main__':check()
