import EnterpriseMath.PrecisionPi.PaperIIContinuumSplitV1

namespace EnterpriseMath.PrecisionPi.PaperIIK4RotationV1

open EnterpriseMath.PrecisionPi.PaperIIKernelV1

/-! ## 1. The six carrier lines are exactly the edges of `K₄` -/

/-- Unordered pairs of distinct slice charts. -/
abbrev SlicePair := {s : Finset SliceChart // s.card = 2}

/-- A line family is sent to the two slice charts containing it. -/
def lineToSlicePair (l : LineFamily) : SlicePair :=
  ⟨incidentSlices l, incidentSlices_card l⟩

/-- Explicit endpoint table for the six line families. -/
def lineSlicePairTable : LineFamily → Finset SliceChart :=
  ![({0, 1} : Finset SliceChart),
    ({2, 3} : Finset SliceChart),
    ({0, 2} : Finset SliceChart),
    ({1, 3} : Finset SliceChart),
    ({1, 2} : Finset SliceChart),
    ({0, 3} : Finset SliceChart)]

/-- The filtered incidence definition agrees with the explicit endpoint table. -/
@[simp] theorem incidentSlices_eq_lineSlicePairTable (l : LineFamily) :
    incidentSlices l = lineSlicePairTable l := by
  fin_cases l <;> native_decide

/-- Incidence is recovered exactly from the associated slice pair. -/
theorem mem_lineToSlicePair_iff (l : LineFamily) (s : SliceChart) :
    s ∈ (lineToSlicePair l : Finset SliceChart) ↔ l ∈ sliceLines s := by
  simp [lineToSlicePair, incidentSlices]

/-- The six line families are exactly the six unordered pairs of four slice
charts. -/
theorem lineToSlicePair_bijective : Function.Bijective lineToSlicePair := by
  native_decide

/-- Exact `K₄` edge equivalence for the selected Enterprise-coordinate
carrier. -/
noncomputable def lineFamilyEquivSlicePair : LineFamily ≃ SlicePair :=
  Equiv.ofBijective lineToSlicePair lineToSlicePair_bijective

/-- The abstract edge set of `K₄` has six elements. -/
theorem slicePair_card : Fintype.card SlicePair = 6 := by
  calc
    Fintype.card SlicePair = Fintype.card LineFamily :=
      Fintype.card_congr lineFamilyEquivSlicePair.symm
    _ = 6 := six_lines

/-- Every unordered pair of distinct slices determines one line family. -/
noncomputable def sharedLineOfPair (p : SlicePair) : LineFamily :=
  lineFamilyEquivSlicePair.symm p

@[simp] theorem lineToSlicePair_sharedLineOfPair (p : SlicePair) :
    lineToSlicePair (sharedLineOfPair p) = p := by
  exact lineFamilyEquivSlicePair.apply_symm_apply p

@[simp] theorem sharedLineOfPair_lineToSlicePair (l : LineFamily) :
    sharedLineOfPair (lineToSlicePair l) = l := by
  exact lineFamilyEquivSlicePair.symm_apply_apply l

/-- Abstract `K₄` incidence and the explicit slice-line incidence table are the
same relation. -/
theorem sharedLine_incident_iff (p : SlicePair) (s : SliceChart) :
    s ∈ (p : Finset SliceChart) ↔ sharedLineOfPair p ∈ sliceLines s := by
  simpa using mem_lineToSlicePair_iff (sharedLineOfPair p) s

/-! ## 2. Slice permutations induce line-family permutations -/

/-- Transport an unordered slice pair by a slice permutation. -/
def mapSlicePair (σ : Equiv.Perm SliceChart) (p : SlicePair) : SlicePair :=
  ⟨(p : Finset SliceChart).map σ.toEmbedding, by simpa using p.property⟩

/-- Transport of slice pairs is itself a permutation. -/
def slicePairPerm (σ : Equiv.Perm SliceChart) : Equiv.Perm SlicePair where
  toFun := mapSlicePair σ
  invFun := mapSlicePair σ.symm
  left_inv p := by
    apply Subtype.ext
    ext s
    simp [mapSlicePair]
  right_inv p := by
    apply Subtype.ext
    ext s
    simp [mapSlicePair]

/-- The corresponding permutation of the six line families. -/
noncomputable def lineFamilyPerm
    (σ : Equiv.Perm SliceChart) : Equiv.Perm LineFamily :=
  lineFamilyEquivSlicePair.trans
    ((slicePairPerm σ).trans lineFamilyEquivSlicePair.symm)

/-- The associated slice pair of a transported line is the transported
associated pair. -/
theorem lineToSlicePair_lineFamilyPerm
    (σ : Equiv.Perm SliceChart) (l : LineFamily) :
    lineToSlicePair (lineFamilyPerm σ l) =
      mapSlicePair σ (lineToSlicePair l) := by
  calc
    lineToSlicePair (lineFamilyPerm σ l) =
        lineFamilyEquivSlicePair (lineFamilyPerm σ l) := rfl
    _ = mapSlicePair σ (lineFamilyEquivSlicePair l) := by
      simp [lineFamilyPerm, slicePairPerm]
    _ = mapSlicePair σ (lineToSlicePair l) := by rfl

/-- The incident slices of a transported line are exactly the transported
incident slices. -/
theorem incidentSlices_lineFamilyPerm
    (σ : Equiv.Perm SliceChart) (l : LineFamily) :
    incidentSlices (lineFamilyPerm σ l) =
      (incidentSlices l).map σ.toEmbedding := by
  have h := congrArg (fun p : SlicePair => (p : Finset SliceChart))
    (lineToSlicePair_lineFamilyPerm σ l)
  simpa [lineToSlicePair, mapSlicePair] using h

/-- Incidence is covariant under simultaneous slice and line transport. -/
theorem incidence_covariant
    (σ : Equiv.Perm SliceChart) (l : LineFamily) (s : SliceChart) :
    lineFamilyPerm σ l ∈ sliceLines (σ s) ↔ l ∈ sliceLines s := by
  rw [← mem_lineToSlicePair_iff, ← mem_lineToSlicePair_iff]
  rw [lineToSlicePair_lineFamilyPerm]
  simp [mapSlicePair]

/-- Identity transport induces identity line transport. -/
theorem lineFamilyPerm_refl :
    lineFamilyPerm (Equiv.refl SliceChart) = Equiv.refl LineFamily := by
  apply Equiv.ext
  intro l
  apply lineFamilyEquivSlicePair.injective
  simp [lineFamilyPerm, slicePairPerm, mapSlicePair]

/-- Composition of slice transports agrees with composition of induced line
transports. -/
theorem lineFamilyPerm_trans (σ τ : Equiv.Perm SliceChart) :
    lineFamilyPerm (σ.trans τ) =
      (lineFamilyPerm σ).trans (lineFamilyPerm τ) := by
  apply Equiv.ext
  intro l
  apply lineFamilyEquivSlicePair.injective
  simp [lineFamilyPerm, slicePairPerm, mapSlicePair]
  rw [Finset.map_map]
  apply Finset.ext
  intro s
  simp [Function.comp_def]

/-! ## 3. Equivariance of the carrier slice-to-line map -/

universe u

/-- Slice-labelled states with coefficients in `R`. -/
abbrev SliceState (R : Type u) := SliceChart → R

/-- Line-labelled states with coefficients in `R`. -/
abbrev LineState (R : Type u) := LineFamily → R

/-- Sum the two incident slice values on each carrier line. -/
def carrierDelta {R : Type u} [AddCommMonoid R]
    (v : SliceState R) : LineState R :=
  fun l => (incidentSlices l).sum v

/-- Pull a slice-labelled state through a slice permutation. -/
def rotateSliceState {R : Type u}
    (σ : Equiv.Perm SliceChart) (v : SliceState R) : SliceState R :=
  fun s => v (σ.symm s)

/-- Pull a line-labelled state through the induced line permutation. -/
noncomputable def rotateLineState {R : Type u}
    (σ : Equiv.Perm SliceChart) (x : LineState R) : LineState R :=
  fun l => x ((lineFamilyPerm σ).symm l)

/-- The carrier slice-to-line incidence map is equivariant under every slice
permutation and its induced line permutation. -/
theorem carrierDelta_equivariant {R : Type u} [AddCommMonoid R]
    (σ : Equiv.Perm SliceChart) (v : SliceState R) :
    carrierDelta (rotateSliceState σ v) =
      rotateLineState σ (carrierDelta v) := by
  funext l
  have hinc :
      incidentSlices l =
        (incidentSlices ((lineFamilyPerm σ).symm l)).map σ.toEmbedding := by
    simpa using
      incidentSlices_lineFamilyPerm σ ((lineFamilyPerm σ).symm l)
  change
    (incidentSlices l).sum (fun s => v (σ.symm s)) =
      (incidentSlices ((lineFamilyPerm σ).symm l)).sum v
  rw [hinc]
  simp

/-- Identity rotation fixes every slice-labelled state. -/
theorem rotateSliceState_refl {R : Type u} (v : SliceState R) :
    rotateSliceState (Equiv.refl SliceChart) v = v := by
  rfl

/-- Identity rotation fixes every line-labelled state. -/
theorem rotateLineState_refl {R : Type u} (x : LineState R) :
    rotateLineState (Equiv.refl SliceChart) x = x := by
  funext l
  simp [rotateLineState, lineFamilyPerm_refl]

/-- Successive slice rotations compose in the expected order. -/
theorem rotateSliceState_trans {R : Type u}
    (σ τ : Equiv.Perm SliceChart) (v : SliceState R) :
    rotateSliceState (σ.trans τ) v =
      rotateSliceState τ (rotateSliceState σ v) := by
  funext s
  rfl

/-- Successive line rotations compose in the expected order. -/
theorem rotateLineState_trans {R : Type u}
    (σ τ : Equiv.Perm SliceChart) (x : LineState R) :
    rotateLineState (σ.trans τ) x =
      rotateLineState τ (rotateLineState σ x) := by
  funext l
  simp [rotateLineState, lineFamilyPerm_trans]

/-! ## 4. Bridge to the six-coordinate residual kernel -/

/-- Coordinate position of each line family in the kernel's edge ordering
`12,13,14,23,24,34`. -/
def edgeIndexOfLine : LineFamily → Fin 6 :=
  ![0, 5, 1, 4, 3, 2]

/-- The line-to-edge-index table is a permutation. -/
theorem edgeIndexOfLine_bijective : Function.Bijective edgeIndexOfLine := by
  native_decide

/-- Exact equivalence between carrier-line labels and edge-coordinate slots. -/
noncomputable def lineFamilyEquivEdgeIndex : LineFamily ≃ Fin 6 :=
  Equiv.ofBijective edgeIndexOfLine edgeIndexOfLine_bijective

/-- Read an edge-coordinate state as a line-labelled state. -/
noncomputable def lineStateOfEdge {R : Type u}
    (x : Fin 6 → R) : LineState R :=
  fun l => x (lineFamilyEquivEdgeIndex l)

/-- Write a line-labelled state into the kernel's edge-coordinate ordering. -/
noncomputable def edgeStateOfLineState {R : Type u}
    (x : LineState R) : Fin 6 → R :=
  fun i => x (lineFamilyEquivEdgeIndex.symm i)

@[simp] theorem lineStateOfEdge_edgeStateOfLineState {R : Type u}
    (x : LineState R) :
    lineStateOfEdge (edgeStateOfLineState x) = x := by
  funext l
  simp [lineStateOfEdge, edgeStateOfLineState]

@[simp] theorem edgeStateOfLineState_lineStateOfEdge {R : Type u}
    (x : Fin 6 → R) :
    edgeStateOfLineState (lineStateOfEdge x) = x := by
  funext i
  simp [lineStateOfEdge, edgeStateOfLineState]

/-- Reading edge states by carrier-line labels is injective. -/
theorem lineStateOfEdge_injective {R : Type u} :
    Function.Injective (@lineStateOfEdge R) := by
  intro x y h
  have h' := congrArg edgeStateOfLineState h
  simpa using h'

/-- The coordinate-level integer map `delta` is exactly the carrier incidence
map after relabelling its six coordinates by line families. -/
theorem lineStateOfEdge_delta (v : VertexData) :
    lineStateOfEdge (delta v) = carrierDelta v := by
  funext l
  fin_cases l <;>
    simp [lineStateOfEdge, lineFamilyEquivEdgeIndex, edgeIndexOfLine,
      carrierDelta, lineSlicePairTable, delta]

/-- Rotate an edge-coordinate state through the induced carrier-line
permutation. -/
noncomputable def rotateEdgeData
    (σ : Equiv.Perm SliceChart) (x : EdgeData) : EdgeData :=
  edgeStateOfLineState (rotateLineState σ (lineStateOfEdge x))

@[simp] theorem lineStateOfEdge_rotateEdgeData
    (σ : Equiv.Perm SliceChart) (x : EdgeData) :
    lineStateOfEdge (rotateEdgeData σ x) =
      rotateLineState σ (lineStateOfEdge x) := by
  simp [rotateEdgeData]

/-- The original integer slice-to-line residual map commutes exactly with every
`K₄` slice rotation. -/
theorem rotateEdgeData_delta
    (σ : Equiv.Perm SliceChart) (v : VertexData) :
    rotateEdgeData σ (delta v) = delta (rotateSliceState σ v) := by
  apply lineStateOfEdge_injective
  rw [lineStateOfEdge_rotateEdgeData, lineStateOfEdge_delta,
    lineStateOfEdge_delta]
  exact (carrierDelta_equivariant σ v).symm

end EnterpriseMath.PrecisionPi.PaperIIK4RotationV1
