"""Local exact tests; independent symbolic oracle optional, no hosted execution."""
from __future__ import annotations
from fractions import Fraction as F
from dataclasses import replace
from pathlib import Path
import hashlib
import itertools
import json
import random
import sys
import unittest
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT/'src'))
from enterprise_math import heartbeat_newton_spectrum as n
from enterprise_math import heartbeat_residual_holonomy as h
from enterprise_math.brc_transport import Affine, EffectHistogram, eye, mm, inv
from enterprise_math.brc_histogram import WeightHistogram

REPORT = {}

def block_diag(blocks):
    d = sum(map(len, blocks)); a = [[0]*d for _ in range(d)]; offset = 0
    for block in blocks:
        for i, row in enumerate(block):
            for j, value in enumerate(row): a[offset+i][offset+j] = value
        offset += len(block)
    return tuple(tuple(row) for row in a)

def companion(coeff):
    d = len(coeff)-1; a = [[0]*d for _ in range(d)]
    for i in range(1,d): a[i][i-1] = 1
    for i in range(d): a[i][-1] = -coeff[d-i]
    return tuple(tuple(row) for row in a)

def conjugate(a, seed):
    rng = random.Random(seed); d = len(a); u = h.identity(d)
    for _ in range(8):
        i,j = rng.sample(range(d),2); e = [list(row) for row in h.identity(d)]
        e[i][j] = rng.choice((-2,-1,1,2)); u = h.matmul(tuple(map(tuple,e)),u)
    ui = tuple(tuple(int(v) for v in row) for row in inv(n.qmatrix(u)))
    assert h.matmul(u,ui) == h.identity(d)
    return h.matmul(h.matmul(u,a),ui)

B = ((0,-2),(1,2)); D = ((0,-2),(1,1))
BAL = block_diag((B,B,B)); DRIFT = block_diag((D,D,D))

class NewtonHeartbeatTests(unittest.TestCase):
    def test_01_source_pins(self):
        pins = {'heartbeat_residual_holonomy.py':'2b66743c3f4cd52263aa6e15c00d7837008fb8ad',
                'brc_transport.py':'be1debe367263931bd5e93fd750be3ed54624fe1',
                'brc_histogram.py':'9a3962ec095095f14e63a91cfe6b7ebf07d9a1d1'}
        for file, expected in pins.items():
            b=(ROOT/'src/enterprise_math'/file).read_bytes()
            self.assertEqual(hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest(),expected)
        REPORT['executed_unchanged_sources']=pins

    def test_02_independent_characteristic_and_smith(self):
        try:
            import sympy as sp
            from sympy.matrices.normalforms import smith_normal_form
            from sympy.polys.domains import ZZ
        except ImportError:
            self.skipTest('Optional independent oracle requires sympy==1.14.0')
        rng=random.Random(920261)
        for _ in range(36):
            while True:
                a=tuple(tuple(rng.randint(-3,3) for _ in range(6)) for __ in range(6))
                if h.determinant(a): break
            oracle=sp.Matrix(a)
            self.assertEqual(n.characteristic_coefficients(a),tuple(F(int(v)) for v in oracle.charpoly().all_coeffs()))
            self.assertEqual(h.determinant(a),int(oracle.det()))
            self.assertEqual(h.smith_invariant_factors(a),tuple(abs(int(v)) for v in smith_normal_form(oracle,domain=ZZ).diagonal()))
        REPORT['independent_oracle']={'sympy':sp.__version__,'dense_6x6_matrices':36}

    def test_03_monomial_reduction(self):
        rng=random.Random(920262); checks=0
        for _ in range(40):
            perm=list(range(6));rng.shuffle(perm); a=[[0]*6 for _ in range(6)]
            for j,i in enumerate(perm):a[i][j]=rng.choice((-12,-6,-2,1,3,5,8))
            a=tuple(map(tuple,a))
            for p in (2,3,5):
                spec=n.NewtonSpectrum.from_matrix(a,p)
                expected=[]
                for cyc,v,d in h.monomial_cycle_valuation_data(a,p): expected.extend([F(v,d)]*d)
                self.assertEqual(spec.slopes,tuple(sorted(expected)))
                self.assertEqual(spec.balanced,h.monomial_valuation_balance(a,p));checks+=1
        REPORT['old_monomial_rule_recovered']=checks

    def test_04_same_volume_mixing_pair(self):
        self.assertEqual(h.determinant(BAL),8);self.assertEqual(h.determinant(DRIFT),8)
        self.assertEqual(n.NewtonSpectrum.from_matrix(BAL,2).slopes,(F(1,2),)*6)
        self.assertEqual(n.NewtonSpectrum.from_matrix(DRIFT,2).slopes,(F(0),)*3+(F(1),)*3)
        certificate=n.certify_balanced_powers(BAL,2)
        self.assertEqual(certificate.spread_bound,1)
        dense_bal,dense_drift=conjugate(BAL,1),conjugate(DRIFT,1)
        for k in range(1,25):
            b=n.local_smith_depths(BAL,2,k);d=n.local_smith_depths(DRIFT,2,k)
            self.assertEqual(b,(k//2,)*3+((k+1)//2,)*3)
            self.assertEqual(d,(0,)*3+(k,)*3)
            self.assertEqual(n.local_smith_depths(dense_bal,2,k),b)
            self.assertEqual(n.local_smith_depths(dense_drift,2,k),d)
        REPORT['mixing_pair']={'determinants':[8,8],'powers_per_map':24,'maps':4,
            'balanced_slope':'1/2 (six times)','drift_slopes':['0','0','0','1','1','1'],
            'balanced_spread_bound':str(certificate.spread_bound),'drift_spread':'n',
            'dense_conjugate_maps': [dense_bal,dense_drift]}

    def test_05_general_single_slope_bounds(self):
        rng=random.Random(920263); checks=0; certs=[]
        for idx in range(18):
            p=(2,3,5)[idx%3]
            coeff=[1]+[p*rng.randint(-4,4) for _ in range(5)]+[p*rng.choice((1,p+1,2*p+1))]
            a=conjugate(companion(coeff),100+idx)
            cert=n.certify_balanced_powers(a,p);cert.recheck(a)
            self.assertEqual(cert.slope,F(1,6))
            for k in range(19):
                depths=n.local_smith_depths(a,p,k); lo,hi=cert.interval(k)
                self.assertTrue(all(lo<=x<=hi for x in depths))
                self.assertLessEqual(depths[-1]-depths[0],cert.spread_bound); checks+=1
            certs.append(str(cert.spread_bound))
            # This is evaluation of a proved bound, not simulation of 10^12 cycles.
            self.assertEqual(cert.interval(10**12)[1]-cert.interval(10**12)[0],
                             cert.lower_offsets[(10**12)%6]+cert.upper_offsets[(10**12)%6])
        REPORT['all_n_bound_certificates']={'dense_eisenstein_maps':18,'finite_power_crosschecks':checks,
            'proved_bounds':certs,'huge_index_bound_only':10**12}

    def test_06_obstructions_and_polygons(self):
        rng=random.Random(920264); checked=balanced=0
        for _ in range(32):
            while True:
                a=tuple(tuple(rng.randint(-5,5) for _ in range(6)) for __ in range(6))
                if h.determinant(a):break
            for p in (2,3,5):
                s=n.NewtonSpectrum.from_matrix(a,p)
                self.assertEqual(s.balanced,s.coefficient_obstruction() is None)
                self.assertEqual(sum(s.slopes),h.prime_valuation(h.determinant(a),p))
                if s.balanced:
                    cert=n.certify_balanced_powers(a,p);cert.recheck(a);balanced+=1
                else:
                    with self.assertRaises(ValueError):n.certify_balanced_powers(a,p)
                # Hodge polygon lies below Newton polygon, independently per power.
                for k in (1,3):
                    depths=n.local_smith_depths(a,p,k)
                    for r in range(1,7):self.assertLessEqual(sum(depths[:r]),k*sum(s.slopes[:r]))
                checked+=1
        REPORT['general_coefficient_tests']={'matrix_prime_cases':checked,'balanced':balanced}

    def test_07_general_phase_invariance(self):
        rng=random.Random(920265);checked=0
        for _ in range(18):
            steps=[]
            for _t in range(3):
                while True:
                    a=tuple(tuple(rng.randint(-2,2) for _ in range(6)) for __ in range(6))
                    if h.determinant(a):break
                steps.append(a)
            for p in (2,3,5):
                spectra=n.periodic_newton_spectra(steps,p)
                self.assertEqual(len({s.slopes for s in spectra}),1);checked+=1
        REPORT['general_mixing_phase_checks']={'programs':18,'phases':3,'prime_cases':checked}

    def test_08_exact_eight_beat_shear_rhythm(self):
        a=[[8*int(i==j) for j in range(6)] for i in range(6)];a[0][1]=1;a=tuple(map(tuple,a))
        cert=n.find_smith_rhythm(a,2,max_trials=8)
        self.assertEqual((cert.period,cert.depth_increment),(8,24));cert.recheck(a)
        self.assertIsNone(n.find_smith_rhythm(a,2,max_trials=7))
        seq=[]
        for k in range(33):
            depths=n.local_smith_depths(a,2,k)
            if k: gap=max(0,3-h.prime_valuation(k,2)); expected=(3*k-gap,)+(3*k,)*4+(3*k+gap,)
            else:expected=(0,)*6
            self.assertEqual(depths,expected)
            self.assertEqual(n.local_smith_depths(a,2,k+8),tuple(x+24 for x in depths))
            if k<=8:seq.append(depths)
        REPORT['exact_smith_rhythm']={'period':8,'depth_increment':24,'recurrence_checks':33,
            'early_search_exhaustion_is_not_nonexistence':True,'first_nine_profiles':seq}

    def test_09_rhythm_and_bound_nonsemisimple(self):
        maps=[BAL,h.cyclic_radix_heartbeat(2),companion((1,0,0,0,0,2,2))]
        for s in (1,2,3):
            a=[[2**s*int(i==j) for j in range(6)] for i in range(6)];a[0][1]=1;maps.append(tuple(map(tuple,a)))
        result=[]
        for a in maps:
            cert=n.find_smith_rhythm(a,2,max_trials=64);self.assertIsNotNone(cert);cert.recheck(a)
            bound=n.certify_balanced_powers(a,2)
            for k in range(13):
                left=n.local_smith_depths(a,2,k);right=n.local_smith_depths(a,2,k+cert.period)
                self.assertEqual(right,tuple(v+cert.depth_increment for v in left))
                lo,hi=bound.interval(k);self.assertTrue(all(lo<=v<=hi for v in left))
            result.append([cert.period,cert.depth_increment])
        REPORT['additional_exact_rhythms']={'maps':len(maps),'period_increment_pairs':result,'recurrence_checks':len(maps)*13}

    def test_10_brc_torsion_capacity(self):
        b=h.smith_invariant_factors(h.matpow(BAL,20)); d=h.smith_invariant_factors(h.matpow(DRIFT,20))
        nb=h.torsion_killed_count(b,2**10);nd=h.torsion_killed_count(d,2**10)
        self.assertEqual((nb,nd),(2**60,2**30))
        count=8**20
        wb=WeightHistogram.from_counts({F(1,count):nb});wd=WeightHistogram.from_counts({F(1,count):nd})
        self.assertEqual((wb.total_mass,wd.total_mass),(1,F(1,2**30)))
        sb=n.NewtonSpectrum.from_matrix(BAL,2);sd=n.NewtonSpectrum.from_matrix(DRIFT,2)
        self.assertEqual(n.torsion_capacity_rate(sb,F(1,2)),3)
        self.assertEqual(n.torsion_capacity_rate(sd,F(1,2)),F(3,2))
        REPORT['brc_capacity']={'uniform_weight_assumed':True,'n':20,'multiplier':2**10,
            'equal_total_branches':count,'surviving_torsion_counts':[nb,nd],
            'selected_mass':[str(wb.total_mass),str(wd.total_mass)]}

    def test_11_smith_and_real_metric_are_distinct(self):
        scale=tuple(tuple(2*int(i==j) for j in range(6)) for i in range(6))
        shear=[list(r) for r in scale];shear[0][1]=2;shear=tuple(map(tuple,shear))
        self.assertEqual(n.NewtonSpectrum.from_matrix(scale,2),n.NewtonSpectrum.from_matrix(shear,2))
        e2=(0,1,0,0,0,0)
        for k in (1,2,5,20):
            self.assertEqual(n.local_smith_depths(scale,2,k),n.local_smith_depths(shear,2,k))
            a=h.matpow(scale,k);b=h.matpow(shear,k)
            pa=EffectHistogram.from_terms(6,[(1,Affine(a,(0,)*6),1)])
            pb=EffectHistogram.from_terms(6,[(1,Affine(b,(0,)*6),1)])
            self.assertNotEqual(pa.evaluate(e2),pb.evaluate(e2))
            self.assertEqual(pa.forget_effects(),pb.forget_effects())
            y=Affine(b,(0,)*6).apply(e2)
            self.assertEqual(sum(v*v for v in y),4**k*(k*k+1))
        REPORT['observer_boundary']={'identical_newton_spectrum':True,'identical_all_n_smith_factors_proved':True,
            'BRC_endpoint_effects_differ':True,'sheared_length_squared':'4^n*(n^2+1)'}

    def test_12_invalid_and_forged(self):
        bad=[lambda:n.NewtonSpectrum.from_matrix(((1,1),(1,1)),2),
             lambda:n.NewtonSpectrum.from_matrix(((1.0,),),2),
             lambda:n.NewtonSpectrum.from_matrix(((True,),),2),
             lambda:n.NewtonSpectrum.from_matrix(((1,),),4),
             lambda:n.newton_polygon((1,0),2),lambda:n.valuation(1.0,2),
             lambda:n.find_smith_rhythm(BAL,2,max_trials=0),
             lambda:n.find_smith_rhythm(DRIFT,2),lambda:n.local_smith_depths(BAL,2,-1),
             lambda:n.periodic_newton_spectra([],2),lambda:n.valuation(F(1),True),
             lambda:n.NewtonSpectrum.from_matrix(h.identity(7),2)]
        for f in bad:
            with self.assertRaises((ValueError,TypeError)):f()
        cert=n.certify_balanced_powers(BAL,2)
        with self.assertRaises(ValueError):replace(cert,source_digest='x').recheck(BAL)
        rhythm=n.find_smith_rhythm(BAL,2)
        with self.assertRaises(ValueError):replace(rhythm,depth_increment=99).recheck(BAL)
        REPORT['guard_rejections']=len(bad)+2

if __name__=='__main__':
    result=unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(NewtonHeartbeatTests))
    out={'status':'PASS' if result.wasSuccessful() else 'FAIL','test_groups':result.testsRun,
         'skipped':len(result.skipped),'failures':len(result.failures),'errors':len(result.errors),
         'checks':REPORT,'independent_mathematical_review':False,'full_repository_tests':False,
         'production_changed':False}
    folder=ROOT/'research_notes/heartbeat_newton_spectrum_20260920_AD0416';folder.mkdir(parents=True,exist_ok=True)
    (folder/'RESULTS.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
    raise SystemExit(not result.wasSuccessful())
