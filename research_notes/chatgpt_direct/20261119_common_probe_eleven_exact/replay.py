"""Run a proof group and compare its entire JSON receipt with the archived result."""
import argparse
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CASES = {
    'eleven': ('eleven', 'replay', 'result'),
    'native': ('native', 'replay', 'result'),
    'ties': ('eleven', 'tie', 'tie_result'),
    'neighbors': ('eleven_neighbors', 'replay', 'result'),
    'four_cores': ('twelve_lower', 'replay', 'four_core_result'),
    'landscape': ('eleven_landscape', 'replay', 'result'),
    'twelve_lower': ('twelve_lower', 'replay', 'result'),
    'cores': ('twelve_cores', 'replay', 'result'),
    'distance': ('twelve_distance', 'replay', 'result'),
    'migration': ('migration', 'replay', 'result'),
    'nesting': ('nesting', 'replay', 'result'),
    'frozen': ('frozen', 'replay', 'result'),
    'adjacent': ('adjacent', 'replay', 'result'),
    'four': ('four', 'replay', 'result'),
    'overlap': ('overlap', 'replay', 'result'),
    'history': ('overlap', 'history', 'history_result'),
}
if (ROOT/'bias/replay.py').is_file():
    CASES['bias'] = ('bias', 'replay', 'result')
if (ROOT/'eleven/gap.py').is_file():
    CASES['gap'] = ('eleven', 'gap', 'gap_result')

def main():
    args = argparse.ArgumentParser(description=__doc__)
    args.add_argument('--only', nargs='+', choices=CASES)
    args.add_argument('--previous', type=Path, default=ROOT/'previous')
    args.add_argument('--jobs', type=int, default=3)
    selected = args.parse_args()
    if selected.jobs < 1:
        args.error('--jobs must be a positive integer')
    for name in selected.only or CASES:
        directory, script, receipt = CASES[name]
        folder = ROOT/directory
        cmd = [sys.executable, '-B', str(folder/(script+'.py')), '--previous', str(selected.previous.resolve())]
        if name in {'eleven', 'ties', 'gap', 'twelve_lower', 'cores', 'four', 'overlap', 'neighbors', 'four_cores'}:
            cmd.extend(['--jobs', str(selected.jobs)])
        if name=='four_cores':
            cmd.append('--four-cores')
        actual = json.loads(subprocess.check_output(cmd, text=True))
        expected = json.loads((folder/(receipt+'.json')).read_text())
        if actual != expected:
            raise ValueError(f'{name}: receipt differs')
        print(f'{name}: verified', flush=True)

if __name__ == '__main__':
    main()
