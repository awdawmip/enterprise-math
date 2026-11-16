"""Count unlabelled covers for all placements of the two differently priced 12-classes."""
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from tempfile import TemporaryDirectory
import json,sys,subprocess
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent/'anchors'))
from replay import maps,bank,LOW_MASK,moved
from extra_triples import pair_orbits
def run(work):
    lin,tr,_=maps()
    group=[bytes(t[i]for i in g)for t in tr for g in lin]
    rows=bank(work,lin,tr,8728)
    placements=list(pair_orbits(rows,group,(12,1104),(12,1116)))
    with (work/'jobs').open('w')as f:
        for (a,b),st in placements:print(2,a&LOW_MASK,a>>64,b&LOW_MASK,b>>64,9,2,file=f)
    with (work/'rows').open('w')as f:
        for c,s in ((557,9),(744,10)):
            masks=rows[s,c];print(s,c,len(masks),file=f)
            for m in masks:print(m&LOW_MASK,m>>64,0,file=f)
    exe=work/'cover';subprocess.run(['c++','-std=c++17','-O3','-mpopcnt',str(HERE/'count.cpp'),'-o',str(exe)],check=True)
    def search(i):
        data=subprocess.check_output([str(exe),str(work/'rows'),str(work/'jobs'),str(i),str(i+1),'mixed12'],text=True,cwd=work)
        j,solutions,nodes=map(int,data.split());assert i==j
        return solutions,nodes
    with ThreadPoolExecutor(max_workers=3)as pool:summary=list(pool.map(search,range(len(placements))))
    only=[i for i,(n,_) in enumerate(summary)if n];assert len(only)==1
    i,=only
    # The two anchors have different costs and therefore cannot be exchanged.
    assert len(placements[i][1])==1 and summary[i][0]==1
    return {'placements':len(placements),'unique_completable_placement':i,'completions_at_representative':summary[i][0],
            'placement_stabilizer':1,'unlabelled_partitions':len(group),'search_nodes':sum(v for _,v in summary)}
if __name__=='__main__':
    with TemporaryDirectory()as tmp:print(json.dumps(run(Path(tmp)),sort_keys=True))
