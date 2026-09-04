import EnterpriseMath.Precision.EulerHolonomyResidualDuality

namespace EnterpriseMath.Precision.EulerTwistedEndpointCohomology

open EnterpriseMath.Precision.EulerC12RootTorsorFlatness
open EnterpriseMath.Precision.EulerHolonomyResidualDuality

/-! ## Integral vertex and edge cochains -/

@[ext]
structure IntVertexState where
  a : ℤ
  b : ℤ
  c : ℤ
  d : ℤ
  deriving DecidableEq

@[ext]
structure IntEdgeState where
  ab : ℤ
  ac : ℤ
  ad : ℤ
  bc : ℤ
  bd : ℤ
  cd : ℤ
  deriving DecidableEq

def vertexTotal (v : IntVertexState) : ℤ :=
  v.a + v.b + v.c + v.d

def edgeTotal (e : IntEdgeState) : ℤ :=
  e.ab + e.ac + e.ad + e.bc + e.bd + e.cd

/-- Ordinary graph coboundary for the flat `+1` coefficient system. -/
def ordinaryCoboundary (v : IntVertexState) : IntEdgeState :=
  ⟨v.b - v.a,
   v.c - v.a,
   v.d - v.a,
   v.c - v.b,
   v.d - v.b,
   v.d - v.c⟩

/-- Twisted graph coboundary when every overlap transports the coefficient by
    `-1`.  This is exactly the endpoint-sum map. -/
def twistedCoboundary (v : IntVertexState) : IntEdgeState :=
  ⟨v.a + v.b,
   v.a + v.c,
   v.a + v.d,
   v.b + v.c,
   v.b + v.d,
   v.c + v.d⟩

def edgeSub (x y : IntEdgeState) : IntEdgeState :=
  ⟨x.ab - y.ab,
   x.ac - y.ac,
   x.ad - y.ad,
   x.bc - y.bc,
   x.bd - y.bd,
   x.cd - y.cd⟩

/-- Every vertex occurs in exactly three tetrahedral edges. -/
theorem edgeTotal_twistedCoboundary (v : IntVertexState) :
    edgeTotal (twistedCoboundary v) = 3 * vertexTotal v := by
  simp [edgeTotal, twistedCoboundary, vertexTotal]
  ring

/-- A zero-total twisted coboundary has a zero-total vertex preimage. -/
theorem zero_total_twisted_preimage (v : IntVertexState)
    (h : edgeTotal (twistedCoboundary v) = 0) :
    vertexTotal v = 0 := by
  rw [edgeTotal_twistedCoboundary] at h
  omega

/-- If an edge representative has total `3m`, subtracting the twisted
    coboundary of `(m,0,0,0)` produces a zero-total representative. -/
theorem neutralize_total_mod_three
    (x : IntEdgeState) (m : ℤ)
    (h : edgeTotal x = 3 * m) :
    edgeTotal
      (edgeSub x (twistedCoboundary ⟨m, 0, 0, 0⟩)) = 0 := by
  simp [edgeTotal, edgeSub, twistedCoboundary] at h ⊢
  linarith

/-! ## Flat and uniformly twisted parallel sections -/

/-- The kernel of the ordinary incidence map consists of constant vertex
    sections. -/
theorem ordinary_kernel_is_constant (v : IntVertexState)
    (h : ordinaryCoboundary v = ⟨0, 0, 0, 0, 0, 0⟩) :
    v.b = v.a ∧ v.c = v.a ∧ v.d = v.a := by
  have hab := congrArg IntEdgeState.ab h
  have hac := congrArg IntEdgeState.ac h
  have had := congrArg IntEdgeState.ad h
  simp [ordinaryCoboundary] at hab hac had
  omega

/-- The uniformly reversing sign system has no nonzero integral parallel
    section.  An odd triangle forces `v=-v`, hence `v=0`. -/
theorem uniform_twist_kernel_is_zero (v : IntVertexState)
    (h : twistedCoboundary v = ⟨0, 0, 0, 0, 0, 0⟩) :
    v = ⟨0, 0, 0, 0⟩ := by
  have hab := congrArg IntEdgeState.ab h
  have hac := congrArg IntEdgeState.ac h
  have hbc := congrArg IntEdgeState.bc h
  have had := congrArg IntEdgeState.ad h
  simp [twistedCoboundary] at hab hac hbc had
  have ha : v.a = 0 := by omega
  have hb : v.b = 0 := by omega
  have hc : v.c = 0 := by omega
  have hd : v.d = 0 := by omega
  apply IntVertexState.ext
  · simpa using ha
  · simpa using hb
  · simpa using hc
  · simpa using hd

/-! ## Characteristic-two coincidence -/

@[ext]
structure ModTwoEdgeState where
  ab : ZMod 2
  ac : ZMod 2
  ad : ZMod 2
  bc : ZMod 2
  bd : ZMod 2
  cd : ZMod 2
  deriving DecidableEq

def reduceModTwo (e : IntEdgeState) : ModTwoEdgeState :=
  ⟨e.ab, e.ac, e.ad, e.bc, e.bd, e.cd⟩

/-- The flat oriented and uniformly twisted endpoint incidence maps become
    identical in characteristic two because `-1=+1`. -/
theorem ordinary_eq_twisted_mod_two (v : IntVertexState) :
    reduceModTwo (ordinaryCoboundary v) =
      reduceModTwo (twistedCoboundary v) := by
  ext <;>
    simp [reduceModTwo, ordinaryCoboundary, twistedCoboundary,
      ZModModule.sub_eq_add] <;>
    ac_rfl

/-! ## The two fully symmetric phases -/

/-- The zero and constant-one states are the only endpoint residuals fixed by
    the three adjacent transpositions generating `S4`. -/
theorem only_symmetric_residuals : ∀ r : AffineResidual,
    (swapABResidual r = r ∧ swapBCResidual r = r ∧ swapCDResidual r = r) ↔
      r = zeroResidual ∨ r = torsionResidual :=
  s4_fixed_states_are_torsion_line

/-- Consequently the endpoint torsion is the unique nonzero possible image of
    a trivial `C2` root-sheet generator under a fully `S4`-equivariant bridge. -/
theorem unique_nonzero_symmetric_kernel_image : ∀ r : AffineResidual,
    swapABResidual r = r →
    swapBCResidual r = r →
    swapCDResidual r = r →
    r ≠ zeroResidual →
    r = torsionResidual := by
  intro r hab hbc hcd hne
  have h := (only_symmetric_residuals r).1 ⟨hab, hbc, hcd⟩
  rcases h with hzero | htorsion
  · exact False.elim (hne hzero)
  · exact htorsion

/-- The uniformly sign-reversing edge system is the all-face-flip holonomy
    class and therefore maps to the endpoint torsion state. -/
def uniformTwistEdges : EdgeBits :=
  ⟨true, true, true, true, true, true⟩

theorem uniform_twist_has_all_face_holonomies :
    faceABC uniformTwistEdges = true ∧
    faceABD uniformTwistEdges = true ∧
    faceACD uniformTwistEdges = true ∧
    faceBCD uniformTwistEdges = true := by
  native_decide

theorem uniform_twist_maps_to_endpoint_torsion :
    edgeToResidual uniformTwistEdges = torsionResidual := by
  native_decide

end EnterpriseMath.Precision.EulerTwistedEndpointCohomology
