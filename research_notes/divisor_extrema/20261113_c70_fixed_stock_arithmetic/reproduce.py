"""Run every C70 finite certificate and compare its output byte for byte."""
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parent


def section(number, folder):
    for name in (f'C{number}', f'c{number}'):
        path = ROOT.parent / name / folder
        if path.is_dir():
            return str(path)
    raise FileNotFoundError(f'C{number}/{folder}')


def main():
    prior = section(67,'joint')
    arithmetic = section(69,'arithmetic')
    jobs = [
        ('one/verify_one.py', ['--prior', prior], 'one/one.json'),
        ('one/raw_rank.py', ['--prior', prior], 'one/raw_rank.json'),
        ('two/eventual_two.py', ['--prior', prior], 'two/eventual_two.json'),
        ('deep/eighth_rank.py', ['--prior', arithmetic], 'deep/eighth_rank.json'),
        ('order/sparse_stocks.py', [], 'order/sparse_stocks.json'),
    ]
    def run(job):
        code, switches, golden = job
        completed = subprocess.run([sys.executable,str(ROOT / code),*switches],check=True,capture_output=True)
        if completed.stdout != (ROOT / golden).read_bytes():
            raise ValueError(f'Certificate differs: {golden}')
        print('OK', golden,flush=True)
    with ThreadPoolExecutor(max_workers=3) as workers:
        list(workers.map(run,jobs))


if __name__ == '__main__':
    main()
