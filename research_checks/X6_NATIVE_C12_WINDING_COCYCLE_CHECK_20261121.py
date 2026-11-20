import json
from pathlib import Path

# Frozen restricted OUTER native microcycle C12 physical phase.
# P_rot precision readouts are separate inverse-limit cyclic groups.
def phase(q,k):
    return (q+k)%12

def carry(q,k):
    return (q+k)//12

def increment(q,k):
    return k-12*carry(q,k)

def run():
    levels=range(9)
    steps=range(-24,25)
    pair_checks=0
    exact_checks=0
    for q in range(12):
        for k in steps:
            f=phase(q,k)
            d=increment(q,k)
            assert d==f-q
            for ell in steps:
                lhs=increment(q,k+ell)
                rhs=d+increment(f,ell)
                assert lhs==rhs
                exact_checks+=1
                for m in levels:
                    modulus=6*(2**m)
                    assert (lhs-rhs)%modulus==0
                    pair_checks+=1
    homogeneous=[a for a in range(24) if a%12==1]
    assert homogeneous==[1,13]
    assert all((12*a)%24==12 for a in homogeneous)
    seam=[increment(q,1) for q in range(12)]
    assert seam==[1]*11+[-11]
    assert sum(seam)==0
    cases=0
    for j in range(6):
        q=2*j
        delta=increment(q,6)
        assert delta%12==6
        for eps in (-1,1):
            assert (3*eps)%12!=delta%12
            cases+=1
    return {
      "schema":"X6_NATIVE_OUTER_C12_PROFINITE_CLOCK_COCYCLE_V1",
      "physical_microcycle":"C12_E_k_to_G_k_to_E_(k+1)",
      "precision_levels":list(levels),
      "physical_start_phases":12,
      "event_step_range":[-24,24],
      "exact_integer_cocycle_comparisons":exact_checks,
      "precision_readout_compatibility_comparisons":pair_checks,
      "mismatches":0,
      "single_cycle_fiber_section_increments":seam,
      "homogeneous_one_step_lifts_at_C24":homogeneous,
      "homogeneous_12_step_monodromy_mod_C24":12,
      "half_turn_oriented_chirality_cases":cases,
      "first_layer_half_turn_phase_increment_mod_12":6,
      "first_layer_root_lineage_residues_mod_12":[3,9],
      "status":"RESTRICTED_NATIVE_OUTER_C12_DERIVED_COROLLARY_NOT_FORMAL_ADMISSION",
      "note":"Profinite integer embedding is algebraic typing; does not construct an arbitrary-X6 physical precision mechanism."
    }

if __name__=="__main__":
    result=run()
    out=Path(__file__).with_name("X6_NATIVE_C12_WINDING_COCYCLE_RESULTS_20261121.json")
    out.write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(result,ensure_ascii=False))
