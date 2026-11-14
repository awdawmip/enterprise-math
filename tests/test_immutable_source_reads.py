"""Raw-byte reuse is distinct from interpretation, lifecycle and CLI reads."""
from contextvars import copy_context
import json

import pytest

from control_plane import research_read_view as view
from control_plane import research_task_records_impl as publications
from tools import research_execution_records as executions
import research_driver_authority as drivers
import research_review_evidence_store as evidence
import research_driver_followup_guard as followups
from types import SimpleNamespace


def test_cli_reads_and_new_native_views_remain_fresh(tmp_path):
    calls=[]
    def read():
        calls.append(None)
        return [{'value':len(calls)}]
    assert view.source_rows(tmp_path,'raw',read)==[{'value':1}]
    assert view.source_rows(tmp_path,'raw',read)==[{'value':2}]
    with view.immutable_source_view(tmp_path):
        first=view.source_rows(tmp_path,'raw',read)
        first[0]['value']=-1
        assert view.source_rows(tmp_path,'raw',read)==[{'value':3}]
    with view.immutable_source_view(tmp_path):
        assert view.source_rows(tmp_path,'raw',read)==[{'value':4}]


def test_raw_scope_does_not_cache_operational_bootstrap_interpretation(tmp_path):
    calls=[]
    def interpret():
        calls.append(None)
        return len(calls)
    with view.immutable_source_view(tmp_path):
        assert view.reuse_read(tmp_path,'operational',{},interpret)==1
        assert view.reuse_read(tmp_path,'operational',{},interpret)==2
        with view.read_view(tmp_path):
            assert view.reuse_read(tmp_path,'operational',{},interpret)==3
            assert view.reuse_read(tmp_path,'operational',{},interpret)==3
        with view.read_view(tmp_path):
            assert view.reuse_read(tmp_path,'operational',{},interpret)==4


def test_nested_roots_and_inherited_closed_contexts_are_isolated(tmp_path):
    first=tmp_path/'first';second=tmp_path/'second'
    calls=[]
    def read():
        calls.append(None);return len(calls)
    with view.immutable_source_view(first):
        assert view.source_rows(first,'records',read)==1
        with view.immutable_source_view(first):
            assert view.source_rows(first,'records',read)==1
        with view.immutable_source_view(second):
            assert view.source_rows(second,'records',read)==2
            assert view.source_rows(first,'records',read)==3
        assert view.source_rows(first,'records',read)==1
        inherited=copy_context()
    assert inherited.run(view.source_rows,first,'records',read)==4


def test_nested_json_containers_remain_caller_owned(tmp_path):
    def read():return [{'nested':{'values':[1,2]}}]
    with view.immutable_source_view(tmp_path):
        first=view.source_rows(tmp_path,'raw',read)
        first[0]['nested']['values'].append(3)
        assert view.source_rows(tmp_path,'raw',read)==[{'nested':{'values':[1,2]}}]


def test_exceptions_are_not_retained_and_exit_always_clears(tmp_path):
    def broken():raise ValueError('synthetic malformed input')
    with view.immutable_source_view(tmp_path):
        with pytest.raises(ValueError,match='synthetic malformed'):
            view.source_rows(tmp_path,'records',broken)
        assert view.source_rows(tmp_path,'records',lambda: 'fixed')=='fixed'
    with view.immutable_source_view(tmp_path):
        with pytest.raises(ValueError):view.source_rows(tmp_path,'records',broken)


def test_object_cache_excludes_other_roots_and_parent_paths(tmp_path):
    calls=[]
    def read():calls.append(None);return {'value':len(calls)}
    root=tmp_path/'source';inside=root/'record.json'
    with view.immutable_source_view(root):
        assert view.source_object(inside,read)=={'value':1}
        changed=view.source_object(inside,read);changed['value']=-1
        assert view.source_object(inside,read)=={'value':1}
        assert view.source_object(tmp_path/'other.json',read)=={'value':2}
        assert view.source_object(tmp_path/'other.json',read)=={'value':3}
        assert view.source_object(root/'..'/'other.json',read)=={'value':4}


@pytest.mark.parametrize('module,loader,directory,key',[
    (executions,'_parse_records','research_execution_records','ER-SYNTHETIC'),
    (publications,'_read_records','research_task_records','TP-SYNTHETIC'),
    (drivers,'_read_records',drivers.RECORD_ROOT,'DA-SYNTHETIC'),
])
def test_actual_record_loaders_scan_once_only_in_explicit_raw_scope(tmp_path,monkeypatch,module,loader,directory,key):
    path=tmp_path/directory/'SYNTHETIC'/f'{key}.json'
    path.parent.mkdir(parents=True);path.write_text(json.dumps({'synthetic':1}))
    original=getattr(module,loader);calls=[]
    def tracked(root):calls.append(None);return original(root)
    monkeypatch.setattr(module,loader,tracked)
    with view.immutable_source_view(tmp_path):
        first=module.iter_records(tmp_path);first[0]['synthetic']=-1
        assert module.iter_records(tmp_path)[0]['synthetic']==1
        assert len(calls)==1
    path.write_text(json.dumps({'synthetic':2}))
    assert module.iter_records(tmp_path)[0]['synthetic']==2
    assert len(calls)==2


def test_existing_review_json_validation_is_preserved(tmp_path):
    path=tmp_path/'review.json';path.write_text('[]')
    with view.immutable_source_view(tmp_path):
        with pytest.raises(evidence.ReviewEvidenceError,match='JSON object required'):
            evidence._load(path)
    path.write_text('{"synthetic":1}')
    with view.immutable_source_view(tmp_path):
        result=evidence._load(path);result['synthetic']=-1
        assert evidence._load(path)=={'synthetic':1}
    path.write_text('{"synthetic":2}')
    assert evidence._load(path)=={'synthetic':2}


def test_followup_interpretation_only_reuses_after_bootstrap_and_invalidates_readers(tmp_path,monkeypatch):
    readers=SimpleNamespace(iter_results=lambda root:[],iter_reviews=lambda root:[],result_map=lambda root:{})
    monkeypatch.setattr(followups,'_canonical_results',lambda:readers)
    calls=[]
    def calculate(root):
        calls.append(None);return {'synthetic':{'value':len(calls)}}
    monkeypatch.setattr(followups,'_authority_map_with_snapshot',calculate)
    with view.immutable_source_view(tmp_path):
        assert followups.authority_map(tmp_path)['synthetic']['value']==1
        assert followups.authority_map(tmp_path)['synthetic']['value']==2
        with view.read_view(tmp_path):
            first=followups.authority_map(tmp_path);first['synthetic']['value']=-1
            assert followups.authority_map(tmp_path)['synthetic']['value']==3
            readers.iter_reviews=lambda root:[]
            assert followups.authority_map(tmp_path)['synthetic']['value']==4
    assert followups.authority_map(tmp_path)['synthetic']['value']==5
