"""Count covers with two minimum 12-classes and a 569-cost nine-point class."""
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
    placements=[]
    for (a,b),st in pair_orbits(rows,group,(12,1104),(12,1104)):
        available={m for m in rows[9,569]if not m&(a|b)}
        while available:
            x=min(available);orb={moved(x,g)for g in st};assert orb<=available;available-=orb
            placements.append((a,b,x))
    with (work/'jobs').open('w')as f:
        for a,b,x in placements:print(3,a&LOW_MASK,a>>64,b&LOW_MASK,b>>64,x&LOW_MASK,x>>64,8,2,file=f)
    with (work/'rows').open('w')as f:
        for c,s in ((557,9),(744,10)):
            masks=rows[s,c];print(s,c,len(masks),file=f)
            for m in masks:print(m&LOW_MASK,m>>64,0,file=f)
    exe=work/'cover';subprocess.run(['c++','-std=c++17','-O3','-mpopcnt',str(HERE/'count.cpp'),'-o',str(exe)],check=True)
    def block(i):
        end=min(i+10,len(placements))
        text=subprocess.check_output([str(exe),str(work/'rows'),str(work/'jobs'),str(i),str(end),'uneven9'],text=True,cwd=work)
        values=[tuple(map(int,line.split()))for line in text.splitlines()]
        assert [row[0]for row in values]==list(range(i,end))
        return values
    with ThreadPoolExecutor(max_workers=3)as pool:summary=[r for chunk in pool.map(block,range(0,len(placements),10)) for r in chunk]
    return {'placements':len(placements),'completions_at_representatives':sum(h for _,h,_ in summary),'search_nodes':sum(n for _,_,n in summary)}
if __name__=='__main__':
    with TemporaryDirectory()as tmp:print(json.dumps(run(Path(tmp)),sort_keys=True))
