"""Supplement to ../cost/core_cost.py. Run after placing this directory next to the base proof's directory."""
from itertools import combinations
import json
from pathlib import Path
import subprocess
import sys
from tempfile import TemporaryDirectory

HERE=Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'cost'))
import core_cost


def main():
    with TemporaryDirectory() as temp:
        work=Path(temp);data=work/'observations.bin';core_cost.observations(data)
        linear,trans=core_cost.point_symmetries()
        floor,cheap,runners,parents=core_cost.cheap_families(work,data,linear,trans)
        representatives,_=core_cost.packing_reps(cheap,linear,trans)
        jobs=[];pairs=0
        for five in representatives[5]:
            occupied=0
            for group in five:occupied|=group
            for runner in runners:
                if runner&occupied:continue
                pairs+=1
                for count in range(6):
                    for indexes in combinations(range(5),count):
                        groups=[parents[c] if i in indexes else c for i,c in enumerate(five)] + [runner]
                        union=0
                        for g in groups:union|=g
                        if union.bit_count()!=sum(g.bit_count() for g in groups):continue
                        fixed_cost=5*1104+1116+192*count
                        jobs.append((fixed_cost,*core_cost.members(core_cost.ALL^union)))
        cases=work/'cases.txt';exe=work/'five_group_batch'
        cases.write_text(''.join(' '.join(map(str,row))+'\n' for row in jobs))
        subprocess.run(['c++','-std=c++17','-O3','-mpopcnt',str(HERE/'five_group_batch.cpp'),'-o',str(exe)],check=True)
        output=subprocess.check_output([str(exe),str(data),str(cases)],text=True)
        assert output.split()==['results',str(len(jobs)),'0']
        # Reuse the base classification for six and four cores. In a complete eleven-table
        # five cores actually allow no runner. This script tightens precisely that case.
        minimum=core_cost.lower_bound(floor,{4:2,5:0})
        assert minimum[0]==10937
        print(json.dumps({'five_core_orbits':len(representatives[5]),'compatible_runner_choices':pairs,
             'tested_residuals':len(jobs),'eleven_class_completions':0,'cost_lower_bound':minimum[0],
             'profile':{'size13':minimum[1],'cheap12':minimum[2],'runner12':minimum[3],
                        'higher12':minimum[4],'smaller':minimum[5]}},indent=2))

if __name__=='__main__':main()
