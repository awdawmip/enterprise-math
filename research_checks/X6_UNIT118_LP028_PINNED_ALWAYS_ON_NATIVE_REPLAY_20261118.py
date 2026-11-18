#!/usr/bin/env python3
"""Versioned strict runner for the actual, pinned LP028 signed R063 source consumer.

Requires the original enterprise-math repository checkout. It never edits the
original modules. The source guard conversion is limited to original Python
assert checks, demonstrably erased by -O/-OO (Unit117).

Status on publication: source implementation and isolated AST smoke verified;
full original-module native run requires the actual pinned checkout.
"""
from __future__ import annotations

import ast
from collections import Counter
from contextlib import redirect_stdout
from hashlib import sha1, sha256
from io import StringIO
import json
from pathlib import Path
import types

ORIGINAL_REL = 'research_checks/X6_LP028_SIGNED_PATHSQRT_TYPED_CURRENT_CONSUMER_CHECK_20261112_2300.py'
ORIGINAL_BLOB = 'db46dde5a962b93b65775bf2b4d8f52d5e3f83b9'
EXPECTED_NATIVE_COMPARISONS = 24600
EXPECTED_GUARD_COUNT = 13


def blob_sha1(data: bytes) -> str:
    return sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()


class AlwaysOnAsserts(ast.NodeTransformer):
    """Turn exactly the original module's assert nodes into if/raise guards."""
    def __init__(self):
        self.count = 0

    def visit_Assert(self, node: ast.Assert):
        self.count += 1
        label = f'original source assertion at line {node.lineno}'
        message = node.msg if node.msg is not None else ast.Constant(label)
        statement = ast.If(
            test=ast.UnaryOp(op=ast.Not(), operand=self.visit(node.test)),
            body=[ast.Raise(exc=ast.Call(func=ast.Name(id='AssertionError',ctx=ast.Load()),
                                         args=[message], keywords=[]), cause=None)],
            orelse=[])
        return ast.copy_location(statement, node)


def load_source_guarded(original: Path):
    data = original.read_bytes()
    actual = blob_sha1(data)
    if actual != ORIGINAL_BLOB:
        raise RuntimeError(f'original LP028 Git blob mismatch: {actual} != {ORIGINAL_BLOB}')
    tree = ast.parse(data, filename=str(original))
    rewrite = AlwaysOnAsserts()
    tree = rewrite.visit(tree)
    ast.fix_missing_locations(tree)
    if rewrite.count != EXPECTED_GUARD_COUNT or any(isinstance(x,ast.Assert) for x in ast.walk(tree)):
        raise RuntimeError(f'unexpected guard inventory {rewrite.count}')
    module=types.ModuleType('x6_unit118_pinned_source_replay')
    module.__file__=str(original)
    exec(compile(tree,str(original),'exec'),module.__dict__)
    return module,rewrite.count


def run(root: Path):
    original=root/ORIGINAL_REL
    mod,guards=load_source_guarded(original)
    functions=('shortest_path_multiplicity','endpoint_multiplicity',
               'full_distance_squared','spatial_norm_squared')
    counters=Counter()
    for name in functions:
        f=getattr(mod,name)
        def wrapper(*args,_func=f,_name=name,**kw):
            counters[_name]+=1
            return _func(*args,**kw)
        setattr(mod,name,wrapper)
    stream=StringIO()
    with redirect_stdout(stream):
        mod.main()
    output=stream.getvalue()
    if 'PASS_SIGNED_PATHSQRT_CURRENT_SOURCE_IMPORT' not in output:
        raise RuntimeError('missing original PASS marker')
    for f in functions:
        if counters[f]!=EXPECTED_NATIVE_COMPARISONS:
            raise RuntimeError(f'actual native calls {f}={counters[f]}, expected {EXPECTED_NATIVE_COMPARISONS}')
    validated_native_counts = dict(sorted(counters.items()))
    # Fault injection only in this independent module namespace. The pristine
    # original source and imported native kernel are not edited.
    old=mod.shortest_path_multiplicity
    mod.shortest_path_multiplicity=lambda d:old(d)+1
    try:
        mod.exhaustive_labelled_charts(1,mod.Spatial6())
    except AssertionError:
        mutation_rejected=True
    else:
        mutation_rejected=False
    if not mutation_rejected:
        raise RuntimeError('wrong native BRC return was not rejected')
    result={
      'schema':'X6_UNIT118_PINNED_ALWAYS_ON_NATIVE_REPLAY_V1',
      'original_source':ORIGINAL_REL,
      'original_blob':ORIGINAL_BLOB,
      'actual_guards_lifted':guards,
      'actual_native_call_counts':validated_native_counts,
      'fault_injection_rejected':mutation_rejected,
      'original_stdout_sha256':sha256(output.encode()).hexdigest(),
      'original_stdout_final_line':output.strip().splitlines()[-1],
      'scope':'ACTUAL_UNMODIFIED_SOURCE_MODULE_IMPORTS_VIA_PINNED_ORIGINAL_CHECKER',
    }
    return result


def main():
    root=Path(__file__).resolve().parents[1]
    print(json.dumps(run(root),sort_keys=True,separators=(',',':')))


if __name__=='__main__':
    main()
