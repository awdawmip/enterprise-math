# D25 original-216 → quartic 2304: proven comparator and tested cross-valuation bridge

2026-11-04 (+08). **AUTHOR-DERIVED / EXACT_SCOPED_LEMMA / FINITE_EXACT_CHECKED / CROSS_FAMILY_BRIDGE_UNPROVED / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING**. Portable mathematics, not a native checkpoint, Result, independent review or admission.

**Binding:** task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`, publication `TP2-B6F4FC938FF94941C1B7`, frozen scientific source `c47e13e4aba0e006366f989d6334d443f6333ae3`; this research lane `chatgpt-research-onhour-enterprise-math-20260923` remains separate from maintenance `chatgpt-hourly-enterprise-math-20260921`. Consume preceding original-216 valuation note (20261104_onhour_d25_original216_character_scope_and_valuation.md), CM/Hensel and F4 results at original proven scope; no native completed units asserted.

## Literature-based proven comparator

For p>=5 prime, in Z_(p), define the unchanged original

```text
a_k = C(2k,k)^2 C(3k,k) / 216^k,
W_p = sum_{k=0}^{p-1} (6k+1) a_k,
```

and a **different**, quartic family

```text
b_k = C(2k,k)^2 C(4k,2k) / (48^(2k))
    = (4k)!/((k!)^4 * 2304^k),
V_p = sum_{k=0}^{p-1} (8k+1) b_k.
```

Guo–Zudilin (2019), as explicitly reported by Zhi-Hong Sun, *Supercongruences involving Apéry-like numbers and binomial coefficients*, AIMS Mathematics 7(2) (2022), Remark 5.4, printed p. 2761, **proved** `V_p = p*(p/3) (mod p^3)` for p>3. Here `(p/3)=(-3/p)`. Exact secondary source: https://www.aimspress.com/aimspress-data/math/2022/2/PDF/math-07-02-153.pdf, Remark 5.4. Source attribution and theorem cover V only; do not attribute an original-W proof to that paper.

Therefore, **conditional on the unproved bridge** `W_p = V_p mod p^3`, the original all-prime character claim follows. On frozen p=13,19 mod24, this yields `W_p=p mod p^3`, sufficient for the existing frozen scalar Delta-R target when its established bridge is retained. This is a rigorous implication, not a proof of the premise.

## Exact two-family valuation-port lemma — PROVED

For all primes p>=5, 0<=k<p,

```text
v_p(a_k) = floor(2k/p)+floor(3k/p);
v_p(b_k) = floor(4k/p).
```

Proof: p divides neither k! nor 216/2304. Also 4k<4p<p^2 for p>=5, so Legendre's factorial formula has only the first floor term. Thus modulo p^3 the complete sums admit these **exact** cutoffs:

```text
W_p = sum_{k<=floor(2p/3)} (6k+1) a_k  (mod p^3);
V_p = sum_{k<ceil(3p/4)} (8k+1) b_k  (mod p^3).
```

Label the weighted sums over coefficient valuation s∈{0,1,2} respectively by A_{p,s}, B_{p,s}. Their difference is an exact three-port decomposition

```text
W_p-V_p = (A_0-B_0)+(A_1-B_1)+(A_2-B_2) (mod p^3).
```

The weight can increase a term's actual valuation. This lemma is elementary; no novel general valuation theorem is claimed.

## FINITE experiment — 301 primes (not all-prime proof)

An author-side Python 3 standard-library checker independently generated both original coefficient recurrences:

```text
a_{k+1}/a_k=(2k+1)(3k+1)(3k+2)/(36(k+1)^3),
b_{k+1}/b_k=(4k+1)(4k+2)(4k+3)(4k+4)/(2304(k+1)^4).
```

For k<p-1 denominators are p-units. Exact modular integer calculation covered **all 301 primes 5<=p<=2000**; independent direct `math.comb` checks on 5,7,11,13,19,37,73,373. Results: 301/301 W=V mod p^3 and V=p*(p/3) mod p^3. Further **new finite observations**: B_{p,2}=0 mod p^3 on 301/301 (unproved for all primes); A_{p,2}≠0 on 301/301; A_{p,0}≠B_{p,0} and A_{p,1}≠B_{p,1} mod p^3 for all 301; yet A_{p,0}=B_{p,0} mod p for all 301.

Exact residues in the common modulus p^3:

```text
p=13, m=2197: A=[780,1937,1690], B=[325,1885,0],
     differences=[455,52,1690]; sum differences=2197=0 mod m,
     A2/p^2=10 mod 13.
p=19, m=6859: A=[5662,4826,3249], B=[6384,494,0],
     differences=[6137,4332,3249]; sum differences=13718=0 mod m,
     A2/p^2=9 mod 19.
p=373, m=51895117: A=[28094360,38687933,37008314],
     B=[45069217,6826273,0],
     differences=[34920260,31861660,37008314],
     sum differences=103790234=2*m, A2/p^2=266 mod373.
```

The finite port data establish that a **termwise or valuation-bandwise mod p^3 bridge is false** (p=13 suffices). Any valid global bridge must transport a nonzero original valuation-2 port across the other two ports. The quartic valuation-2 vanishing is a candidate lemma, not a result of the 2019 theorem by itself.

## Highest frontier, missing evidence and exact next action

**Mother:** frozen D25 Delta_p-R_p=0 on p≡13,19 mod24; exact scalar W_p=p mod p^3 under existing source-aligned bridge. **Author-side frontier:** previous F4, Gauss/CM root and original valuation work; this literature-grounded quartic comparator, proved support theorem and finite cross-family bridge experiment. **Do not redo:** accepted D24 UR and past completed auxiliary derivations. **Next small science:** derive or refute the terminating W-to-V transform *with original endpoints and three valuation ports*, first targeting the quartic port-2 vanishing, then a full signed transport. Verify proposed identity itself at p=5,11,13,19,373, not merely final sums; if unavailable return to F4 signed Green/WZ for the original object.

**Native benchmark:** issue #1559 remains OPEN, no assigned actual executor; fixed same-original-class H0/B0 divided-power [X]U mod139129, native module rank, semilinear Frobenius and eta, signed odd Hesse/Green κ and independent replay remain NOT_EXECUTED. Portable quartic arithmetic is not a replacement.

**Current control:** Site gateway 0.6.11 returns `research_authority_granted=false`, `write_relay_enabled=false`. This run's precise read-only continuation request returned `CONTROL_QUOTA`; this is not NO_DISPATCH. The old `research-onhour-20261031-0205-dispatch-r15` was not replayed. No session, claim, open, run, native Source checkpoint, Result or review was created. Author-side GitHub publication, when verified, only preserves portable evidence. The scheduler's frequency, enablement and notifications remain unchanged.
