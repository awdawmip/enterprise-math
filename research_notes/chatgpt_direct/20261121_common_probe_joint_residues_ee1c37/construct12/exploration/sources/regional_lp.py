"""Complete regional candidate census, exact integer dual, then integer cover.

LP discovery is floating point; every accepted exclusion uses only saved integers.
Candidates omitted by the census have c(S)+DP(n-|S|,k-1)>old_region_cost-1.
Thus none can participate in any strictly improving regional partition.
"""
import argparse,json,subprocess,time
from pathlib import Path
import numpy as np
from scipy.sparse import csr_matrix
from scipy.optimize import linprog

HERE=Path(__file__).resolve().parents[2]

def discover_dual(a,mat,rhs,spec):
    """Column generation is only a faster discovery route; full columns are checked."""
    if len(a)<50000:
        return linprog(a['cost'],A_eq=mat,b_eq=rhs,bounds=(0,None),method='highs',options={'threads':1}),0
    known=json.loads((HERE/'initial.json').read_text())['groups']
    active=[]
    for label in spec['selected']:
        mask=sum(1<<p for p in known[label])
        active.extend(np.flatnonzero((a['lo']==mask%(1<<64))&(a['hi']==mask>>64)).tolist())
    rng=np.random.default_rng(spec['job'])
    active=np.unique(np.r_[active,rng.choice(len(a),min(2000,len(a)),replace=False)]).astype(np.int32)
    for iteration in range(30):
        lp=linprog(a['cost'][active],A_eq=mat[:,active],b_eq=rhs,bounds=(0,None),method='highs',options={'threads':1})
        if not lp.success:break
        y=lp.eqlin.marginals
        q=1000000;w=np.rint(q*y).astype(np.int64)
        w[-1]-=max(0,int(np.max(mat.T@w-q*a['cost'].astype(np.int64))))
        if int(rhs@w)>q*spec['budget']:
            return lp,iteration+1
        violation=mat.T@y-a['cost']
        bad=np.flatnonzero(violation>1e-8)
        if not len(bad):return lp,iteration+1
        if len(bad)>3000:bad=bad[np.argpartition(violation[bad],-3000)[-3000:]]
        active=np.union1d(active,bad).astype(np.int32)
        if len(active)>len(a)//2:break
    return linprog(a['cost'],A_eq=mat,b_eq=rhs,bounds=(0,None),method='highs',options={'threads':1}),-1

def run(k,obs,limit,only=None):
    jobs=json.loads((HERE/f'jobs{k}_reps.json').read_text())
    if only is not None:
        jobs=[j for j in jobs if j['job']==only]
        assert len(jobs)==1
    work=HERE/f'lp{k}';work.mkdir(exist_ok=True)
    receipts=work/'completed.jsonl';done={}
    if receipts.exists():
        done={r['job']:r for r in map(json.loads,receipts.read_text().splitlines())}
    for spec in jobs:
        jid=spec['job']
        if jid in done:continue
        start=time.monotonic()
        jp=work/f'job_{jid}.txt';bp=work/f'bank_{jid}'
        jp.write_text(f"{jid} {k} {spec['budget']} {len(spec['points'])} "+' '.join(map(str,spec['points']))+'\n')
        if not bp.exists():
            result=subprocess.check_output([HERE/'regional_v2',obs,jp,work],text=True)
            (work/f'census_{jid}.json').write_text(result)
        a=np.fromfile(bp,dtype=[('lo','<u8'),('hi','<u8'),('cost','<u4'),('size','<u4')])
        points=spec['points'];chunks=[];indptr=[0]
        for p in points:
            chunk=np.flatnonzero((a['lo' if p<64 else 'hi']>>np.uint64(p%64))&np.uint64(1)).astype(np.int32)
            chunks.append(chunk);indptr.append(indptr[-1]+len(chunk))
        chunks.append(np.arange(len(a),dtype=np.int32));indptr.append(indptr[-1]+len(a))
        indices=np.concatenate(chunks);mat=csr_matrix((np.ones(len(indices),dtype=np.int8),indices,np.array(indptr)),shape=(len(points)+1,len(a)))
        rhs=np.array([1]*len(points)+[k],dtype=np.int64)
        lp,rounds=discover_dual(a,mat,rhs,spec)
        answer={'job':jid,'selected_old_classes':spec['selected'],'k':k,'region_size':len(points),'budget':spec['budget'],'candidate_count':len(a),'lp_status':int(lp.status),'lp_master_value':lp.fun,'column_generation_rounds':rounds}
        if lp.success:
            # The following matrix multiplication uses integers throughout.
            scale=1000000
            weights=np.rint(scale*lp.eqlin.marginals).astype(np.int64)
            violation=max(0,int(np.max(mat.T@weights-scale*a['cost'].astype(np.int64))))
            weights[-1]-=violation
            slack=scale*a['cost'].astype(np.int64)-mat.T@weights
            assert np.min(slack)>=0
            bound=int(rhs@weights)
            certificate={'job':jid,'scale':scale,'point_weights':{str(p):int(w)for p,w in zip(points,weights[:-1])},'class_weight':int(weights[-1]),'scaled_lower_bound':bound,'scaled_budget':scale*spec['budget'],'minimum_column_slack':int(np.min(slack)),'exclusion':bound>scale*spec['budget']}
            (work/f'dual_{jid}.json').write_text(json.dumps(certificate,indent=2)+'\n')
            if certificate['exclusion']:
                answer.update(method='exact_integer_dual',complete=True,found=False,scaled_lower_bound=bound,scale=scale)
            else:
                # A smaller denominator keeps exact search arithmetic compact.
                scale=1000;weights=np.rint(scale*lp.eqlin.marginals).astype(np.int64)
                weights[-1]-=max(0,int(np.max(mat.T@weights-scale*a['cost'].astype(np.int64))))
        else:
            scale=1;weights=np.zeros(len(points)+1,dtype=np.int64)
        if not answer.get('complete'):
            w=[0]*125
            for p,value in zip(points,weights[:-1]):w[p]=int(value)
            wp=work/f'weights_{jid}.txt';wp.write_text(f'{scale} {int(weights[-1])}\n'+' '.join(map(str,w))+'\n')
            rp=work/f'cover_{jid}.json'
            subprocess.run([HERE/'cover_region',jp,bp,wp,rp,str(limit)],check=True)
            answer.update(json.loads(rp.read_text()))
        answer['seconds']=time.monotonic()-start
        with receipts.open('a')as f:f.write(json.dumps(answer,sort_keys=True)+'\n');f.flush()
        done[jid]=answer
        print(json.dumps(answer,sort_keys=True),flush=True)
        if answer['found']:return
        # Regeneration is deterministic, and only text proof inputs are durable.
        if answer.get('complete'):bp.unlink()

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--k',type=int,required=True);p.add_argument('--obs',type=Path,required=True);p.add_argument('--nodes',type=int,default=0);p.add_argument('--only',type=int)
    a=p.parse_args();run(a.k,a.obs,a.nodes,a.only)
