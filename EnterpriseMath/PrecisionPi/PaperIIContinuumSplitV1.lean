import EnterpriseMath.PrecisionPi.PaperIIResidualClassificationV1

namespace EnterpriseMath.PrecisionPi.PaperIIContinuumSplitV1

open EnterpriseMath.PrecisionPi.PaperIIKernelV1
open EnterpriseMath.PrecisionPi.PaperIIResidualClassificationV1

/-! ## 1. Real slice-to-line geometry -/

/-- Real-valued four-slice data. -/
abbrev VertexDataR := Fin 4 → ℝ

/-- Real-valued six-line data. -/
abbrev EdgeDataR := Fin 6 → ℝ

/-- Three real opposite-pair coordinates. -/
abbrev MatchingDataR := Fin 3 → ℝ

/-- Total real slice weight. -/
def vertexSumR (v : VertexDataR) : ℝ :=
  v 0 + v 1 + v 2 + v 3

/-- Total real edge weight. -/
def edgeSumR (x : EdgeDataR) : ℝ :=
  x 0 + x 1 + x 2 + x 3 + x 4 + x 5

/-- Real extension of the tetrahedral slice-to-line incidence map. -/
def deltaR (v : VertexDataR) : EdgeDataR :=
  ![v 0 + v 1, v 0 + v 2, v 0 + v 3,
    v 1 + v 2, v 1 + v 3, v 2 + v 3]

/-- Coordinatewise subtraction of real edge states. -/
def edgeSubR (x y : EdgeDataR) : EdgeDataR := fun i => x i - y i

/-- The three opposite-edge matching sums over the reals. -/
def matchingR (x : EdgeDataR) : MatchingDataR :=
  ![x 0 + x 5, x 1 + x 4, x 2 + x 3]

/-- Antisymmetric opposite-pair kernel pattern over the reals. -/
def patternR (a b c : ℝ) : EdgeDataR :=
  ![a, b, c, -c, -b, -a]

/-- The real incidence map triples total slice weight. -/
theorem edgeSumR_deltaR (v : VertexDataR) :
    edgeSumR (deltaR v) = 3 * vertexSumR v := by
  simp [edgeSumR, deltaR, vertexSumR]
  ring

/-- A zero-sum real slice potential contributes no opposite-pair residual. -/
theorem matchingR_deltaR_of_zero_sum
    {v : VertexDataR} (hv : vertexSumR v = 0) :
    matchingR (deltaR v) = 0 := by
  have hv' : v 0 + v 1 + v 2 + v 3 = 0 := by
    simpa [vertexSumR] using hv
  funext i
  fin_cases i <;> simp [matchingR, deltaR] <;> linarith

@[simp] theorem edgeSumR_patternR (a b c : ℝ) :
    edgeSumR (patternR a b c) = 0 := by
  simp [edgeSumR, patternR]

@[simp] theorem matchingR_patternR (a b c : ℝ) :
    matchingR (patternR a b c) = 0 := by
  funext i
  fin_cases i <;> simp [matchingR, patternR]

/-- Vanishing real matching coordinates are exactly the antisymmetric
three-parameter kernel patterns. -/
theorem matchingR_eq_zero_iff_patternR (x : EdgeDataR) :
    matchingR x = 0 ↔ x = patternR (x 0) (x 1) (x 2) := by
  constructor
  · intro h
    have h0 := congrFun h (0 : Fin 3)
    have h1 := congrFun h (1 : Fin 3)
    have h2 := congrFun h (2 : Fin 3)
    simp [matchingR] at h0 h1 h2
    funext i
    fin_cases i <;> simp [patternR] <;> linarith
  · intro h
    rw [h]
    exact matchingR_patternR _ _ _

/-! ## 2. Division by two removes the integral parity obstruction -/

/-- Explicit real zero-sum slice potential for a matching-kernel pattern. -/
def realWitness (a b c : ℝ) : VertexDataR :=
  ![(a + b + c) / 2,
    a - (a + b + c) / 2,
    b - (a + b + c) / 2,
    c - (a + b + c) / 2]

@[simp] theorem vertexSumR_realWitness (a b c : ℝ) :
    vertexSumR (realWitness a b c) = 0 := by
  simp [vertexSumR, realWitness]
  ring

@[simp] theorem deltaR_realWitness (a b c : ℝ) :
    deltaR (realWitness a b c) = patternR a b c := by
  funext i
  fin_cases i <;> simp [deltaR, realWitness, patternR] <;> ring

/-- Over the reals every matching-kernel pattern is slice-induced.  The
integer condition `a+b+c=2k` has disappeared because `k=(a+b+c)/2` is always
available. -/
theorem patternR_in_image (a b c : ℝ) :
    ∃ v : VertexDataR,
      vertexSumR v = 0 ∧ deltaR v = patternR a b c := by
  exact ⟨realWitness a b c, vertexSumR_realWitness a b c,
    deltaR_realWitness a b c⟩

/-! ## 3. Real residual equivalence has no parity coordinate -/

/-- Two real edge states are equivalent when their difference is induced by a
zero-sum real slice potential. -/
def RealDeltaEquivalent (x y : EdgeDataR) : Prop :=
  ∃ v : VertexDataR, vertexSumR v = 0 ∧ deltaR v = edgeSubR x y

/-- Matching coordinates commute with real subtraction. -/
theorem matchingR_edgeSubR (x y : EdgeDataR) :
    matchingR (edgeSubR x y) = fun i => matchingR x i - matchingR y i := by
  funext i
  fin_cases i <;> simp [matchingR, edgeSubR] <;> ring

/-- A real slice-induced difference preserves the three matching coordinates. -/
theorem matchingR_eq_of_realDeltaEquivalent {x y : EdgeDataR}
    (h : RealDeltaEquivalent x y) : matchingR x = matchingR y := by
  rcases h with ⟨v, hv, hd⟩
  have hzero : matchingR (edgeSubR x y) = 0 := by
    rw [← hd]
    exact matchingR_deltaR_of_zero_sum hv
  rw [matchingR_edgeSubR] at hzero
  funext i
  have hi := congrFun hzero i
  simp at hi
  linarith

/-- Equal matching coordinates put the real difference in the matching kernel. -/
theorem matchingR_edgeSubR_eq_zero_of_eq {x y : EdgeDataR}
    (h : matchingR x = matchingR y) : matchingR (edgeSubR x y) = 0 := by
  rw [matchingR_edgeSubR, h]
  funext i
  simp

/-- Complete real classification criterion: equality modulo zero-sum slice
potentials is exactly equality of the two-dimensional matching residual.  No
additional parity condition survives. -/
theorem realDeltaEquivalent_iff_matchingR_eq (x y : EdgeDataR) :
    RealDeltaEquivalent x y ↔ matchingR x = matchingR y := by
  constructor
  · exact matchingR_eq_of_realDeltaEquivalent
  · intro hm
    have hzero := matchingR_edgeSubR_eq_zero_of_eq hm
    have hpattern := (matchingR_eq_zero_iff_patternR (edgeSubR x y)).mp hzero
    rcases patternR_in_image
        (edgeSubR x y 0) (edgeSubR x y 1) (edgeSubR x y 2) with
      ⟨v, hv, hd⟩
    refine ⟨v, hv, ?_⟩
    rw [hpattern]
    exact hd

/-- Real residual equivalence is reflexive. -/
theorem realDeltaEquivalent_refl (x : EdgeDataR) :
    RealDeltaEquivalent x x :=
  (realDeltaEquivalent_iff_matchingR_eq x x).2 rfl

/-- Real residual equivalence is symmetric. -/
theorem realDeltaEquivalent_symm {x y : EdgeDataR}
    (h : RealDeltaEquivalent x y) : RealDeltaEquivalent y x :=
  (realDeltaEquivalent_iff_matchingR_eq y x).2
    ((realDeltaEquivalent_iff_matchingR_eq x y).1 h).symm

/-- Real residual equivalence is transitive. -/
theorem realDeltaEquivalent_trans {x y z : EdgeDataR}
    (hxy : RealDeltaEquivalent x y) (hyz : RealDeltaEquivalent y z) :
    RealDeltaEquivalent x z :=
  (realDeltaEquivalent_iff_matchingR_eq x z).2
    (((realDeltaEquivalent_iff_matchingR_eq x y).1 hxy).trans
      ((realDeltaEquivalent_iff_matchingR_eq y z).1 hyz))

/-- The real residual relation as a setoid. -/
def realDeltaSetoid : Setoid EdgeDataR where
  r := RealDeltaEquivalent
  iseqv := ⟨realDeltaEquivalent_refl, realDeltaEquivalent_symm,
    realDeltaEquivalent_trans⟩

/-! ## 4. Canonical real normal forms and the `R²` quotient -/

/-- Canonical balanced real edge state with two free coordinates. -/
def realNormalForm (p q : ℝ) : EdgeDataR :=
  ![0, 0, 0, -p - q, q, p]

@[simp] theorem edgeSumR_realNormalForm (p q : ℝ) :
    edgeSumR (realNormalForm p q) = 0 := by
  change (0 : ℝ) + 0 + 0 + (-p - q) + q + p = 0
  ring

@[simp] theorem matchingR_realNormalForm (p q : ℝ) :
    matchingR (realNormalForm p q) = ![p, q, -p - q] := by
  funext i
  fin_cases i <;> simp [matchingR, realNormalForm]

/-- Canonical real forms are equivalent exactly when both free coordinates
agree. -/
theorem realNormalForm_equivalent_iff (p q p' q' : ℝ) :
    RealDeltaEquivalent (realNormalForm p q) (realNormalForm p' q') ↔
      p = p' ∧ q = q' := by
  constructor
  · intro h
    have hm := (realDeltaEquivalent_iff_matchingR_eq
      (realNormalForm p q) (realNormalForm p' q')).1 h
    constructor
    · have h0 := congrFun hm (0 : Fin 3)
      simpa using h0
    · have h1 := congrFun hm (1 : Fin 3)
      simpa using h1
  · rintro ⟨rfl, rfl⟩
    exact realDeltaEquivalent_refl _

/-- The matching coordinates sum to total edge weight. -/
theorem matchingR_sum_eq_edgeSumR (x : EdgeDataR) :
    matchingR x 0 + matchingR x 1 + matchingR x 2 = edgeSumR x := by
  simp [matchingR, edgeSumR]
  ring

/-- Every balanced real edge state is equivalent to a unique two-coordinate
normal form. -/
theorem exists_realNormalForm (x : EdgeDataR) (hx : edgeSumR x = 0) :
    ∃ p q : ℝ, RealDeltaEquivalent x (realNormalForm p q) := by
  have hsum := matchingR_sum_eq_edgeSumR x
  have hthird : matchingR x 2 = -matchingR x 0 - matchingR x 1 := by
    rw [hx] at hsum
    linarith
  refine ⟨matchingR x 0, matchingR x 1, ?_⟩
  apply (realDeltaEquivalent_iff_matchingR_eq x
    (realNormalForm (matchingR x 0) (matchingR x 1))).2
  funext i
  fin_cases i
  · simp
  · simp
  · simpa using hthird

/-- Balanced real edge states. -/
abbrev ZeroEdgeR := {x : EdgeDataR // edgeSumR x = 0}

/-- Canonical balanced real representative. -/
def realNormalZeroEdge (p q : ℝ) : ZeroEdgeR :=
  ⟨realNormalForm p q, edgeSumR_realNormalForm p q⟩

/-- Real residual relation restricted to the balanced plane. -/
def zeroRealDeltaSetoid : Setoid ZeroEdgeR where
  r := fun x y => RealDeltaEquivalent x.1 y.1
  iseqv := ⟨fun x => realDeltaEquivalent_refl x.1,
    fun h => realDeltaEquivalent_symm h,
    fun h₁ h₂ => realDeltaEquivalent_trans h₁ h₂⟩

/-- Balanced real residual quotient. -/
abbrev ZeroResidualQuotientR := Quotient zeroRealDeltaSetoid

/-- Quotient class of one real normal form. -/
def realNormalClass (p q : ℝ) : ZeroResidualQuotientR :=
  Quotient.mk zeroRealDeltaSetoid (realNormalZeroEdge p q)

/-- Every real quotient class has a canonical representative. -/
theorem quotientR_exists_normal (Q : ZeroResidualQuotientR) :
    ∃ p q : ℝ, Q = realNormalClass p q := by
  refine Quotient.inductionOn Q ?_
  intro x
  rcases exists_realNormalForm x.1 x.2 with ⟨p, q, h⟩
  exact ⟨p, q, Quotient.sound h⟩

/-- Equality of canonical real quotient representatives is coordinatewise. -/
theorem realNormalClass_eq_iff (p q p' q' : ℝ) :
    realNormalClass p q = realNormalClass p' q' ↔ p = p' ∧ q = q' := by
  constructor
  · intro h
    have hr := Quotient.exact h
    change RealDeltaEquivalent (realNormalForm p q) (realNormalForm p' q') at hr
    exact (realNormalForm_equivalent_iff p q p' q').1 hr
  · rintro ⟨rfl, rfl⟩
    rfl

/-- Coordinate-to-quotient real normal-form map. -/
def realNormalClassMap : (ℝ × ℝ) → ZeroResidualQuotientR :=
  fun c => realNormalClass c.1 c.2

/-- The real normal-form map is bijective. -/
theorem realNormalClassMap_bijective : Function.Bijective realNormalClassMap := by
  constructor
  · rintro ⟨p, q⟩ ⟨p', q'⟩ h
    rcases (realNormalClass_eq_iff p q p' q').1 h with ⟨rfl, rfl⟩
    rfl
  · intro Q
    rcases quotientR_exists_normal Q with ⟨p, q, h⟩
    exact ⟨(p, q), h.symm⟩

/-- Exact set-level classification of the balanced real residual quotient as
`R²`. -/
noncomputable def realNormalCoordinateEquiv :
    (ℝ × ℝ) ≃ ZeroResidualQuotientR :=
  Equiv.ofBijective realNormalClassMap realNormalClassMap_bijective

/-- Paper-facing orientation of the continuum quotient classification. -/
noncomputable def zeroResidualQuotientREquiv :
    ZeroResidualQuotientR ≃ (ℝ × ℝ) :=
  realNormalCoordinateEquiv.symm

/-! ## 5. Exact comparison with the integral `C₂` witness -/

/-- Coordinatewise embedding of integral edge data into real edge data. -/
def castEdge (x : EdgeData) : EdgeDataR := fun i => (x i : ℝ)

/-- Integral kernel patterns embed as the corresponding real patterns. -/
theorem cast_pattern (p q r : ℤ) :
    castEdge (pattern p q r) = patternR (p : ℝ) (q : ℝ) (r : ℝ) := by
  funext i
  fin_cases i <;> simp [castEdge, pattern, patternR]

/-- The primitive integral parity witness has an explicit real zero-sum lift. -/
theorem basicParity_real_lift :
    ∃ v : VertexDataR,
      vertexSumR v = 0 ∧ deltaR v = castEdge (pattern 1 0 0) := by
  rcases patternR_in_image (1 : ℝ) 0 0 with ⟨v, hv, hd⟩
  refine ⟨v, hv, ?_⟩
  calc
    deltaR v = patternR (1 : ℝ) 0 0 := hd
    _ = castEdge (pattern 1 0 0) := (cast_pattern 1 0 0).symm

/-- The same primitive witness is the zero class in the real residual quotient. -/
theorem cast_basicParity_real_equivalent_zero :
    RealDeltaEquivalent (castEdge (pattern 1 0 0)) 0 := by
  rcases basicParity_real_lift with ⟨v, hv, hd⟩
  exact ⟨v, hv, by simpa [edgeSubR] using hd⟩

/-- Every integral canonical representative maps to the real class determined
only by its two free coordinates; the Boolean parity coordinate is forgotten. -/
theorem cast_normalForm_equivalent_realNormalForm
    (p q : ℤ) (ε : Bool) :
    RealDeltaEquivalent (castEdge (normalForm p q ε))
      (realNormalForm (p : ℝ) (q : ℝ)) := by
  apply (realDeltaEquivalent_iff_matchingR_eq
    (castEdge (normalForm p q ε))
    (realNormalForm (p : ℝ) (q : ℝ))).2
  funext i
  fin_cases i <;> cases ε <;>
    simp [matchingR, castEdge, normalForm, bitInt, realNormalForm]

/-- The two integral parity representatives with the same free coordinates
collapse to one real residual class. -/
theorem cast_parity_pair_collapse (p q : ℤ) :
    RealDeltaEquivalent
      (castEdge (normalForm p q false))
      (castEdge (normalForm p q true)) := by
  exact realDeltaEquivalent_trans
    (cast_normalForm_equivalent_realNormalForm p q false)
    (realDeltaEquivalent_symm
      (cast_normalForm_equivalent_realNormalForm p q true))

/-- Machine-level contrast: the primitive parity pattern is not integrally
slice-induced, but it is slice-induced after real completion. -/
theorem c2_disappears_under_real_completion :
    (¬ ∃ v : VertexData,
      vertexSum v = 0 ∧ delta v = pattern 1 0 0) ∧
    (∃ v : VertexDataR,
      vertexSumR v = 0 ∧ deltaR v = castEdge (pattern 1 0 0)) := by
  exact ⟨basic_parity_nonzero, basicParity_real_lift⟩

end EnterpriseMath.PrecisionPi.PaperIIContinuumSplitV1
