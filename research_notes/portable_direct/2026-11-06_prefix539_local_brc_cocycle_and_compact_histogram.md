# PREFIX-539 — Nonnegative local BRC cocycle and compact histogram experiment

Date: 2026-11-06 Asia/Shanghai. Line: RS-X6-NATIVE-ROTATION-DYNAMICS. Frozen scientific input: enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d. Independent author derivation, unreviewed and not admitted. This note follows PREFIX-538.

## New theorem: BRC as a local additive 0/1 cocycle

In the four-STAR directed X6 model, there are 48 phases, 144 legal directed phase edges and two labeled INNER/OUTER choices per step. Define sigma(i) as +1/-1 if phase i points along the first signed axis, or 0 otherwise; let epsilon(i)=|sigma(i)|. For any rooted legal path i_0,...,i_d, set r=sigma(i_0). For any legal directed edge i->j define

    tau_r(i,j)=[epsilon(i)+epsilon(j)-|sigma(j)-r|+|sigma(i)-r|]/2.

**Theorem.** For each r in {-1,0,+1} and every legal edge, tau_r(i,j) belongs to {0,1}. At every depth d>=0, the signed first-axis BRC cancellation number satisfies

    p_1(i_0,...,i_d) = sum_{k=0}^{d-1} tau_r(i_k,i_{k+1}).

**Proof.** A signed first-axis phase is followed by a non-first-axis phase under the frozen directed transition table. Consequently, for r=0, tau equals epsilon(i); for r=+1, it is one exactly when sigma(i)=-1 or sigma(j)=+1; for r=-1, it is one exactly when sigma(i)=+1 or sigma(j)=-1. In all other legal cases it is zero. The assertions cover all signs of adjacent legal phases. Telescoping the definition gives

    sum tau = [K - |sigma(i_d)-r| + |sigma(i_0)-r|]/2,
    K=sum_{k=0}^{d-1}[epsilon(i_k)+epsilon(i_{k+1})].

Since sigma(i_0)=r, this is exactly the frozen BRC endpoint formula (K-|sigma(i_d)-sigma(i_0)|)/2. The empty path gives zero. QED.

This makes the chosen BRC observable a nonnegative *local* edge-weight sum after remembering only the initial sign seed r; it is an exact statement at arbitrary finite depth within this frozen model.

## Exact three-seed recurrence

Let T=(A,+L1,-L3) be the frozen aAc gate phase and b the previous microstep INNER bit. Let F_d^r(i,b;q,z) count all d-step futures with factor q^tau on each edge and factor z on an INNER step arriving at T iff the prior bit was INNER. With F_0^r(i,b)=1,

    F_{d+1}^r(i,b) =
       sum_{j in NEXT(i)} q^tau_r(i,j)
          [ F_d^r(j,0) + z^[b=1 and j=T] F_d^r(j,1) ].

For any root s with sigma(s)=r, the exact rooted joint polynomial P_s(d;q,z) equals F_d^r(s,0;q,z). This follows by partitioning the two microstep choices and using the theorem. Three shared runs suffice for all 48 rooted joint polynomials. Unlike the 49-coordinate rank-one lift, this direct recurrence uses only nonnegative polynomial coefficients, with 96 phase/last-INNER states per sign seed.

Root outputs obey PREFIX-538's sharp support: 0<=h<=floor((d+2)/4), h<=p<=floor((d+1)/3). The prototype uses padded rectangular arrays in intermediate non-root seed/phase states, checking the exact sharp support upon root extraction.

## Exact execution and benchmark

The attached executable Python certificate (stored as gzip to reduce Git storage) implements three independent approaches: (1) the new three-seed dense cocycle, (2) the PREFIX-537 three-seed sparse 49-coordinate lift, (3) forward raw labeled-phase counting with signed-axis K and gate memory. Each method returns full Z[q,z] coefficient dictionaries for all 48 roots and every depth through the target.

All methods agreed at depths 0..8, 0..16 and 0..20 (432, 816 and 1008 root/depth polynomial equalities). The cocycle was checked for all 144 edges and three sign seeds (432 exact cases). Exact integer assertions passed, status ALL_CHECKS_PASS.

CPython, same process, tracemalloc enabled for all methods, gc before each measurement, **one run** per method and depth:

| Target depth | Dense cocycle | Sparse rank-one | Raw forward | Sharp root candidate slots | Actual max nonzero |
|--:|--:|--:|--:|--:|--:|
| 8 | 0.471987s | 0.066220s | 0.374348s | 9 | 9 |
| 16 | 1.586392s | 0.310723s | 3.408775s | 20 | 20 |
| 20 | 2.053769s | 0.522365s | 5.382802s | 33 | 32 |

At depth 20, peak traced memory was 1,948,620 / 1,891,764 / 1,855,168 bytes for dense/sparse/raw respectively. These single-run performance readings diagnose this implementation; the sparse rank-one lift was fastest at these depths. The new contribution is a positive additive BRC law, an independent exact implementation and a measured dense-allocation cost.

**Reproduction:** Save the adjacent PREFIX539_compact_cocycle_benchmark.py.gz, then run `gzip -d PREFIX539_compact_cocycle_benchmark.py.gz` followed by `python PREFIX539_compact_cocycle_benchmark.py`. It writes PREFIX539_EXACT_BENCHMARK_SUMMARY.json; the adjacent published JSON is the recorded execution output. Standard Python library only.

## Next: PREFIX-540

Pack only reachable intermediate supports for the new 0/1 cocycle; keep separate padded bounds for non-root phases. Benchmark repeated runs and memory against the sparse 49-coordinate lift. Assess whether the proven 26 observation classes lower extraction costs while preserving original labeled Cell/provenance data for future operations.

Source: PREFIX-537 c9f20aa52a0f55441e0c94bf4b4ce9b1ef6ba44a; PREFIX-538 310fb44e1fb07ef7d74914f2f5913f18a9afc4ed. No formal CLAIM, independent review or Foundation admission has been asserted.
