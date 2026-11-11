"""Reproduce the eleven independent result files from an unpacked evidence archive."""
import argparse,hashlib,json,sys,subprocess,tempfile,concurrent.futures,os
from pathlib import Path
HERE=Path(__file__).resolve().parent
ROOT=HERE.parent
PAIRS={'kernel/endogenous_kernel': 'kernel/endogenous_kernel_results', 'kernel/two_block': 'kernel/two_block_results', 'kernel/product_deadline': 'kernel/product_results', 'math/menu_checks': 'math/menu_results', 'math/menu_kernel': 'math/menu_kernel_results', 'oracle/deadline_checks': 'oracle/deadline_results', 'oracle/deadline_kernel': 'oracle/deadline_kernel_results', 'graph/feedback_graph': 'graph/feedback_graph_results', 'graph/cover': 'graph/cover_results', 'phase/phase_kernel': 'phase/phase_results', 'repair/joint_repair': 'repair/joint_repair_results'}
def verify(pair):
    a,b=pair;src=HERE/(a+'.py');exp=HERE/(b+'.json')
    with tempfile.TemporaryDirectory() as d:
        out=Path(d)/'recovered.json';cmd=[sys.executable,'-B','-s',str(src)]
        subprocess.run(cmd+['--out',str(out)],cwd=d,check=True,stdout=subprocess.PIPE)
        raw=out.read_bytes();assert raw==exp.read_bytes(),b
    return {'result':b+'.json','sha256':hashlib.sha256(raw).hexdigest(),'bytes':len(raw)}
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--receipt',type=Path);opts=ap.parse_args()
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        data=dict(status='PASS',scope='eleven result sets byte-equal; zero source mutations',results=list(pool.map(verify,PAIRS.items())))
    if opts.receipt:opts.receipt.write_text(json.dumps(data,indent=2)+'\n')
    print(data['status'],len(data['results']))
