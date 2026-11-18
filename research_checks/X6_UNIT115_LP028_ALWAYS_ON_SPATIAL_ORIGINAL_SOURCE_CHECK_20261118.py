#!/usr/bin/env python3
"""Unit115: source-pinned LP028 original check_spatial always-on guard regression.

Original R063 fixed-chart source is not modified. A temporary AST function lift
replaces only its seven check_spatial assert statements with always-on guards.
This is NOT an execution of the native C3/C4 benchmark.
"""
from __future__ import annotations
import ast
import copy
import hashlib
import importlib.util
import json
import pathlib
import sys

ORIGINAL='experiments/tool_discovery_native_geometry_of_numbers_minima_calculus_20260822.py'
PIN='643b2bac659a445891dcb5588b647972977104e0'


def require(c,msg):
    if not c: raise RuntimeError(msg)


def load_source(path):
    raw=path.read_bytes()
    blob=hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()
    require(blob==PIN,'original source Git blob mismatch')
    spec=importlib.util.spec_from_file_location('x6_r063_original_checked',path)
    mod=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod,raw,blob


def build_always_on(mod,raw):
    tree=ast.parse(raw.decode('utf-8'))
    fns=[x for x in tree.body if isinstance(x,ast.FunctionDef) and x.name=='check_spatial']
    require(len(fns)==1,'check_spatial not uniquely found')
    node=copy.deepcopy(fns[0])
    guards=sum(isinstance(x,ast.Assert) for x in ast.walk(node))
    require(guards==7,'unexpected number of original assertions')
    class Lift(ast.NodeTransformer):
        def visit_Assert(self,n):
            self.generic_visit(n)
            replacement=ast.If(
                test=ast.UnaryOp(op=ast.Not(),operand=n.test),
                body=[ast.Raise(exc=ast.Call(func=ast.Name(id='RuntimeError',ctx=ast.Load()),
                          args=[ast.Constant(value='ALWAYS_ON_SOURCE_GUARD_LINE_'+str(n.lineno))],keywords=[]),cause=None)],
                orelse=[])
            return ast.copy_location(replacement,n)
    node=Lift().visit(node)
    module=ast.fix_missing_locations(ast.Module(body=[node],type_ignores=[]))
    exec(compile(module,filename=ORIGINAL,mode='exec'),mod.__dict__)
    return mod.check_spatial,guards


def result_digest(obj):
    return hashlib.sha256(json.dumps(obj,sort_keys=True,separators=(',',':')).encode()).hexdigest()


def guarded_residue(old,stats):
    def wrapper(point,modulus):
        stats['calls']+=1
        a,b,c=point
        require(type(a) is int and type(b) is int and type(c) is int and
                a>=0 and b>=0 and c==0 and type(modulus) is int and modulus>=1,
                'original check_spatial internal call left the fixed-positive chart')
        value=old(point,modulus)
        require(value==(a%modulus,b%modulus),'original in-chart residue mismatch')
        return value
    return wrapper


def execute(fn,mod,residue):
    mod.residue=residue
    try:
        result=fn()
        return {'kind':'RETURN','rows':len(result['spatial_modular_sector']),'sha256':result_digest(result)}
    except Exception as e:
        return {'kind':'RAISED','exception':type(e).__name__}


def main(path):
    mod,raw,blob=load_source(path)
    orig=mod.check_spatial
    old_residue=mod.residue
    strict,guard_count=build_always_on(mod,raw)
    a={'calls':0}
    b={'calls':0}
    ordinary=execute(orig,mod,guarded_residue(old_residue,a))
    checked=execute(strict,mod,guarded_residue(old_residue,b))
    require(ordinary==checked and ordinary['kind']=='RETURN' and ordinary['rows']==19,
            'unchanged original and always-on outputs differ')
    require(b['calls']==6194,'always-on expected exact native callable executions changed')
    expected_original=6194 if sys.flags.optimize==0 else 228
    require(a['calls']==expected_original,'original optimization call erasure count changed')
    bad=lambda point,m:(0,0)
    wrong_original=execute(orig,mod,bad)
    wrong_strict=execute(strict,mod,bad)
    if sys.flags.optimize==0:
        require(wrong_original=={'kind':'RAISED','exception':'AssertionError'},'original normal mutation should fail')
    else:
        require(wrong_original['kind']=='RETURN' and wrong_original['rows']==19,
                'original optimized mutation should falsely return')
    require(wrong_strict=={'kind':'RAISED','exception':'RuntimeError'},
            'strict mutation should be rejected in all modes')
    output={
      'schema':'ENTERPRISE_MATH_X6_UNIT115_LP028_ORIGINAL_SPATIAL_ALWAYS_ON_CHECK_V1',
      'source_git_blob_sha1':blob,
      'optimization':sys.flags.optimize,
      'source_assert_guards_in_check_spatial':guard_count,
      'original_residue_calls':a['calls'],
      'always_on_residue_calls':b['calls'],
      'all_original_internal_calls_valid_fixed_positive_chart':True,
      'unmodified_original':ordinary,
      'opt_in_always_on':checked,
      'constant_residue_fault_original':wrong_original,
      'constant_residue_fault_always_on':wrong_strict,
      'test_scope':'actual old check_spatial only; no original native R063/Helly C3/C4 benchmark'
    }
    print(json.dumps(output,sort_keys=True,separators=(',',':')))


if __name__=='__main__':
    args=sys.argv[1:]
    if len(args)==2 and args[0]=='--source':
        source=pathlib.Path(args[1])
    elif not args:
        source=pathlib.Path(ORIGINAL)
    else:
        raise SystemExit('usage: checker.py [--source exact_original.py]')
    main(source)
