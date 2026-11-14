"""EC49DB self-contained exact native signed-X6 / positive BRC verifier.
Python 3 standard library. Run beside EC49DB_SEEDS.json.zlib.b64.
"""
import base64, json, zlib
from pathlib import Path
P = 1000003
O = {'a':(-1,-1),'b':(-2,-2),'c':(1,2,-1,-2),
     'd':(2,1,-2,-1),'e':(3,1,1,-3)}
W = ((2,3,3,2,1,1),(3,2,3,2,1,1))
def word(w): return tuple(t for a in w for t in O[a])
def ep(p):
    z=[0]*6
    for a in p:
        assert type(a)==int and 1<=abs(a)<=6
        z[abs(a)-1]+=1 if a>0 else -1
    return tuple(z)
def tag(p):
    return 2*int(any(x==1 and y==2 for x,y in zip(p,p[1:])))+int(any(x==2 and y==1 for x,y in zip(p,p[1:])))
def weight(p):
    a=b=1
    for t in p:
        if t>0: a*=W[0][t-1];b*=W[1][t-1]
    return a,b,1
def mat(paths,rows):
    out=[]
    for s,lab in rows:
        suff=word(s)
        ws=[weight(tuple(p)+suff) if tag(tuple(p)+suff)==lab else (0,0,0) for p in paths]
        for j in range(3):out.append([w[j] for w in ws])
    return out
def det(a):
    a=[[v%P for v in row] for row in a];n=len(a);d=1
    assert all(len(row)==n for row in a)
    for j in range(n):
        k=next((i for i in range(j,n) if a[i][j]),None)
        if k is None:return 0
        if k!=j:a[k],a[j]=a[j],a[k];d=-d
        q=a[j][j];d=d*q%P;t=pow(q,-1,P)
        for i in range(j+1,n):
            if a[i][j]:
                r=a[i][j]*t%P
                for l in range(j+1,n):a[i][l]=(a[i][l]-r*a[j][l])%P
                a[i][j]=0
    return d%P

def lift(seed,s,v,h):
    mode,h0,(x0,y0)=seed['language'],seed['h'],seed['target']
    q=x0//2
    assert v>=0 and abs(s)+v<h
    if q==1: assert s>=1; x=s-1;y=v; tail='a'*x+'b'*y
    elif q==-1: assert s<=-1;x=-s-1;y=v;tail='e'*x+'b'*y
    elif y0==2: assert s==0 and v>=1;x=0;y=v-1;tail='b'*y
    else: assert (x0,y0)==(0,0);x=abs(s);y=v;tail=('a'*s if s>0 else 'e'*(-s))+'b'*v
    ax=(q if q else (1 if s>0 else -1))
    b1=[ax]*(2*x);b2=[2]*(2*y)
    dh=h-(h0+x+y)
    assert dh>=0 and (mode=='le' or dh%2==0)
    if mode=='eq':tail+='ae'*(dh//2)
    neutral=[-3,3]*dh
    paths=[neutral+b1+[-3]+b2+[3]+p[2:] for p in seed['paths']]
    rows=[[w+tail,lab] for w,lab in seed['rows']]
    assert all(len(p)==2*h+8 and ep(p)==(2*s,2*v,0,0,0,0) for p in paths)
    assert all(ep(word(w))==(-2*s,-2*v,0,0,0,0) and
               (len(w)==h if mode=='eq' else len(w)<=h) for w,lab in rows)
    a=weight(b1+b2);b=weight(word(tail));c=weight(neutral)
    return paths,rows,tuple(a[i]*b[i]*c[i] for i in range(3))

def main():
    p=Path(__file__).with_name('EC49DB_SEEDS.json.zlib.b64')
    seeds=json.loads(zlib.decompress(base64.b64decode(p.read_text().strip())))
    assert len(seeds)==9
    data={}
    for r in seeds:
        k=(r['language'],r['h'],tuple(r['target']))
        assert k not in data
        R=len(r['rows']);assert len(r['paths'])==3*R
        assert R==(6 if k[0]=='le' or k==('eq',2,(0,0)) else 5)
        for path in r['paths']:
            assert len(path)==2*r['h']+8 and path[:2]==[-3,3]
            assert ep(path)==(*r['target'],0,0,0,0)
        for w,lab in r['rows']:
            assert ep(word(w))==(-r['target'][0],-r['target'][1],0,0,0,0)
            assert (len(w)==r['h'] if k[0]=='eq' else 1<=len(w)<=r['h'])
        d=det(mat(r['paths'],r['rows']));assert d!=0
        data[k]=(r,d)
    assert sum(len(x[0]['paths']) for x in data.values())==150
    checked=0
    for h in range(2,13):
        eq=le=0
        for s in range(-h+1,h):
            for v in range(h-abs(s)):
                k=abs(s)+v
                base=(2,0) if s>0 else (-2,0) if s<0 else (0,2) if v else (0,0)
                for mode in ('eq','le'):
                    if mode=='le':key=('le',2,base)
                    elif (h-k)%2==0:key=('eq',2,(0,0))
                    elif k==0:key=('eq',3,(0,0))
                    else:key=('eq',2,base)
                    seed,d0=data[key]
                    paths,rows,scale=lift(seed,s,v,h)
                    actual=det(mat(paths,rows))
                    expected=d0*pow(scale[0]*scale[1],len(rows),P)%P
                    assert actual==expected!=0,(h,s,v,mode)
                    checked+=1
                    if mode=='eq':eq+=3*len(rows)
                    else:le+=3*len(rows)
        assert eq+12*(2*h+1)==3*(11*h*h+15*h+8)//2
        assert le+12*(2*h+1)==18*h*h+24*h+12
    print(json.dumps({'status':'PASS','literal_seed_paths':150,'nonzero_seed_minors':9,
      'finite_lift_minors_h2_through_h12':checked,'prime':P,
      'seed_det_mod':{str(k):x[1] for k,x in data.items()}},sort_keys=True))
if __name__=='__main__':main()
