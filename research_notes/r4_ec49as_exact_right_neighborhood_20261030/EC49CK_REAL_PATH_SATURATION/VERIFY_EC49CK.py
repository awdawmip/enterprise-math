"""EC49CK author-side exact finite BRC suffix Hankel rank study.
Reuses EC49CJ modular path-space DP for native typed X6/BRC carrier,
with provably exact distance-to-target pruning via cached L1 distances.
"""
from VERIFY_EC49CJ import *
from functools import lru_cache
from pathlib import Path
import time, json

H=5
D=tuple((2*i,2*j) for i in range(H+1) for j in range(H-i+1))
@lru_cache(maxsize=None)
def xy_dist(x,y):
    return min(abs(x-a)+abs(y-b) for a,b in D)

def fast_reach(z,rem,ds):
    # Every target has even component sum and n even; parity automatic.
    return xy_dist(z[0],z[1])+sum(map(abs,z[2:])) <= rem

import VERIFY_EC49CJ as CJ
CJ.reach_back=fast_reach

def from_states(n,sufs,rs,states,peaks):
    blocks=[]
    for d,rows in rs.items():
        dimension=3*len(rows)
        basis=VecBasis()
        for q in range(9):
            obj=states.get((d,q))
            if obj is None:continue
            for _weights,word in obj.samples:
                basis.add(row_values(word,sufs,rows),word)
        paths=basis.samples
        mat=[[row_values(w,sufs,rows)[i] for w in paths] for i in range(dimension)] if len(paths)==dimension else []
        det=det_mod(mat) if mat else 0
        blocks.append({'target':list(d),'rank_bound':dimension,'actual_mod_rank':len(paths),'minor_mod_p':det,
                       'selected_rows':[[name,a,c] for name,a,_pat in rows for c in range(3)],
                       'paths':[list(w) for w in paths]})
    return {'n':n,'h':H,'suffix_operation_count':len(sufs),'p':P,'target_count':len(rs),
            'abstract_rank_bound':sum(3*len(rows) for rows in rs.values()),
            'real_path_mod_rank':sum(b['actual_mod_rank'] for b in blocks),
            'all_fibers_full':all(b['rank_bound']==b['actual_mod_rank'] and b['minor_mod_p']!=0 for b in blocks),
            'peak':max(peaks,key=lambda a:a['typed_states']), 'layers':peaks, 'blocks':blocks}

if __name__=='__main__':
    print('TARGETS',len(D),'distance optimized',flush=True)
    for n in (12,14):
        t0=time.monotonic()
        states,peaks=gen_paths(n,tuple((i,j,0,0,0,0) for i,j in D))
        print('n',n,'generated',len(states),'terminal states; peak',max(x['typed_states'] for x in peaks),'seconds',round(time.monotonic()-t0,2),flush=True)
        for upto in (False,True):
            sufs=suffixes(H,upto);rs=row_system(sufs)
            v=from_states(n,sufs,rs,states,peaks)
            assert recheck_certificate(v,sufs,rs)
            kind='S5' if not upto else 'SLE5'
            p=Path(f'CERT_EC49CK_{kind}_n{n}.json')
            p.write_text(json.dumps(v,sort_keys=True,separators=(',',':'))+'\n')
            print(kind,'rank',v['real_path_mod_rank'],'bound',v['abstract_rank_bound'], 'full',v['all_fibers_full'], 'seconds',round(time.monotonic()-t0,2),flush=True)
