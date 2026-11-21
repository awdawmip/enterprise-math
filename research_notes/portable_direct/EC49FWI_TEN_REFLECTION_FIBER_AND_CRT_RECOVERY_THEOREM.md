# EC49FWI — Exact fibers of the ten-cycle reflection spectrum and CRT information recovery

Date: 2026-11-22 (Asia/Shanghai). Scientific state: AUTHOR_PROVED / EXACT_FINITE_CERTIFICATE / PARENT_DEPENDENT / NOT_REVIEWED.
Frozen scientific input: BRC16943, unchanged. Parent: EC49FWH, enterprise-math commit e988397004b2df200b275b2969b6bbbd7e410e82.
Scope: combinatorial auxiliary certificate on Z/10 and its product with Z/11. No native X6/Farey step is inferred.

## Definitions

For S ⊆ Z/10, write f(t)=1_{t∈S}, k=|S|, r_c(t)=c−t mod10 and the indexed complete reflection defect vector Δ_S(c)=|S △ r_c(S)|, c=0,...,9.

Set K_S(c)=∑_{t∈Z/10} f(t)f(c−t). Then

(1) Δ_S(c)=2(k−K_S(c)).

Define H(S)=S+5 and C(S)=(Z/10)\S. The commuting involutions H and C generate the four-element transformation group G={id,H,C,HC}.

## Theorem 1: complete ten-cycle spectrum fiber classification

For every S,T⊆Z/10,

(2) Δ_S(c)=Δ_T(c) for all c∈Z/10 if and only if T∈{S,H(S),C(S),HC(S)}.

Consequently the 1,024 binary words have exactly 272 different indexed reflection-defect spectra. Exactly 32 fibers have two words and 240 fibers have four words; there are no singleton or larger fibers.

### Proof and finite certificate

Complementation preserves symmetric difference under each reflection, so Δ_C(S)=Δ_S. Translating by five sends r_c correspondence to r_(c−10), hence Δ_H(S)=Δ_S. Thus each G-orbit lies in one defect-spectrum fiber.

By Burnside, the number of G-orbits is (1024+32+0+32)/4=272: H-fixed words are the 32 choices of five equal opposite-position pairs; C fixes no binary word; HC-fixed words are the 32 choices of five opposite-position complementary pairs. The two nontrivial fixed sets do not intersect. The orbit sizes are 32 orbits of size two and 240 of size four.

To prove that no two distinct G-orbits have the same spectrum, the attached exact verifier enumerates all integers mask=0,...,1023, computes ten defects directly by bitwise symmetric difference against each reflection, groups by the resulting ordered ten-tuple and asserts (i) exactly 272 distinct groups, (ii) the (2,4) size histogram (32,240), and (iii) each computed group equals precisely the explicit G-orbit of any of its elements. It separately checks (1) for every mask and center using a literal cyclic self-convolution. The exhaustive finite domain is explicitly 2^10=1024; integer operations are exact. The analytic orbit inclusion and the complete finite check together establish (2), without making a general statement for arbitrary cyclic modulus.

## Theorem 2: the mod-11 factor recovers a precise missing statistic

Let U⊆Z/10 be any binary word, and V⊆Z/11. Form W⊆Z/110 through CRT: t∈W iff (t mod10)∈U and (t mod11)∈V. For each center c∈Z/110, let x=c mod10 and y=c mod11. The exact correlation identity is

(3) K_W(c)=K_U(x)K_V(y), and Δ_W(c)=2(|U||V|−K_U(x)K_V(y)).

If V=Z/11 (F=11), then

(4) Δ_W(c)=11 Δ_U(x).

If V=(Z/11)\{z} (F=10), then K_V(y)=10 for y=2z and 9 otherwise; therefore

(5) Δ_W(c)=
- 10 Δ_U(x), for y=2z mod11;
- 9 Δ_U(x)+2|U|, for y≠2z mod11.

Thus for a fixed one-hole V, two product words have identical indexed complete 110-center defect spectra if and only if both their ten-center spectra and |U| agree. For a fixed full V, equality depends only on their ten-center spectra. The proof is substitution into (3); recovery of Δ_U uses y=2z in (5) and recovery of |U| uses any y≠2z.

The mod11 hole recovers the cardinality |U| but does not generally restore the signed support. The exact gain is specified by (5).

## Exact information fibers and sharp side information

Across all 1024 ten-bit words:
- Δ alone: 272 fibers, of sizes 2 (32 fibers) or 4 (240 fibers).
- (Δ,|U|): 473 fibers, sizes 1 (32 fibers), 2 (386 fibers), 4 (55 fibers).
- A worst-case two-bit selector in the ordered preimage fiber is sufficient and necessary for lossless recovery of any ten-bit word from its complete indexed Δ vector. Even after adjoining |U|, two bits are still sharp in the worst case.

For the frozen P10 auxiliary model only, using the 44-cell four-slope decoder inherited from EC49FWE and the 72 primitive directions mod10: these directions generate exactly 50 distinct ten-bit words (multiple directions can produce the same word). Within these 50 support words:
- Δ gives 38 fibers: 26 singleton and 12 doubleton;
- (Δ,|U|) gives 40 fibers: 30 singleton and 10 doubleton.
Thus one extra binary selector bit, conditional on knowing the support belongs to this finite set, is sharp for reconstructing the support. This bit is not a reconstruction of the original direction label or a full native-X6 state.

Canonical decoding: declare an input domain Q (all 1024 words, or the 50-word restricted set); enumerate all q∈Q matching the supplied full indexed spectrum (plus |U| if available), sort the matching ten-bit integer masks and supply the rank of the actual word. The rank requires ceil(log2 maximum fiber size) bits in the worst case.

## A sharpened explanation of the parent collision

The inherited exact rational-anchor words are

A=S(1/11)={0,2,3,4,7}, B=S(3/5)={0,1,3,4,6}.

Both have k=5 and Δ=(4,6,6,6,2,6,4,2,8,6). The new exact identity is

(6) B=C(H(A)).

They are not rotation/reflection equivalent (as established in EC49FWH), but are explicitly in the same G-orbit. Since their cardinalities agree, (5) proves that their full 110-center spectra remain equal when lifted against the same one-hole V; (4) proves the analogous statement for full V. A position-1 membership query separates them: 1∉A, 1∈B.

## Verification

Companion file EC49FWI_REFLECTION_SPECTRUM_FIBER_VERIFY.py uses Python 3 standard library, exact integers, and the frozen P10 four-slope predicate. It checks all 1,024 words, direct/convolution formulas at all ten centers, 272 exact equivalence classes, the Burnside fixed-point count, all 72 primitive directions, all 50 distinct frozen source words, and the explicit 1/11 versus 3/5 witness.

Additionally, for each of the 50 distinct frozen U words, it constructs full 110-site supports for V=Z11, V=Z11\{0}, and V=Z11\{6}, compares every one of the 110 direct defects against (4)/(5): 16,500 separate full-center comparisons. The exact run output is archived alongside the verifier and reports ALL PASS.

All universal claims here are the finite ten-cycle theorem or the analytic CRT identity conditional on the stated U,V. The frozen P10 source and upstream Bernoulli-to-projective derivation are inherited, not independently reviewed in this turn.

## Next discriminating dependency

Fix an actual moving-height Farey update F and readout Y from the frozen scientific task. Test if Y∘F is constant on each of the 38 frozen ten-spectrum classes or, after the one-hole mod11 factor, each of the 40 (Δ,|U|) classes. If not, identify the least selector information that separates the first genuine witness under that exact update/readout. The auxiliary contrast at position 1 does not itself prove a difference for an unspecified next-height Farey observer.

Preserve historical authorship of EC49FWH. This independently preservable portable note asserts no live shared CLAIM, Result/Review acceptance, or P000 change.
