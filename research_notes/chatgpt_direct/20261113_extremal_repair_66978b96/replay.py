"""Independent certificate entry points. Python 3.12 and GNU C++17 compatible compiler."""
from pathlib import Path
import subprocess,sys,tempfile,hashlib,json,argparse,concurrent.futures
HERE=Path(__file__).resolve().parent
def jobs():
    leaf=[
    ('ind2/audit.py','ind2/audit_results.json',[]),('ind2/verify.py','ind2/results.json',['--workers','2']),
    ('common/escape.py','common/escape_results.json',[]),('native/replay_joint.py','native/escape12.json',['--case','escape12']),('common/translation.py','common/translation_results.json',[]),('common/hybrid.py','common/hybrid_results.json',[]),
    ('packing/block_lift.py','packing/block_lift_results.json',[]),
    ('native/replay_joint.py','native/hybrid11.json',['--case','hybrid11']),('native/replay_joint.py','native/parent12.json',['--case','parent12']),
    ('native/saturated_block.py','native/saturated_block.json',[])]
    for sc,out,flags in [('native/exception_gate.py','native/exception_gate.json',[]),('common/repair_radius.py','common/repair_radius_results.json',[]),('common/neighborhood.py','common/neighborhood_results.json',[]),('common/reflection.py','common/reflection_results.json',[]),('orbits/coordinate_cycle.py','orbits/cycle_results.json',[]),('common/uniform_check.py','common/uniform_results.json',[]),('native/replay_joint.py','native/uniform11.json',['--case','uniform11'])]:
        if (HERE/sc).is_file() and (HERE/out).is_file():leaf.append((sc,out,flags))
    return leaf
def check(it):
    sc,expected,flags=it
    with tempfile.TemporaryDirectory()as t:
        out=Path(t)/'result.json';subprocess.run([sys.executable,'-B',str(HERE/sc),*flags,'--out',str(out)],cwd=t,check=True,stdout=subprocess.DEVNULL);raw=out.read_bytes()
        assert raw==(HERE/expected).read_bytes(),expected
    return dict(result=expected,bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest())
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--out',type=Path);p.add_argument('--only',nargs='*');p.add_argument('--workers',type=int,default=3);arg=p.parse_args()
    j=[it for it in jobs() if not arg.only or it[1] in arg.only];assert j
    with concurrent.futures.ThreadPoolExecutor(max_workers=arg.workers) as pool:r=list(pool.map(check,j))
    if arg.out:arg.out.write_text(json.dumps({'status':'PASS','results':r},indent=2)+'\n')
    print('PASS',len(r))
