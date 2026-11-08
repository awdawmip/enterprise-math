# D25 original 216/2304 fourth-digit boundary: exact grade-3 companions and sharpness witness

Date: 2026-11-09. Classification: AUTHOR_SIDE_PROVED_IDENTITIES / EXACT_FINITE_WITNESS / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE.
Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT. Publication: TP2-B6F4FC938FF94941C1B7. Frozen scientific source pin: c47e13e4aba0e006366f989d6334d443f6333ae3.
This is a portable scientific increment for the original signed 216/2304 finite sums. It grants no current native CLAIM, run, checkpoint or review status.

## 1. Original coefficients and grade definition

For every prime p=6m+1>3 define, unchanged from the frozen input,

W_p = sum_{n=0}^{p-1} (6n+1) C(2n,n)^2 C(3n,n) / 216^n,
V_p = sum_{n=0}^{p-1} (8n+1) C(4n,2n) C(2n,n)^2 / 2304^n.

Define coefficient-grades before applying signed weights:
g_W(n)=floor(2n/p)+floor(3n/p), g_V(n)=floor(4n/p), 0<=n<p.
The equalities follow from Legendre's formula for factorial valuations, since n<p and 4(p-1)<p^2. All denominators 216,2304 are p-units. Denote W_i and V_i the source-labeled sums of terms with grade i. For p=6m+1 the W blocks are n=0..2m, 2m+1..3m, 3m+1..4m, 4m+1..6m, with grades 0,1,2,3 respectively. V_i uses floor(4n/p)=i.

## 2. Theorem: original W third-valuation grade, all p=6m+1>3

Put n_W=4m+1 and define the rising-factorial finite sum

S_W3 = sum_{j=0}^{2m-1} (6j+3) (5/6)_j (2/3)_j (1)_j / ( 2^j (4/3)_j^3 ) mod p.

Set K_W3 = -2 (2m+1)! / ((4m+1)!)^5 * 216^{-(4m+1)} mod p.
Then the **exact universal coefficient-grade formula** is

W_3 / p^3 = K_W3 S_W3 (mod p).

Proof. The first coefficient in this grade has index n_W, where 2n_W=p+(2m+1), 3n_W=2p+1 and n_W<p. Divide (2n_W)!(3n_W)!/n_W!^5 by p^3. The unit factorial congruence U((kp+r)!)=(-1)^k k!r! (mod p) gives the prefactor K_W3. The exact next-term ratio of the unweighted original W coefficient is
[(2n+1)(2n+2)(3n+1)(3n+2)(3n+3)]/[216(n+1)^5].
At n=n_W+j, reducing mod p yields
[(j+5/6)(j+2/3)(j+1)]/[2(j+4/3)^3].
The signed original weight 6(n_W+j)+1 equals 4p+6j+3. Multiply ratios for j from 0 to 2m-1. Every (4/3+r) with 0<=r<=2m-2 is a p-unit. This proves the stated formula.

## 3. Theorem: original V third-valuation grade, all p=6m+1>3

Let epsilon=p mod 4 in {1,3}, s=(p-epsilon)/4, n_V=(3p+epsilon)/4=3s+epsilon.
Set
K_V3 = -6 epsilon! / ((n_V)!)^4 * 2304^{-n_V} mod p,
S_V3 = sum_{j=0}^{s-1} (8j+2epsilon+1)
 [( (epsilon+1)/4 )_j ( (epsilon+2)/4 )_j ( (epsilon+3)/4 )_j]
 / [ 9^j ( (epsilon+4)/4 )_j^3 ] mod p.

Then V_3/p^3 = K_V3 S_V3 (mod p).

Proof. As 4n_V=3p+epsilon, the unit factorial formula gives
(4n_V)!/(p^3(n_V!)^4)=-6 epsilon!/(n_V!)^4 mod p.
The unweighted original V term ratio is
[(4n+1)(4n+2)(4n+3)(4n+4)]/[2304(n+1)^4].
For n=n_V+j it reduces to (1/9) times the product of the three listed shifted numerator parameters divided by the cube of the listed denominator parameter. The original signed weight reduces to 8j+2epsilon+1. The denominator is a p-unit for 0<=j<s. Multiply the s ratios; the formula follows.

## 4. Exact p=373 sharpness witness for the original target

p=373, m=62, p^3=51895117, p^4=19356878641.
Independent integer-binomial and p-adic unit-factorial implementations give
W_373=11832087049 (mod 19356878641),
V_373=5916043711 (mod 19356878641),
W_373-V_373=5916043338=114*51895117 (mod 19356878641).

Thus W_373=V_373 (mod 373^3) but **W_373 is not V_373 modulo 373^4**.
This is an exact counterexample to a universal fourth-digit strengthening, not to the frozen third-digit conjecture.

The grade-3 companion observations are
K_W3=277, S_W3=238, K_W3*S_W3=278 (mod373);
K_V3=288, S_V3=297, K_V3*S_V3=119 (mod373).

The complete p^4 grade vectors (grade 0,1,2,3) are:
W=(17724329257,8808962706,9585709842,14426842526),
V=(252649685,6701296366,12143457378,6175518923), each entry mod p^4.

The BRC/source-preserving fourth-digit carrier divides into:
L=[W_0+W_1+W_2-(V_0+V_1)]/p^3=189 (mod373);
W_3/p^3=278;
(V_2+V_3)/p^3=353 (of which V_2/p^3=234, V_3/p^3=119).
Hence 189+278-353=114 mod373. These divisions are valid at p373 by direct exact check, with the V tail's general p^3 divisibility available independently from Guo-Zudilin's V half/full theorem.

## 5. Independent exact computation and scope

The attached checker computes *every original summand* via two different exact paths: (i) Python integer binomial coefficients; (ii) p-adic factorial units and Legendre valuations. It separately checks both grade-3 hypergeometric companions, the source grade sums, and the p^3 cancellation before division.

18 exact tested primes: 7,13,19,31,37,43,61,67,73,97,109,127,157,163,193,211,229,373.
The normalized fourth-digit discrepancy (W_p-V_p)/p^3 mod p is respectively
4,11,6,11,28,31,34,61,23,94,43,119,154,68,173,96,119,114.
All 18 values are nonzero. The counterexample already follows from p=373 (or p=13), while the two companion identities hold for every p=6m+1>3 by the algebraic proofs above. A finite screen does not determine an all-prime nonvanishing law.

## 6. Mother objective / recovery

The mother objective remains the original all-prime third-digit congruence Delta_p-R_p=0 (mod p), equivalently W_p-V_p=0 (mod p^3), for p=13,19 (mod24) under the earlier exact source crosswalk. Previous D25 precision-three grade1 jet and Theta_p=B_p+(K1 mod p)S1+K2S2 are unchanged and not recomputed as new results. The fourth-digit witness identifies the exact strength to target and leaves the finite-field cross-grade Theta identity as the smallest unfinished all-prime proof obligation.

Separate native hard target: the original p=373 H0/B0 divided-power [X]U mod 139129, its rank, semilinear orientation/eta, signed kappa, original Delta-R and independent reproduction, tracked by existing #1559 without an established executor. No ordinary W/V calculation replaces that native experiment.
Historical Source researcher EM-ENTERPRISE-4DEB43/session MCP-ecbfd1c046864bb3bff1a2e04c87d207 is provenance; the current private execution capability and winning CLAIM are not verified. Historical continuation request onhour11-20261108-2202-current-task-continuation was SUCCEEDED and was consumed by read, not resent.

Next exact portable action: attempt a terminating creative-telescoping / Fricke identity annihilating the source-labeled Theta triple modulo p across both target classes; test candidate at p373 first, preserving original weights, summation limits and units. The newly proved grade3 companions may be used as boundary diagnostic, not as surrogate native evidence.
