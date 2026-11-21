"""Check direct k-to-(k-1) exchanges in the specified globally feasible witnesses."""
from collections import Counter
from itertools import combinations
from pathlib import Path
from tempfile import TemporaryDirectory
import subprocess, sys, json, argparse

HERE=Path(__file__).resolve().parent
def run(older):
    sys.path.insert(0,str(older/'bounds'))
    from prior_bounds import observation_file
    groups13=json.loads((older/'curve/open_witnesses.json').read_text())['13']['groups']
    code12=list(map(int,(older/'bounds/twelve_10147.txt').read_text().split()))
    groups12=[[i for i,v in enumerate(code12) if v==label] for label in sorted(set(code12))]
    result={}
    with TemporaryDirectory() as tmp:
        work=Path(tmp)
        observation_file(work/'menus')
        exe=work/'packets'
        subprocess.run(['c++','-O3','-std=c++20','-mpopcnt',str(HERE/'packets.cpp'),'-o',str(exe)],check=True)
        for groups,k in ((groups13,4),(groups13,5),(groups12,4)):
            queries=[]
            for selection in combinations(range(len(groups)),k):
                points=[p for j in selection for p in groups[j]]
                queries.append(' '.join(map(str,[k-1,len(points),*selection,*points])))
            response=subprocess.check_output([str(exe), str(work/'menus')],input='\n'.join(queries)+'\n',text=True)
            nodes=covers=0
            for line,selection in zip(response.splitlines(),combinations(range(len(groups)),k),strict=True):
                nums=list(map(int,line.split()))
                assert tuple(nums[:k]) == selection
                nodes+=nums[k]
                covers+=nums[k+1]
            result[f'{len(groups)}_{k}_to_{k-1}']={'selections':len(queries),'nodes':nodes,'covers':covers}
    return result
if __name__=='__main__':
    a=argparse.ArgumentParser()
    a.add_argument('--older',type=Path,required=True)
    print(json.dumps(run(a.parse_args().older.resolve()),indent=2))
