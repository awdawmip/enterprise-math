"""Compile and rerun both finite certificates from clean files; at most four parallel deterministic seed passes.
Usage: python3 verify.py --out /path/to/results.json
"""
import argparse,concurrent.futures,json,os,subprocess,tempfile
from collections import Counter
from pathlib import Path
HERE=Path(__file__).resolve().parent
def from_logs(ans,raw):
    seeds=[int(z) for z in (HERE/'seeds.txt').read_text().split()]
    ans=sorted(ans);assert [x for x,_ in ans]==seeds and len(ans)==496
    return dict(status='PASS',shape='three independent five-point inputs; each full two-endpoint cube; 3 fixed old messages and <=2 adaptive coordinate probes',raw_seeds=raw,number_of_normalized_seeds=len(ans),exhausted_seeds=len(ans),successful_extensions=0,total_extension_nodes=sum(y for _,y in ans),max_nodes_per_seed=max(y for _,y in ans),endpoint_boxes=1000,previous_four_message_upper='parent triple_proof.md; first pair 4-color one-read followed by one optional endpoint read of third service',minimum_old_messages=4,rows=ans)
def run(workers):
    with tempfile.TemporaryDirectory() as tmp:
        base=Path(tmp)
        for name in ('seeds','extend'):
            subprocess.run([os.environ.get('CXX','g++'),'-O3','-std=c++17',str(HERE/(name+'.cpp')),'-o',str(base/name)],cwd=base,check=True)
        p=subprocess.run([str(base/'seeds')],capture_output=True,text=True,check=True,cwd=base)
        raw=p.stdout;assert raw==(HERE/'seeds.txt').read_text()
        seeds=[int(z)for z in raw.split()];assert len(seeds)==len(set(seeds))==496
        def one(rows):
            q=subprocess.run([str(base/'extend'),'2147483646'],input=''.join(str(z)+'\n'for z in rows),capture_output=True,text=True,cwd=base,check=True)
            ans=[]
            for ln in q.stdout.splitlines():
                msg=ln.split()
                if len(msg)!=3 or msg[1]!='UNSAT':raise ValueError('Not a complete exclusion: '+ln)
                ans.append((int(msg[0]),int(msg[2])))
            assert [x for x,_ in ans]==rows
            return ans
        with concurrent.futures.ThreadPoolExecutor(max_workers=workers)as pool:
            ans=sorted([t for row in pool.map(one,[seeds[j::workers] for j in range(workers)])for t in row])
        return from_logs(ans,p.stderr.strip())
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--out',type=Path,default=HERE/'results.json');ap.add_argument('--workers',type=int,default=2);a=ap.parse_args();d=run(a.workers);a.out.write_text(json.dumps(d,indent=1)+'\n');print('PASS',d['exhausted_seeds'],d['total_extension_nodes'],d['max_nodes_per_seed'])
