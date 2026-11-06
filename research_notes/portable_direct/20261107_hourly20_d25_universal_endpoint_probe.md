# D25: Universal endpoint-sequence observer, sparse roots and labelled collision

Date: 2026-11-07 (Asia/Hong_Kong). Author-side portable result: UNREVIEWED / NOT_ADMITTED / NOT_NATIVE_CHECKPOINT.
Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7; frozen scientific pin c47e13e4aba0e006366f989d6334d443f6333ae3 (unchanged). Prior author-side frontier: research_notes/portable_direct/20261107_hourly20_d25_top_jet_moment_universality.md.

## Theorem 1 — universal rational endpoint sequences

Let p=6m+1 >=7 be prime. Put a=2m, b=3m, c=4m and define the original labelled finite-field observer

    P_m(z) = sum_{j=0}^b (6j+1)(-1/2)^j binom(b,j) binom(a+z,j) binom(c+z,j).

For each integer t>=0 define rational numbers, independent of p,

    E_t(eps) = sum_{j=0}^t (6j+1) binom(2j,j)/8^j * binom(t,j) * binom(t+eps/3,j),
    eps = -1 or +1.

For **every integer 0<=t<p**:

    P_m(t-a) == E_t(-1) (mod p),    P_m(t-c) == E_t(+1) (mod p).

All denominators on the right are p-units. Consequently either single universal rational sequence, after an index shift and reduction, supplies the complete p-point function-value table of P_m.

Proof: In F_p, b=-1/2, c-a=-1/3 and a-c=+1/3. For j<p the polynomial binomial binom(x,j) respects reduction because j! is invertible. The identity (-1/2)^j binom(-1/2,j)=binom(2j,j)/8^j then converts each term. At z=t-a or z=t-c, one varying binomial becomes binom(t,j), which is zero for j>t. Extending the finite sum beyond j=b to j=t is valid, even for t>b, since binom(-1/2,j)=binom(b,j)=0 (mod p) when b<j<p. QED.

This observer reparametrization retains the provenance of its three labelled factors in the proof; the resulting scalar E_t alone is not a source-faithful state.

## Theorem 2 — exact endpoint-sequence moments and tangent representation

Let chi=(2/p). Reuse the previously proved top-coefficient identities for P_m:

    sum_{z in F_p} P_m(z)    = -2chi,
    sum_{z in F_p} z P_m(z)  = chi/2.

Since a=-1/3 and c=-2/3 modulo p, Theorem 1 gives the four universal finite-sequence congruences:

    sum_{t=0}^{p-1} E_t(-1)   = -2chi;
    sum_{t=0}^{p-1} t E_t(-1) = (7/6)chi;
    sum_{t=0}^{p-1} E_t(+1)   = -2chi;
    sum_{t=0}^{p-1} t E_t(+1) = (11/6)chi      (mod p).

From the already proved finite-field inverse moment for deg(P_m)=p-1 we obtain two new equivalent forms of the *open* exterior tangent:

    T_{1,p}+T_{3,p} = [z]P_m(z)
      = -sum_{0<=t<p, t != a} E_t(-1)/(t-a)
      = -sum_{0<=t<p, t != c} E_t(+1)/(t-c)     (mod p).

The equality is proved; the conjectured zero of these sums remains open. This representation suggests a creative-telescoping relation in the sequence index t while retaining the head/carry decomposition as the independent provenance observer.

## Theorem 3 — sparse exact modular roots

The explicit rational samples are

    E_7(+1) = 34753223537 / 13436928,
    E_8(+1) = 208260224932279 / 27518828544,
    E_8(-1) = 32361249364675 / 6115295232.

Numerator divisibility, unit denominators, and Theorem 1 give certified roots:

| prime p | t | eps | z modulo p | required original terms |
| ---: | ---: | ---: | ---: | ---: |
| 31 | 7 | +1 | 18 | 8 |
| 31 | 8 | +1 | 19 | 9 |
| 357681673 | 8 | -1 | 238454457 | 9 |
| 516774751693 | 8 | +1 | 172258250573 | 9 |

All these p are prime, congruent 1 mod 6, and exceed t. The modular original-source sums were independently evaluated over the t+1 nonzero terms. For p=516774751693, b+1=258387375847, while the exact special-input root certificate requires nine terms. This is a bounded-cost sparse input evaluation, not a claim of general-p generic evaluation speed.

### BRC provenance/collision witness

At p=31, (a,b,c)=(10,15,20). The two distinct states z=18 and z=19 have equal scalar total P_5(18)=P_5(19)=0 (mod 31). The labelled weighted j=1 source port

    V_1(z) = 7(-1/2) b(a+z)(c+z)

satisfies V_1(18)=2 and V_1(19)=3 (mod31). Thus the scalar total has a two-state zero fibre resolved by retaining one labelled port. Input carrier: the three source-tagged integer binomial factors and their signed j weights. Observer: total mod 31. Future operation tested: read the labelled j=1 port. BRC reuse decision: COMPOSE_APPLIED.

## Executed validation and continuity

An exact Python stdlib checker evaluated both endpoint identities for **every field argument** for primes 7,13,19,31,37,43,61 (211 original field inputs, two endpoint tables), independently formed [z]P_m from the original factor products, checked all four global moments, verified the four sparse-root certificates and deterministic 64-bit primality, and checked the distinct j=1 ports at p=31. All assertions passed on 2026-11-07. Portable script: d25_universal_endpoint_sequences_20261107.py. This is author-side finite-field evidence, awaiting independent review. Original H0/B0 (p=373), eta/kappa, Frobenius and the mother objective remain open.

**Next executable scientific unit:** derive a rational recurrence or a WZ certificate in t for E_t(+1)/(t-c), explicitly preserving t=0, t=p-1 and the omitted pole t=c, and compare resulting boundary terms to the labelled A_m-B_m head/carry tangent expression. A second question is whether a recurrence controls common prime divisors of consecutive E_t(+1) numerators, as seen for p=31 at t=7,8.

## Original native-control boundary (2026-11-07)

The Site gateway's local status reported CONFIGURED_NOT_LIVE_VERIFIED; backend_connected=false, pinned backend 0.6.11. Calls to em_status and receipts for original requests em-h20-20261106-1324-d25-task-r13 and em-h20-20261106-1324-d25-cont-r13 failed with BACKEND_IDENTITY_OR_VERSION_MISMATCH, operation_sent=false. Existing session/claim/run/staging are unknown, not empty. No session close/start, claim, open, publish_checkpoint, freeze, or duplicate request mutation occurred. CONTROL_PLANE_MAINTENANCE owns the existing support issue #1558. Acceptance: a live Site-bound backend read with identity/version verified; reconcile original requests and protected staging; obtain a lawful successor Researcher and winning claim/run; Source-backed checkpoint as current contract permits.
