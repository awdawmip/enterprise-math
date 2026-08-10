from enterprise_math.closure_async_fairness_equivalence import (
    fairness_completion_certificate,
)


def test_finite_helper_system_certificate_closes_fairness_completion_equivalence():
    for arity in range(4, 9):
        cert = fairness_completion_certificate(arity)
        assert cert.every_nonterminal_has_enabled_helper
        assert cert.enabled_helpers_persist_until_fired
        assert cert.finite_one_shot
        assert cert.weak_fair_implies_completion
        assert cert.completion_implies_weak_fair
        assert cert.execution_classes_equal
