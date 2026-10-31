"""EC49CJ: exact native signed X6 suffix observability / finite-state witness.

Pure Python 3 standard library. Modular linear algebra over prime 1000003,
exact integer weights; no native physical evolution claimed.
"""
import json, time, sys, itertools, hashlib
from collections import defaultdict
from pathlib import Path

P=1_000_003
S={'a':(-1,-1),'b':(-2,-2),'c':(1,2,-1,-2),'d':(2,1,-2,-1)}
W=((2,3,3,2,1,1),(3,2,3,2,1,1))
Z=(0,)*6

def suffixes(h,upto=False):
    return {''.join(k):tuple(itertools.chain.from_iterable(S[x] for x in k))
            for length in range(1 if upto else h,h+1)
            for k in itertools.product(S,repeat=length)}

def advance(q,a):
    qa,qb=divmod(q,3)
    def step(r,first,second):
        return 2 if r==2 or (r==1 and a==second) else int(a==first)
    return 3*step(qa,1,2)+step(qb,2,1)

def follow(q,w):
    for a in w:q=advance(q,a)
    return q

def label(q):return 2*(q//3==2)+(q%3==2)

def displacement(w):
    z=[0]*6
    for a in w:z[abs(a)-1]+=1 if a>0 else -1
    return tuple(z)

def weight(w):
    a=b=1
    for x in w:
        if x>0:
            a*=W[0][x-1]; b*=W[1][x-1]
    return (a,b,1)

def rank_select(rows):
    """Independently pick pivot rows, with raw rows retained for minor check."""
    echelon=[];selected=[]
    for i,row in enumerate(rows):
        v=list(row)
        for p,w in echelon:
            if v[p]:
                f=v[p];v=[(x-f*y)%P for x,y in zip(v,w)]
        p=next((j for j,x in enumerate(v) if x%P),None)
        if p is not None:
            inv=pow(v[p],-1,P)
            echelon.append((p,[x*inv%P for x in v]))
            echelon.sort(key=lambda entry:entry[0])
            selected.append(i)
    return selected


def det_mod(rows):
    a=[list(map(lambda x:x%P,row)) for row in rows]; n=len(a);d=1
    assert all(len(row)==n for row in a)
    for j in range(n):
        k=next((i for i in range(j,n) if a[i][j]),None)
        if k is None:return 0
        if k!=j:a[j],a[k]=a[k],a[j];d=-d
        p=a[j][j]; d=d*p%P; inv=pow(p,-1,P)
        for i in range(j+1,n):
            if a[i][j]:
                f=a[i][j]*inv%P
                for col in range(j+1,n):a[i][col]=(a[i][col]-f*a[j][col])%P
                a[i][j]=0
    return d%P


def row_system(sufs):
    groups=defaultdict(list)
    for suffix_key,s in sufs.items():
        d=tuple(-x for x in displacement(s))
        labs=[label(follow(q,s)) for q in range(9)]
        for a in range(4):
            groups[d].append((suffix_key,a,tuple(int(k==a) for k in labs)))
    result={}
    for d,rows in sorted(groups.items()):
        selected=rank_select([row[2] for row in rows])
        assert selected
        result[d]=[rows[i] for i in selected]
    return result

class VecBasis:
    __slots__=('echelon','samples')
    def __init__(self):self.echelon=[];self.samples=[]
    def add(self,vec,sample):
        v=[x%P for x in vec]
        for p,w in self.echelon:
            if v[p]:
                f=v[p];v=[(x-f*y)%P for x,y in zip(v,w)]
        p=next((i for i,x in enumerate(v) if x),None)
        if p is None:return False
        iv=pow(v[p],-1,P)
        self.echelon.append((p,[x*iv%P for x in v]))
        self.echelon.sort(key=lambda entry:entry[0])
        self.samples.append(sample)
        return True


def reach_back(z,rem,ds):
    for d in ds:
        k=sum(abs(x-y) for x,y in zip(z,d))
        if k<=rem and ((rem-k)&1)==0:return True
    return False


def gen_paths(n,ds):
    """Dynamic modular basis: <=3 true path samples per (displacement, DFA state).
    All representative column spans equal those from *all* n-step paths over F_P.
    """
    initial=VecBasis(); initial.add((1,1,1),((1,1,1),()))
    states={(Z,0):initial}; peaks=[]
    for t in range(n):
        nxt={}; rem=n-t-1
        for (z,q),basis in states.items():
            for sign in (1,-1):
                for i in range(6):
                    a=sign*(i+1)
                    zz=list(z);zz[i]+=sign;zz=tuple(zz)
                    if not reach_back(zz,rem,ds):continue
                    key=(zz,advance(q,a))
                    obj=nxt.get(key)
                    if obj is None:obj=nxt[key]=VecBasis()
                    c0=W[0][i] if sign>0 else 1
                    c1=W[1][i] if sign>0 else 1
                    for w,word in basis.samples:
                        v=(w[0]*c0,w[1]*c1,1)
                        obj.add(v,(v,word+(a,)))
        states=nxt
        peaks.append({'step':t+1,'typed_states':len(states),
                      'retained_paths':sum(len(v.samples) for v in states.values())})
    return states,peaks


def row_values(path,suf,selected_rows):
    z=displacement(path);q=follow(0,path);v=weight(path)
    out=[]
    for key,a,pattern in selected_rows:
        w=suf[key];sw=weight(w)
        k=label(follow(q,w))
        out.extend(v[c]*sw[c] if a==k else 0 for c in range(3))
    return tuple(out)


def certify(n,sufs,rs):
    t0=time.monotonic();ds=sorted(rs)
    states,peaks=gen_paths(n,ds)
    blocks=[]
    for d,rows in rs.items():
        dimension=3*len(rows)
        basis=VecBasis()
        for q in range(9):
            entry=states.get((d,q))
            if not entry:continue
            for weights,word in entry.samples:
                val=row_values(word,sufs,rows)
                basis.add(val,(word,val))
        choices=basis.samples
        selected_rows=[(name,a,c) for (name,a,_pat) in rows for c in range(3)]
        mat=[[val[i] for _word,val in choices] for i in range(dimension)] if len(choices)==dimension else []
        det=det_mod(mat) if mat else 0
        blocks.append({'target':list(d),'rank_bound':dimension,'actual_mod_rank':len(choices),
                       'minor_mod_p':det,'selected_rows':[list(t) for t in selected_rows],
                       'paths':[list(w) for w,_v in choices]})
    result={'n':n,'suffix_operation_count':len(sufs),'p':P,'target_count':len(rs),
            'abstract_rank_bound':sum(3*len(rows) for rows in rs.values()),
            'real_path_mod_rank':sum(b['actual_mod_rank'] for b in blocks),
            'all_fibers_full':all(b['rank_bound']==b['actual_mod_rank'] and b['minor_mod_p']!=0 for b in blocks),
            'peak':max(peaks,key=lambda a:a['typed_states']),'layers':peaks,
            'elapsed_seconds':round(time.monotonic()-t0,3),'blocks':blocks}
    print('n',n,'suffixes',len(sufs),'abstract',result['abstract_rank_bound'],'actual',result['real_path_mod_rank'],
          'full',result['all_fibers_full'],'peak',result['peak'],'elapsed',result['elapsed_seconds'],flush=True)
    return result

def recheck_certificate(result,sufs,rs):
    for block in result['blocks']:
        d=tuple(block['target']); rows=rs[d]
        dimension=block['rank_bound']; assert dimension==3*len(rows)
        paths=[tuple(w) for w in block['paths']]
        assert all(len(p)==result['n'] and displacement(p)==d for p in paths)
        assert len(paths)==block['actual_mod_rank']
        mat=[[row_values(w,sufs,rows)[i] for w in paths] for i in range(dimension)] if len(paths)==dimension else None
        assert (det_mod(mat) if mat is not None else 0)==block['minor_mod_p']
    return True

if __name__=='__main__':
    base=Path(__file__).parent
    for h,upto in [(3,False),(3,True)]:
        suf=suffixes(h,upto);rs=row_system(suf)
        kind='S3' if not upto else 'S123'
        summary=[]
        for n in (8,10,12):
            record=certify(n,suf,rs)
            recheck_certificate(record,suf,rs)
            (base/f'CERT_EC49CJ_{kind}_n{n}.json').write_text(json.dumps(record,ensure_ascii=False,separators=(',',':'),sort_keys=True)+'\n')
            summary.append({k:v for k,v in record.items() if k not in ('layers','blocks')})
        (base/f'REPORT_EC49CJ_{kind}.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n')
