"""Exhaust a 13-, 12- and 10-point anchor before packing the residual low-cost nine-point classes."""
from pathlib import Path
from tempfile import TemporaryDirectory
from concurrent.futures import ThreadPoolExecutor
import json
import subprocess
from replay import HERE, bank, maps, moved, LOW_MASK

def verify(work):
    lin,trans,_=maps()
    elements=[bytes(t[i] for i in g)for g in lin for t in trans]
    rows=bank(work,lin,trans,8728)
    twelve=rows[12,1104]
    thirteen=rows[13,1296];fixed=min(thirteen)
    assert {moved(fixed,g)for g in elements}==set(thirteen)
    stab=[g for g in elements if moved(fixed,g)==fixed]
    others={v for v in twelve if not fixed&v}
    jobs=[]
    while others:
        y=min(others)
        orbit={moved(y,g)for g in stab}
        assert orbit <= others
        others-=orbit
        pair_stab=[g for g in stab if moved(y,g)==y]
        used=fixed|y
        thirds={v for v in rows[10,747] if not v&used}
        while thirds:
            z=min(thirds)
            orbit={moved(z,g)for g in pair_stab}
            assert orbit<=thirds
            thirds-=orbit
            jobs.append((fixed,y,z))

    jobfile=work/'all.jobs'
    jobfile.write_text(''.join(' '.join(str(x)for m in group for x in (m&LOW_MASK,m>>64))+' 10\n'for group in jobs))
    nine=rows[9,557]
    rfile=work/'nines'
    rfile.write_text('1\n9 557 '+str(len(nine))+'\n'+''.join(f'{m&LOW_MASK} {m>>64}\n'for m in nine))
    exe=work/'pure'
    subprocess.run(['c++','-std=c++17','-mpopcnt','-O3',str(HERE/'pure.cpp'),'-o',str(exe)],check=True)

    def chunk(start):
        proc=subprocess.run([str(exe),str(rfile),str(jobfile),str(start),str(min(start+1100,len(jobs)))],capture_output=True,text=True,check=True)
        out=[list(map(int,line.split())) for line in proc.stdout.splitlines()]
        assert [idx for idx,n,found in out] == list(range(start,min(start+1100,len(jobs))))
        assert not any(found for idx,n,found in out)
        return sum(n for idx,n,found in out)
    with ThreadPoolExecutor(max_workers=2) as pool:
        visits=list(pool.map(chunk,range(0,len(jobs),1100)))
    return {'profile_cost':8717,'anchor_triples':len(jobs),'sum_nodes':sum(visits),'found':False}

if __name__=='__main__':
    with TemporaryDirectory()as t:
        print(json.dumps(verify(Path(t)),sort_keys=True,indent=2))
