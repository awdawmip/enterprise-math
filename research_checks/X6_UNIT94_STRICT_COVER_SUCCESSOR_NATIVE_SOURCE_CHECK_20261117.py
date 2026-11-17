#!/usr/bin/env python3
"""Unit94: exact typed CoverState successor vs frozen original. No project benchmark."""
from __future__ import annotations
import hashlib, json, os, sys
from itertools import product
from pathlib import Path

HERE=Path(__file__).resolve().parent
COORD=HERE.parent / "experiments" / "x6_native_coordinate_completion_v7_20260905"
sys.path.insert(0,str(COORD))
from x6_coordinate import Coord6,canonical
import x6_cover
import x6_cover_strict_v2 as strict

ORIGINAL_SHA='171baf1cee7f1aceaf38c73d0c0659a25fd8d7bd'

def blob_sha(path):
    b=Path(path).read_bytes()
    return hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()

def require(condition,message):
    if not condition: raise AssertionError(message)

def reduced(z,m):
    h=min(z)
    return tuple(v-h for v in z), h if m==0 else h%m

def read(s):
    return s.coordinate.values,s.depth,s.modulus

def expected(z,axis,d,m):
    arr=list(z);arr[axis]+=d
    k=reduced(arr,m)
    return (*k,m)

def main():
    require(blob_sha(COORD/'x6_cover.py')==ORIGINAL_SHA,'frozen source blob changed')
    checks=0
    for z in product((-1,0,1),repeat=6):
        h=min(z)
        relative=Coord6(canonical(z))
        for m in range(5):
            old=x6_cover.CoverState(relative,h,m)
            new=strict.CoverState(relative,h,m)
            require(read(old)==read(new),'source construction mismatch')
            for axis in range(6):
                for d in (-1,1):
                    a=old.step(axis,d)
                    b=new.step(axis,d)
                    exp=expected(z,axis,d,m)
                    require(read(a)==read(b)==exp,(z,m,axis,d,read(a),read(b),exp))
                    if m==0: require(b.signed_native_displacement()==tuple(z[i]+(d if i==axis else 0) for i in range(6)),'m0 native lift wrong')
                    checks+=1
    invalid=(True,False,1.0,-1.0,'1',None,0,2)
    for m in range(5):
        new=strict.CoverState(Coord6((0,)*6),0,m)
        old=x6_cover.CoverState(Coord6((0,)*6),0,m)
        require(read(old.step(0,True))==read(old.step(0,1)),'original True witness disappeared')
        for bad in invalid:
            try:new.step(0,bad)
            except ValueError:pass
            else:raise AssertionError(('invalid accepted',m,repr(bad)))
        for bad in (True,False,1.0,-1.0,'0',None,-1,6):
            try:new.step(bad,1)
            except ValueError:pass
            else:raise AssertionError(('axis invalid accepted',m,repr(bad)))
    for m in range(5):
        s=strict.CoverState(Coord6((0,)*6),0,m)
        t=strict.diagonal_loop(s,2)
        u=x6_cover.diagonal_loop(x6_cover.CoverState(Coord6((0,)*6),0,m),2)
        require(isinstance(t,strict.CoverState),'successor diagonal return type changed')
        require(read(t)==read(u),'diagonal depth mismatch')
        try:strict.CoverState(Coord6((0,)*6),0,m).step(0,True)
        except ValueError:pass
        else:raise AssertionError('True accepted')
    summary={
        'schema':'EM_X6_UNIT94_STRICT_COVER_SUCCESSOR_CHECK_V1',
        'frozen_cover_git_blob_sha1':ORIGINAL_SHA,
        'strict_cover_git_blob_sha1':blob_sha(COORD/'x6_cover_strict_v2.py'),
        'execution_environment':'CPython with exact original x6_cover blob and extracted necessary Coord6 dependency, NOT complete project source tree',
        'original_full_coordinate_module_executed':False,
        'original_native_R063_Helly_or_LP026_full_benchmark_executed':False,
        'witness_original_true_accepted':True,
        'strict_rejected_direction_types':[repr(x) for x in invalid],
        'states':729,'moduli':5,'axes':6,'directions':2,
        'integer_transition_checks':checks,
        'verified_diagonal_loop_moduli':5,
        'all_checks_passed':True,
    }
    print(json.dumps(summary,ensure_ascii=False,sort_keys=True,separators=(',',':')))

if __name__=='__main__':main()
