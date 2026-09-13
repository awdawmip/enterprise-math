# RSA-270 continuation: pin the public generation prior and halve the 3-adic recovery depth

Status: `RESEARCH NOTE / SOURCE PIN + EXACT ALGORITHMIC REDUCTION / NOT CANONICAL PROMOTION`  
Researcher-ID: `EM-DIRECT-66DE45`  
Research mode: `TASK_RESEARCH`  
At: `2026-09-08T00:42:00+08:00`  
Parents:
- `research_notes/RSA270_3ADIC_BRANCH_ORACLE_EQUIVALENCE_20260906.md`
- `research_notes/RSA270_CARTIER_FINITE_STATE_NOGO_20260908.md`

No RSA-270 factor is obtained.

## 1. The former P000/H2 dependency can now be pinned to the original RSA Challenge record

The archived RSA Factoring Challenge list distributed by the RSA Challenge Administrator (list dated 1994, archived mail header 1997) explicitly states that every decimal-labelled RSA challenge number was generated as the product of two randomly chosen primes of approximately the same length and that **both primes were chosen congruent to 2 modulo 3**, for use with public exponent 3.

The same original list contains RSA-270 itself.

Primary archived source:

`https://www.ontko.com/pub/rayo/primes/rsa_fact.html`

Relevant generation statement: lines 35--45 in the archived list; RSA-270 appears at line 91.

Therefore, for RSA-270, the prior used throughout the corrected 3-adic line is not a speculative hidden-factor assumption:

`H2: p ≡ q ≡ 2 (mod 3)`

is documented challenge-generation metadata.

This repairs the provenance gap identified in the review of PR #1330. The mathematical conclusions must still state H2 explicitly, but the source is now pinned.

## 2. The previous e=282 stopping criterion was unnecessarily strong

The prior branch-oracle note used the sufficient condition

`M_E=2*3^E > sqrt(N)`

so that a recovered factor residue modulo `M_E` equals the factor itself as an ordinary integer. For RSA-270 this gave `E=282` and at most 281 successive branch decisions from e=2.

That is correct but far from optimal.

A classical Coppersmith/Howgrave-Graham divisor-in-residue-class result gives a stronger stopping rule.

Coppersmith, Howgrave-Graham and Nagaraj, *Divisors in residue classes, constructively*, Mathematics of Computation 77 (2008), 531--545, construct all divisors of n in a known residue class

`d ≡ r (mod s)`

when `gcd(r,s)=1` and

`s >= n^alpha` for `alpha>1/4`.

Thus once a nontrivial factor p of N is known modulo a modulus M satisfying

`M > N^(1/4)`,

p can be recovered by the constructive residue-class factor algorithm. This is the arbitrary-modulus analogue of the familiar Coppersmith 'half the bits of one balanced RSA prime' result.

Here `M=2*3^E` is coprime to RSA-270's factors, so the condition applies directly. Because the 3-adic decoder produces an unordered residue pair, run the residue-class construction on the at most two final residue representatives.

## 3. Exact RSA-270 cutoff

For RSA-270,

`N = 233108530344407544527637656910680524145619812480305449042948611968495918245135782867888369318577116418213919268572658314913060672626911354027609793166341626693946596196427744273886601876896313468704059066746903123910748277606548649151920812699309766587514735456594993207`.

It has 895 bits.

The exact minimal E satisfying

`(2*3^E)^4 > N`

is

`E=141`.

Indeed:

`2*3^140 = 12531574964355940758512448388683860664413388893621330549719196101602`

and

`(2*3^140)^4 < N`,

while

`2*3^141 = 37594724893067822275537345166051581993240166680863991649157588304806`

and

`(2*3^141)^4 > N`.

Numerically,

`log2(N)/4 ~= 223.7049`,

`log2(2*3^140) ~= 222.8948`,

`log2(2*3^141) ~= 224.4797`.

Therefore the corrected conditional factorization chain is

`H2 metadata`
` -> recover factor residues mod 2*3^e one ternary lift at a time`
` -> reach e=141`
` -> apply constructive divisor-in-residue-class / Coppersmith method`
` -> factor N`.

Starting with the known H2 base modulo 6 and first unresolved level e=2, the number of branch decisions required is at most

`141-2+1 = 140`.

This halves the previous 281-decision bound.

## 4. Scope and significance

This does **not** make the branch oracle N-only computable. The hard step remains exactly the same: obtain the required 2--4 local BRC residue-flow traces at each level without first knowing the factor packet.

What changes is the target depth and information budget:

- old direct-residue target: about `sqrt(N)`, e=282;
- corrected Coppersmith target: just above `N^(1/4)`, e=141.

So any future N-only trace evaluator needs only about half as many successful ternary lifts as previously recorded.

This is particularly relevant after the finite-state no-go: although the global faithful coefficient sequence cannot have a fixed finite ternary state, an **adaptive 140-step sparse branch-decoder** is still a logically open route.

## 5. Updated preferred target

Do not seek full 3-adic factor recovery to e=282.

Seek an N-only evaluator for the adaptive 2--4 trace branch selector through at most e=141. At that point hand off to the classical residue-class/Coppersmith recovery algorithm.
