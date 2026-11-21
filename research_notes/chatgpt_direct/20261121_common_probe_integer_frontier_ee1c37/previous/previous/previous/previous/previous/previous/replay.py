"""Rebuild the finite certificates from the previous native model, included in the archive."""
import argparse
from pathlib import Path
import subprocess
import sys,json,os
from concurrent.futures import ThreadPoolExecutor
ROOT=Path(__file__).resolve().parent

def main():
    p=argparse.ArgumentParser()
    p.add_argument('sections',nargs='*')
    p.add_argument('--jobs',type=int,default=2)
    p.add_argument('--previous',type=Path,default=ROOT/'previous')
    args=p.parse_args()
    old=args.previous.resolve()
    if not old.exists():old=next((a/'round2/delivery'for a in ROOT.parents if (a/'round2/delivery/curve').exists()),old)
    if not old.is_dir():p.error('Supply the previous shared-probe certificate directory with --previous')
    env=dict(os.environ,NATIVE_PROBE_PREVIOUS=str(old))
    suites={'symmetry':[('inversion.py','inversion.json',['--older',str(old)]),('orbit.py','orbit.json',['--older',str(old)]),('packets.py','packets.json',['--older',str(old)])],
            'native':[('replay.py','result.json',['--original',str((ROOT/'original').resolve())])], 'group':[('replay.py','result.json',[]),('translation_replay.py','translation.json',[]),('rotation_three.py','rotation_three.json',[])],'anchors':[('replay.py','result.json',[]),('three.py','three.json',[]),('extra_triples.py','extra_triples.json',[]),('slices.py','slices.json',[])]}
    suites['asymmetric']=[('replay.py','result.json',['--older',str(old),'--group',str(ROOT/'group'),'--original',str((ROOT/'original').resolve())])]
    suites['asymmetric8721']=[('replay.py','result.json',['--older',str(old),'--group',str(ROOT/'group'),'--original',str((ROOT/'original').resolve())]),('structure.py','structure.json',[])]
    suites['eleven_neighborhood']=[('replay.py','result.json',['--older',str(old)])]
    suites['exchange']=[('replay.py','result.json',['--older',str(old),'--group',str(ROOT/'group'),'--table',str(ROOT/'asymmetric/groups.json')]),('overlap.py','overlap.json',['--group',str(ROOT/'group'),str(ROOT/'asymmetric/groups.json'),str(ROOT/'asymmetric8721/groups.json')])]
    suites['twelve']=[('replay.py','result.json',['--older',str(old),'--original',str((ROOT/'original').resolve())])]
    suites['twelve'].append(('neighborhood.py','neighborhood.json',['--older',str(old)]))
    suites['twelve'].append(('five.py','five.json',['--older',str(old)]))
    suites['mixed_twelve']=[('replay.py','result.json',[])]
    suites['mixed_twelve'].append(('two_cores.py','two_cores.json',[]))
    suites['large_triplets']=[('verify_8721.py','result.json',[])]
    suites['frontier_cases']=[('replay.py','result.json',[])]
    if (ROOT/'low/result.json').is_file():suites['low']=[('replay.py','result.json',['--prior',str(old)])]
    if (ROOT/'relaxed/result.json').is_file():
        costs=list(json.loads((ROOT/'relaxed/result.json').read_text()))
        suites['relaxed']=[('replay.py','result.json',['--older',str(old),'--group',str(ROOT/'group'),'--costs',*costs])]
    for extra in ('alternates','budgets'):
        if (ROOT/extra/'result.json').is_file():suites[extra]=[('replay.py','result.json',[])]
    def run(key):
        base=ROOT/key
        for script,check,flags in suites[key]:
            out=subprocess.check_output([sys.executable,'-B',str(base/script),*flags],env=env,cwd=base,text=True)
            ref=json.loads((base/check).read_text())
            try: result=json.loads(out)
            except json.JSONDecodeError:result=json.loads(out.strip().splitlines()[-1])
            assert result==ref, (script,result,ref)
            print('PASS',key,script,flush=True)
    wanted=args.sections or list(suites)
    if not set(wanted)<=set(suites) or args.jobs<1:p.error('Unknown suite or invalid job count')
    with ThreadPoolExecutor(max_workers=args.jobs)as pool:list(pool.map(run,wanted))
if __name__=='__main__':main()
