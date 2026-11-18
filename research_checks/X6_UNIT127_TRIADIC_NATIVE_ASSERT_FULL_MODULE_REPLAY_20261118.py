"""Opt-in exact original triadic-scatter full-module native BRC trace and assert fault test.
Use in a checkout containing both unchanged signed source files. No write to upstream sources.
"""
import ast
import hashlib
import json
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TRIAD = 'experiments/x6_triadic_atomic_scatter_v1_20260906/check_triadic_atomic_scatter.py'
BRC = 'experiments/x6_signed_native_spatial_v16_20260905/signed_brc.py'
PIN = ('d5f6dfcfd0dedbe46feae3bc1b227185af417c2f',
       '300a96e3dc24bf6fff73743037a0347a8bc83176')

def gitblob(b):
    return hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()

class AlwaysOn(ast.NodeTransformer):
    def __init__(self):
        self.count = 0
    def visit_Assert(self, node):
        self.count += 1
        replacement = ast.If(test=ast.UnaryOp(op=ast.Not(), operand=node.test),
          body=[ast.Raise(exc=ast.Call(func=ast.Name(id='AssertionError',ctx=ast.Load()),
                 args=[ast.Constant('guard_'+str(self.count))],keywords=[]),cause=None)],orelse=[])
        return ast.copy_location(replacement, node)

WRAPPER = '''import sys,runpy,json,collections
from pathlib import Path
p=Path(sys.argv[1]); counts=collections.Counter(); error=None
def profile(frame,event,arg):
 if event=='call' and Path(frame.f_code.co_filename).name=='signed_brc.py':
  counts[frame.f_code.co_name]+=1
sys.setprofile(profile)
try: runpy.run_path(str(p),run_name='__main__')
except Exception as e: error=type(e).__name__+':'+str(e)
finally: sys.setprofile(None)
print('__TRACE__'+json.dumps({'counts':dict(counts),'error':error},sort_keys=True))
if error: sys.exit(19)
'''

def one(original, brc, variant, corrupt, mode):
    with tempfile.TemporaryDirectory() as temp:
        root=Path(temp); t=root/TRIAD; b=root/BRC
        t.parent.mkdir(parents=True); b.parent.mkdir(parents=True)
        if variant=='strict':
            tree=ast.parse(original); transformer=AlwaysOn()
            tree=transformer.visit(tree); ast.fix_missing_locations(tree)
            t.write_text(ast.unparse(tree)+'\n')
        else:
            t.write_bytes(original)
        if corrupt:
            old=b'    z=_z6(z); m=shortest_event_count(z)\n    out=factorial(m)'
            assert brc.count(old)==1
            b.write_bytes(brc.replace(old,b'    return 0\n'+old))
        else:
            b.write_bytes(brc)
        wrapper=root/'profile.py'; wrapper.write_text(WRAPPER)
        command=[sys.executable]+(['-'+mode] if mode else [])+[str(wrapper),str(t)]
        result=subprocess.run(command,capture_output=True,text=True,timeout=45)
        lines=result.stdout.splitlines()
        observation=json.loads(next(s[9:] for s in lines if s.startswith('__TRACE__')))
        printed='\n'.join(s for s in lines if not s.startswith('__TRACE__'))+'\n'
        return {'variant':variant,'fault':corrupt,'mode':mode or 'normal',
                'code':result.returncode,'native_counts':observation['counts'],
                'error':observation['error'],
                'output_sha256':hashlib.sha256(printed.encode()).hexdigest(),
                'reported_pass':printed.startswith('PASS_X6_TRIADIC_ATOMIC_SCATTER_V1')}

def main():
    src=(ROOT/TRIAD).read_bytes(); brc=(ROOT/BRC).read_bytes()
    assert (gitblob(src),gitblob(brc))==PIN
    guards=sum(isinstance(n,ast.Assert) for n in ast.walk(ast.parse(src)))
    cases=[one(src,brc,v,b,o) for b in (False,True)
           for v in ('original','strict') for o in ('','O','OO')]
    for row in cases:
        mode=row['mode']; fault=row['fault']; strict=row['variant']=='strict'
        expected_calls=480 if (strict or mode=='normal') else 0
        if fault: expected_calls=1 if expected_calls else 0
        assert row['native_counts'].get('shortest_path_multiplicity',0)==expected_calls
        assert (row['code']==0)==(not fault or (not strict and mode!='normal'))
        if not fault: assert row['reported_pass']
    clean={c['output_sha256'] for c in cases if not c['fault']}
    assert len(clean)==1
    payload={'schema':'EM_X6_UNIT127_FULL_NATIVE_REPLAY_V1','source_git_blobs':PIN,
             'guard_nodes':guards,'clean_output_sha256':next(iter(clean)),
             'status':'AUTHOR_EXECUTED_UNREVIEWED_NOT_ADMITTED','cases':cases}
    print(json.dumps(payload,ensure_ascii=False,sort_keys=True,indent=2))

if __name__=='__main__': main()
