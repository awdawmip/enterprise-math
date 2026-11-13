#!/usr/bin/env python3
"""R41 integration using the exact R32/R33/R36 predecessor scripts in ./src.
The local archive R41_RESEARCH_BUNDLE.zip contains those pinned scripts.
Run from the same directory as VERIFY_R41_STANDALONE.py.
"""
import hashlib,sys
from pathlib import Path
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE/'src'))
from VERIFY_R41_STANDALONE import r41_hybrid
import VERIFY_R32 as r32
import VERIFY_R33 as r33
import VERIFY_R36 as r36

def run(force_endpoint=False):
    class HybridCompiler(r36.Compiler):
        def _prepare_stage(self,first,i,j):
            low=first-i;N=j-low
            assert N>=1
            val,stats=r41_hybrid(self.lo,self.hi,self.m,j,N,0 if force_endpoint else 4*self.m)
            self.current_last_sources=sorted(x for x in val if x is not None)
            self.prepared_ranks+=1
            self.batch_methods.append({'first':first,'i':i,'j':j,**stats})
    stages,_,_,jumps=r33.jump_stages()
    comp=HybridCompiler(128,389,*r36.S23)
    initial=comp.compile()
    assert initial==(-7551,28800) and len(comp.blocks)==4
    assert len(stages)==78 and jumps==28
    r32.early_updates=lambda:list(comp.blocks)
    r32.produce_farey_stages=lambda:(stages,0,0)
    got,runs,segs,final,_,_,used,blocks=r32.generate()
    assert len(got)==78 and len(runs)==298 and used==74 and blocks==148
    assert final==(-4017401528447,15321634290944)
    blob=r32.as_tsv(runs,['n0','n1','A0','B0','dA','dB'])
    digest=hashlib.sha256(blob).hexdigest()
    assert digest=='2573a84999d53dfd1cce772c45a41abaff251da735171efe904c860f2b2294f6'
    assert blob==(HERE/'src/AFFINE_RUNS_R32.tsv').read_bytes()
    print('R41_FULL_298',('ENDPOINT_ONLY' if force_endpoint else 'HYBRID'),
          len(comp.batch_methods),'initial stages',len(runs),'runs',final,digest)

if __name__=='__main__':
    run(False)
    run(True)
    print('PASS_R41_298_AFFINE_RUNS_WITH_HYBRID_AND_R40_FORCED_ENDPOINT')
