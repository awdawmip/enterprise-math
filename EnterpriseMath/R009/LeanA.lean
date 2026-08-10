import Mathlib
import EnterpriseMath.R009.ScaleNaturalLiftTargets

namespace EnterpriseMath.R009

private theorem div_succ_adjacent_of_same_block
    {d x y : ℕ} (hd : 0 < d) (hxy : x / d = y / d) :
    x / (d + 1) ≤ y / (d + 1) + 1 := by
  have hxlt : x < x / d * d + d := Nat.lt_div_mul_add hd
  rw [hxy] at hxlt
  have hyle : y / d * d ≤ y := Nat.div_mul_le_self y d
  have hxylt : x < y + d :=
    lt_of_lt_of_le hxlt (Nat.add_le_add_right hyle d)
  have hxy' : x ≤ y + (d + 1) := by omega
  have hdiv := Nat.div_le_div_right hxy' (k := d + 1)
  simpa [Nat.add_div_right, Nat.succ_pos] using hdiv

private theorem div_succ_dist_le_one_of_same_block
    {d x y : ℕ} (hd : 0 < d) (hxy : x / d = y / d) :
    x / (d + 1) ≤ y / (d + 1) + 1 ∧
      y / (d + 1) ≤ x / (d + 1) + 1 := by
  exact ⟨div_succ_adjacent_of_same_block hd hxy,
    div_succ_adjacent_of_same_block hd hxy.symm⟩

/-- R009-T01: the zero-residue lift is natural at every positive scale edge. -/
theorem r009_t01 : T01Statement := by
  unfold T01Statement ScaleNatural zeroResidueLift
  intro H d r m hd hr
  calc
    (d * r * H (m / (d * r))) / r
        = d * H (m / (d * r)) := by
            rw [Nat.mul_assoc, Nat.mul_comm r (H (m / (d * r))), ← Nat.mul_assoc]
            exact Nat.mul_div_cancel _ hr
    _ = d * H (m / r / d) := by
          rw [Nat.div_div_eq_div_mul, Nat.mul_comm r d]

/-- R009-T02: naturality to scale 1 forces the unique Euclidean residue. -/
theorem r009_t02 : T02Statement := by
  unfold T02Statement
  intro F H hNat hOne d m hd
  have hq : F d m / d = H (m / d) := by
    have h := hNat 1 d m (by omega) hd
    simpa [hOne] using h
  refine ⟨F d m % d, ?_, ?_⟩
  · constructor
    · exact Nat.mod_lt _ hd
    · calc
        F d m = (F d m / d) * d + F d m % d := by
          simpa [Nat.add_comm, Nat.mul_comm] using (Nat.div_add_mod (F d m) d).symm
        _ = d * H (m / d) + F d m % d := by rw [hq, Nat.mul_comm]
  · intro ρ hρ
    rcases hρ with ⟨hρlt, hEq⟩
    calc
      ρ = (d * H (m / d) + ρ) % d := by
        simp [Nat.mod_eq_of_lt hρlt]
      _ = F d m % d := by rw [← hEq]

/-- R009-T03: after normal form, full naturality is exactly residue coherence. -/
theorem r009_t03 : T03Statement := by
  unfold T03Statement
  intro F ρ H hNF
  constructor
  · intro hNat
    unfold ResidueCoherent
    intro d r m hd hr
    rcases hNF (d * r) m (Nat.mul_pos hd hr) with ⟨hρf, hFf⟩
    rcases hNF d (m / r) hd with ⟨hρc, hFc⟩
    have h := hNat d r m hd hr
    rw [hFf, hFc] at h
    have hbase :
        d * r * H (m / (d * r)) = r * (d * H (m / (d * r))) := by
      ring
    rw [hbase, Nat.add_comm (r * (d * H (m / (d * r))))] at h
    rw [Nat.add_mul_div_left _ _ hr] at h
    rw [Nat.div_div_eq_div_mul, Nat.mul_comm r d] at h
    omega
  · intro hCoh
    unfold ScaleNatural
    intro d r m hd hr
    rcases hNF (d * r) m (Nat.mul_pos hd hr) with ⟨hρf, hFf⟩
    rcases hNF d (m / r) hd with ⟨hρc, hFc⟩
    rw [hFf, hFc]
    have hbase :
        d * r * H (m / (d * r)) = r * (d * H (m / (d * r))) := by
      ring
    rw [hbase, Nat.add_comm (r * (d * H (m / (d * r)))), Nat.add_mul_div_left _ _ hr]
    rw [Nat.div_div_eq_div_mul, Nat.mul_comm r d]
    have hc := hCoh d r m hd hr
    omega

/-- R009-T09: every coherent finite-grid endomorphism is adjacent 1-Lipschitz. -/
theorem r009_t09 : T09Statement := by
  unfold T09Statement
  intro φ hGrid d s hd hs
  rcases hGrid with ⟨hRange, hCoh⟩
  let u : ℕ := (d + 1) * s + d
  let v : ℕ := (d + 1) * (s + 1)
  have huv : u + 1 = v := by
    dsimp [u, v]
    ring
  have hvlt : v < d * (d + 1) := by
    dsimp [v]
    have hmul := Nat.mul_lt_mul_left (d + 1) hs
    simpa [Nat.mul_comm] using hmul
  have hult : u < d * (d + 1) := by omega
  have hudivBig : u / (d + 1) = s := by
    apply Nat.div_eq_of_lt_le
    · dsimp [u]
      ring_nf
      omega
    · dsimp [u]
      ring_nf
      omega
  have hvdivBig : v / (d + 1) = s + 1 := by
    dsimp [v]
    exact Nat.mul_div_cancel_left (s + 1) (by omega : 0 < d + 1)
  have hudivSmall : u / d = s + 1 := by
    apply Nat.div_eq_of_lt_le
    · dsimp [u]
      ring_nf
      omega
    · dsimp [u]
      ring_nf
      omega
  have hvdivSmall : v / d = s + 1 := by
    apply Nat.div_eq_of_lt_le
    · dsimp [v]
      ring_nf
      omega
    · dsimp [v]
      ring_nf
      omega
  have huBig := hCoh d (d + 1) u hd (by omega) hult
  have hvBig := hCoh d (d + 1) v hd (by omega) hvlt
  have huSmall := hCoh (d + 1) d u (by omega) hd (by simpa [Nat.mul_comm] using hult)
  have hvSmall := hCoh (d + 1) d v (by omega) hd (by simpa [Nat.mul_comm] using hvlt)
  rw [hudivBig] at huBig
  rw [hvdivBig] at hvBig
  rw [hudivSmall] at huSmall
  rw [hvdivSmall] at hvSmall
  have hSame : φ (d * (d + 1)) u / d = φ (d * (d + 1)) v / d := by
    simpa [Nat.mul_comm] using huSmall.trans hvSmall.symm
  have hAdj := div_succ_dist_le_one_of_same_block hd hSame
  constructor
  · rw [huBig, hvBig] at hAdj
    exact hAdj.2
  · rw [huBig, hvBig] at hAdj
    exact hAdj.1

/-- R009-T12: exact downwardness inequality inside one quotient block. -/
theorem r009_t12 : T12Statement := by
  unfold T12Statement collapse
  intro p d q s φ hp hd hs hφ
  have hp0 : p ≠ 0 := by omega
  have hc : (Nat.nthRoot p q) ^ p ≤ q := Nat.pow_nthRoot_le (Or.inl hp0)
  have hdc : d * (Nat.nthRoot p q) ^ p ≤ d * q := Nat.mul_le_mul_left d hc
  rw [Nat.mul_sub_left_distrib]
  omega

/-- R009-T14: idempotence reduces exactly to the residue retraction equation. -/
theorem r009_t14 : T14Statement := by
  unfold T14Statement
  intro C φ hC d q s hd hs hφ
  dsimp
  let F : ℕ → ℕ := fun m => d * C (m / d) + φ (m / d) d (m % d)
  have hdiv0 : (d * q + s) / d = q := by
    apply Nat.div_eq_of_lt_le
    · omega
    · ring_nf
      omega
  have hmod0 : (d * q + s) % d = s := by
    simpa [Nat.mod_eq_of_lt hs] using Nat.mul_add_mod_self_left d q s
  have hdiv1 : (d * C q + φ q d s) / d = C q := by
    apply Nat.div_eq_of_lt_le
    · omega
    · ring_nf
      omega
  have hmod1 : (d * C q + φ q d s) % d = φ q d s := by
    simpa [Nat.mod_eq_of_lt hφ] using Nat.mul_add_mod_self_left d (C q) (φ q d s)
  change F (F (d * q + s)) = F (d * q + s) ↔ _
  simp only [F, hdiv0, hmod0, hdiv1, hmod1, hC q]
  exact Nat.add_left_cancel_iff

/-- R009-T22: scales 1 and 2 already obstruct bare perfect-power image semantics. -/
theorem r009_t22 : T22Statement := by
  unfold T22Statement
  intro p hp
  rintro ⟨F, hNat, hOne, hPow⟩
  have hp0 : p ≠ 0 := by omega
  have hq : F 2 2 / 2 = 1 := by
    have h := hNat 1 2 2 (by omega) (by omega)
    simpa [hOne, collapse] using h
  have hFlt : F 2 2 < 4 := by omega
  obtain ⟨k, hk⟩ := hPow 2 2 (by omega)
  have hk2 : 2 ≤ k := by
    by_contra hnot
    have hk01 : k = 0 ∨ k = 1 := by omega
    rcases hk01 with rfl | rfl
    · simp [hp0] at hk
      omega
    · simp at hk
      omega
  have h4 : 4 ≤ k ^ p := by
    calc
      4 = 2 ^ 2 := by norm_num
      _ ≤ k ^ 2 := Nat.pow_le_pow_left hk2 2
      _ ≤ k ^ p := Nat.pow_le_pow_right (by omega : 0 < k) hp
  rw [hk] at hFlt
  omega

/-- R009-T23: zero/top residue lifts are respectively left/right adjoint to scale-1 evaluation. -/
theorem r009_t23 : T23Statement := by
  unfold T23Statement
  constructor
  · intro H F hNat
    constructor
    · intro hLE n
      have h := hLE 1 n (by omega)
      simpa [zeroResidueLift, EndLE] using h
    · intro hH d m hd
      obtain ⟨ρ, hρ, hEq⟩ := r009_t02 F (F 1) hNat rfl d m hd
      have hbase : d * H (m / d) ≤ d * F 1 (m / d) :=
        Nat.mul_le_mul_left d (hH (m / d))
      rw [zeroResidueLift, hEq]
      exact hbase.trans (Nat.le_add_right _ _)
  · intro H F hNat
    constructor
    · intro hLE n
      have h := hLE 1 n (by omega)
      simpa [upperResidueLift, EndLE] using h
    · intro hH d m hd
      obtain ⟨ρ, hρ, hEq⟩ := r009_t02 F (F 1) hNat rfl d m hd
      have hbase : d * F 1 (m / d) ≤ d * H (m / d) :=
        Nat.mul_le_mul_left d (hH (m / d))
      have hρ' : ρ ≤ d - 1 := by omega
      rw [upperResidueLift, hEq]
      exact Nat.add_le_add hbase hρ'

end EnterpriseMath.R009
