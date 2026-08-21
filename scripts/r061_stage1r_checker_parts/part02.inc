                    "edge_j_i":q3(sub(end_ji,mid_j))==9,
                    "terminal_matches_chart":end_ij==center3(sector,p+1,q+1),
                    "all_states_sector":all(is_open_sector_global3(sector,x) for x in (start,mid_i,mid_j,end_ij)),
                }
                if not all(checks.values()) and len(mismatches)<20:
                    mismatches.append({"sector":sector,"p":p,"q":q,"checks":checks})
    return {"tested_diamonds":count,"max_prefix_a_plus_b":max_prefix_total,
            "mismatch_count":len(mismatches),"mismatch_examples":mismatches,
            "pass":not mismatches}

# ------------------- axis gluing / composition ------------------------

def axis_local_pair(sector: str, component_index: int, n: int):
    return (n,0) if component_index==0 else (0,n)

def canonical_axis_trajectory(sector: str, component_index: int, n: int):
    w=("X"*n) if component_index==0 else ("Y"*n)
    return tuple(physical_centers_from_states(sector,local_states_from_word(w)))

def axis_gluing_audit(max_radius: int = 18):
    duplicate_physical=0; mismatches=[]; rows=[]
    identity_count=0; presentation_count=0
    for axis,presentations in AXIS_CHARTS.items():
        row={"axis":axis,"charts":[p[0] for p in presentations],"radial_rows":[]}
        for n in range(max_radius+1):
            identity=(axis,n); identity_count+=1
            trajs=[]
            for sector,idx in presentations:
                local=axis_local_pair(sector,idx,n)
                traj=canonical_axis_trajectory(sector,idx,n)
                presentation_count+=1
                trajs.append((sector,local,traj))
            same_identity=True
            distinct=(trajs[0][2] != trajs[1][2])
            if not distinct: duplicate_physical += 1
            if not same_identity and len(mismatches)<20:
                mismatches.append({"axis":axis,"n":n,"kind":"identity"})
            row["radial_rows"].append({"n":n,"identity":list(identity),
                                       "distinct_adjacent_sector_trajectories":distinct,
                                       "start_centers3":[list(t[2][0]) for t in trajs]})
        rows.append(row)
    return {"axis_range":[0,max_radius],
            "global_axis_line_identity_count":identity_count,
            "chart_presentation_count":presentation_count,
            "physical_trajectory_duplicate_count":duplicate_physical,
            "mismatch_count":len(mismatches),
            "rows":rows,
            "pass":not mismatches and duplicate_physical==0}

def bubble_normalize(w: str):
    arr=list(w); swaps=0
    changed=True
    while changed:
        changed=False
        for i in range(len(arr)-1):
            if arr[i]=="Y" and arr[i+1]=="X":
                arr[i],arr[i+1]=arr[i+1],arr[i]
                swaps+=1; changed=True
    return "".join(arr),swaps

def scaling_concatenation_audit(parameter_limit: int = 8, closure_explicit_max_total: int = 16):
    mismatches=[]
    scale_cases=0
    for a in range(parameter_limit+1):
        for b in range(parameter_limit+1):
            for k in range(parameter_limit+1):
                scale_cases+=1
                repeated=(a*k,b*k)
                target=(k*a,k*b)
                if repeated != target and len(mismatches)<20:
                    mismatches.append({"kind":"scale","a":a,"b":b,"k":k})
    concat_cases=0
    for a in range(parameter_limit+1):
        for b in range(parameter_limit+1):
            for c in range(parameter_limit+1):
                for d in range(parameter_limit+1):
                    concat_cases+=1
                    A,B=a+c,b+d
                    w=("X"*a+"Y"*b)+("X"*c+"Y"*d)
                    if w.count("X")!=A or w.count("Y")!=B:
                        if len(mismatches)<20:
                            mismatches.append({"kind":"concat_membership","params":[a,b,c,d]})
    closure_words=0
    for n in range(closure_explicit_max_total+1):
        for a in range(n+1):
            canonical="X"*a+"Y"*(n-a)
            for pos in itertools.combinations(range(n),a):
                w=make_word(n,pos)
                norm,_=bubble_normalize(w)
                closure_words+=1
                if norm!=canonical and len(mismatches)<20:
                    mismatches.append({"kind":"commutation_closure","n":n,"a":a,"word":w,"normalized":norm})
    return {"parameter_limit":parameter_limit,
            "scaling_cases":scale_cases,
            "concatenation_cases":concat_cases,
            "closure_explicit_max_a_plus_b":closure_explicit_max_total,
            "closure_explicit_words":closure_words,
            "mismatch_count":len(mismatches),
            "mismatch_examples":mismatches,
            "identity_law":"T_(a,b)*T_(c,d)=T_(a+c,b+d)",
            "closure_rule":"adjacent YX<->XY commutations connect every fixed-count word to X^A Y^B",
            "pass":not mismatches}

# ------------------------ exact N examples ----------------------------

def fiber_for_N(N: int):
    out=set()
    for a in range(isqrt(N)+1):
        b2=N-a*a; b=isqrt(b2)
        if b*b==b2:
            out.add((a,b)); out.add((b,a))
    return sorted(out)

def exact_examples():
    records={}
    for N in MANDATORY_N:
        branches=[]
        for a,b in fiber_for_N(N):
            rec={"a":a,"b":b,"path_count":comb(a+b,a),"native_length_squared":N}
            if N==25 and (a,b) in ((3,4),(4,3)):
                xcount=a
                rec["path_ids"]=[
                    f"S12-T{a}-{b}-XPOS-"+"-".join(str(i+1) for i in pos)
                    for pos in itertools.combinations(range(a+b),xcount)
                ]
            branches.append(rec)
        records[str(N)]={
            "branches":branches,
            "sector_total_path_count":sum(r["path_count"] for r in branches),
            "representable":bool(branches),
        }
    scaled=[{"a":a,"b":b,"r":r,"N":r*r,"valid":a*a+b*b==r*r,
             "path_count":comb(a+b,a)} for a,b,r in SCALED_TRIPLES]
    nonrep={str(N):len(fiber_for_N(N))==0 for N in NONREPRESENTABLE}
    n25=records["25"]
    n25_counts={(r["a"],r["b"]):r["path_count"] for r in n25["branches"]}
    n25_check={
        "D25":[[r["a"],r["b"]] for r in n25["branches"]],
        "branch_3_4_path_count":n25_counts.get((3,4)),
        "branch_4_3_path_count":n25_counts.get((4,3)),
        "axis_0_5_path_count":n25_counts.get((0,5)),
        "axis_5_0_path_count":n25_counts.get((5,0)),
        "sector_total_path_count":n25["sector_total_path_count"],
        "decomposition":"generated sum of branch path counts",
    }
    return {"mandatory":records,"scaled_triples":scaled,
            "nonrepresentable":nonrep,"n25":n25_check}

# ---------------------------- orchestration ---------------------------

def append_mismatch(mismatches, category, expected, observed, locator=None):
    mismatches.append({
        "category":category,
        "expected":expected,
        "observed":observed,
        "locator":locator,
    })

def native_phase_bundle():
    return {
        "origin": origin_incidence_certificate(),
        "affine": affine_typing_audit(),
        "replay": trace_native_replay(),
        "compressed": compressed_trace(),
        "third": third_direction_audit(),
        "diamonds": commutation_diamond_audit(),
        "gluing": axis_gluing_audit(),
        "composition": scaling_concatenation_audit(),
        "examples": exact_examples(),
    }

def finalize_results(out: Path, native: dict, s0: dict, s0cmp: dict, command: str):
    mismatches=[]
    origin=native["origin"]; affine=native["affine"]; replay=native["replay"]
    compressed=native["compressed"]; third=native["third"]; diamonds=native["diamonds"]
    gluing=native["gluing"]; composition=native["composition"]; examples=native["examples"]

    # Frozen Stage 0 comparisons after actual generation.
    for key,target_key in (
        ("coordinate_fiber_sha256","coordinate_fiber_sha256"),
        ("explicit_shuffle_sha256","explicit_shuffle_sha256"),
        ("compressed_pascal_sha256","compressed_pascal_sha256"),
        ("explicit_shuffle_word_count","explicit_shuffle_word_count"),
    ):
        observed=s0[key]; expected=FROZEN_STAGE0_TARGETS[target_key]
        if observed != expected:
            append_mismatch(mismatches,"stage0_regression",expected,observed,key)
    if s0["euclid_mismatch_count"] != 0:
        append_mismatch(mismatches,"stage0_euclid",0,s0["euclid_mismatch_count"],"r<=4096")
    if s0["shuffle_mismatch_count"] != 0:
        append_mismatch(mismatches,"stage0_shuffle_semantics",0,s0["shuffle_mismatch_count"],"a+b<=22")
    if s0["pascal_mismatch_count"] != 0:
        append_mismatch(mismatches,"stage0_pascal",0,s0["pascal_mismatch_count"],"a+b<=512")

    comparisons = {
        "pair_count": replay["pair_count"] == CLAIMED_STAGE1_TARGETS["pair_count"],
        "formal_linearization_count": replay["formal_linearization_count"] == CLAIMED_STAGE1_TARGETS["formal_linearization_count"],
        "three_sector_native_path_count": replay["three_sector_native_path_count"] == CLAIMED_STAGE1_TARGETS["three_sector_native_path_count"],
        "native_replay_sha256": replay["native_replay_sha256"] == CLAIMED_STAGE1_TARGETS["native_replay_sha256"],
        "compressed_trace_sha256": compressed["compressed_trace_sha256"] == CLAIMED_STAGE1_TARGETS["compressed_trace_sha256"],
    }
    observed_map={
        "pair_count":replay["pair_count"],
        "formal_linearization_count":replay["formal_linearization_count"],
        "three_sector_native_path_count":replay["three_sector_native_path_count"],
        "native_replay_sha256":replay["native_replay_sha256"],
        "compressed_trace_sha256":compressed["compressed_trace_sha256"],
    }
    for k,ok in comparisons.items():
        if not ok:
            append_mismatch(mismatches,"stage1_claimed_evidence",CLAIMED_STAGE1_TARGETS[k],observed_map[k],k)

    structural_checks={
        "origin_incidence":origin["pass"],
        "affine_typing":affine["pass"],
        "native_replay_semantics":all(replay[k]==0 for k in (
            "bad_neighbor_transition_count","bad_endpoint_count","bad_sector_prefix_count",
            "bad_single_cell_state_count","duplicate_trajectory_within_trace_pair_count")),
        "compressed_trace":compressed["mismatch_count"]==0,
        "third_direction_classification":third["pass"],
        "commutation_diamonds":diamonds["pass"],
        "axis_gluing":gluing["pass"],
        "scaling_concatenation":composition["pass"],
        "n25_72":examples["n25"]["branch_3_4_path_count"]==35 and
                  examples["n25"]["branch_4_3_path_count"]==35 and
                  examples["n25"]["axis_0_5_path_count"]==1 and
                  examples["n25"]["axis_5_0_path_count"]==1 and
                  examples["n25"]["sector_total_path_count"]==72,
        "scaled_triples":all(r["valid"] for r in examples["scaled_triples"]),
        "nonrepresentable_examples":all(examples["nonrepresentable"].values()),
