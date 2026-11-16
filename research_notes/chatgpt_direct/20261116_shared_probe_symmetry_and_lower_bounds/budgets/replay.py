"""Recreate all anchor types and exhaust the selected global budget profiles."""
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import subprocess,sys,json,tempfile
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent/'group'))
from generate import main as generate
from jobs import prepare

def run(folder,keep):
    generate(folder)
    n=prepare(folder,8728,'tasks',set(keep))
    exe=folder/'cover'
    subprocess.run(['c++','-std=c++17','-O3','-mpopcnt',str(HERE/'planes.cpp'),'-o',str(exe)],check=True)
    def job(i):
        result=subprocess.check_output([str(exe),str(folder),'tasks',str(i)],text=True)
        idx,p,cost,nodes,ok=map(int,result.split());assert i==idx and ok==0
        return p,cost,nodes
    with ThreadPoolExecutor(max_workers=3)as pool:
        results=list(pool.map(job,range(n)))
    return [{'id':p,'cost':next(v for s,v,_ in results if s==p),'cases':sum(s==p for s,_,_ in results),'nodes':sum(q for s,_,q in results if s==p)}for p in keep]
if __name__=='__main__':
    keep=json.loads((HERE/'result.json').read_text())
    with tempfile.TemporaryDirectory()as tmp:
        print(json.dumps(run(Path(tmp),[q['id']for q in keep]),sort_keys=True))
