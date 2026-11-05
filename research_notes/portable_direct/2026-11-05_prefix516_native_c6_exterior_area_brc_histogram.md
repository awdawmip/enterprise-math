# PREFIX-516 — Native C6 BRC microtrace: an exact exterior-square lift and complete branch histogram

Date: 2026-11-05 (Asia/Shanghai).
Research mode: AUTHOR_PROVED / EXACT_FINITE_CHECKED / UNREVIEWED / NOT_ADMITTED.
Researcher-ID: EM-X6-8F1C55. Activity: RA-F3707FF28D3C2045499872FE.
Task connection: RS-X6-NATIVE-ROTATION-DYNAMICS (independent author-side research; no CLAIM asserted).
Frozen scientific input: awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d.

## Scientific sources and typed model

P000 defines native X6 as a signed six-axis cell torsor; native spatial rotations and triadic dynamics remain the mother objective. The frozen note `research_notes/VIETE_X6_FIXED_RADIUS_MICROTRACE_C12_20260905.md` (§§3–4, 6, 9–11) establishes that, inside one selected STAR, a local adjacent C6 phase pair `a,b` (signed distinct axis units) has two shortest native microtraces: inner `(-a,b)`, visiting the pivot, and outer `(b,-a)`, visiting the radius-squared-two cell `a+b`. It also retains inner/outer branch provenance. The frozen `research_notes/X6_BRC_C6_GRADE_AND_EXACT_MULTINOMIAL_KERNEL_V9_20260905.md` establishes endpoint multiplicity as a BRC readout. PREFIX-515 (current Source, 2026-11-05) supplies the exact composable signature `Gamma_g=(n,y,V,W,T_g,T_g^rev,first,last)` for the 5-axis restriction, where `g` is `aab` or `aba`. This note preserves the ordered native branches and extends that observer for a specific future operation: oriented native path area.

Work in the STAR `S_B={L1,L4,L5}`, embedded into X6 as axes `i=1,j=4,k=5` (zero-based 0,3,4), with a selected local chirality. Its six signed radius-one phases are
`a_0=+e_i, a_1=-e_k, a_2=+e_j, a_3=-e_i, a_4=+e_k, a_5=-e_j`, periodically extended; `a_{r+3}=-a_r`. Each macroedge `a_r→a_{r+1}` has exactly two shortest signed native words `I_r=(-a_r,a_{r+1})` and `O_r=(a_{r+1},-a_r)`. There are `2^6=64` labeled branch histories in one C6 revolution. This is the declared local phase realization, not a selection rule for all X6 rotations.

## Theorem 1: exterior-square BRC path lift

For any native signed path word `w=(s_1,...,s_n)` with `s_h∈{±e_1,...,±e_6}`, define `y(w)=sum_h s_h` and the integral antisymmetric degree-two path signature

`A(w)=sum_{1≤r<t≤n} s_r∧s_t ∈ Λ²(Z⁶)`,

with coordinates `A_{ij}(w)=sum_{r<t}(s_{r,i}s_{t,j}-s_{r,j}s_{t,i})` for `i<j`. It has 15 integer coordinates. With the BRC pair counts from PREFIX-515, define `Gamma^A_g(w)=(Gamma_g(w),A(w))`; the sixth displacement coordinate is retained (zero in the restricted 5-axis input).

For arbitrary signed words `u,v`:

`A(uv)=A(u)+A(v)+y(u)∧y(v)`.

For formal order reversal, `A(rev w)=-A(w)`. For the native c/C reflection `R_c`, `A(R_c w)=(Λ²R_c)A(w)`: exactly those wedge coordinates involving axis c change sign. In consequence, `Gamma^A_g` remains exact under concatenation, formal reversal and c/C reflection, extending the PREFIX-515 laws. Proof: split each ordered pair in `uv` into two internal pair sets and the complete cross product `(sum u)∧(sum v)`; reversing order reverses every wedge pair; any signed-axis linear reflection acts functorially on wedges. All arithmetic is in exact integers.

This area is an observer of signed ordered path provenance, not native Cell identity and not a seventh axis. The BRC branch carrier remains the labeled word; counts and area are derived observers with an explicit operation horizon.

## Theorem 2: exact local C6 inner/outer information-loss witness

For signed distinct unit phases `a,b` and their two native macrostep words `I=(-a,b)`, `O=(b,-a)`, the endpoint displacement is `b-a` in either case and the single-edge BRC cancellation counts are identical (zero for two distinct axes). However

`A(I)=-a∧b, A(O)=a∧b, A(O)-A(I)=2a∧b ≠ 0`.

In the selected STAR one adjacent pair is `a_1=-e_k`, `a_2=+e_j`. Using the established signed alphabet `a,A,b,B,c,C,d,D,e,E`, its two microtrace words are precisely `ed` (inner) and `de` (outer). Both gates give exactly the same `Gamma_g`: length 2, identical signed displacement, `V=W=0`, identical KMP forward/reverse transition maps (both colors are 4), and sources `first=last=N`. Their area components obey `A_{d,e}(ed)=-1` and `A_{d,e}(de)=+1`.

Thus `Gamma_g` alone cannot answer the declared future query “did this two-step C6 macroedge visit the pivot?”, while `Gamma^A_g` distinguishes these two shortest branches. A single inner/outer bit is the minimal local binary repair when the only demanded information is this macroedge's branch. `A` supplies an operation-safe algebraic repair useful beyond that local query.

## Theorem 3: exact oriented-area histogram for one or many C6 circuits

The area difference for changing the r-th macroedge from inner to outer is `Δ_r=2a_r∧a_{r+1}`. Since its net displacement is unchanged, all cross-macroedge contributions to area are independent of branch choices. Because `a_{r+3}=-a_r`, `Δ_{r+3}=Δ_r`. In the chosen chirality:

`Δ_0=-2e_i∧e_k, Δ_1=+2e_j∧e_k, Δ_2=+2e_i∧e_j`.

They are independent in the three-dimensional exterior-square subspace. Let `A_0` be the all-inner six-macroedge path area. For branch bits `β_r∈{0,1}`:

`A(β)=A_0+(β_0+β_3)Δ_0+(β_1+β_4)Δ_1+(β_2+β_5)Δ_2`.

Consequently the 64 labeled BRC branch histories yield **exactly 27 distinct area classes**. If the three class coordinates are `k_0,k_1,k_2∈{0,1,2}`, their exact fiber multiplicity is `binom(2,k_0)binom(2,k_1)binom(2,k_2)`. The largest area fiber has eight histories. As a cross-check,

`A(all outer)-A(all inner)=4(e_i∧e_j+e_j∧e_k+e_k∧e_i)`.

Repeating the same closed C6 macrocycle `m≥0` times gives `6m` independent labeled binary macroedge choices and a closed signed X6 displacement in each circuit. Since cross-circuit endpoint displacements vanish, the same argument yields

`A_m(β)=m A_0+k_0Δ_0+k_1Δ_1+k_2Δ_2` with `0≤k_h≤2m`.

Therefore the number of distinct oriented-area classes is exactly `(2m+1)^3`, and the exact positive BRC multiplicity of `(k_0,k_1,k_2)` is

`M_m(k_0,k_1,k_2)=∏_{h=0}² binom(2m,k_h)`,

summing to `2^{6m}` by the binomial theorem. This is an infinite, exact family derived from native path combinatorics. Even though area is sufficient for the stated total-area observer, distinct labeled branch histories may fall in the same area fiber; queries about individual visits retain the per-macroedge bit history.

## Executed exact-integer certificate

Run `node research_notes/portable_direct/prefix516_native_c6_area_certificate.js`. The program implements native signed paths with integer BRC cancellation updates, both established KMP gates, the old Gamma fields and the new exterior-square observer. It exhausts all 1,111 ten-direction words of lengths 0…3, including 4,321 ordered concatenation splits per gate, checking composition, reversal and c-reflection. It explicitly checks the `ed/de` Gamma collision, each of the six two-path C6 edges, the whole-cycle area difference, and all `2^6=64` and `2^12=4096` labeled branch histories for m=1 and m=2 against the closed histogram. Both gates return `ALL_CHECKS_PASS`.

The arbitrary-length statements follow from the algebraic proofs; the finite certificate checks the implemented observer and small circuit populations. Signed axis vectors, KMP/source fields and all BRC counts remain exact; no pi/trigonometric or floating numerical rotation is used.

## Next discriminating question (PREFIX-517)

Determine the smallest operation-safe joint observer for the actual phase continuation and specified radius/pivot-visit readouts across the four-STAR atlas. In particular, test whether `(Gamma,A,previous/current phase,frame)` is sufficient when the future operation asks about an individual prior intermediate Cell, or exhibit a minimal same-observer counterexample and adjoin the smallest provenance coordinate. Preserve the full path branch history until a proven factorization exists.

Sources: frozen P000 and definitions/HEARTBEAT_WORLD_NATIVE_X6_TIME.json; frozen research_notes/VIETE_X6_FIXED_RADIUS_MICROTRACE_C12_20260905.md and research_notes/X6_BRC_C6_GRADE_AND_EXACT_MULTINOMIAL_KERNEL_V9_20260905.md; current research_notes/portable_direct/2026-11-05_prefix515_signed_path_composition_reversal_lift.md; docs/PORTABLE_RESEARCH_PROTOCOL.md; docs/RESEARCH_CONTINUATION_PROTOCOL.md#current-normative-context.
