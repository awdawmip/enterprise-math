"""Independent exact certificate and native signed BRC audit for EC49CK.

This module does not import the path-sampling/rank-selection implementation.
It checks every literal path and selected observer row using direct substrings,
exact integer BRC weights and modular Gauss elimination. The full native
BRC endpoint_weight/endpoint_multiplicity runs on all 21 target fibers and
both n=12,14; each S^<=5 suffix is also audited by a separate typed DP.
"""
import itertools, json, hashlib, subprocess
from pathlib import Path
from collections import defaultdict
from native_signed_brc import endpoint_weight, endpoint_multiplicity

P=1_000_003
POS=((2,3,3,2,1,1),(3,2,3,2,1,1))
ALPH={'a':(-1,-1),'b':(-2,-2),'c':(1,2,-1,-2),'d':(2,1,-2,-1)}
DIR=(1,-1,2,-2,3,-3,4,-4,5,-5,6,-6)
H=5
D=[(2*i,2*j,0,0,0,0) for i in range(H+1) for j in range(H-i+1)]

def displacement(w):
    z=[0]*6
    for a in w: z[abs(a)-1] += 1 if a>0 else -1
    return tuple(z)

def weight(w):
    v=[1,1,1]
    for a in w:
        if a>0:
            for ch in (0,1):v[ch]*=POS[ch][a-1]
    return tuple(v)

def direct_label(w):
    x=any((w[i],w[i+1])==(1,2) for i in range(len(w)-1))
    y=any((w[i],w[i+1])==(2,1) for i in range(len(w)-1))
    return 2*int(x)+int(y)

def q_step(q,a):
    r,s=divmod(q,3)
    r=2 if r==2 or (r==1 and a==2) else int(a==1)
    s=2 if s==2 or (s==1 and a==1) else int(a==2)
    return r*3+s

def follow(q,w):
    for a in w:q=q_step(q,a)
    return q

def qlabel(q):
    return 2*int(q//3==2)+int(q%3==2)

def rank_det_mod(matrix):
    a=[[x%P for x in row] for row in matrix]
    if not a: return 0,1
    n=len(a); m=len(a[0]); p=0; det=1
    for j in range(m):
        k=next((i for i in range(p,n) if a[i][j]),None)
        if k is None: continue
        a[p],a[k]=a[k],a[p]
        if k!=p:det=-det
        diag=a[p][j];det=det*diag%P
        inv=pow(diag,-1,P)
        for i in range(p+1,n):
            if a[i][j]:
                f=a[i][j]*inv%P
                for jj in range(j+1,m):a[i][jj]=(a[i][jj]-f*a[p][jj])%P
                a[i][j]=0
        p+=1
        if p==min(n,m): break
    return p,(det%P if n==m and p==n else 0)

def suffix_word(name):
    return tuple(itertools.chain.from_iterable(ALPH[c] for c in name))

def validate_certificate(filename):
    cert=json.loads(Path(filename).read_text())
    total=0;dets=[]
    for block in cert['blocks']:
        d=tuple(block['target']); rows=block['selected_rows']; paths=block['paths']
        assert len(rows)==block['rank_bound'] and len(paths)==block['actual_mod_rank']
        for w in paths:
            assert len(w)==cert['n'] and all(x in DIR for x in w)
            assert displacement(w)==d
        matrix=[]
        for name,l,channel in rows:
            suffix=suffix_word(name)
            assert tuple(a+b for a,b in zip(displacement(suffix),d))==(0,)*6
            matrix.append([
                weight(tuple(w)+suffix)[channel] if direct_label(tuple(w)+suffix)==l else 0
                for w in paths
            ])
        rk,det=rank_det_mod(matrix)
        assert rk==len(paths),(filename,d,rk,len(paths))
        assert det==block['minor_mod_p'],(filename,d,det,block['minor_mod_p'])
        total+=rk
        dets.append((d,rk,det))
    assert total==cert['real_path_mod_rank']
    assert len(dets)==21
    return {'file':str(filename),'rank':total,'all_fibers_full':cert['all_fibers_full'],
            'full_minors_nonzero':sum(1 for _,_,det in dets if det!=0),
            'deficient':[(list(d),cert['blocks'][i]['rank_bound']-r) for i,(d,r,_) in enumerate(dets)
                         if r<cert['blocks'][i]['rank_bound']]}

def min_target_dist(z):
    return min(abs(z[0]-d[0])+abs(z[1]-d[1]) for d in D)+sum(abs(v) for v in z[2:])

def dp(n):
    state={((0,)*6,0):(1,1,1)}
    peak=1
    for t in range(n):
        nex={}; rem=n-t-1
        for (z,q),v in state.items():
            for a in DIR:
                zz=list(z);zz[abs(a)-1]+=1 if a>0 else -1;zz=tuple(zz)
                if min_target_dist(zz)>rem:continue
                nq=q_step(q,a); key=(zz,nq)
                aweight=[POS[ch][a-1] if a>0 else 1 for ch in (0,1)]
                old=nex.get(key,(0,0,0))
                nex[key]=(old[0]+v[0]*aweight[0],old[1]+v[1]*aweight[1],old[2]+v[2])
        state=nex;peak=max(peak,len(nex))
    return state,peak

def native_audit(n,state):
    totals=defaultdict(lambda:[0,0,0]); labels=defaultdict(lambda:[[0]*3 for _ in range(4)])
    for (z,q),v in state.items():
        target=totals[z]
        for ch in range(3):target[ch]+=v[ch]
    for d in D:
        native=(int(endpoint_weight(n,d,POS[0],(1,)*6)),
                int(endpoint_weight(n,d,POS[1],(1,)*6)),
                endpoint_multiplicity(n,d))
        assert tuple(totals[d])==native,(n,d,totals[d],native)
    all_obs=0; by_len={}
    for h in range(1,H+1):
        for symbols in itertools.product(ALPH,repeat=h):
            suffix=tuple(itertools.chain.from_iterable(ALPH[k] for k in symbols))
            d=tuple(-x for x in displacement(suffix)); sw=weight(suffix)
            lab_tot=[[0]*3 for _ in range(4)]
            for q in range(9):
                v=state.get((d,q))
                if v:
                    l=qlabel(follow(q,suffix))
                    for ch in range(3):lab_tot[l][ch]+=v[ch]*sw[ch]
            native=tuple(totals[d][ch]*sw[ch] for ch in range(3))
            assert tuple(sum(lab_tot[l][ch] for l in range(4)) for ch in range(3))==native
            all_obs+=12
            by_len[h]=by_len.get(h,0)+1
    return {'n':n,'terminal_typed_states':len(state),'native_target_fibers_checked':len(D),
            'operation_words_checked':sum(by_len.values()),'observations_checked':all_obs,
            'operation_words_by_length':by_len, 'native_origin':totals[(0,)*6]}

if __name__=='__main__':
    native_sha=subprocess.check_output(['git','hash-object','native_signed_brc.py'],text=True).strip()
    assert native_sha=='300a96e3dc24bf6fff73743037a0347a8bc83176'
    summary={'native_git_blob':native_sha,'prime':P,'witnesses':[],'native':[]}
    for n in (12,14):
        for kind in ('S5','SLE5'):
            fp=f'CERT_EC49CK_{kind}_n{n}.json'
            r=validate_certificate(fp);summary['witnesses'].append(r)
            print('WITNESS',n,kind,r['rank'],'full',r['all_fibers_full'],flush=True)
        state,peak=dp(n)
        r=native_audit(n,state);r['peak_typed_states']=peak;summary['native'].append(r)
        print('NATIVE',n,'peak',peak,'obs',r['observations_checked'],flush=True)
    Path('EXACT_REPORT_EC49CK.json').write_text(json.dumps(summary,indent=2,ensure_ascii=False)+'\n')
    print('ALL CHECKS PASS',flush=True)
