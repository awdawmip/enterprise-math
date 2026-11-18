"""Independent certificate checker: literal signed words and modular integer determinants.
Does not call the original witness generator or old BRC DFA helpers.
"""
import json, math, sys
from pathlib import Path
MOD=1000003
WP0=(2,3,3,2,1,1); WP1=(3,2,3,2,1,1)
OPS={'a':(-1,-1),'b':(-2,-2),'c':(1,2,-1,-2),'d':(2,1,-2,-1),'e':(3,1,1,-3)}

def trace(word):
    pos=[0]*6; q0=q1=0; a=b=1
    for step in word:
        pos[abs(step)-1] += 1 if step>0 else -1
        if step>0:
            a*=WP0[step-1]; b*=WP1[step-1]
        if q0!=2: q0 = 2 if q0==1 and step==2 else (1 if step==1 else 0)
        if q1!=2: q1 = 2 if q1==1 and step==1 else (1 if step==2 else 0)
    return tuple(pos),2*(q0==2)+(q1==2),(a,b,1)

def minor(M):
    n=len(M); assert all(len(r)==n for r in M)
    A=[[v%MOD for v in row] for row in M]; d=1
    for j in range(n):
        k=next((i for i in range(j,n) if A[i][j]),None)
        if k is None:return 0
        if k!=j: A[k],A[j]=A[j],A[k]; d=-d
        pv=A[j][j]; d=d*pv%MOD; iv=pow(pv,-1,MOD)
        for i in range(j+1,n):
            if A[i][j]:
                f=A[i][j]*iv%MOD
                for m in range(j+1,n):A[i][m]=(A[i][m]-f*A[j][m])%MOD
                A[i][j]=0
    return d%MOD

def verify(fn):
    d=json.loads(Path(fn).read_text());assert d['p']==MOD
    ranks=[]
    for block in d['blocks']:
        target=tuple(block['target']); paths=[tuple(p) for p in block['paths']]
        coords=[(w,int(label),int(c)) for w,label,c in block['selected_rows']]
        assert len(coords)==block['rank_bound']
        col=[]
        for path in paths:
            z,lab,weight=trace(path)
            assert z==target and len(path)==d['n']
            read=[]
            for word,expect,c in coords:
                suffix=tuple(x for op in word for x in OPS[op])
                zz,tag,v=trace(path+suffix)
                read.append(v[c] if zz==(0,)*6 and tag==expect else 0)
            col.append(read)
        got=minor([list(row) for row in zip(*col)]) if len(col)==len(coords) else 0
        assert got==block['minor_mod_p'], (target,got,block['minor_mod_p'])
        if got:assert got!=0
        ranks.append(block['actual_mod_rank'])
    assert sum(ranks)==d['real_path_mod_rank']
    print('OK:',Path(fn).name,'n=',d['n'],'actual_mod_rank=',sum(ranks),'full=',d['all_fibers_full'],
          'nonzero_minors=',sum(bool(x['minor_mod_p']) for x in d['blocks']))

if __name__=='__main__':
    for x in sys.argv[1:]:verify(x)
