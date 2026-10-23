"""Rebuild the direct PREFIX180 family and its complete optimum distribution.

No PREFIX179 archive is used. Requires Python 3.10+ and a C++17 compiler.
Large logs and compiler outputs stay in the explicitly new local run directory.
"""
import argparse
from pathlib import Path
import shutil
import subprocess
import sys


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--run-dir',type=Path,required=True)
    parser.add_argument('--compiler',default='g++')
    args=parser.parse_args()
    here=Path(__file__).resolve().parent
    original=here.parents[1]/'research_notes/handoffs/PREFIX180_20261022'
    run=args.run_dir.resolve()
    run.mkdir(parents=True,exist_ok=False)
    names=['generate_180.py','independent_support_obstruction_180.py','exact_180.cpp',
           'exact_all_180.cpp','independent_180.cpp','independent_k12_180.cpp',
           'SHA256SUMS_PREFIX180.txt']
    for name in names:
        shutil.copyfile(original/name,run/name)
    shutil.copyfile(here/'independent_budget.cpp',run/'independent_budget.cpp')

    def execute(argv,output):
        print('RUN', ' '.join(map(str,argv)),flush=True)
        with (run/output).open('w') as stream:
            subprocess.run(list(map(str,argv)),cwd=run,stdout=stream,check=True)

    execute([sys.executable,'generate_180.py'],'generation.txt')
    execute([sys.executable,'independent_support_obstruction_180.py'],'support_filter.txt')
    for source,binary in [('exact_180.cpp','solve11'),('exact_all_180.cpp','solve_budget'),
                          ('independent_180.cpp','independent11'),
                          ('independent_k12_180.cpp','independent12'),
                          ('independent_budget.cpp','independent_budget')]:
        subprocess.run([args.compiler,'-std=c++17','-O3',source,'-o',binary],cwd=run,check=True)
    execute([run/'solve11','distance3_remove1264_180.bin',67525,11,200000],'primary_180.log')
    execute([run/'independent11','distance3_remove1264_180.bin'],'fresh_second_180.log')
    execute([run/'solve_budget','eligible_no_support_obstruction_180.bin',646,12,200000],
            'eligible_k12_results_180.log')
    execute([run/'independent12','eligible_no_support_obstruction_180.bin'],'fresh_independent_k12_180.log')
    execute([run/'solve_budget','eligible_no_support_obstruction_180.bin',646,13,200000],
            'fresh_k13_results.log')
    execute([run/'independent_budget','eligible_no_support_obstruction_180.bin',13],
            'fresh_independent_k13.log')
    execute([run/'solve_budget','eligible_no_support_obstruction_180.bin',646,14,200000],
            'fresh_k14_results.log')
    for fresh,old in [('fresh_second_180.log','second_180.log'),
                      ('fresh_independent_k12_180.log','independent_k12_180.log')]:
        if (run/fresh).read_bytes()!=(original/old).read_bytes():
            raise ValueError('replay differs from historical '+old)
    execute([sys.executable,here/'verify_census.py','--run-dir',run,
             '--output',run/'OPTIMUM_CERTIFICATE.json'],'audit.json')
    print('COMPLETE_OPTIMUM_CERTIFICATE',run/'OPTIMUM_CERTIFICATE.json',flush=True)


if __name__=='__main__':
    main()
