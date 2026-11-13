"""One physical endpoint probe on the saturated 16-history class and its coset copies."""
from itertools import product,combinations
import sys,json,hashlib,argparse
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT))
from next_repair.native import native_recovery as orig
def run():
    W=[tuple(next((i for i in range(3) if t[i]!=p[i]),3+t[3])for p in product(range(2),repeat=3))for t in product(range(2),repeat=4)]
    blocks=[{i for i,w in enumerate(W)if w[k]==v} for k in range(8)for v in range(5)]
    assert all(not(a&b)or a<=b or b<=a for a in blocks for b in blocks)
    C=orig.core.prior.Compiler(slots=15);qread=0;nraw=0;sizes={};hashes=hashlib.sha256();totalcost=[]
    # 16 cyclic shifts (including identity); stratified over all 120 pairs, alternate shifts + preserve/distinguish modes.
    def execute(hi,shift,m,e):
        nonlocal qread,nraw
        h=tuple((v+s)%5 for v,s in zip(W[hi],shift));ps=[];guards=[]
        for j,v in enumerate(h):
            raw,g=orig.old(C,v);ps.append(raw);guards.append(g);orig.update(raw,m[j])
        # Fixed class is valid here because these are the represented histories; no value is revealed to decoder.
        WW=[tuple((a+s)%5 for a,s in zip(w,shift))for w in W];assert tuple(guards) in WW
        bank=[p.codes()for p in ps];fs=tuple(orig.first(p,ed)['code']for p,ed in zip(ps,e))
        cand=set()
        for w in WW:
            vals=[orig.audit(ed,orig.F[k][x])for x,k,ed in zip(w,m,e)]
            if tuple(z[0]for z in vals)==fs:cand.add(tuple(z[1]for z in vals))
        assert 1<=len(cand)<=2;trace=()
        if len(cand)==2:
            a,b=sorted(cand);i=next(j for j in range(8)if a[j]!=b[j]);assert fs[i]==11
            key=e[i]+1;ans=int(ps[i].probe(orig.marker_slot(key),orig.least_one(key)));cand={c for c in cand if c[i]==(11 if ans else key)};trace=(i,key,ans);qread+=1
        (out,)=cand;ks=tuple(orig.emit(p,[k])[0]['bind_delivered']for p,k in zip(ps,out))
        assert all(orig.audit(ed,orig.F[k][x])==(f,r) for x,k,ed,f,r in zip(h,m,e,fs,ks)) and bank==[p.codes() for p in ps]
        fee=sum(p.cost for p in ps);totalcost.append(fee);nraw+=1
        hashes.update((json.dumps([hi,shift,m,e,fs,ks,trace,fee],separators=(',',':'))+'\n').encode());sizes[int(bool(trace))]=sizes.get(int(bool(trace)),0)+1
    # For each unordered pair choose menu with common first receipts and different required second vectors;
    # two histories sharing all other coordinates' outside reports can always be arranged.
    for cnt,(i,j) in enumerate(combinations(range(16),2)):
        sh=tuple((cnt//(k+1)+k+(cnt%3)*k*k)%5 for k in range(8)) if cnt%3 else (0,)*8
        x=tuple((v+s)%5 for v,s in zip(W[i],sh));y=tuple((v+s)%5 for v,s in zip(W[j],sh));dsel=[k for k in range(8)if x[k]!=y[k]][cnt%sum(a!=b for a,b in zip(x,y))]
        m=[];es=[]
        for k,(aa,bb) in enumerate(zip(x,y)):
            items=[(f,e)for f in orig.MAPS for e in range(5)if (orig.F[f][aa] in orig.E[e])==(k==dsel) and (orig.F[f][bb] in orig.E[e])==(k==dsel)]
            f,e=items[(cnt+2*k)%len(items)];m.append(f);es.append(e)
        execute(i,sh,tuple(m),tuple(es));execute(j,sh,tuple(m),tuple(es))
    assert qread==240
    for i,w in enumerate(W):
        sh=tuple((i+j)%5 for j in range(8));maps=tuple(orig.MAPS[(i+j)%2]for j in range(8));es=tuple(next(e for e in range(5)if orig.F[f][(v+s)%5] not in orig.E[e])for f,v,s in zip(maps,w,sh));execute(i,sh,maps,es)
    assert nraw==256 and sizes=={0:16,1:240}
    return {'status':'PASS','scope':'stratified full eight-original-program paths, not a frequency estimate or exhaustive eight-dimensional experiment; each of 120 unordered same-message pairs forced to need a paid original endpoint read, plus one zero-read path per leaf; representative code geometry and coordinate translates','paths':nraw,'per_service_raw_preparations_writers_firsts_seconds_each':8*nraw,'pair_witnesses':120,'read_histogram':sizes,'min_observed_total':min(totalcost),'max_observed_total':max(totalcost),'ordered_trace_sha256':hashes.hexdigest()}
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--out',type=Path,required=True);a=ap.parse_args();r=run();a.out.write_text(json.dumps(r,indent=2,sort_keys=True)+'\n');print(r)
