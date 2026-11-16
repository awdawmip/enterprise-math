"""Replay C75's finite evidence and compare each recorded output exactly."""
from pathlib import Path
import hashlib
import subprocess
import sys


def main():
    here = Path(__file__).resolve().parent
    for line in (here / 'SHA256SUMS').read_text().splitlines():
        expected, name = line.split('  ', 1)
        if hashlib.sha256((here / name).read_bytes()).hexdigest() != expected:
            raise ValueError('File digest mismatch: ' + name)
    pairs = [
        ('near_sync_controls.py', 'near_sync_controls.json'),
        ('check_calibration.py', 'calibration.json'),
        ('check_preparations.py', 'preparations.json'),
        ('preparation_collision.py', 'preparation_collision.json'),
        ('check_pointwise.py', 'pointwise_controls.json'),
        ('check_macro.py', 'macro_controls.json'),
        ('check_tied.py', 'tied_controls.json'),
        ('check_finite.py', 'finite_control.txt'),
    ]
    for script, output in pairs:
        actual = subprocess.check_output([sys.executable, str(here / script)], cwd=here)
        if actual != (here / output).read_bytes():
            raise ValueError('Output mismatch: ' + output)
        print('Verified', output, flush=True)


if __name__ == '__main__':
    main()
