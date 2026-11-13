import EnterpriseMath.PrecisionPi.PaperIIK4RotationV1

namespace EnterpriseMath.PrecisionPi.PaperIIResidualCocycleV1

open EnterpriseMath.PrecisionPi.PaperIIKernelV1
open EnterpriseMath.PrecisionPi.PaperIIResidualClassificationV1

/-! ## 1. Three explicit adjacent transpositions of the tetrahedral charts -/

/-- Swap slice vertices `0` and `1`. -/
def swap01Vertex (v : VertexData) : VertexData :=
  ![v 1, v 0, v 2, v 3]

/-- Swap slice vertices `1` and `2`. -/
def swap12Vertex (v : VertexData) : VertexData :=
  ![v 0, v 2, v 1, v 3]

/-- Swap slice vertices `2` and `3`. -/
def swap23Vertex (v : VertexData) : VertexData :=
  ![v 0, v 1, v 3, v 2]

/-- Induced edge-coordinate permutation for the transposition `(0 1)`. -/
def swap01Edge (x : EdgeData) : EdgeData :=
  ![x 0, x 3, x 4, x 1, x 2, x 5]

/-- Induced edge-coordinate permutation for the transposition `(1 2)`. -/
def swap12Edge (x : EdgeData) : EdgeData :=
  ![x 1, x 0, x 2, x 3, x 5, x 4]

/-- Induced edge-coordinate permutation for the transposition `(2 3)`. -/
def swap23Edge (x : EdgeData) : EdgeData :=
  ![x 0, x 2, x 1, x 4, x 3, x 5]

@[simp] theorem vertexSum_swap01Vertex (v : VertexData) :
    vertexSum (swap01Vertex v) = vertexSum v := by
  simp [vertexSum, swap01Vertex]
  ring

@[simp] theorem vertexSum_swap12Vertex (v : VertexData) :
    vertexSum (swap12Vertex v) = vertexSum v := by
  simp [vertexSum, swap12Vertex]
  ring

@[simp] theorem vertexSum_swap23Vertex (v : VertexData) :
    vertexSum (swap23Vertex v) = vertexSum v := by
  simp [vertexSum, swap23Vertex]
  ring

/-- The coordinate incidence map is equivariant for `(0 1)`. -/
theorem swap01Edge_delta (v : VertexData) :
    swap01Edge (delta v) = delta (swap01Vertex v) := by
  funext i
  fin_cases i <;>
    simp [swap01Edge, delta, swap01Vertex, add_comm]

/-- The coordinate incidence map is equivariant for `(1 2)`. -/
theorem swap12Edge_delta (v : VertexData) :
    swap12Edge (delta v) = delta (swap12Vertex v) := by
  funext i
  fin_cases i <;>
    simp [swap12Edge, delta, swap12Vertex, add_comm]

/-- The coordinate incidence map is equivariant for `(2 3)`. -/
theorem swap23Edge_delta (v : VertexData) :
    swap23Edge (delta v) = delta (swap23Vertex v) := by
  funext i
  fin_cases i <;>
    simp [swap23Edge, delta, swap23Vertex, add_comm]

@[simp] theorem swap01Edge_edgeSub (x y : EdgeData) :
    swap01Edge (edgeSub x y) = edgeSub (swap01Edge x) (swap01Edge y) := by
  funext i
  fin_cases i <;> simp [swap01Edge, edgeSub]

@[simp] theorem swap12Edge_edgeSub (x y : EdgeData) :
    swap12Edge (edgeSub x y) = edgeSub (swap12Edge x) (swap12Edge y) := by
  funext i
  fin_cases i <;> simp [swap12Edge, edgeSub]

@[simp] theorem swap23Edge_edgeSub (x y : EdgeData) :
    swap23Edge (edgeSub x y) = edgeSub (swap23Edge x) (swap23Edge y) := by
  funext i
  fin_cases i <;> simp [swap23Edge, edgeSub]

/-- Residual equivalence is preserved by `(0 1)`. -/
theorem deltaEquivalent_swap01 {x y : EdgeData}
    (h : DeltaEquivalent x y) :
    DeltaEquivalent (swap01Edge x) (swap01Edge y) := by
  rcases h with ⟨v, hv, hd⟩
  refine ⟨swap01Vertex v, by simpa using hv, ?_⟩
  calc
    delta (swap01Vertex v) = swap01Edge (delta v) :=
      (swap01Edge_delta v).symm
    _ = swap01Edge (edgeSub x y) := by rw [hd]
    _ = edgeSub (swap01Edge x) (swap01Edge y) :=
      swap01Edge_edgeSub x y

/-- Residual equivalence is preserved by `(1 2)`. -/
theorem deltaEquivalent_swap12 {x y : EdgeData}
    (h : DeltaEquivalent x y) :
    DeltaEquivalent (swap12Edge x) (swap12Edge y) := by
  rcases h with ⟨v, hv, hd⟩
  refine ⟨swap12Vertex v, by simpa using hv, ?_⟩
  calc
    delta (swap12Vertex v) = swap12Edge (delta v) :=
      (swap12Edge_delta v).symm
    _ = swap12Edge (edgeSub x y) := by rw [hd]
    _ = edgeSub (swap12Edge x) (swap12Edge y) :=
      swap12Edge_edgeSub x y

/-- Residual equivalence is preserved by `(2 3)`. -/
theorem deltaEquivalent_swap23 {x y : EdgeData}
    (h : DeltaEquivalent x y) :
    DeltaEquivalent (swap23Edge x) (swap23Edge y) := by
  rcases h with ⟨v, hv, hd⟩
  refine ⟨swap23Vertex v, by simpa using hv, ?_⟩
  calc
    delta (swap23Vertex v) = swap23Edge (delta v) :=
      (swap23Edge_delta v).symm
    _ = swap23Edge (edgeSub x y) := by rw [hd]
    _ = edgeSub (swap23Edge x) (swap23Edge y) :=
      swap23Edge_edgeSub x y

/-! ## 2. Exact action on canonical `(p,q,ε)` representatives -/

/-- Boolean complement, the nonzero translation of the `C₂` coordinate. -/
def flipBit : Bool → Bool
  | false => true
  | true => false

/-- The transposition `(1 2)` exchanges the two displayed free coordinates and
leaves the parity bit unchanged. -/
theorem swap12Edge_normalForm (p q : ℤ) (ε : Bool) :
    DeltaEquivalent (swap12Edge (normalForm p q ε))
      (normalForm q p ε) := by
  apply (deltaEquivalent_iff_matching_eq_and_even
    (swap12Edge (normalForm p q ε)) (normalForm q p ε)).2
  constructor
  · funext i
    fin_cases i <;> cases ε <;>
      simp [matching, swap12Edge, normalForm, bitInt] <;> ring
  · refine ⟨0, ?_⟩
    cases ε <;> simp [edgeSub, swap12Edge, normalForm, bitInt]

/-- The transposition `(2 3)` sends `(p,q)` to `(p,-p-q)` and leaves the parity
bit unchanged. -/
theorem swap23Edge_normalForm (p q : ℤ) (ε : Bool) :
    DeltaEquivalent (swap23Edge (normalForm p q ε))
      (normalForm p (-p - q) ε) := by
  apply (deltaEquivalent_iff_matching_eq_and_even
    (swap23Edge (normalForm p q ε)) (normalForm p (-p - q) ε)).2
  constructor
  · funext i
    fin_cases i <;> cases ε <;>
      simp [matching, swap23Edge, normalForm, bitInt]
  · refine ⟨0, ?_⟩
    cases ε <;> simp [edgeSub, swap23Edge, normalForm, bitInt]

/-- If `p` is even, the transposition `(0 1)` has the same free action as
`(2 3)` and does not change the parity bit. -/
theorem swap01Edge_normalForm_even
    (p q k : ℤ) (ε : Bool) (hp : p = 2 * k) :
    DeltaEquivalent (swap01Edge (normalForm p q ε))
      (normalForm p (-p - q) ε) := by
  apply (deltaEquivalent_iff_matching_eq_and_even
    (swap01Edge (normalForm p q ε)) (normalForm p (-p - q) ε)).2
  constructor
  · funext i
    fin_cases i <;> cases ε <;>
      simp [matching, swap01Edge, normalForm, bitInt]
  · refine ⟨-k, ?_⟩
    cases ε <;>
      simp [edgeSub, swap01Edge, normalForm, bitInt, hp]

/-- If `p` is odd, the transposition `(0 1)` has the same free action as
`(2 3)` but flips the parity bit. -/
theorem swap01Edge_normalForm_odd
    (p q k : ℤ) (ε : Bool) (hp : p = 2 * k + 1) :
    DeltaEquivalent (swap01Edge (normalForm p q ε))
      (normalForm p (-p - q) (flipBit ε)) := by
  apply (deltaEquivalent_iff_matching_eq_and_even
    (swap01Edge (normalForm p q ε))
    (normalForm p (-p - q) (flipBit ε))).2
  constructor
  · funext i
    fin_cases i <;> cases ε <;>
      simp [matching, swap01Edge, normalForm, bitInt, flipBit]
  · cases ε with
    | false =>
        refine ⟨-k - 1, ?_⟩
        simp [edgeSub, swap01Edge, normalForm, bitInt, flipBit, hp]
        ring
    | true =>
        refine ⟨-k, ?_⟩
        simp [edgeSub, swap01Edge, normalForm, bitInt, flipBit, hp]
        ring

/-- Every integral free coordinate falls into exactly the two displayed
cocycle cases: even `p` preserves `ε`, odd `p` translates `ε` by the nonzero
`C₂` element. -/
theorem swap01Edge_normalForm_parity_cases
    (p q : ℤ) (ε : Bool) :
    (∃ k : ℤ, p = 2 * k ∧
      DeltaEquivalent (swap01Edge (normalForm p q ε))
        (normalForm p (-p - q) ε)) ∨
    (∃ k : ℤ, p = 2 * k + 1 ∧
      DeltaEquivalent (swap01Edge (normalForm p q ε))
        (normalForm p (-p - q) (flipBit ε))) := by
  rcases Int.even_or_odd' p with ⟨k, hk | hk⟩
  · exact Or.inl ⟨k, hk, swap01Edge_normalForm_even p q k ε hk⟩
  · exact Or.inr ⟨k, hk, swap01Edge_normalForm_odd p q k ε hk⟩

/-- The primitive torsion class is fixed by `(0 1)`. -/
theorem torsion_fixed_swap01 :
    DeltaEquivalent (swap01Edge (normalForm 0 0 true))
      (normalForm 0 0 true) := by
  simpa using swap01Edge_normalForm_even 0 0 0 true (by norm_num)

/-- The primitive torsion class is fixed by `(1 2)`. -/
theorem torsion_fixed_swap12 :
    DeltaEquivalent (swap12Edge (normalForm 0 0 true))
      (normalForm 0 0 true) := by
  simpa using swap12Edge_normalForm 0 0 true

/-- The primitive torsion class is fixed by `(2 3)`. -/
theorem torsion_fixed_swap23 :
    DeltaEquivalent (swap23Edge (normalForm 0 0 true))
      (normalForm 0 0 true) := by
  simpa using swap23Edge_normalForm 0 0 true

/-! ## 3. Mod-two shadow and the obstruction to an equivariant splitting -/

/-- The mod-two shadow of the two free coordinates and one torsion coordinate. -/
abbrev ResidualF2 := ((ZMod 2 × ZMod 2) × ZMod 2)

/-- Mod-two action of `(1 2)`. -/
def action12F2 (c : ResidualF2) : ResidualF2 :=
  ((c.1.2, c.1.1), c.2)

/-- Mod-two action of `(2 3)`.  Minus signs disappear in characteristic two. -/
def action23F2 (c : ResidualF2) : ResidualF2 :=
  ((c.1.1, c.1.1 + c.1.2), c.2)

/-- Mod-two action of `(0 1)`.  Its last component contains the parity
translation cocycle. -/
def action01F2 (c : ResidualF2) : ResidualF2 :=
  ((c.1.1, c.1.1 + c.1.2), c.2 + c.1.1)

/-- The three generator formulas are additive. -/
theorem action12F2_add :
    ∀ x y : ResidualF2,
      action12F2 (x + y) = action12F2 x + action12F2 y := by
  native_decide

theorem action23F2_add :
    ∀ x y : ResidualF2,
      action23F2 (x + y) = action23F2 x + action23F2 y := by
  native_decide

theorem action01F2_add :
    ∀ x y : ResidualF2,
      action01F2 (x + y) = action01F2 x + action01F2 y := by
  native_decide

/-- Each adjacent-transposition formula is an involution. -/
theorem action12F2_involutive :
    ∀ c : ResidualF2, action12F2 (action12F2 c) = c := by
  native_decide

theorem action23F2_involutive :
    ∀ c : ResidualF2, action23F2 (action23F2 c) = c := by
  native_decide

theorem action01F2_involutive :
    ∀ c : ResidualF2, action01F2 (action01F2 c) = c := by
  native_decide

/-- The three generators satisfy the Coxeter relations for `S₄`. -/
theorem action01_action12_braid :
    ∀ c : ResidualF2,
      action01F2 (action12F2 (action01F2 c)) =
        action12F2 (action01F2 (action12F2 c)) := by
  native_decide

theorem action12_action23_braid :
    ∀ c : ResidualF2,
      action12F2 (action23F2 (action12F2 c)) =
        action23F2 (action12F2 (action23F2 c)) := by
  native_decide

theorem action01_action23_commute :
    ∀ c : ResidualF2,
      action01F2 (action23F2 c) = action23F2 (action01F2 c) := by
  native_decide

/-- Free-coordinate basis vectors and the torsion generator. -/
def freeP : ResidualF2 := ((1, 0), 0)

def freeQ : ResidualF2 := ((0, 1), 0)

def torsionF2 : ResidualF2 := ((0, 0), 1)

@[simp] theorem action12F2_freeP : action12F2 freeP = freeQ := by
  native_decide

@[simp] theorem action23F2_freeP :
    action23F2 freeP = freeP + freeQ := by
  native_decide

@[simp] theorem action01F2_freeP :
    action01F2 freeP = freeP + freeQ + torsionF2 := by
  native_decide

@[simp] theorem action12F2_torsion : action12F2 torsionF2 = torsionF2 := by
  native_decide

@[simp] theorem action23F2_torsion : action23F2 torsionF2 = torsionF2 := by
  native_decide

@[simp] theorem action01F2_torsion : action01F2 torsionF2 = torsionF2 := by
  native_decide

/-- A hidden double transposition: it is invisible on the free pair and
translates the torsion coordinate by the first free parity. -/
def hiddenDoubleSwapF2 (c : ResidualF2) : ResidualF2 :=
  action01F2 (action23F2 c)

theorem hiddenDoubleSwapF2_formula :
    ∀ c : ResidualF2,
      hiddenDoubleSwapF2 c = ((c.1.1, c.1.2), c.2 + c.1.1) := by
  native_decide

@[simp] theorem hiddenDoubleSwapF2_freeP :
    hiddenDoubleSwapF2 freeP = freeP + torsionF2 := by
  native_decide

/-- There is no additive projection to the torsion coordinate which both sends
the torsion generator to `1` and is invariant under the three adjacent
transpositions.  Since these transpositions generate `S₄`, the integral
`Z² ⊕ C₂` splitting cannot be chosen `S₄`-equivariantly. -/
theorem no_adjacent_swap_invariant_torsion_retraction :
    ¬ ∃ r : ResidualF2 →+ ZMod 2,
      r torsionF2 = 1 ∧
      (∀ c, r (action12F2 c) = r c) ∧
      (∀ c, r (action23F2 c) = r c) ∧
      (∀ c, r (action01F2 c) = r c) := by
  rintro ⟨r, ht, h12, h23, h01⟩
  have hPQ : r freeQ = r freeP := by
    simpa using h12 freeP
  have hP0 : r freeP = 0 := by
    have h := h23 freeP
    rw [action23F2_freeP, r.map_add, hPQ] at h
    simpa using h
  have h := h01 freeP
  rw [action01F2_freeP, r.map_add, r.map_add, hPQ, ht, hP0] at h
  norm_num at h

/-- Structural conclusion: the torsion line is invariant under the generator
action, but no invariant additive retraction onto it exists. -/
theorem invariant_torsion_without_equivariant_complement :
    (action12F2 torsionF2 = torsionF2 ∧
      action23F2 torsionF2 = torsionF2 ∧
      action01F2 torsionF2 = torsionF2) ∧
    (¬ ∃ r : ResidualF2 →+ ZMod 2,
      r torsionF2 = 1 ∧
      (∀ c, r (action12F2 c) = r c) ∧
      (∀ c, r (action23F2 c) = r c) ∧
      (∀ c, r (action01F2 c) = r c)) := by
  exact ⟨⟨action12F2_torsion, action23F2_torsion,
    action01F2_torsion⟩,
    no_adjacent_swap_invariant_torsion_retraction⟩

end EnterpriseMath.PrecisionPi.PaperIIResidualCocycleV1
