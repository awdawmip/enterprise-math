"""Discover non-star clique cuts with two intersecting anchors and a point."""
from pathlib import Path
from fractions import Fraction
import json
import numpy as np
HERE=Path(__file__).resolve().parent

def points(mask):
    while mask:
        b=mask&-mask;yield b.bit_length()-1;mask-=b

def search(frame):
    d=json.loads((HERE.parent/'proof'/f'cover_{frame}.json').read_text());rows=d['weights'];masks=[int(r['mask'])for r in rows]
    w=np.array([r['numerator']/r['denominator']for r in rows]);lo=np.array([m%(1<<64)for m in masks],dtype=np.uint64);hi=np.array([m>>64 for m in masks],dtype=np.uint64)
    adj=((lo[:,None]&lo[None,:])!=0)|((hi[:,None]&hi[None,:])!=0)
    inc=np.zeros((len(rows),125),dtype=np.int8)
    for i,m in enumerate(masks):inc[i,list(points(m))]=1
    best=(-1,None);eligible_pairs=0
    for p in points(int(d['free_mask'])):
        star=np.flatnonzero(inc[:,p]);out=np.flatnonzero(1-inc[:,p]);star_sums=adj[:,star]@w[star]
        slack=1-star_sums-w
        ids=out[slack[out]<w.max()+1e-10]
        if len(ids)<2:continue
        a=adj[np.ix_(ids,star)].astype(float)
        vals=(a*w[star])@a.T+w[ids,None]+w[ids][None,:]
        pairadj=adj[np.ix_(ids,ids)];np.fill_diagonal(pairadj,False)
        eligible_pairs+=int(pairadj.sum()//2);vals[~pairadj]=-1
        ij=np.unravel_index(np.argmax(vals),vals.shape);v=float(vals[ij])
        if v>best[0]:best=(v,(int(ids[ij[0]]),int(ids[ij[1]]),p))
    result={'frame':frame,'discovery_eligible_intersecting_pairs':eligible_pairs,'best_float':best[0]}
    if best[1]is not None:
        a,b,p=best[1];ma,mb=masks[a],masks[b]
        selected=[r for i,r in enumerate(rows)if i in(a,b)or((masks[i]>>p)&1 and masks[i]&ma and masks[i]&mb)]
        lhs=sum((Fraction(r['numerator'],r['denominator'])for r in selected),Fraction())
        result.update(anchors=[str(ma),str(mb)],point=p,positive_clique_classes=len(selected),lhs_numerator=lhs.numerator,lhs_denominator=lhs.denominator,violated=lhs>1)
    print(json.dumps(result),flush=True);return result

if __name__=='__main__':
    out=[search(f)for f in range(1,6)];(HERE/'two_anchor_results.json').write_text(json.dumps(out,indent=2)+'\n')
