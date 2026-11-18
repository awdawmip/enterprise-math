"""Regression for native X6 triadic main checker; run from an enterprise-math checkout."""
from __future__ import annotations
import ast
import hashlib
import json
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
MODULE='experiments/x6_triadic_atomic_scatter_v1_20260906/check_triadic_atomic_scatter.py'
NATIVE='experiments/x6_signed_native_spatial_v16_20260905/signed_brc.py'
EXPECTED_MODULE='eb2036264f5b754988a5841ca1d83fab561aa49b'
EXPECTED_NATIVE='300a96e3dc24bf6fff73743037a0347a8bc83176'
OUTPUT_SHA='03f98b37a4dcf346cc3a7063206f84253a3b7c1a219f1892f7967cd55201c2a2'

def blob(data):
    return hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()

PROFILER='''import sys,collections,runpy,json
from pathlib import Path
counts=collections.Counter();error=None
def trace(frame,event,arg):
 if event=='call' and Path(frame.f_code.co_filename).name=='signed_brc.py': counts[frame.f_code.co_name]+=1
sys.setprofile(trace)
try:runpy.run_path(sys.argv[1],run_name='__main__')
except Exception as exc:error=type(exc).__name__+':'+str(exc)
finally:sys.setprofile(None)
print('__TRACE__'+json.dumps({'counts':dict(counts),'error':error},sort_keys=True))
if error:sys.exit(19)
'''

def check():
    source=(ROOT/MODULE).read_bytes()
    brc=(ROOT/NATIVE).read_bytes()
    assert blob(source)==EXPECTED_MODULE, 'upstream module changed'
    assert blob(brc)==EXPECTED_NATIVE, 'pinned original BRC changed'
    assert not any(isinstance(n,ast.Assert) for n in ast.walk(ast.parse(source)))
    replacement=b'    z=_z6(z); m=shortest_event_count(z)\n    out=factorial(m)'
    assert brc.count(replacement)==1
    results=[]
    with tempfile.TemporaryDirectory() as td:
        root=Path(td)
        module=root/MODULE; module.parent.mkdir(parents=True)
        native=root/NATIVE; native.parent.mkdir(parents=True)
        module.write_bytes(source)
        runner=root/'trace.py';runner.write_text(PROFILER)
        for mutation in (False,True):
            native.write_bytes(brc.replace(replacement,b'    return 0\n'+replacement) if mutation else brc)
            for mode in ('normal','O','OO'):
                command=[sys.executable]+([] if mode=='normal' else ['-'+mode])+[str(runner),str(module)]
                p=subprocess.run(command,capture_output=True,text=True,timeout=40)
                lines=p.stdout.splitlines()
                trace=json.loads(next(line[len('__TRACE__'):] for line in lines if line.startswith('__TRACE__')))
                output='\n'.join(line for line in lines if not line.startswith('__TRACE__'))+'\n'
                short_calls=trace['counts'].get('shortest_path_multiplicity',0)
                event_calls=trace['counts'].get('shortest_event_count',0)
                assert short_calls==(1 if mutation else 480)
                assert event_calls==(1 if mutation else 960)
                assert p.returncode==(19 if mutation else 0)
                if not mutation: assert hashlib.sha256(output.encode()).hexdigest()==OUTPUT_SHA
                results.append({'mode':mode,'mutation':mutation,'exit':p.returncode,
                                'shortest_path_calls':short_calls,'shortest_event_calls':event_calls,
                                'stdout_sha256':hashlib.sha256(output.encode()).hexdigest()})
    return {'schema':'EM_X6_UNIT128_NATIVE_ALWAYS_ON_REGRESSION_V1',
            'module_blob':EXPECTED_MODULE,'native_blob':EXPECTED_NATIVE,
            'results':results,'status':'AUTHOR_EXECUTED_UNREVIEWED_NOT_ADMITTED'}

if __name__=='__main__': print(json.dumps(check(),indent=2,sort_keys=True))
