"""EC49CM: constructive X6/BRC suffix-observability rank certificates.
Exact integer path weights, modular nonzero minors, all h=1..7.
Author-side portable mathematics; not a Source Result or physical calibration.
"""
from __future__ import annotations
from collections import defaultdict
from itertools import chain, product
from pathlib import Path
import hashlib,json

P=1_000_003
W=((2,3,3,2,1,1),(3,2,3,2,1,1))
OPS={'a':(-1,-1),'b':(-2,-2),'c':(1,2,-1,-2),'d':(2,1,-2,-1)}
Q=(0,1,2,3,5,6,7,8)


def next_q(q,s):
    a,b=divmod(q,3)
    def upd(x,first,second):
        return 2 if x==2 or (x==1 and s==second) else int(s==first)
    return 3*upd(a,1,2)+upd(b,2,1)

def path_state(path):
    z=[0]*6;q=0;v=[1,1,1]
    for s in path:
        ix=abs(s)-1;z[ix]+=1 if s>0 else -1;q=next_q(q,s)
        if s>0:v[0]*=W[0][ix];v[1]*=W[1][ix]
    return tuple(z),q,tuple(v)

def label(q):return 2*(q//3==2)+(q%3==2)

def follow(q,word):
    for s in word:q=next_q(q,s)
    return q

def suffixes(h,upto):
    return {''.join(x):tuple(chain.from_iterable(OPS[a] for a in x))
            for m in range(1 if upto else h,h+1) for x in product(OPS,repeat=m)}

def select(vectors):
    """Independent vector positions in input order over F_p."""
    basis=[];idx=[]
    for i,original in enumerate(vectors):
        v=[x%P for x in original]
        for p,row in basis:
            if v[p]:
                f=v[p];v=[(a-f*b)%P for a,b in zip(v,row)]
        pivot=next((k for k,x in enumerate(v) if x),None)
        if pivot is not None:
            inv=pow(v[pivot],-1,P)
            basis.append((pivot,[x*inv%P for x in v]));basis.sort(key=lambda w:w[0]);idx.append(i)
    return idx

def determinant(rows):
    a=[[x%P for x in row] for row in rows];n=len(a);d=1
    assert all(len(row)==n for row in a)
    for j in range(n):
        k=next((i for i in range(j,n) if a[i][j]),None)
        if k is None:return 0
        if k!=j:a[j],a[k]=a[k],a[j];d=-d
        t=a[j][j];d=d*t%P;inv=pow(t,-1,P)
        for i in range(j+1,n):
            if a[i][j]:
                scale=a[i][j]*inv%P
                for col in range(j+1,n):a[i][col]=(a[i][col]-scale*a[j][col])%P
                a[i][j]=0
    return d%P

def row_system(sufs):
    rows=defaultdict(list)
    for name,word in sufs.items():
        z,_,_=path_state(word);target=tuple(-x for x in z)
        after=[label(follow(q,word)) for q in range(9)]
        for tag in range(4):
            rows[target].append((name,tag,tuple(int(x==tag) for x in after)))
    return {d:[rs[i] for i in select([r[2] for r in rs])] for d,rs in sorted(rows.items())}

def sym_expect(h,k,upto):
    return 3 if k==0 else 4 if k==h else 6 if upto else 5

def swap(word):
    return tuple((2 if s==1 else 1 if s==2 else -2 if s==-1 else -1 if s==-2 else s) for s in word)

def base_q(i,j):
    """Exactly one neutral pair and ALL eight reachable DFA states; length 2(i+j)+2."""
    assert i+j>=1
    if i and j:
        a=(1,)*(2*i);b=(2,)*(2*j)
        result={0:a+(-3,)+b+(3,),1:a+(3,-3)+b,3:b+(3,-3)+a,
                2:b+a+(3,-3),5:(3,-3)+b+a,6:a+b+(3,-3),
                7:(3,-3)+a+b,8:(3,-3)+a[:-1]+b+(1,)}
    elif i:
        a=(1,)*(2*i)
        result={0:a+(3,-3),1:a+(-2,2),3:(3,-3)+a,
                2:(2,)+a+(-2,),5:(-2,2)+a,6:a+(2,-2),
                7:(-2,)+a+(2,),8:a[:-1]+(2,1,-2)}
    else:
        original=base_q(j,0)
        result={3*(q%3)+q//3:swap(word) for q,word in original.items()}
    expected=(2*i,2*j,0,0,0,0)
    assert set(result)==set(Q)
    for q,word in result.items():
        z,t,_=path_state(word)
        assert z==expected and t==q and len(word)==2*(i+j)+2,(i,j,q,word,z,t)
    return result

def candidates(i,j,n):
    k=i+j;d=(2*i,2*j,0,0,0,0)
    if n>=2*k+4:
        pad=(3,-3)*((n-2*k-4)//2)
        if k:
            return [pad+(r,-r)+word for q,word in base_q(i,j).items() for r in (1,2,3)]
        return [pad+(r,-r)+trailer for trailer in ((3,-3),(-1,1),(-2,2)) for r in (1,2,3)]
    assert n==2*k+2
    if i and j:
        a=(1,)*(2*i);b=(2,)*(2*j)
        # Four observed A/B flag labels with independent weight triples.
        none=[a+(1,-1)+b,b+(2,-2)+a,a+(3,-3)+b]
        yes_a=[(r,-r)+a+b for r in (1,2,3)]
        yes_b=[(r,-r)+b+a for r in (1,2,3)]
        both=[(r,-r)+a[:-1]+b+(1,) for r in (1,2,3)]
        seq=none+yes_a+yes_b+both
        assert all(path_state(w)[0]==d and len(w)==n for w in seq)
        assert [label(path_state(w)[1]) for w in seq]==[0]*3+[2]*3+[1]*3+[3]*3
        return seq
    a=(1,)*(2*k)
    seq=[a+(r,-r) for r in (1,3,4)]+[a+(2,-2),(2,)+a+(-2,),a[:-1]+(2,1,-2)]
    return [swap(w) for w in seq] if j else seq

def row_value(word,sufs,rows):
    z,q,v=path_state(word);out=[]
    for name,tag,_ in rows:
        _,_,wv=path_state(sufs[name]);t=label(follow(q,sufs[name]))
        out.extend(v[c]*wv[c] if t==tag else 0 for c in range(3))
    return out

def certificate(h,upto,n,with_blocks):
    sufs=suffixes(h,upto);rs=row_system(sufs)
    assert len(rs)==(h+1)*(h+2)//2
    for d,rows in rs.items():
        k=(d[0]+d[1])//2
        assert len(rows)==sym_expect(h,k,upto),(h,upto,d,len(rows))
    blocks=[];rank=0
    for d,rows in rs.items():
        i,j=d[0]//2,d[1]//2
        words=candidates(i,j,n)
        matrix=[row_value(w,sufs,rows) for w in words]
        chosen=select(matrix);r=len(chosen);dimension=3*len(rows)
        expect=dimension-(6 if n==2*h+2 and i+j==h and (i==0 or j==0) else 0)
        assert r==expect,(h,upto,n,i,j,r,expect)
        rank+=r
        if with_blocks:
            sub=[matrix[c] for c in chosen]
            idx=select([[col[t] for col in sub] for t in range(dimension)])
            assert len(idx)==r
            det=determinant([[sub[c][j] for c in range(r)] for j in idx])
            assert det
            blocks.append({'target':list(d),'dimension':dimension,'rank':r,
                           'selected_rows':[[name,t,c] for name,t,_ in rows for c in range(3)],
                           'minor_row_indices':idx,'minor_mod_p':det,
                           'paths':[list(words[c]) for c in chosen]})
    full=3*((5*h*h+13*h+4)//2 if not upto else 3*h*h+7*h+1)
    expect=full-(12 if n==2*h+2 else 0)
    assert rank==expect,(h,upto,n,rank,expect)
    result={'schema':'EC49CM_EXPLICIT_NATIVE_X6_WITNESS_V1','h':h,'n':n,
            'suffix_language':'S<=h' if upto else 'S^h','suffix_words':len(sufs),
            'prime':P,'target_fibers':len(rs),'formal_rank':full,
            'real_mod_rank':rank,'all_fibers_full':rank==full,
            'method':'explicit 8 DFA states * 3 independent positive BRC channels; two extreme one-pair fibers at n=2h+2'}
    if with_blocks:result['blocks']=blocks
    return result

def main():
    root=Path(__file__).resolve().parent;report=[]
    for h in range(1,8):
        for upto in (False,True):
            for n in (2*h+2,2*h+4):
                exact=certificate(h,upto,n,with_blocks=(h==7))
                record={k:v for k,v in exact.items() if k!='blocks'}
                report.append(record)
                if h==7:
                    name=f'EC49CM_CERT_h{h}_{"SLE" if upto else "S"}_n{n}.json'
                    (root/name).write_text(json.dumps(exact,sort_keys=True,separators=(',',':'))+'\n')
                print(f'h={h} {record["suffix_language"]:<5} n={n}: {record["real_mod_rank"]}/{record["formal_rank"]} over F_{P}',flush=True)
    payload={'schema':'EC49CM_VERIFICATION_V1','scope':'native signed X6, specific four suffix operations, exact Q-additive weighted path-observer rank',
             'theorem':'n_sat(h)=2h+4 for all integer h>=1; at 2h+2 both ranks deficient exactly 12',
             'note':'Computed for h<=7; arbitrary-h proof is symbolic in README','cases':report}
    (root/'EC49CM_EXACT_REPORT.json').write_text(json.dumps(payload,indent=2,ensure_ascii=False)+'\n')
    print('TOTAL',len(report),'CASES PASS',flush=True)
if __name__=='__main__':main()
