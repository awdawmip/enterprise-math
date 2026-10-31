# EC49CB — Exact parity-aware spectral extraction and blocked CRT for signed-X6 BRC

**2026-10-31 · AUTHOR_ANALYTIC_PROOF / EXACT_NATIVE_X6_FINITE_CHECK_PASS / PORTABLE_DRAFT / UNREVIEWED / NOT_ADMITTED.**

Frozen inputs: GLOBAL_KNOWLEDGE_V1 main e60bed072f3bd5702efacf4c54f08a4cd5e54226; Enterprise Math main 9c0243232b458bec8b015f5f9ba57b217f6aeb86; preceding EC49CA at d282085f780d5715e9c61a27be070510028ac97c, PR #1730; unchanged native signed_brc Git Blob 300a96e3dc24bf6fff73743037a0347a8bc83176. P000 startup's original Git Blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc was verified. P000 and ACTIVE worldview remain unmodified. These results concern finite ordered signed-X6 combinatorial BRC paths, not physical heartbeat time, phase cancellation, absolute spatial coordinates or a native two-dimensional plane.

## Exact observer

All length-n ordered words use letters Σ={±E1,...,±E6}; relative displacement d(word)∈Z^6. Let H be any finite sign-preserving permutation subgroup of the six axes, and let δ be a complete DFA on the signed letters. Use a *joint* DFA state recording δ for every h∈H; its state size is q=|Q|^|H|. Fixed-instrument channel h assigns positive integer weights c_(h·a) to letter a. For rational w_a=c_a/D, the original BRC total is its integer numerator divided by D^n. The test case uses H={identity, swap axes 1 and 2}, A=(+E1,+E2), B=(+E2,+E1) substring flags (atoms 00,01,10,11), original positive weights (2,3,3,2,1,1), all negative weights 1; it measures the original, swapped, and unweighted channels.

## Theorem A — finite-field spectral identity and *sharp* no-spatial-alias condition

Let T_h(x) be the q×q Laurent-polynomial transfer matrix with entry
T_h(x)[u,v] = sum over letters a with δ_joint(u,a)=v of c_(h·a)·x^(d(a)).
Let p be prime, L≥1 a divisor of p-1, ω a primitive L-th root in F_p, and e_φ the terminal-state indicator for atom φ. The finite-field root average

S_(h,φ)(n,L;p) = L^(-6) · Σ_(j∈{0,...,L-1}^6) e_(q0)^T · T_h(ω^j1,...,ω^j6)^n · e_φ (mod p)

is exactly the sum modulo p over all ordered length-n paths with atom φ and displacement in (LZ)^6.

**For every even n**, this expression is guaranteed to contain *only zero-displacement words* if and only if
- L is odd and 2L>n; or
- L is even and L>n.

**Proof:** expanding the ordered matrix product gives one monomial x^(d(word)) with its exact ordered path weight and DFA endpoint for each original word. The character orthogonality identity L^(-1) Σ_(j=0)^(L-1) ω^(jm) = 1 if L divides m, and 0 otherwise, selects each displacement component divisible by L. For an even-length signed-axis walk, ||d||_1≤n and Σd_i has even parity. If L is odd and d=Lk≠0, then Σk_i is even, so Σ|k_i|≥2 and ||d||_1≥2L; for even L any nonzero d=Lk has ||d||_1≥L. These inequalities prove sufficiency. Conversely, for odd L with n≥2L, use 2L copies of +E1 plus (n-2L)/2 inverse-axis pairs; for even L with n≥L, use L copies of +E1 plus (n-L)/2 inverse pairs. These legal ordered words have nonzero displacement divisible by L and strictly positive weight, proving sharpness for all words. ∎

For even n, a suitable odd period just larger than n/2 requires around (n/2)^6 frequency points instead of (n+1)^6 under the generic sufficient condition L>n. The evaluation-grid ratio approaches 64, but this is **not** a 64-fold runtime guarantee.

## Theorem B — unambiguous CRT lift

Let B_n denote the native unscreened signed-X6 zero-return BRC numerator endpoint_weight(n,0,c_positive,c_negative). Each terminal-atom numerator F_(h,φ) satisfies 0≤F≤B_n because it sums a positive subset; permuting axes bijects the zero-return paths, preserving the full sum. For pairwise coprime primes p_j≡1(mod L) satisfying the period condition and product M=∏p_j>B_n, root-filter residues reconstruct exactly one integer in [0,B_n] via CRT. Two candidates would differ by a multiple of M with magnitude <M. Dividing by D^n restores rational BRC for rational letter weights. The period/no-alias hypothesis and M>B_n are independent; neither can replace the other. ∎

A streaming spectral algorithm uses O(12·k·|H|·q·n·L^6) modular arithmetic operations and O(|H|·q + L + k·|H|·q) finite-field elements of working storage, apart from prime/CRT overhead. A separate *theoretical* matrix-binary-power variant requires O(k·|H|·L^6·q^3·log n) modular operations and was not benchmarked. Prime selection, primitive-root proof, variable modulus bit lengths and CRT bit costs must be added for bit-complexity claims.

## Theorem C — one traversal of k CRT moduli

A block-DP state has key (t, signed six-vector z, joint DFA state) and k parallel residue vectors, one per modulus. Letter transitions and exact backward-cone pruning are shared; each residue coefficient is separately multiplied and reduced modulo its own p_j. Induction on t proves every component matches the previous separate-prime DP; final CRT results agree. The general modular-arithmetic count remains O(k·|H|·q·n^7) while Python key construction and dispatch are shared. Simultaneous block memory grows with k. No universal speedup is claimed. ∎

## Actually executed finite evidence

A compact standard-library Python checker VERIFY_EC49CB.py was executed and generated EXACT_REPORT_EC49CB.json. It imports the unchanged adjacent EC49CA_CRT/native_signed_brc.py, checks native endpoint_weight and endpoint_multiplicity, all 4×3 atom coordinates, independently implemented spectral and block DP, and explicit wrong-period aliases. Two expanded independent scripts VERIFY_EC49CB_SPECTRAL.py and VERIFY_EC49CB_BLOCK.py were also executed locally with separate JSON reports. Original compact verifier SHA256: 51ba2bbfa8aa11ee06cf49fbbe7670722a956cc7202481d131efd3fa42d8efcf; its generated complete JSON SHA256: 38976ce3524852106441da1ef384aad23679c1ad7a81c852fd85463c79364e14.

| even n | closed paths | native weighted sum | safe odd L | evaluated L^6 roots | peak block states |
|---:|---:|---:|---:|---:|---:|
| 0 | 1 | 1 | 1 | 1 | — |
| 2 | 12 | 24 | 3 | 729 | — |
| 4 | 396 | 1,560 | 3 | 729 | 94 |
| 6 | 19,920 | 152,640 | 5 | 15,625 | 480 |
| 8 | 1,281,420 | 18,921,000 | 5 | 15,625 | 1,874 |

At n=4, the three CRT primes 7·13·19 produce capacity 1,729>1,560. At n=6 and 8, the certified prime 100000081≡1(mod 5) already exceeds B_n. The 4×3 exact per-atom coordinates and modulus selection are preserved in the companion JSON.

**Counterexamples, computed in all three channels:** n=4, L=2 (unsafe even period) gives spectral totals (8,680,8,680,1,536), native totals (1,560,1,560,396), integer excess (7,120,7,120,1,140). n=6, L=3 (unsafe odd period) gives (197,694,197,694,21,132) versus native (152,640,152,640,19,920), excess (45,054,45,054,1,212). In both cases the unrestricted positive weight sum 18^n is less than the 100000081 modulus, so the computed excess is exact, not a modular artifact.

**Measured resource tradeoff:** one instrumented CPython run at n=8 with four small primes: blocked CRT DP 0.266 seconds, four separate modular DPs 1.095 seconds, one exact-integer sparse DP 0.184 seconds; tracemalloc peaks 1.025/0.768/0.490 MB respectively. One uninstrumented n=8 spectral pass at 15,625 roots took ~2.7 seconds. These measurements cover only the stated machine/run and do not establish portability or scaling. The general mathematical statements rely on the proofs, not finite timings.

**Existing literature:** finite-field roots-of-unity filtering, transfer matrices, CRT and NTT are standard. Contemporary NTT implementation examples are Özcan–Javeed–Savaş, IEEE Access (2025), DOI 10.1109/ACCESS.2025.3570024, and Ji et al., ASPLOS (March 2025), DOI 10.1145/3669940.3707241. These papers do not certify this project-specific parity alias lemma or imply its independent novelty.

**Actual authority:** service 0.6.11 em_status on 2026-10-31 returned research_authority_granted=false, registered_session_count=0, executor_binding_configured=false, active job quota 5/5. Live formal owner was not verified; the existing draft PR stores author-side evidence only. No native CLAIM, Result or Driver admission was performed.

**Next EC49CC:** determine valid weighted-DFA group actions on the six-dimensional root grid; prove correct orbit compression or exhibit counterexamples to naive fixed-instrument axis symmetry; validate n=8 and n=10 against native BRC and compare exact resource usage. See NEXT_EC49CC.md.
