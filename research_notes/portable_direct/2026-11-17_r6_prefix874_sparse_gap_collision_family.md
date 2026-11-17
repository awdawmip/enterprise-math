# PREFIX-874 — Sparse-gap collision certificates for two odd residue ports

Date: 2026-11-17. Researcher: EM-DIRECT-66B43A / TASK_RESEARCH; own Source session MCP-fd0fa1850d90423180438ef799a4c632. Activity RA-8E34353D2E35BF5C339E5DBD. Continuation: PREFIX-873 (all-residue fiber and intrinsic single-port obstruction), PREFIX-872/871 (p=32, B=19 open boundary).
Frozen scientific-input pin: \`f42f2906d77f24085c123f3ccfe9667d41caa96d\` (unchanged).
Status: AUTHOR_PROVED / EXACT_INTEGER_REGRESSION / NOT_INDEPENDENTLY_REVIEWED / NOT_ADMITTED.

## Typed model

The auxiliary named-binary BRC state is \`u=sum_{i=0}^{p-1}2^i x_i\`, with \`x_i in {0,1}\`, \`0<=u<2^p\`. A legal **ordered** transition is \`(u,v)\` with \`v=u\` or \`v=u XOR 2^i\` for exactly one named bit. Two *fixed* odd ports observe
\`Phi(u,v)=(u mod q_1,v mod q_2)\`. Full recovery is injectivity on this complete legal-transition relation. Counts include no-change and both signs of each named toggle; no source or direction is discarded.

This is an auxiliary observer, not the native X6 Cell/Link/Port event model. P000's six native spatial axes, independent time coordinate, and no-native-plane/three-dimensional-slice typing remain unchanged.

## Theorem 874-A (explicit sparse-gap no-go)

Let integers \`B>=3\`, \`p>=B+2\`, \`Q=2^B-1\`. Let \`q_1,q_2\` be distinct **positive odd** integers at most \`Q\`. If their positive difference \`d=|q_1-q_2|\` belongs to
\[
 D_B=\{2^i:1\le i<B\}
 \ \cup\ \{2^i+2^j:1\le j<i<B\}
 \ \cup\ \{2^i-2^j:1\le j<i\le B\},
\]
then \`Phi\` fails to be injective. In every case a collision consists of two *different old states*, separated by the larger modulus, whose new states differ by the smaller modulus. The certificate requires at most two named single-bit toggles (one on each of the two compared transitions), never a multi-bit transition.

**Proof.** By reversal symmetry of the legal transition relation (PREFIX-873-B), take \`a=q_1>b=q_2\` without loss of generality; if the larger port is the second observation port, reverse each witness transition.

Write \`a-b=d\`. All powers below are genuine available named bits because \`i<=B<p\`.

1. \`d=2^i\`. Choose \`u=0\` when bit \`i\` of \`a\` is 1, and \`u=2^i\` otherwise. Then bit \`i\` of \`u+a\` is 1. The two legal ordered transitions are \`A=(u,u)\` (no change) and \`C=(u+a,u+a-2^i)=(u+a,u+b)\` (toggle bit \`i\` down). Their first observed residues agree modulo \`a\` and their second observed residues agree modulo \`b\`.
2. \`d=2^i+2^j\`, \`1<=j<i<B\`. Choose the same \`u\` as in (1). Its bit \`j\` is zero since \`i!=j\`. Therefore the legal transitions \`A=(u,u+2^j)\` (toggle \`j\` up) and \`C=(u+a,u+a-2^i)=(u+a,u+b+2^j)\` (toggle \`i\` down) collide.
3. \`d=2^i-2^j\`, \`1<=j<i<=B\`. Start with \`u=2^j\`. If bit \`i\` of \`a+u\` is zero, replace \`u\` by \`u+2^i\`; otherwise leave it. Since \`i>j\`, bit \`j\` of \`u\` remains one; bit \`i\` of \`u+a\` is one. The legal transitions \`A=(u,u-2^j)\` (toggle \`j\` down) and \`C=(u+a,u+a-2^i)=(u+a,u+b-2^j)\` (toggle \`i\` down) collide.

All old/new states are within \`[0,2^p)\`: \`u<=2^B+2^{B-1}\`, \`u+a<2^{B+2}<=2^p\`; the bit toggles preserve the interval. First residues differ by exactly \`a\`; second residues by exactly \`b\`. The old states are distinct. Time reversal supplies a collision for the other port order. QED.

These witnesses use actual XOR flips with the specified old-bit values; integer addition/subtraction is only a concise way to display each permitted one-bit toggle.

## Theorem 874-B (exact number of arithmetic pair exclusions)

For \`B>=3\`, the distinct eligible positive differences and their sum are
\[
 |D_B|=B^2-3B+3,\qquad
 \sum_{d\in D_B}d=(12B-38)2^{B-2}+16.
\]
Consequently the number of **ordered** positive-odd modulus pairs \`(q_1,q_2)\` with \`q_i<=2^B-1\`, \`q_1!=q_2\` and \`|q_1-q_2|\in D_B\` is exactly
\[
\boxed{\#\mathcal{E}_B=(4B^2-24B+50)2^{B-2}-16.}
\]

**Proof.** The first family consists of \`B-1\` single-one binary numbers. The second consists of \`binom(B-1,2)\` distinct two-one numbers. The last consists of \`binom(B,2)\` runs \`2^j(2^{i-j}-1)\` of consecutive binary ones. Their overlaps are exactly \`B-1\` runs of length one (with the first family) and \`B-2\` runs of length two (with the second family). This gives \`|D_B|\` directly. Summing the powers, the two-power sums and all runs, then subtracting these exact overlaps, yields the displayed value of \`sum d\` by finite geometric-series identities.

For each fixed positive even \`d<2^B\`, exactly \`(2^B-d)/2\` unordered odd pairs have difference \`d\`; both orders are admitted. Sum \`2^B-d\` over \`D_B\` and substitute the two identities. QED.

At \`B=19,p=32\`:
- \`Q=524287\`; \`|D_{19}|=307\`.
- \`sum D_{19}=24,903,696\`.
- **136,052,720 ordered odd-modulus pairs are mathematically excluded** by this explicit two-transition collision family.
- This is a subfamily of the full \`262144^2=68,719,476,736\` ordered odd-modulus pairs; the open \`B_fix,odd(32) in {19,20}\` boundary remains.

Examples independent of the PREFIX-873 extremal list:
- \`(a,b)=(500001,499995)\`, \`d=6=2^3-2^1\`: \`u=10\`, \`A=(10,8)\`, \`C=(500011,500003)\`; \`u'=500011=10+500001\`, \`v'=500003=8+499995\`. Both are legal single-bit-down events.
- \`(a,b)=(524285,524277)\`, \`d=8\`: use case (1) to construct the no-change vs bit-3-down collision.

These are candidate-modulus obstructions, not an enumeration of all potentially invalid pairs. Theorem 874-A also covers non-extremal configurations and non-coprime moduli when their gaps belong to \`D_B\`.

## Exact implementation, coverage and limits

Attached \`PREFIX874_R6_SPARSE_GAP_COLLISION_CHECK.js\` constructs witnesses with integer arithmetic only; the recorded \`PREFIX874_R6_SPARSE_GAP_RESULTS.json\` contains the exact difference count/sum, ordered-pair count and small-domain tests. The same three collision constructions were separately implemented in Python and exhaustively checked for all matching pairs at \`(p,B)=(7,5),(8,6),(9,7)\`: 112, 392, 1,240 unordered configurations respectively; zero invalid certificates. At \`(p,B)=(32,19)\`, every eligible difference has an explicit formula; the program checks 33 representative high-first pairs for each difference, without enumerating 136 million pairs. Their universal coverage is the algebraic proof, not this sample.

A file/readback documents exactly its bytes and content, not independent mathematical review. No claim is made that native X6 dynamics, a formal shared Task CLAIM or mathematical admission follows from this auxiliary BRC observer theorem.

## Next discriminating work

1. Extend the collision family to small integers \`k,l\` in the lattice relation \`k q_1-l q_2 = 2^i\pm2^j\`, with exact bit-feasibility and state-range conditions; this can exclude non-near-diagonal pairs analytically.
2. Combine sparse-gap exclusions with PREFIX-873's all-residue/dual-fiber bounds and intrinsic port obstruction, deduplicating by actual pair rather than adding counts from overlapping tests.
3. Seek either one full valid \`p=32,B=19\` witness or a complete no-go across all admissible odd-modulus pairs.
