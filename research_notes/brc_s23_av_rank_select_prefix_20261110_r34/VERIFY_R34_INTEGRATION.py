#!/usr/bin/env python3
"""Integrated R33 quotient-jump + R34 rank/select prefix + R32 long-tail bulk compiler.

Requires exact predecessor code files, supplied explicitly as filesystem paths.
No download/network; upstream interfaces are imported unchanged, and the two
entrypoints are wired by transparent function injection for this regression.
"""
from __future__ import annotations
import argparse,csv,hashlib,importlib.util,sys
from pathlib import Path
HERE=Path(__file__).resolve().parent

def load(name,filepath):
    spec=importlib.util.spec_from_file_location(name,filepath)
    assert spec and spec.loader
    obj=importlib.util.module_from_spec(spec)
    sys.modules[name]=obj
    spec.loader.exec_module(obj)
    return obj

def main():
    a=argparse.ArgumentParser()
    a.add_argument('--r32',type=Path,required=True,help='Immutable R32 VERIFY_R32.py source')
    a.add_argument('--r33',type=Path,required=True,help='Immutable R33 VERIFY_R33.py source')
    a.add_argument('--reference',type=Path,help='Optional R32 affine-run reference TSV')
    a.add_argument('--out',type=Path,default=HERE/'AFFINE_RUNS_R34.tsv')
    args=a.parse_args()
    prefix=load('R34_PREFIX',HERE/'VERIFY_R34_PREFIX.py')
    r32=load('R32_BASE',args.r32)
    r33=load('R33_JUMPS',args.r33)
    stages,_,_,jumps=r33.jump_stages()
    prefixes,regimes,at389,q,events=prefix.compile_prefix()
    assert len(stages)==78 and jumps==28 and len(prefixes)==4 and len(regimes)==3
    assert len(events)==225 and q==6
    # Wire the *new* provenance-labelled initial segment selector into the
    # already verified R32 long-tail compiler. Do not modify either upstream file.
    r32.early_updates=lambda: list(prefixes)
    r32.produce_farey_stages=lambda:(stages,0,0)
    got_stages,runs,segs,final,_,_,used,blocks=r32.generate()
    assert got_stages==stages and len(runs)==298 and used==74 and blocks==148
    assert final==(-4017401528447,15321634290944)
    data=r32.as_tsv(runs,['n0','n1','A0','B0','dA','dB'])
    args.out.write_bytes(data)
    digest=hashlib.sha256(data).hexdigest()
    expected='2573a84999d53dfd1cce772c45a41abaff251da735171efe904c860f2b2294f6'
    assert digest==expected,(digest,expected)
    if args.reference:
        assert data==args.reference.read_bytes()
        print('INDEPENDENT_R32_COMPLETE_TSV_MATCH',len(runs),'of',len(runs))
    print('PREFIX',len(regimes),'farey stages','6 exact risk endpoint calls','225 sourced events; 4 maximal prefix intervals')
    print('JUMPS',jumps,'certified quotient decisions; complete Farey stages',len(stages))
    print('BULK',blocks,'positive blocks; complete affine segments',len(runs))
    print('FINAL_RISK',final)
    print('R34_AFFINE_SHA256',digest)
    print('PASS_R34_NO_STEPWISE_PREFIX_END_TO_END_298')

if __name__=='__main__':main()
