"""Read reuse is local to one immutable backend request, never a writer policy."""
from concurrent.futures import ThreadPoolExecutor
from contextvars import copy_context
from pathlib import Path
import sys

import pytest
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from control_plane.research_read_view import read_view,reuse_read,_CURRENT


def test_same_input_reads_once_and_return_values_are_isolated(tmp_path):
    calls=[]
    def compute():calls.append(1);return {'rows':[1]}
    with read_view(tmp_path):
        first=reuse_read(tmp_path,'k',{'v':1},compute)
        first['rows'].append(2)
        second=reuse_read(tmp_path,'k',{'v':1},compute)
        assert second=={'rows':[1]}
        second['rows'].append(3)
        assert reuse_read(tmp_path,'k',{'v':1},compute)=={'rows':[1]}
    assert calls==[1]
    assert _CURRENT.get() is None


def test_changed_input_and_new_request_are_fresh(tmp_path):
    calls=[]; inputs={'v':[1]}
    def compute():calls.append(1);return len(calls)
    with read_view(tmp_path):
        assert reuse_read(tmp_path,'k',inputs,compute)==1
        inputs['v'].append(2)
        assert reuse_read(tmp_path,'k',inputs,compute)==2
    with read_view(tmp_path):assert reuse_read(tmp_path,'k',inputs,compute)==3


def test_no_scope_and_other_root_always_compute(tmp_path):
    calls=[]
    def compute():calls.append(1);return 1
    reuse_read(tmp_path,'k',{},compute);reuse_read(tmp_path,'k',{},compute)
    with read_view(tmp_path):
        reuse_read(tmp_path/'other','k',{},compute)
        reuse_read(tmp_path/'other','k',{},compute)
    assert len(calls)==4


def test_failure_and_reentrant_partial_result_not_cached(tmp_path):
    calls=[]
    def fail():calls.append(1);raise ValueError('bad')
    with read_view(tmp_path):
        for _ in range(2):
            with pytest.raises(ValueError):reuse_read(tmp_path,'k',{},fail)
        def outer():return reuse_read(tmp_path,'k',{},lambda:'inner')+' outer'
        assert reuse_read(tmp_path,'k',{},outer)=='inner outer'
        assert reuse_read(tmp_path,'k',{},lambda:'wrong')=='inner outer'
    assert calls==[1,1]


def test_inherited_closed_view_cannot_reuse_results(tmp_path):
    with read_view(tmp_path):
        reuse_read(tmp_path,'k',{},lambda:'old')
        context=copy_context(); view=_CURRENT.get()
    assert not view.active and not view.values
    assert context.run(reuse_read,tmp_path,'k',{},lambda:'new')=='new'


def test_threads_and_nested_roots_do_not_share(tmp_path):
    with read_view(tmp_path):
        assert reuse_read(tmp_path,'k',{},lambda:'main')=='main'
        with ThreadPoolExecutor(1) as pool:
            assert pool.submit(reuse_read,tmp_path,'k',{},lambda:'thread').result()=='thread'
        with read_view(tmp_path/'other'):
            assert reuse_read(tmp_path/'other','k',{},lambda:'other')=='other'
        assert reuse_read(tmp_path,'k',{},lambda:'wrong')=='main'


def test_followup_wrapper_reuses_success_only_in_enabled_request(tmp_path):
    import ast
    file=Path(__file__).resolve().parents[1]/'control_plane/research_driver_followup_fault_isolation.py'
    tree=ast.parse(file.read_text())
    fn=next(n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name=='_validated_quarantines')
    calls=[]
    def actual(root,rows):calls.append(1);return {'packet':{'review_rows':rows}}
    ns={'Path':Path,'Any':object,'_compute_validated_quarantines':actual}
    exec(compile(ast.Module(body=[fn],type_ignores=[]),str(file),'exec'),ns)
    validate=ns['_validated_quarantines']
    with read_view(tmp_path):
        for _ in range(100):assert validate(tmp_path,{'R':{'valid':True}})['packet']
    assert len(calls)==1
    validate(tmp_path,{'R':{'valid':True}})
    assert len(calls)==2
