import EnterpriseMath.PrecisionPi.TetrahedralParity

namespace EnterpriseMath.PrecisionPi.TetrahedralInjectivity

open TetrahedralResidual TetrahedralMatching TetrahedralParity

/-- The endpoint-sum incidence map on the tetrahedron is injective over the integers. -/
theorem delta_injective : Function.Injective delta := by
  intro v w h
  have h12 := congrArg EdgeData.e12 h
  have h13 := congrArg EdgeData.e13 h
  have h14 := congrArg EdgeData.e14 h
  have h23 := congrArg EdgeData.e23 h
  have h24 := congrArg EdgeData.e24 h
  have h34 := congrArg EdgeData.e34 h
  simp [delta] at h12 h13 h14 h23 h24 h34
  apply VertexData.ext <;> omega

/-- A zero-sum edge image has a unique zero-sum slice potential. -/
theorem zeroSum_delta_witness_unique
    {x : EdgeData} {v w : VertexData}
    (_hv : vertexSum v = 0) (_hw : vertexSum w = 0)
    (hvx : delta v = x) (hwx : delta w = x) :
    v = w := by
  apply delta_injective
  rw [hvx, hwx]

/-- The explicit witness from an even matching-kernel pattern is the unique integral witness. -/
theorem edgePattern_vertexWitness_unique
    {a b c k : ℤ}
    (hk : a + b + c = 2 * k)
    {v : VertexData}
    (_hv : vertexSum v = 0)
    (hd : delta v = edgePattern a b c) :
    v = vertexWitness a b c k := by
  apply delta_injective
  rw [hd, delta_vertexWitness_of_even hk]

/-- Twice the basic generator has a unique zero-sum preimage. -/
theorem twice_basic_generator_unique :
    ∃! v : VertexData,
      vertexSum v = 0 ∧ delta v = edgePattern 2 0 0 := by
  obtain ⟨v, hv, hd⟩ := twice_basic_parity_class_mem
  refine ⟨v, ⟨hv, hd⟩, ?_⟩
  intro w hw
  exact zeroSum_delta_witness_unique hw.1 hv hw.2 hd

/-- Every doubled kernel pattern has a unique zero-sum preimage. -/
theorem doubled_edgePattern_unique (a b c : ℤ) :
    ∃! v : VertexData,
      vertexSum v = 0 ∧
        delta v = edgePattern (2 * a) (2 * b) (2 * c) := by
  obtain ⟨v, hv, hd⟩ := doubled_edgePattern_mem a b c
  refine ⟨v, ⟨hv, hd⟩, ?_⟩
  intro w hw
  exact zeroSum_delta_witness_unique hw.1 hv hw.2 hd

/-- Exact order-two certificate for the basic parity obstruction. -/
theorem basic_generator_exact_order_two_certificate :
    (¬ ∃ v : VertexData,
      vertexSum v = 0 ∧ delta v = edgePattern 1 0 0) ∧
    (∃! v : VertexData,
      vertexSum v = 0 ∧ delta v = edgePattern 2 0 0) := by
  exact ⟨basic_parity_class_not_mem, twice_basic_generator_unique⟩

end EnterpriseMath.PrecisionPi.TetrahedralInjectivity
