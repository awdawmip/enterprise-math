"""Scoped exact checks; independent Smith-form and literal-path cross-checks."""
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
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'src'))
from enterprise_math.brc_transport import Affine, matrix, eye, inv, mm, sm
from enterprise_math.brc_control_port import ControlPacket, certify_control_partition
from enterprise_math.brc_conditional_lift import ConditionalLift, certify_conditional_lift
from enterprise_math.brc_weighted_recurrent import gauge_recurrent_mass_matrix, recurrent_mass_power
from enterprise_math.heartbeat_switching_carry import linear_carry_spread, _valuation, _minimum
from enterprise_math.heartbeat_graph_carry import (CarryEdge, GraphColumn, find_graph_lattices,
    replay_graph_word, verify_graph_result, graph_endpoint_bound, graph_from_packet, bottom_component_absorption, carry_peak_tail_bound)
from enterprise_math.heartbeat_lattice_search import find_phase_lattice
REPORT={}

def diagonal(v):
    return tuple(tuple(F(v[i]) if i==j else F(0) for j in range(6)) for i in range(6))
def shear(i,j,c):
    a=[list(r) for r in eye(6)]; a[i][j]=F(c); return matrix(a)
def affine(a,b=(0,)*6):return Affine(a,b)
def split(p=2):return diagonal([p]*3+[1]*3),diagonal([1]*3+[p]*3)
def hyperbolic(p=2):return diagonal([p*p,1,p,p,p,p])
def smith_width(a,p):
    den=1
    from math import lcm
    for row in a:
        for x in row:den=lcm(den,x.denominator)
    sf=smith_normal_form(sp.Matrix(a)*den,domain=sp.ZZ)
    vals=[_valuation(int(sf[i,i]),p)-_valuation(den,p) for i in range(6)]
    return max(vals)-min(vals)
def chain_packet(edges,n):
    return ControlPacket.from_edges(n,0,1,edges)
def weighted_mm(a,b):
    return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(len(b))) for j in range(len(b[0]))) for i in range(len(a)))

class GraphCarryTests(unittest.TestCase):
    def test_01_inputs_and_empty_graph(self):
        for n,e,p,R in [(0,[],2,0),(1,[CarryEdge(0,1,eye(6))],2,0),
                        (1,[CarryEdge(0,0,sm(F(1,2),eye(6)))],2,1),
                        (1,[CarryEdge(0,0,diagonal([0,1,1,1,1,1]))],2,1),
                        (1,[],4,0),(1,[],2,True)]:
            with self.assertRaises((ValueError,TypeError)):find_graph_lattices(n,e,p,depth_budget=R)
        r=find_graph_lattices(2,[],2,depth_budget=0)
        self.assertTrue(verify_graph_result(2,[],r));self.assertEqual(r.all_path_spread_bound,0)
        with self.assertRaises(ValueError):graph_endpoint_bound(2,[],r,(0,0),(1,0))
    def test_02_single_port_specialization(self):
        a=sm(2,shear(0,1,F(1,2)));e=[CarryEdge(0,0,a)]
        r=find_graph_lattices(1,e,2,depth_budget=1);old=find_phase_lattice([a],2,depth_budget=1)
        self.assertEqual(r.bases,old.bases);self.assertEqual(r.rounds,old.rounds)
        self.assertTrue(verify_graph_result(1,e,r));self.assertTrue(all(d==0 for *_,d in r.edge_defects))
    def test_03_alternating_vs_unrestricted(self):
        u,v=split();e=[CarryEdge(0,1,u),CarryEdge(1,0,v)]
        r=find_graph_lattices(2,e,2,depth_budget=1)
        self.assertEqual(r.status,'FIXED_LATTICES');self.assertTrue(all(d==0 for *_,d in r.edge_defects))
        checked=0
        for source in r.states:
            for n in range(1,25):
                word=tuple((source[0]+k)%2 for k in range(n))
                a,_,t=replay_graph_word(2,e,2,source,word)
                self.assertEqual(smith_width(a,2),n%2)
                self.assertLessEqual(linear_carry_spread(a,2),graph_endpoint_bound(2,e,r,source,t));checked+=1
        free=[CarryEdge(0,0,u),CarryEdge(0,0,v)]
        for R in range(4):
            rr=find_graph_lattices(1,free,2,depth_budget=R)
            self.assertEqual(rr.status,'ESCAPING_WORD');self.assertTrue(verify_graph_result(1,free,rr))
        REPORT['alternating']={'lifted_states':len(r.states),'rounds':r.rounds,'certificate_bound':r.all_path_spread_bound,
            'exact_optimal_bound':1,'independent_smith_paths':checked,'free_U_power_spread':'n (proved, not inferred from budgets)'}
    def test_04_one_way_defect_is_finite(self):
        e=[CarryEdge(0,0,eye(6)),CarryEdge(1,1,eye(6)),
           CarryEdge(0,1,sm(2,eye(6))),CarryEdge(0,1,hyperbolic())]
        r=find_graph_lattices(2,e,2,depth_budget=1)
        self.assertEqual(r.status,'FIXED_LATTICES');self.assertEqual(r.potentials,(0,-1))
        self.assertEqual([d for s,t,j,d in r.edge_defects if s!=t],[1,1])
        self.assertEqual(r.all_path_spread_bound,2)
        checks=0
        for a in range(6):
            for b in range(6):
                for edge in (2,3):
                    word=(0,)*a+(edge,)+(1,)*b
                    action,_,target=replay_graph_word(2,e,2,(0,0),word)
                    self.assertEqual(smith_width(action,2),0 if edge==2 else 2);checks+=1
        with self.assertRaises(ValueError):replay_graph_word(2,e,2,(0,0),(3,3))
        REPORT['one_way']={'rounds':r.rounds,'potentials':list(r.potentials),'crossing_index_defects':[1,1],
             'uniform_bound':2,'independent_smith_paths':checks,'all_edge_bijection_impossible':'proved using I and diag(2,1/2,1,1,1,1) parallel edges'}
    def test_05_phase_cycle_fractional_mean(self):
        a=matrix([[F(2) if i==0 and j==5 else F(i==j+1) for j in range(6)] for i in range(6)])
        e=[CarryEdge(0,0,a)]
        r=find_graph_lattices(1,e,2,depth_budget=1)
        self.assertEqual(len(r.states),6);self.assertEqual(r.status,'FIXED_LATTICES')
        self.assertTrue(all(d==0 for *_,d in r.edge_defects));self.assertTrue(verify_graph_result(1,e,r))
    def test_06_actual_columns_and_tampering(self):
        e=[CarryEdge(0,0,sm(2,shear(0,1,F(1,2))))]
        r=find_graph_lattices(1,e,2,depth_budget=1)
        for cols in r.spanning_columns:
            self.assertEqual(len(cols),6)
            for col in cols:
                a,k,t=replay_graph_word(1,e,2,col.source_state,col.word)
                self.assertEqual(col.vector,tuple(F(2)**(-k)*a[i][col.axis] for i in range(6)))
                self.assertEqual(col.target_state,t)
        for rr in [replace(r,source_digest='0'*64),replace(r,potentials=(12,)),replace(r,all_path_spread_bound=0),
                   replace(r,states=((False,0),)),replace(r,potentials=(True,)),replace(r,all_path_spread_bound=True)]:
            with self.assertRaises(ValueError):verify_graph_result(1,e,rr)
        esc=find_graph_lattices(1,e,2,depth_budget=0)
        self.assertTrue(verify_graph_result(1,e,esc))
        with self.assertRaises(ValueError):verify_graph_result(1,e,replace(esc,escape=replace(esc.escape,word=(1,))))
        with self.assertRaises(ValueError):verify_graph_result(1,e,replace(esc,escape=replace(esc.escape,axis=True)))
        with self.assertRaises(ValueError):verify_graph_result(1,e,replace(esc,escape=replace(esc.escape,target_state=(False,0))))
        with self.assertRaises(ValueError):graph_endpoint_bound(1,e,r,(False,0),(0,0))
    def test_07_search_limit_and_retry(self):
        e=[CarryEdge(0,0,sm(2,shear(0,1,F(1,2))))]
        r=find_graph_lattices(1,e,2,depth_budget=1,max_rounds=1)
        self.assertEqual(r.status,'SEARCH_LIMIT')
        with self.assertRaises(ValueError):verify_graph_result(1,e,r)
        zero=find_graph_lattices(1,e,2,depth_budget=1,max_rounds=0)
        self.assertEqual(zero.status,'SEARCH_LIMIT');self.assertEqual(zero.rounds,0)
        r=find_graph_lattices(1,e,2,depth_budget=1);self.assertEqual(r.status,'FIXED_LATTICES')
    def test_08_hidden_multiport_lattices(self):
        rng=random.Random(2026092017);cases=checks=0;maxq=maxrounds=0
        for p in (2,3,5):
            for trial in range(2):
                frames=[]
                for _ in range(3):
                    s=diagonal([F(p)**(-rng.randrange(3)) for _ in range(6)])
                    i,j=rng.sample(range(6),2);frames.append(mm(shear(i,j,rng.choice([-1,1])),s))
                e=[]
                for s,t in ((0,1),(1,2),(2,0),(1,0),(2,1),(0,2)):
                    i,j=rng.sample(range(6),2);unit=shear(i,j,rng.choice([-2,-1,1,2]))
                    a=sm(p*p,mm(mm(frames[t],unit),inv(frames[s])))
                    self.assertTrue(all(v.denominator==1 for row in a for v in row))
                    e.append(CarryEdge(s,t,a))
                r=find_graph_lattices(3,e,p,depth_budget=4)
                self.assertEqual(r.status,'FIXED_LATTICES');verify_graph_result(3,e,r)
                self.assertTrue(all(d==0 for *_,d in r.edge_defects))
                maxq=max(maxq,len(r.states));maxrounds=max(maxrounds,r.rounds)
                for _ in range(12):
                    source=rng.choice(r.states);current=source[0];word=[]
                    for _ in range(8):
                        j=rng.choice([j for j,x in enumerate(e) if x.source==current]);word.append(j);current=e[j].target
                    action,_,target=replay_graph_word(3,e,p,source,tuple(word))
                    width=smith_width(action,p)
                    self.assertLessEqual(width,graph_endpoint_bound(3,e,r,source,target));checks+=1
                cases+=1
        REPORT['hidden_graphs']={'families':cases,'independent_smith_paths':checks,'max_lifted_ports':maxq,'max_rounds':maxrounds}
    def test_09_mass_quotient_loses_order(self):
        u,v=split();packet=chain_packet([(0,1,1,affine(u),1),(1,0,1,affine(v),1)],2)
        lift=ConditionalLift((0,0),(F(1,2),F(1,2)))
        cert=certify_conditional_lift(packet,lift,mode='mass');self.assertTrue(cert.recheck(packet))
        with self.assertRaises(ValueError):certify_conditional_lift(packet,lift,mode='affine_mass')
        with self.assertRaises(ValueError):certify_control_partition(packet,(0,0))
        independent=chain_packet([(0,0,F(1,2),affine(u),1),(0,0,F(1,2),affine(v),1)],1)
        start=(1,)*6
        actual=packet.then(packet.at(1)).evaluate(0,start)
        coarse=independent.then(independent.at(1)).evaluate(0,start)
        actual_mass={str(x):str(h.total_mass) for (port,x),h in actual.items()}
        coarse_mass={str(x):str(h.total_mass) for (port,x),h in coarse.items()}
        self.assertEqual(list(actual_mass.values()),['1'])
        self.assertEqual(sorted(coarse_mass.values()),['1/2','1/4','1/4'])
        REPORT['correlation_witness']={'mass_lift':'PASS','affine_mass_lift':'REJECT','actual_two_step':actual_mass,'iid_two_step':coarse_mass}
    def test_10_packet_weights_not_erased(self):
        a=sm(2,shear(0,1,F(1,2))); b=affine(a,(1,0,-1,0,0,0))
        packet=chain_packet([(0,0,F(1,8),b,2),(0,0,F(3,4),affine(sm(2,eye(6))),1)],1)
        before=repr(packet);edges=graph_from_packet(packet);r=find_graph_lattices(1,edges,2,depth_budget=1)
        self.assertEqual(before,repr(packet));self.assertEqual(r.status,'FIXED_LATTICES')
        joined=packet
        for n in range(1,4):joined=joined.then(packet.at(n))
        out=joined.evaluate(0,(0,)*6)
        self.assertEqual(sum(h.total_mass for h in out.values()),1)
        self.assertEqual(sum(h.count for h in out.values()),3**4)
        REPORT['actual_BRC_execution']={'steps':4,'total_mass':'1','branch_multiplicity':81,'nonzero_affine_offsets_retained':True}
    def test_11_transient_random_debt(self):
        packet=chain_packet([(0,0,F(1,2),affine(hyperbolic()),1),(0,1,F(1,2),affine(eye(6)),1),
                            (1,1,1,affine(eye(6)),1)],2)
        absorption=bottom_component_absorption(packet)
        self.assertEqual(absorption.bottom_components,((1,),))
        self.assertEqual(absorption.absorption_probabilities,((F(1),),(F(1),)))
        self.assertEqual(absorption.transient_star,((F(2),),))
        for n in range(1,41):
            power=recurrent_mass_power(absorption.mass_matrix,n)
            self.assertEqual(power[0][0],F(1,2**n))
        REPORT['transient']={'bottom_components':[[1]],'good_absorption':'1','transient_star':[['2']],
             'max_spread':'2 K','K_distribution':'P(K=k)=2^(-k-1), k>=0','tail':'P(max_spread>=2m)=2^(-m)',
             'almost_sure_finite':True,'common_deterministic_bound':False,'expected_max_spread':'2 (analytic)'}
    def test_12_exact_bad_class_absorption(self):
        packet=chain_packet([(0,0,F(1,4),affine(eye(6)),1),(0,1,F(1,2),affine(eye(6)),1),
                            (0,2,F(1,4),affine(eye(6)),1),(1,1,1,affine(eye(6)),1),
                            (2,2,1,affine(hyperbolic()),1)],3)
        a=bottom_component_absorption(packet)
        self.assertEqual(a.bottom_components,((1,),(2,)))
        self.assertEqual(a.absorption_probabilities[0],(F(2,3),F(1,3)))
        self.assertEqual(a.transient_star,((F(4,3),),))
        REPORT['mixed_absorption']={'bottom_components':[[1],[2]],'probabilities_from_zero':['2/3','1/3'],
           'bad_class_proof':'H^n has p-Smith spread 2n','unbounded_peak_probability':'1/3 (theorem plus exact absorption)'}
    def test_13_subcritical_input_not_normalized(self):
        packet=chain_packet([(0,0,F(1,2),affine(eye(6)),1)],1)
        with self.assertRaises(ValueError):bottom_component_absorption(packet)
        p=chain_packet([(0,1,1,affine(eye(6)),1),(1,0,1,affine(eye(6)),1)],2)
        a=bottom_component_absorption(p);self.assertEqual(a.bottom_components,((0,1),));self.assertEqual(a.transient_star,())
    def test_14_index_weight_is_endpoint_gauge(self):
        e=[CarryEdge(0,0,eye(6)),CarryEdge(1,1,eye(6)),CarryEdge(0,1,sm(2,eye(6))),CarryEdge(0,1,hyperbolic())]
        r=find_graph_lattices(2,e,2,depth_budget=1);self.assertEqual(r.potentials,(0,-1))
        w=((F(1,2),F(1,2)),(F(0),F(1)))
        h=tuple(F(2)**g for g in r.potentials)
        tilted=gauge_recurrent_mass_matrix(w,h)
        self.assertEqual(tilted,((F(1,2),F(1,4)),(F(0),F(1))))
        for n in range(65):
            wn=recurrent_mass_power(w,n);tn=recurrent_mass_power(tilted,n)
            self.assertEqual(tn,gauge_recurrent_mass_matrix(wn,h))
            self.assertEqual(sum(tn[0]),F(1,2)+F(1,2**(n+1)))
        REPORT['index_gauge']={'g':[0,-1],'weighted_mass_at_n':'1/2 + 2^(-n-1)',
            'positive_limit':'1/2','powers_checked':65,'physical_dissipation_claimed':False}
    def test_15_source_reuse_hashes(self):
        pins={'heartbeat_lattice_search.py':'307cb147949256115bc6bc4a479c4f9af884c3eb',
              'heartbeat_switching_carry.py':'81fa56ea5967daa9fbbec66f06fed696a5620bb5',
              'brc_control_mass.py':'e8811e5f194fc57b294be7255214361fe99395d5',
              'brc_weighted_recurrent.py':'4e6b3132580e3cd70a20a0d8bd4d28792b961afb',
              'brc_conditional_lift.py':'6b41c2c2f2d7f7c2bd0bd6624e44b6c333d9675d',
              'brc_control_port.py':'44def6b8ac787e798d3cc2c6be16f873f91b9db8',
              'brc_transport.py':'be1debe367263931bd5e93fd750be3ed54624fe1',
              'brc_histogram.py':'9a3962ec095095f14e63a91cfe6b7ebf07d9a1d1'}
        for f,sha in pins.items():
            b=(ROOT/'src/enterprise_math'/f).read_bytes()
            self.assertEqual(hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest(),sha)
        REPORT['inherited_source_hashes']=pins

    def test_16_geometric_peak_moment_and_confidence_bound(self):
        packet=chain_packet([(0,0,F(1,2),affine(hyperbolic()),1),(0,1,F(1,2),affine(eye(6)),1),
                             (1,1,1,affine(eye(6)),1)],2)
        internal=[CarryEdge(1,1,eye(6))]
        certificate=find_graph_lattices(2,internal,2,depth_budget=0)
        b=carry_peak_tail_bound(packet,2,[certificate],z=F(4,3),threshold=20)
        self.assertEqual(b.majorant_moments,(F(9,2),F(1)))
        self.assertEqual(b.majorant_means,(F(2),F(0)))
        self.assertEqual(b.peak_tail_upper_bounds[0],F(9,2)*F(3,4)**20)
        for m in range(25):
            bb=carry_peak_tail_bound(packet,2,[certificate],z=F(4,3),threshold=2*m)
            self.assertGreaterEqual(bb.peak_tail_upper_bounds[0],F(1,2**m))
        for z in [1,True,1.1,F(3,2)]:
            with self.assertRaises(ValueError):carry_peak_tail_bound(packet,2,[certificate],z=z,threshold=20)
        with self.assertRaises(ValueError):carry_peak_tail_bound(packet,2,[],z=F(4,3),threshold=20)
        REPORT['peak_tail_resource']={'geometric_mgf_z_4_over_3':'9/2','geometric_mean_majorant':'2',
            'R20_upper_bound':str(b.peak_tail_upper_bounds[0]),'R20_exact_tail':'1/1024',
            'probability_bound_not_exact_law':True,'bottom_certificates_actually_verified':True}
    def test_17_two_transient_cost_star_and_certificate_binding(self):
        u,v=split()
        packet=chain_packet([(0,0,F(1,3),affine(hyperbolic()),1),(0,1,F(1,3),affine(u),1),
            (0,2,F(1,3),affine(eye(6)),1),(1,0,F(1,4),affine(v),1),
            (1,2,F(3,4),affine(sm(2,eye(6))),1),(2,2,1,affine(eye(6)),1)],3)
        internal=[CarryEdge(2,2,eye(6))]
        certificate=find_graph_lattices(3,internal,2,depth_budget=0)
        b=carry_peak_tail_bound(packet,2,[certificate],z=F(5,4),threshold=10)
        self.assertEqual(b.majorant_means,(F(13,7),F(5,7),F(0)))
        q=b.weighted_transient_matrix;r=(F(1,3),F(3,4))
        partial=[F(0),F(0)];power=((F(1),F(0)),(F(0),F(1)))
        for k in range(30):
            for i in range(2):partial[i]+=sum(power[i][j]*r[j] for j in range(2))
            for i in range(2):self.assertLessEqual(partial[i],b.majorant_moments[i])
            power=weighted_mm(power,q)
        for i in range(2):
            self.assertEqual(b.majorant_moments[i],r[i]+sum(q[i][j]*b.majorant_moments[j] for j in range(2)))
        wrong=find_graph_lattices(3,[CarryEdge(1,1,eye(6))],2,depth_budget=0)
        with self.assertRaises(ValueError):carry_peak_tail_bound(packet,2,[wrong],z=F(5,4),threshold=10)
        with self.assertRaises(ValueError):carry_peak_tail_bound(packet,3,[certificate],z=F(5,4),threshold=10)
        bad=chain_packet([(0,0,1,affine(hyperbolic()),1)],1)
        escaped=find_graph_lattices(1,graph_from_packet(bad),2,depth_budget=0)
        with self.assertRaises(ValueError):carry_peak_tail_bound(bad,2,[escaped],z=F(5,4),threshold=10)
        REPORT['peak_tail_resource']['two_transient_mgf']=list(map(str,b.majorant_moments))
        REPORT['peak_tail_resource']['two_transient_expected_majorant']=['13/7','5/7','0']
        REPORT['peak_tail_resource']['positive_star_prefixes_checked']=30

if __name__=='__main__':
    suite=unittest.defaultTestLoader.loadTestsFromTestCase(GraphCarryTests)
    result=unittest.TextTestRunner(verbosity=2).run(suite)
    report_path=ROOT/'research_notes/heartbeat_graph_carry_20260920_AD0416/RESULTS.json'
    report_path.parent.mkdir(parents=True,exist_ok=True)
    REPORT['summary']={'groups_run':result.testsRun,'failures':len(result.failures),'errors':len(result.errors),
                      'all_passed':result.wasSuccessful(),'arithmetic':'integer/Fraction; exact SymPy Smith cross-check'}
    report_path.write_text(json.dumps(REPORT,indent=2,ensure_ascii=False)+'\n')
    sys.exit(not result.wasSuccessful())
