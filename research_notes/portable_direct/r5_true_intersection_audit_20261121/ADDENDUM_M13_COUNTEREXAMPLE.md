# Addendum: an explicit counterexample to the R5 four-way **minimal-period theorem**

Date: 2026-11-21. This addendum extends RESEARCH.md in the same directory without rewriting the predecessor or the earlier evidence. Status: **EXACT FINITE COUNTEREXAMPLE; AUTHOR_VERIFIED; NOT_REVIEWED**.

## Stronger result

The archived [primitive-16 all-m theorem](https://github.com/awdawmip/enterprise-math/blob/49ead3e7754e3df58b407393a917024bc0400b8b/research_notes/portable_direct/r5_primitive16_allm_20261121/RESEARCH.md) asserts that when the threshold m has m mod 16 in {12,13,14,15,0} and m mod 17 in {13,14,15,16,0}, the **strict minimum** coefficient period of the scalar count modulo an O_m(N^4) remainder is 360360.

**Take m=13.** Its residues are 13 mod 16 and 13 mod 17, so the predecessor asserts a minimum period of 360360. But the exactly corrected seven-event-mask primitive-16 pole numerator is

\[
\boxed{A_{13}^{\mathrm{true}}(z)=60+36z+4z^2-36z^3-60z^4-84z^5-84z^6-76z^7}
\]
for every primitive 16th root \(z\), expressed in the integral basis of \(\mathbb{Q}[z]/(z^8+1)\). This vector is nonzero. \(\Phi_{16}(z)=z^8+1\) is irreducible, so the polynomial cannot vanish at any primitive 16th root. Each such root has a **true order-six pole**, and hence a nonzero \(N^5\) Fourier component in the original R5 scalar failure count.

Six prices 224,240,256,272,288,304 are divisible by 16. The only maximal-pole inclusion-exclusion masks are the seven nonempty subsets of events E0,E1,E2. Every other event mask constrains at least one of those prices and has pole order at most five, so no lower-pole term can cancel this \(N^5\) coefficient. The nonmultiple-price factors are analytic and nonzero at these roots.

Any quasipolynomial whose coefficient period fails to be divisible by 16 has no primitive 16th-root Fourier component. Since \(360360=2^3\cdot 3^2\cdot5\cdot7\cdot11\cdot13\), it is **not divisible by 16**. Consequently

\[
\boxed{M_{13}\bigl(O_{13}(N^4)\bigr)\neq 360360,\qquad 16\mid M_{13}\bigl(O_{13}(N^4)\bigr).}
\]

This **falsifies the predecessor's minimum-period value at m=13**, rather than merely identifying a gap in its proof. Its actual minimum period remains to be computed; the present result does not assert a replacement value. In particular, the previous four-class classification should not be used as an established exact universal formula.

## Two exact, structurally different implementations

The companion VERIFY_M13.py computes the same cyclotomic vector in two ways.

**Method A, multiconstraint state DP:** for every inclusion-exclusion mask I among E0,E1,E2, process the individual prices in the union, tracking separately the partial count for *each selected event* together with the weighted-cost residue modulo 16. Reject transitions exceeding any selected event's cap. Sum the exact histograms and multiply by their respective \(\prod_{p\in U_I}(1-z^p)\) factors.

**Method B, grouped-count convolution:** use individual multiplicities a=a214, b=a215 and count totals c on 216..218 and d on 219..221, with exact residue histograms for c and d. For each (a,b,c,d), evaluate all three truth values \(a+b+c<m\), \(a+c+d<m\), \(b+c+d<m\). The correction to the three single-event terms is \(-(\#\mathrm{true}-1)\) when at least two are true. This method does **not** reuse Method A's event-mask DP. Both methods yield the exact displayed eight-coordinate vector at m=13. At m=16 they independently agree on

\[
A_{16}^{\mathrm{true}}(z)=(-32,32,96,136,160,152,128,88)\neq0,
\]

contrary to the previous zero classification. Finite m=1..19 grouped computations likewise give nonzero vectors, but no infinite m claim is drawn from those samples.

## Evidence/provenance

The original frozen five event sets, 101 price range and input pins remain unchanged. The mathematical correction concerns the derived overlap encoding, not P000. Full finite program output and both precise algorithms are retained in the same source directory. This additive counterexample can be integrated into review/audit without overwriting any historic authorship, commit, Result or Activity.

Next: derive the full exact threshold rational generating function for the **true** three-conjunction incidence structure, then re-establish (or refute) minimum periods for every m and inspect downstream root-order derivations that used the same union-cap shortcut. Independent Review remains NOT_REVIEWED.
