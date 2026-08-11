import Mathlib.Data.Set.Lattice
import Mathlib.Data.List.Basic
import Mathlib.Tactic

namespace EnterpriseMath.BranchRecoalescence

open Set

/-- A homogeneous binary relation on fine states. -/
abbrev Rel (X : Type*) := X → X → Prop

/-- Existential/direct image of a set under a relation. -/
def relImage {X : Type*} (R : Rel X) (A : Set X) : Set X :=
  {y | ∃ x, x ∈ A ∧ R x y}

/-- The graph relation of a deterministic map. -/
def graphRel {X : Type*} (f : X → X) : Rel X :=
  fun x y => f x = y

@[simp] theorem relImage_empty {X : Type*} (R : Rel X) :
    relImage R (∅ : Set X) = ∅ := by
  ext y
  simp [relImage]

/-- Relational direct image preserves binary unions. -/
theorem relImage_union {X : Type*} (R : Rel X) (A B : Set X) :
    relImage R (A ∪ B) = relImage R A ∪ relImage R B := by
  ext y
  constructor
  · rintro ⟨x, hx, hxy⟩
    rcases hx with hxA | hxB
    · exact Or.inl ⟨x, hxA, hxy⟩
    · exact Or.inr ⟨x, hxB, hxy⟩
  · intro hy
    rcases hy with hyA | hyB
    · rcases hyA with ⟨x, hxA, hxy⟩
      exact ⟨x, Or.inl hxA, hxy⟩
    · rcases hyB with ⟨x, hxB, hxy⟩
      exact ⟨x, Or.inr hxB, hxy⟩

/-- Deterministic graph image agrees with ordinary set image. -/
theorem relImage_graph_eq_image {X : Type*} (f : X → X) (A : Set X) :
    relImage (graphRel f) A = f '' A := by
  ext y
  constructor
  · rintro ⟨x, hx, hxy⟩
    exact ⟨x, hx, hxy⟩
  · rintro ⟨x, hx, rfl⟩
    exact ⟨x, hx, rfl⟩

/-- Execute a finite word of relation generators from left to right. -/
def runWord {X G : Type*} (step : G → Rel X) : List G → Set X → Set X
  | [], A => A
  | g :: w, A => runWord step w (relImage (step g) A)

/-- Set-valued observable support. -/
def observeSupport {X O : Type*} (obs : X → O) (A : Set X) : Set O :=
  obs '' A

/-- A declared future language is an index family of finite words. -/
abbrev FutureLanguage (G V : Type*) := V → List G

/-- Remaining/future support signature of an exact support. -/
def supportSignature {X G O V : Type*}
    (step : G → Rel X) (obs : X → O) (language : FutureLanguage G V)
    (A : Set X) : V → Set O :=
  fun v => observeSupport obs (runWord step (language v) A)

/-- Declared future signature of a fine point. -/
def pointSignature {X G O V : Type*}
    (step : G → Rel X) (obs : X → O) (language : FutureLanguage G V)
    (x : X) : V → Set O :=
  supportSignature step obs language ({x} : Set X)

/-- `target` is computed only from the complete runtime encoding `encoder`. -/
def Recovers {X E Y : Type*} (encoder : X → E) (target : X → Y) : Prop :=
  ∃ decode : E → Y, ∀ x, decode (encoder x) = target x

/-- Kernel refinement induced by factorization through a complete runtime encoder.
This is the exact information-theoretic content of `NO_RESURRECTION`. -/
theorem noResurrection {X E Y : Type*} {encoder : X → E} {target : X → Y}
    (h : Recovers encoder target) {x y : X} (hxy : encoder x = encoder y) :
    target x = target y := by
  rcases h with ⟨decode, hdecode⟩
  rw [← hdecode x, ← hdecode y, hxy]

/-- Contrapositive form of `NO_RESURRECTION`. -/
theorem noResurrection_ne {X E Y : Type*} {encoder : X → E} {target : X → Y}
    (h : Recovers encoder target) {x y : X} (hxy : target x ≠ target y) :
    encoder x ≠ encoder y := by
  intro henc
  exact hxy (noResurrection h henc)

/-- Specialization of `NO_RESURRECTION` to declared pointwise support signatures. -/
theorem pointSignature_noResurrection {X G O V E : Type*}
    (step : G → Rel X) (obs : X → O) (language : FutureLanguage G V)
    (encoder : X → E)
    (h : Recovers encoder (pointSignature step obs language))
    {x y : X} (hxy : encoder x = encoder y) :
    pointSignature step obs language x = pointSignature step obs language y :=
  noResurrection h hxy

/-- Coarse successor-support signature for one relational generator. -/
def coarseSuccessorSupport {X Q : Type*} (q : X → Q) (R : Rel X) (x : X) : Set Q :=
  observeSupport q (relImage R ({x} : Set X))

/-- The one-step deterministic repair key `(q(x), sigma(x))`. -/
def oneStepKey {X Q S : Type*} (q : X → Q) (sigma : X → S) (x : X) : Q × S :=
  (q x, sigma x)

/-- A classifier is sufficient for the one-step interface when both current coarse
observation and successor-support signature can be recovered from it. -/
def OneStepSufficient {X C Q S : Type*}
    (classifier : X → C) (q : X → Q) (sigma : X → S) : Prop :=
  Recovers classifier q ∧ Recovers classifier sigma

/-- The pair key itself recovers both components. -/
theorem oneStepKey_sufficient {X Q S : Type*} (q : X → Q) (sigma : X → S) :
    OneStepSufficient (oneStepKey q sigma) q sigma := by
  constructor
  · refine ⟨Prod.fst, ?_⟩
    intro x
    rfl
  · refine ⟨Prod.snd, ?_⟩
    intro x
    rfl

/-- Every classifier sufficient for both components factors onto the pair key. -/
theorem oneStepKey_recovers_of_sufficient {X C Q S : Type*}
    {classifier : X → C} {q : X → Q} {sigma : X → S}
    (h : OneStepSufficient classifier q sigma) :
    Recovers classifier (oneStepKey q sigma) := by
  rcases h.1 with ⟨decodeQ, hQ⟩
  rcases h.2 with ⟨decodeS, hS⟩
  refine ⟨fun c => (decodeQ c, decodeS c), ?_⟩
  intro x
  simp [oneStepKey, hQ x, hS x]

/-- `ONE_STEP_COARSEST`: `(q,sigma)` is sufficient, and every other sufficient
classifier refines it in the factorization/kernel sense. No injectivity,
surjectivity, finiteness, or partition library is required. -/
theorem oneStepCoarsest {X Q S : Type*} (q : X → Q) (sigma : X → S) :
    OneStepSufficient (oneStepKey q sigma) q sigma ∧
      ∀ (C : Type*) (classifier : X → C),
        OneStepSufficient classifier q sigma →
          Recovers classifier (oneStepKey q sigma) := by
  constructor
  · exact oneStepKey_sufficient q sigma
  · intro C classifier h
    exact oneStepKey_recovers_of_sufficient h

/-- Exact R021 specialization: the one-step key uses current coarse observation
and the next coarse successor-support under the declared relation. -/
theorem oneStepCoarseSuccessorCoarsest {X Q : Type*} (q : X → Q) (R : Rel X) :
    OneStepSufficient
        (oneStepKey q (coarseSuccessorSupport q R))
        q (coarseSuccessorSupport q R) ∧
      ∀ (C : Type*) (classifier : X → C),
        OneStepSufficient classifier q (coarseSuccessorSupport q R) →
          Recovers classifier
            (oneStepKey q (coarseSuccessorSupport q R)) :=
  oneStepCoarsest q (coarseSuccessorSupport q R)

/-- Kernel form of the coarsest universal property. -/
theorem oneStepCoarsest_kernel {X C Q S : Type*}
    {classifier : X → C} {q : X → Q} {sigma : X → S}
    (h : OneStepSufficient classifier q sigma)
    {x y : X} (hxy : classifier x = classifier y) :
    oneStepKey q sigma x = oneStepKey q sigma y :=
  noResurrection (oneStepKey_recovers_of_sufficient h) hxy

/-- Canonical exact branch atom: the token denotes exactly the represented support. -/
abbrev ExactBranch (X : Type*) := Set X

/-- A finite live branch configuration. -/
abbrev BranchConfig (X : Type*) := List (ExactBranch X)

/-- Exact denotation of a live branch configuration: union of all branch supports. -/
def configSupport {X : Type*} : BranchConfig X → Set X
  | [] => ∅
  | A :: rest => A ∪ configSupport rest

/-- Execute every exact branch by relational direct image. -/
def executeConfig {X : Type*} (R : Rel X) (cfg : BranchConfig X) : BranchConfig X :=
  cfg.map (relImage R)

/-- Lossless recoalescence: replace all live branches by one token denoting their
literal union. -/
def exactRecoalesce {X : Type*} (cfg : BranchConfig X) : BranchConfig X :=
  [configSupport cfg]

@[simp] theorem configSupport_exactRecoalesce {X : Type*} (cfg : BranchConfig X) :
    configSupport (exactRecoalesce cfg) = configSupport cfg := by
  simp [exactRecoalesce, configSupport]

/-- Executing each exact branch and then taking the configuration union is the
same as executing the union directly. -/
theorem configSupport_executeConfig {X : Type*} (R : Rel X) :
    ∀ cfg : BranchConfig X,
      configSupport (executeConfig R cfg) = relImage R (configSupport cfg) := by
  intro cfg
  induction cfg with
  | nil =>
      simp [executeConfig, configSupport]
  | cons A rest ih =>
      change relImage R A ∪ configSupport (executeConfig R rest) =
        relImage R (A ∪ configSupport rest)
      rw [ih, relImage_union]

/-- A runtime split policy is exact when every split preserves the denoted support. -/
def SupportPreservingSplit {X G : Type*}
    (split : G → BranchConfig X → BranchConfig X) : Prop :=
  ∀ g cfg, configSupport (split g cfg) = configSupport cfg

/-- One concrete exact binary split of a support by a predicate. -/
def splitBy {X : Type*} (p : X → Prop) (A : Set X) : BranchConfig X :=
  [A ∩ {x | p x}, A \ {x | p x}]

/-- The concrete predicate split is lossless at the Boolean-support level. -/
theorem configSupport_splitBy {X : Type*} (p : X → Prop) (A : Set X) :
    configSupport (splitBy p A) = A := by
  classical
  ext x
  simp [splitBy, configSupport]

/-- Split, execute, and exact-union recoalesce after each generator. -/
def branchRun {X G : Type*}
    (step : G → Rel X) (split : G → BranchConfig X → BranchConfig X) :
    List G → BranchConfig X → BranchConfig X
  | [], cfg => cfg
  | g :: w, cfg =>
      branchRun step split w
        (exactRecoalesce (executeConfig (step g) (split g cfg)))

/-- `SUPPORT_BRANCH_INVARIANT`: any support-preserving split policy followed by
relational execution and literal-union recoalescence preserves the exact fine
reachable support for every finite word. -/
theorem supportBranchInvariant {X G : Type*}
    (step : G → Rel X) (split : G → BranchConfig X → BranchConfig X)
    (hsplit : SupportPreservingSplit split) :
    ∀ (w : List G) (cfg : BranchConfig X),
      configSupport (branchRun step split w cfg) =
        runWord step w (configSupport cfg) := by
  intro w
  induction w with
  | nil =>
      intro cfg
      rfl
  | cons g w ih =>
      intro cfg
      simp only [branchRun, runWord]
      rw [ih]
      rw [configSupport_exactRecoalesce, configSupport_executeConfig, hsplit g cfg]

/-- Observable corollary of `SUPPORT_BRANCH_INVARIANT`: exact fine-support
preservation immediately preserves every declared set-valued final observation. -/
theorem supportBranchObservableInvariant {X G O : Type*}
    (step : G → Rel X) (split : G → BranchConfig X → BranchConfig X)
    (hsplit : SupportPreservingSplit split) (obs : X → O)
    (w : List G) (cfg : BranchConfig X) :
    observeSupport obs (configSupport (branchRun step split w cfg)) =
      observeSupport obs (runWord step w (configSupport cfg)) := by
  rw [supportBranchInvariant step split hsplit w cfg]

/-- Operational suffix safety: every declared remaining word gives the same
final observable support from the exact support `A` and replacement `H`. -/
def SuffixSafe {X G O V : Type*}
    (step : G → Rel X) (obs : X → O) (language : FutureLanguage G V)
    (A H : Set X) : Prop :=
  ∀ v, observeSupport obs (runWord step (language v) A) =
    observeSupport obs (runWord step (language v) H)

/-- `FORGETFUL_RECOALESCENCE_IFF`: operational suffix safety is exactly equality
of the packaged remaining support signatures. The operational condition is
introduced independently before the signature equality theorem. -/
theorem forgetfulRecoalescence_iff {X G O V : Type*}
    (step : G → Rel X) (obs : X → O) (language : FutureLanguage G V)
    (A H : Set X) :
    SuffixSafe step obs language A H ↔
      supportSignature step obs language A = supportSignature step obs language H := by
  constructor
  · intro h
    funext v
    exact h v
  · intro h v
    exact congrFun h v

/-- Existential quotient/lift of a homogeneous relation through a coarse map. -/
def quotientRel {X Q : Type*} (q : X → Q) (R : Rel X) : Rel Q :=
  fun a b => ∃ x y, q x = a ∧ q y = b ∧ R x y

/-- Typed existential quotient of a relation between different state spaces. -/
def quotientRelBetween {A B QA QB : Type*}
    (qA : A → QA) (qB : B → QB) (R : A → B → Prop) : QA → QB → Prop :=
  fun qa qb => ∃ a b, qA a = qa ∧ qB b = qb ∧ R a b

/-- Ordinary relational composition, retaining the shared middle witness. -/
def relComp {A B C : Type*} (R : A → B → Prop) (S : B → C → Prop) : A → C → Prop :=
  fun a c => ∃ b, R a b ∧ S b c

namespace Counterexamples

inductive Fine3 where
  | x0 | x1 | x2
  deriving DecidableEq

inductive Coarse2 where
  | q0 | q1
  deriving DecidableEq

open Fine3 Coarse2

def q3 : Fine3 → Coarse2
  | x0 => q0
  | x1 => q0
  | x2 => q1

def f3 : Fine3 → Fine3
  | x0 => x0
  | x1 => x2
  | x2 => x0

def fRel3 : Rel Fine3 := graphRel f3

def fullFiber0 : Set Fine3 := {x | q3 x = q0}

def coarseStart0 : Set Coarse2 := {q0}

def twoSteps : List Unit := [(), ()]

/-- The full fine fibre over coarse state `0` is exactly `{0,1}`. -/
theorem fullFiber0_eq : fullFiber0 = ({x0, x1} : Set Fine3) := by
  ext x
  cases x <;> simp [fullFiber0, q3]

theorem fine_first_step : relImage fRel3 fullFiber0 = ({x0, x2} : Set Fine3) := by
  rw [fullFiber0_eq]
  change relImage (graphRel f3) ({x0, x1} : Set Fine3) = ({x0, x2} : Set Fine3)
  rw [relImage_graph_eq_image]
  ext x
  cases x <;> simp [f3]

theorem fine_second_step :
    relImage fRel3 (relImage fRel3 fullFiber0) = ({x0} : Set Fine3) := by
  rw [fine_first_step]
  change relImage (graphRel f3) ({x0, x2} : Set Fine3) = ({x0} : Set Fine3)
  rw [relImage_graph_eq_image]
  ext x
  cases x <;> simp [f3]

/-- Exact two-step fine execution from the full `q=0` fibre reaches only `x0`. -/
theorem threeState_fine_twoStep_support :
    runWord (fun _ : Unit => fRel3) twoSteps fullFiber0 = ({x0} : Set Fine3) := by
  simpa [twoSteps, runWord] using fine_second_step

/-- One exact fine step has coarse support `{0,1}`. -/
theorem threeState_fine_oneStep_coarseSupport :
    observeSupport q3 (relImage fRel3 fullFiber0) =
      ({q0, q1} : Set Coarse2) := by
  rw [fine_first_step]
  ext q
  cases q <;> simp [observeSupport, q3]

/-- Therefore exact two-step fine execution has final coarse support `{0}`. -/
theorem threeState_fine_twoStep_coarseSupport :
    observeSupport q3 (runWord (fun _ : Unit => fRel3) twoSteps fullFiber0) =
      ({q0} : Set Coarse2) := by
  rw [threeState_fine_twoStep_support]
  simp [observeSupport, q3]

private theorem quotient_q0_q0 : quotientRel q3 fRel3 q0 q0 := by
  exact ⟨x0, x0, rfl, rfl, rfl⟩

private theorem quotient_q0_q1 : quotientRel q3 fRel3 q0 q1 := by
  exact ⟨x1, x2, rfl, rfl, rfl⟩

private theorem quotient_q1_q0 : quotientRel q3 fRel3 q1 q0 := by
  exact ⟨x2, x0, rfl, rfl, rfl⟩

/-- The naive existential quotient already reaches both coarse states in one step. -/
theorem threeState_quotient_first_full :
    relImage (quotientRel q3 fRel3) coarseStart0 = (Set.univ : Set Coarse2) := by
  ext y
  constructor
  · intro _
    simp
  · intro _
    cases y with
    | q0 =>
        exact ⟨q0, by simp [coarseStart0], quotient_q0_q0⟩
    | q1 =>
        exact ⟨q0, by simp [coarseStart0], quotient_q0_q1⟩

/-- From the coarse universal support, the naive quotient still reaches both states. -/
theorem threeState_quotient_univ_full :
    relImage (quotientRel q3 fRel3) (Set.univ : Set Coarse2) = Set.univ := by
  ext y
  constructor
  · intro _
    simp
  · intro _
    cases y with
    | q0 =>
        exact ⟨q0, by simp, quotient_q0_q0⟩
    | q1 =>
        exact ⟨q0, by simp, quotient_q0_q1⟩

/-- The existential quotient is one-step exact on the chosen full starting fibre. -/
theorem threeState_oneStep_exact :
    observeSupport q3 (relImage fRel3 fullFiber0) =
      relImage (quotientRel q3 fRel3) coarseStart0 := by
  rw [threeState_fine_oneStep_coarseSupport, threeState_quotient_first_full]
  ext y
  cases y <;> simp

/-- Two repeated applications of the naive existential quotient reach `{0,1}`. -/
theorem threeState_quotient_twoStep_coarseSupport :
    runWord (fun _ : Unit => quotientRel q3 fRel3) twoSteps coarseStart0 =
      ({q0, q1} : Set Coarse2) := by
  have huniv : (Set.univ : Set Coarse2) = ({q0, q1} : Set Coarse2) := by
    ext y
    cases y <;> simp
  simp only [twoSteps, runWord]
  rw [threeState_quotient_first_full, threeState_quotient_univ_full, huniv]

/-- Explicit spurious state admitted only by repeated coarse quotient composition. -/
theorem threeState_composition_spurious_q1 :
    q1 ∈ runWord (fun _ : Unit => quotientRel q3 fRel3) twoSteps coarseStart0 ∧
      q1 ∉ observeSupport q3
        (runWord (fun _ : Unit => fRel3) twoSteps fullFiber0) := by
  constructor
  · rw [threeState_quotient_twoStep_coarseSupport]
    simp
  · rw [threeState_fine_twoStep_coarseSupport]
    simp

/-- One declared remaining suffix consisting of one application of `f`. -/
def oneStepLanguage : FutureLanguage Unit Unit :=
  fun _ => [()]

theorem singleton_current_coarse :
    observeSupport q3 ({x0} : Set Fine3) = ({q0} : Set Coarse2) := by
  simp [observeSupport, q3]

theorem hull_current_coarse :
    observeSupport q3 ({x0, x1} : Set Fine3) = ({q0} : Set Coarse2) := by
  ext q
  cases q <;> simp [observeSupport, q3]

theorem singleton_future_coarse :
    observeSupport q3
        (runWord (fun _ : Unit => fRel3) [()] ({x0} : Set Fine3)) =
      ({q0} : Set Coarse2) := by
  simp [runWord, relImage_graph_eq_image, fRel3, f3, observeSupport, q3]

theorem hull_future_coarse :
    observeSupport q3
        (runWord (fun _ : Unit => fRel3) [()] ({x0, x1} : Set Fine3)) =
      ({q0, q1} : Set Coarse2) := by
  change observeSupport q3 (relImage fRel3 ({x0, x1} : Set Fine3)) =
    ({q0, q1} : Set Coarse2)
  rw [← fullFiber0_eq]
  exact threeState_fine_oneStep_coarseSupport

/-- Equality of the current coarse observation alone does not imply suffix safety. -/
theorem sameCurrentCoarse_notSuffixSafe :
    observeSupport q3 ({x0} : Set Fine3) =
        observeSupport q3 ({x0, x1} : Set Fine3) ∧
      ¬ SuffixSafe (fun _ : Unit => fRel3) q3 oneStepLanguage
        ({x0} : Set Fine3) ({x0, x1} : Set Fine3) := by
  constructor
  · rw [singleton_current_coarse, hull_current_coarse]
  · intro hsafe
    have hs := hsafe ()
    have heq : ({q0} : Set Coarse2) = ({q0, q1} : Set Coarse2) := by
      calc
        ({q0} : Set Coarse2) =
            observeSupport q3
              (runWord (fun _ : Unit => fRel3) [()] ({x0} : Set Fine3)) :=
          singleton_future_coarse.symm
        _ = observeSupport q3
              (runWord (fun _ : Unit => fRel3) [()] ({x0, x1} : Set Fine3)) := by
          simpa [oneStepLanguage] using hs
        _ = ({q0, q1} : Set Coarse2) := hull_future_coarse
    have hmem : q1 ∈ ({q0} : Set Coarse2) := by
      rw [heq]
      simp
    have hcontra : q1 = q0 := by
      simpa only [Set.mem_singleton_iff] using hmem
    cases hcontra

inductive Middle where
  | b1 | b2
  deriving DecidableEq

open Middle

/-- First relation reaches only middle witness `b1`. -/
def firstMiddle : Unit → Middle → Prop :=
  fun _ b => b = b1

/-- Second relation departs only from distinct middle witness `b2`. -/
def secondMiddle : Middle → Unit → Prop :=
  fun b _ => b = b2

/-- Exact composition is empty because the middle witness must be identical. -/
theorem middleIncidence_exact_empty :
    ¬ relComp firstMiddle secondMiddle () () := by
  rintro ⟨b, hfirst, hsecond⟩
  cases b <;> simp [firstMiddle, secondMiddle] at hfirst hsecond

private def coarseFirstMiddle : Unit → Unit → Prop :=
  quotientRelBetween (fun _ : Unit => ()) (fun _ : Middle => ()) firstMiddle

private def coarseSecondMiddle : Unit → Unit → Prop :=
  quotientRelBetween (fun _ : Middle => ()) (fun _ : Unit => ()) secondMiddle

private theorem coarseFirstMiddle_edge : coarseFirstMiddle () () := by
  exact ⟨(), b1, rfl, rfl, rfl⟩

private theorem coarseSecondMiddle_edge : coarseSecondMiddle () () := by
  exact ⟨b2, (), rfl, rfl, rfl⟩

/-- After erasing middle identity, both nonempty coarse marginals compose and create
an existential result that the exact relational composition does not have. -/
theorem middleIncidence_coarse_spurious :
    relComp coarseFirstMiddle coarseSecondMiddle () () := by
  exact ⟨(), coarseFirstMiddle_edge, coarseSecondMiddle_edge⟩

end Counterexamples

end EnterpriseMath.BranchRecoalescence
