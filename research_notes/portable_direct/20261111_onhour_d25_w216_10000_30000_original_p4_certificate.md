# D25 — Original W216: 503 new target primes, full p^4 digits

Date: 2026-11-11 (Asia/Hong_Kong)
Evidence status: **AUTHOR_SIDE / FINITE_EXACT / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE_H0B0**
Mother objective: ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION
Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT
Publication: TP2-B6F4FC938FF94941C1B7
Frozen science pin: c47e13e4aba0e006366f989d6334d443f6333ae3 (unchanged)
Logical lane: chatgpt-research-onhour-enterprise-math-20260923
Maintenance lane: chatgpt-hourly-enterprise-math-20260921 (excluded)
Checker: research_notes/portable_direct/d25_w216_10000_30000_verify_20261111.py

## Actual new exact finite unit

Prior author's documented original W216 finite p^3 scan ended at p<=10000.
This unit evaluates **every prime 10000<p<=30000 in the frozen classes p mod 24 in {13,19}**, exactly 503 primes, with the **original** signed coefficients

    a_k=(2k)!(3k)!/(216^k(k!)^5),
    W_p=sum_{k=0}^{p-1}(6k+1)a_k.

It evaluates W_p **modulo p^4**, checks W_p==p modulo p^3 on each member, and retains the additional observable

    epsilon_p = ((W_p-p)/p^3) mod p.

All **503** target primes passed the original p^3 condition; none of the 503 has epsilon_p=0. These are exact finite computations, not a proof for unbounded primes and not a statistical claim that a p^4 lift cannot occur. The absence of p^4 extra lifts in this range is only the observed range result.

The first four (p,epsilon_p): (10069,7949), (10093,2413), (10099,3966), (10141,6079).
The last four: (29851,4933), (29917,24002), (29947,4361), (29989,12538).
A full 503-record JSON was materialized by the local checker:
SHA-256 e4d49756cc720bfa361f136cb16758e730f69fef41e93a535ef3bb62c6be017d.
The source checker regenerates every record; the JSON bytes are a local output, not represented as a Source-published/native artifact.

## Why this is an original arithmetic certificate

An exact factorial simplification gives

    a_(k+1)/a_k=(2k+1)(3k+1)(3k+2)/(36(k+1)^3).

For every index 0<=k<p-1 the denominator is a p-unit. Thus the checker obtains all original a_k in Z/p^4 by one exact forward recurrence, preserving the sign-sensitive multiplier 6k+1; it does not use E3, a different g/h series, or a projected Hasse proxy.

Three widely spaced primes 10069, 19531, 29989 were **independently** cross-checked using stripped factorial units:

    v_p(a_k)=floor(2k/p)+floor(3k/p);
    U(n)=prod_{1<=j<=n}(j/p if p|j else j);
    a_k=p^v U(2k)U(3k)/(216^k(k!)^5) modulo p^4.

This is independent of the coefficient recurrence and has the same original coefficients and cutoff. All 3 outputs agreed. The checker regenerates the full raw table in JSON.

## Research outcome and next exact action

New science: precise original signed W216 finite p^4 observations in a nonoverlapping interval beyond the previous <=10000 scan. This supports the p^3 LIFT conjecture on the stated finite set, **does not close the unbounded proof**, and provides reproducible fourth digits for future cancellation/exception hypotheses.

The frozen **highest-priority native benchmark remains NOT_RUN**: same-original-class H0/B0 divided-power [X]U mod 139129 at p=373; actual ring/module rank, semilinear Frobenius direction and eta, odd signed kappa, frozen Delta_p-R_p, raw independent replication. Existing support Issue #1559 remains the responsible path, with no confirmed native executor at the time of this note. A W216 certificate never substitutes for the original native operator.

## Source/authentication boundary

Ordinary-Chat control operation `recovery_status`, payload {}, logical conversation ID as above, had a SUCCEEDED current transport receipt in awdawmip/kimi-query-bridge Issue #6759. It found historical local registration `session-start-20261007-1122-d25-01` FAILED with `UPSTREAM_CODE_REVIEW_REQUIRED`; no own winning CLAIM/open run was exposed. This is **not** the Sites `em_site_control/recovery_status` operation. A fresh exact Source continuation read was requested in Issue #6760; a QUEUED response was visible at draft time. Preserve that original request ID for receipt/reconcile; do not replay a write or infer Source ownership.

GitHub publication/readback, when completed, constitutes author-side evidence preservation only; it does not create a Source-native checkpoint, formal Result, owner assignment or mathematical acceptance. No scheduler was changed.
