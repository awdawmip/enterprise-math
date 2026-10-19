import EnterpriseMath.Relation.DeepChamberColorBalance
import Mathlib.Tactic

namespace EnterpriseMath.CoreDeepEnergyBridge

open EnterpriseMath.DeepChamberColorBalance

noncomputable section

/-- Reduced factorial-core history: first color and one of the two final-slot orders. -/
abbrev CoreHistory := Fin 3 × Bool

/-- Deep constant-map state, indexed by its unique image/uncut color. -/
abbrev DeepColor := Fin 3

/-- Canonical first-color map from the six reduced core histories to three deep colors. -/
def coreToDeep : CoreHistory → DeepColor :=
  Prod.fst

/-- Color permutations act on the reduced core while retaining final-order provenance. -/
def actCore (σ : Equiv.Perm (Fin 3)) (s : CoreHistory) : CoreHistory :=
  (σ s.1, s.2)

/-- Color permutations act naturally on the deep constant-map color. -/
def actDeep (σ : Equiv.Perm (Fin 3)) (j : DeepColor) : DeepColor :=
  σ j

/-- The core-to-deep color map is equivariant. -/
theorem coreToDeep_equivariant
    (σ : Equiv.Perm (Fin 3)) (s : CoreHistory) :
    coreToDeep (actCore σ s) = actDeep σ (coreToDeep s) := by
  rfl

/-- Conditional uniform mass of one of the six core histories. -/
def coreConditionalAtomMass : ℝ :=
  1 / 6

/-- Full-packet mass of one of the three deepest constant-map states. -/
def deepFullPacketAtomMass : ℝ :=
  1 / 27

/-- Subprobability retained by one core history in the core-to-deep bridge. -/
def coreToDeepRetention : ℝ :=
  1 / 9

/-- Two core histories of one first color, each retained with mass `1/9`, yield `1/27`. -/
theorem coreToDeep_pushes_atom_mass :
    2 * coreConditionalAtomMass * coreToDeepRetention =
      deepFullPacketAtomMass := by
  norm_num [coreConditionalAtomMass, coreToDeepRetention,
    deepFullPacketAtomMass]

/-- The three deep colors have total full-packet mass `1/9`. -/
theorem deepFullPacket_total_mass :
    3 * deepFullPacketAtomMass = coreToDeepRetention := by
  norm_num [deepFullPacketAtomMass, coreToDeepRetention]

/-- Conditional factorial-core color energy. -/
def coreConditionalEnergy (h : Fin 3 → ℝ) : ℝ :=
  normalizedColorEnergy h

/-- Deep color energy measured in the full 27-state packet. -/
def deepFullPacketEnergy (h : Fin 3 → ℝ) : ℝ :=
  ((h 0) ^ 2 + (h 1) ^ 2 + (h 2) ^ 2) / 27

/-- Core energy after the weighted `S_3` mixer scales each standard amplitude by `1/3`. -/
def mixedCoreEnergy (h : Fin 3 → ℝ) : ℝ :=
  coreConditionalEnergy (fun i => h i / 3)

/-- Full-packet deep energy is exactly one ninth of conditional core energy. -/
theorem deepFullPacketEnergy_eq_one_ninth_core
    (h : Fin 3 → ℝ) :
    deepFullPacketEnergy h =
      (1 / 9 : ℝ) * coreConditionalEnergy h := by
  unfold deepFullPacketEnergy coreConditionalEnergy normalizedColorEnergy
  ring

/-- The mixed conditional core energy is exactly one ninth of its input. -/
theorem mixedCoreEnergy_eq_one_ninth_core
    (h : Fin 3 → ℝ) :
    mixedCoreEnergy h =
      (1 / 9 : ℝ) * coreConditionalEnergy h := by
  unfold mixedCoreEnergy coreConditionalEnergy normalizedColorEnergy
  ring

/-- Amplitude contraction on the core and mass attenuation on the deep packet are isometric. -/
theorem mixedCoreEnergy_eq_deepFullPacketEnergy
    (h : Fin 3 → ℝ) :
    mixedCoreEnergy h = deepFullPacketEnergy h := by
  rw [mixedCoreEnergy_eq_one_ninth_core,
    deepFullPacketEnergy_eq_one_ninth_core]

/-- The bridge keeps the color amplitude while moving the `1/9` factor into measure. -/
theorem amplitude_measure_tradeoff
    (h : Fin 3 → ℝ) :
    coreConditionalEnergy (fun i => h i / 3) =
      deepFullPacketEnergy h :=
  mixedCoreEnergy_eq_deepFullPacketEnergy h

end

end EnterpriseMath.CoreDeepEnergyBridge
