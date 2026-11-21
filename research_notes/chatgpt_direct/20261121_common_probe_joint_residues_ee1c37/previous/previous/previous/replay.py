"""Compare independently regenerated certificates with the archived integer receipts."""
import argparse
import json
import os
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

HERE=Path(__file__).resolve().parent

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--previous',type=Path,default=HERE/'previous')
    parser.add_argument('--only',nargs='+')
    parser.add_argument('--jobs',type=int,default=3)
    parser.add_argument('--parallel',type=int,default=1)
    args=parser.parse_args()
    previous=args.previous.resolve()
    third=previous/'previous/previous'
    os.environ['NATIVE_PROBE_PREVIOUS']=str(third/'previous')
    prev=['--previous',previous]
    work=prev+['--jobs',str(args.jobs)]
    tests={}
    def add(name,options,folder=None,script='replay.py',receipt='result.json'):
        root=HERE/(folder or name)
        tests[name]=(root/script, root/receipt, options)
    add('involutions',['--last',third])
    add('pure_c2',['--round3',third,'--c4',previous/'c4/groups.json'])
    add('klein',work)
    add('klein_native',['--round3',third],'klein','native.py','native_result.json')
    add('mothers',prev)
    add('eleven_lb',work+['--base',HERE/'mothers'])
    add('one_exception',prev+['--base',HERE/'mothers'])
    add('seven',work)
    add('history_distance',prev)
    add('local_alternatives',work)
    add('fixed_classes',work)
    if (HERE/'fixed_two/result.json').exists():
        add('fixed_two',work)
    add('refinement',work)
    add('overlap',work)
    add('orbit_distance',prev)
    add('gainpack',prev)
    add('changes',prev)
    selection=args.only or list(tests)
    if set(selection)-set(tests):
        parser.error('unknown suite, choose from '+', '.join(tests))
    def check(name):
        program,receipt,options=tests[name]
        out=subprocess.check_output([sys.executable,'-B',program,*options],text=True)
        actual=json.loads(out[out.rfind('\n{')+1:])
        assert actual==json.loads(receipt.read_text()),name
        print(name,'PASS',flush=True)
    with ThreadPoolExecutor(args.parallel)as pool:
        list(pool.map(check,selection))

if __name__=='__main__':
    main()
