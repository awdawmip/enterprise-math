# D25 — exact first Frobenius-defect repair of the Lucas carrier modulo p²

Date: 2026-10-31 Asia/Hong_Kong. Research mode: AUTHOR-SIDE / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING. This note is portable mathematical evidence and does not establish a service-issued Researcher session, CLAIM, OPEN, native H0/B0 calculation, Result, or Driver acceptance.

Mother objective: ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION. Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7. Frozen science source pin c47e13e4aba0e006366f989d6334d443f6333ae3 (not rebased). P000 remains ACTIVE_LOCKED. This is an **external finite-field/combinatorial** lemma; native X6 geometry is not claimed.

## Consumed frontier and exact question

The prior onhour note at commit `4a473edd23a609d2614c9a5e4318175945cf9ca2` proved a first-digit Lucas factorization for the signed integer port

```text
U_l = sum_{k=0}^{2l} (6k+1)(-1)^k 2^(2l-k)
                         C(3l,k) C(2l,k) C(4l,k).
```

For each p >= 5 prime dividing 6l+1, the first-digit factor equals the original weighted-216 A_p modulo p. The exact all-integer conjecture `(6l+1) | U_l` remains OPEN. Here the **new unfinished unit** was the first power-lift: retaining source and carry information modulo p². The original LIFT target, `A_p = p (mod p³)` for p mod24 in {13,19}, is independently still OPEN.

## Theorem 1: exact two-port binomial lift (proved)

For every prime p >= 5, any nonnegative n = a+pb with 0 <= a < p, and any nonnegative k=c+pd with 0 <= c < p, put

```text
E_p(x) = ((1+x)^p - 1 - x^p)/p
       = sum_{s=1}^{p-1} (C(p,s)/p) x^s             in Z[x],
T_{p,a}(t) = [x^t] (1+x)^a E_p(x),
L_{p,n}(k) = C(a,c) C(b,d),
Q_{p,n}(k) = b [ T_{p,a}(c) C(b-1,d)
                  + T_{p,a}(c+p) C(b-1,d-1) ].
```

Here C(r,s)=0 when s is outside 0..r, T is zero outside its polynomial support, and Q=0 for b=0. The two summands in Q are distinct in-digit and adjacent-digit carry ports. Then

```text
C(n,k) = L_{p,n}(k) + p Q_{p,n}(k)    (mod p²)       (1)
```

for **all** n,k, including carried k digits. Neither binomial quotients nor modular inverses are used.

**Proof.** The polynomial identity `(1+x)^p=1+x^p+p E_p(x)` holds exactly in Z[x], so

```text
(1+x)^(a+pb)
 = (1+x)^a (1+x^p+p E_p(x))^b
 = (1+x)^a (1+x^p)^b
   + pb (1+x)^a (1+x^p)^(b-1) E_p(x)  (mod p²).
```

The first coefficient at x^(c+pd) is L. The polynomial `(1+x)^a E_p(x)` has degree at most a+p-1 < 2p. Hence exactly two possible congruent exponents occur, c and c+p. Their coefficients are precisely Q, giving (1). For b=0 the second term vanishes. QED.

## Theorem 2: source-separated U_l lift (proved)

For s in {3,2,4} let L_s(k)=L_{p,s l}(k), Q_s(k)=Q_{p,s l}(k), and let W_l(k)=(6k+1)(-1)^k 2^(2l-k).

Define the integer source ports

```text
U_l^(0)  = sum_{k=0}^{2l} W_l(k) L_3(k)L_2(k)L_4(k),
U_l^(s)  = sum_{k=0}^{2l} W_l(k) Q_s(k)
                              product_{t in {3,2,4}, t!=s} L_t(k).
```

Then uniformly in every integer l >= 1 and prime p >= 5,

```text
U_l = U_l^(0) + p (U_l^(3)+U_l^(2)+U_l^(4))   (mod p²).    (2)
```

**Proof.** Apply (1) separately to the three original binomial coefficients, multiply in the fixed source order, and discard terms containing at least two first defects because each is divisible by p². The signed weight and all k labels remain unchanged. QED.

This is a BRC `COMPOSE_APPLIED` at the **signed, valuation-labelled, original-index** carrier. Its observer is reduction modulo p², with future operation triple multiplication and weighted summation. First-digit Lucas projection alone loses the three Q_s and their in-digit/adjacent-digit distinction; equation (2) is the exact repair coordinate. Positive total-mass simplification would not preserve these signed cancellations.

## Executed exact certificates and falsifier

Executed the accompanying standard-library Python program, `d25_lucas_p2_carry_20261031.py` (Git blob `50830a74073b04090a1d3020e9f2f97d2163bd86`). It independently checked (1) against exact binomial integers in **9,468** (p,n,k) coefficient cases across p=5,7,11,13,17,19, and checked (2) against direct integer U_l for ten prime-square-divisor probes plus additional higher-digit and single-divisor probes. All arithmetic was exact, no floating point.

If p² | (6l+1), the following are observed source ports. Listed U^(s) values are reduced mod p and U^(0) is reduced mod p²:

| p | l | U^(0) mod p² | (U^(3),U^(2),U^(4)) mod p | U_l mod p² |
|---:|---:|---:|---:|---:|
|5|4|20|(0,0,1)|0|
|7|8|21|(1,5,5)|0|
|11|20|77|(4,2,9)|0|
|13|28|0|(0,0,0)|0|
|17|48|0|(0,0,0)|0|
|19|60|0|(0,0,0)|0|
|23|88|0|(0,0,0)|0|
|29|140|812|(17,17,25)|0|
|31|160|930|(18,0,14)|0|
|37|228|0|(0,0,0)|0|

**Essential carry witness.** At p=5,l=4, the zero-defect integer carrier is 20 (mod25), not zero. The uniquely nonzero defect source is the 4l binomial factor, and (2) gives `20+5*(0+0+1)=25=0 (mod25)`. At p=29,l=140, `812+29*(17+17+25)=2523=0 (mod841)`. Discarding Q_s is an invalid prime-square lift even though ordinary mod-p Lucas is valid.

**Exact counterexamples to a stronger false premise.** A single p factor in N=6l+1 does *not* imply p² | U_l: `U_2 mod 13²=143` and `U_3 mod 19²=171`. This cleanly distinguishes the full composite conjecture, which requires p^e divisibility only when p^e | N, from an unjustified square divisibility assertion for any p|N.

These finite instances are exact computational witnesses; (1) and (2) are universal proved identities. No universal theorem `p² | U_l if p² | 6l+1` is claimed, and no bridge from this auxiliary congruence to the original second-digit LIFT has been proved.

## Canonical execution and next mathematical action

On 2026-10-31 the read-only Site gateway 0.6.11 reports `research_authority_granted=false`, `executor_binding_configured=false`, `source_sync.control.state=CODE_REVIEW_REQUIRED`, and `control_quota.active_jobs=5/5`. Client-scoped `checkpoint_get/list` returned `ACCESS_DENIED`. These reads establish no own Source session/CLAIM/run. The original onhour dispatch `research-onhour-20261031-0205-dispatch-r15` in bridge issue #6633 has a recorded failure; no equivalent mutation was replayed. No maintenance conversation identity was used.

Exact original fixed-p373 native H0/B0 scientific benchmark support stays with existing enterprise-math issue #1559, OPEN and requiring an actual executor for `[X]U mod139129`, original module rank, semilinear Frobenius and eta, signed odd Green/Hesse, kappa, and independent validation. This binomial program does not execute or replace that benchmark.

The smallest new prime-square follow-up is to evaluate the right side of (2) under `6l+1=0 mod p²` for general higher base-p digits and prove cancellation or find a precise counterexample. In parallel, the highest original scientific obligation remains proving the frozen signed `C01+F2+I_p=0 (mod p)` (equivalently Delta_p-R_p=0) in both target classes; consume already proved three-stratum jets and the two-wall Clausen operators, not a new first-digit proof. All Source claims/checkpoints require genuine current authority and receipt.

Status: PROVED UNIVERSAL p² DIGIT DEFECT / EXECUTED EXACT CHECK / COMPOSITE CONJECTURE OPEN / ORIGINAL LIFT OPEN / AUTHOR-SIDE / UNREVIEWED / NOT_ADMITTED.
