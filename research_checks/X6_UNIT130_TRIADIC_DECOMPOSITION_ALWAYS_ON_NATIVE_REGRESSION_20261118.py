#!/usr/bin/env python3
"""Actual current signed triadic decomposition BRC checker three-mode integrity and fault test.
Run this single file from the Enterprise Math checkout with Python 3; no network needed.
The historical false PASS was established against the exact unmodified former source.
"""
from __future__ import annotations
import ast
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile

ROOT=Path(__file__).resolve().parents[1]
PATH=ROOT/'experiments/x6_triadic_decomposition_brc_v2_20260906/check_triadic_decomposition_brc.py'


def check(ok, msg):
    if not ok: raise AssertionError(msg)


def git_blob(b):
    return hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()


source=PATH.read_bytes()
check(git_blob(source)=='d2b4ce1c13f90e31ca1167ee1eea1ef49c24b95d','current source exact blob mismatch')
tree=ast.parse(source)
check(not any(isinstance(node,ast.Assert) for node in ast.walk(tree)), 'live mathematical assert elision')
text=source.decode()
checks=re.findall(r'unit130_guard_\d\d',text)
check(len(checks)==14 and len(set(checks))==14,'14 original proof obligations must remain live')
old='    return n\n\n# Exhaustive signed ordered branch census'
check(text.count(old)==1,'fault injection point not uniquely present')
mutated=text.replace(old,'    return 0\n\n# Exhaustive signed ordered branch census')
expected_stdout_sha='c7c06070d738fe78128ef2683cfcebf04195658bf2793993bed90e0bd7489dbc'
rows=[]
with tempfile.TemporaryDirectory(prefix='x6-unit130-') as tmp:
    p=Path(tmp)/'controlled_brc_fault.py'
    p.write_text(mutated)
    for mode,flags in [('normal',[]),('-O',['-O']),('-OO',['-OO'])]:
        env=dict(os.environ, PYTHONHASHSEED='0')
        clean=subprocess.run([sys.executable,*flags,str(PATH)],capture_output=True,env=env,check=False)
        faulty=subprocess.run([sys.executable,*flags,str(p)],capture_output=True,env=env,check=False)
        clean_sha=hashlib.sha256(clean.stdout).hexdigest()
        check(clean.returncode==0 and clean_sha==expected_stdout_sha,f'clean invalid: {mode}')
        check(faulty.returncode!=0 and b'unit130_guard_06' in faulty.stderr,f'mutation escaped: {mode}')
        rows.append({'mode':mode,'clean_exit':clean.returncode,'clean_stdout_sha256':clean_sha,
                     'mutation_exit':faulty.returncode,'mutation_rejected_at':'unit130_guard_06'})
record={'schema':'X6_UNIT130_ALWAYS_ON_NATIVE_VALIDATION_V1',
        'source_git_blob_sha1':git_blob(source),'mathematical_conditions_always_on':14,
        'full_original_output_sha256':expected_stdout_sha,
        'degree_vectors_checked':2493,'signed_formula_states_checked':5444,
        'atomic_signed_triad_types':160,'two_event_histories':25600,
        'test_modes':rows,
        'scope':'real existing active signed triadic decomposition module, not R063 benchmark',
        'author_status':'EXECUTED_UNREVIEWED_NOT_ADMITTED'}
print(json.dumps(record,sort_keys=True,separators=(',',':')))
