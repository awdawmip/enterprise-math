#!/usr/bin/env python3
"""Frozen-BRC, current-live-source audit of general signed X6 two-step midpoints.
Run with python, python -O and python -OO; requires the exact source layout.
"""
from __future__ import annotations
import ast
import contextlib
import hashlib
import io
import itertools
import json
from pathlib import Path
import runpy

ROOT=Path(__file__).resolve().parents[1]
P=ROOT/'experiments/x6_triadic_atomic_scatter_v1_20260906/check_triadic_atomic_scatter.py'
B=ROOT/'experiments/x6_signed_native_spatial_v16_20260905/signed_brc.py'

def git_blob(data):
    return hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()

def require(value, msg):
    if not value: raise AssertionError(msg)

p,brc_source_bytes=P.read_bytes(),B.read_bytes()
require(git_blob(p)=='cf5bc031b90b26d82216925d2768583db4e10f57','active source blob drift')
require(git_blob(brc_source_bytes)=='300a96e3dc24bf6fff73743037a0347a8bc83176','frozen signed BRC blob drift')
require(not any(isinstance(x,ast.Assert) for x in ast.walk(ast.parse(p.decode()))),'optimization guard regression')
out=io.StringIO()
with contextlib.redirect_stdout(out):
    ns=runpy.run_path(str(P))
require(hashlib.sha256(out.getvalue().encode()).hexdigest()=='03f98b37a4dcf346cc3a7063206f84253a3b7c1a219f1892f7967cd55201c2a2','original full-module stdout drift')
mid=ns['midpoint_options']; unit=ns['unit']; add=ns['add']; sub=ns['sub']; brc=ns['brc']
Z=(0,)*6
shift=(2,-1,1,0,0,-2)
valid=0; old_valid=0; translations=0
for a in itertools.product(range(-1,2),repeat=6):
    for i,j in itertools.combinations(range(6),2):
        for si,sj in itertools.product((-1,1),repeat=2):
            step1,step2=unit(i,si),unit(j,sj)
            b=add(add(a,step1),step2)
            actual=mid(a,b)
            expected={add(a,step1),add(a,step2)}
            require(set(actual)==expected and len(set(actual))==2,'native full midpoint set mismatch')
            require(all(brc.shortest_event_count(sub(w,a))==1 and brc.shortest_event_count(sub(b,w))==1 for w in actual),'nongeodesic midpoint')
            old={Z,add(a,b)}
            old_valid+=int(old==expected)
            valid+=1
            az,bz=add(a,shift),add(b,shift)
            require(set(mid(az,bz))=={add(w,shift) for w in expected},'translation covariance failure')
            translations+=1
require(valid==43740 and old_valid==120 and translations==43740,'census counts')
real_cases=0
for S in itertools.combinations(range(6),3):
    q=ns['q_triad'](S)
    for signs in itertools.product((-1,1),repeat=3):
        starts=[unit(i,s) for i,s in zip(S,signs)]
        targets=[ns['act'](q,a) for a in starts]
        for a,b in zip(starts,targets):
            require(mid(a,b)==(Z,add(a,b)),'original triadic branch identity drift')
            real_cases+=1
require(real_cases==480,'live original caller census')
invalid=[(Z,Z),(Z,unit(0,2)),(Z,unit(0)),(Z,unit(0,3))]
for a,b in invalid:
    try: mid(a,b)
    except AssertionError: pass
    else: raise AssertionError('illegal displacement accepted')
original=brc.shortest_path_multiplicity
try:
    brc.shortest_path_multiplicity=lambda z:0
    try: mid(unit(0),unit(1))
    except AssertionError: pass
    else: raise AssertionError('BRC fault not rejected')
finally:
    brc.shortest_path_multiplicity=original
record={
  'schema':'X6_UNIT129_TRANSLATION_COVARIANT_NATIVE_MIDPOINT_CERT_V1',
  'model':'P000 six signed Cell axes; L1 length 2, Bmin 2',
  'source_blob':git_blob(p),'frozen_brc_blob':git_blob(brc_source_bytes),
  'legal_2_step_signed_pairs':valid,
  'new_correct':valid,
  'old_correct':old_valid,
  'old_off_domain_invalid':valid-old_valid,
  'translation_covariance_cases':translations,
  'real_triad_caller_pairs':real_cases,
  'invalid_rejection_cases':len(invalid),
  'mutated_brc_rejection_cases':1,
  'full_module_stdout_sha256':hashlib.sha256(out.getvalue().encode()).hexdigest(),
  'status':'AUTHOR_LOCAL_EXECUTED_UNREVIEWED_NOT_ADMITTED'
}
print(json.dumps(record,ensure_ascii=False,sort_keys=True,separators=(',',':')))
