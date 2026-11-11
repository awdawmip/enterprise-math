"""Recompute the delivered numerical evidence and compare it to the stored results."""
from pathlib import Path
from tempfile import TemporaryDirectory
from zipfile import ZipFile
import json
import subprocess
import sys

ROOT = Path(__file__).resolve().parent

def call(script, *args):
    return subprocess.check_output([sys.executable, str(script), *map(str,args)], cwd=ROOT, text=True)

def compare(name, value):
    assert value == json.loads((ROOT/name).read_text()), name
    print('PASS',name,flush=True)

def verify():
    with TemporaryDirectory() as folder:
        directory = Path(folder)
        with ZipFile(ROOT/'prime_quantum_pointwise_minimum_c63.zip') as archive:
            for info in archive.infolist():
                if not (directory/info.filename).resolve().is_relative_to(directory):
                    raise ValueError('Invalid archive path')
            archive.extractall(directory)
        old = directory/'prime_quantum_pointwise_minimum_c63'
        gluing=json.loads(call(old/'global'/'check_gluing.py'))
        assert gluing['cut']==63 and gluing['small_cut_competitor_lower_over_U_floor']==14
        print('PASS C63 cut',flush=True)
        for script, evidence in [('top_schedules.py','top64.json'),('rank_four.py','rank_four.json'),
                                 ('check_three_states.py','three_state7.json'),
                                 ('rank_four_direct.py','rank_four_direct.json')]:
            output=directory/evidence
            call(ROOT/script, '--output', output)
            compare(evidence,json.loads(output.read_text()))
        compare('brc.json', json.loads(call(ROOT/'check_brc.py', old/'inherited'/'prime_quantum_schedule_extrema_c62.zip')))
        compare('ratio_evidence.json', json.loads(call(ROOT/'ratio_certificate.py')))
        compare('fourth_limit.json', json.loads(call(ROOT/'fourth_limit.py')))
        assert call(ROOT/'front_cost.py').strip()=='3380/1357'
        print('PASS initial double-5 limit',flush=True)

if __name__=='__main__':
    verify()
