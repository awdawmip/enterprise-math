"""Complete pending canonical-root profiles, with separate atomic receipts."""
import argparse
import hashlib
import json
import subprocess
import time
from pathlib import Path

HERE=Path(__file__).resolve().parent

def read_done(path):
    if not path.exists():return {}
    ans={}
    for line in path.read_text().splitlines():
        row=json.loads(line)
        if row.get('found')==0:ans[row['tag']]=row
    return ans

def counts(tag):
    return {(s,c):n for s,c,n in (tuple(map(int,x.split('-'))) for x in tag.split('_'))}

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--work',type=Path,required=True)
    p.add_argument('--cost',type=int,required=True)
    p.add_argument('--tag')
    p.add_argument('--skip-running',action='store_true',help='Do not duplicate profiles named in current running*.json')
    p.add_argument('--reverse',action='store_true',help='Work from the other end of the pending profile list')
    p.add_argument('--all-pending',action='store_true',help='Also run profiles without a useful fixed-core stabilizer')
    a=p.parse_args();work=a.work.resolve()
    manifest=json.loads((work/'manifest.json').read_text());types=list(map(tuple,manifest['types']))
    tags=(HERE/'audit'/f'cost_{a.cost}_profiles.txt').read_text().splitlines()
    assert not a.tag or a.tag in tags
    log=HERE/'orbit_min_completed.jsonl';status=HERE/'orbit_min_running.json'
    start_priority={}
    for f in work.glob('running*.json'):
        row=json.loads(f.read_text());start_priority[row['tag']]=row['started']
    tags.sort(key=lambda t:(0,start_priority[t]) if t in start_priority else (1,t))
    if a.reverse:tags.reverse()
    source=HERE/'front_orbit_min_witness.cpp'
    provenance={'engine':'orbits-min-witness','source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
                'bank_sha256':hashlib.sha256((work/'bank').read_bytes()).hexdigest()}
    with subprocess.Popen([work/'front_orbit_min_witness',work/'bank',work,work],
                          stdin=subprocess.PIPE,stdout=subprocess.PIPE,text=True) as proc:
        for tag in tags:
            if a.tag and tag!=a.tag:continue
            if a.skip_running:
                busy={json.loads(f.read_text())['tag'] for f in work.glob('running*.json')}
                if tag in busy:continue
            if tag in read_done(work/'completed.jsonl') or tag in read_done(log) or tag in read_done(HERE/'root_probe_completed.jsonl'):continue
            row=counts(tag)
            core=row.get((12,1104),0)+row.get((13,1296),0)
            if not a.all_pending and (not core or row.get((12,1116),0)):continue
            assert sum(s*n for (s,c),n in row.items())==125
            assert sum(c*n for (s,c),n in row.items())==a.cost
            began=time.monotonic()
            status.write_text(json.dumps({'cost':a.cost,'tag':tag,'started':time.time()})+'\n')
            proc.stdin.write(' '.join(map(str,[a.cost]+[row.get(t,0) for t in types]))+'\n');proc.stdin.flush()
            fields=list(map(int,proc.stdout.readline().split()))
            assert len(fields)==5 and fields[0]==a.cost,fields
            item=dict(zip(('cost','geometric_nodes','leaf_nodes','search_nodes','found'),fields))
            item.update(provenance,tag=tag,seconds=time.monotonic()-began)
            with log.open('a') as out:out.write(json.dumps(item,sort_keys=True)+'\n')
            print(json.dumps(item,sort_keys=True),flush=True)
            if item['found']:
                assert (work/f'found_{a.cost}.json').exists()
                break
        proc.stdin.close();assert proc.wait()==0
    status.unlink(missing_ok=True)

if __name__=='__main__':main()
