"""Exact local acceptance with an independent Smith-normal-form oracle."""
from __future__ import annotations
from dataclasses import replace
from fractions import Fraction as F
from itertools import product
from math import comb
from pathlib import Path
import hashlib
import json
import random
import sys
import unittest
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT/'src'))
from enterprise_math.heartbeat_switching_carry import (
    SplitCarryState, growing_block_state, split_carry_push, split_feedback_packet,
    certify_lattice_ports, linear_carry_spread)
from enterprise_math.brc_transport import Affine, eye, mm, sm, inv, matrix
from enterprise_math.brc_histogram import WeightHistogram
from enterprise_math.brc_control_port import ControlPacket, certify_control_partition

REPORT = {}

def depths(a, prime=2):
    a = sp.Matrix(a)
    den = sp.ilcm(*[v.q for v in a])
    sf = smith_normal_form(a*den, domain=sp.ZZ)
    def v(n):
        n = abs(int(n)); out = 0
        assert n
        while n % prime == 0:
            n //= prime; out += 1
        return out
    return tuple(v(sf[i,i])-v(den) for i in range(a.rows))


def shear(i,j,k):
    a = [list(row) for row in eye(6)]; a[i][j] = F(k)
    return tuple(tuple(row) for row in a)


class SwitchingTests(unittest.TestCase):
    def test_01_pinned_sources(self):
        pins={'brc_transport.py':'be1debe367263931bd5e93fd750be3ed54624fe1',
              'brc_control_port.py':'44def6b8ac787e798d3cc2c6be16f873f91b9db8',
              'brc_histogram.py':'9a3962ec095095f14e63a91cfe6b7ebf07d9a1d1'}
        for name, sha in pins.items():
            data=(ROOT/'src/enterprise_math'/name).read_bytes()
            got=hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
            self.assertEqual(got,sha)
        REPORT['source_reuse']={'exact_unchanged_modules':pins}

    def test_02_all_short_split_words(self):
        plus=SplitCarryState(1,1).action(2).a
        minus=SplitCarryState(1,-1).action(2).a
        self.assertEqual(mm(plus,minus),sm(2,eye(6)))
        count=0
        for n in range(1,9):
            for word in product((-1,1),repeat=n):
                s=SplitCarryState(0,0); a=eye(6)
                for sign in word:
                    s=s.advance(sign); a=mm(plus if sign==1 else minus,a)
                self.assertEqual(a,s.action(2).a)
                self.assertEqual(depths(a),s.smith_depths)
                self.assertEqual(linear_carry_spread(a,2),abs(s.debt))
                count+=1
        REPORT['all_short_words']={'words':count,'max_length':8}

    def test_03_sqrt_debt_schedule(self):
        s=SplitCarryState(0,0); checked=0
        for k in range(1,51):
            for sign in [1]*k+[-1]*k:
                s=s.advance(sign)
                self.assertEqual(s,growing_block_state(s.steps)); checked+=1
            self.assertEqual(s.debt,0)
        peaks=[]
        for k in (1,2,3,10,100,10000):
            peak=growing_block_state(k*k)
            self.assertEqual(peak.debt,k)
            self.assertEqual(sum(peak.smith_depths),3*k*k)
            self.assertEqual(growing_block_state(k*(k+1)).debt,0)
            peaks.append({'time':k*k,'debt':k})
        REPORT['nonperiodic_schedule']={'literal_beats':checked,'peaks':peaks}

    def test_04_smith_type_not_future_state(self):
        a,b=SplitCarryState(4,2),SplitCarryState(4,-2)
        self.assertEqual(a.smith_depths,b.smith_depths)
        self.assertEqual(abs(a.advance(1).debt),3)
        self.assertEqual(abs(b.advance(1).debt),1)
        REPORT['erased_orientation_witness']={'current':a.smith_depths,
            'next_spreads':[3,1]}

    def test_05_exact_branch_distribution(self):
        distribution={SplitCarryState(0,0):WeightHistogram.from_counts({1:1})}
        comparisons=0
        for n in range(1,81):
            distribution=split_carry_push(distribution,[(1,F(1,2),1),(-1,F(1,2),1)])
            for s,h in distribution.items():
                u=(n+s.debt)//2
                self.assertEqual(h.entries,((F(1,2**n),comb(n,u)),)); comparisons+=1
            self.assertEqual(sum(h.total_mass for h in distribution.values()),1)
            self.assertEqual(sum(h.total_mass*s.debt for s,h in distribution.items()),0)
            self.assertEqual(sum(h.total_mass*s.debt**2 for s,h in distribution.items()),n)
        REPORT['brc_distribution']={'beats':80,'binomial_coefficients_checked':comparisons,
            'represented_paths':str(2**80),'retained_debt_states':len(distribution),
            'mean_debt':0,'mean_squared_spread':80,'mass':'1'}

    def test_06_feedback_lattice(self):
        packet,bases,scales=split_feedback_packet()
        cert=certify_lattice_ports(packet,bases,2,scales)
        self.assertTrue(cert.recheck(packet))
        self.assertEqual(cert.basis_spreads,(1,0,1))
        current=ControlPacket.identity(3)
        for n in range(1,33):
            current=current.then(packet.at(n-1))
            out=current.evaluate(1,(1,-2,3,0,1,5))
            mass=sum(h.total_mass for h in out.values())
            self.assertEqual(mass,1)
            if n%2==0:
                self.assertEqual(len(out),1)
                (control,x),hist=next(iter(out.items()))
                self.assertEqual(control,1)
                self.assertEqual(x,tuple(F(2**(n//2))*v for v in (1,-2,3,0,1,5)))
                self.assertEqual(hist.entries,((F(1,2**(n//2)),2**(n//2)),))
            for s,t,h in current.blocks:
                for w,a,c in h.entries:
                    self.assertLessEqual(linear_carry_spread(a.a,2),cert.endpoint_bound(s,t))
        with self.assertRaises(ValueError):
            certify_control_partition(packet,(0,0,0))
        REPORT['feedback']={'heartbeat_updates':32,'pair_choices':65536,
            'ready_to_ready_spread_bound':0,'ready_to_odd_bound':1,
            'all_ports_collapsed_rejected':True}

    def test_07_dense_common_lattice(self):
        # Three genuine mixing actions share one lattice after scalar removal.
        diagonal=tuple(tuple(2**[0,1,0,2,0,3][i] if i==j else 0 for j in range(6)) for i in range(6))
        frame=mm(shear(0,5,1),mm(shear(2,1,-1),diagonal))
        units=(mm(shear(0,1,1),shear(3,4,-2)),
               mm(shear(5,2,3),shear(1,3,1)),
               mm(shear(4,0,1),shear(2,5,-1)))
        actions=tuple(Affine(sm(8,mm(mm(frame,u),inv(frame))),(0,)*6) for u in units)
        self.assertTrue(all(v.denominator==1 for a in actions for row in a.a for v in row))
        packet=ControlPacket.from_edges(1,0,1,((0,0,F(1,3),a,1) for a in actions))
        cert=certify_lattice_ports(packet,(frame,),2,{(0,0):3})
        self.assertEqual(cert.endpoint_bound(0,0),6)
        checked=0; biggest=0
        for word in product(range(3),repeat=4):
            a=eye(6)
            for j in word:a=mm(actions[j].a,a)
            s=depths(a); spread=max(s)-min(s)
            self.assertLessEqual(spread,6)
            self.assertEqual(spread,linear_carry_spread(a,2))
            biggest=max(biggest,spread); checked+=1
        REPORT['dense_lattice']={'actions':3,'all_length4_words':checked,
            'uniform_all_words_bound':6,'observed_max':biggest}

    def test_08_incompatible_local_lattices(self):
        a=[list(row) for row in sm(2,eye(6))];a[0][1]=F(1);a=tuple(map(tuple,a))
        b=[list(row) for row in sm(2,eye(6))];b[1][0]=F(1);b=tuple(map(tuple,b))
        sa=tuple(tuple((2 if i==1 else 1) if i==j else 0 for j in range(6)) for i in range(6))
        sb=tuple(tuple((2 if i==0 else 1) if i==j else 0 for j in range(6)) for i in range(6))
        pa=ControlPacket.from_edges(1,0,1,[(0,0,1,Affine(a,(0,)*6),1)])
        pb=ControlPacket.from_edges(1,0,1,[(0,0,1,Affine(b,(0,)*6),1)])
        certify_lattice_ports(pa,(sa,),2,{(0,0):1})
        certify_lattice_ports(pb,(sb,),2,{(0,0):1})
        with self.assertRaises(ValueError):
            certify_lattice_ports(pa.alternatives(pb),(sa,),2,{(0,0):1})
        combined=mm(b,a); ac=eye(6); bc=eye(6); pc=eye(6)
        for n in range(1,21):
            ac=mm(a,ac);bc=mm(b,bc);pc=mm(combined,pc)
            self.assertLessEqual(linear_carry_spread(ac,2),2)
            self.assertLessEqual(linear_carry_spread(bc,2),2)
            self.assertEqual(depths(pc),(0,2*n,2*n,2*n,2*n,4*n))
        REPORT['incompatible_lattices']={'powers':20,'individual_bound':2,
            'alternating_spread_per_pair':4,'shared_supplied_lattice_rejected':True}

    def test_09_rejections(self):
        packet,bases,scales=split_feedback_packet()
        cert=certify_lattice_ports(packet,bases,2,scales)
        calls=[lambda:SplitCarryState(2,1), lambda:SplitCarryState(-1,0),
               lambda:SplitCarryState(1,True), lambda:SplitCarryState(0,0).advance(0),
               lambda:growing_block_state(True),lambda:linear_carry_spread(eye(6),4),
               lambda:certify_lattice_ports(packet,bases,2,{(1,2):0}),
               lambda:replace(cert,source_digest='x').recheck(packet),
               lambda:cert.recheck(packet.at(1)),
               lambda:certify_lattice_ports(packet,bases,2,{k:0 for k in scales}),
               lambda:cert.endpoint_bound(-1,0),
               lambda:split_carry_push({SplitCarryState(0,0):WeightHistogram.from_counts({1:1}),
                                        SplitCarryState(1,1):WeightHistogram.from_counts({1:1})},[(1,1,1)])]
        for call in calls:
            with self.assertRaises((ValueError,TypeError)):call()
        REPORT['invalid_inputs']=len(calls)

if __name__=='__main__':
    suite=unittest.defaultTestLoader.loadTestsFromTestCase(SwitchingTests)
    result=unittest.TextTestRunner(verbosity=2).run(suite)
    target=ROOT/'research_notes/heartbeat_switching_carry_20260920_AD0416/RESULTS.json'
    target.parent.mkdir(parents=True,exist_ok=True)
    output={'status':'PASS' if result.wasSuccessful() else 'FAIL',
        'test_groups':result.testsRun,'failures':len(result.failures),'errors':len(result.errors),
        'oracle':'SymPy '+sp.__version__+' exact Smith normal form',
        'checks':REPORT,'scope':'research candidate; no full-repository or production acceptance'}
    target.write_text(json.dumps(output,ensure_ascii=False,indent=2)+'\n')
    sys.exit(not result.wasSuccessful())
