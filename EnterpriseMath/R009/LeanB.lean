import Mathlib
import EnterpriseMath.R009.LeanA
import EnterpriseMath.R009.CollapseRigidityTargets

namespace EnterpriseMath.R009

private theorem top_mul_sub_one_div
    {d r : ℕ} (hd : 0 < d) (hr : 0 < r) :
    (d * r - 1) / r = d - 1 := by
  have hdr : 0 < d * r := Nat.mul_pos hd hr
  have hd1 : d - 1 + 1 = d := by omega
  apply Nat.div_eq_of_lt_le
  · simpa [hd1] using (Nat.sub_lt hdr (by omega : 0 < 1))
  · have hprod : d * r = (d - 1) * r + r := by
      calc
        d * r = (d - 1 + 1) * r := by rw [hd1]
        _ = (d - 1) * r + r := by ring
    omega

private theorem clamp_fixed_below
    (P : ScaleFamily) (hGrid : GridEndomorphism P)
    (hRed : LevelReductive P)
    {d a : ℕ} (hd : 0 < d) (ha : a < d)
    (hFix : P d a = a) :
    ∀ s ≤ a, P d s = s := by
  have hAdj : ∀ j : ℕ, j + 1 < d → P d (j + 1) ≤ P d j + 1 := by
    intro j hj
    exact (r009_t09 P hGrid d j hd hj).1
  have hSub : ∀ k : ℕ, k ≤ a → P d (a - k) = a - k := by
    intro k hk
    induction k with
    | zero => simpa using hFix
    | succ k ih =>
        have hk' : k ≤ a := by omega
        have hprev : P d (a - k) = a - k := ih hk'
        have hsucc : a - (k + 1) + 1 = a - k := by omega
        have hcur_lt : a - (k + 1) < d := by omega
        have hnext_lt : a - (k + 1) + 1 < d := by omega
        have hadj := hAdj (a - (k + 1)) hnext_lt
        rw [hsucc, hprev] at hadj
        have hred := hRed d (a - (k + 1)) hd hcur_lt
        omega
  intro s hsa
  have hk : a - s ≤ a := Nat.sub_le _ _
  have hs : a - (a - s) = s := Nat.sub_sub_self hsa
  simpa [hs] using hSub (a - s) hk

/-- R009-T17: coherent monotone reductive idempotent grid maps are exactly clamps. -/
theorem r009_t17 : T17Statement := by
  unfold T17Statement
  intro P hGrid hMono hRed hIdem
  rcases hGrid with ⟨hRange, hCoh⟩
  let a : ℕ → ℕ := fun d => if d = 0 then 0 else P d (d - 1)
  have haEndpoint : Endpoint a := by
    refine ⟨?_, ?_, ?_⟩
    · simp [a]
    · intro d hd
      simp [a, ne_of_gt hd]
      exact hRange d (d - 1) hd (by omega)
    · intro d r hd hr
      have hdr : 0 < d * r := Nat.mul_pos hd hr
      have htop : d * r - 1 < d * r := by omega
      have hc := hCoh d r (d * r - 1) hd hr htop
      have hq : (d * r - 1) / r = d - 1 := top_mul_sub_one_div hd hr
      simp [a, ne_of_gt hd, ne_of_gt hdr, hq]
      simpa [hq] using hc
  have hClamp : ∀ d s, 0 < d → s < d → P d s = min s (a d) := by
    intro d s hd hs
    have hdne : d ≠ 0 := ne_of_gt hd
    have htop : d - 1 < d := by omega
    have ha_def : a d = P d (d - 1) := by simp [a, hdne]
    have ha_lt : a d < d := haEndpoint.2.1 d hd
    have hFixA : P d (a d) = a d := by
      rw [ha_def]
      exact hIdem d (d - 1) hd htop
    by_cases hsa : s ≤ a d
    · have hfix := clamp_fixed_below P ⟨hRange, hCoh⟩ hRed hd ha_lt hFixA s hsa
      simpa [min_eq_left hsa] using hfix
    · have has : a d ≤ s := by omega
      have htopEq : P d (d - 1) = a d := ha_def.symm
      have hs_top : s ≤ d - 1 := by omega
      have hlow := hMono d (a d) s hd ha_lt hs has
      have hupp := hMono d s (d - 1) hd hs htop hs_top
      rw [hFixA] at hlow
      rw [htopEq] at hupp
      have heq : P d s = a d := le_antisymm hupp hlow
      simpa [min_eq_right has] using heq
  refine ⟨a, ⟨haEndpoint, hClamp⟩, ?_⟩
  intro b hb
  funext d
  by_cases hd0 : d = 0
  · subst d
    exact haEndpoint.1.trans hb.1.1.symm
  · have hd : 0 < d := Nat.pos_of_ne_zero hd0
    have htop : d - 1 < d := by omega
    have hb_lt : b d < d := hb.1.2.1 d hd
    have hb_le : b d ≤ d - 1 := by omega
    have hform := hb.2 d (d - 1) hd htop
    have hmin : min (d - 1) (b d) = b d := min_eq_right hb_le
    simp [a, hd0]
    rw [hform, hmin]

end EnterpriseMath.R009

namespace EnterpriseMath.R009

private theorem div_mul_add_small
    {d q s : ℕ} (hd : 0 < d) (hs : s < d) :
    (d * q + s) / d = q := by
  apply Nat.div_eq_of_lt_le
  · ring_nf
    omega
  · ring_nf
    omega

private theorem mod_mul_add_small
    {d q s : ℕ} (hs : s < d) :
    (d * q + s) % d = s := by
  rw [Nat.mul_add_mod_self_left, Nat.mod_eq_of_lt hs]

private theorem div_min (x y r : ℕ) :
    min x y / r = min (x / r) (y / r) := by
  rcases le_total x y with hxy | hyx
  · have hdiv : x / r ≤ y / r := Nat.div_le_div_right hxy
    simp [min_eq_left hxy, min_eq_left hdiv]
  · have hdiv : y / r ≤ x / r := Nat.div_le_div_right hyx
    simp [min_eq_right hyx, min_eq_right hdiv]

/-- R009-T18: complete four-axiom classification of natural lifts of `collapse p`. -/
theorem r009_t18 : T18Statement := by
  unfold T18Statement
  intro p hp F hOne
  have hp0 : p ≠ 0 := by omega
  constructor
  · rintro ⟨hNat, hDown, hIdem, hMono⟩
    let ρ : ScaleFamily := fun d m => F d m % d
    have hNF : ResidueNormalForm F (collapse p) ρ := by
      intro d m hd
      have hq : F d m / d = collapse p (m / d) := by
        have h := hNat 1 d m (by omega) hd
        simpa [hOne] using h
      refine ⟨Nat.mod_lt _ hd, ?_⟩
      calc
        F d m = (F d m / d) * d + F d m % d := by
          simpa [Nat.add_comm, Nat.mul_comm] using (Nat.div_add_mod (F d m) d).symm
        _ = d * collapse p (m / d) + ρ d m := by
          simp [ρ, hq, Nat.mul_comm]
    have hρCoh : ResidueCoherent ρ :=
      (r009_t03 F ρ (collapse p) hNF).1 hNat
    have hBlock : ∀ d q s : ℕ, 0 < d → s < d →
        F d (d * q + s) = d * collapse p q + ρ d (d * q + s) := by
      intro d q s hd hs
      have h := (hNF d (d * q + s) hd).2
      rw [div_mul_add_small hd hs] at h
      exact h
    have hPerfectCollapse : ∀ k : ℕ, collapse p (k ^ p) = k ^ p := by
      intro k
      simp [collapse, Nat.nthRoot_pow hp0]
    have hTk : ∀ k : ℕ,
        ∃! a : ℕ → ℕ, Endpoint a ∧
          ∀ d s, 0 < d → s < d →
            ρ d (d * k ^ p + s) = min s (a d) := by
      intro k
      let P : ScaleFamily := fun d s => ρ d (d * k ^ p + s)
      have hGridP : GridEndomorphism P := by
        constructor
        · intro d s hd hs
          exact (hNF d (d * k ^ p + s) hd).1
        · intro d r t hd hr ht
          have h := hρCoh d r ((d * r) * k ^ p + t) hd hr
          have hquot : ((d * r) * k ^ p + t) / r = d * k ^ p + t / r := by
            calc
              ((d * r) * k ^ p + t) / r
                  = (t + r * (d * k ^ p)) / r := by congr 1 <;> ring
              _ = t / r + d * k ^ p := Nat.add_mul_div_left t (d * k ^ p) hr
              _ = d * k ^ p + t / r := by omega
          rw [hquot] at h
          exact h
      have hMonP : LevelMonotone P := by
        intro d s t hd hs ht hst
        have hFst := (hMono d hd) (Nat.add_le_add_left hst (d * k ^ p))
        have hsF := hBlock d (k ^ p) s hd hs
        have htF := hBlock d (k ^ p) t hd ht
        rw [hsF, htF, hPerfectCollapse k] at hFst
        exact Nat.add_le_add_iff_left.mp hFst
      have hRedP : LevelReductive P := by
        intro d s hd hs
        have hD := hDown d (d * k ^ p + s) hd
        have hF := hBlock d (k ^ p) s hd hs
        rw [hF, hPerfectCollapse k] at hD
        omega
      have hIdemP : LevelIdempotent P := by
        intro d s hd hs
        have hP_lt : P d s < d := hGridP.1 d s hd hs
        have hF1 : F d (d * k ^ p + s) = d * k ^ p + P d s := by
          have h := hBlock d (k ^ p) s hd hs
          simpa [P, hPerfectCollapse k] using h
        have hF2 : F d (d * k ^ p + P d s) = d * k ^ p + P d (P d s) := by
          have h := hBlock d (k ^ p) (P d s) hd hP_lt
          simpa [P, hPerfectCollapse k] using h
        have hI := hIdem d (d * k ^ p + s) hd
        rw [hF1, hF2] at hI
        exact Nat.add_left_cancel hI
      have hClamp := r009_t17 P hGridP hMonP hRedP hIdemP
      simpa [P] using hClamp
    choose a ha using fun k => (hTk k).exists
    refine ⟨a, ?_, ?_⟩
    · intro k
      exact (ha k).1
    · intro d q s hd hs
      let k : ℕ := Nat.nthRoot p q
      let c : ℕ := k ^ p
      let u : ℕ := ρ d (d * q + s)
      have hc_le : c ≤ q := by
        dsimp [c, k]
        exact Nat.pow_nthRoot_le (Or.inl hp0)
      have hcollapse_q : collapse p q = c := by rfl
      have hu_lt : u < d := by
        dsimp [u]
        exact (hNF d (d * q + s) hd).1
      have hF1 : F d (d * q + s) = d * c + u := by
        have h := hBlock d q s hd hs
        simpa [hcollapse_q, u] using h
      have hClampU :
          ρ d (d * c + u) = min u (a k d) := by
        have h := (ha k).2 d u hd hu_lt
        simpa [c] using h
      have hcCollapse : collapse p c = c := by
        dsimp [c]
        exact hPerfectCollapse k
      have hF2 : F d (d * c + u) = d * c + min u (a k d) := by
        have h := hBlock d c u hd hu_lt
        rw [hcCollapse] at h
        exact h.trans (congrArg (fun z => d * c + z) hClampU)
      have hI := hIdem d (d * q + s) hd
      rw [hF1, hF2] at hI
      have hminEq : min u (a k d) = u := Nat.add_left_cancel hI
      have hu_le_a : u ≤ a k d := by
        have hminle := min_le_right u (a k d)
        rw [hminEq] at hminle
        exact hminle
      by_cases hPerfect : q = c
      · subst q
        have hClampS := (ha k).2 d s hd hs
        change F d (d * c + s) = d * collapse p c + min s (a k d)
        rw [hcCollapse]
        have h := hBlock d c s hd hs
        rw [hcCollapse] at h
        rw [h]
        exact congrArg (fun z => d * c + z) (by simpa [c] using hClampS)
      · have hc_lt : c < q := lt_of_le_of_ne hc_le (Ne.symm hPerfect)
        have ha_lt : a k d < d := (ha k).1.2.1 d hd
        have htop : d - 1 < d := by omega
        have hClampTop := (ha k).2 d (d - 1) hd htop
        have ha_le_top : a k d ≤ d - 1 := by omega
        have hTopResid : ρ d (d * c + (d - 1)) = a k d := by
          rw [hClampTop, min_eq_right ha_le_top]
        have hstep : d * c + (d - 1) < d * (c + 1) := by
          ring_nf
          omega
        have hc1q : c + 1 ≤ q := by omega
        have htoStart : d * c + (d - 1) ≤ d * q :=
          (le_of_lt hstep).trans (Nat.mul_le_mul_left d hc1q)
        have hMonoStart := (hMono d hd) htoStart
        have hTopF : F d (d * c + (d - 1)) = d * c + a k d := by
          have h := hBlock d c (d - 1) hd htop
          rw [hcCollapse, hTopResid] at h
          exact h
        have hzero : (0 : ℕ) < d := hd
        have hStartF : F d (d * q) = d * c + ρ d (d * q) := by
          have h := hBlock d q 0 hd hzero
          simpa [hcollapse_q] using h
        rw [hTopF, hStartF] at hMonoStart
        have ha_le_rho0 : a k d ≤ ρ d (d * q) := by omega
        have hStartInput : d * q ≤ d * q + s := Nat.le_add_right _ _
        have hMonoS := (hMono d hd) hStartInput
        have hSF := hBlock d q s hd hs
        rw [hStartF, hSF, hcollapse_q] at hMonoS
        have hrho0_le_u : ρ d (d * q) ≤ u := by
          simpa [u] using Nat.add_le_add_iff_left.mp hMonoS
        have hu_eq : u = a k d := le_antisymm hu_le_a (ha_le_rho0.trans hrho0_le_u)
        change F d (d * q + s) = d * collapse p q + a k d
        rw [hF1, hcollapse_q, hu_eq]
  · rintro ⟨a, haEndpoint, hForm⟩
    have hPerfectCollapse : ∀ k : ℕ, collapse p (k ^ p) = k ^ p := by
      intro k
      simp [collapse, Nat.nthRoot_pow hp0]
    have hEndpointDiv : ∀ k d r, 0 < d → 0 < r → a k (d * r) / r = a k d := by
      intro k d r hd hr
      exact (haEndpoint k).2.2 d r hd hr
    have hFormula : ∀ d m : ℕ, 0 < d →
        let q := m / d
        let s := m % d
        let k := Nat.nthRoot p q
        F d m = d * collapse p q +
          (if q = k ^ p then min s (a k d) else a k d) := by
      intro d m hd
      have hs : m % d < d := Nat.mod_lt _ hd
      have h := hForm d (m / d) (m % d) hd hs
      simpa [Nat.mul_comm] using h
    refine ⟨?_, ?_, ?_, ?_⟩
    · unfold ScaleNatural
      intro d r m hd hr
      have hdr : 0 < d * r := Nat.mul_pos hd hr
      let q : ℕ := m / (d * r)
      let s : ℕ := m % (d * r)
      let k : ℕ := Nat.nthRoot p q
      have hs : s < d * r := by
        dsimp [s]
        exact Nat.mod_lt _ hdr
      have hsr : s / r < d := by
        exact (Nat.div_lt_iff_lt_mul hr).2 (by simpa [Nat.mul_comm] using hs)
      have hmdecomp : m = (d * r) * q + s := by
        dsimp [q, s]
        have h := Nat.div_add_mod m (d * r)
        omega
      have hmr : m / r = d * q + s / r := by
        rw [hmdecomp]
        calc
          ((d * r) * q + s) / r
              = (s + r * (d * q)) / r := by congr 1 <;> ring
          _ = s / r + d * q := Nat.add_mul_div_left s (d * q) hr
          _ = d * q + s / r := by omega
      have hBig := hForm (d * r) q s hdr hs
      have hSmall := hForm d q (s / r) hd hsr
      have haDiv := hEndpointDiv k d r hd hr
      have hResidDiv :
          (if q = k ^ p then min s (a k (d * r)) else a k (d * r)) / r =
          (if q = k ^ p then min (s / r) (a k d) else a k d) := by
        by_cases hperf : q = k ^ p
        · simp [hperf, div_min, haDiv]
        · simp [hperf, haDiv]
      rw [hmdecomp, hBig, hmr, hSmall]
      have hbase : (d * r) * collapse p q = r * (d * collapse p q) := by ring
      rw [hbase, Nat.add_comm (r * (d * collapse p q)), Nat.add_mul_div_left _ _ hr]
      exact congrArg (fun z => d * collapse p q + z) hResidDiv
    · unfold ScaleDownward
      intro d m hd
      let q : ℕ := m / d
      let s : ℕ := m % d
      let k : ℕ := Nat.nthRoot p q
      let c : ℕ := k ^ p
      have hs : s < d := by
        dsimp [s]
        exact Nat.mod_lt _ hd
      have hmdecomp : m = d * q + s := by
        dsimp [q, s]
        have h := Nat.div_add_mod m d
        omega
      have hF := hForm d q s hd hs
      have hc_le : c ≤ q := by
        dsimp [c, k]
        exact Nat.pow_nthRoot_le (Or.inl hp0)
      have ha_lt : a k d < d := (haEndpoint k).2.1 d hd
      rw [hmdecomp, hF]
      change d * collapse p q +
          (if q = c then min s (a k d) else a k d) ≤ d * q + s
      change d * c + (if q = c then min s (a k d) else a k d) ≤ d * q + s
      by_cases hperf : q = c
      · subst q
        simp [hperf, min_le_left]
      · have hc_lt : c < q := lt_of_le_of_ne hc_le (Ne.symm hperf)
        have hc1q : c + 1 ≤ q := by omega
        have hleft : d * c + a k d < d * (c + 1) := by
          ring_nf
          omega
        have hright : d * (c + 1) ≤ d * q := Nat.mul_le_mul_left d hc1q
        simp [hperf]
        omega
    · unfold ScaleIdempotent
      intro d m hd
      let q : ℕ := m / d
      let s : ℕ := m % d
      let k : ℕ := Nat.nthRoot p q
      let c : ℕ := k ^ p
      let u : ℕ := if q = c then min s (a k d) else a k d
      have hs : s < d := by
        dsimp [s]
        exact Nat.mod_lt _ hd
      have ha_lt : a k d < d := (haEndpoint k).2.1 d hd
      have hu_lt : u < d := by
        dsimp [u]
        split_ifs
        · exact lt_of_le_of_lt (min_le_right _ _) ha_lt
        · exact ha_lt
      have hu_le : u ≤ a k d := by
        dsimp [u]
        split_ifs
        · exact min_le_right _ _
        · exact le_rfl
      have hF1 : F d m = d * c + u := by
        have h := hFormula d m hd
        dsimp [q, s, k, c, u] at h ⊢
        simpa [collapse] using h
      have hcCollapse : collapse p c = c := by
        dsimp [c]
        exact hPerfectCollapse k
      have hF2 := hForm d c u hd hu_lt
      have hrootc : Nat.nthRoot p c = k := by
        dsimp [c]
        exact Nat.nthRoot_pow hp0 k
      rw [hF1]
      rw [hF2, hcCollapse, hrootc]
      simp [min_eq_left hu_le]
    · unfold ScaleMonotone
      intro d hd x y hxy
      let q : ℕ := x / d
      let s : ℕ := x % d
      let Q : ℕ := y / d
      let t : ℕ := y % d
      let k : ℕ := Nat.nthRoot p q
      let K : ℕ := Nat.nthRoot p Q
      let c : ℕ := k ^ p
      let C : ℕ := K ^ p
      have hs : s < d := by dsimp [s]; exact Nat.mod_lt _ hd
      have ht : t < d := by dsimp [t]; exact Nat.mod_lt _ hd
      have hxdec : x = d * q + s := by
        dsimp [q, s]
        have h := Nat.div_add_mod x d
        omega
      have hydec : y = d * Q + t := by
        dsimp [Q, t]
        have h := Nat.div_add_mod y d
        omega
      have hqQ : q ≤ Q := by
        dsimp [q, Q]
        exact Nat.div_le_div_right hxy
      have hkK : k ≤ K := by
        dsimp [k, K, q, Q]
        apply (Nat.le_nthRoot_iff hp0).2
        exact (Nat.pow_nthRoot_le (Or.inl hp0)).trans hqQ
      have hxF := hForm d q s hd hs
      have hyF := hForm d Q t hd ht
      rw [hxdec, hydec, hxF, hyF]
      change d * c + (if q = c then min s (a k d) else a k d) ≤
        d * C + (if Q = C then min t (a K d) else a K d)
      by_cases hqeq : q = Q
      · subst Q
        have hst : s ≤ t := by omega
        have hkEq : K = k := by rfl
        subst K
        have hCEq : C = c := by rfl
        subst C
        by_cases hperf : q = c
        · simp [hperf, min_le_min_right _ hst]
        · simp [hperf]
      · have hqLt : q < Q := lt_of_le_of_ne hqQ hqeq
        by_cases hkEq : k = K
        · subst K
          have hCEq : C = c := by rfl
          subst C
          have hc_le_q : c ≤ q := by
            dsimp [c, k, q]
            exact Nat.pow_nthRoot_le (Or.inl hp0)
          by_cases hqperf : q = c
          · have hQnot : Q ≠ c := by omega
            have hamin : min s (a k d) ≤ a k d := min_le_right _ _
            simp [hqperf, hQnot]
            exact Nat.add_le_add_left hamin (d * c)
          · have hQnot : Q ≠ c := by omega
            simp [hqperf, hQnot]
        · have hkLt : k < K := lt_of_le_of_ne hkK hkEq
          have hcC : c < C := by
            dsimp [c, C]
            exact (Nat.pow_left_strictMono hp0) hkLt
          have hres_lt : (if q = c then min s (a k d) else a k d) < d := by
            have ha_lt : a k d < d := (haEndpoint k).2.1 d hd
            split_ifs
            · exact lt_of_le_of_lt (min_le_right _ _) ha_lt
            · exact ha_lt
          have hc1C : c + 1 ≤ C := by omega
          have hleft : d * c + (if q = c then min s (a k d) else a k d) <
              d * (c + 1) := by
            ring_nf
            omega
          have hmiddle : d * (c + 1) ≤ d * C := Nat.mul_le_mul_left d hc1C
          have hbase : d * C ≤ d * C +
              (if Q = C then min t (a K d) else a K d) := Nat.le_add_right _ _
          exact (le_of_lt hleft).trans (hmiddle.trans hbase)

end EnterpriseMath.R009
