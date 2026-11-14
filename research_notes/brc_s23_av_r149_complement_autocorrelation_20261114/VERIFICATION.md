# R149 verification

Date: 2026-11-14. Frozen scientific input: `43ec6098b1330ae86d0a7863be336c5d97f6ef34`.

Command: `python check_r149.py` (Python 3 with standard-library `fractions` and `math`).

Observed local output:

```text
R149_COMPLEMENT_AUTOCORRELATION_PASS
{'words': 1906, 'complement_checks': 11436, 'conditional_autocorrelation_checks': 1906, 'reversal_covariance_checks': 1906, 'noncoprime_congruence_observations': 298, 'positive_covariance_words': 6}
```

Completeness: the source iterates all `2^m` binary candidates for each `1<=m<=15`; support endpoints are calculated from every ordered prefix-index pair `0<=i<j<=m` in exact rational arithmetic. Nonempty support is equivalent to `alpha<beta`. Count and covariance use exact integer quotient/remainder and rational sums. Complement fiber equality is tested at six named K values per retained word; the theorem establishes equality for all K. The condition `a+c≡0 (mod g)` was observed on all 298 noncoprime endpoint cases and remains unproved globally. No independent reviewer acceptance or formal checker execution is claimed.

New reusable results: exact complement C-sequence bijection; closed g-residue autocorrelation under the stated congruence; reversal covariance invariance under that same congruence. Project status: author-side external scalar auxiliary model, `NOT_REVIEWED`, no task CLAIM in this proof.
