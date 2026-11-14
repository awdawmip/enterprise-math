# OAI7-090: Lean proof-chain and density-domain audit

**Driver source/semantic review** — 2026-11-15, EM-DVR-DEBB5E (RESEARCH_DRIVER). This is a non-claiming external-model audit of the frozen `openai/math@adc7f1241b42e322a6451854ab7e4b4c146bf78a` tree, complementary to `research_notes/driver/2026-11-14_oai7_090_python_lean_evidence_crosswalk.md`. The assigned task is `RS-OAI7-090-A-20261007-6F2A81`. Original theorem, numerical certificate, and Lean implementation authorship remains with `openai/math`; this Driver establishes the two narrower source/logic correspondences below.

## 1. A local-finiteness hypothesis is mathematically redundant **under this exact Lean definition of density one**

In `lean/OAI/Analysis/Triangular/Energy/Basic.lean`, set `Plane := EuclideanSpace ℝ (Fin 2)`, and write
`D_C(R) := C ∩ Metric.closedBall 0 R`. The definitions are:

- `LocallyFinite C := ∀ R : ℝ, (D_C(R)).Finite`.
- `diskPoints C R := if h : (D_C(R)).Finite then h.toFinset else ∅`; `diskCount C R := (diskPoints C R).card`.
- `DensityOne C := Tendsto (fun R : ℝ => (diskCount C R : ℝ)/(Real.pi*R^2)) atTop (𝓝 1)`.

**Proposition.** For every `C : Set Plane`, `DensityOne C → LocallyFinite C`.

**Proof.** Fix any radius `r ∈ ℝ`. The density limit equals 1, so there is an `R > max(r,1)` with `diskCount C R/(πR²) > 1/2`. In particular `diskCount C R > 0`. If `D_C(R)` were infinite, the definitional `if` would choose `∅`, forcing `diskCount C R=0`, contradiction. Thus `D_C(R)` is finite. Because `r≤R`, `D_C(r)⊆D_C(R)`; hence `D_C(r)` is finite. The radius was arbitrary. ∎

The proof is a direct mathematical derivation from the exact Lean definitions, not a newly Lean-compiled theorem. In `lean/OAI/Analysis/Triangular/Energy/Universal.lean`, `universal_energy_minimum` takes `(_hC : LocallyFinite C)` but its proof invokes `gaussian_energy_bound hd` and `universal_from_gaussian_bounds hd ... hg` using `hd : DensityOne C`, without using `_hC`. The `Energy/Density.lean` LP argument is also density-only. This is **consistent**, not a missing mathematical assumption: `hd` already entails `LocallyFinite C` for these exact definitions. It also means the formalized energy observable is specifically the centered-disk extended-`ENNReal` `Filter.liminf` of normalized off-diagonal energies; claims about other thermodynamic-limit definitions need their own equivalence.

## 2. The two finite inverse certificates refer to one and the same 20×20 matrix

In `lean/OAI/Analysis/Triangular/Certificate/AtomicMatrix.lean`, the precise declaration is
`noncomputable abbrev RValue : Matrix (Fin 20) (Fin 20) ℝ := Construction.R`.
Thus `AtomicMatrix.RValue` and `Construction.R` are *definitionally equal*, not merely numerically similar matrices.

- `Certificate/AtomicFiniteCertificate.lean` proves `AtomicMatrix.sub_isUnit`, `add_isUnit`, the two-sided inverse identities and entrywise inverse enclosures for `1 ± RValue`, assembled as `atomic_finite_certificate`. Its proof uses a **right-residual** `E=I-AB` and a second-order correction.
- `Certificate/Inverse.lean` separately proves `FiniteCertificate.minusBlock_isUnit : IsUnit (1 - Construction.R)` and the plus analogue using its certified residual data and inverse bounds.
- `Construction/FiniteSystem.lean` derives `Uplus_equation` and `Uminus_equation` from those `FiniteCertificate` invertibility lemmas. `Triangular/Main.lean` invokes the same `FiniteCertificate.minusBlock_isUnit`, `plusBlock_isUnit` in `largeGaussian_hasAtomicConstruction`.

The shared matrix is therefore **identified exactly**, while the main Gaussian construction follows the `Certificate/Inverse` proof route. The standalone `AtomicFiniteCertificate` theorem is an additional certificate on the same matrix, not an automatically verified claim that every constant, rational enclosure, or Python assertion agrees across all artifacts. This resolves one source-level normalization question in the earlier crosswalk and precisely locates the remaining numerical comparison.

## Status and continuation

**Verified:** exact frozen source bytes, definition-level proof of `DensityOne→LocallyFinite`, the definitional identity `RValue=Construction.R`, and the names/use-sites of the two finite inverse paths. No local Lean build or transitive axiom audit was executed; no Python checker execution or formal Task Result acceptance is claimed.

**Next independent research unit:** compare the finite coefficient/residual enclosure constants in the two Lean certificates with the original Python assertions and manuscript's finite matrix, then run assert-enabled Python and an appropriately pinned Lean build/axiom check under the actually assigned RESEARCHER. The existing OAI7 Task and author/owner separation remain intact.

### Pinned source artifacts (`openai/math@adc7f1241b42e322a6451854ab7e4b4c146bf78a`)

- `lean/OAI/Analysis/Triangular/Energy/Basic.lean`: blob `74d533d7830745af6e389a93d4b4f30360764b23`.
- `lean/OAI/Analysis/Triangular/Energy/Density.lean`: blob `5a710439afcdb410aa0202872a94fe14e90fb1b8`.
- `lean/OAI/Analysis/Triangular/Energy/Gaussian.lean`: blob `bd179d5d86af6401548172fbc769135658c95ac9`.
- `lean/OAI/Analysis/Triangular/Energy/Universal.lean`: blob `67105df7ccf22afc7930a13a56bb2128478982e7`.
- `lean/OAI/Analysis/Triangular/Energy/Potentials.lean`: blob `9d88de312caac23fe1432513586e825c204bdcc4`.
- `lean/OAI/Analysis/Triangular/Certificate/AtomicMatrix.lean`: blob `df3cd4517bd13dd35943d5f55aeab284767b93b7`.
- `lean/OAI/Analysis/Triangular/Certificate/AtomicFiniteCertificate.lean`: blob `f6c0cef43766cb949aabadf92772e290cd92a360`.
- `lean/OAI/Analysis/Triangular/Certificate/Inverse.lean`: blob `0374d7b4975865906fa07bcebdc0e0c1b4f3e633`.
- `lean/OAI/Analysis/Triangular/Construction/FiniteSystem.lean`: blob `f8d17fe7cc8110c859f36c81e3f977585b9c0236`.
- `lean/OAI/Analysis/Triangular/Main.lean`: blob `7c673bde297afccf2f246051adc62a0b843eef2c`.

This is Euclidean-plane external-model source analysis; no X6 native-path mapping or P000 promotion is asserted.
