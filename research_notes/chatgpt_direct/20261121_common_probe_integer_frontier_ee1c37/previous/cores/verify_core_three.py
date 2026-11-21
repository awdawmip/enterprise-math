"""Replay an exact three-core bound from the previous immutable source archive.

No optimizer is trusted: the finite menu generator, class census, integer
reduced-cost verification and exact-cover enumeration are rebuilt from source.
Only timing data are omitted when comparing results.
"""
import argparse,json,subprocess,sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from tempfile import TemporaryDirectory

HERE=Path(__file__).resolve().parent

def verify(previous,receipt,jobs,selected_case=None):
    third=previous/'previous/previous/previous/previous'
    second=third/'previous'
    sys.path[:0]=[str(previous/'twelve_cores'),str(third/'low'),str(second/'curve'),str(second/'bounds')]
    from replay import placements
    from cores import write_all
    from prior_bounds import observation_file,symmetries
    from verify import lower,MINIMA
    budget=receipt['excluded_through']
    weights=json.loads((previous/'twelve_cores/weights.json').read_text())['3/9860']
    for index,values in receipt.get('weight_overrides',{}).items():weights[int(index)]=values
    with TemporaryDirectory()as temp:
        work=Path(temp)
        observation_file(work/'obs');write_all(work)
        frames=placements(work/'cores3.txt',3)
        assert len(frames)==len(weights)==receipt['branches']==134
        maximum=[0]*14;ceilings=[0]*8+[550,740,880,1090,1230,1350]
        for mask,spent in frames:
            for size in range(1,14):
                cap=budget-spent-lower(mask.bit_count()-size,8)
                if cap>=MINIMA[size]:
                    assert size>=8 and (size==13 or cap<=ceilings[size])
                    maximum[size]=max(maximum[size],cap)
        (work/'caps').write_text(' '.join(map(str,maximum))+'\n')
        (work/'linear').write_text(''.join(' '.join(map(str,row))+'\n'for row in symmetries()[0]))
        for name,source in [('census',third/'low/class_enumeration.cpp')]+[(name,previous/'twelve_cores'/(name+'.cpp'))for name in ('global','filter','cover')]:
            subprocess.run(['c++','-std=c++20','-O3','-mpopcnt',source,'-o',work/name],check=True)
        subprocess.run([work/'census',work/'obs',work/'seeds'],stdout=subprocess.DEVNULL,check=True)
        subprocess.run([work/'global',work/'linear',work/'seeds',work/'caps',work/'global.bin'],stdout=subprocess.DEVNULL,check=True)
        def run(index):
            mask,spent=frames[index];left=budget-spent
            caps=[left-lower(mask.bit_count()-size,8)for size in range(14)]
            least=next(size for size in range(1,14)if caps[size]>=MINIMA[size])
            inp=work/f'i{index}';data=work/f'd{index}';wf=work/f'w{index}'
            inp.write_text(' '.join(map(str,[mask%2**64,mask>>64,least,13,*caps[least:]]))+'\n')
            wf.write_text(' '.join(map(str,weights[index]))+'\n')
            subprocess.run([work/'filter',work/'global.bin',inp,data,'1'],check=True)
            raw=subprocess.check_output([work/'cover',data,wf,inp,str(left),'9'],text=True).strip()
            words=list(map(int,raw.split()))
            assert len(words)==5 and words[-1]==0
            expected=receipt['cases'][index]
            assert expected['case']==index and expected['raw']==raw
            data.unlink()
            return words
        indices=[selected_case]if selected_case is not None else list(range(134))
        with ThreadPoolExecutor(jobs)as pool:rows=list(pool.map(run,indices))
        if selected_case is None:assert sum(row[3]for row in rows)==receipt['nodes']
        return {'scope':'exactly 3 cores','excluded_through':budget,'verified_branches':len(rows),'nodes':sum(row[3]for row in rows)}

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--previous',type=Path,required=True);p.add_argument('--receipt',type=Path,default=HERE/'core_three_result.json');p.add_argument('--jobs',type=int,default=2);p.add_argument('--case',type=int);a=p.parse_args()
    print(json.dumps(verify(a.previous.resolve(),json.loads(a.receipt.read_text()),a.jobs,a.case),sort_keys=True,indent=2))
