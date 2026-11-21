"""Replay a named new result against the self-contained preceding archive."""
import argparse
from concurrent.futures import ThreadPoolExecutor
import json
import os
from pathlib import Path
import subprocess
import sys

HERE=Path(__file__).resolve().parent

def main():
    p=argparse.ArgumentParser()
    p.add_argument('--previous',type=Path,default=HERE/'previous')
    p.add_argument('--only',nargs='+')
    p.add_argument('--parallel',type=int,default=2)
    p.add_argument('--jobs',type=int,default=3)
    args=p.parse_args()
    prev=args.previous.resolve()
    last=prev/'previous'
    older=last/'previous'
    group=last/'group'
    os.environ['NATIVE_PROBE_PREVIOUS']=str(older)
    common=['--older',older,'--group',group]
    tests={}
    def add(name,folder,options,program='replay.py',receipt='result.json'):
        tests[name]=(HERE/folder/program,HERE/folder/receipt,options)
    add('c3','c3',['--previous',prev])
    add('c3_native','c3',['--round3',last],'native.py','native_result.json')
    add('c4','c4',['--previous',prev])
    add('c4_native','c4',['--round3',last],'native.py','native_result.json')
    add('involutions','involutions',['--older',older,'--last',last])
    add('involutions_equal','involutions_equal',['--proof',HERE/'involutions','--older',older,'--last',last])
    add('eleven_equal','eleven_equal',common)
    add('eleven_native','eleven_equal',['--round3',last],'witness.py','witness_result.json')
    add('rank3','rank3',common)
    add('bridge','bridge',['--older',older,'--groups',HERE/'c3/groups.json','--jobs',str(args.jobs)])
    add('five_base','five_max/predecessor',[],'five13_stratum.py','five13_stratum.json')
    add('planes','planes',['--previous',prev,'--groups',HERE/'c3/groups.json'])
    add('five_max','five_max',['--previous',prev])
    add('three_max','three_max',['--older',older,'--jobs',str(args.jobs)])
    add('parents','parents',['--older',older,'--jobs',str(args.jobs)])
    add('local','local',['--previous',prev,'--groups',HERE/'c3/groups.json','--jobs',str(args.jobs)])
    if (HERE/'lower/result.json').is_file():
        add('lower','lower',['--previous',prev,'--last',last,'--native',older,'--jobs',str(args.jobs)])
    for f in ('eleven_order3','eleven_order4','eleven_other_order4','eleven_klein'):
        add('audit_'+f,'audit/'+f,common)
    def run(name):
        program,receipt,options=tests[name]
        out=subprocess.check_output([sys.executable,'-B',program,*options],text=True)
        if name=='lower':
            result=json.loads(out[out.rfind('\n{')+1:])
        else:
            result=json.loads(out)
        assert result==json.loads(receipt.read_text()),name
        print(name,'PASS',flush=True)
    selection=args.only or list(tests)
    unknown=set(selection)-set(tests)
    if unknown:p.error('unknown suites '+', '.join(sorted(unknown)))
    with ThreadPoolExecutor(max_workers=args.parallel)as ex:list(ex.map(run,selection))
if __name__=='__main__':
    main()
