"""Exact finite tests, with independent explicit endpoint and matrix oracles."""
from __future__ import annotations
import hashlib
import importlib.util
import itertools
import json
from pathlib import Path
import random
import sys
import unittest
from dataclasses import replace
from fractions import Fraction as F

ROOT=Path(__file__).resolve().parents[1]
NOTE=ROOT/'research_notes/heartbeat_brc_conditional_lift_20260920_AD0416'
sys.path[:0]=[str(ROOT/'src'),str(NOTE)]
from enterprise_math.brc_transport import Affine, eye, mm, ma, sm, MomentState
from enterprise_math.brc_control_port import ControlPacket
from enterprise_math.brc_control_mass import control_mass_matrix, certify_control_mass_partition
from enterprise_math.brc_conditional_lift import (ConditionalLift, independence_witness,
    certify_conditional_lift, conditional_mass_matrix, conditional_mass_defect,
    encode_endpoint_measure, lift_endpoint_measure)
from enterprise_math.brc_weighted_recurrent import (finite_recurrent_mass_analysis,
    recurrent_mass_power, verify_recurrent_integer_stable_certificate,
    verify_recurrent_integer_divergence_certificate)
_spec=importlib.util.spec_from_file_location('hb_conditional_model_AD0416',NOTE/'model.py')
model=importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(model)
REPORT={}
ID=Affine.identity(6)
ZERO=(0,)*6

def scalar_packet(weights,reset=False):
    n=len(weights)
    return ControlPacket.from_edges(n,0,1,((i,j,weights[i]/n if reset else weights[i],ID,1)
        for i in range(n) for j in (range(n) if reset else (i,))))

def moments(mu):
    out={}
    for (a,x),w in mu.items():
        m=sm(w,MomentState.from_point(x).to_matrix())
        out[a]=ma(out[a],m) if a in out else m
    return {a:MomentState.from_matrix(m) for a,m in out.items()}

def rownorm(a):return max(sum(abs(v) for v in row) for row in a)

class ConditionalLiftTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.packets=[model.phase_packet(p,start=p) for p in range(6)]
        cls.certificates=[certify_conditional_lift(p,model.LIFT,mode='affine_mass') for p in cls.packets]

    def test_01_source_reuse(self):
        expected={'brc_transport.py':'be1debe367263931bd5e93fd750be3ed54624fe1',
          'brc_histogram.py':'9a3962ec095095f14e63a91cfe6b7ebf07d9a1d1',
          'brc_control_port.py':'44def6b8ac787e798d3cc2c6be16f873f91b9db8',
          'brc_control_mass.py':'e8811e5f194fc57b294be7255214361fe99395d5',
          'brc_weighted_recurrent.py':'4e6b3132580e3cd70a20a0d8bd4d28792b961afb'}
        for filename,sha in expected.items():
            data=(ROOT/'src/enterprise_math'/filename).read_bytes()
            self.assertEqual(hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest(),sha)
        REPORT['source_reuse']={'verified_blobs':expected,'executed_unchanged':True}

    def test_02_independence_and_common_cause(self):
        rng=random.Random(20260920)
        for _ in range(150):
            a=[F(rng.randrange(7),5) for _ in range(3)]
            b=[F(rng.randrange(9),7) for _ in range(4)]
            self.assertIsNone(independence_witness([[x*y for y in b] for x in a]))
        self.assertIsNone(independence_witness([[0,0],[0,0]]))
        gated=((F(3,8),F(1,8)),(F(1,8),F(3,8)))
        self.assertEqual(independence_witness(gated),(0,0,F(1,8)))
        mixture=((F(1,2),0),(0,F(1,2)))
        self.assertEqual(independence_witness(mixture),(0,0,F(1,4)))
        REPORT['factorization']={'product_tables':150,'gate_defect':'1/8','forgotten_common_cause_defect':'1/4'}

    def test_03_false_independence_changes_stability(self):
        w=(F(9,8),F(3,8),F(3,8),F(9,8))
        held=scalar_packet(w);reset=scalar_packet(w,True)
        lift=ConditionalLift.uniform((0,)*4)
        cert=certify_conditional_lift(reset,lift)
        self.assertEqual(conditional_mass_matrix(cert),((F(3,4),),))
        cert.recheck(reset)
        with self.assertRaises(ValueError):certify_conditional_lift(held,lift)
        with self.assertRaises(ValueError):certify_control_mass_partition(reset,(0,)*4)
        with self.assertRaises(ValueError):cert.check_input((1,0,0,0))
        ar=finite_recurrent_mass_analysis(control_mass_matrix(reset))
        ah=finite_recurrent_mass_analysis(control_mass_matrix(held))
        self.assertTrue(ar.stable);self.assertFalse(ah.stable)
        self.assertTrue(ar.verify_stable_certificate())
        self.assertTrue(verify_recurrent_integer_divergence_certificate(control_mass_matrix(held),(1,0,0,0)))
        self.assertEqual(sum(ar.canonical_potential)/4,4)
        masses=[sum(x**n for x in w)/4 for n in range(13)]
        self.assertEqual(masses[2],F(45,64))
        self.assertEqual(F(3,4)**2,F(9,16))
        REPORT['stability_witness']={'held':'DIVERGENT','actual_reset':'STABLE','reset_total':'4',
          'held_two_tick_mass':'45/64','false_product_two_tick_mass':'9/16',
          'closed_form_checked_depths':13}

    def test_04_mass_does_not_certify_spatial_correlation(self):
        plus=Affine(eye(6),(1,0,0,0,0,0));minus=Affine(eye(6),(-1,0,0,0,0,0))
        p=ControlPacket.from_edges(2,0,1,((i,j,F(1,2),plus if j==0 else minus,1)
                                         for i in range(2) for j in range(2)))
        lift=ConditionalLift.uniform((0,0))
        certify_conditional_lift(p,lift,mode='mass')
        with self.assertRaises(ValueError):certify_conditional_lift(p,lift,mode='affine_mass')
        with self.assertRaises(ValueError):encode_endpoint_measure(lift,{(0,ZERO):F(1,2),(1,(1,0,0,0,0,0)):F(1,2)})
        good=lift_endpoint_measure(lift,{(0,ZERO):1})
        self.assertEqual(encode_endpoint_measure(lift,good),{(0,ZERO):1})
        REPORT['joint_effect_boundary']={'mass_passed':True,'affine_mass_rejected':True,
                                         'mass_only_input_check_insufficient_for_space':True}

    def test_05_six_phase_exact_certificates(self):
        for p,c in zip(self.packets,self.certificates):
            self.assertEqual(c.quotient.state_count,28)
            self.assertEqual(c.coefficient_checks,512)
            with self.assertRaises(ValueError):certify_control_mass_partition(p,model.LABELS)
        signature={(r,sum(mask),tuple(1+F(1 if r in (0,3) else -1,2)*(mask[p]-F(sum(mask),6))
                    for p in range(6))) for r,mask in model.STATES}
        self.assertEqual(len(signature),256)
        REPORT['six_phase_certificates']={'raw_controls':256,'conditional_controls':28,'phases':6,
          'coefficient_equalities':3072,'strong_partition_rejected_phases':6,
          'all_phase_mass_row_signatures':256,'raw_branch_blocks':[len(p.blocks) for p in self.packets]}

    def test_06_actual_refresh_is_required(self):
        for phase in range(6):
            p=model.phase_packet(phase,refresh=False)
            with self.assertRaises(ValueError):certify_conditional_lift(p,model.LIFT)
        REPORT['refresh_removal']={'failed_certificates':6,'reset_not_performed_by_compiler':True}

    def test_07_exact_endpoint_measures_and_moments(self):
        coarse={(1,(0,2,-1,0,1,3)):F(1,2),(26,(3,0,2,1,-1,2)):F(1,2)}
        raw=lift_endpoint_measure(model.LIFT,coarse)
        state=moments(coarse)
        sizes=[]
        for t,(p,c) in enumerate(zip(self.packets,self.certificates)):
            raw=model.endpoint_push(raw,p)
            coarse=model.endpoint_push(coarse,c.quotient)
            self.assertEqual(raw,lift_endpoint_measure(model.LIFT,coarse))
            self.assertEqual(coarse,encode_endpoint_measure(model.LIFT,raw))
            self.assertTrue(all(x[0]%4==model.STATES[i][0] for i,x in raw))
            state=c.quotient.moment_action(state)
            self.assertEqual(state,moments(coarse))
            sizes.append((len(raw),len(coarse)))
        REPORT['endpoint_oracle']={'steps':6,'all_six_motion_axes_used':True,'endpoint_support_sizes':sizes,
          'raw_integer_residue_consistency':True,'conditional_moment_checks':6}

    def test_08_long_mass_and_periodic_potential(self):
        alpha=tuple(F(i+1,406) for i in range(28))
        raw=model.LIFT.lift_mass(alpha)
        micro_edges=[model.mass_edges(p) for p in self.packets]
        coarse_edges=[model.mass_edges(c.quotient) for c in self.certificates]
        for t in range(60):
            raw=model.row_push(raw,micro_edges[t%6],256)
            alpha=model.row_push(alpha,coarse_edges[t%6],28)
            self.assertEqual(raw,model.LIFT.lift_mass(alpha))
            self.assertEqual(sum(raw),F(3,4)**(t+1))
        gains=[]
        for phase in range(6):
            gains.append(tuple(1+F(1 if r in (0,3) else -1,2)*(m[phase]-F(sum(m),6))
                               for r,m in model.STATES))
        potentials=[tuple(1+3*g for g in row) for row in gains]
        for phase,edges in enumerate(micro_edges):
            stepped=[F(0)]*256
            for i,j,w in edges:stepped[i]+=w*potentials[(phase+1)%6][j]
            self.assertEqual(tuple(stepped),tuple(h-1 for h in potentials[phase]))
        W=control_mass_matrix(self.packets[0])
        cert=tuple(int(4*h) for h in potentials[0])
        self.assertTrue(verify_recurrent_integer_stable_certificate(W,cert))
        self.assertEqual(max(sum(row) for row in W),F(17,16))
        product=eye(28)
        for c in self.certificates:product=mm(product,conditional_mass_matrix(c))
        a=finite_recurrent_mass_analysis(product)
        self.assertTrue(a.stable);self.assertTrue(a.verify_stable_certificate())
        self.assertEqual(set(a.canonical_potential),{F(4096,3367)})
        REPORT['recurrent_reuse']={'mass_steps':60,'raw_max_one_step_row_mass':'17/16',
          'full_256_state_integer_certificate':True,'time_periodic_potential_checks':1536,
          'cycle_quotient_size':28,'cycle_potential':'4096/3367','all_tick_total_for_admissible_unit_input':'4'}

    def test_09_residual_identity_and_bound(self):
        packet=scalar_packet((F(1,2),F(3,4)))
        lift=ConditionalLift.uniform((0,0))
        Q,E=conditional_mass_defect(packet,lift);W=control_mass_matrix(packet);L=lift.matrix()
        self.assertEqual(Q,((F(5,8),),));self.assertEqual(E,((F(-1,16),F(1,16)),))
        for n in range(1,11):
            actual=ma(mm(L,recurrent_mass_power(W,n)),sm(-1,mm(recurrent_mass_power(Q,n),L)))
            total=((F(0),F(0)),)
            for j in range(n):
                total=ma(total,mm(mm(recurrent_mass_power(Q,j),E),recurrent_mass_power(W,n-1-j)))
            self.assertEqual(actual,total)
            bound=rownorm(E)*sum(rownorm(Q)**j*rownorm(W)**(n-1-j) for j in range(n))
            self.assertLessEqual(rownorm(actual),bound)
        sw=finite_recurrent_mass_analysis(W).star;sq=finite_recurrent_mass_analysis(Q).star
        actual=ma(mm(L,sw),sm(-1,mm(sq,L)))
        self.assertEqual(actual,mm(mm(sq,E),sw))
        self.assertEqual(rownorm(actual),1)
        bound=rownorm(E)/((1-rownorm(W))*(1-rownorm(Q)))
        self.assertEqual(bound,F(4,3))
        REPORT['defect_accounting']={'finite_depths':10,'E':[['-1/16','1/16']],
          'actual_star_defect_norm':'1','proved_star_norm_bound':'4/3','unsafe_certificate_not_granted':True}

    def test_10_zero_support_boundary(self):
        lift=ConditionalLift((0,0),(1,0))
        packet=scalar_packet((F(1,2),2))
        c=certify_conditional_lift(packet,lift)
        self.assertFalse(lift.full_support)
        self.assertTrue(finite_recurrent_mass_analysis(conditional_mass_matrix(c)).stable)
        self.assertFalse(finite_recurrent_mass_analysis(control_mass_matrix(packet)).stable)
        REPORT['support_boundary']={'restricted_family_stable':True,'unrepresented_state_unstable':True}

    def test_11_type_and_binding_guards(self):
        p=scalar_packet((F(1,2),F(1,2)));l=ConditionalLift.uniform((0,0));c=certify_conditional_lift(p,l)
        calls=[lambda:ConditionalLift((0,2),(1,1)),lambda:ConditionalLift((0,0),(1,1)),
          lambda:ConditionalLift((0,0),(F(1,2),.5)),lambda:ConditionalLift((True,),(1,)),
          lambda:independence_witness([[1],[1,2]]),lambda:independence_witness([[1,-1]]),
          lambda:certify_conditional_lift(p,l,mode='full_path'),
          lambda:certify_conditional_lift(p,ConditionalLift.uniform((0,1,2))),
          lambda:replace(c,source_digest='0'*64).recheck(p),lambda:c.recheck(p.at(1)),
          lambda:l.encode_mass((1,0)),lambda:encode_endpoint_measure(l,{(0,(0,)*7):1})]
        calls.append(lambda:certify_conditional_lift(ControlPacket.from_edges(1,0,1,[(0,0,1,Affine(eye(6),(F(1,2),0,0,0,0,0)),1)]),ConditionalLift.uniform((0,)),mode='affine_mass'))
        for call in calls:
            with self.assertRaises((ValueError,TypeError)):call()
        REPORT['guard_rejections']=len(calls)

    def test_12_compose_with_existing_mass_quotient(self):
        from enterprise_math.brc_control_mass import ControlMassQuotient
        from enterprise_math.brc_control_port import certify_control_partition
        for cert in self.certificates:
            small=ControlMassQuotient.compile(cert.quotient,(0,)*28)
            self.assertEqual(small.quotient_mass_matrix,((F(3,4),),))
            with self.assertRaises(ValueError):certify_control_partition(cert.quotient,(0,)*28)
        REPORT['composed_observer_scopes']={'conditional_joint_controls':28,'mass_only_controls':1,
          'scalar_recurrent_mass':'3/4','effect_merge_rejected':True}

    def test_13_partial_refresh_threshold(self):
        from enterprise_math.brc_control_mass import ControlMassQuotient
        values=sorted(set([F(k,100) for k in range(101)]+[F(5,21),F(1,4),F(1,2)]))
        for theta in values:
            packet=model.partial_refresh_packet(theta)
            q=ControlMassQuotient.compile(packet,(0,1,1,0)).quotient_mass_matrix
            expected=((F(9,8)*(1-theta/2),F(9,8)*theta/2),
                      (F(3,8)*theta/2,F(3,8)*(1-theta/2)))
            self.assertEqual(q,expected)
            a=finite_recurrent_mass_analysis(q)
            self.assertEqual(a.stable,theta>F(5,21))
            self.assertEqual(a.stable,finite_recurrent_mass_analysis(control_mass_matrix(packet)).stable)
            if a.stable:
                self.assertEqual(sum(a.canonical_potential)/2,(16+48*theta)/(21*theta-5))
            if theta<1:
                with self.assertRaises(ValueError):certify_conditional_lift(packet,ConditionalLift.uniform((0,)*4))
        REPORT['partial_refresh']={'exact_parameter_values':len(values),'threshold':'5/21',
          'condition':'theta > 5/21','total_at_quarter':'112','total_at_half':'80/11',
          'total_at_full':'4','exact_relation_quotient':2,'initial_joint_states':4}

if __name__=='__main__':
    result=unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(ConditionalLiftTests))
    report={'status':'PASS' if result.wasSuccessful() else 'FAIL','new_test_groups':result.testsRun,
      'checks':REPORT,'independent_review':False,'full_project_tests':False,'production_changed':False,
      'scope':'finite exact conditional measures; no universal independence/complexity claim'}
    (NOTE/'RESULTS.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    sys.exit(not result.wasSuccessful())
