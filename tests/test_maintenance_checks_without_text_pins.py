"""Maintenance checks must not require exact prose or source spelling."""
import importlib.util
import json
from pathlib import Path

import pytest


def load(name,root):
    path=Path(__file__).resolve().parents[1]/'control_plane'/(name+'.py')
    spec=importlib.util.spec_from_file_location(name,path)
    obj=importlib.util.module_from_spec(spec);spec.loader.exec_module(obj);obj.ROOT=root
    return obj


def task_config():
    return dict(remote_manual_transport_fallback_allowed=True,
        remote_manual_validation_fallback_allowed=False,
        remote_manual_equivalent_preflight_required=True,
        remote_manual_body_style_required=False,
        remote_manual_exact_taskbook_blob_required=True,
        remote_manual_exact_supersedes_required_when_revision=True,
        remote_manual_unresolved_fork='FAIL_CLOSED_NO_HEAD_SELECTION',
        remote_manual_cas_nonforce_required=True,
        reference_integrity_is_publication_authorization=False,
        if_equivalent_preflight_unavailable='NONEXECUTABLE_DRAFT_OR_HANDOFF_ONLY')


def test_remote_checker_does_not_open_protocol_or_source(tmp_path):
    path=tmp_path/'control_plane/current_control_authority.json';path.parent.mkdir()
    task=task_config();task['remote_manual_recommended_body_sections']=['user-defined label']
    path.write_text(json.dumps({'task_publication':task}))
    check=load('check_remote_manual_publication_preflight',tmp_path)
    check.check()  # No protocol, source, renderer or fixed headings exist here.
    task['remote_manual_cas_nonforce_required']=False
    path.write_text(json.dumps({'task_publication':task}))
    with pytest.raises(check.RemotePublicationPreflightError,match='CAS'):
        check.check()


def test_authority_configuration_errors_remain_errors(tmp_path):
    for name in ['control_plane/current_control_authority.json',
        'research_task_publication_contract_v2.json','research_dispatch_contract.json',
        'tool_invocation_policy.json','control_plane/role_transition_matrix.json']:
        path=tmp_path/name;path.parent.mkdir(parents=True,exist_ok=True);path.write_text('{}')
    check=load('check_current_control_authority',tmp_path)
    with pytest.raises(check.ControlAuthorityError,match='wrong schema'):
        check.check()
