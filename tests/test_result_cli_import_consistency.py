"""The command-line and package imports compose the compatibility reader once."""
from pathlib import Path
import os
import subprocess
import sys
import textwrap
import unittest

PROGRAM = r'''
from pathlib import Path
import importlib, runpy, sys, tempfile
root=Path(sys.argv[1]);sys.path.insert(0,str(root))
from control_plane import research_result_records_compat_runtime as compat
calls=[]
def base(*args,**kwargs):
    calls.append((args,kwargs))
    if sys.argv[2]=='exception':raise ValueError('exact immutable Result failed validation')
    return None
compat.task_result_state=base
first=runpy.run_path(str(root/'tools/research_result_records.py'),run_name='first_cli_import')
def stale_facade(*args,**kwargs):
    raise AssertionError('a package import reentered the earlier CLI facade')
first['task_result_state'].__globals__['_task_result_state_operational']=stale_facade
canonical=importlib.import_module('tools.research_result_records')
if sys.argv[2]=='three_imports':
    third=runpy.run_path(str(root/'tools/research_result_records.py'),run_name='third_cli_import')
    reduce=third['_task_result_state_operational']
else:
    reduce=canonical._task_result_state_operational
with tempfile.TemporaryDirectory() as temporary:
    try:
        result=reduce('RS-ISOLATED-IMPORT',Path(temporary),'TP2-ISOLATED')
    except ValueError as exc:
        assert sys.argv[2]=='exception' and str(exc)=='exact immutable Result failed validation'
    else:
        assert sys.argv[2]!='exception' and result is None
assert len(calls)==1, 'one logical reduction invoked its compatibility reader more than once'
print('PASS: composed reducer uses its original compatibility reader once')
'''


class ResultCliImportTests(unittest.TestCase):
    def check(self, mode):
        root=Path(__file__).resolve().parents[1]
        env={key:value for key,value in os.environ.items()
             if key in {'PATH','LANG','LC_ALL','SYSTEMROOT','WINDIR','TZ'}}
        env['PYTHONDONTWRITEBYTECODE']='1'
        run=subprocess.run([sys.executable,'-I','-c',PROGRAM,str(root),mode],
                           cwd=root,env=env,capture_output=True,text=True,timeout=30)
        self.assertEqual(run.returncode,0,run.stdout+run.stderr)
        self.assertIn('PASS: composed reducer',run.stdout)

    def test_cli_then_package_import_reads_once(self):
        self.check('two_imports')

    def test_third_import_does_not_stack_another_facade(self):
        self.check('three_imports')

    def test_original_validation_exception_is_preserved(self):
        self.check('exception')


if __name__=='__main__':
    unittest.main()
