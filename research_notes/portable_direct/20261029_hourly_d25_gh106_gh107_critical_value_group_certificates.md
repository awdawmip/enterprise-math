# D25/LIFT GH-106/GH-107 — sufficient A_N criterion and exact critical-value collision certificates

2026-10-29 Asia/Hong_Kong. TASK_RESEARCH logical lane `chatgpt-research-hourly-enterprise-math-20260923`; author portable work.
Parent `ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION` D25/LIFT/JT2 OPEN; task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`, publication `TP2-B6F4FC938FF94941C1B7`, frozen scientific pin `c47e13e4aba0e006366f989d6334d443f6333ae3`.
Status `AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING`.

## Prior exact source and GH-106 theorem

For prime `p=8m+3>=11`, set `N=4m+1`, `k=F_p`. Reuse GH-102/GH-104 in their **Hasse-moment** scope: the signed finite-log polynomial `M` has `M(0)=0`, `ord_0 M=2m+1`, `deg M=N` and `M'=-z^(2m)G^2`, with `G` monic degree `m`, squarefree and nonzero at zero. Put `K(t)=Res_z(G,t-M)`. GH-104 gives `Disc_z(M-t)=-(1/2)t^(2m)K(t)^2`, hence the geometric and arithmetic generic Galois groups are transitive subgroups of `A_N`. The original GH-3 truncation and GH-16 reflected tail are distinct inputs.

**GH-106 (full-alternating sufficient criterion).** For `m>=2`, if `gcd_z(M,G)=1` and `K(t)` has at least one simple root over `kbar`, then

```text
Gal_geom(M(z)-t) = Gal_arith(M(z)-t) = A_N.
```

If `N` is prime, the gcd condition can be replaced with the weaker requirement that K has a simple **nonzero** root.

**Proof.** The finite critical points are precisely z=0 and the simple roots of G, because `M'=-z^(2m)G²`. Under gcd(M,G)=1, no G-root maps to t=0. The tame inertia above t=0 is therefore a single `q=(2m+1)`-cycle fixing all other points. Here `q>N/2` and `gcd(q,N)=1`. This forces primitivity: in a nontrivial block system with block size `s` dividing N and `1<s<=N/2`, if that single q-cycle moves any blocks then its support is the union of entire moved blocks (points in a moved block cannot be fixed), forcing `s|q`, a contradiction. Otherwise all blocks are stable and its unique q-orbit lies in one block, forcing `q<=s<=N/2`, also impossible.

A simple root `lambda` of K corresponds to exactly one G-root alpha with `M(alpha)=lambda`. It yields tame ramification index3, so inertia above that value is a genuine **3-cycle**. By Jordan's primitive 3-cycle theorem, geometric monodromy contains `A_N`; GH-104 bounds it above by `A_N`. Arithmetic monodromy contains geometric and is similarly bounded, giving equality. If N is prime, the transitive geometric group is primitive without needing the pure zero-fiber cycle; a simple nonzero critical value still yields a 3-cycle. As `N<p`, the Galois closure has no characteristic-p wild inertia. QED.

Jordan's theorem is external classical group theory; e.g. `Mathlib.GroupTheory.GroupAction.Jordan`, theorem `Equiv.Perm.alternatingGroup_le_of_isPreprimitive_of_isThreeCycle_mem`, following Wielandt §13.3; https://leanprover.github.io/hex/docs/Mathlib/GroupTheory/GroupAction/Jordan.html.

## GH-107: three concrete, exactly checked fibers

The program `d25_gh106_critical_value_collision_check.py` computes K **independently** as the characteristic polynomial of multiplication by `M mod G` in `F_p[z]/(G)`. Newton sums and quotient-ring multiplication give its full coefficients; modular Euclidean gcd and direct evaluation furnish the following finite certificates.

**p=131, m=16, N=65.** `gcd_z(M,G)=1`, `K(0)=89`. The full critical-value K has `gcd(K,K')=t+74=t-57`; `K(57)=K'(57)=0`, `K''(57)=18!=0`. Exactly one value has multiplicity2; the other 14 are simple. GH-106 implies **A_65** for both groups.

**p=139, m=17, N=69.** `gcd_z(M,G)=1`, `K(0)=69`; `gcd(K,K')=t+114=t-25`, with `K(25)=K'(25)=0`, `K''(25)=39!=0`. One double critical value and 15 simple ones; both groups are **A_69**. Thus the stronger blanket claim “K is always squarefree” is false even though full alternating monodromy persists.

**p=347, m=43, N=173.** `gcd_z(M,G)=z+109`; its zero `alpha=238` satisfies `G(alpha)=M(alpha)=0` and `G'(alpha)=118!=0`. For its exact degree43 critical-value polynomial, `K(0)=0`, `K'(0)=162!=0`, `gcd(K,K')=1`. Hence the fiber t=0 contains both the distinguished index87 ramification at z=0 **and** an index3 critical point at z=238. The tame inertia cycle type is `(87)(3)(1^83)`. It is **not** one pure 87-cycle. But 173 is prime, so the transitive geometric group is primitive; the 42 other distinct critical values yield genuine isolated 3-cycles. By Jordan plus GH-104, both monodromy groups are **A_173**.

The complete p347 K coefficient vector, in ascending powers, is:
```text
[0,162,45,30,312,73,59,244,89,33,325,271,253,269,245,223,53,12,275,29,63,21,11,206,106,339,51,282,58,154,76,48,305,321,334,247,72,144,136,328,121,334,265,1]
```

This distinguishes two BRC observer losses: p131/139 fuse distinct ordinary Hasse critical *points* into the same *value*; p347 fuses a Hasse critical value with the distinguished high-ramification value 0. A square discriminant alone does not preserve the underlying inertia cycle type.

## Evidence, strength, next unit

Exact Python 3 standard-library program `research_notes/portable_direct/d25_gh106_critical_value_collision_check.py` uses the already-published GH-104 script for Legendre/G/M; it checks modular characteristic polynomials, Euclidean gcds, local values/derivatives and p347 `K(M) mod G=0`. All three prime cases PASS. General conditional group theorem uses the cited Jordan theorem and GH-102/GH-104. The special-prime A_N conclusions depend on the declared finite exact certificates. No native Enterprise Math experiment or independent review.

Next: characterize via independent Hasse/CM/Jacobi methods the distribution of repeated critical values and collisions at zero; seek a value identity for `C_p^*(9)-3M_p(9)` that is not merely the derivative-square rewrite. The p347 branch collision is **different** from the p3347 reflected-tail exception. Preserve original GH-92, GH-83, GH-20/GH-21, native p373 and P000/Source-pins as separate obligations. No CLAIM, OPEN, Source checkpoint, formal Result or research-activity registration is inferred from these GitHub author artifacts.
