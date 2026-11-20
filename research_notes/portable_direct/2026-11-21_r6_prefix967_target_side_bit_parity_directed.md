# PREFIX-967 — Target-side XOR-bit inversion and parity-directed odd-gap quotient fibers

Date: 2026-11-21 (Asia/Shanghai). Status: **AUTHOR_PROOF / EXACT_INTEGER_VERIFIED / NOT_REVIEWED**. Frozen scientific input pin: `f42f2906d77f24085c123f3ccfe9667d41caa96d`.

Research type: auxiliary signed/named integer observer continuing PREFIX-966; no assertion that this constitutes native P000, X6, a BRC theorem, a formal CLAIM, RESULT or an independent review. Source attribution for the prior frontier is historical `EM-DIRECT-58C410`; this note does not claim possession of that identity's live capability.

## Statement and conventions

Let p>=4, H=2^(p-1), Q_p={H+1,H+3,...,2H-1}, and k>=1 odd with k+2<H. We study a,b in Q_p, 0<=i,j,I,J<p, positive quotients t,T and the exact original named equations

    ((k*a) XOR 2^j) - 2^i = t*b,
    (((k+2)*a) XOR 2^J) - 2^I = T*b.

Let m=T-t be a **positive odd integer** (in the adjacent-core gap range, m is 1,3 or 5). Write s=1-2*bit_j(k*a), S=1-2*bit_J((k+2)*a), c=2^i-s*2^j and C=2^I-S*2^J. Distinct numerical residues in D_p have *all* their named (i,j,s) source slots retained.

Previous exact identities are C-c=2a-mb and N=kC-(k+2)c=(2t-km)b, with odd N and odd nonzero d=2t-km.

## Theorem 967.1 — Target-side sign recovery (exact iff, no source-product bit scan required)

For all nonnegative integers x, integers t,b>=1, and source indices i,j>=0, write y=t*b+2^i. Then

    (x XOR 2^j)-2^i=t*b

holds **if and only if** there exists s in {-1,+1} satisfying both

    x=t*b+2^i-s*2^j
    s=2*bit_j(t*b+2^i)-1.

Equivalently, a candidate residual c=2^i-s*2^j obeys its actual sign predicate if and only if

    bit_j(t*b+2^i)=(s+1)/2.

This is an exact dyadic congruence: t*b+2^i (mod 2^(j+1)) belongs to [2^j,2^(j+1)) if s=+1 and to [0,2^j) if s=-1. It is computable on the **quotient target** instead of recalculating bit_j(k*a).

**Proof.** By the original equation x XOR 2^j = y. Let q=bit_j(y). Toggling the j-th bit obeys y XOR 2^j=y+(1-2q)2^j=y-(2q-1)2^j. Thus x=y-s2^j with s=2q-1. Conversely the two displayed identities imply x=y XOR 2^j, hence the original equation. No assumptions about carries outside bit j are needed. QED.

For the second equation replace t,i,j,s by T,I,J,S.

## Theorem 967.2 — Parity-directed residual fiber, with exact halving

In the above odd-core, odd-modulus setting:

    c mod 2 = (1-t) mod 2,
    C mod 2 = (1-t-m) mod 2.

Thus for odd m, **t odd forces (c even, C odd)** and **t even forces (c odd, C even)**. This is stronger than testing only c,C of opposite parity after enumerating both orientations for every quotient.

For p>=3 the established numerical dictionary has |D_p odd|=3p-4 and |D_p even|=(3p^2-11p+18)/2. Therefore the number of admissible numerical residual pairs at **each fixed t** is

    F_p=(3p-4)*(3p^2-11p+18)/2,

and for t=1,...,2k the aggregate exact integer divisibility tests are

    K(p,k)=2k*F_p = k*(3p-4)*(3p^2-11p+18).

In contrast, unconditionally testing both opposite-parity orientations at every t uses 2*K(p,k) tests. The reduction is **exactly 50%** in the tested quotient-residual triples, with no lost numerical or named witness.

**Proof.** Reduce c=ka-tb and C=(k+2)a-(t+m)b modulo two; odd k,a,b give the claimed parities. For each fixed t exactly one orientation is allowed, with F_p possible pairs. The previously proved positive quotient bound 1<=t<=2k applies, so the counts follow. The target-side sign theorem recovers each actual original source slot, and thus both necessity and sufficiency of the candidate reconstruction remain intact. QED.

## Reproduction (exact integer checks)

Program: `PREFIX967_R6_TARGET_BIT_QUOTIENT.py` in the same directory. It independently implements parity-directed numerical residual pairs, integer division for N/d, target-side source-bit checks, reconstruction of all named tuples and the two **raw XOR equations**. Independently, a source-first direct scanner enumerates original XOR source outputs and joins matching endpoint values, *without building the signed residual dictionary*. Comparisons are at the (a,b)->named-multiplicity Counter level.

- Complete direct small-domain comparison: **168 parameter cases** (p=4..7, all odd k with k+2<2^(p-1), m=1,3,5).
- One additional bit-involution microcheck covered y=1..255 and j=0..8 (2,295 exact tests).
- Frozen Q19 p=19,k=21, off-diagonal: m=1 -> 442 distinct ordered pairs / 614 named histories; m=3 -> 839 / 1,286; m=5 -> 3 / 3.
- Per odd gap: **992,796** exact divisibility tests, versus **1,985,592** in PREFIX-966. Per-gap (arithmetic pre-sign candidates, source-sign checks): m=1 (1,419, 3,866), m=3 (2,825, 7,695), m=5 (15, 35).
- The three sorted named-tuple SHA-256 values agree *exactly* with PREFIX-966:
  - m=1: `ccbccc30c4171a809f7270ce59f0b72b368839e93ffeeed8df9ba1045720da71`
  - m=3: `1360a9ca274b357d0b87058d35ef6ccd059d0c5aef995e4d93b0d1363e1aaae3`
  - m=5: `c429ef59749f36ef295b4ac9171fb5171ab3a706beaa270563728d4962649c1b`

A saved result file records every small case and Q19 witness digest. This is an exact reduction in the number of candidate integer divisions, not yet a full wall-clock performance comparison.

## Typed provenance and next scientific unit

A numerical residual c is a quotient **only for the candidate arithmetic filter**. Its complete (i,j,s) slot fiber is retained, and the exact dyadic target-side sign condition is applied before counting any named histories. This is consistent with the project's BRC provenance/nonloss principle, but no BRC interface was run or certified here.

Next: combine the exact target-side dyadic residue constraints with odd-divisor fibers and even-gap resonance; investigate a shared automaton that preserves named-slot multiplicities while amortizing both modulo-2^(j+1) tests and divisor extraction. Benchmark total preprocessing, generation, reconstruction, verification and byte cost rather than only division counts. The mother target B_fix,odd(32) in {19,20} is still open.

Sources: `research_notes/portable_direct/2026-11-20_r6_prefix966_odd_gap_exact_named_inversion.md` and associated `PREFIX966_R6_ODD_GAP_RECONSTRUCT.py`; P000 machine contract `p000_reality_foundation.json`; current normative continuation `docs/RESEARCH_CONTINUATION_PROTOCOL.md#current-normative-context`; prior exact results used only for independent digest comparison, not generating new candidates.
