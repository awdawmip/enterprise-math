# R256 — Periodic 13-adic denominator drop at an exceptional rational parameter

Date: 2026-11-18 (Asia/Shanghai). Status: **AUTHOR_PROVED / EXACT_INTEGER_MODULAR_CERTIFICATE / NOT_REVIEWED**.
Frozen scientific input: \`43ec6098b1330ae86d0a7863be336c5d97f6ef34\`. Direct predecessors: R254 (\`d97f5cb6d3cae6fc35107b605da809a2eb12e5dc\`), R255B (\`6c12b514474d865d3fb8efb940a1b100b14d9208\`).

## Theorem — exact output denominator for every horizon

Work in the same seven-source **positive scalar auxiliary observer**, keeping all 63 distinct source-mask labels. Let \`s=67/169\`, \`t=(1691s-2615)/(2615s-3539)\`, \`a=(1/5,1/4,3/10,9/20,s,2/3,t)\`, \`b_0=13/60\`, and \`b_i=(5/18)|1/2-a_i|\` for \`1<=i<=6\`. Let \`pi_i=b_i/(1-a_i)\`, \`Z=sum_i b_i/(1-a_i)^2\`, \`rho_i=b_i/(Z(1-a_i)^2)\`. For each mask \`0<=m<=62\`, \`D_m={0} union {i+1 : bit_i(m)=1}\` and \`W=(144,576,1440,4320,17280,86400,518400)\`, set

\`h_{m,k}=W_{popcount(m)} sum_{i in D_m} rho_i (P_{D_m}^k 1)_i\`, where \`P_D[i,j]=a_i delta_ij+(1-a_i)pi_j\` for \`i,j in D\` (no renormalization of the restricted \`pi\`).

For every integer **k>=3**, the least common multiple of the 63 reduced rational denominators is exactly

\[
\boxed{\operatorname{lcm}_{m=0}^{62}\operatorname{den}(h_{m,k})=
\frac{J T^k}{K}\begin{cases}
13^{-1},&k\equiv1\pmod{1092},\\
1,&k\not\equiv1\pmod{1092},
\end{cases}}
\]

where \`J=1184397599\`, \`T=989553240\`, \`K=3805974000\`; \`JT^k/K\` is an integer for \`k>=3\`. Thus the first exceptional horizon is **k=1093** (event number \`n=1094\`); the next is \`k=2185\`. The exceptional factor is exactly one power of 13 at every such horizon. This supplies an explicit delayed counterexample to the candidate extension \`lcm den(h)=JT^k/K\` with a constant divisor across all k for this parameter.

## Proof — full finite modular certificate for an infinite statement

For each mask of size d, form the monic characteristic polynomial

\`c_m(x)=prod_{i in D_m}(x-a_i)-sum_{i in D_m} b_i prod_{j in D_m\{i}}(x-a_j)\`.

By R255B and independent coefficient recalculation, \`C_m(y)=T^d c_m(y/T)\` is integral for all 63 masks (249 nonleading coefficients); \`T\` is the minimal joint spectral scaling. Direct rational evaluation yields \`J=lcm_{m,i in D_m} den(W_popcount(m) rho_i)\`, and \`K=JT^3/lcm_m den(h_{m,3})\`. Put \`q_{m,k}=(JT^k/K)h_{m,k}\`. Its first \`d\` entries at \`k=3,...,d+2\` are integers (249 base cases). The Cayley–Hamilton recurrence has characteristic polynomial \`C_m\`, so every \`q_{m,k}\` is integral for \`k>=3\`. Therefore \`D_k=JT^k/K\` is a common denominator for all outputs.

Prime support of \`D_k\` is contained in \`{2,3,5,7,11,13,17,70481,904811}\`. For p in \`{2,3,5,7,70481,904811}\` the indicated mask has \`C_m(y) = y^(d-1)(y-u) (mod p)\`, with \`u != 0\` and all \`d\` starting residues \`q_{m,3},...,q_{m,d+2}\` nonzero. The subsequent sequence is a nonzero geometric progression. Exact witnesses \`(p,mask,u)\` are \`(2,3,1)\`, \`(3,17,1)\`, \`(5,2,2)\`, \`(7,2,2)\`, \`(70481,32,51999)\`, \`(904811,0,624845)\`. For \`p=11\`, mask 4 has a completely nonzero length-10 residue cycle; for \`p=17\`, mask 32 has a completely nonzero length-8 cycle. These secure the full p-adic denominator exponent at every k.

For \`p=13\`, use **all 63** labelled recurrences modulo 13, starting with the exact 249 integer base entries. Each complete state orbit returns to its starting state (no transient), with period distribution: \`39*1, 6*6, 4*12, 2*21, 2*26, 2*28, 8*168\`; the lcm of these periods is 2184. Exhaustive checking of the complete 2184-step joint period shows *all 63* residues are zero precisely at the two positions \`k=1093\` and \`k=2185\` modulo 2184. At every other position at least one of masks \`{9,26,10,13}\` is nonzero modulo 13.

To prove that the loss is exactly **one** factor 13 at the exceptional horizons, lift mask 9's integer recurrence to modulus \`13^2=169\`. Its complete state orbit has period 2184 with no transient, and \`q_{9,1093}=143=13*11 (mod 169)\`, \`q_{9,2185}=26=13*2 (mod 169)\`. The common gcd of the 63 integer numerators thus has 13-adic valuation exactly 1 at those two classes, and 0 elsewhere. Combined with the other prime witnesses, the denominator formula follows for **all** \`k>=3\`. QED.

## Validation, scope and next problem

The companion pure-Python \`R256_periodic_13adic_certificate.py\` reconstructs \`a,b,pi,rho\`, 63 characteristic polynomials, 249 exact integral base cases and all 9 prime arguments, then discovers and checks finite modular orbits. Executed locally with Python standard-library \`Fraction\`: **PASS**; modulo-13 global period 2184, exceptional positions 1093 and 2185; modulus-169 witness \`[143,26]\`. A structured additional evidence record \`R256_verification.json\` was generated using a separate, longer independent certificate with the same theorem and source formulas, also **PASS**.

This exact theorem concerns the fixed scalar positive rational observer and its **labelled** source outputs. It does not identify a native signed/port BRC realization. The frozen scientific input, P000 and ACTIVE worldview were left unchanged. Project mathematical review and native Result/Review admission remain pending; no formal CLAIM is asserted.

**Next question:** characterize the \`p\`-adic output denominator dips for arbitrary rational \`s in (39/100,41/100)\`, including 23-adic exceptional parameters, and determine whether their periods have a structural bound expressible from residue characteristic polynomials rather than complete 63-mask enumeration. Independently, the continuous-parameter 270/403 two-mode threshold question remains open.
