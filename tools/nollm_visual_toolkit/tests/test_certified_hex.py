"""Slice-03 tests. Fraction/mpmath/float are independent test observers only."""
from __future__ import annotations
from copy import deepcopy
from fractions import Fraction
from itertools import product
import importlib.util
import json
import math
from pathlib import Path
import random
import subprocess
import sys
import unittest
from unittest.mock import patch

from nollm_visual_toolkit import multiplication_lab as lab
from nollm_visual_toolkit.certified_hex import (DyadicInterval, PolarSource,
    phase_bounds, root_ratio_bound, round_axial, certify_box, certified_population,
    verify_cell_record)


def fraction_round(q, r):
    source = [q, r, -q-r]
    a, b, c = [math.floor(v + Fraction(1, 2)) for v in source]
    da, db, dc = [abs(x-y) for x, y in zip((a,b,c), source)]
    if da >= db and da >= dc:
        a = -b-c
    elif db >= dc:
        b = -a-c
    return a, b


class CertifiedHexTests(unittest.TestCase):
    def test_signed_half_up_and_all_axis_ties(self):
        cases = 0
        for d in range(1, 13):
            for q, r in product(range(-12,13), repeat=2):
                result = round_axial(q, r, d)
                cell = tuple(map(int, result['cube_cell'][:2]))
                self.assertEqual(cell, fraction_round(Fraction(q,d), Fraction(r,d)))
                a,b=cell
                dist=(q-a*d)**2+(q-a*d)*(r-b*d)+(r-b*d)**2
                # A separate finite closest-lattice-point oracle around the cell.
                for aa,bb in product(range(a-2,a+3), range(b-2,b+3)):
                    other=(q-aa*d)**2+(q-aa*d)*(r-bb*d)+(r-bb*d)**2
                    self.assertLessEqual(dist,other)
                residuals=list(map(int,result['signed_residual_numerators']))
                self.assertEqual(sum(residuals),0)
                self.assertEqual([q,r,-q-r],[d*int(x)+y for x,y in zip(result['cube_cell'],residuals)])
                cases+=1
        self.assertEqual(cases,7500)

    def test_large_integer_translation_and_unreduced_source(self):
        large=2**100+7
        for q,r,d in ((1,1,3),(-1,0,2),(2,4,6)):
            first=round_axial(q,r,d)
            shifted=round_axial(q+large*d,r-large*d,d)
            self.assertEqual([int(v) for v in shifted['cube_cell']],
                             [int(first['cube_cell'][0])+large,int(first['cube_cell'][1])-large,int(first['cube_cell'][2])])
        first=round_axial(1,2,3);second=round_axial(2,4,6)
        self.assertEqual(first['cube_cell'],second['cube_cell'])
        self.assertNotEqual(first,second)

    def test_interval_arithmetic_outward_against_fraction(self):
        intervals=[DyadicInterval(a,b,8) for a in range(-4,5) for b in range(a,5)]
        for a,b in product(intervals, repeat=2):
            c=a*b
            values=[Fraction(x*y,256**2) for x,y in product((a.lo,a.hi),(b.lo,b.hi))]
            self.assertLessEqual(Fraction(c.lo,256),min(values))
            self.assertGreaterEqual(Fraction(c.hi,256),max(values))
            self.assertLess(min(values)-Fraction(c.lo,256),Fraction(1,256))
            self.assertLess(Fraction(c.hi,256)-max(values),Fraction(1,256))

    def test_root_ratio_certificates(self):
        cases=0
        for n in range(65):
            for d in (1,2,3,7,16):
                for bits in (8,17,64):
                    interval,t=root_ratio_bound(n,d,bits)
                    k=int(t['root_index']);s=1<<bits;rem=int(t['polynomial_residual'])
                    self.assertEqual(n*s*s,d*k*k+rem)
                    self.assertTrue(0<=rem<d*(2*k+1))
                    self.assertLessEqual(d*interval.lo**2,n*s*s)
                    self.assertGreaterEqual(d*interval.hi**2,n*s*s)
                    cases+=1
        self.assertEqual(cases,975)

    def test_half_angles_all_quadrants_high_precision_oracle(self):
        import mpmath as mp
        ticks=sorted(set(range(0,65536,31))|{0,1,8191,8192,16383,16384,32767,32768,49151,49152,65535})
        with mp.workdps(100):
            for tick in ticks:
                c,s=phase_bounds(tick,64)
                if tick%16384==0:
                    co,si=((1,0),(0,1),(-1,0),(0,-1))[tick//16384]
                else:
                    angle=2*mp.pi*tick/65536;co,si=mp.cos(angle),mp.sin(angle)
                for interval,value in ((c,co),(s,si)):
                    self.assertLessEqual(mp.mpf(interval.lo)/(1<<64),value)
                    self.assertGreaterEqual(mp.mpf(interval.hi)/(1<<64),value)
        self.assertGreater(len(ticks),2100)

    def test_polar_bounds_high_precision_oracle(self):
        import mpmath as mp
        rng=random.Random(20260920)
        with mp.workdps(100):
            for _ in range(512):
                n=rng.randrange(1,65536);tick=rng.randrange(1,65536)
                sn,sd=rng.choice(((1,2),(1,1),(3,2),(2,3),(3,1)))
                source=PolarSource(n,tick,sn,sd);coords,_=source.coordinates(64)
                angle=2*mp.pi*tick/65536
                x=mp.mpf(sn)/sd*mp.sqrt(n)*mp.cos(angle)
                h=mp.mpf(sn)/sd*mp.sqrt(mp.mpf(n)/3)*mp.sin(angle)
                for interval,value in zip(coords,(x-h,2*h,-x-h)):
                    self.assertLessEqual(mp.mpf(interval.lo)/(1<<64),value)
                    self.assertGreaterEqual(mp.mpf(interval.hi)/(1<<64),value)

    def test_true_boundaries_keep_declared_rule(self):
        cases=[(1,0,1,2,(0,0)),(1,32768,3,2,(-2,0)),
               (3,16384,1,2,(-1,1)),(3,16384,3,2,(-2,3))]
        for n,t,sn,sd,cell in cases:
            result=PolarSource(n,t,sn,sd).locate()
            self.assertEqual(result['status'],'CERTIFIED_TIE')
            self.assertEqual(tuple(map(int,result['cell'])),cell)
            self.assertTrue(verify_cell_record(result))

    def test_shared_irrational_cardinal_ties_are_not_interval_noise(self):
        cases=[(811,16384,1,1,(-17,33)),(811,16384,3,2,(-24,49)),
               (2927,49152,1,2,(15,-31))]
        for n,t,sn,sd,cell in cases:
            result=PolarSource(n,t,sn,sd).locate(initial_bits=8,max_bits=8)
            self.assertEqual(result['status'],'CERTIFIED_TIE')
            self.assertEqual(tuple(map(int,result['cell'])),cell)
            self.assertEqual(result['rounding_certificate']['kind'],'SHARED_RADICAL_AXIAL_CELL_CERTIFICATE')
            self.assertTrue(verify_cell_record(result))

    def test_cardinal_radical_rounding_against_independent_oracle(self):
        import mpmath as mp
        directions={0:(1,0,-1),16384:(-1,2,-1),32768:(-1,0,1),49152:(1,-2,1)}
        cases=0
        with mp.workdps(100):
            for n,tick,scale in product(range(1,129),directions,((1,2),(1,1),(3,2),(2,3))):
                sn,sd=scale;d=3 if tick in (16384,49152) else 1
                ratio=Fraction(n*sn*sn,d*sd*sd)
                nr,dr=math.isqrt(ratio.numerator),math.isqrt(ratio.denominator)
                rational=(nr*nr==ratio.numerator and dr*dr==ratio.denominator)
                root=Fraction(nr,dr) if rational else mp.sqrt(mp.mpf(n)*sn*sn/(d*sd*sd))
                xyz=[k*root for k in directions[tick]]
                # A high-precision decimal oracle cannot decide exact corner ties.
                half=Fraction(1,2) if rational else mp.mpf('0.5')
                rounded=[math.floor(v+half) for v in xyz]
                errors=[abs(a-v) for a,v in zip(rounded,xyz)]
                axis=max(range(3),key=lambda i:errors[i])
                rounded[axis]=-sum(rounded[i] for i in range(3) if i!=axis)
                result=PolarSource(n,tick,sn,sd).locate()
                self.assertEqual(list(map(int,result['cell'])),rounded[:2],(n,tick,scale))
                cases+=1
        self.assertEqual(cases,2048)

    def test_near_boundary_and_negative_coordinates_not_epsilon_merged(self):
        d=10**90
        for q,expected in ((d-1,(0,0)),(d+1,(1,0))):
            self.assertEqual(tuple(map(int,round_axial(q,0,2*d)['cube_cell'][:2])),expected)
        self.assertNotEqual(round_axial(-d-1,0,2*d)['cube_cell'],round_axial(-d+1,0,2*d)['cube_cell'])

    def test_box_on_boundary_stays_unresolved(self):
        q=DyadicInterval(127,129,8);r=DyadicInterval(0,0,8);s=-q
        result=certify_box(q,r,s)
        self.assertEqual(result['status'],'UNRESOLVED_BOUNDARY');self.assertIsNone(result['cell'])
        q=DyadicInterval(127,127,8)
        self.assertEqual(certify_box(q,r,-q)['cell'],['0','0'])

    def test_refinement_resolves_but_budget_exhaustion_is_not_success(self):
        source=PolarSource(65535,12345,3,1)
        coarse=source.locate(initial_bits=8,max_bits=8)
        self.assertIsNone(coarse['cell'])
        self.assertEqual(coarse['status'],'UNRESOLVED_BOUNDARY')
        fine=source.locate(initial_bits=8,max_bits=128)
        self.assertIsNotNone(fine['cell'])
        self.assertGreater(len(fine['refinement_bits']),1)
        self.assertTrue(verify_cell_record(fine))

    def test_unresolved_population_never_issues_exact_collision_claims(self):
        phi=[None]+[12345]*15
        result=certified_population(phi,3,1,initial_bits=8,max_bits=8)
        self.assertTrue(result['unresolved_identities'])
        for key in ('occupied_cells','collision_groups','excess_identities_if_collapsed','max_cell_load'):
            self.assertIsNone(result[key])
        self.assertEqual(int(result['certified_identities'])+len(result['unresolved_identities']),16)
        exact=certified_population(phi,3,1)
        lo,hi=map(int,result['occupied_cells_bounds'])
        self.assertTrue(lo<=int(exact['occupied_cells'])<=hi)

    def test_real_diagnostics_exact_branch_does_not_call_float_geometry(self):
        spf=lab.smallest_factors(256);phi=lab.phases(spf,lab.prime_phases(spf))
        before=deepcopy(phi)
        with patch.object(lab,'rounded_hex',side_effect=AssertionError('legacy geometry')), \
             patch.object(math,'sqrt',side_effect=AssertionError('float sqrt')), \
             patch.object(math,'sin',side_effect=AssertionError('float sin')), \
             patch.object(math,'cos',side_effect=AssertionError('float cos')):
            result=lab.diagnostics(phi,cell_scale=(1,1),exact_scale=10**12)
        self.assertEqual(result['cell_membership_exact']['status'],'CERTIFIED_ALL')
        self.assertEqual(result['occupied_cells']+result['excess_identities_if_collapsed'],len(phi))
        self.assertIsNone(result['angular_cv'])
        self.assertEqual(result['angular_cv_role'],'OMITTED_IN_EXACT_MODE')
        self.assertEqual(before,phi)

    def test_legacy_diagnostics_fields_are_unchanged(self):
        path=Path(__file__).resolve().parents[3]/'evidence/migration03/frozen_m02_multiplication_lab.py'
        spec=importlib.util.spec_from_file_location('nollm_visual_toolkit.frozen_m02_lab',path)
        baseline=importlib.util.module_from_spec(spec);spec.loader.exec_module(baseline)
        cases=0
        for n,mode,scale in product((16,256,1024),('golden','rank','zero'),(0.5,1,3)):
            spf=lab.smallest_factors(n);phi=lab.phases(spf,lab.prime_phases(spf,mode))
            self.assertEqual(lab.diagnostics(phi,scale),baseline.diagnostics(phi,scale));cases+=1
        self.assertEqual(cases,27)

    def test_no_float_or_bool_input_laundering(self):
        for args in ((True,None),(1,True),(1,1.0),(1,'1'),(-1,0),(0,0),(1,None),(1,65536),(1,0,1.0,2),(1,0,1,False)):
            with self.assertRaises(ValueError):PolarSource(*args)
        for scale in ((0,1),(-1,1),(1,0),(1,3),(7,2),(1.0,2),(True,1),[1,1]):
            with self.assertRaises(ValueError):lab.diagnostics([None,0],cell_scale=scale)
        for scale in (0,True,float('nan'),2):
            with self.assertRaises(ValueError):lab.diagnostics([None,0],scale,cell_scale=(1,1))
        for values in ([None,False],[None,0.0],[0,0],[None,-1],[None,65536]):
            with self.assertRaises(ValueError):lab.diagnostics(values,cell_scale=(1,1))

    def test_interval_and_precision_validation(self):
        for args in ((1,0,8),(0,1,True),(0.0,1,8),(0,1,7),(0,1,513)):
            with self.assertRaises(ValueError):DyadicInterval(*args)
        with self.assertRaises(ValueError):PolarSource(1,0).locate(initial_bits=64,max_bits=32)
        with self.assertRaises(ValueError):DyadicInterval(-1,1,8).sqrt_nonnegative()
        with self.assertRaises(ValueError):certify_box(*([DyadicInterval(1,2,8)]*3))

    def test_source_identity_and_json_replay(self):
        a=PolarSource(3,16384,1,2).locate();b=PolarSource(3,16384,2,4).locate()
        self.assertEqual(a['cell'],b['cell']);self.assertNotEqual(a['source'],b['source'])
        self.assertTrue(verify_cell_record(json.loads(json.dumps(a))))
        x=certified_population([None,0,8192],1,1,include_certificates=True)
        self.assertTrue(all(verify_cell_record(v) for v in x['certificates']))

    def test_population_digest_preserves_ordered_phase_sources(self):
        first=[None,0,8192,16384];second=[None,0,16384,8192]
        a=lab.diagnostics(first,cell_scale=(1,1))
        b=lab.diagnostics(second,cell_scale=(1,1))
        self.assertEqual(a['angular_counts'],b['angular_counts'])
        self.assertNotEqual(a['cell_membership_exact']['phase_source_sha256'],
                            b['cell_membership_exact']['phase_source_sha256'])
        import hashlib
        raw=json.dumps([None,'0','8192','16384'],separators=(',',':')).encode('utf-8')
        self.assertEqual(a['cell_membership_exact']['phase_source_sha256'],hashlib.sha256(raw).hexdigest())

    def test_replay_rejects_tampered_certificate(self):
        source=PolarSource(3,16384,1,2).locate()
        corruptions=[lambda r:r['cell'].__setitem__(0,'0'),
                     lambda r:r['root_certificates'][0].__setitem__('polynomial_residual','0'),
                     lambda r:r['coordinate_bounds'][0].__setitem__('lower_numerator','0'),
                     lambda r:r.__setitem__('status','CERTIFIED_INTERIOR'),
                     lambda r:r['source'].__setitem__('phase_tick','16384.0'),
                     lambda r:r['rounding_certificate'].__setitem__('boundary',1)]
        for mutate in corruptions:
            bad=deepcopy(source);mutate(bad);self.assertFalse(verify_cell_record(bad))

    def test_cached_phase_values_cannot_bypass_type_validation(self):
        phase_bounds(1,64)
        for tick,bits in ((True,64),(1.0,64),(1,64.0),(1,True)):
            with self.assertRaises(ValueError):phase_bounds(tick,bits)
        with self.assertRaises(ValueError):certified_population([None,0],1,1,include_certificates='yes')

    def test_brc_root_and_division_facades_are_executed(self):
        from enterprise_math import exact_arithmetic as brc
        with patch.object(brc,'brc_evaluate_root',wraps=brc.brc_evaluate_root) as roots, \
             patch.object(brc,'brc_evaluate_division',wraps=brc.brc_evaluate_division) as divisions:
            PolarSource(10,12345).locate(initial_bits=65,max_bits=65)
        self.assertGreater(roots.call_count,0)
        self.assertGreater(divisions.call_count,0)

    def test_transitive_missing_brc_dependency_is_not_hidden(self):
        import builtins
        original=builtins.__import__
        def missing(name,*args,**kwargs):
            if name=='enterprise_math':
                raise ModuleNotFoundError('transitive missing',name='unrelated_dependency')
            return original(name,*args,**kwargs)
        with patch('builtins.__import__',side_effect=missing):
            with self.assertRaises(ModuleNotFoundError) as caught:PolarSource(1,0).locate()
        self.assertEqual(caught.exception.name,'unrelated_dependency')

    def test_standalone_import_requires_brc_for_execution(self):
        path=Path(sys.modules[PolarSource.__module__].__file__).resolve()
        code='''import importlib.util,sys
s=importlib.util.spec_from_file_location("certified",sys.argv[1]);m=importlib.util.module_from_spec(s);sys.modules[s.name]=m;s.loader.exec_module(m)
x=m.PolarSource(1,0)
try:x.locate()
except RuntimeError as e:assert "No approximate fallback" in str(e)
else:raise AssertionError("missing BRC hidden")
'''
        result=subprocess.run([sys.executable,'-I','-S','-c',code,str(path)],capture_output=True,text=True)
        self.assertEqual(result.returncode,0,result.stderr)

if __name__=='__main__':unittest.main(verbosity=2)
