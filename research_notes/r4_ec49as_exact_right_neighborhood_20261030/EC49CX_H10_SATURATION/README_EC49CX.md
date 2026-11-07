# EC49CX — h=10 genuine signed-X6 BRC saturation

2026-11-01 Asia/Shanghai · AUTHOR_ANALYTIC_PROOF / EXACT_INTEGER_CERTIFICATE_PASS / PORTABLE_DRAFT / REGISTER_PENDING / UNREVIEWED / NOT_ADMITTED.

## Frozen inputs and status

GLOBAL_KNOWLEDGE_V1 canonical main: 1cea747f65ceda1d892eccbcbb27dcf84dbeadd1 (verified this run).
Enterprise Math canonical main: ac48238d40c28c9ad139faa5b0e11cb7defdd8f9 (verified this run).
Immediate author-side predecessor: EC49CW at PR #1730 commit 3c127f832cedb315ff6a4379afa7cc4248124f2d. Input formal-rank theorem: EC49CS commit 8ccf4816303707e0514f2cb61c7b398da9d3de25. Input lower bound: EC49CU commit a97e2b7625d365b05e0b77dbbcf6d49bfa731c84. P000 projection blob c6d4d2d79b09537bdae55253baef9c28583e44dc matches original P000 blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc. ACTIVE worldview blob 99238c3466eb0805748bae01fd1a20868a5a351e. Protected premises unchanged.

The live native gateway reported research_authority_granted=false and active-owner read returned CONTROL_QUOTA. The results below are author-side independently executable evidence; no Source-native CLAIM, activity, Result, independent Driver review or admission is asserted.

## Exact mathematical carrier and observation

Primitive histories are literal ordered paths of signed ±E1,...,±E6, with all six signed endpoint coordinates retained as displacement relative to a selected cell; they are not final six-nonnegative-integer addresses. Two positive BRC weight vectors on positive letters are W0=(2,3,3,2,1,1) and W1=(3,2,3,2,1,1), with negative-letter weights 1. Channel W2 is exact multiplicity/count. A nine-state deterministic automaton detects ordered adjacent substrings A=(+E1,+E2) and B=(+E2,+E1), outputting four joint terminal tags.

Five complete future operations are:
a=(-E1,-E1), b=(-E2,-E2),
c=(+E1,+E2,-E1,-E2), d=(+E2,+E1,-E2,-E1),
e=(+E3,+E1,+E1,-E3).

For an ordered prefix p and an operation word u, R_(u,t,j)(p) equals the BRC product of the literal concatenation p.u in channel j if all six final displacement coordinates are zero and the terminal A/B tag equals t, and is zero otherwise. Allowed futures have exactly h full operations or 1..h full nonempty operations. The observer is rational-linear and additive over path multisets; order and exact positive-weight semantics are not discarded.

## Theorem at h=10

At h=10 the formal rational observation rank for exactly ten future operations is **1887**. The rank for one through ten operations is **2052**. There are **121** target displacement fibers. At prefix length n=28, every fiber achieves its full formal rank on literal ordered signed-X6 paths. Subject to the already stated EC49CU all-h necessary-bound proof, the first saturated even prefix length is precisely

**n_sat(10)=28=2h+8**.

All greater even prefix lengths also saturate. Odd path lengths cannot reach these even displacement targets.

### Proof of formal upper bounds

Represent each complete suffix word by the pair (six-coordinate net displacement, complete transformation of all nine DFA states). Concatenation composes these signatures exactly. Any two words with equal signatures produce identical terminal-tag indicator rows from every possible initial DFA state. Their positive suffix BRC factors are nonzero and act by scalar multiplication on each independent channel row. Thus signature deduplication preserves the *rational linear* span of observer rows, with no claim that arbitrary ordered paths are equivalent.

A deterministic finite dynamic program computes **547 distinct signatures at depth ten**, instead of enumerating the 5^10=9,765,625 raw operation words, and **602 distinct signatures for depths 1..10**. Exact Fraction elimination on the nine-dimensional tag-indicator rows grouped by full endpoint yields **1887** for depth ten. The cumulative 121 fibers have 21 boundary fibers with four independent DFA rows each and 100 interior fibers with six rows each. Therefore 3*(21*4+100*6)=**2052**. The runnable independent checker recomputes both formal ranks and signature counts, using exact rational arithmetic.

### Proof of the genuine lower bound

The adjacent EC49CX_REPLAY_CERT.json.xz.b64 is a deterministic replay certificate. For each of 121 target fibers it records the independent selected suffix/tag rows, fixed random candidate seed and indices, any necessary *literal* rare-tag paths, and one exact integer determinant residue modulo 1,000,003.

The adjacent Python 3 standard-library-only verifier, VERIFY_EC49CX_GITHUB.py, reconstructs **2052 distinct genuine signed-X6 prefix paths of length 28**. For every path and suffix, it checks all six primitive endpoint coordinates, complete concatenation, the ordered A/B flags, and the two positive BRC products plus count. For each fiber it forms the square integer observation matrix with 3*r rows and 3*r actual paths and recomputes its determinant modulo 1,000,003. **All 121 residues are nonzero**, with minimum 2024 and maximum 995887. Nonzero residue proves a nonzero *integer* determinant, hence linearly independent path columns over Q. Summing gives cumulative rank >=2052, matching the exact formal upper bound. The exact-depth-ten formal observer is a subspace of this cumulative space; injectivity on the entire cumulative space proves its rank 1887 on the same genuine paths.

Randomness is merely a deterministic candidate-path description; each selected literal path and integer determinant is checked. This is a finite exact proof, not a Monte Carlo confidence assertion.

The necessary lower bound n_sat(h)>=2h+8 for h>=4 is inherited from the specific EC49CU author-side argument; the present verifier does not independently re-prove that general lemma. With h=10 it excludes n<28. Prepending the neutral ordered primitive pair (+E3,-E3) preserves all six endpoints and A/B tag history; it multiplies each positive BRC channel by 3 and count by 1, preserving every square-minor nonzero property at length n+2. Even target displacements also rule out odd-length prefixes by parity.

## Exact execution and reproducibility

Run:
    python3 VERIFY_EC49CX_GITHUB.py EC49CX_REPLAY_CERT.json.xz.b64

Actually executed report: {"status":"PASS","h":10,"n":28,"fibers":121,"real_paths":2052,"nonzero_minors":121,"formal_exact":1887,"formal_cumulative":2052,"min_mod_p":2024,"max_mod_p":995887}.

Expected Git blobs (checked against local executed source and local certificate): verifier 9423ec3b007033c9ecbfd1e57f225d44e8ce556e; replay certificate 842e3e351a7ea86bc33426fef2ca7429f590eb40. Local SHA256: verifier 0a9190069732699defad44203e6590436a60065e9f092001b33d3050afa5e85c; certificate 090c74fcb5d476f3309e01419a13bd4cd103fb962da40ca9c0c78d38f5a67fe1.

A separate local literal-matrix implementation also passed all 121 determinant checks. The expanded 2052-path original JSON, actual discovery and rare-tag augment scripts, independent literal verifier, source BRC kernel, and logs are in the full conversation evidence archive. The GitHub replay certificate plus program is independently sufficient to reconstruct and check the complete claimed finite proof.

Scope: exact finite future positive integer BRC and rational-linear additive observers only. This result does not prove signed or complex amplitude cancellation, physical laws, native 3D-slice dynamics, or a fixed-dimensional sufficient state for unbounded future.

## Next scientific unit

EC49CY: test h=11 at n=30 for 144 target fibers, exact-depth formal rank 2256, cumulative rank 2454, with literal nonzero-minor certificates. The all-h sufficiency n_sat(h)=2h+8 remains open: find a simultaneous rowspace-and-genuine-minor h->h+1 construction or the least rigorous counterexample. Neutral pair padding at fixed h does not establish that missing induction.
