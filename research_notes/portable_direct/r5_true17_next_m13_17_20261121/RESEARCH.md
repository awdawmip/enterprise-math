# R5 — Genuine-event primitive-17 next Laurent residue at five cancelled thresholds

Date: 2026-11-21. Scientific status: AUTHOR_EXACT_FINITE_DERIVATION / TWO_EXACT_IMPLEMENTATIONS_AGREE / NOT_REVIEWED. This is independent portable research, not a native CLAIM, REVIEW, accepted Task Result, or alteration of P000. The frozen R5 scalar input is retained: 256 hypotheses, 101 integer price variables p=214,...,314, original five failure events. The preceding genuine-incidence correction is immutable enterprise-math@5aefe382332056f38cf942775097bf09afbcbb58, and its original audit is @75d986aa23b68a7ecf9b29dc1006f0e322b35a15. Historical provenance EM-DIRECT-4C3E47; current native execution identity and activity write binding unconfirmed. The present calculation is locally executed by the current worker and has no claimed independent review.

## Scientific statement: five finite thresholds

Write F_m(q)=sum_{N>=0} f_m(N)q^N for the cost count under the original **union of individual events** E_i={sum_{p in S_i} a_p<m}, with all a_p nonnegative, and S0={214,...,218}, S1={214,216,...,221}, S2={215,...,221}, S3={223,...,290}, S4={296,...,312}. Let ζ be a primitive 17th root of unity. For each m in {13,14,15,16,17}, F_m(q) has a pole of **exact order five** at every primitive 17th root. Thus the cost count has a nonzero primitive-17 Fourier contribution of order N^4, and any coefficient-quasipolynomial representation valid modulo O_m(N^3) has coefficient period divisible by 17.

This is a finite five-threshold result. An infinite extension to all m congruent to 13,...,17 modulo 17 remains open.

## Exact computation and derivation

Let C(q)=prod_{p=214}^{314}(1-q^p)^(-1). For a nonempty event mask I, let U_I=union_{i in I} S_i and let P_I(q) be the **finite** generating polynomial summing q^(sum p*a_p) over all nonnegative a_p on U_I satisfying the individual inequalities for every i in I. Define R_I(q)=P_I(q) prod_{p in U_I}(1-q^p). Genuine inclusion-exclusion gives F_m(q)=C(q)R_m(q), R_m=sum_{I≠∅}(-1)^(|I|+1)R_I(q).

Exactly six prices are multiples of 17: M17={221,238,255,272,289,306}. If I includes E3, its root pole order is at most two, so its R_I vanishes to order at least four at ζ and does not affect the first or second Laurent orders. Let A=E0∪E1∪E2. Since E4 uses disjoint variables, the relevant analytic factor is R_A+R4-R_A R4.

For the five specified m, exact finite state enumeration shows R_A(ζ)=0. Also R4(ζ)=0 because 306∈S4. Put D=q d/dq. Then D R_m(ζ)=D R_A(ζ)+D R4(ζ) (terms from E3 and cross product vanish).

The 17 successive prices of S4 represent each residue modulo 17 exactly once. Hence
    prod_{p in S4}(1-ζ^p t)=1-t^17,
so the bounded complete homogeneous sum for at most m-1<17 selected price copies satisfies P4(ζ)=1. As prod_{r=1}^{16}(1-ζ^r)=17 and 306 is the unique S4 multiple of 17,
    D R4(ζ)=-306*17=-5202.

Direct **per-event load-state DP** (not an invalid union-cardinality collapse) computes D R_A(ζ) exactly in Z[ζ]/Φ17. An independent grouped h_u/h_v computation using x=a214,y=a215,u=a216+a217+a218,v=a219+a220+a221 reproduces all five results. The two routines use different state decompositions and agree on the full 16-coordinate field vector.

In the basis (1,ζ,...,ζ^15), D R_m(ζ) has first coordinates:

| m | coordinate 0 | coordinate 1 | zero vector? |
|---|---:|---:|---|
| 13 | -13328 | -8840 | no |
| 14 | -6681 | 6171 | no |
| 15 | -7565 | 1105 | no |
| 16 | -12631 | -8602 | no |
| 17 | -4046 | 9724 | no |

All full exact vectors are preserved in RESULT_PRIMITIVE17_NEXT_M13_17.json. The field representation uses ζ^17=1 and Φ17(ζ)=1+ζ+...+ζ^16=0; a reduced 16-vector is zero exactly when all components are zero. Every displayed vector is nonzero.

Let x=1-q/ζ. Since C(q)=K17(ζ)x^(-6)(1+O(x)) with
    K17(ζ)=[prod_{p in M17}p * prod_{p not in M17}(1-ζ^p)]^(-1) ≠0,
and R_m(ζ)=0, R_m(q)=-x D R_m(ζ)+O(x^2), it follows that
    F_m(q)= -K17(ζ) D R_m(ζ) x^(-5) + O(x^(-4)).
The nonzero Laurent coefficient gives a nonzero N^4 term for the primitive 17th Fourier mode. Cyclotomic conjugacy extends the statement from a chosen primitive ζ to every such root.

## Verification and limits

VERIFY_PRIMITIVE17_NEXT_M13_17.py is a standalone standard-library exact-load-state enumerator. A second locally executed method groups the three-price blocks by complete-homogeneous polynomials; the complete local evidence files are included in the accompanying handoff package, and their compared vectors were equal for m=13,...,17. Both compute integer polynomials modulo z^17-1 and reduce at the end modulo Φ17, so no floating point or rounding occurs. The finite checked set is exactly {13,14,15,16,17}; there is no independent mathematical review or formal Source Task acceptance.

This finding does not reinstate the falsified prior four-class minimum-period formula at O_m(N^4). It instead resolves a missing **next order** for these five thresholds under the real joint incidence. The remaining scientific objective is to derive a rational m-generating function for D R_m(ζ) on the primitive-17 leading-cancellation classes, establish or refute global nonvanishing, then combine the corrected lower Laurent orders at 11 and 13 and relevant higher roots to determine the actual complete minimum-period classification.

## BRC / observer interpretation

This is a scalar auxiliary Fourier model, not a native Heartbeat X6 evolution calculation. The observer is whether any of three individual loads crosses m. Collapsing the joint load state to a union-cardinality scalar is not sufficient for that observer; preserving the load vector (or the proven sufficient minimum h) is the appropriate residual carrier. Cyclotomic amplitudes are signed/complex and are never reinterpreted as positive BRC mass. P000 and the native three-dimensional-slice distinctions are unchanged.
