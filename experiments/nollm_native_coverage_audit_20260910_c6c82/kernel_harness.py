"""Isolated execution of hash-pinned Nollm kernel and recall functions.
NOT NollmCore/provider integration: imports are supplied by minimal typed fixtures.
No lateral or persistent bridge is supplied to the actual-kernel tests.
"""
from __future__ import annotations
import ast, hashlib, os, sys, types
from dataclasses import dataclass
from pathlib import Path
ROOT=Path(__file__).resolve().parent
SOURCE_DIR=Path(os.environ.get("NOLLM_CORE_SOURCE", str(ROOT/"source_snapshots")))
PINS={'coverage_contract.py':'f08885e526248597edbd840b134bf7dbb26e1420','approximate_coverage.py':'b322638a0fe77e57ec84ac32cf817749a8b06582','fixed_point.py':'9ea00e3c84a82f480c692a6ca0ca717a579dab60','recall.py':'02c148caad1929a0f72055100b75f806f55a956d'}

@dataclass(frozen=True)
class GeometryAddress:
    profile_id:str;chart_id:str;layer:int;q:int;r:int;phase:str|None=None
    def stable_key(self):return self.profile_id,self.chart_id,self.layer,self.q,self.r,self.phase or ''
    def to_mapping(self):return dict(profile_id=self.profile_id,chart_id=self.chart_id,layer=self.layer,q=self.q,r=self.r,phase=self.phase)
def cell(q=0,r=0,layer=0):return GeometryAddress('default_dream_v1','default',layer,q,r)
@dataclass(frozen=True)
class MemoryAtom:
    value:str
@dataclass(frozen=True)
class AtomHandle:
    geometry_address:GeometryAddress;local_atom_id:str
@dataclass(frozen=True)
class CoreTraceEvent:
    name:str;data:dict;visibility:str

def load(name,globals_):
    path=SOURCE_DIR/name;raw=path.read_bytes()
    blob=hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()
    if blob!=PINS[name]:raise ValueError(f'Pinned source mismatch: {name}')
    tree=ast.parse(raw.decode())
    tree.body=[n for n in tree.body if not (isinstance(n,ast.ImportFrom) and n.level)]
    mod=types.ModuleType('pinned_'+name.replace('.','_'));mod.__dict__.update(globals_)
    sys.modules[mod.__name__]=mod
    exec(compile(tree,str(path),'exec'),mod.__dict__)
    return mod
fixed=load('fixed_point.py',{})
contract=load('coverage_contract.py',dict(GeometryAddress=GeometryAddress,Q16_ONE=65536))
g={k:v for k,v in vars(contract).items() if not k.startswith('__')}
g.update(Q16_ONE=65536,normalize_q16_weights=fixed.normalize_q16_weights,DEFAULT_PROFILE_ID='default_dream_v1')
coverage=load('approximate_coverage.py',g)
def forbidden(*a,**kw):raise AssertionError('Fixture does not implement lateral templates')
recall=load('recall.py',dict(GeometryAddress=GeometryAddress,MemoryAtom=MemoryAtom,
       AtomHandle=AtomHandle,CoreTraceEvent=CoreTraceEvent,Q16_ONE=65536,
       expand_template=forbidden,validate_lateral_ring=forbidden))
class Registry:
    def expand_coverage(self,c,d):return coverage.expand_approximate_coverage(c,d).targets()
class Runtime:
    def __init__(self,registry=None):self.kernel_registry=registry or Registry();self.visited=[];self.trace=[]
    def _emit_trace(self,e):self.trace.append(e)
    def _atoms_at_locked(self,c):
        self.visited.append(c)
        return [(AtomHandle(c,'fixture'),MemoryAtom('synthetic location marker'))]
    def _bridges_locked(self):return ()
def run_recall(depth=6,beam=32,layer_delta=2,origin=None,registry=None,fn=None):
    rt=Runtime(registry);request=recall.CoreRecallRequest('physical-audit',(origin or cell(),),('coverage_down','coverage_up'),recall.RecallBudget(depth,beam,layer_delta,0,0,1000000))
    out=(fn or recall.resolve_recall)(rt,request)
    return rt,out

def support_ball(depth,layer_delta=2,origin=None):
    root=origin or cell();dist={root:0};front={root};reg=Registry()
    for k in range(depth):
        new=set()
        for s in front:
            for d in ('coverage_up','coverage_down'):
                for t,w in reg.expand_coverage(s,d):
                    if abs(t.layer-root.layer)<=layer_delta and t not in dist:new.add(t)
        for t in new:dist[t]=k+1
        front=new
    return dist
if __name__=='__main__':
    from collections import Counter
    for direction in ('coverage_up','coverage_down'):
        c=coverage.expand_approximate_coverage(cell(),direction)
        print(direction,[(m.target.q,m.target.r,m.hit_count,m.weight_q16) for m in c.members])
    print('support',len(support_ball(8)))
    for b in (1,2,4,8,16,32,64,128,512,4096):
        rt,out=run_recall(8,b)
        print('beam',b,'visits',len(set(rt.visited)),'layers',Counter(c.layer for c in set(rt.visited)), 'exhausted',out.budget_exhausted,'steps',len([e for e in rt.trace if e.name=='core.recall.frontier']))
