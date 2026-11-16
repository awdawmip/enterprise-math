"""Check the package manifest and replay the linked arithmetic certificates."""
from pathlib import Path
import hashlib
import subprocess
import sys


def main():
    here = Path(__file__).resolve().parent
    for line in (here / 'SHA256SUMS').read_text().splitlines():
        digest, name = line.split('  ',1)
        if hashlib.sha256((here/name).read_bytes()).hexdigest() != digest:
            raise ValueError('Manifest mismatch in '+name)
    checks = [
        ('check_adjacent','adjacent_controls.json'),
        ('check_center_line','center_line.json'),
        ('check_center_shape','center_shape.json'),
        ('check_tail_invariants','tail_invariants.json'),
        ('check_edge_slope','edge_slope.json'),
        ('check_macro_point','macro_point.json'),
        ('check_macro_rectangle','macro_rectangle.json'),
        ('check_macro_alias','macro_alias.json'),
        ('check_grid_drift','grid_drift.json'),
        ('ray_certificate','ray_coefficients.json'),
        ('check_dyadic','dyadic_controls.json'),
        ('check_polynomial_rays','polynomial_controls.json'),
        ('check_center_anchor','center_anchor.json'),
        ('check_finite','finite_control.txt'),
    ]
    for program, record in checks:
        output=subprocess.check_output([sys.executable,str(here/(program+'.py'))],cwd=here)
        if output!=(here/record).read_bytes():
            raise ValueError('Replay differs from '+record)
        print('Verified',record,flush=True)


if __name__=='__main__':
    main()
