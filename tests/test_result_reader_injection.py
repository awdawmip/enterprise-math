"""Focused reducer tests; extract real function bodies without loading history."""
import ast
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import threading
from types import SimpleNamespace

import pytest

ROOT=Path(__file__).resolve().parents[1]


def reducer():
    source=ROOT/'control_plane/research_result_records_compat_runtime.py'
    parsed=ast.parse(source.read_text())
    nodes=[n for n in parsed.body if isinstance(n,ast.FunctionDef)
           and n.name in {'_single_result_state','task_result_state'}]
    state={'phase':'SINGLE_RESULT_FLOW'}
    ns={'ROOT':ROOT,'Path':Path,'Any':object,'TERMINAL_DISPOSITIONS':{'ACCEPT'},
        'ResultRecordError':ValueError,'_publication_for_state':lambda t,r,p:p,
        '_parallel':SimpleNamespace(state=lambda t,p,r:{'parallel_state':state['phase'],
            'result_ids':['A','B'],'intake_id':'I','evidence_set_sha256':'H'}),
        'iter_results':lambda r:[{'task_id':'T','publication_id':'P','result_id':'default'}],
        'latest_review':lambda rid,r:None,'_parallel_synthesis':lambda *args:None}
    exec(compile(ast.Module(body=nodes,type_ignores=[]),str(source),'exec'),ns)
    return ns,state


def test_default_readers_retain_old_result_semantics():
    ns,_=reducer()
    result=ns['task_result_state']('T',ROOT,'P')
    assert result['state']=='AWAITING_DRIVER_REVIEW'
    assert result['result']['result_id']=='default'


def test_explicit_readers_do_not_replace_base_globals():
    ns,_=reducer(); before={key:ns[key] for key in ('iter_results','latest_review','_parallel_synthesis')}
    result=ns['task_result_state']('T',ROOT,'P',
        result_reader=lambda r:[{'task_id':'T','publication_id':'P','result_id':'explicit'}],
        review_reader=lambda rid,r:{'disposition':'ACCEPT'})
    assert result['terminal'] and result['result']['result_id']=='explicit'
    assert all(ns[key] is value for key,value in before.items())
    assert ns['task_result_state']('T',ROOT,'P')['result']['result_id']=='default'


def test_exception_does_not_require_restoring_global_readers():
    ns,_=reducer(); original=ns['iter_results']
    def broken(root):raise RuntimeError('reader failed')
    with pytest.raises(RuntimeError):ns['task_result_state']('T',ROOT,'P',result_reader=broken)
    assert ns['iter_results'] is original


def test_non_lifo_threads_keep_their_own_reader():
    ns,_=reducer(); a_entered=threading.Event(); b_entered=threading.Event(); a_done=threading.Event()
    def a_reader(root):
        a_entered.set(); assert b_entered.wait(2)
        return [{'task_id':'T','publication_id':'P','result_id':'A'}]
    def b_reader(root):
        assert a_entered.wait(2); b_entered.set(); assert a_done.wait(2)
        return [{'task_id':'T','publication_id':'P','result_id':'B'}]
    def first():
        value=ns['task_result_state']('T',ROOT,'P',result_reader=a_reader)
        a_done.set();return value
    with ThreadPoolExecutor(2) as pool:
        a=pool.submit(first)
        b=pool.submit(ns['task_result_state'],'T',ROOT,'P',result_reader=b_reader)
        assert a.result()['result']['result_id']=='A'
        assert b.result()['result']['result_id']=='B'
    assert ns['task_result_state']('T',ROOT,'P')['result']['result_id']=='default'


def test_parallel_synthesis_reader_is_explicit():
    ns,state=reducer();state['phase']='PARALLEL_SYNTHESIS_TERMINAL'
    result=ns['task_result_state']('T',ROOT,'P',
       synthesis_reader=lambda i,h,r:{'synthesis_id':'S','terminal_control_disposition':'ACCEPT'})
    assert result['terminal'] and result['result']['result_id']=='S'
    assert ns['task_result_state']('T',ROOT,'P')['parallel_state']=='AWAITING_SYNTHESIS'


def test_facade_forwards_readers_without_global_setattr():
    source=ROOT/'tools/research_result_records.py'; parsed=ast.parse(source.read_text())
    assert not any(isinstance(n,ast.FunctionDef) and n.name=='_base_runtime_view' for n in parsed.body)
    node=next(n for n in parsed.body if isinstance(n,ast.FunctionDef) and n.name=='_task_result_state_operational')
    captured={}
    def base(*args,**kwargs):captured.update(kwargs);return None
    result_reader=lambda r:[]; review_reader=lambda *args:None; synthesis=lambda *args:None
    ns={'ROOT':ROOT,'Path':Path,'Any':object,'_BASE_TASK_RESULT_STATE':base,
        'iter_results':result_reader,'latest_review':review_reader,'_parallel_synthesis':synthesis}
    exec(compile(ast.Module(body=[node],type_ignores=[]),str(source),'exec'),ns)
    assert ns['_task_result_state_operational']('T',ROOT,'P') is None
    assert captured=={'result_reader':result_reader,'review_reader':review_reader,'synthesis_reader':synthesis}
