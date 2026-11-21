"""Rebuild each new certificate using the bundled earlier observations and witnesses."""
import argparse
from concurrent.futures import ThreadPoolExecutor
import json
import os
from pathlib import Path
import subprocess
import sys

HERE = Path(__file__).resolve().parent

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--previous', type=Path, default=HERE/'previous')
    parser.add_argument('--parallel', type=int, default=2)
    parser.add_argument('--jobs', type=int, default=3, help='threads for each lower-bound or local exchange check')
    parser.add_argument('--only', nargs='+', help='run named sections only')
    args = parser.parse_args()
    last = args.previous.resolve()
    older, group, original = last/'previous', last/'group', last/'original'
    os.environ['NATIVE_PROBE_PREVIOUS'] = str(older)
    common = ['--older', older, '--group', group]
    tests = {
        'translation': ('translation/replay.py', 'translation/result.json', ['--last', last]),
        'native': ('translation/native.py', 'translation/native_result.json', ['--original',original]),
        'six': ('twelve_order6/replay.py', 'twelve_order6/result.json', [*common, '--original',original]),
        'rank3': ('eleven_rank3/replay.py', 'eleven_rank3/result.json', common),
        'eleven_six': ('eleven_six_counts/replay.py', 'eleven_six_counts/result.json', ['--previous',last]),
        'klein': ('eleven_klein/replay.py', 'eleven_klein/result.json', common),
        'reflection': ('eleven_reflection/replay.py', 'eleven_reflection/result.json', ['--older',older]),
        'three': ('eleven_order3/replay.py', 'eleven_order3/result.json', common),
        'four': ('eleven_order4/replay.py', 'eleven_order4/result.json', common),
        'other_four': ('eleven_other_order4/replay.py', 'eleven_other_order4/result.json', common),
        'twelve_four': ('twelve_order4/replay.py', 'twelve_order4/result.json', [*common, '--previous',last]),
        'stabilizers': ('stabilizers/replay.py', 'stabilizers/result.json', []),
        'retained': ('retained/replay.py', 'retained/result.json', ['--last',last,'--jobs',str(args.jobs)]),
        'lower': ('lower/replay.py', 'lower/result.json', ['--native',older,'--last',last,'--jobs',str(args.jobs)])
    }
    def test(name):
        program, receipt, options = tests[name]
        out = subprocess.check_output([sys.executable,'-B', HERE/program, *options], text=True)
        start = out.find('{') if name != 'lower' else out.rfind('\n{') + 1
        result = json.loads(out[start:])
        expected = json.loads((HERE/receipt).read_text())
        assert result == expected, name
        print(name, 'PASS', flush=True)
    with ThreadPoolExecutor(max_workers=args.parallel) as pool:
        list(pool.map(test, args.only or tests))
if __name__ == '__main__':
    main()
