"""Check every typed twelve-label exact-cover problem in the claimed cost interval."""
import argparse
import hashlib
import json
import struct
import subprocess
import sys
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from queue import Empty, Queue
from tempfile import TemporaryDirectory

HERE = Path(__file__).resolve().parent

def tag(counts):
    return '_'.join('-'.join(map(str, (s, c, n))) for (s, c), n in sorted(counts.items()))

def verify(previous, jobs, receipt, only_four=False, selected_cost=None):
    third = previous/'previous/previous/previous'
    fourth = previous/'previous/previous'
    sys.path[:0] = [str(third/'low'), str(third/'previous/bounds')]
    from prior_bounds import observation_file, symmetries
    from cores import write_all
    from profiles import get, make_profiles, mn
    old = json.loads((previous/'frontier.json').read_text())['general']['12'][0]
    upper = receipt['last_cost_excluded']
    assert old == 9847 and upper <= 9860
    caps = get(12, upper)
    ceilings = {8:550, 9:740, 10:880, 11:1090, 12:1230, 13:1350}
    assert all(s in ceilings and (s == 13 or cap <= ceilings[s]) for s, cap in caps.items())
    with TemporaryDirectory() as tmp:
        d = Path(tmp)
        observation_file(d/'obs')
        write_all(d)
        full = (1 << 125) - 1
        (d/'cores0.txt').write_text(f'{full % (1<<64)} {full >> 64}\n')
        for name, source in [('census',third/'low/class_enumeration.cpp'),
                             ('anchor',fourth/'lower/anchor.cpp'),('anchor_two',fourth/'lower/anchor_two.cpp'),
                             *((n,HERE/(n+'.cpp')) for n in ('genprof','front'))]:
            subprocess.run(['c++','-std=c++20','-O3','-mpopcnt',source,'-o', d/name],check=True)
        subprocess.run([d/'census',d/'obs',d/'seeds'],stdout=subprocess.DEVNULL,check=True)
        seen = set()
        with (d/'seeds').open() as f:
            for line in f:
                s,c = map(int,line.split(' ',2)[:2])
                if c <= caps.get(s,0):
                    seen.add((s,c))
        keys = sorted(seen)
        cases = {}
        for cost, counts in make_profiles(12,upper,old,mn,keys):
            row = {key:n for key,n in zip(keys,counts) if n}
            h = row.get((13,1296),0)
            k = row.get((12,1104),0) + h
            p = row.get((12,1116),0)
            core_counts = (4,) if only_four else (0,1,2,4)
            if k not in core_counts or k+p >= 7:
                continue
            anchor = min(p, 2 if k <= 1 else 1)
            cases[tag(row)] = (cost,row,k,h,anchor)
        digest = hashlib.sha256(('\n'.join(sorted(cases))+'\n').encode()).hexdigest()
        assert digest == receipt['profile_digest']
        if selected_cost is not None:
            assert old <= selected_cost <= upper
            cases = {t:row for t,row in cases.items() if row[0] == selected_cost}
        used = sorted({(12,1116)}.union(*(set(dct) for _,dct,*_ in cases.values())))
        with (d/'seeds').open() as source, (d/'needed').open('w') as out:
            for line in source:
                if tuple(map(int,line.split(' ',2)[:2])) in used:
                    out.write(line)
        (d/'caps').write_text(' '.join(str(caps.get(i,0)) for i in range(14))+'\n')
        (d/'linear').write_text(''.join(' '.join(map(str,row))+'\n' for row in symmetries()[0]))
        stats = subprocess.check_output([d/'genprof',d/'linear',d/'needed',d/'caps',d/'bank'],text=True)
        assert [tuple(map(int,l.split()[:2])) for l in stats.splitlines()] == used
        punctures = []
        with (d/'bank').open('rb') as f:
            for buf in iter(lambda:f.read(24*32768), b''):
                for lo,hi,c,s in struct.iter_unpack('<QQII', buf):
                    if (s % 256,c) == (12,1116):
                        punctures.append((lo,hi,int(s>=256)))
        assert len(punctures) == 3000
        (d/'punct').write_text(f'1\n12 1116 {len(punctures)}\n'+
                 ''.join(f'{lo} {hi} {r}\n' for lo,hi,r in sorted(punctures)))
        placements = sorted({(k,h,a) for key,(_,_,k,h,a) in cases.items() if a})
        for k,h,a in placements:
            pg = 'anchor_two' if a == 2 else 'anchor'
            fn = ('pair' if a == 2 else 'anchored')+f'{k}_{h}'
            args = [d/pg,str(k),str(h),str(a),d/'punct',d/f'cores{k}.txt']
            if a == 2:
                args.append('2')
            with (d/fn).open('w') as out:
                subprocess.run(args,stdout=out,check=True)
            assert (d/fn).stat().st_size > 0
        tallies = Counter()
        q = Queue()
        for cost,row,*_ in cases.values():
            q.put((cost, [row.get(key,0) for key in used]))
        def worker(_):
            counts = Counter()
            with subprocess.Popen([d/'front',d/'bank',d,d],stdin=subprocess.PIPE,stdout=subprocess.PIPE,text=True) as proc:
                while True:
                    try:
                        cost, vec = q.get_nowait()
                    except Empty:
                        break
                    proc.stdin.write(' '.join(map(str,[cost,*vec]))+'\n')
                    proc.stdin.flush()
                    words = list(map(int,proc.stdout.readline().split()))
                    assert len(words)==5 and words[0]==cost and words[-1]==0, words
                    counts[cost]+=1
                proc.stdin.close()
                assert proc.wait()==0
            return counts
        with ThreadPoolExecutor(max_workers=jobs) as pool:
            for result in pool.map(worker,range(min(jobs,q.qsize()))):
                tallies.update(result)
    if selected_cost is not None:
        assert tallies == Counter({selected_cost:receipt['profiles_by_cost'][str(selected_cost)]})
        return {'verified_cost':selected_cost,'profiles':tallies[selected_cost]}
    answer = {'profiles_by_cost':{str(v):c for v,c in sorted(tallies.items())},
              'first_cost_excluded':old,'last_cost_excluded':upper,'lower_bound':upper+1,
              'profile_digest':hashlib.sha256(('\n'.join(sorted(cases))+'\n').encode()).hexdigest()}
    assert receipt == answer
    return answer

if __name__ == '__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--previous',type=Path,required=True)
    parser.add_argument('--jobs',type=int,default=3)
    parser.add_argument('--four-cores',action='store_true',help='verify the separate exact-four-core stratum through cost 9860')
    parser.add_argument('--cost',type=int,help='replay only the specified cost in the claimed interval')
    a=parser.parse_args()
    receipt = HERE/('four_core_result.json' if a.four_cores else 'result.json')
    print(json.dumps(verify(a.previous.resolve(),a.jobs,json.loads(receipt.read_text()),a.four_cores,a.cost),sort_keys=True,indent=2))
