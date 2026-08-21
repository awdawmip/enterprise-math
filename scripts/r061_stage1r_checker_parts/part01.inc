        "expected_incident_set": tuple(on_boundary)==tuple(sorted(INCIDENT3)),
        "pairwise_spacing_exact": len(pairwise)==3 and all(r["q3"]==9 for r in pairwise),
        "origin_radius_exact": all(q3(p)==3 for p in on_boundary),
        "no_fourth_boundary_center": len(on_boundary)==3 and next_shell>3,
        "one_anchor_per_open_sector": all(len(sector_members[s])==1 for s in SECTORS),
        "no_anchor_on_axis": len(axis_hits)==0,
        "cyclic_counts_equal": len({len(sector_members[s]) for s in SECTORS})==1,
        "mirror_counts_equal": all(mirror_sector_counts[s]==1 for s in SECTORS),
    }
    cert={
        "schema":"R061_STAGE1R_ORIGIN_INCIDENCE_CERTIFICATE_V1",
        "carrier_scale":"3x integer coordinates; q3/9 is carrier squared length",
        "carrier_quadratic_form":"q3(x,y)=x^2+y^2-xy",
        "exhaustive_bound":"4*q3=(2x-y)^2+3y^2=(2y-x)^2+3x^2; q3<=12 => |x|,|y|<=4",
        "cell_radius_squared":"1/3",
        "incident_centers_3x":[list(p) for p in on_boundary],
        "incident_center_q3":[q3(p) for p in on_boundary],
        "pairwise_center_separation_q3":pairwise,
        "next_center_shell_q3":next_shell,
        "next_center_shell_distance_squared":f"{next_shell}/9",
        "sector_members_3x":{s:[list(p) for p in sector_members[s]] for s in SECTORS},
        "axis_hit_count":len(axis_hits),
        "mirror_sector_counts":mirror_sector_counts,
        "anchor3":{s:list(ANCHOR3[s]) for s in SECTORS},
        "checks":pass_flags,
        "pass":all(pass_flags.values()),
    }
    return cert

# ----------------------- Typed affine replay --------------------------

def affine_typing_audit(max_total: int = 18):
    mismatches=[]
    checked=0
    for sector in SECTORS:
        anchor=ANCHOR3[sector]
        for n in range(max_total+1):
            for a in range(n+1):
                b=n-a
                v=vertex3(sector,a,b)
                c=center3(sector,a,b)
                checked += 1
                tests=[
                    ("constant_anchor", sub(c,v)==anchor),
                    ("terminal_incidence", q3(sub(c,v))==3),
                    ("typed_origin_vertex", (a,b)!=(0,0) or v==(0,0)),
                    ("center_not_origin_at_zero", (a,b)!=(0,0) or c!=(0,0)),
                    ("center_in_sector", is_open_sector_global3(sector,c)),
                ]
                for kind,ok in tests:
                    if not ok and len(mismatches)<20:
                        mismatches.append({"sector":sector,"a":a,"b":b,"kind":kind,
                                           "vertex3":v,"center3":c,"anchor3":anchor})
    return {"tested_endpoint_records":checked,
            "max_a_plus_b":max_total,
            "mismatch_count":len(mismatches),
            "mismatch_examples":mismatches,
            "V_00_is_origin":all(vertex3(s,0,0)==(0,0) for s in SECTORS),
            "C_00_is_not_origin":all(center3(s,0,0)!=(0,0) for s in SECTORS),
            "pass":not mismatches}

def local_states_from_word(w: str):
    x=y=0
    st=[(0,0)]
    for ch in w:
        if ch=="X": x+=1
        elif ch=="Y": y+=1
        else: raise ValueError(ch)
        st.append((x,y))
    return st

def physical_centers_from_states(sector: str, states):
    return [center3(sector,a,b) for a,b in states]

def trace_native_replay(max_total: int = 18):
    """Explicitly enumerate every trace linearization and all three sector realizations.

    The local prefix (x,y) is the typed CADDR index. Exact sector formulas are
    checked directly without allocating full physical-center lists:
      S12 center3=(1+3x, 2+3y)
      S23 center3=(-2-3y, -1+3x-3y)
      S31 center3=(1-3x+3y, -1-3x)
    """
    h=hashlib.sha256()
    pairs=formal=paths=0
    bad_neighbor=bad_endpoint=bad_sector=bad_single=duplicates=0
    first_mismatches=[]

    # Exact nearest-neighbor certificate for each active basis letter.
    basis_neighbor_ok = {
        s: q3(BASIS3[s][0])==9 and q3(BASIS3[s][1])==9
        for s in SECTORS
    }

    def sector_prefix_ok(s,x,y):
        if s=="S12":
            gx,gy=1+3*x,2+3*y
            return gx>0 and gy>0
        if s=="S23":
            gx,gy=-2-3*y,-1+3*x-3*y
            return gx<0 and (gy-gx)>0
        gx,gy=1-3*x+3*y,-1-3*x
        return gy<0 and (gx-gy)>0

    for n in range(max_total+1):
        for a in range(n+1):
            b=n-a; pairs+=1
            seen_masks=set()
            for pos in itertools.combinations(range(n),a):
                mask=0
                chars=["Y"]*n
                for i in pos:
                    mask |= 1<<i
                    chars[i]="X"
                if mask in seen_masks:
                    duplicates += 1
                seen_masks.add(mask)
                w="".join(chars)

                x=y=0
                states_parts=["0.0"]
                word_semantic_ok=True
                sector_ok={s:sector_prefix_ok(s,0,0) for s in SECTORS}
                for ch in chars:
                    if ch=="X": x+=1
                    elif ch=="Y": y+=1
                    else: word_semantic_ok=False
                    states_parts.append(f"{x}.{y}")
                    for s in SECTORS:
                        sector_ok[s] = sector_ok[s] and sector_prefix_ok(s,x,y)
                state_serial=";".join(states_parts)

                if (x,y)!=(a,b):
                    bad_endpoint += 3
                    if len(first_mismatches)<20:
                        first_mismatches.append({"kind":"endpoint","a":a,"b":b,"word":w})
                if not word_semantic_ok:
                    bad_single += 3
                formal += 1

                for s in SECTORS:
                    h.update(f"{s}:{a},{b}:{w}:{state_serial}\n".encode())
                    paths += 1
                    if not basis_neighbor_ok[s]:
                        bad_neighbor += n
                    if not sector_ok[s]:
                        bad_sector += 1
                        if len(first_mismatches)<20:
                            first_mismatches.append({"kind":"sector","sector":s,"a":a,"b":b,"word":w})

            if len(seen_masks)!=comb(n,a):
                if len(first_mismatches)<20:
                    first_mismatches.append({"kind":"trace_cardinality","a":a,"b":b,
                                             "observed":len(seen_masks),"expected":comb(n,a)})
    return {
        "max_a_plus_b":max_total,
        "pair_count":pairs,
        "formal_linearization_count":formal,
        "three_sector_native_path_count":paths,
        "bad_neighbor_transition_count":bad_neighbor,
        "bad_endpoint_count":bad_endpoint,
        "bad_sector_prefix_count":bad_sector,
        "bad_single_cell_state_count":bad_single,
        "duplicate_trajectory_within_trace_pair_count":duplicates,
        "native_replay_sha256":h.hexdigest(),
        "mismatch_examples":first_mismatches,
    }

def compressed_trace(max_total: int = 256):
    h=hashlib.sha256(); mismatches=[]
    for n in range(max_total+1):
        for a in range(n+1):
            b=n-a; c=comb(n,a)
            h.update(f"{n},{a},{b},{c}\n".encode())
            if 0<a<n and c != comb(n-1,a-1)+comb(n-1,a):
                if len(mismatches)<20:
                    mismatches.append({"n":n,"a":a,"b":b,"count":str(c)})
    return {"max_a_plus_b":max_total,
            "mismatch_count":len(mismatches),
            "mismatch_examples":mismatches,
            "compressed_trace_sha256":h.hexdigest()}

# ---------------- third direction and diamonds ------------------------

def third_direction_audit(max_total: int = 18):
    mismatches=[]
    tested=0
    smallest=None
    for sector in SECTORS:
        ui,uj=BASIS3[sector]
        diag=add(ui,uj)  # carrier reverse-third direction = -t_k
        if q3(diag)!=9:
            mismatches.append({"kind":"diag_not_neighbor","sector":sector,"diag3":diag})
        for n in range(2,max_total+1):
            for a in range(1,n):
                b=n-a
                start=center3(sector,0,0)
                end=center3(sector,a,b)
                m=min(a,b)
                rem_i=a-m; rem_j=b-m
                step_labels=["-Xk"]*m + ["Xi"]*rem_i + ["Xj"]*rem_j
                p=start
                for lab in step_labels:
                    if lab=="-Xk": step=diag
                    elif lab=="Xi": step=ui
                    else: step=uj
                    if q3(step)!=9 and len(mismatches)<20:
                        mismatches.append({"kind":"third_path_nonneighbor","sector":sector,"a":a,"b":b,"label":lab})
                    p=add(p,step)
                same_endpoint=(p==end)
                different_trace=any(lab=="-Xk" for lab in step_labels)
                tested += 1
                if not same_endpoint or not different_trace:
                    if len(mismatches)<20:
                        mismatches.append({"kind":"classification","sector":sector,"a":a,"b":b,
                                           "same_endpoint":same_endpoint,"different_trace":different_trace})
                if (a,b)==(1,1) and smallest is None:
                    s=start
                    xi=add(s,ui); xj=add(s,uj); terminal=add(xi,uj)
                    direct=add(s,diag)
                    smallest={
                        "sector":sector,"N":2,"branch":[1,1],
                        "trace_representatives":["XiXj","XjXi"],
                        "carrier_shortcut":["-Xk"],
                        "start_center3":list(s),
                        "Xi_intermediate3":list(xi),
                        "Xj_intermediate3":list(xj),
                        "terminal_center3":list(terminal),
                        "direct_terminal_center3":list(direct),
                        "same_carrier_endpoint":terminal==direct,
                        "trace_component_labels_preserved_by_shortcut":False,
                        "classification":"CARRIER_ONLY_SHORTCUT_NOT_NATIVE_LINE",
                    }
    return {"tested_nondegenerate_sector_branches":tested,
            "smallest_witness":smallest,
            "mismatch_count":len(mismatches),
            "mismatch_examples":mismatches,
            "classification_basis":"native component labels; jump count not used",
            "pass":not mismatches}

def commutation_diamond_audit(max_prefix_total: int = 18):
    mismatches=[]; count=0
    for sector in SECTORS:
        ui,uj=BASIS3[sector]
        for n in range(max_prefix_total+1):
            for p in range(n+1):
                q=n-p
                start=center3(sector,p,q)
                mid_i=add(start,ui); mid_j=add(start,uj)
                end_ij=add(mid_i,uj); end_ji=add(mid_j,ui)
                count += 1
                checks={
                    "distinct_intermediates":mid_i!=mid_j,
                    "same_terminal":end_ij==end_ji,
                    "edge_start_i":q3(sub(mid_i,start))==9,
                    "edge_i_j":q3(sub(end_ij,mid_i))==9,
                    "edge_start_j":q3(sub(mid_j,start))==9,
