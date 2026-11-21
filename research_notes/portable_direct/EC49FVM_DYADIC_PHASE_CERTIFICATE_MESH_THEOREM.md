# EC49FVM — Sharp-scale dyadic mesh of excluded rational phases

Date: 2026-11-21 (Asia/Shanghai)
Scientific status: AUTHOR_PROVED / EXACT_MODULAR_CERTIFICATE / PARENT_DEPENDENT / NOT_REVIEWED / NOT_ADMITTED

## Frozen source and mother problem

This is an independent portable-research continuation of EC49FVL, at exact research pin BRC16943. The load-bearing science comes from:
- awdawmip/enterprise-math@34284e2c73c711c3ae80e53e762051b76c01b6cd, EC49FVJ_FOUR_PRIME_PROJECTIVE_PHASE_THEOREM.md and EC49FVJ_FOUR_PRIME_PROJECTIVE_PHASE_VERIFY.py;
- awdawmip/enterprise-math@a35947428af2e1b440d2f48dca0495b2ae3b757a, EC49FVL_ANGULAR_EQUIDISTRIBUTION_THEOREM.md.

The question concerns the rational-phase scalar readout t(x)=log R(x)/log S(x) of the frozen derived Bernoulli observer for rational x in (0,1). Nothing here changes its exact inputs, P000, the ACTIVE X6 Heartbeat World, the Source firewall, a shared task claim, Result, Review, or the pending FUQ/FUR compound-minimax transfer. This proof uses exact modular integers only for an already frozen observer; it asserts no native heartbeat dynamics or physical ontology.

EC49FVL established uniform local *proportions* of four-prime excluded phases for intervals whose widths w_H obey H w_H / log H -> infinity. Our new theorem concerns a DIFFERENT property, namely existence of a certified excluded fraction in every interval at the sharper width O(1/H). We do not deduce the 90.4687% local proportion at that width.

## Theorem — explicit all-interval mesh at optimal scale 1/H

Let S_H denote the reduced rational phases 0<h/k<1, k<=H, which are ruled out for EVERY rational observer width x by at least one of the four exact projective finite-prime certificates (11,17,19,31) from EC49FVJ.

For all integers H>=128, every interval I within [0,1] whose length is strictly greater than 20/H contains an element of S_H.

Specifically let j=floor(log_2 H), k=2^j, and define
  D_j = {h/k : 1<=h<k, h mod 110 belongs to A_j},
where A_j consists of the odd residues r in {1,3,...,109} for which the p=11 projective certificate holds on the exponent pair (r,2^j-r) modulo 110.

Then D_j is a subset of S_H, every element has reduced denominator exactly k, and every consecutive gap in the ordered set D_j union {0,1} is at most 10/k, hence strictly less than 20/H.

More precisely, for EVERY real half-open I=[a,b) within [0,1], w=b-a, and every j>=7:
  # (D_j intersect I) = (2/11)*2^j*w + E_j(I),
with |E_j(I)|<=20, uniformly in interval placement. Consequently for moving intervals I_H of width w_H with H*w_H -> infinity, the number of members of this single-denominator certified subfamily in I_H goes to infinity uniformly in placement.

The scale O(1/H) is sharp for an all-interval nonemptiness theorem for rational numbers with denominators <=H: no such positive rational belongs to the interval (0,1/H).

## Proof: one-prime projective mask and a 20-state exponent cycle

Use the *unchanged* exact observer constants
  U = 4822040484 / 8132285009,
  gamma = 141024 / 1653649,
  La(z) = (637-3z)/637,
  Lb(z) = U*(1+gamma*z),
  a(z) = 1-(1-z)*La(z),
  b(z) = 1-(1-z)*Lb(z).

If the phase were t(x)=h/(h+n), then the necessary rational polynomial relation from EC49FVJ would vanish:
  H_{h,n}(z) = [a(z)^h La(z)^n - b(z)^h Lb(z)^n] / [La(z)-Lb(z)].

The quotient is a polynomial by the common boundary value at the unique finite collision; projective homogenization also supplies a point at infinity. If its reduction mod p has no zero anywhere on P^1(F_p), the polynomial has no rational root (including rational denominators divisible by p), so t(x) cannot equal h/(h+n).

At p=11, the unique finite coincidence is z=3 with a=b=La=Lb=10 mod 11. The divided-difference value at z=3 is nonzero exactly when 9h+10n is nonzero mod 11. At the other ten projective points, the quotient is evaluated exactly modulo 11. For positive h,n the nonzero-base powers depend on h,n mod 10 and zero bases vanish for all positive exponents; thus the entire projective no-zero predicate depends only on (h,n) mod 110.

For any j>=1, define the twenty-candidate mask A_j as in the theorem. The exact enumerator in the companion Python code checks the singular point, all nonsingular finite points, and projective infinity. For each j=1,...,20:
  (i) A_j contains EXACTLY 20 odd residues modulo 110;
  (ii) the cyclic maximum gap between successive residues of A_j, including the wraparound, equals 10;
  (iii) the compact modular mask equals direct divided-difference/projective evaluation for every odd residue at positive representative exponents.

The period in j is exactly bounded by 20, since 2^20 = 1 mod 55 and both 2^j and 2^(j+20) are even, so 2^(j+20)=2^j mod 110. The finite verification of twenty exponent classes is exhaustive for ALL j>=1. This is a finite-field *certificate for an infinite theorem*, not an extrapolation from bounded numerical testing.

Fix j>=7. Each h in the mask is odd, so gcd(h,2^j)=1. The pair (h,2^j-h) shares its full mod-110 predicate with a verified element of A_j and hence satisfies the exact p=11 no-zero criterion. Therefore every member of D_j lies in S_H.

The union of the twenty progressions r+110Z, r in A_j, has consecutive integer gaps <=10. Because k>=128>110, restriction to 0<h<k leaves both endpoint gaps and all internal gaps <=10 (the residues on one circular period bound the partial end segments). Dividing by k proves the mesh bound 10/k. If k is the largest power of two not exceeding H, then k>H/2, so 10/k<20/H; any interval strictly longer than 20/H must meet this certified mesh.

For the finite-height count, each of the twenty residue progressions has its count in [ak,bk) differing from wk/110 by at most 1. Summing gives the stated (20/110)=2/11 factor and |E_j(I)|<=20. The width-H conclusion follows from k>H/2. Finally, any positive fraction h/k with k<=H satisfies h/k>=1/H; the empty endpoint interval proves order optimality. QED.

## Reproduction and verified finite scope

EC49FVM_DYADIC_MESH_VERIFY.py uses only Python standard-library Fraction, modular exponentiation, and integers. It rebuilds the p=11 observer, checks the unique singular point and exact 44 nonsingular exponent-base patterns, evaluates ALL j=1..20 and 55 odd numerator residues (1100 direct homogeneous/projective crosschecks), checks the 20 certified residues and cyclic max gap 10 for each j, and verifies dyadic whole-numerator gaps for j=7..18 and rational interval-count identities at j=7,8,9,10,12.

Selected exact outputs:
- j=7, denominator 128, 24 certified numerators, largest gap 10;
- j=8, denominator 256, 45 certified numerators, largest gap 10;
- j=9, denominator 512, 93 certified numerators, largest gap 10;
- j=10, denominator 1024, 187 certified numerators, largest gap 10.
The independent output file records all twenty period states and terminal ALL PASS. The infinite conclusion uses the finite complete period and the preceding proof, not bounded enumeration.

## Scientific interpretation and further work

The prior four-prime asymptotic certificate density δ=36018427/39813120 concerns reduced phases averaged over ALL denominators k<=H. This new dyadic construction uses just ONE denominator k=2^j, where p=11 already certifies 20 of 55 possible odd residue classes: 4/11 of reduced numerators asymptotically along the dyadic denominator sequence. It proves uniform SUPPORT coverage at the optimal 1/H scale, rather than δ-density at that scale.

Open: can the 20/H support constant be improved by combining masks or denominators? Can a uniform δ-proportion theorem extend from w_H >> log H/H down toward w_H >> 1/H? Are any of the remaining uncertified rational phases actually attained by rational observer widths? FUQ/FUR compound-minimax transfer and independent mathematical review remain unresolved.

This is an author-level, reproducible, independent portable scientific artifact; do not interpret GitHub publication as an authenticated CLAIM, formal Result, or accepted Review.
