"""Reproduce the seven independent result files from an unpacked evidence archive."""
import argparse,hashlib,json,sys,subprocess,tempfile,concurrent.futures,os
from pathlib import Path
HERE=Path(__file__).resolve().parent
ROOT=HERE.parent
PAIRS={'kernel/subset_kernel':'kernel/subset_kernel_results','oracle/projection_checks':'oracle/projection_results','math/timing_checks':'math/timing_results','math/timing_kernel':'math/timing_kernel_results','math/helper_order_checks':'math/helper_order_results','design/helper_capacity':'design/capacity_results','cost/weighted':'cost/weighted_results'}
def verify(pair):
    a,b=pair;src=HERE/(a+'.py');exp=HERE/(b+'.json')
    with tempfile.TemporaryDirectory() as d:
        out=Path(d)/'recovered.json';cmd=[sys.executable,'-B','-s',str(src)]
        if a=='oracle/projection_checks':
            with out.open('wb') as w:subprocess.run(cmd,cwd=d,check=True,stdout=w)
        else:
            subprocess.run(cmd+['--out',str(out)],cwd=d,check=True,stdout=subprocess.PIPE)
        raw=out.read_bytes();assert raw==exp.read_bytes(),b
    return {'result':b+'.json','sha256':hashlib.sha256(raw).hexdigest(),'bytes':len(raw)}
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--receipt',type=Path);opts=ap.parse_args()
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        data=dict(status='PASS',scope='seven result sets byte-equal; zero source mutations',results=list(pool.map(verify,PAIRS.items())))
    if opts.receipt:opts.receipt.write_text(json.dumps(data,indent=2)+'\n')
    print(data['status'],len(data['results']))
