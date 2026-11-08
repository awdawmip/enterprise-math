# D25: original W216 grade-zero Legendre–Clausen deformation with two exact p-adic jets

Date: 2026-11-09 (Asia/Hong_Kong). Status: **AUTHOR_SIDE_EXACT_IDENTITY_DERIVED / EXACT_18_PRIME_CHECK / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE**.
Task: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`, publication `TP2-B6F4FC938FF94941C1B7`, frozen scientific pin `c47e13e4aba0e006366f989d6334d443f6333ae3`. Logical Research lane `chatgpt-research-onhour-enterprise-math-20260923`, never the maintenance lane `chatgpt-hourly-enterprise-math-20260921`. The result is an author-side portable proof, not Source CLAIM / Result / native H0/B0.

## Original model and local unfinished question

For primes p=6m+1>3 the original W216 coefficient and signed weight are, unchanged,

[
W_p=sum_{n=0}^{p-1}(6n+1)rac{inom{2n}{n}^{2}inom{3n}{n}}{216^n},
qquad
W_{0,p}=sum_{n=0}^{2m}(6n+1)rac{inom{2n}{n}^{2}inom{3n}{n}}{216^n}.
]

The accompanying original V2304 sum is
[
V_p=sum_{n=0}^{p-1}(8n+1)rac{inom{4n}{2n}inom{2n}{n}^{2}}{2304^n}.
]
The known source-port equivalence reduces the frozen p=13,19 mod24 target to W_p=V_p modp³. Earlier exact grade1/grade2 notes already reduce the unfinished third digit to a source-preserving cross-grade cancellation. Here we replace the largest unexpanded W grade0 component by a terminating classical polynomial and two explicit finite harmonic moments.

## Theorem 1: universal terminating deformation through p³

Fix p=6m+1>3, N=2m and q=p³. Set

[
R_n=rac{(1/2)_n(-N)_n(N+1)_n}{2^n(n!)^3},qquad
a_r=(r+1/3)(r+2/3),qquad
z=rac{p(p+1)}9,
]

and the two finite harmonic observations

[
h_n=sum_{r=0}^{n-1} a_r^{-1}, qquad
h^{(2)}_n=sum_{r=0}^{n-1} a_r^{-2},quad h_0=h_0^{(2)}=0.
]

Define source-labeled terminating moments
[
F_0=sum_{n=0}^{N}(6n+1)R_n,quad
F_1=sum_{n=0}^{N}(6n+1)R_nh_n,quad
F_2=sum_{n=0}^{N}(6n+1)R_nleft(h_n^2+h_n^{(2)}ight).
]

**For every prime p=6m+1>3,**
[
oxed{W_{0,p}equiv F_0+z F_1+rac{z^2}{2} F_2 pmod{p^3}.}
]

Proof. The ordinary W coefficient has exact hypergeometric identity
[
rac{inom{2n}{n}^{2}inom{3n}{n}}{216^n}
 =rac{(1/2)_n(1/3)_n(2/3)_n}{2^n(n!)^3}.
]
Since N=(p-1)/3, the terminated parameters satisfy -N=1/3-p/3, N+1=2/3+p/3. Thus for every r,
[
(r-N)(r+N+1)=(r+1/3-p/3)(r+2/3+p/3)
=(r+1/3)(r+2/3)-p(p+1)/9=a_r-z.
]
For n≤N, every a_r (r<n) and every factorial/2^n denominator are units modulo p: the least zero of 3r+1 or 3r+2 occurs at r=N, outside the product. Therefore
[
prod_{r<n}a_r=prod_{r<n}(a_r-z)prod_{r<n}(1-z/a_r)^{-1}.
]
The multiplicative inverse-product expansion is
[
prod_{r<n}(1-z/a_r)^{-1}
=1+zh_n+rac{z^2}{2}left(h_n^2+h_n^{(2)}ight)+O(z^3)
]
in (mathbb Z_{(p)}), and z is divisible by p. Multiply by R_n and the original signed weight (6n+1), sum n=0..N, and reduce modulo p³. This proves the stated theorem with no change of model or cutoff.

## Theorem 2: Legendre evaluation of F0

Let P_N(x) be the classical Legendre polynomial, and set s=1/sqrt(2) in the quadratic extension of (mathbb Q), noting that the expression below is rational for even N. The classical terminating Clausen identity and Legendre quadratic transformation give the exact finite polynomial identity
[
sum_{n=0}^{N}
rac{(1/2)_n(-N)_n(N+1)_n}{(n!)^3}t^n
=P_N(sqrt{1-t})^2.
]

Indeed, Clausen's formula with a=-N/2, b=(N+1)/2 and a+b=1/2 identifies the left {}_3F_2 with the square of {}_2F_1(a,b;1;t); the latter is P_N(sqrt(1-t)) by the Legendre quadratic transformation. For N even both expressions are polynomials, so the identities hold over (mathbb Q[t]) without analytic limiting arguments. Apply the exact weighted operator (1+6trac{d}{dt}) and evaluate at t=1/2 to obtain
[
oxed{F_0=P_{2m}(s)^2-rac3s P_{2m}(s)P_{2m}'(s)
=P_{2m}(1/sqrt2)^2-3sqrt2,P_{2m}(1/sqrt2)P_{2m}'(1/sqrt2).}
]
As N=2m even, P_N(s) is rational and P_N'(s) is s times a rational number. All the Legendre recurrences' divisors n+1 in 1..N are p-units, proving this expression's legitimate reduction modulo p³.

## Exact interaction with the existing frozen third-digit certificate

Preserve the earlier author-side exact grade1 jet (pK_1(S_0+pS_1)), grade2 companion (p^2K_2S_2), and published Guo–Zudilin V half/full congruence. The original unsolved p³ cancellation is equivalently
[
oxed{
Xi_p:=
F_0+zF_1+rac{z^2}{2}F_2
-V_{mathrm{half},p}
+pK_1(S_0+pS_1)+p^2K_2S_2
equiv0pmod{p^3}.}
]
This is a precise equivalent reformulation under those existing results, not a proof that Xi vanishes for arbitrary target p. The Legendre polynomial replaces the original W grade0, while the source-labelled deformation jets and grade1/grade2 channels remain present. BRC/provenance retention is applied: no residual or sign channel is silently collapsed.

## Executed exact calculation

The saved Python reproducer independently evaluates: (i) original W0 from integer `math.comb`; (ii) terminating R_n and both inverse-factor moment sums by exact modular recurrences; (iii) Legendre P_N and P_N' by the usual exact integer-coefficient three-term recurrence in (mathbb Z/p^3), representing s via s²=1/2. All identity checks passed at
p=7,13,19,31,37,43,61,67,73,97,109,127,157,163,193,211,229,373.

At p=373, m=62, N=124, q=51895117,
[
F_0=18377337,quad
z=40378369,quad F_1=37546395,quad F_2=8792857pmod q.
]
Thus (zF_1=8325733), (z^2F_2/2=1391290), and
[
18377337+8325733+1391290=28094360=W_{0,373}pmod{51895117}.
]
The separately computed Legendre expression equals F0=18377337 exactly modq.
All values use modular exact arithmetic, no floats. The computation verifies the statement in the indicated finite cases; the all-prime formulas have the algebraic derivations given above.

Program: `research_notes/portable_direct/d25_original_w216_terminating_legendre_20261109.py`.
Machine result: `research_notes/portable_direct/d25_original_w216_terminating_legendre_compact_20261109.json`.

## The next decisive mathematical and native actions

Use this Legendre–Clausen base and first two moments to seek a nontrivial terminating transformation / Fricke or creative-telescoping certificate which cancels the *combined* source-labelled (Xi_p) across both target classes, with the earlier (Theta_p) observer unchanged. Reuse the already proved grade1/grade2 formulas instead of appending unrelated auxiliary models.

Native same-original-class H0/B0 divided-power ([X]Umod139129) at p373 still requires actual module rank, semilinear orientation/eta, signed kappa and Delta-R, with independent verification; existing support issue #1559 is OPEN and has no verified executor. The historical Researcher `EM-ENTERPRISE-4DEB43` and activity `RA-9553E027FD14223807511263` are provenance only: current private session capability is absent and no current winning CLAIM, open run or native Source checkpoint has been verified.

**Status: AUTHOR_SIDE_DERIVED / EXACT_18_PRIME_CHECK / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE.**
