# PREFIX-277: A Sharp Three-Source C4-BRC Obstruction and a Minimal Four-Source Witness

**Classification:** Exact author-side mathematics in the Stage50 declared ordered source-load pair observer; finite exact checking; no native execution or independent result admission.

## Typed source, provenance and definitions

Pinned global source: `awdawmip/chatgpt-global-knowledge@2fb4d3ecd15c2dcf1e55c804d8b91a24801db4b6`; pinned Enterprise Math source: `awdawmip/enterprise-math@406367147f6e34f78d873b24d2818ebca96d61fc`. Reused Stage50 declaration `research_notes/HEARTBEAT50_INTERFERENCE_KERNEL_20260923_6DD798.md` (blob 0f4ec78225cfc799a267ca6b96d9f994422f8ad2) and previous PREFIX-276 Toeplitz analysis.

Fix a nonempty finite set `S⊂Z` of occupied integer source-history loads. Exactly one coherent C4 character per occupied load has coefficient `a_j=w_j i^{p_j}` with `w_j∈Q_{>0}` and `p_j∈Z/4Z`. Distinct branches at the same load may not be erased or treated as one such coefficient without a separate proof. Set `Z=Σ_j w_j²`; define source-labeled ordered-pair moments and the declared detector by
```text
c_r= (Σ_{j,j+r∈S} conj(a_{j+r}) a_j)/Z ; c_0=1
P_ext(r,p)=(5/18)*(1-Re(i^p c_r)), p=0,1,2,3.
```
These are typed C4 BRC pair terms, not a positive-total-mass surrogate. Source count is not native X6 dimensionality; history-lag r is not physical heartbeat time. Legitimate native phase/detector controls and the full H_n dynamics have not been established.

## Theorem 1: strict Toeplitz positivity from finite support

Let `f=Σ a_j |j>` be a nonzero finite packet and `T|j>=|j+1>`. The shifts `f,Tf,...,T^Hf` are linearly independent for every finite H. In a supposed nontrivial vanishing combination choose the least shift with nonzero coefficient and the least occupied load in f. The amplitude at their sum cannot cancel against any later shift, yielding a contradiction. Their normalized Gram `T_H=(c_{v-u})_{0≤u,v≤H}` is therefore strictly positive definite.

At `c_1=i/2`, the Stage50 formal extension disk is strict: `|c_2+1/4|<3/4`, hence `5/36<P_ext(2,0)<5/9`. Any one finite nonzero source packet fails to attain the old closed PSD boundary. No claim is made that every interior point has a C4 source realization.

## Theorem 2: sharp support-three no-go

If `|S|≤3` and `c_1=i/2`, then `c_2` is real and
```text
-(2+sqrt(2))/8 < c_2 ≤ 0.
```
If there is no adjacent integer source pair, c1 is zero. If there is just one adjacent pair with positive weights a,b and a third occupied load c, then `|c_1|=ab/(a²+b²+c²)<1/2`. Thus two occupied loads must be adjacent and equally weighted (yielding c2=0), and three occupied loads must be consecutive.

For three consecutive loads with weights a,b,c, the two adjacent C4 pair contributions have phases among `{±1,±i}`. A zero real and positive imaginary total of magnitude Z/2 forces both phases to be +i: one real and one imaginary contribution cannot cancel the real part; both real terms have no imaginary part; opposing ±i signs yield at most `b|a-c|/Z<1/2`; two -i signs give the opposite direction. Up to common C4 gauge, the amplitudes are `(a,-ib,-c)`, with
```text
Z=a²+b²+c²=2b(a+c), c_2=-ac/Z<0.
```
Set `s=a+c, t=b/s, u=ac/s²`. Then `u=(t-1)²/2`, `0<u≤1/4`, and
```text
1-1/sqrt(2) ≤ t ≤ 1+1/sqrt(2),
-c_2=(t-1)²/(4t).
```
The last function decreases up to t=1 and increases afterward. Its larger endpoint maximum is attained at the left bound and equals `(2+sqrt(2))/8`. Attaining equality would require `a=c` and `t=1-1/sqrt(2)`, irrational and impossible for positive rational a,b,c; the inequality is strict.

Sharpness as an unattained infimum follows from the pre-existing rational one-parameter three-load family
```text
(a,b,c)=(2/(1+q²),1,(q-1)²/(1+q²)),
phases=(1,-i,-1), q∈Q\{1}.
```
It fixes `c_1=i/2`; as rational q approaches `1-sqrt(2)`, one obtains `a/c→1`, `t→1-1/sqrt(2)`, hence `c_2→-(2+sqrt(2))/8`.

**Scope:** This does not extend automatically to multiple branches per load, arbitrary complex amplitudes, mixtures, different detector effects or physical preparations.

## Theorem 3: four occupied loads are necessary and sufficient for positive second-lag moment

For `c_1=i/2` under the same source restrictions, any `c_2>0` requires at least four distinct occupied labels. The bound is sharp:
```text
f_C=|0>+i|1>+4|2>-2i|3>, Z=22.
Z c_1=conj(i)*1+conj(4)*i+conj(-2i)*4=11i
Z c_2=conj(4)*1+conj(-2i)*i=2
c_1=i/2, c_2=1/11, P_ext(2,0)=25/99<5/18.
```
Conversely, Theorem 2 guarantees `P_ext(2,0)≥5/18` with at most three sources. In this fixed, declared detector language a legal same-preparation reading with `c_1=i/2` and `P_ext(2,0)<5/18` thus certifies at least four occupied source loads, **not** four native spatial axes or four physical cells. Compare `f_A=(1,-i)` (c2=0), `f_B=(2,-i,-1)` (c2=-1/3), and fC (c2=1/11): all have `r=1` C4 outputs `[5/18,5/12,5/18,5/36]`, but the `r=2,p=0` outputs are `5/18,10/27,25/99`, respectively.

## Exact reproducibility, prior art and native-transfer boundary

`verify_prefix277.py` uses source-labeled ordered C4 pairs and exact Gaussian rationals via Python `fractions.Fraction`; it enumerates all 72,100 packets with two/three distinct loads from 0..6, integer weights 1..5, every relative C4 phase (first phase fixed as an exact global gauge). All 60 packets satisfying `c_1=i/2` meet the proved obstruction (30 two-load, 30 three-load). Explicit A/B/C packets and five rational approach parameters are checked separately. These finite checks are not the universal proof; the arguments above are.

The strict Toeplitz/Schur component builds on classical positive-definite kernel theory, not asserted as novel mathematics; the new scoped synthesis is the sharp *source-support bound in the Stage50 declared C4 BRC observer*. Existing `src/enterprise_math/brc_weighted_recurrent.py` is strictly positive mass, hence cannot be executed as a phase-cancellation backend. Source `definitions/HEARTBEAT_WORLD_NATIVE_X6_TIME.json` has `fixed_heartbeat_program=null`, whereas `definitions/HEARTBEAT_SELF_CONSISTENT_INSTANT_V0_1.json` requires a `model_law_id` and complete cell/material/field/source/boundary/time state; those two checked contracts do not supply the native H_n transition or typed physical T² gate. The historical Stage50 source package is referenced in a separately stored Git bundle and was not imported or executed here. The native research session is denied with `STATIC_READONLY_SCOPE_DENIED` and task listing returns `CONTROL_QUOTA`; active owner/claim is unknown. Mathematical promotion, formal Result, independent Driver acceptance and physical attribution remain pending.

**Next, PREFIX-278:** inspect and execute the original stage50/interference.py under the same three source packets, normalization and detector, then determine whether genuine native H_n operations legalize r=2. If not, preserve c2 as a future-relevant source-history residual and identify the first missing typed operation.
