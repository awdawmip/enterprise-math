"""Recheck all four EC49CL literal X6/BRC rank certificates from GitHub .b64.
No imports from generators or previous research code. Exact integer arithmetic only.
Usage: python RECHECK_EC49CL_GITHUB.py [EC49CL_LITERAL_WITNESS_CERTS.tar.xz.b64]
"""
import base64,io,itertools,json,sys,tarfile
from math import prod
from pathlib import Path
P=1000003
W=((2,3,3,2,1,1),(3,2,3,2,1,1))
S={'a':(-1,-1),'b':(-2,-2),'c':(1,2,-1,-2),'d':(2,1,-2,-1)}

def displacement(path):
    z=[0]*6
    for a in path:z[abs(a)-1]+=(1 if a>0 else -1)
    return tuple(z)

def label(path):
    return 2*int(any(x==1 and y==2 for x,y in zip(path,path[1:])))+int(any(x==2 and y==1 for x,y in zip(path,path[1:])))

def weight(path,ch):
    return prod(W[ch][a-1] for a in path if a>0) if ch<2 else 1

def step(q,a):
    x,y=divmod(q,3)
    if x!=2:x=2 if x==1 and a==2 else int(a==1)
    if y!=2:y=2 if y==1 and a==1 else int(a==2)
    return 3*x+y

def terminal(q):return 2*int(q//3==2)+int(q%3==2)

def rank_det(mat):
    a=[[v%P for v in row] for row in mat]
    if not a:return 0,1
    m=len(a); n=len(a[0]); k=0; d=1
    for col in range(n):
        p=next((i for i in range(k,m) if a[i][col]),None)
        if p is None:continue
        if p!=k:a[p],a[k]=a[k],a[p];d=-d
        v=a[k][col]; d=d*v%P; iv=pow(v,-1,P)
        for i in range(k+1,m):
            u=a[i][col]*iv%P
            for j in range(col+1,n):a[i][j]=(a[i][j]-u*a[k][j])%P
            a[i][col]=0
        k+=1
        if k==min(m,n):break
    return k,(d%P if m==n and k==m else 0)

def suffixes(upto):
    for h in range(1 if upto else 6,7):
        for word in itertools.product(S,repeat=h):
            yield ''.join(word),tuple(itertools.chain.from_iterable(S[a] for a in word))

def verify(obj,words):
    n=obj['n']; rank=0; actual_full=0
    assert obj['target_count']==28 and obj['suffix_operation_count']==len(words)
    grouped={}
    for name,word in words.items():
        d=tuple(-z for z in displacement(word))
        out=grouped.setdefault(d,[])
        for tag in range(4):
            row=[]
            for q0 in range(9):
                q=q0
                for a in word:q=step(q,a)
                row.append(int(terminal(q)==tag))
            out.append((name,tag,tuple(row)))
    assert len(grouped)==28
    for b in obj['blocks']:
        d=tuple(b['target']);s=b['rank_bound'];paths=list(map(tuple,b['paths']))
        assert d in grouped and len(paths)==b['actual_mod_rank'] and len(b['selected_rows'])==s
        for p in paths:assert len(p)==n and displacement(p)==d and all(1<=abs(a)<=6 for a in p)
        mat=[]
        for name,tag,ch in b['selected_rows']:
            assert name in words and tuple(-x for x in displacement(words[name]))==d
            mat.append([weight(p+words[name],ch) if label(p+words[name])==tag else 0 for p in paths])
        r,det=rank_det(mat)
        assert r==b['actual_mod_rank'] and det==b['minor_mod_p'],(n,d,r,det)
        formal=rank_det([row for _,_,row in grouped[d]])[0]
        assert formal*3==s,(n,d,formal,s)
        rank+=r;actual_full+=int(r==s)
    assert len(obj['blocks'])==28 and rank==obj['real_path_mod_rank']
    assert (n,rank,actual_full) in ((14,381,26),(14,441,26),(16,393,28),(16,453,28))
    print('PASS',n,'suffix words',len(words),'rational-rank lower bound',rank,'full fibers',actual_full)

def main():
    file=Path(sys.argv[1]) if len(sys.argv)>1 else Path(__file__).with_name('EC49CL_LITERAL_WITNESS_CERTS.tar.xz.b64')
    encoded=file.read_text().strip()
    with tarfile.open(fileobj=io.BytesIO(base64.b64decode(encoded)),mode='r:xz') as t:
        for n in (14,16):
            for kind in ('S6','SLE6'):
                name='CERT_EC49CL_'+kind+'_n'+str(n)+'.json'
                obj=json.load(t.extractfile(name))
                words=dict(suffixes(kind=='SLE6'))
                verify(obj,words)
    print('All four actual-path integer-minor certificates verified; no independent Driver admission claimed.')
if __name__=='__main__':main()
