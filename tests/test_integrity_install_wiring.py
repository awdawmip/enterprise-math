"""Exercise real installer without importing the unrelated full Source history."""
import ast
from pathlib import Path
import sys
from types import ModuleType

import pytest

PATH=Path(__file__).resolve().parents[1]/'control_plane/research_task_integrity_fault_isolation.py'


def installer(monkeypatch,tmp_path):
    def module(name,**values):
        obj=ModuleType(name);obj.__dict__.update(values);monkeypatch.setitem(sys.modules,name,obj);return obj
    core=module('control_plane.research_task_records_impl')
    roots=[]
    publication=module('control_plane.research_publication_fault_isolation',install=lambda root:roots.append(root))
    module('control_plane',research_task_records_impl=core,research_publication_fault_isolation=publication)
    records=module('tools.research_task_records',current_records=lambda root:{'blocked':{},'ok':{}})
    dispatch=module('tools.research_dispatch',ROOT=tmp_path,merged_definitions=lambda root:[{'task_id':'ok'},{'task_id':'blocked'}])
    module('tools',research_task_records=records,research_dispatch=dispatch)
    validations=[]
    def validate(root):
        validations.append(root)
        if root.name=='invalid':raise ValueError('actual validation failed')
        return {'blocked':{'reason':'fixture'}}
    node=next(n for n in ast.parse(PATH.read_text()).body if isinstance(n,ast.FunctionDef) and n.name=='install')
    space={'Path':Path,'ROOT':tmp_path,'Any':object,'validated_quarantines':validate,
           'blocked_definition':lambda task,row,old:{**old,'blocked':True}}
    exec(compile(ast.Module(body=[node],type_ignores=[]),str(PATH),'exec'),space)
    return space['install'],records,dispatch,validations,roots


def test_install_wires_once_without_scanning_and_reads_still_validate(monkeypatch,tmp_path):
    install,records,dispatch,calls,roots=installer(monkeypatch,tmp_path)
    install(tmp_path);first=records.current_records
    install(tmp_path)
    assert records.current_records is first and calls==[]
    assert roots==[tmp_path,tmp_path]
    assert records.current_records(tmp_path)=={'ok':{}}
    assert dispatch.merged_definitions(tmp_path)==[{'task_id':'blocked','blocked':True},{'task_id':'ok'}]
    assert calls==[tmp_path,tmp_path]


def test_invalid_root_only_fails_when_its_data_is_consumed(monkeypatch,tmp_path):
    install,records,dispatch,calls,_=installer(monkeypatch,tmp_path)
    invalid=tmp_path/'invalid'
    install(invalid)
    assert calls==[]
    with pytest.raises(ValueError,match='actual validation failed'):records.current_records(invalid)
    with pytest.raises(ValueError,match='actual validation failed'):dispatch.merged_definitions(invalid)
    assert records.current_records(tmp_path)=={'ok':{}}
    assert calls==[invalid,invalid,tmp_path]


def test_bootstrap_does_not_duplicate_publication_install(monkeypatch,tmp_path):
    path=PATH.with_name('research_control_bootstrap.py')
    node=next(n for n in ast.parse(path.read_text()).body if isinstance(n,ast.FunctionDef) and n.name=='install')
    calls=[]
    names={n.value.id for n in ast.walk(node) if isinstance(n,ast.Attribute)
           and n.attr=='install' and isinstance(n.value,ast.Name)}
    from types import SimpleNamespace
    space={'Path':Path,'ROOT':tmp_path,'Any':object,
        '_install_operational_audit_views':lambda root:calls.append('operational')}
    for name in names:
        space[name]=SimpleNamespace(install=lambda root,n=name:calls.append(n))
    def integrity(root):
        calls.append('research_publication_fault_isolation')
        calls.append('research_task_integrity_fault_isolation')
    space['research_task_integrity_fault_isolation'].install=integrity
    dispatch=ModuleType('tools.research_dispatch');dispatch.ROOT=tmp_path
    dispatch.merged_definitions=lambda root:[]
    tools=ModuleType('tools');tools.research_dispatch=dispatch
    monkeypatch.setitem(sys.modules,'tools',tools)
    monkeypatch.setitem(sys.modules,'tools.research_dispatch',dispatch)
    exec(compile(ast.Module(body=[node],type_ignores=[]),str(path),'exec'),space)
    space['install'](tmp_path)
    assert calls.count('research_publication_fault_isolation')==1
    assert calls[:2]==['research_publication_fault_isolation','research_task_integrity_fault_isolation']
    assert set(names)<=set(calls)
