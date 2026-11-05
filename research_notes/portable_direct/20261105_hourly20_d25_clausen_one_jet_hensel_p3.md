# D25 — Clausen one-jet curvature reduction for the p-adic Hensel zero

Date: 2026-11-05 (+08); TASK_RESEARCH, portable author-side proof. Task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`, publication `TP2-B6F4FC938FF94941C1B7`. Scientific input pin remains `c47e13e4aba0e006366f989d6334d443f6333ae3`. Evidence: AUTHOR-PROVED algebra with 94 exact finite checks; UNREVIEWED / NOT_ADMITTED / NOT_NATIVE_CM.

## New theorem: exact first-jet derivative and two universal curvatures

Let `p=6n+1>=7` be prime. Over `Z_(p)` define the terminating polynomial
[
G(z)={}_2F_1(-n,-2n;1-p/2;z),qquad L(z)=G(z)+12zG'(z),qquad Psi(z)=G(z)L(z).
]
All denominator factors for the degree-`n` polynomial are p-adic units. At `x=1/2`, put `g=G(x)`, `v=G'(x)`, and `f=g(g+6v)`. Then **without any first-digit hypothesis**, the following is an *exact* identity in `Z_(p)`:
[
oxed{Psi'(x)=A:=6v^2+(8+6p)gv+rac43(p-1)^2g^2.}
]
Moreover,
[
oxed{rac12Psi''(x)equiv B_0:=rac49(5g^2+24gv+9v^2)pmod p.}
]

Assume the first-digit premise `f=Psi(x)≡0 (mod p)`. From the already proved simple-root/unique-factor theorem for this precise polynomial, `A` is a unit, and exactly one of `g≡0` and `g+6v≡0` holds mod `p`. The curvature quotient has **universal, branch-dependent values**:
[
oxed{rac{Psi''(x)/2}{Psi'(x)}
equiv
egin{cases}
2/3 &(gequiv0),\
10/3 &(g+6vequiv0)
end{cases}pmod p.}
]
Consequently, writing `d=f/A`, the unique Hensel zero `x_p ≡ 1/2 (mod p)` satisfies the **one-jet-only** formula
[
oxed{x_pequiv	frac12-d-cd^2pmod{p^3},quad
c=2/3	ext{ on the }G	ext{ branch, }c=10/3	ext{ on the }L	ext{ branch}.}
]
The input readout for this formula is only `(p,g,v,branch)` modulo `p^3`; no computed `G''`, `G'''` or separate second derivative of `Psi` is necessary. The first-digit premise is supplied by frozen source in the target classes `p≡13,19 (mod 24)`; the theorem is conditional for other `p≡1 (mod 6)`.

## Proof (algebra, not a finite-experiment inference)

The exact Gauss differential equation for the terminating polynomial is
[
z(1-z)G''+[1-p/2-(1-3n)z]G'-2n^2G=0.
]
At `z=1/2`, using `6n=p-1`, this gives
[
G''(x)=(p-1)v+rac29(p-1)^2g.
]
As `L(x)=g+6v` and `L'(x)=13v+6G''(x)`, the product rule gives
[
Psi'(x)=v(g+6v)+g[13v+6G''(x)]
=6v^2+(8+6p)gv+rac43(p-1)^2g^2.
]
Differentiate the Gauss equation once, evaluate at `x`, and reduce mod `p`:
[
G''(x)equiv-v+	frac29g,qquad G'''(x)equiv 	frac{65}{9}v-	frac29gpmod p.
]
Since `L''(x)=25G''(x)+6G'''(x)`, substituting into
`Psi''=G''L+2G'L'+GL''` gives
[
Psi''(x)/2equiv	frac49(5g^2+24gv+9v^2)pmod p.
]
If `g≡0`, then `A≡6v²` and `B_0≡4v²`, hence `B_0/A≡2/3`. If `g+6v≡0`, then `v≡-g/6`, so `A≡g²/6` and `B_0≡5g²/9`, giving `B_0/A≡10/3`. The previous mutual-exclusion/simple-root theorem makes each denominator a unit under the first-digit premise.

Taylor's formula for a zero `x_p=x-delta` is `0=f-Adelta+Bdelta²+O(delta³)`; because `f∈pZ_(p)`, `A` is a unit and `d=f/A∈pZ_(p)`, solving yields `delta≡d+(B/A)d² (mod p³)`. Only `B/A mod p` is needed; replacing it by `c` proves the formula. QED.

## Exact independent check and reproducibility

Companion program `d25_clausen_one_jet_hensel_20261105.py` was actually run in a local isolated Python environment, using modular integer arithmetic only. For all 94 primes `7<=p<=1200`, `p≡1 mod6`, it independently (a) constructs `G,G',G'',G'''` from term moments at `1/2`; (b) verifies exact `A` and branch curvature `B/A`; (c) evaluates `G(z)`, `G'(z)` independently at the predicted `x_p` and verifies `Psi(x_p)=0 mod p³`. Result: **94/94 PASS**. The finite check is validation of the algebraic identities and roots on this declared domain, not an all-prime proof of the first-digit premise.

Selected tuples `(p,branch,A mod p,c mod p,x_p mod p³)`: `(7,L,3,1,165)`, `(13,G,6,5,1918)`, `(19,G,5,7,675)`, `(31,L,27,24,28970)`, `(373,G,211,125,31342631)`.

## Relation to BRC and remaining D25

This supplies a faithful typed compression for the *local signed Clausen root computation*: `(g,v,p,branch,precision)` suffices to reconstruct `Psi'`, the second-derivative ratio mod `p`, and the `p³` Hensel lift. The two branches remain separate; collapsing to the scalar `Psi(x) mod p` loses the branch label and curvature (2/3 versus 10/3). It reduces the derivative information needed by this specific local operator, not the original-class native H0/B0 or full Enterprise X6 state.

Next executable mathematical unit: substitute the branch-local one-jet representation into the prior six-port and harmonic source expansion of `W_p-p mod p³`, evaluate the residual at `p=13,19,373`, then look for a uniform signed cancellation certificate against the frozen `Delta_p-R_p` observer. Native original-class p373 `H0/B0`, `[X]U mod 139129`, Frobenius direction, eta/kappa and independent review remain open.

## Control/provenance

This is portable independent author-side reasoning using prior author-side lemmas as explicitly named dependencies. It does not claim native computation, a new Source claim/open/checkpoint, or mathematical admission. Existing native Source checkpoint/contributor/source pins are preserved; freshness is assessed by the separate current continuation receipt. The held logical research lane is `chatgpt-research-hourly-enterprise-math-20260923`, never the maintenance lane.
