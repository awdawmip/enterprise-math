"""Capture reproducible commands, source hashes, and observed result metadata."""
from datetime import datetime, timezone
from hashlib import sha256
import json
from pathlib import Path
import platform
import subprocess
import sys

from prepare_family import DIRECTORY, ROOT, M, L, PRIMES


def main():
    relative = DIRECTORY.relative_to(ROOT).as_posix()
    names = [
        'prepare_family.py', 'minimize_family.cpp', 'check_kernel.py',
        'verify_family_results.py', 'make_manifest.py', 'proof.md',
        'family_input.json', 'kernel_checks.json', 'minimum_M.json',
        'minimum_3M.json', 'verification.json',
        'new_table_unrestricted.json', 'new_table_divisible3.json',
    ]
    base = f'{relative}/'
    compiled = base+'minimize_family'
    commands = [
        ['python',base+'prepare_family.py'],
        ['g++','-O3','-std=c++17','-Wall','-Wextra',base+'minimize_family.cpp','-o',compiled],
        ['python',base+'check_kernel.py'],
        [compiled,base+'family_M.bin','240'],
        [compiled,base+'family_3M.bin','240'],
        ['python',base+'verify_family_results.py','--source-dir','vendor_src'],
    ]
    inp = json.loads((DIRECTORY/'family_input.json').read_text())
    evidence = []
    for name, factor in [('minimum_M.json',1),('minimum_3M.json',3)]:
        result = json.loads((DIRECTORY/name).read_text())
        count = result['left_count']*result['right_count']*result['shift_count']
        assert count == inp['odd_root_classes_per_branch']
        assert int(result['modulus']) == factor*M
        evidence.append({'output':name,'odd_crt_modulus':str(2*factor*M),
                         'minimum':result['minimum'],'seconds_observed':result['seconds'],
                         'root_classes_count_from_list_product':count})
    report = {
        'schema':'RIESEL_V4_COMPUTATION_MANIFEST_V1',
        'recorded_utc':datetime.now(timezone.utc).isoformat(),
        'researcher_id':'EM-DIRECT-970E1C',
        'research_activity_id':'RA-D2EC212845B63844081F9A14',
        'commands_in_workspace_root':commands,
        'stdout_redirection':{3:base+'minimum_M.json',4:base+'minimum_3M.json'},
        'python_version':sys.version,'byteorder':sys.byteorder,
        'platform':platform.platform(),
        'compiler':subprocess.check_output(['g++','--version'],text=True).splitlines()[0],
        'files_sha256':{name:sha256((DIRECTORY/name).read_bytes()).hexdigest() for name in names},
        'input_binary_sha256':{name:sha256((DIRECTORY/name).read_bytes()).hexdigest()
                               for name in ['family_M.bin','family_3M.bin']},
        'input_binary_policy':'Reproducible intermediates; not required as permanent proof files.',
        'class_count_basis':{'shape_vector_count':inp['distinct_translated_phase_vectors'],
                             'sign_count':2**len(PRIMES),
                             'L':L,'per_branch_count':inp['odd_root_classes_per_branch']},
        'results':evidence,
        'scope':'Complete explicitly defined F plus all translations and square-root signs, independently in each odd CRT modulus. Not all fixed-P covers.',
        'review_status':'Author computation and verification; no independent project Review asserted.'
    }
    (DIRECTORY/'computation_manifest.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({'manifest':str(DIRECTORY/'computation_manifest.json'),'root_classes_per_branch':inp['odd_root_classes_per_branch'],'files_hashed':len(names)}))


if __name__ == '__main__':
    main()
