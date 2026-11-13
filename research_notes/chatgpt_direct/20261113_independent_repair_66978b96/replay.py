"""Run the supplied finite checks in fresh directories, comparing exact result bytes."""
import argparse,concurrent.futures,hashlib,json,subprocess,sys,tempfile
from pathlib import Path
H=Path(__file__).resolve().parent
def jobs():
    lst=[('independent/independent_geometry.py','independent/independent_geometry_results.json',[]),('independent/optimal_total.py','independent/optimal_total_results.json',[]),('opt/optimize.py','opt/results.json',[]),('laminar/capacity.py','laminar/capacity_results.json',[]),('triple/triple_verify.py','triple/triple_results.json',[])]
    for p in sorted((H/'native').glob('*.json')):lst.append(('native/native_recovery.py','native/'+p.name,['--phase',p.stem]))
    for src,ref in [('triple/common_short.py','triple/common_short_results.json'),('triple/common_opt.py','triple/common_opt_results.json'),('triple/two_probe_criterion.py','triple/two_probe_criterion_results.json')]:
        if (H/src).exists():lst.append((src,ref,[]))
    return lst
def test(job):
    sc,f,flags=job
    with tempfile.TemporaryDirectory() as tmp:
        out=Path(tmp)/'out.json';subprocess.run([sys.executable,'-B',str(H/sc),*flags,'--out',str(out)],cwd=tmp,check=True,stdout=subprocess.DEVNULL)
        content=out.read_bytes();assert content==(H/f).read_bytes(),f
    return dict(result=f,bytes=len(content),sha256=hashlib.sha256(content).hexdigest())
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--receipt',type=Path);p.add_argument('--only',nargs='*');a=p.parse_args()
    ls=[j for j in jobs() if not a.only or j[1] in a.only];assert ls
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:vals=list(pool.map(test,ls))
    d=dict(status='PASS',clean_results=vals)
    if a.receipt:a.receipt.write_text(json.dumps(d,indent=2)+'\n')
    print('PASS',len(vals))
