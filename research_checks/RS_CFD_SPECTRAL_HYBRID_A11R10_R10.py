#!/usr/bin/env python3
"""Fail-closed checker for the R10 bounded surrogate trajectory checkpoint."""
from __future__ import annotations
import json, sys
from pathlib import Path

def main(path: str) -> int:
    d=json.loads(Path(path).read_text())
    assert d['status']=='SURROGATE_3D_FULL_TRAJECTORY_CHECKPOINT_NOT_SPECTRALDNS_NATIVE_HOST'
    assert d['frozen']=={
        'n':16,'cutoff':4,'precision':'complex128/float64','fft_norm':'forward','fft_workers':1,
        'viscosity':0.01,'dt':0.0005,'steps':5,'source':'zero',
        'dealiasing':'retained cube |k_i|<=4; N>3K','integrator':'classical fixed-step RK4'}
    assert d['calibrated_sparse_threshold_full_modes']==256
    assert len(d['calibration'])==6
    assert max(r['rhs_relative_max_error'] for r in d['calibration']) < 2e-11
    assert len(d['cases'])==3
    expected={(91001,16):(2,18),(91003,32):(2,18),(91007,64):(1,19)}
    for c in d['cases']:
        assert c['final_relative_max_state'] < 2e-11
        assert c['final_energy_relative_error'] < 1e-15
        assert len(c['hybrid_calls']) == 20
        assert sum(c['route_counts'].values()) == 20
        exp=expected[(c['seed'],c['initial_full_modes'])]
        assert (c['route_counts']['SPARSE'],c['route_counts']['FFT_FALLBACK']) == exp
        assert max(r['dense_divergence_max'] for r in c['step_rows']) < 1e-12
        assert max(r['hybrid_divergence_max'] for r in c['step_rows']) < 1e-12
        assert all(r['dense_full_support']==r['hybrid_full_support'] for r in c['step_rows'])
        assert c['step_rows'][-1]['dense_full_support']==729
        assert c['step_rows'][-1]['hybrid_full_support']==729
    print('R10 checkpoint verification: PASS')
    return 0

if __name__=='__main__':
    raise SystemExit(main(sys.argv[1]))
