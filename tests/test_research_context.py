import json, sys, tempfile, unittest
from copy import deepcopy
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'tools')); sys.path.insert(0,str(ROOT/'experiments'))
from research_context import derive_signature, compile_signature, audit_pack, relevant_common_surface_slice, render_human
from r030_context_backtest import run_backtest, run_sweep

REG=json.load(open(ROOT/'research_reasoning_tools_seed.json'))
GOLD=json.load(open(ROOT/'R030_HISTORICAL_CONTEXT_GOLD.json'))

class ResearchContextTests(unittest.TestCase):
    def test_header_and_horizon_without_future_keyword(self):
        s=derive_signature('<!-- ENTERPRISE_MATH_TASK_V1 {"task_id":"T"} -->\nDeclared horizon is arbitrary finite word length 3; compare one-step exactness with composition.')
        self.assertEqual(s['task_id'],'T'); self.assertEqual(s['future_horizon'],'FINITE_WORD')
        self.assertIn('one_step_to_composition',s['risk_flags'])

    def test_boolean_negation_does_not_assert_boolean_carrier(self):
        s=derive_signature('<!-- ENTERPRISE_MATH_TASK_V1 {"task_id":"T"} -->\nCarrier: N-count. no Boolean result-support is an observable.')
        self.assertIn('N-count',s['carrier_types']); self.assertNotIn('Boolean support',s['carrier_types'])

    def test_boolean_does_not_trigger_lean_substring(self):
        s=derive_signature('<!-- ENTERPRISE_MATH_TASK_V1 {"task_id":"T"} -->\nBoolean support only.')
        self.assertNotIn('LEAN',s['evidence_targets'])

    def test_interpretive_lens_never_exact(self):
        s={'task_id':'T','risk_flags':[]}
        p=compile_signature(s,REG,diagnostic_text='ontology possible actual world',strategy='ALL_MATCHES')
        self.assertNotIn('INTERPRETIVE_ONTOLOGY_LENS',p['selected_exact_tools'])
        self.assertIn('INTERPRETIVE_ONTOLOGY_LENS',p['selected_diagnostic_tools'])

    def test_mcc_is_smaller_than_all_matches(self):
        t=next(x for x in GOLD['tasks'] if x['task']=='R022')
        m=compile_signature(t['signature_fixture'],REG,diagnostic_text=t['startup_excerpt'],strategy='MINIMUM_CRITICAL_COVER')
        a=compile_signature(t['signature_fixture'],REG,diagnostic_text=t['startup_excerpt'],strategy='ALL_MATCHES')
        self.assertLess(len(m['selected_exact_tools'])+len(m['selected_diagnostic_tools']),len(a['selected_exact_tools'])+len(a['selected_diagnostic_tools']))
        self.assertFalse(m['uncovered_required_capabilities'])

    def test_r023i_selects_actual_module_coverage_guard(self):
        t=next(x for x in GOLD['tasks'] if x['task']=='R023I')
        p=compile_signature(t['signature_fixture'],REG,strategy='MINIMUM_CRITICAL_COVER')
        self.assertIn('ROOT_COVERAGE_EVIDENCE_CHECK',p['selected_exact_tools'])
        self.assertIn('SOURCE_PROVENANCE_VS_COVERAGE_EVIDENCE',p['selected_exact_tools'])

    def test_r025_selects_regime_exhaustion_without_hindsight_answer(self):
        t=next(x for x in GOLD['tasks'] if x['task']=='R025')
        p=compile_signature(t['signature_fixture'],REG,strategy='MINIMUM_CRITICAL_COVER')
        self.assertIn('REGIME_EXHAUSTION',p['selected_exact_tools'])
        joined=' '.join(p['known_non_implications'])
        self.assertNotIn('k=0 invalidates',joined)
        self.assertNotIn('r>=2^p',joined)

    def test_declared_vs_realized_tool_is_specific(self):
        b=compile_signature({'task_id':'T','risk_flags':['future_modality']},REG,strategy='MINIMUM_CRITICAL_COVER')
        m=compile_signature({'task_id':'T','risk_flags':['future_modality','realized_vs_declared']},REG,strategy='MINIMUM_CRITICAL_COVER')
        self.assertNotIn('DECLARED_VS_REALIZED_FUTURE',b['selected_exact_tools'])
        self.assertIn('DECLARED_VS_REALIZED_FUTURE',m['selected_exact_tools'])

    def test_digest_changes_with_task_signature(self):
        s={'task_id':'T','risk_flags':['future_modality']}
        a=compile_signature(s,REG,strategy='MINIMUM_CRITICAL_COVER')
        b=compile_signature({**s,'future_horizon':'FINITE_WORD'},REG,strategy='MINIMUM_CRITICAL_COVER')
        self.assertNotEqual(a['context_digest'],b['context_digest'])

    def test_irrelevant_common_surface_movement_does_not_invalidate(self):
        s={'task_id':'T','risk_flags':['evidence_coverage']}
        c1={'schema':'C','families':{'A4_BRC_semantic_core':{'validation':'v1'},'UNRELATED':{'x':1}}}
        c2=deepcopy(c1); c2['families']['UNRELATED']['x']=999
        a=compile_signature(s,REG,common_surface=c1,strategy='MINIMUM_CRITICAL_COVER')
        b=compile_signature(s,REG,common_surface=c2,strategy='MINIMUM_CRITICAL_COVER')
        self.assertEqual(a['source_snapshot']['relevant_common_surface_digest'],b['source_snapshot']['relevant_common_surface_digest'])
        self.assertEqual(a['context_digest'],b['context_digest'])

    def test_relevant_common_surface_movement_invalidates(self):
        s={'task_id':'T','risk_flags':['evidence_coverage']}
        c1={'schema':'C','families':{'A4_BRC_semantic_core':{'validation':'v1'}}}
        c2={'schema':'C','families':{'A4_BRC_semantic_core':{'validation':'v2'}}}
        a=compile_signature(s,REG,common_surface=c1,strategy='MINIMUM_CRITICAL_COVER')
        b=compile_signature(s,REG,common_surface=c2,strategy='MINIMUM_CRITICAL_COVER')
        self.assertNotEqual(a['context_digest'],b['context_digest'])

    def test_audit_detects_tamper(self):
        p=compile_signature({'task_id':'T','risk_flags':['future_modality']},REG,strategy='MINIMUM_CRITICAL_COVER')
        self.assertTrue(audit_pack(p)['pass'])
        p['context_digest']='0'*64
        self.assertFalse(audit_pack(p)['pass'])

    def test_historical_backtest_hits_all_gold(self):
        r=run_backtest(GOLD,REG)
        self.assertEqual(r['aggregate']['covered_gold'],23)
        self.assertEqual(r['aggregate']['recovered_late_distinctions'],4)
        self.assertTrue(r['keyword_attacks']['pass']); self.assertTrue(r['mutation_suite']['pass'])

    def test_mcc_pareto_dominates_unbounded_context(self):
        points,front,_=run_sweep(GOLD,REG)
        self.assertEqual(len(front),1)
        self.assertEqual(front[0]['strategy'],'MINIMUM_CRITICAL_COVER')
        allp=next(x for x in points if x['strategy']=='ALL_MATCHES')
        self.assertEqual(allp['critical_tool_recall'],1.0)
        self.assertGreater(allp['estimated_tool_tokens'],front[0]['estimated_tool_tokens'])

    def test_human_pack_has_required_sections(self):
        t=next(x for x in GOLD['tasks'] if x['task']=='R020')
        p=compile_signature(t['signature_fixture'],REG,strategy='MINIMUM_CRITICAL_COVER')
        h=render_human(p,REG)
        for x in ['TASK SEMANTIC SIGNATURE','CRITICAL REASONING TOOLS','KNOWN NON-IMPLICATIONS','EVIDENCE BOUNDARY','WHAT WAS INTENTIONALLY OMITTED']:
            self.assertIn(x,h)

if __name__=='__main__': unittest.main()
