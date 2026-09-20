"""Independent finite-prefix/SNF oracles for the exact peak observer candidate."""
from dataclasses import replace
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json, random, sys, unittest
from sympy import Matrix as SM, ZZ
from sympy.matrices.normalforms import smith_normal_form
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'src'))
from enterprise_math.brc_transport import Affine, matrix, eye, mm, inv, sm
from enterprise_math.brc_control_port import ControlPacket
from enterprise_math.heartbeat_switching_carry import _valuation
from enterprise_math.heartbeat_peak_kernel import (
    canonical_carry_lattice, compile_peak_kernel, verify_peak_kernel,
    solve_peak_probability, first_passage_prefix, killed_symmetric_peak)
from enterprise_math.heartbeat_graph_carry import (
    graph_from_packet, find_graph_lattices, carry_peak_tail_bound)
REPORT={}; ZERO=(0,)*6; I=eye(6)
U=matrix([[2 if i==j and i<3 else int(i==j) for j in range(6)] for i in range(6)])
V=matrix([[2 if i==j and i>=3 else int(i==j) for j in range(6)] for i in range(6)])
def block3(a):
    return matrix([[a[i%2][j%2] if i//2==j//2 else 0 for j in range(6)] for i in range(6)])
A=block3(((0,2),(1,0)));B=block3(((1,1),(1,-1)))
S=matrix([[int(j>=i) for j in range(6)] for i in range(6)])
DA=mm(mm(S,A),inv(S));DB=mm(mm(S,B),inv(S))
def model(actions=(U,V),s=F(4,5)):
    return ControlPacket.from_edges(2,0,1,
       [(0,0,s/len(actions),Affine(a,ZERO),1) for a in actions if s]
       + ([(0,1,1-s,Affine.identity(6),1)] if s!=1 else [])
       + [(1,1,1,Affine.identity(6),1)])
def snf_spread(a,p=2):
    sf=smith_normal_form(SM([[int(v) for v in row] for row in a]),domain=ZZ)
    vals=[_valuation(int(sf[i,i]),p) for i in range(6)]
    return max(vals)-min(vals)
def literal_first_hits(packet,m,steps,p=2):
    edges=[[] for _ in range(packet.state_count)]
    for s,t,h in packet.blocks:
        for w,a,c in h.entries:edges[s].append((t,w*c,a.a))
    live=[(0,I,F(1))];first=[];checks=0
    for _ in range(steps):
        nxt=[];hit=F(0)
        for s,prod,mass in live:
            for t,prob,a in edges[s]:
                q=mm(a,prod);checks+=1
                if snf_spread(q,p)>=m:hit+=mass*prob
                else:nxt.append((t,q,mass*prob))
        first.append(hit);live=nxt
    return tuple(first),checks
class PeakTests(unittest.TestCase):
    def test_01_canonical_homothety_and_right_units(self):
        rng=random.Random(20260926)
        for _ in range(36):
            while True:
                a=matrix([[rng.randint(-3,3) for _ in range(6)] for __ in range(6)])
                if SM(a).det():break
            h=canonical_carry_lattice(a,2)
            self.assertEqual(h,canonical_carry_lattice(h,2))
            self.assertEqual(snf_spread(a),snf_spread(h))
            k=matrix([[3 if i==j==0 else int(i==j) for j in range(6)] for i in range(6)])
            k=mm(k,S)
            self.assertEqual(h,canonical_carry_lattice(sm(F(8,5),mm(a,k)),2))
        self.assertEqual(canonical_carry_lattice(sm(3,I),2),I)
        REPORT['canonical_random_SNF_and_right_unit_cases']=36
    def test_02_smith_type_not_future_state(self):
        p=mm(U,U);q=mm(V,V)
        self.assertEqual(snf_spread(p),snf_spread(q))
        self.assertNotEqual(canonical_carry_lattice(p,2),canonical_carry_lattice(q,2))
        self.assertEqual((snf_spread(mm(U,p)),snf_spread(mm(U,q))),(3,1))
        REPORT['orientation_witness']={'current_spreads':[2,2],'next_spreads':[3,1]}
    def test_03_exact_killed_peak(self):
        p=model();rows=[]
        for m in (1,2,3,4,5,8,12,16):
            k=compile_peak_kernel(p,2,threshold=m,max_states=256)
            r=solve_peak_probability(p,k);expected=F(2**(m+1),4**m+1)
            self.assertTrue(k.complete and r.exact)
            self.assertEqual((r.lower,r.upper),(expected,expected))
            self.assertEqual(killed_symmetric_peak(F(4,5),m),expected)
            rows.append({'threshold':m,'states':len(k.states),'active':len(r.active_states),
               'exact_tail':str(r.lower),'stepcount_tail':str(F(4,5)**m)})
        REPORT['killed_peak_rows']=rows
    def test_04_compare_prior_tool(self):
        p=model();edges=graph_from_packet(p)
        cert=find_graph_lattices(2,tuple(e for e in edges if e.source==e.target==1),2,depth_budget=0)
        old=carry_peak_tail_bound(p,2,(cert,),z=F(6,5),threshold=16)
        r=solve_peak_probability(p,compile_peak_kernel(p,2,threshold=16,max_states=128))
        self.assertEqual(old.majorant_means[0],4);self.assertEqual(old.majorant_moments[0],5)
        self.assertLess(r.upper,F(4,5)**16)
        self.assertLess(F(4,5)**16,old.peak_tail_upper_bounds[0])
        REPORT['prior_tool_executed']={'old_mean_cost':'4','old_mgf':'5',
            'old_bound':str(old.peak_tail_upper_bounds[0]),'new_exact':str(r.lower)}
    def test_05_dense_noncommuting(self):
        self.assertEqual(mm(A,A),sm(2,I));self.assertEqual(mm(B,B),sm(2,I))
        self.assertNotEqual(mm(A,B),mm(B,A))
        self.assertGreater(max(sum(v!=0 for v in row) for row in DA),1)
        p=model((DA,DB));rows=[]
        for m in (1,2,3,4,6):
            k=compile_peak_kernel(p,2,threshold=m,max_states=256)
            r=solve_peak_probability(p,k)
            self.assertEqual(r.lower,killed_symmetric_peak(F(4,5),m));self.assertTrue(r.exact)
            rows.append((m,len(k.states),str(r.lower)))
        checks=0
        for length in range(1,7):
            for word in product((0,1),repeat=length):
                stack=[];a=I
                for j in word:
                    if stack and stack[-1]==j:stack.pop()
                    else:stack.append(j)
                    a=mm((DA,DB)[j],a)
                self.assertEqual(snf_spread(a),len(stack));checks+=1
        REPORT['dense_noncommuting']={'threshold_rows':rows,'literal_SNF_checks':checks}
    def test_06_first_hit_not_endpoint(self):
        p=model((DA,DB));k=compile_peak_kernel(p,2,threshold=2,max_states=128)
        actual=tuple(x for x,_ in first_passage_prefix(p,k,5))
        expected,checks=literal_first_hits(p,2,5);self.assertEqual(actual,expected)
        a=I;sp=[]
        for action in (A,B,B,A):a=mm(action,a);sp.append(snf_spread(a))
        self.assertEqual(sp,[1,2,1,0])
        REPORT['first_hit']={'prefix_checks':checks,'probabilities':list(map(str,actual)),
                             'return_after_hit_spreads':sp}
    def test_07_safe_closed_cycle(self):
        p=ControlPacket.from_edges(2,0,1,[(0,1,1,Affine(U,ZERO),1),(1,0,1,Affine(V,ZERO),1)])
        k=compile_peak_kernel(p,2,threshold=2,max_states=16);r=solve_peak_probability(p,k)
        self.assertEqual((r.lower,r.upper),(0,0));self.assertEqual(r.active_states,())
        self.assertEqual(len(k.states),2)
        REPORT['safe_closed_cycle']={'states':2,'tail':'0','singular_inverse_avoided':True}
    def test_08_unstopped(self):
        p=model(s=F(1));r=solve_peak_probability(p,compile_peak_kernel(p,2,threshold=5,max_states=64))
        self.assertEqual(r.lower,1);self.assertTrue(r.exact)
        REPORT['unstopped_threshold5']='1'
    def test_09_frontier_intervals(self):
        p=model();m=4;exact=killed_symmetric_peak(F(4,5),m);rows=[];last=(F(0),F(1))
        for cap in (1,2,4,8,14,32):
            k=compile_peak_kernel(p,2,threshold=m,max_states=cap);r=solve_peak_probability(p,k)
            self.assertLessEqual(r.lower,exact);self.assertGreaterEqual(r.upper,exact)
            self.assertGreaterEqual(r.lower,last[0]);self.assertLessEqual(r.upper,last[1])
            rows.append((cap,str(r.lower),str(r.upper),r.exact));last=(r.lower,r.upper)
        REPORT['budget_intervals']=rows
    def test_10_weight_count_and_translation(self):
        p=ControlPacket.from_edges(2,7,3,[(0,0,F(1,5),Affine(U,(1,-2,0,0,0,0)),2),
          (0,0,F(1,10),Affine(V,(0,0,1,0,-1,0)),4),
          (0,1,F(1,5),Affine.identity(6),1),(1,1,1,Affine.identity(6),1)])
        r=solve_peak_probability(p,compile_peak_kernel(p,2,threshold=4,max_states=32))
        self.assertEqual(r.lower,F(32,257));REPORT['nonzero_translation_and_BRC_counts']='PASS'
    def test_11_random_dense_prefix(self):
        rng=random.Random(20260927);checked=0;completed=0
        for trial in range(5):
            mats=[]
            for _ in range(2):
                while True:
                    a=matrix([[rng.randint(-1,1) for _ in range(6)] for __ in range(6)])
                    if SM(a).det():break
                mats.append(a)
            p=model(tuple(mats),s=F(2,3));k=compile_peak_kernel(p,2,threshold=2,max_states=192)
            if k.complete:
                actual=tuple(v for v,_ in first_passage_prefix(p,k,3))
                expected,checks=literal_first_hits(p,2,3)
                self.assertEqual(actual,expected);checked+=checks;completed+=1
            r=solve_peak_probability(p,k);self.assertLessEqual(r.lower,r.upper)
        REPORT['random_dense']={'literal_checks':checked,'complete_kernels':completed,'models':5}
    def test_12_input_and_certificate_failures(self):
        p=model();k=compile_peak_kernel(p,2,threshold=2,max_states=16)
        calls=[lambda:compile_peak_kernel(p,4,threshold=2),lambda:compile_peak_kernel(p,2,threshold=0),
          lambda:compile_peak_kernel(p,2,threshold=True),lambda:compile_peak_kernel(p,2,threshold=2,max_states=0),
          lambda:compile_peak_kernel(p,2,threshold=2,start_control=8),
          lambda:canonical_carry_lattice(((1,0),(0,1)),2),lambda:killed_symmetric_peak(0.8,4),
          lambda:verify_peak_kernel(p,replace(k,source_digest='0'*64)),
          lambda:verify_peak_kernel(p,replace(k,arcs=k.arcs[:-1])),
          lambda:verify_peak_kernel(p,replace(k,witnesses=((),)*len(k.states)))]
        for call in calls:
            with self.assertRaises((ValueError,TypeError)):call()
        bad=ControlPacket.from_edges(1,0,1,[(0,0,F(1,2),Affine.identity(6),1)])
        with self.assertRaises(ValueError):compile_peak_kernel(bad,2,threshold=1)
        with self.assertRaises(ValueError):compile_peak_kernel(ControlPacket.identity(1),2,threshold=1)
        REPORT['rejections']=len(calls)+2
    def test_13_resource_quantile(self):
        risk=F(1,10000)
        exact=next(m for m in range(1,100) if killed_symmetric_peak(F(4,5),m)<=risk)
        crude=next(m for m in range(1,100) if F(4,5)**m<=risk)
        self.assertEqual((exact,crude),(15,42))
        p=model();r=solve_peak_probability(p,compile_peak_kernel(p,2,threshold=15,max_states=128))
        self.assertEqual(r.lower,F(65536,1073741825))
        self.assertLessEqual(r.upper,risk)
        REPORT['risk_budget']={'risk':str(risk),'exact_first_safe_threshold':exact,
            'majorant_first_safe_threshold':crude,'exact_capacity':exact-1,'majorant_capacity':crude-1,
            'exact_tail_at15':str(r.lower)}
if __name__=='__main__':
    result=unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(PeakTests))
    folder=ROOT/'research_notes/heartbeat_peak_kernel_20260920_AD0416';folder.mkdir(parents=True,exist_ok=True)
    (folder/'RESULTS.json').write_text(json.dumps({'status':'PASS' if result.wasSuccessful() else 'FAIL',
        'test_groups':result.testsRun,'failures':len(result.failures),'errors':len(result.errors),'checks':REPORT},
        ensure_ascii=False,indent=2)+'\n')
    sys.exit(not result.wasSuccessful())
