# D25 — Second reflection digit: mixed-valuation Clausen cutoff certificate

Date: 2026-11-08 Asia/Hong_Kong. Classification: author-side TASK_RESEARCH portable **exact theorem proved**, modular regression **77 target primes checked**; **UNREVIEWED / NOT_ADMITTED**, not a native H0/B0 benchmark. Research logical lane `chatgpt-research-onhour-enterprise-math-20260923`; maintenance lane `chatgpt-hourly-enterprise-math-20260921` excluded.
Task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication `TP2-B6F4FC938FF94941C1B7`; frozen scientific pin `c47e13e4aba0e006366f989d6334d443f6333ae3`.

This unit consumes (and does not re-prove) the frozen original reflection source and the author-side first-cutoff identity from `20261026_onhour_d25_native_lift_source_port_identity.md`, then the finite Green/adjoint resonance work ending in `20261108_onhour_d25_finite_adjoint_resonance_original_R.md` (main contains `698f6bf033747ea7b2af46babb274b7a9f2689ac`). **New question:** does the proven mod-p identification `Q_p/p² = R_p (mod p)` survive one extra p-adic digit? Answer: a specific, computable low-high and middle-high correction intervenes.

## Exact source setup, with retained observer ports

Let p=6m+1 be prime and p>=13 (in the frozen application p mod24 in {13,19}). In the local ring Z_(p), put
[
 b_k=rac{(1/6)_k(1/3)_k}{2^k(k!)^2},quad 0leq k<p,qquad
 q_i=2^{-i}{mchoose i}{2mchoose i},quad 0leq ileq m.
]
Let `c_1=1/10`, and `c_{a+1}=c_a 36a²/((6a+5)(3a+2))` for 1<=a<2m. In particular the pre-existing original reflection uses c_a only for 1<=a<=m; the **same rational recurrence is extended here to 2m** to observe the new middle-high sector. Write `w(i,a)=1+6(i-a)`.

Define the exact rational reflected lift
[
 {cal R}_m=2sum_{i=1}^msum_{a=1}^i q_i w(i,a)c_ain{f Z}_{(p)}.
]
Its reduction modulo p is precisely the frozen original `R_p`. For the actual Clausen cutoff, with its independent coefficient source,
[
 {cal Q}_p=sum_{0le i,j<p, i+jge p} (6(i+j)+1)b_i b_j.
]

There are exactly three b_k valuation bands below p:
[
v_p(b_k)=0 (0le kle m),quad 1 (m<kle2m),quad
2 (2m<k<p).
	ag{BAND}
]
Only one p-factor occurs in the numerator (6j+1) at j=m and one in (3j+1) at j=2m; all denominators are p-units.

The two first-digit reflection comparisons hold in F_p:
[
 b_i=q_iquad(0le ile m),qquad b_{p-a}/p²=c_aquad(1le ale2m).
	ag{BASE}
]
The first follows by substituting `m=(p-1)/6` into q_i. For the second, Wilson's theorem gives `b_{p-1}/p²=1/10` mod p: the products of nonzero (6j+1) and (3j+1) over j=0..p-2, excluding their unique zero index, respectively have residues 1/5 and 1/2. The backward recurrence is
[
 b_{p-a-1}/b_{p-a}=
 rac{36(p-a)^2}{(6p-6a-5)(3p-3a-2)}
 equivrac{36a^2}{(6a+5)(3a+2)}pmod p.
]
Every denominator is a p-unit for 1<=a<2m, so (BASE) extends through the required middle-high pairs.

Define **three independently typed first-correction arrays**, with each indicated division performed in Z_(p) *before* reduction:
[
 d_i=(b_i-q_i)/pmod pquad(1le ile m),qquad
 v_a=(b_{p-a}/p²-c_a)/pmod pquad(1le ale2m),qquad
 u_i=b_i/pmod pquad(m<ile2m).
]

## Theorem — exact second reflection digit

The cutoff has valuation at least two and
[
oxed{ rac{{cal Q}_p}{p²}equiv {cal R}_m+p(S_{m low}+S_{m mid})pmod{p²} },
	ag{SECOND-REFLECTION}
]
where both new observations are well-defined in F_p:
[
egin{split}
 S_{m low}&=2sum_{i=1}^msum_{a=1}^i
 igl[w(i,a)(d_ic_a+q_iv_a)+6q_ic_aigr],\
 S_{m mid}&=2sum_{i=m+1}^{2m}sum_{a=1}^i w(i,a)u_ic_a.
end{split}
	ag{PORTS}
]

**Proof.** The index condition i+j>=p and (BAND) exhaustively partition all pairs with valuation below four into: (i) low-high, i<=m and j=p-a for 1<=a<=i, with valuation 0+2; and (ii) middle-high, m<i<=2m and j=p-a for 1<=a<=i, with valuation 1+2. Both admit the symmetric partner, hence the factor 2. Low-low, low-middle and middle-middle cannot reach i+j>=p (their largest sums are 2m, 3m, 4m respectively, all below 6m+1=p); high-high has valuation four and vanishes modulo p^4. For j=p-a the **exact** weight is w(i,a)+6p. In (i), substitute b_i=q_i+pd_i mod p² and b_{p-a}/p²=c_a+pv_a mod p². The zero-order term is `R_m` and the order-p terms give `S_low`. In (ii), use b_i=p u_i mod p² and b_{p-a}=p² c_a mod p³, giving `p S_mid`. Thus all p^4 terms are covered and the congruence follows. No absolute-value, norm, or provenance collapse is used.

## Original LIFT second-digit interface (exact conditional consequence)

Keep the **original** Gauss sums `M=sum b_k`, `N=sum k b_k`, `h=M+12N`, `G=M/p`, and original weighted `W`. Clausen convolution gives `W=Mh-Q`. Under the already recorded first-digit conditions p|M and p|(Gh-1), set `Delta=(Gh-1)/p` as a p-local rational number. Then **exactly**
[
 Delta-rac{{cal Q}_p}{p²}=rac{W-p}{p²}.
]
Combining with SECOND-REFLECTION,
[
 oxed{ Delta-{cal R}_mequivrac{W-p}{p²}+p(S_{m low}+S_{m mid})pmod{p²}. }
	ag{LIFT-2}
]
When the previously checked W=p mod p³ holds for a given prime, the right side is divisible by p and the next source readout is
[
 oxed{ rac{Delta-{cal R}_m}{p}equiv
 rac{W-p}{p³}+S_{m low}+S_{m mid}pmod p. }
	ag{NEXT-DIGIT}
]
This exactly specifies the extra observation required before lifting `R_p=Q/p² (mod p)` to a second digit. It is **not** a proof of the all-prime W=p mod p³ target, nor a native CM claim.

## Executed checks and discriminating witnesses

A standalone standard-library checker `d25_second_reflection_digit_check_20261108.py` separately builds both Gauss and weighted `3F2` series modulo p^4; forms Q by an **independent prefix-moment convolution**; forms original rational reflected R from q,c without using Q; verifies the valuation bands, every extended reflection base coefficient and both source ports. It checks all 77 primes p<=2000 with p mod24 in {13,19}, including the original second-digit interface. All 77 satisfy SECOND-REFLECTION and NEXT-DIGIT in exact modular arithmetic; the tested S_low, S_mid and total S are nonzero for every one of the 77 examples (finite observation).

| p | R_m mod p² | Q/p² mod p² | S_low | S_mid | S_total | (W-p)/p³ | (Delta-R_m)/p |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 13 | 130 | 104 | 9 | 2 | 11 | 9 | 7 |
| 19 | 202 | 221 | 18 | 2 | 1 | 12 | 13 |
| 37 | 122 | 1084 | 23 | 3 | 26 | 19 | 8 |
| 43 | 789 | 1563 | 13 | 5 | 18 | 19 | 37 |
| 67 | 1227 | 4443 | 33 | 15 | 48 | 55 | 36 |
| 211 | 6238 | 19742 | 43 | 21 | 64 | 192 | 45 |
| 373 | 52416 | 65844 | 252 | 157 | 36 | 228 | 264 |

For p=373, the two source corrections total 252+157=409=36 (mod373), and `Q/p²-R=13428=373*36` modulo 373². The second digit of the frozen original reflection consequently contains a nonzero new middle-high source. Both p=19 and p=373 are nonzero-boundary controls. The finite 77-prime evidence discriminates naive second-digit reuse of R; the theorem explains *why*.

## Durable continuation and authority

Mother objectives remain `Delta_p=R_p (mod p)` and `W_p=p (mod p³)`; the native p=373 fixed H0/B0 divided-power `[X]U`, original Frobenius eta, signed Hesse κ and independent replication under issue #1559 remain pending. This author-side theorem keeps three source ports (low-high correction, middle-high, original reflected lift) independently callable; it is not a surrogate for the native benchmark.

Next exact scientific action: seek a first-digit Fricke/Cartier/Wronskian pairing of `S_low` and `S_mid` with the original divided `(ZH0-1)/p`, `SH0`, `ZH1`, `Phi_xx` before any projection. Test p=19,373 on the *original* definitions. Preserve the existing old Source request `onhour11-20261106-1400-exact-research-lane-continuation`; 2026-11-08 source status/reconcile failed `BACKEND_IDENTITY_OR_VERSION_MISMATCH / STATUS_DATABASE_UNAVAILABLE`, `operation_sent=false`. Site reports `CONFIGURED_NOT_LIVE_VERIFIED`, `research_authority_granted=false`; there is no verified native own session/claim/run/checkpoint. Native source progression requires the authorized Site-bound backend client and credential. AUTHOR_SIDE_PROVED / EXACT_77_PRIME_CHECKED / UNREVIEWED / NOT_ADMITTED.
