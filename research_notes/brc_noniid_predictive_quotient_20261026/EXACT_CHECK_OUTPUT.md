# Actual local exact-check execution (2026-10-26)

Run: python VERIFY_PORTABLE.py (Python standard-library fractions.Fraction, no floating point).

NONIID_POSITIVE_QUOTIENT PASS (Fraction(341, 600), Fraction(10489, 25200), Fraction(3, 2), Fraction(3, 2))
POSITIVE_PREDICTIVE_CLASS_COUNTS (1,1,2)
NONIID_LR_ONLY_OBSTRUCTION PASS (Fraction(3, 10), Fraction(3, 10), Fraction(3, 2), Fraction(3, 2)) error_sum_lower_bound 7/10
NEGATIVE_PREDICTIVE_CLASS_COUNTS (1,2,4)
NO_LR_OBSTRUCTION PASS (Fraction(3, 4), Fraction(3, 4))
ALL_EXACT_AUTHOR_CHECKS_PASS

Scope: finite explicitly specified positive rational non-iid trees at horizon 2, and the separate horizon-one LR-loss witness. These author-side checks are not an independent Driver review or native EM experiment. GitHub storage/readback does not imply the code was remotely executed.
