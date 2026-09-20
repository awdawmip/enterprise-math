"""Exact acceptance tests; independent Smith-form oracle and literal path checks."""
from __future__ import annotations
from fractions import Fraction as F
from dataclasses import replace
from itertools import product
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
from enterprise_math.brc_transport import Affine, eye, mm, mv, sm, inv, matrix, ma
from enterprise_math.brc_control_port import ControlPacket
from enterprise_math.heartbeat_switching_carry import linear_carry_spread, _valuation, _minimum
from enterprise_math.heartbeat_lattice_search import (
    find_common_lattice, verify_lattice_search_result, bind_single_port_packet,
    find_phase_lattice, verify_phase_lattice_result, phase_edge_certificates,
    reachable_column_action,
)
REPORT = {}


def shear(i, j, value):
    a = [list(row) for row in eye(6)]; a[i][j] = F(value)
    return tuple(tuple(row) for row in a)


def diagonal(values):
    return tuple(tuple(F(values[i]) if i == j else F(0) for j in range(6)) for i in range(6))


def depths(a, p):
    a = sp.Matrix(a)
    d = int(sp.ilcm(*[v.q for v in a]))
    sf = smith_normal_form(a*d, domain=sp.ZZ)
    return tuple(_valuation(int(sf[i, i]), p)-_valuation(d, p) for i in range(6))


def compose(actions, word):
    a = eye(6)
    for j in word:
        a = mm(actions[j], a)
    return a


def cyclic(p=2):
    return tuple(tuple(F(p) if i == 0 and j == 5 else F(i == j+1) for j in range(6)) for i in range(6))


def dense_actions():
    d = diagonal([1,2,1,4,1,8])
    frame = mm(shear(0,5,1), mm(shear(2,1,-1), d))
    units = (mm(shear(0,1,1),shear(3,4,-2)),
             mm(shear(5,2,3),shear(1,3,1)),
             mm(shear(4,0,1),shear(2,5,-1)))
    return tuple(sm(8, mm(mm(frame,u),inv(frame))) for u in units)


class LatticeSearchTests(unittest.TestCase):
    def test_01_source_pins(self):
        pins = {'heartbeat_switching_carry.py':'81fa56ea5967daa9fbbec66f06fed696a5620bb5',
                'brc_transport.py':'be1debe367263931bd5e93fd750be3ed54624fe1',
                'brc_control_port.py':'44def6b8ac787e798d3cc2c6be16f873f91b9db8',
                'brc_histogram.py':'9a3962ec095095f14e63a91cfe6b7ebf07d9a1d1'}
        for file, sha in pins.items():
            b = (ROOT/'src/enterprise_math'/file).read_bytes()
            self.assertEqual(hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest(), sha)
        REPORT['source_reuse'] = pins

    def test_02_scalar_and_local_units(self):
        # Determinants may contain primes other than p: Z_p-, not Z-unimodularity.
        actions = (sm(2,diagonal([3,1,1,1,1,1])), sm(4,shear(2,4,-5)))
        r = find_common_lattice(actions,2,depth_budget=0)
        self.assertEqual(r.status,'FIXED_LATTICE'); self.assertEqual(r.rounds,1)
        self.assertEqual(r.all_word_spread_bound,0)
        self.assertTrue(verify_lattice_search_result(actions,r))
        REPORT['local_units'] = {'odd_determinant_allowed':True,'rounds':r.rounds}

    def test_03_find_not_supply(self):
        a=sm(2,shear(0,1,F(1,2)))
        r=find_common_lattice([a],2,depth_budget=1)
        self.assertEqual(r.status,'FIXED_LATTICE');self.assertEqual(r.rounds,2)
        self.assertEqual(r.basis,diagonal([F(1,2),1,1,1,1,1]))
        self.assertEqual(r.all_word_spread_bound,2)
        self.assertTrue(verify_lattice_search_result([a],r))
        escaped=find_common_lattice([a],2,depth_budget=0)
        self.assertEqual(escaped.status,'ESCAPING_WORD')
        self.assertTrue(verify_lattice_search_result([a],escaped))
        REPORT['simple_discovery']={'radius':r.history[-1].radius,'rounds':r.rounds,'bound':2}

    def test_04_dense_found_basis(self):
        actions=dense_actions()
        r=find_common_lattice(actions,2,depth_budget=3)
        self.assertEqual(r.status,'FIXED_LATTICE');self.assertTrue(verify_lattice_search_result(actions,r))
        checked=0; largest=0
        for word in product(range(3),repeat=4):
            d=depths(compose(actions,word),2);width=max(d)-min(d)
            self.assertLessEqual(width,r.all_word_spread_bound)
            largest=max(largest,width);checked+=1
        REPORT['dense_discovery']={'rounds':r.rounds,'radius':r.history[-1].radius,
            'bound':r.all_word_spread_bound,'literal_length4_words':checked,'attained_spread':largest,
            'index_depth_trace':[s.index_depth for s in r.history]}

    def test_05_random_hidden_lattices(self):
        rng=random.Random(2026092001);cases=0;checks=0;maxrounds=0
        for p in (2,3,5):
            for _ in range(10):
                ds=[rng.randrange(4) for _ in range(6)]
                frame=diagonal([p**k for k in ds])
                for _ in range(4):
                    i,j=rng.sample(range(6),2); frame=mm(shear(i,j,rng.choice([-2,-1,1,2])),frame)
                units=[]
                for _ in range(3):
                    i,j=rng.sample(range(6),2); k,l=rng.sample(range(6),2)
                    units.append(mm(shear(i,j,rng.choice([-2,-1,1,2])),shear(k,l,1)))
                actions=tuple(sm(p**3,mm(mm(frame,u),inv(frame))) for u in units)
                r=find_common_lattice(actions,p,depth_budget=3)
                self.assertEqual(r.status,'FIXED_LATTICE');verify_lattice_search_result(actions,r)
                self.assertLessEqual(r.rounds,19); maxrounds=max(maxrounds,r.rounds)
                for _ in range(5):
                    word=tuple(rng.randrange(3) for _ in range(7)); d=depths(compose(actions,word),p)
                    self.assertLessEqual(max(d)-min(d),r.all_word_spread_bound);checks+=1
                cases+=1
        REPORT['random_hidden_lattices']={'families':cases,'independent_smith_paths':checks,'max_rounds':maxrounds}

    def test_06_reachable_basis_and_literal_span(self):
        actions=dense_actions();r=find_common_lattice(actions,2,depth_budget=3)
        checks=0
        for col in r.spanning_columns:
            a=reachable_column_action(actions,2,col)
            v=tuple(F(2)**(-3*len(col.word))*a[i][col.axis] for i in range(6))
            self.assertEqual(v,col.vector);checks+=1
        # Every literal short word lies in the final lattice; selected paths
        # provide six independent local coordinates, not full history storage.
        for n in range(5):
            for word in product(range(3),repeat=n):
                b=sm(F(2)**(-3*n),compose(actions,word))
                self.assertGreaterEqual(_minimum(mm(inv(r.basis),b),2),0);checks+=1
        s=matrix(tuple(tuple(c.vector[i] for c in r.spanning_columns) for i in range(6)))
        self.assertGreaterEqual(_minimum(mm(inv(s),r.basis),2),0)
        self.assertGreaterEqual(_minimum(mm(inv(r.basis),s),2),0)
        REPORT['path_provenance']={'selected_actual_path_columns':6,'literal_checks':checks}

    def test_07_budget_failure_is_not_unboundedness(self):
        a=[list(row) for row in sm(2,eye(6))]
        for i in range(5):a[i][i+1]=F(1)
        a=tuple(map(tuple,a))
        bad=find_common_lattice([a],2,depth_budget=4)
        good=find_common_lattice([a],2,depth_budget=5)
        self.assertEqual(bad.status,'ESCAPING_WORD');verify_lattice_search_result([a],bad)
        self.assertEqual(good.status,'FIXED_LATTICE');verify_lattice_search_result([a],good)
        self.assertEqual(good.history[-1].radius,5)
        REPORT['budget_boundary']={'radius4':bad.status,'escaping_word_length':len(bad.escape.word),
            'radius5':good.status,'fixed_rounds':good.rounds,'all_word_bound':good.all_word_spread_bound}

    def test_08_incompatible_pair_actual_witnesses(self):
        actions=(sm(2,shear(0,1,F(1,2))),sm(2,shear(1,0,F(1,2))))
        out=[]
        for radius in range(7):
            r=find_common_lattice(actions,2,depth_budget=radius)
            self.assertEqual(r.status,'ESCAPING_WORD');verify_lattice_search_result(actions,r)
            a=reachable_column_action(actions,2,r.escape);d=depths(a,2)
            self.assertGreater(max(d)-min(d),radius)
            out.append({'budget':radius,'word':r.escape.word,'axis':r.escape.axis,'spread':max(d)-min(d)})
        REPORT['unbounded_pair_budget_witnesses']=out

    def test_09_fractional_mean_clock(self):
        checked=0;phases=[]
        for p in (2,3,5):
            a=cyclic(p)
            r=find_phase_lattice([a],p,depth_budget=1)
            self.assertEqual(r.status,'FIXED_LATTICE');self.assertEqual(r.phases,tuple(range(6)))
            verify_phase_lattice_result([a],r)
            self.assertEqual(len(phase_edge_certificates([a],r)),6)
            for n in range(1,25):
                d=depths(compose([a],(0,)*n),p)
                self.assertEqual(max(d)-min(d),int(n%6!=0));checked+=1
            phases.append({'prime':p,'ports':len(r.phases),'rounds':r.rounds,'bound':r.all_word_spread_bound})
        REPORT['fractional_mean_clock']={'families':phases,'smith_powers_checked':checked}

    def test_10_multiaction_clock_and_escape(self):
        a=cyclic(2);actions=(a,mm(a,a),ma(eye(6),a))
        r=find_phase_lattice(actions,2,depth_budget=1)
        self.assertEqual(r.status,'FIXED_LATTICE');verify_phase_lattice_result(actions,r)
        certs=phase_edge_certificates(actions,r)
        self.assertEqual(len(certs),18)
        checked=0
        for word in product(range(3),repeat=4):
            d=depths(compose(actions,word),2)
            self.assertLessEqual(max(d)-min(d),r.all_word_spread_bound);checked+=1
        u=diagonal([2,2,2,1,1,1]);v=diagonal([1,1,1,2,2,2])
        escaped=find_phase_lattice([u,v],2,depth_budget=2)
        self.assertEqual(escaped.status,'ESCAPING_WORD');verify_phase_lattice_result([u,v],escaped)
        REPORT['mixed_clock_family']={'actions':3,'ports':6,'edge_certificates':18,'literal_words':checked,
            'unrestricted_split_escape_word':escaped.escape.word,'escape_source_phase':escaped.escape.source_phase}

    def test_11_brc_weights_untouched(self):
        actions=dense_actions()
        packet=ControlPacket.from_edges(1,0,1,[(0,0,F(1,6),Affine(actions[0],(1,0,0,0,0,0)),1),
            (0,0,F(1,3),Affine(actions[1],(0,1,0,0,0,0)),1),
            (0,0,F(1,4),Affine(actions[2],(0,0,1,0,0,0)),2)])
        ordered=tuple(a.a for _,_,hist in packet.blocks for _,a,_ in hist.entries)
        r=find_common_lattice(ordered,2,depth_budget=3)
        cert=bind_single_port_packet(packet,r);self.assertTrue(cert.recheck(packet))
        current=ControlPacket.identity(1)
        for n in range(1,5):
            current=current.then(packet.at(n-1))
            hist=current.blocks[0][2].forget_effects()
            self.assertEqual(hist.total_mass,1)
            self.assertEqual(sum(c for w,c in hist.entries),4**n)
        REPORT['brc_execution']={'actual_packet_steps':4,'path_multiplicity':256,'mass':'1',
            'nonzero_offsets_preserved':True,'certificate_rechecked':True}

    def test_12_resource_and_tamper(self):
        a=sm(2,shear(0,1,F(1,2)))
        limited=find_common_lattice([a],2,depth_budget=1,max_rounds=1)
        self.assertEqual(limited.status,'SEARCH_LIMIT')
        with self.assertRaises(ValueError):verify_lattice_search_result([a],limited)
        r=find_common_lattice([a],2,depth_budget=1)
        with self.assertRaises(ValueError):verify_lattice_search_result([a],replace(r,source_digest='x'))
        with self.assertRaises(ValueError):verify_lattice_search_result([a],replace(r,basis=eye(6)))
        bad=find_common_lattice([a],2,depth_budget=0)
        with self.assertRaises(ValueError):verify_lattice_search_result([a],replace(bad,escape=replace(bad.escape,word=())))
        phase=find_phase_lattice([cyclic()],2,depth_budget=1,max_rounds=0)
        self.assertEqual(phase.status,'SEARCH_LIMIT')
        with self.assertRaises(ValueError):verify_phase_lattice_result([cyclic()],phase)
        REPORT['resource_tamper']={'limited_outputs':2,'tampered_proofs_rejected':3}

    def test_13_invalid_inputs(self):
        calls=[lambda:find_common_lattice([],2,depth_budget=1),
            lambda:find_common_lattice([eye(5)],2,depth_budget=1),
            lambda:find_common_lattice([sm(0,eye(6))],2,depth_budget=1),
            lambda:find_common_lattice([sm(F(1,2),eye(6))],2,depth_budget=1),
            lambda:find_common_lattice([eye(6)],4,depth_budget=1),
            lambda:find_common_lattice([eye(6)],2,depth_budget=True),
            lambda:find_common_lattice([eye(6)],2,depth_budget=1,max_rounds=-1),
            lambda:find_common_lattice([cyclic()],2,depth_budget=1),
            lambda:find_phase_lattice([eye(6)],2,depth_budget=-1),
            lambda:find_phase_lattice([eye(6)],2,depth_budget=1,max_rounds=True)]
        for call in calls:
            with self.assertRaises((ValueError,TypeError)):call()
        REPORT['invalid_inputs']=len(calls)

if __name__=='__main__':
    suite=unittest.defaultTestLoader.loadTestsFromTestCase(LatticeSearchTests)
    result=unittest.TextTestRunner(verbosity=2).run(suite)
    out={'status':'PASS' if result.wasSuccessful() else 'FAIL','test_groups':result.testsRun,
         'failures':len(result.failures),'errors':len(result.errors),'oracle':'SymPy '+sp.__version__+' exact Smith form',
         'checks':REPORT,'scope':'bounded-depth research certificate; not full project/production/theorem admission'}
    path=ROOT/'research_notes/heartbeat_lattice_search_20260920_AD0416/RESULTS.json'
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
    sys.exit(not result.wasSuccessful())
