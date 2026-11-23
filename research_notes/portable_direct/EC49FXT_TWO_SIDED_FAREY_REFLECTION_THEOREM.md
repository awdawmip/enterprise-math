# EC49FXT — Two-sided Farey/C11 reflection, sharp seven-miss law and nearest certified fractions

Date: 2026-11-23 Asia/Shanghai. Frozen scientific pin: **BRC16943** (unchanged).
Scientific status: **AUTHOR_PROVED / EXACT_FINITE_CROSSCHECK / PARENT_DEPENDENT / NOT_REVIEWED**.
Scope: exact scalar rational-anchor Farey/CRT observer; a typed native Heartbeat-X6 transition has not yet been established.

## Frozen input and genuine anchor branches

Parent: awdawmip/enterprise-math@95507f064ee46910b32e26d1c49e6df4a05b84fc:research_notes/portable_direct/EC49FWS_FAREY_ONE_HOLE_FIBER_OBSERVER_THEOREM.md and EC49FWS_FAREY_FACTOR_PROBE_VERIFY.py. Frozen P10 50-word census: EC49FWQ_BLIND_FACTOR_FULL_SUPPORT_PROBES_THEOREM.md@d091c8f2757f67c18be8056ae976b1e092a21098.

The true frozen certificate is C11(h,n) = P10(h mod10,n mod10) AND (9h+10n nonzero mod11). The P10 predicate is the four parity/projective-slope SLOPES dictionary in the companion script, not an interpolated mask. Its slope and parity are invariant under simultaneous negation, hence C11(-h,-n)=C11(h,n).

Fix any coprime 0<a<b and put q=a/b. Let e be the inverse of a modulo b, represented in {1,...,b-1}. Define the two canonical determinant-one bases:

    d_minus=e;   h_minus=(a*e-1)/b;          n_minus=d_minus-h_minus
    d_plus=b-e;  h_plus=(a*(b-e)+1)/b;      n_plus=d_plus-h_plus

They satisfy h_minus+h_plus=a, n_minus+n_plus=b-a, d_minus+d_plus=b. For sign sigma∈{-1,+1}, define X_sigma(t)=(h_sigma+a*t,n_sigma+(b-a)*t), t≥0. The determinant b*h_sigma(t)-a*(h_sigma(t)+n_sigma(t)) equals sigma. Both coordinates are positive for all t≥1. Write w_sigma(t)=1_C11(X_sigma(t)).

## Theorem A — genuine right branch by one reflected left trace

For every integer s, as complete 110-periodic words,

    w_plus(s) = w_minus(-1-s).

The identity separately holds for the frozen P10 ten-bit factor and for the full/single-hole eleven-bit factor. When the left origin is rephased by u (the EC49FWS origin X_minus(u+t)), the right word satisfies

    w_plus(s)=w_minus_rephased(-u-1-s).

Proof: the base equalities imply X_plus(s)=-X_minus(-1-s) componentwise. C11 is centrally symmetric. Rephasing is exact substitution. Thus the right trace is fixed by the actual anchor, the left trace and the origin offset. The signed branch, anchor and height remain necessary for the corresponding rational successor readout.

## Theorem B — sharp uniform seven-miss bound

Every frozen product trace U(t mod10)*V(t mod11), with U one of the original 50 ten-bit words and V full or missing exactly one of eleven residues, has at most **7 consecutive zero positions**, including across the end of its 110-period. This finite bound is **sharp for genuine rational anchors**, not just the enlarged product population.

Proof by complete finite enumeration of the fixed input: regenerate P10 from its 44-residue formula, enumerate 72 primitive mod10 directions and their determinant-minus-one affine cycles, deduplicate to the exact 50 distinct U words, then enumerate all 12 genuine permitted V factors and all 110 residue positions. The accompanying standard-library Python program performs these steps and exact cyclic-gap comparison with assertions. All 600 instances are covered; their maximal-zero-run histogram is:

    length 1: 6; 2: 44; 3: 148; 4: 202; 5: 134; 6: 44; 7: 22.

Exactly the masks U=23 and U=833, each with any of the 11 holes, attain 7. For full V, the worst case is 5. The enumeration is a small exhaustive finite proof component, not sampling. FWS supplies the independent reduction that all genuine anchor traces lie inside this 600-instance family.

For the actual anchor a/b=3/7, both canonical branch traces attain seven missing consecutive times. The seven-step bound is therefore globally sharp on actual anchors.

## Theorem C — exact two-sided certified neighbor and sharp height loss

Let H be an integer with H≥16b. For each branch, set T_sigma=floor((H-d_sigma)/b), and let t_sigma be the largest nonnegative t≤T_sigma with C11(X_sigma(t)) true. Then both exist, t_sigma≥1, and

    0≤T_sigma-t_sigma≤7,
    H-(8b-1)≤D_sigma=d_sigma+b*t_sigma≤H.

Among all fractions h/(h+n) on the same strict side of a/b, with h,n positive integers, h+n≤H and C11(h,n), the **unique nearest** certified fractions are

    L(H) = (h_minus+a*t_minus)/D_minus,
    R(H) = (h_plus+a*t_plus)/D_plus.

Proof: the seven-zero lemma gives a C11 hit among the last eight candidate indices, each positive because T_sigma≥8. Its deficit is at most (b-1)+7b=8b-1. For any fraction on either strict side of the anchor, the integer |b*h-a*(h+n)|≥1; the signed determinant-one branch minimizes numerator and distance equals 1/(bD). Within that branch the largest denominator is closest. Every competing fraction with determinant magnitude ≥2 has gap ≥2/(bH); the selected denominator satisfies D_sigma≥H-8b+1>H/2 at H≥16b, so the selected distance 1/(bD_sigma)<2/(bH). This proves genuine nearestness across *all* certified fractions, not merely affine-branch candidates.

The signed approximation errors and paired cross-determinant are exact:

    a/b-L(H) = 1/(b D_minus)
    R(H)-a/b = 1/(b D_plus)
    R(H)-L(H) = (t_minus+t_plus+1)/(D_minus D_plus)
    h_plus(t_plus)*D_minus - h_minus(t_minus)*D_plus = t_minus+t_plus+1.

Sharp genuine-anchor witness: at a/b=3/7 and H=1096, the left selected t_minus=148 gives L=446/1041 and H-D_minus=55=8b-1; the right t_plus=153 gives R=460/1073. Direct integer cross-determinant equals 302=148+153+1. Therefore the uniform integer denominator-deficit constant is optimal.

## Verification and provenance

Independent local execution of the companion Python script returned ALL PASS: 72 primitive directions, 50 ten-bit masks, 600 full/one-hole products, 110 residue positions per product, 7 genuine anchor cases with 110 left/right reflection checks each, and the sharp 3/7 height witness. All comparisons use exact integer arithmetic. The rational-anchor trace is a valid upper model for a native project only with a further typed X6 observer/transition bridge. Existing P000, ACTIVE worldview and frozen input are unchanged. No formal Task CLAIM, Result or independent Review is asserted by publication.

## Next question

Derive which (phase, support color, missing column, anchor, determinant branch, height) tuples are *jointly reachable* in actual indexed-spectrum pair comparisons, rather than treating support and missing column independently. Use this to sharpen or refute the universal-fixed-probe budgets in EC49FWS and EC49FXP–FXS on the genuine correlated anchor family. For Heartbeat X6, retain six-axis signed cell, BRC route, anchor and time provenance; prove observer/future-operation fiber constancy before erasing any coordinate.
