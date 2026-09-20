import base64
import copy
import importlib.util
import os
from pathlib import Path
import sys
import unittest

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,os.environ.get('EM_SOURCE_ROOT',str(ROOT)))
spec=importlib.util.spec_from_file_location('activity_mcp_under_test',ROOT/'tools/research_activity.py')
activity=importlib.util.module_from_spec(spec)
spec.loader.exec_module(activity)


class McpContentsReadbackTest(unittest.TestCase):
    def fixture(self):
        content=b'actual source bytes\n';path='research_activity_records/RA-12345678.json';commit='a'*40
        encoded=base64.b64encode(content).decode();url=f'https://github.com/awdawmip/enterprise-math/blob/{commit}/{path}'
        pin={'repository':'awdawmip/enterprise-math','commit':commit,'path':path,'sha256':activity.digest(content)}
        observed={'tool_name':'em_mcp_github_contents','observation_id':'actual-api-receipt',
          'arguments':{'repository_full_name':pin['repository'],'ref':commit,'path':path},
          'result':{'isError':False,'structuredContent':{'encoding':'base64','content':encoded,'sha':activity.blob_id(content),'display_url':url}},
          'github_response':{'type':'file','path':path,'encoding':'base64','content':encoded+'\n','sha':activity.blob_id(content),'size':len(content),'html_url':url}}
        return pin,observed

    def test_actual_api_transport_is_typed_without_fabricating_connector_call(self):
        pin,observed=self.fixture();value=activity.verify_observation(observed,pin)
        self.assertEqual(value['tool_name'],'em_mcp_github_contents')
        self.assertEqual(value['kind'],'OBSERVED_MCP_GITHUB_API_STRUCTURE_AND_BYTES_VERIFIED')
        self.assertFalse(value['network_request_by_this_tool'])
        self.assertFalse(value['server_signature_authenticated'])

    def test_missing_raw_response_cannot_impersonate_mcp_readback(self):
        pin,observed=self.fixture();del observed['github_response']
        with self.assertRaises(activity.ActivityError):activity.verify_observation(observed,pin)

    def test_tampered_response_bytes_path_sha_ref_size_or_type_fail(self):
        pin,observed=self.fixture()
        changes={'content':base64.b64encode(b'different').decode(),'path':'other.json','sha':'b'*40,
                 'html_url':'https://github.com/awdawmip/enterprise-math/blob/main/unknown','size':1,'type':'symlink'}
        for key,value in changes.items():
            with self.subTest(field=key):
                altered=copy.deepcopy(observed);altered['github_response'][key]=value
                with self.assertRaises(activity.ActivityError):activity.verify_observation(altered,pin)

    def test_existing_connector_observation_contract_is_unchanged(self):
        pin,observed=self.fixture();observed['tool_name']='github_fetch_file';del observed['github_response']
        self.assertEqual(activity.verify_observation(observed,pin)['kind'],'OBSERVED_CONNECTOR_STRUCTURE_AND_BYTES_VERIFIED')


if __name__=='__main__':unittest.main()
