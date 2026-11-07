"""Current activity bookkeeping is not a connector-observation admission gate."""
from pathlib import Path
import json
import sys
import pytest
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from tools import research_activity as activity


def live(root):
    record=activity.registration(mode='TASK_RESEARCH',researcher_id='EM-TEST-01',session_id='session-A')
    path=activity.record_path(record['activity_id'],root);path.parent.mkdir(parents=True)
    path.write_bytes(activity.encoded(record))
    return record,path


def test_current_session_needs_no_tool_readback(tmp_path):
    record,path=live(tmp_path)
    before=path.read_bytes()
    result=activity.guard(activity_id=record['activity_id'],session_id='session-A',root=tmp_path)
    assert result['activity_allowed'] and result['persistence_allowed']
    assert all(v is False for v in result['authority'].values())
    assert path.read_bytes()==before


def test_old_receipt_metadata_does_not_control_current_activity(tmp_path):
    record,_=live(tmp_path)
    result=activity.guard(activity_id=record['activity_id'],session_id='session-A',root=tmp_path,
        registration_source={'old-tool':'different-display-url'},new_semantic_progress=True,boundary='pre-final')
    assert result['activity_allowed'] and result['persistence_allowed']


def test_progress_debt_does_not_prevent_preserving_more_results(tmp_path,monkeypatch):
    record,path=live(tmp_path)
    record['checkpoints']=[{'event_id':'old','state':'SYNC_DEBT'}]
    path.write_bytes(activity.encoded(record))
    monkeypatch.setattr(activity,'_events',lambda *a: (_ for _ in ()).throw(AssertionError('must not replay history')))
    result=activity.guard(activity_id=record['activity_id'],session_id='session-A',root=tmp_path)
    assert result['sync_debt_events']==['old'] and result['persistence_allowed']
    assert not result['checkpoint_status_is_acceptance']


def test_cross_session_binding_is_still_rejected(tmp_path):
    record,_=live(tmp_path)
    with pytest.raises(activity.ActivityError,match='different'):
        activity.guard(activity_id=record['activity_id'],session_id='session-B',root=tmp_path)
    assert not activity.guard(activity_id=record['activity_id'],root=tmp_path)['activity_allowed']


def test_absent_activity_does_not_create_registration(tmp_path):
    result=activity.guard(activity_id=None,root=tmp_path)
    assert not result['activity_allowed'] and not list(tmp_path.iterdir())


def test_retrospective_tracking_can_be_saved_but_never_claims_live_authority(tmp_path):
    record=activity.registration(mode='UNKNOWN_RESEARCH',source_tracking_key='historical')
    path=activity.record_path(record['activity_id'],tmp_path);path.parent.mkdir()
    path.write_bytes(activity.encoded(record))
    result=activity.guard(activity_id=record['activity_id'],root=tmp_path)
    assert result['persistence_allowed'] and not result['activity_allowed']
    assert all(v is False for v in result['authority'].values())


def test_checkpoint_append_does_not_replay_missing_historical_receipts(tmp_path):
    record,path=live(tmp_path)
    old={'event_id':'old','state':'EM_REPRESENTED','em_sources':[{'missing_old_receipt':True}],
         'kb_sources':[],'repairs_event_id':None}
    record['checkpoints']=[old]
    path.write_bytes(activity.encoded(record))
    updated=activity.checkpoint(record['activity_id'],root=tmp_path,event_id='new',
        expected_sha256=activity.digest(path.read_bytes()),em_sources=[],kb_sources=[])
    assert updated['checkpoints'][0]==old
    assert updated['checkpoints'][1]['event_id']=='new'
    assert updated['checkpoints'][1]['state']=='SYNC_DEBT'
    with pytest.raises(activity.ActivityError,match='conflict'):
        activity.checkpoint(record['activity_id'],root=tmp_path,event_id='new',
            expected_sha256=activity.digest(path.read_bytes()),em_sources=[],kb_sources=['changed'])


def test_deprecated_cli_readback_path_is_not_opened(tmp_path,capsys):
    record,_=live(tmp_path)
    rc=activity.main(['--root',str(tmp_path),'guard','--activity-id',record['activity_id'],
         '--session-id','session-A','--registration-json',str(tmp_path/'missing.json')])
    assert rc==0
    assert json.loads(capsys.readouterr().out)['persistence_allowed']


def test_malformed_old_event_id_does_not_block_an_unrelated_append(tmp_path):
    record,path=live(tmp_path)
    old={'event_id':['legacy-invalid'], 'old_material':'preserve'}
    record['checkpoints']=[old]
    path.write_bytes(activity.encoded(record))
    updated=activity.checkpoint(record['activity_id'],root=tmp_path,event_id='new',
        expected_sha256=activity.digest(path.read_bytes()),em_sources=[])
    assert updated['checkpoints'][0]==old
    assert updated['checkpoints'][1]['event_id']=='new'
