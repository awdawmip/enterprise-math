# D25/LIFT — Divided successor residue as an odd-harmonic jet; source-fixed joint transfer through p²

2026-10-24 | TASK_RESEARCH, author-side rational proof and exact-Fraction regression. **UNREVIEWED / NOT_ADMITTED / NO_NEW_SOURCE_CHECKPOINT / REGISTER_PENDING for any unrecorded current activity**. This note is mathematical portable evidence, not Source admission, a native claim/run, experiment, Result or independent review.

**Scope/provenance.** Mother task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`, publication `TP2-B6F4FC938FF94941C1B7`. Frozen scientific Source pin `c47e13e4aba0e006366f989d6334d443f6333ae3` (unchanged). This scheduled lane is `chatgpt-research-hourly-enterprise-math-20260923`, never maintenance `chatgpt-hourly-enterprise-math-20260921` or the distinct onhour Research lane. The exact source-vs-carrier correction and its two singular successor ports are **inherited** from `20261024_hourly_d25_common_cauchy_defect_three_port_contiguity.md`, `20261024_hourly_d25_successor_bridge_pole_rank_31_exception.md`, and `20261024_hourly_d25_pole_free_defect_joint_finite_transfer.md`. Do not re-credit their existing results. The distinct onhour fixed-prime WZ five-tail certificate at `6fceb814b36be8245eb0038e6cb0ac38de46e42f` is a separate exposed author contribution, not a native admission and not rederived here.

## 1. Exact closed odd product for the two successor poles

Fix **any prime** `p=6m+1>=13`, put `M=m+1`. Use the previously defined
```text
D_r=2^r(2r)!/(r!(r-1)!),    h_r(t)=r!(t-1)!/[2^t(t+r)!],
k_s^B=(2-3s)(6s+1)/[3s(3s+1)].
```
The predecessor isolated `s_0=2m-1`, `s_1=2m` and proved the exact equality
[
mathcal E_{M}=R_m/p+S_m,qquad
R_m=D_M{h_M(3m)P_0+h_M(3m+1)P_1},
]
where
[
P_0=rac1{9(2m-1+1/3)}=rac1{6(3m-1)},quad
P_1=rac1{3(p+2)}-rac{(3-p)(2p-1)}{72mM}.
	ag{1}
]
The previous theorem gave `R_m ≡ 31/27 (mod p)`, hence `T_m=(R_m-31/27)/p` is p-integral. **New Theorem A: an all-m exact rational product**, which removes the need to divide two nearly equal huge fractions:
[
oxed{
R_m=C(p),2^{-(p-1)}
prod_{j=0}^{2m-1}left(1-rac{p}{2j+1}ight),quad
C(p)=rac{18p^4-59p^3+132p^2+633p+248}
{36(p-3)(p-1)(p+2)(2p+1)}.
}	ag{2}
]
This is an equality in Q (for every integer `m>=2`, with `p=6m+1` as a literal integer); primality is only needed for the later p-adic reductions. **Proof:** Put `A=D_Mh_M(3m)`, `B=D_Mh_M(m)=4(m+1)/m`. The exact factor `h_M(3m+1)/h_M(3m)=3m/[4(2m+1)]` converts (1) to
[
R_m=A,rac{216m^4+26m^3+21m^2+44m+9}
{48(m+1)(2m+1)^2(3m-1)}.
	ag{3}
]
Exact factorial cancellation gives
[
rac AB=4^{-m}rac{2m+1}{3(4m+1)}
rac{inom{3m}{m}}{inom{4m}{2m}}.
]
Since `3m=(p-1)/2`, the elementary exact generalized-binomial identity `inom{2n}{n}=(-4)^ninom{-1/2}{n}` gives
[
rac{inom{3m}{m}}{inom{4m}{2m}}
=16^{-m}
prod_{j=0}^{2m-1}left(1-rac p{2j+1}ight).
]
Use `64^m=2^{p-1}`; substitution of `m=(p-1)/6` into the remaining rational factor gives exactly `C(p)` in (2). No fitted p-adic coefficients are used.

## 2. New divided-residue mod p² theorem (harmonic/Fermat form)

Define `q=q_p(2)=(2^{p-1}-1)/p` (an **integer**), `H=H_{2m}`, `H_2=H_{2m}^{(2)}`, with rational harmonic sums and p-unit denominators. Put
[
 c_0=rac{31}{27},quad c_1=rac{1031}{648},
 quad c_2=rac{4087}{3888},qquad
 w=q+rac H2,
]
[
 t_0=c_1-c_0w,qquad
 t_1=c_2-c_1w+
 c_0left(q^2+rac{qH}{2}+rac{H^2}{8}-rac{3H_2}{8}ight).
	ag{4}
]
**Theorem B.** For every target prime `p>=13`, the exact divided residue is well-defined and
[
oxed{T_m=rac{R_m-c_0}{p}equiv t_0+p,t_1pmod{p^2}.}	ag{5}
]
In addition, `R_m≡c_0+p t_0 (mod p²)`.

**Proof (fully symbolic):** Expand the *exact* rational prefactor in (2) around `p=0`:
[
C(p)equiv c_0+c_1p+c_2p^2pmod{p^3}.
]
The expansion is legitimate because all denominator factors at `p=0` are p-units for `p>=13`. Write
[
J_1=sum_{j=0}^{2m-1}rac1{2j+1}
=H_{4m}-rac12H_{2m},quad
J_2=H_{4m}^{(2)}-rac14H_{2m}^{(2)}.
]
Because `2^{p-1}=1+pq` exactly, finite-product expansion yields
[
rac{prod_j(1-p/(2j+1))}{1+pq}
equiv1-p(J_1+q)+p^2left[
q^2+qJ_1+rac{J_1^2-J_2}{2}ight]pmod{p^3}.
]
Wolstenholme's congruence `H_{p-1}≡0 (mod p²)` for primes `p>=5`, and reflection through `p-1=6m`, give
[
H_{4m}equiv H_{2m}+pH_{2m}^{(2)}pmod{p^2},
quad H_{4m}^{(2)}equiv-H_{2m}^{(2)}pmod p.
]
Hence `J_1≡H/2+pH_2 (mod p²)` and `J_2≡-5H_2/4 (mod p)`. Multiply the prefactor with the product; the first and second p-coefficients are exactly `t_0,t_1` in (4). The resulting `R_m≡c_0+pt_0+p²t_1 (mod p³)` permits **legitimate division by p** because both `R_m` and `c_0` are p-integral and the derived difference has valuation >=1. This proves (5). The displayed `H_2` coefficient `-3/8`, not `+5/8`, incorporates the first-order reflected `J_1` term and is necessary at the second digit.

## 3. Removal of all apparent singular denominators in S_m

For `1<=s<=2m+1` recall
[
K_M(s)=rac1{27s(M+s+1/6)}
+rac1{18(s+1/3)(M+s+1/2)}
-rac{k_s^B}{12M}.
	ag{6}
]
The old notation `S_m` subtracts `P_0/p` at `s_0=2m-1` and `P_1/p` at `s_1=2m`. Instead define the following **explicit p-integral** summand without any cancellation performed during evaluation:
[
K^{m reg}_m(s)=
egin{cases}
rac1{27s(M+s+1/6)}-rac{k_s^B}{12M},&s=2m-1,\
rac1{27s(M+s+1/6)},&s=2m,\
K_M(s),&	ext{otherwise}.
end{cases}
	ag{7}
]
**Theorem C (exact rational, all m>=2):**
[
oxed{S_m=D_Msum_{s=1}^{2m+1}h_M(M+s)K^{m reg}_m(s)
inmathbb Z_{(p)}.}	ag{8}
]
At `s_0`, the second term of (6) equals `P_0/p` **exactly**. At `s_1`, the second and third terms together equal `P_1/p` **exactly**. This proves (8) termwise, while all remaining rational denominators and factorials are p-units since `4m+3<p` for `m>=2`. The finite sum in (8) is an operationally safe representation of `S_m mod p²`; there is no hidden undefined reduction in an apparent `1/p` term.

## 4. New mod-p² source-vs-auxiliary joint finite-part transfer

Retain *unchanged* predecessor quantities `\mathcal E_m`, `\mathscr F_m^{src}`, `\mathscr F_m^{car}`, and `B_r=(2r-1)!(2r)!/(4r)!`. The existing **exact** source identities are
[
Xi_m=6T_m+R_m+(p+6)S_m-pmathcal E_m,quad
mathscr F_m^{src}-mathscr F_m^{car}
=(B_M-B_m)pmathcal E_m+B_MXi_m.
	ag{9}
]
**Theorem D (new explicit p² certificate).** Using only the p-integral expressions (4), (7)-(8), and `\mathcal E_m` at original rank `m`,
[
oxed{Xi_mequiv
c_0+6t_0+6S_m
+pleft(t_0+6t_1+S_m-mathcal E_might)pmod{p^2}.}
	ag{10}
]
Consequently the entire **source-fixed minus auxiliary** LOW/HIGH observer transfer obeys
[
oxed{mathscr F_m^{src}-mathscr F_m^{car}equiv
B_MBig[c_0+6t_0+6S_m+p(t_0+6t_1+S_m)Big]
-pB_mmathcal E_mpmod{p^2}.}
	ag{11}
]
Proof: substitute `T≡t_0+pt_1 (mod p²)` and `R=c_0+pT` into (9), then combine the two `p\mathcal E_m` contributions. This cancellation is **exactly attributable to the original fixed-rank coefficient**, not to an adjustable auxiliary coefficient. The formula is p-integral before reduction. It computes two p-digits from ordinary p-unit finite sums, `H_{2m}`, `H_{2m}^{(2)}` and the integer Fermat quotient. It does **not** set `\mathscr F^{src}` or original D25 obstruction to zero.

## 5. Exact verification and scientific boundary

A separate author check rebuilt `D,h,k^B,K,\mathcal E_m,R_m,S_m,Xi_m,B_m,B_M` as standard-library `Fraction` values and tested exact equalities (2),(8),(9), plus (5),(10),(11) using modular inversion of p-unit denominators. All **12** tested target primes `13,19,31,37,43,61,67,73,79,97,103,211` passed; the full infinite claims are proved above, **not extrapolated** from these checks. Exact test residues modulo `p²` are shown below; the third column is (11):
```text
p    T_m mod p²   Xi_m mod p²   (F_src-F_car) mod p²
13       52           135                   159
19       99           299                   290
31      111           302                   802
37     1200           364                   478
43      378           737                  1466
61      860           316                   185
67      858          1742                   804
73     3795           181                  3091
79     5108          3786                  1799
97     4513          5876                  2940
103    9203          4355                  9338
211   38179         11451                 18181
```
For the exceptional `p=31`, `T_m≡111 (mod 31²)`, `\Xi_m≡302 (mod 31²)`, and the full source-minus-carrier joint discrepancy is `802 (mod 31²)`, whose reduction is `27 (mod31)`. Hence absence of an `\mathcal E_{m+1}` first-order pole **still** does not permit a first- or second-digit collapse of the original observer into the auxiliary one. `p=7` is excluded from these successor-port theorems: its extra terminal factorial pole was previously established and must remain a separate branch.

**BRC application — REUSE_APPLIED / COMPOSE_APPLIED:** keep original signed HIGH A/B sector identities, low-vs-high rank, the two exact successor seam labels, pole-free `S`, divided-residue `T`, harmonic jet `t_0,t_1`, and source-vs-carrier observer transport. The loss witness is (11): same-rank mod-p equality is not stable under successor and p² observation. This is rational p-adic arithmetic, not a native X6 physical experiment, an accepted D24/D25 Result, or a CM source comparison.

**Current parent status:** original D25/LIFT open; `\mathcal D_m^{finite}≡0 (mod p)` over the full target class is **not** proved by these transfer formulas. The genuine source-specific CM/divided-power representative class, direction/semilinearity, ordinary `\omega+6\nabla_\lambda\omega` comparison, exact normalization and same-class kappa bridge remain absent from native D25. There is no new winning CLAIM, authorized run, checkpoint, freeze/review or Source acceptance in this evidence.

**Smallest next independent unit:** consume the exact source-fixed `\mathscr F_m` and the five-tail fixed-prime WZ identity while preserving their separate owners; determine whether the rank-m terminal coefficient admits a p-integral boundary correction absorbing (11). Test the obstruction at `p=31` and `p=211` with original fixed coefficients before attempting a general termination certificate. The open WZ late-tail range remains owned by the onhour lane; do not repeat its late-tail analysis. Restore formal control only after actual current Source authority and lawful Researcher continuation. Preserve the unmodified frozen input pin and notification/scheduler settings.
