import unittest,sys,hashlib,json,random,re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];ART=ROOT/'artifacts';sys.path.insert(0,str(ROOT/'tools'))
import r055_core as r
class R055Tests(unittest.TestCase):
 def test_frozen_hashes(self):
  exp={'R055_RELAXATION_PROTOCOL.json':'aa69f2bc31cb9b5ec574a85de2879b9f8f765cfdfdb6dd0cbfc625cf8feed683','R055_MOVE_ENERGY_REGISTRY.json':'83d546105a3fa721ba5cadea9a1bbf217a1661fdf0d1560fcdccc6d4c9d29ceb','R055_INITIAL_STATE_REGISTRY.json':'5de0e7ae6ff89cf81342f6c18125eb1eebd78c4725c0324acee2893552acd7f2','R055_THEOREM_COUNTEREXAMPLE_LEDGER.json':'159ba8ed8e664522fec5fa9771b8efc7630d0b0c78ca5a2f67e7c33c724ac660'}
  for f,h in exp.items():self.assertEqual(hashlib.sha256((ART/f).read_bytes()).hexdigest(),h)
 def test_Q_D6_invariant(self):
  for a in range(-7,8):
   for b in range(-7,8):
    q=r.Q((a,b))
    for t in range(12):self.assertEqual(r.Q(r.transform_point((a,b),t)),q)
 def test_pairwise_identity(self):
  for N in [1,2,6,19,43]:
   for C in r.initial_states(N).values():self.assertEqual(r.energy_fast(C),r.energy_pairwise(C))
 def test_delta_identity(self):
  for N in [6,19]:
   C=next(iter(r.initial_states(N).values()));G=r.energy_fast(C)
   for dyn in ['D1','D2']:
    for m in r.legal_moves(C,dyn,strict_desc=False)[:30]:
     Cp=frozenset((set(C)-{m.u})|{m.v});self.assertEqual(r.delta_g(C,m.u,m.v),r.energy_fast(Cp)-G)
 def test_all_frozen_initial_generators_valid(self):
  for N in [19,31,37,53,61,79,91,113,127,151,169,199,217,43,67,103,139,181,241,301]:
   ss=r.initial_states(N);self.assertEqual(len(ss),8)
   for C in ss.values():self.assertEqual(len(C),N);self.assertTrue(r.connected(C));self.assertTrue(r.hole_free(C))
 def test_small_N_counts_and_N6_counterexample(self):
  x=json.loads((ART/'R055_SMALL_N_EXHAUSTIVE_ATLAS.json').read_text());z=x['results']
  self.assertEqual([q['hole_free_classes'] for q in z],[1,1,3,7,22,81,331,1435,6505,30086,141229,669584])
  self.assertEqual(z[5]['D1_local_min_count'],3);self.assertEqual(z[5]['D1_local_not_D2_min_count'],2);self.assertFalse(z[5]['G_P_minimizer_sets_coincide'])
 def test_centered_shell_D1_and_D2_formula(self):
  for rr in range(1,21):
   N=1+3*rr*(rr+1);C=frozenset((a,b) for a in range(-rr,rr+1) for b in range(-rr,rr+1) if max(abs(a),abs(b),abs(a+b))<=rr)
   self.assertEqual(len(C),N);self.assertEqual(r.sum_point(C),(0,0));self.assertIsNone(r.select_move_fast(C,'D1','T0_CANONICAL_MIN'))
   if rr>=6:
    u=(-rr,0);v=((rr+2)//2,(rr+1)//2);d=r.delta_g(C,u,v);self.assertLess(d,0)
    Cp=frozenset((set(C)-{u})|{v});self.assertTrue(r.connected(Cp));self.assertTrue(r.hole_free(Cp))
 def test_external_gate_after_holdout(self):
  ext=json.loads((ART/'R055_EXTERNAL_SHAPE_COMPARISON.json').read_text())
  self.assertEqual(ext['freeze_gate']['R055_THEOREM_COUNTEREXAMPLE_LEDGER_SHA256'],'159ba8ed8e664522fec5fa9771b8efc7630d0b0c78ca5a2f67e7c33c724ac660')
  self.assertEqual(ext['freeze_gate']['R055_HOLDOUT_RESULTS_SHA256'],hashlib.sha256((ART/'R055_HOLDOUT_RESULTS.json').read_bytes()).hexdigest())
 def test_relaxation_engine_has_no_external_target_tokens(self):
  s=(ROOT/'tools/r055_dynamics_exact.cpp').read_text().lower()
  for tok in ['circle','teacher','radius','circumference','tangent','m_pi']:self.assertNotIn(tok,s)
  self.assertIsNone(re.search(r'\bpi\b',s))
 def test_holdout_rules_unchanged(self):
  h=json.loads((ART/'R055_HOLDOUT_RESULTS.json').read_text())
  self.assertEqual(h['status'],'STRICT_HOLDOUT_COMPLETE_NO_RULE_CHANGES');self.assertFalse(h['external_circle_hexagon_comparison_opened_during_holdout']);self.assertFalse(h['classical_pi_used_during_holdout'])
  self.assertTrue(all(q['tie_break_dependence_witnessed'] for q in h['rows']))
if __name__=='__main__':unittest.main(verbosity=2)
