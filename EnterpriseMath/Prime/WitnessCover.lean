import Mathlib.Data.Set.Basic
import Mathlib.Tactic

namespace EnterpriseMath.Prime

/-- A witness language is prime-sound when no witness rejects a true prime. -/
def PrimeSound
    {X W : Type*}
    (prime : X → Prop)
    (pass : W → X → Prop) : Prop :=
  ∀ w x, prime x → pass w x

/-- `x` survives every witness selected by `A`. -/
def AllPass
    {X W : Type*}
    (pass : W → X → Prop)
    (A : Set W)
    (x : X) : Prop :=
  ∀ w, w ∈ A → pass w x

/-- Every composite is rejected by at least one selected witness. -/
def CoversComposites
    {X W : Type*}
    (prime : X → Prop)
    (pass : W → X → Prop)
    (A : Set W) : Prop :=
  ∀ x, ¬ prime x → ∃ w, w ∈ A ∧ ¬ pass w x

/-- The all-pass decision descends to exact primality on the declared domain. -/
def PrimalityDescends
    {X W : Type*}
    (prime : X → Prop)
    (pass : W → X → Prop)
    (A : Set W) : Prop :=
  ∀ x, prime x ↔ AllPass pass A x

/-- A pseudoprime is a composite that remains in the current all-pass fiber. -/
def Pseudoprime
    {X W : Type*}
    (prime : X → Prop)
    (pass : W → X → Prop)
    (A : Set W)
    (x : X) : Prop :=
  ¬ prime x ∧ AllPass pass A x

/-- Rejection support of one witness. -/
def RejectionSupport
    {X W : Type*}
    (pass : W → X → Prop)
    (w : W) : Set X :=
  {x | ¬ pass w x}

/-- Union of rejection supports selected by `A`, written without a finiteness
assumption on either the state or witness type. -/
def FamilyRejectionSupport
    {X W : Type*}
    (pass : W → X → Prop)
    (A : Set W) : Set X :=
  {x | ∃ w, w ∈ A ∧ ¬ pass w x}

/-- The declared composite set. -/
def CompositeSet
    {X : Type*}
    (prime : X → Prop) : Set X :=
  {x | ¬ prime x}

/-- The support-cover form of `CoversComposites`. -/
theorem coversComposites_iff_support_cover
    {X W : Type*}
    {prime : X → Prop}
    {pass : W → X → Prop}
    {A : Set W} :
    CoversComposites prime pass A ↔
      CompositeSet prime ⊆ FamilyRejectionSupport pass A := by
  simp [CoversComposites, CompositeSet, FamilyRejectionSupport]

/-- T-A1.  For a prime-sound witness language, exact primality descends through
the all-pass signature exactly when the selected rejection supports cover every
composite. -/
theorem primalityDescends_iff_coversComposites
    {X W : Type*}
    {prime : X → Prop}
    {pass : W → X → Prop}
    {A : Set W}
    (hSound : PrimeSound prime pass) :
    PrimalityDescends prime pass A ↔ CoversComposites prime pass A := by
  classical
  constructor
  · intro hDesc x hxComposite
    by_contra hNoRejector
    have hAll : AllPass pass A x := by
      intro w hw
      by_contra hFail
      exact hNoRejector ⟨w, hw, hFail⟩
    exact hxComposite ((hDesc x).2 hAll)
  · intro hCover x
    constructor
    · intro hxPrime w hw
      exact hSound w x hxPrime
    · intro hAll
      by_contra hxComposite
      obtain ⟨w, hw, hFail⟩ := hCover x hxComposite
      exact hFail (hAll w hw)

/-- The pseudoprime fiber is exactly the uncovered composite part of the
all-pass state. -/
theorem pseudoprime_iff_uncovered_composite
    {X W : Type*}
    {prime : X → Prop}
    {pass : W → X → Prop}
    {A : Set W}
    {x : X} :
    Pseudoprime prime pass A x ↔
      ¬ prime x ∧ ¬ ∃ w, w ∈ A ∧ ¬ pass w x := by
  classical
  constructor
  · rintro ⟨hxComposite, hAll⟩
    refine ⟨hxComposite, ?_⟩
    rintro ⟨w, hw, hFail⟩
    exact hFail (hAll w hw)
  · rintro ⟨hxComposite, hUncovered⟩
    refine ⟨hxComposite, ?_⟩
    intro w hw
    by_contra hFail
    exact hUncovered ⟨w, hw, hFail⟩

/-- Two states have the same selected witness signature when every selected
witness has the same pass/fail value on both states. -/
def SameSignature
    {X W : Type*}
    (pass : W → X → Prop)
    (A : Set W)
    (x y : X) : Prop :=
  ∀ w, w ∈ A → (pass w x ↔ pass w y)

/-- The witness-signature quotient is primality-safe when signature equality
never identifies a prime with a composite. -/
def SignaturePrimalitySafe
    {X W : Type*}
    (prime : X → Prop)
    (pass : W → X → Prop)
    (A : Set W) : Prop :=
  ∀ x y, SameSignature pass A x y → (prime x ↔ prime y)

/-- Composite coverage is sufficient for witness-signature primality safety.
No existence-of-prime assumption is needed in this direction. -/
theorem coversComposites_signaturePrimalitySafe
    {X W : Type*}
    {prime : X → Prop}
    {pass : W → X → Prop}
    {A : Set W}
    (hSound : PrimeSound prime pass)
    (hCover : CoversComposites prime pass A) :
    SignaturePrimalitySafe prime pass A := by
  classical
  intro x y hSame
  constructor
  · intro hxPrime
    by_contra hyComposite
    obtain ⟨w, hw, hyRejects⟩ := hCover y hyComposite
    have hxPass : pass w x := hSound w x hxPrime
    exact hyRejects ((hSame w hw).mp hxPass)
  · intro hyPrime
    by_contra hxComposite
    obtain ⟨w, hw, hxRejects⟩ := hCover x hxComposite
    have hyPass : pass w y := hSound w y hyPrime
    exact hxRejects ((hSame w hw).mpr hyPass)

/-- R005-A/R005-B bridge with its exact nonempty-truth-class hypothesis.

For a prime-sound witness language on a domain containing at least one true
prime, witness-signature primality safety is equivalent to rejection-support
coverage of every composite.  The prime-existence hypothesis is essential for
the reverse implication: on a prime-free domain the primality label is constant,
so even an empty signature is primality-safe while it need not reject anything. -/
theorem signaturePrimalitySafe_iff_coversComposites
    {X W : Type*}
    {prime : X → Prop}
    {pass : W → X → Prop}
    {A : Set W}
    (hSound : PrimeSound prime pass)
    (hPrime : ∃ p, prime p) :
    SignaturePrimalitySafe prime pass A ↔ CoversComposites prime pass A := by
  classical
  constructor
  · intro hSafe x hxComposite
    obtain ⟨p, hpPrime⟩ := hPrime
    by_contra hNoRejector
    have hSame : SameSignature pass A p x := by
      intro w hw
      have hpPass : pass w p := hSound w p hpPrime
      have hxPass : pass w x := by
        by_contra hxRejects
        exact hNoRejector ⟨w, hw, hxRejects⟩
      exact ⟨fun _ => hxPass, fun _ => hpPass⟩
    exact hxComposite ((hSafe p x hSame).1 hpPrime)
  · exact coversComposites_signaturePrimalitySafe hSound

/-- `w` has an exclusive composite collision when there is a composite rejected
by `w` and passed by every other witness.  Such a collision forces `w` into
every safe witness family. -/
def ForcedWitness
    {X W : Type*}
    (prime : X → Prop)
    (pass : W → X → Prop)
    (w : W) : Prop :=
  ∃ x, ¬ prime x ∧ ¬ pass w x ∧ ∀ v, v ≠ w → pass v x

/-- A witness is mandatory when every composite-covering family must contain it. -/
def MandatoryWitness
    {X W : Type*}
    (prime : X → Prop)
    (pass : W → X → Prop)
    (w : W) : Prop :=
  ∀ A : Set W, CoversComposites prime pass A → w ∈ A

/-- Exclusive collision implies mandatory witness. -/
theorem forcedWitness_mandatory
    {X W : Type*}
    {prime : X → Prop}
    {pass : W → X → Prop}
    {w : W}
    (hForced : ForcedWitness prime pass w) :
    MandatoryWitness prime pass w := by
  intro A hCover
  obtain ⟨x, hxComposite, hwRejects, hOthersPass⟩ := hForced
  obtain ⟨v, hvA, hvRejects⟩ := hCover x hxComposite
  have hvEq : v = w := by
    by_contra hvNe
    exact hvRejects (hOthersPass v hvNe)
  simpa [hvEq] using hvA

/-- If the full witness universe covers every composite, every mandatory witness
has an exclusive composite collision.  Otherwise removing it would still leave
a cover. -/
theorem mandatoryWitness_forced
    {X W : Type*}
    {prime : X → Prop}
    {pass : W → X → Prop}
    {w : W}
    (hUniverse : CoversComposites prime pass (Set.univ : Set W))
    (hMandatory : MandatoryWitness prime pass w) :
    ForcedWitness prime pass w := by
  classical
  by_contra hNotForced
  let A : Set W := {v | v ≠ w}
  have hRemove : CoversComposites prime pass A := by
    intro x hxComposite
    obtain ⟨v, hvUniverse, hvRejects⟩ := hUniverse x hxComposite
    clear hvUniverse
    by_cases hvEq : v = w
    · subst v
      have hReplacement : ∃ u, u ≠ w ∧ ¬ pass u x := by
        by_contra hNoReplacement
        have hOthersPass : ∀ u, u ≠ w → pass u x := by
          intro u huNe
          by_contra huRejects
          exact hNoReplacement ⟨u, huNe, huRejects⟩
        exact hNotForced ⟨x, hxComposite, hvRejects, hOthersPass⟩
      obtain ⟨u, huNe, huRejects⟩ := hReplacement
      exact ⟨u, huNe, huRejects⟩
    · exact ⟨v, hvEq, hvRejects⟩
  have hwA : w ∈ A := hMandatory A hRemove
  have hwNe : w ≠ w := by
    simpa [A] using hwA
  exact hwNe rfl

/-- In a witness universe that is itself safe, "mandatory" and "has an
exclusive collision" are the same notion. -/
theorem mandatoryWitness_iff_forcedWitness
    {X W : Type*}
    {prime : X → Prop}
    {pass : W → X → Prop}
    {w : W}
    (hUniverse : CoversComposites prime pass (Set.univ : Set W)) :
    MandatoryWitness prime pass w ↔ ForcedWitness prime pass w := by
  constructor
  · exact mandatoryWitness_forced hUniverse
  · exact forcedWitness_mandatory

/-- The set of all witnesses forced by exclusive composite collisions. -/
def ForcedBasis
    {X W : Type*}
    (prime : X → Prop)
    (pass : W → X → Prop) : Set W :=
  {w | ForcedWitness prime pass w}

/-- Every safe family contains the forced basis. -/
theorem forcedBasis_subset_of_cover
    {X W : Type*}
    {prime : X → Prop}
    {pass : W → X → Prop}
    {A : Set W}
    (hCover : CoversComposites prime pass A) :
    ForcedBasis prime pass ⊆ A := by
  intro w hwForced
  exact forcedWitness_mandatory hwForced A hCover

/-- Residual composites are those still not rejected by the forced basis. -/
def ResidualComposite
    {X W : Type*}
    (prime : X → Prop)
    (pass : W → X → Prop)
    (x : X) : Prop :=
  ¬ prime x ∧ ∀ w, w ∈ ForcedBasis prime pass → pass w x

/-- Exact forced-core / residual-choice decomposition of safe witness families.

Every safe family contains the forced basis.  After that mandatory core is
fixed, the only remaining obligation is to hit every residual composite with a
non-forced witness. -/
theorem coversComposites_iff_forcedCore_and_residual
    {X W : Type*}
    {prime : X → Prop}
    {pass : W → X → Prop}
    {A : Set W} :
    CoversComposites prime pass A ↔
      ForcedBasis prime pass ⊆ A ∧
      ∀ x, ResidualComposite prime pass x →
        ∃ w, w ∈ A ∧ w ∉ ForcedBasis prime pass ∧ ¬ pass w x := by
  classical
  constructor
  · intro hCover
    refine ⟨forcedBasis_subset_of_cover hCover, ?_⟩
    intro x hxResidual
    obtain ⟨hxComposite, hForcedPass⟩ := hxResidual
    obtain ⟨w, hwA, hwRejects⟩ := hCover x hxComposite
    have hwNotForced : w ∉ ForcedBasis prime pass := by
      intro hwForced
      exact hwRejects (hForcedPass w hwForced)
    exact ⟨w, hwA, hwNotForced, hwRejects⟩
  · rintro ⟨hForcedSub, hResidualCover⟩ x hxComposite
    by_cases hCoreRejects : ∃ w, w ∈ ForcedBasis prime pass ∧ ¬ pass w x
    · obtain ⟨w, hwForced, hwRejects⟩ := hCoreRejects
      exact ⟨w, hForcedSub hwForced, hwRejects⟩
    · have hForcedPass : ∀ w, w ∈ ForcedBasis prime pass → pass w x := by
        intro w hwForced
        by_contra hwRejects
        exact hCoreRejects ⟨w, hwForced, hwRejects⟩
      obtain ⟨w, hwA, hwNotForced, hwRejects⟩ :=
        hResidualCover x ⟨hxComposite, hForcedPass⟩
      clear hwNotForced
      exact ⟨w, hwA, hwRejects⟩

/-- The forced basis covers every composite exactly when no residual composite
survives it. -/
theorem forcedBasis_covers_iff_noResidual
    {X W : Type*}
    {prime : X → Prop}
    {pass : W → X → Prop} :
    CoversComposites prime pass (ForcedBasis prime pass) ↔
      ∀ x, ¬ ResidualComposite prime pass x := by
  classical
  constructor
  · intro hCover x
    rintro ⟨hxComposite, hAllForcedPass⟩
    obtain ⟨w, hwForced, hwRejects⟩ := hCover x hxComposite
    exact hwRejects (hAllForcedPass w hwForced)
  · intro hNoResidual x hxComposite
    by_contra hNoRejector
    have hAllForcedPass :
        ∀ w, w ∈ ForcedBasis prime pass → pass w x := by
      intro w hwForced
      by_contra hwRejects
      exact hNoRejector ⟨w, hwForced, hwRejects⟩
    exact hNoResidual x ⟨hxComposite, hAllForcedPass⟩

/-- Exact least-basis criterion.

If the full witness universe covers the composites, a least safe witness family
exists exactly when the forced basis itself covers the composites.  When it
exists, the forced basis is the unique least family under inclusion. -/
theorem exists_least_cover_iff_forcedBasis_covers
    {X W : Type*}
    {prime : X → Prop}
    {pass : W → X → Prop}
    (hUniverse : CoversComposites prime pass (Set.univ : Set W)) :
    (∃ B : Set W,
      CoversComposites prime pass B ∧
      ∀ A : Set W, CoversComposites prime pass A → B ⊆ A) ↔
      CoversComposites prime pass (ForcedBasis prime pass) := by
  classical
  constructor
  · rintro ⟨B, hBCover, hBLeast⟩
    have hBSubForced : B ⊆ ForcedBasis prime pass := by
      intro w hwB
      have hMandatory : MandatoryWitness prime pass w := by
        intro A hACover
        exact hBLeast A hACover hwB
      exact (mandatoryWitness_iff_forcedWitness hUniverse).1 hMandatory
    have hForcedSubB : ForcedBasis prime pass ⊆ B :=
      forcedBasis_subset_of_cover hBCover
    have hEq : B = ForcedBasis prime pass :=
      Set.Subset.antisymm hBSubForced hForcedSubB
    simpa [hEq] using hBCover
  · intro hForcedCover
    refine ⟨ForcedBasis prime pass, hForcedCover, ?_⟩
    intro A hACover
    exact forcedBasis_subset_of_cover hACover

/-- Under a safe full witness universe, a least safe witness family exists
exactly when the forced core leaves no residual composite fiber. -/
theorem exists_least_cover_iff_noResidual
    {X W : Type*}
    {prime : X → Prop}
    {pass : W → X → Prop}
    (hUniverse : CoversComposites prime pass (Set.univ : Set W)) :
    (∃ B : Set W,
      CoversComposites prime pass B ∧
      ∀ A : Set W, CoversComposites prime pass A → B ⊆ A) ↔
      ∀ x, ¬ ResidualComposite prime pass x := by
  rw [exists_least_cover_iff_forcedBasis_covers hUniverse]
  exact forcedBasis_covers_iff_noResidual

/-- Binary observation refinement is kernel inclusion: equality under `f`
forces equality under `g`. -/
def BinaryRefines
    {X : Type*}
    (f g : X → Prop) : Prop :=
  ∀ x y, (f x ↔ f y) → (g x ↔ g y)

/-- `f` is at least as strong a pass-filter as `g` when every `f`-pass also
passes `g`; equivalently the pass set of `f` is contained in that of `g`. -/
def PassStronger
    {X : Type*}
    (f g : X → Prop) : Prop :=
  ∀ x, f x → g x

/-- T-A3.  Strict pass-set inclusion does not, under the ordinary nondegenerate
hypotheses, induce refinement between the corresponding one-bit partitions.

If `f` has a strictly smaller pass set than `g`, some state passes `f`, and
some state fails `g`, then the `f` and `g` binary partitions are incomparable. -/
theorem strictPassInclusion_binaryPartitions_incomparable
    {X : Type*}
    {f g : X → Prop}
    (hSub : PassStronger f g)
    (hStrict : ∃ x, g x ∧ ¬ f x)
    (hStrongPass : ∃ x, f x)
    (hWeakFail : ∃ x, ¬ g x) :
    ¬ BinaryRefines f g ∧ ¬ BinaryRefines g f := by
  constructor
  · intro hRefines
    obtain ⟨x, hxG, hxNotF⟩ := hStrict
    obtain ⟨z, hzNotG⟩ := hWeakFail
    have hzNotF : ¬ f z := by
      intro hzF
      exact hzNotG (hSub z hzF)
    have hSameF : f x ↔ f z := by
      constructor
      · intro hxF
        exact False.elim (hxNotF hxF)
      · intro hzF
        exact False.elim (hzNotF hzF)
    have hSameG := hRefines x z hSameF
    exact hzNotG (hSameG.mp hxG)
  · intro hRefines
    obtain ⟨x, hxG, hxNotF⟩ := hStrict
    obtain ⟨y, hyF⟩ := hStrongPass
    have hyG : g y := hSub y hyF
    have hSameG : g x ↔ g y := by
      constructor
      · intro _
        exact hyG
      · intro _
        exact hxG
    have hSameF := hRefines x y hSameG
    exact hxNotF (hSameF.mpr hyF)

end EnterpriseMath.Prime
