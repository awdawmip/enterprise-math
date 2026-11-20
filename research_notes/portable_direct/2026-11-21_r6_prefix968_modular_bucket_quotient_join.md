# PREFIX-968 — Modular-bucket quotient join and parity-forced modulus integrality

Date: 2026-11-21 (Asia/Shanghai). Research mode: independent auxiliary signed/named integer observer. Scientific input frozen at `f42f2906d77f24085c123f3ccfe9667d41caa96d`. Status: **AUTHOR_PROOF / EXACT_INTEGER_VERIFIED / NOT_REVIEWED**.

This continues PREFIX-966/967 without modifying their established named histories, their external auxiliary model, the P000 ontology, BRC native scientific computation, formal X6 ownership, or any Review/Result record. Historical provenance `EM-DIRECT-58C410` is not a claimed live credential or authority for this conversation.

## Exact model

Let `p>=4`, `H=2^(p-1)`, `Q_p={H+1,H+3,...,2H-1}`, and `k>=1` odd with `k+2<H`. The named equations for odd `m=T-t>0` are

```text
((k*a) XOR 2^j) - 2^i = t*b,
(((k+2)*a) XOR 2^J) - 2^I = (t+m)*b.
```

Here `a,b in Q_p`, `1<=t<=2*k`, `0<=i,j,I,J<p`. Define `c=2^i-s*2^j` and `C=2^I-S*2^J` with the source actual-bit sign `s=1-2*bit_j(k*a)` and `S=1-2*bit_J((k+2)*a)`; numerical residuals retain ALL named source slots, including duplicate numerical values.

PREFIX-966/967 proved

```text
C-c = 2a-mb,
N = k*C-(k+2)*c = (2t-km)*b.
```

For fixed `t` the required parity is `c ≡ 1-t (mod 2)`, `C ≡ 1-t-m (mod 2)`, so `c,C` have opposite parity.

## Theorem 968.1: Exact modular-bucket join

Fix `p,k,m,t` as above and write `d=2t-km`. Then `d` is odd and nonzero. Define a dictionary, with full named source fibers attached,

```text
B_d(r) = { (C, sources(C)): C in D_p, C ≡ 1-t-m (mod 2), k*C ≡ r (mod |d|) }.
```

For every `c in D_p` with `c ≡ 1-t (mod 2)`, every numerical pair satisfying `d | kC-(k+2)c` occurs **once** in the finite bucket

```text
C in B_d(((k+2)*c) mod |d|).
```

There are no false negatives and no duplicates of numerical pairs at fixed `t`. This statement requires **no** coprimality of `k` and `d`, no modular inverse, and covers `d=±1` as well as negative `d`. Once joined, set `b=N/d` and `a=(mb+C-c)/2`; retain valid strict p-bit moduli, `a≠b`, and apply the exact target-side XOR-bit sign test separately to *each* named slot.

**Proof.** Divisibility is equivalent to `kC ≡ (k+2)c (mod |d|)`; the bucket exactly stores the full residue fiber of this congruence. Each value of `C` belongs to exactly one bucket. The preceding signed two-core determinant identity supplies the displayed reconstruction. With actual source signs checked, the identities are equivalent to both original named XOR equations. Every named source tuple remains explicit; collapsing numerical values only for candidate generation is lossless for this declared observer because the fibers are re-expanded before named output. QED.

## Theorem 968.2: Automatic oddness of the reconstructed first modulus

Under the same hypotheses, suppose the bucket join produces integer `b=N/d in Q_p`, with `c,C` in the required parity orientations. Then `a=(mb+C-c)/2` is automatically an **odd integer**.

**Proof.** Since `m,b` are odd while `C-c` is odd, `mb+C-c` is even and hence `a` is integral. The identity `N=db` rearranges to `k(mb+C-c)=2(tb+c)`, so `ka=tb+c`. Since `b,k` are odd and `c ≡1-t (mod 2)`, the right side is odd, hence `a` is odd. QED.

The reproducibility script keeps a redundant `a mod 2` assertion/filter for fault detection. In all checked admissible `b` in Q19, the parity predicate passed.

## Calculation and independent checks

Algorithm: for each `t`, construct exactly one residue hash map of the parity-oriented numerical `C` values, then probe it once per parity-oriented `c`. Every emitted candidate satisfies the exact divisibility; validate the reconstructed strict odd moduli, non-diagonal condition, each actual named source slot and the original two XOR equations.

Exact Q19 values (`p=19, k=21`):

| m | Baseline residual-pair divisibility tests | Bucket-selected pairs | Named slot sign predicates | Non-diagonal ordered modulus pairs | Named joint histories |
|---:|---:|---:|---:|---:|---:|
| 1 | 992,796 | 132,661 | 3,866 | 442 | 614 |
| 3 | 992,796 | 134,077 | 7,695 | 839 | 1,286 |
| 5 | 992,796 | 24,996 | 35 | 3 | 3 |
| **Total** | **2,978,388** | **291,734** | **11,596** | **1,284** | **1,903** |

The selected-pair reduction is **90.20497%** against PREFIX-967's all-pairs divisibility loop. Both methods still pay dictionary construction, candidate modulus reconstruction and source-sign checking. There are `10,479` `C` bucket insertions and `10,479` `c` lookups per gap in this Q19 run.

For independent verification, a direct source-first XOR endpoint join (no numerical residual dictionary) matched the new algorithm at the full named-tuple multiplicity level for **168** parameter cases: `p=4..7`, every odd `k` satisfying `k+2<H`, and `m=1,3,5`. Counts by p: 9, 21, 45, 93; summed named tuples by p: 48, 210, 1,007, 3,233. The canonical compact JSON list of these 168 `{p,k,m,count}` cases (sorted-key, compact separators) has SHA-256 `493d98b86bb0393586dbc02185d740b6b09c9ebcae26c69162e5e994ab9bd4f6`.

The Q19 tuple SHA-256 values match the earlier independent PREFIX-966/967 certificates:

- `m=1`: `ccbccc30c4171a809f7270ce59f0b72b368839e93ffeeed8df9ba1045720da71`
- `m=3`: `1360a9ca274b357d0b87058d35ef6ccd059d0c5aef995e4d93b0d1363e1aaae3`
- `m=5`: `c429ef59749f36ef295b4ac9171fb5171ab3a706beaa270563728d4962649c1b`

### Runtime observation (Python 3.13.5, x86_64, same process)

Ten alternated-order repeats per branch gave **median wall times**, including building slot dictionaries, bucket construction / baseline scanning, named recovery and XOR validation:

| m | Bucket join median (s) | Baseline median (s) | Observed median ratio |
|---:|---:|---:|---:|
| 1 | 0.034485 | 0.174982 | 5.074x |
| 3 | 0.036499 | 0.172678 | 4.731x |
| 5 | 0.008737 | 0.167822 | 19.207x |

These are environment-specific Python observations, not an asymptotic speedup theorem or a production engineering benchmark. Worst-case buckets can remain quadratic (notably `|d|=1`). The full proof result is exact candidate equivalence, not timing.

## Reproduce

Run `python PREFIX968_R6_MODULAR_BUCKET_JOIN.py --small` in `research_notes/portable_direct/`. It writes `PREFIX968_R6_EXACT_RESULTS.json`, checks all 168 independent small cases, recomputes all three Q19 tuple hashes and checks the baseline's full named tuples against the bucket join. Run without `--small` for the Q19 comparison alone.

The recorded local full-result JSON has SHA-256 `38f0957948a58a22b4d4fbac8974027e455566db2619de0ba32548252c54aa0f` (run-specific elapsed seconds; this digest is for the actual local run and need not equal a repeat-run output). The executable source as locally run has SHA-256 `5ce90bc2418518a2f226b9b63b3a758c7020d1acc81e0473641a4e8a94e3ac2b`. The committed GitHub script differs only by a blank line in the copied text; its actual immutable file readback is the authoritative remote script byte sequence. Both encode identical operations.

## Limits and next unit

The algorithm is exact for the declared *auxiliary integer XOR observer*, not a proof of an X6 native transformation or typed BRC operation. It does not acquire or change any shared Task claim, native progress, Review or Result. Historical researcher identity is a provenance label; live custody remains to be authenticated.

Open next: measure per-quotient congestion of each modular bucket and compare with odd-divisor-fiber factoring, including preprocessing, memory and source-multiplicity reconstruction; investigate an exact common index across `m=1,3,5` without erasing signed named provenance. The mother question `B_fix,odd(32) in {19,20}` remains open.

Main prior exact sources: `research_notes/portable_direct/2026-11-21_r6_prefix967_target_side_bit_parity_directed.md`, `research_notes/portable_direct/2026-11-20_r6_prefix966_odd_gap_exact_named_inversion.md`, frozen science pin above.