import json, hashlib, pathlib
OUT=pathlib.Path('/mnt/data/r055_work/artifacts')
OUT.mkdir(parents=True, exist_ok=True)

def dump(name,obj):
    p=OUT/name
    data=json.dumps(obj,ensure_ascii=False,sort_keys=True,indent=2,separators=(',', ': '))+'\n'
    p.write_text(data,encoding='utf-8')
    h=hashlib.sha256(data.encode()).hexdigest()
    print(name,h)

construction=[19,31,37,53,61,79,91,113,127,151,169,199,217]
holdout=[43,67,103,139,181,241,301]
small=list(range(1,13))
dirs=[[1,0],[0,1],[-1,1],[-1,0],[0,-1],[1,-1]]
protocol={
  'schema':'R055_RELAXATION_PROTOCOL_V1',
  'task_id':'RS-R055-FIXED-N-GRAVITY-RELAXATION-SELF-CENTERED-SHAPE',
  'researcher_id':'EM-R055-4C2A71',
  'taskbook_source':'18072ad7a3ca50728b23e0fc21478b98ed027631',
  'packet_source':'73e48ac77f403dc468cdea3458e14d10130386e0',
  'frozen_at':'2026-08-13T19:28:00+08:00',
  'generation':'R055-G0',
  'status':'FROZEN_BEFORE_CONSTRUCTION_TRAJECTORIES',
  'semantic_typing':{
    'lattice_coordinates':'I0_IMPLEMENTATION_CARRIER + task-declared operational affine geometry',
    'occupancy_and_nearest_neighbor_adjacency':'task-declared base relational substrate for R055',
    'boundary_move_rule':'N1_DERIVED_OPERATIONAL_SEMANTICS',
    'centroid_gravity_moment_diagnostics':'N2_READOUT_COLLAPSE',
    'external_disk_hexagon_models':'N3_CONTINUUM_CLASSICAL; forbidden until post-ledger/post-holdout comparison stage',
    'native_claim_policy':'No centroid, Euclidean metric, quadratic gravity, disk, or hexagon is promoted to N0-native by this task.'
  },
  'lattice':{
    'type':'normalized_triangular_lattice','axial_coordinate_domain':'Z^2',
    'basis_symbolic':['e1=(1,0)','e2=(1/2,sqrt(3)/2)'],'neighbor_directions':dirs,
    'quadratic_form':'Q(a,b)=a^2+a*b+b^2','cell_scale':'ell_0 symbolic','cell_mass':1
  },
  'state_predicate':{
    'fixed_cardinality':'|C|=N',
    'connected':'all occupied sites form one component under the six nearest-neighbor directions',
    'hole_free':('Within the axial bounding box of C padded by 1 in each coordinate, flood-fill empty sites from every empty site on the padded-box boundary using the same six-neighbor adjacency. '
                 'C is hole-free iff every empty site in the unpadded bounding box is exterior-reachable. This finite test is translation-invariant and exactly detects finite empty components for finite C.'),
    'equivalence_for_shape_classes':'translation + D6','orientation_metadata':'retained for orientation-sensitive alternative tie-break diagnostics'
  },
  'boundary_definitions':{
    'occupied_boundary':'{u in C: at least one of u+d_k is not in C}',
    'exterior_frontier':'{v not in C: at least one of v-d_k is in C}',
    'post_removal_frontier':'frontier(C\\{u}) evaluated before v is added'
  },
  'centroid':{
    'definition':'g(C)=(1/N) sum_{x in C} x in the declared affine lattice realization',
    'machine_representation':'sum_axial=(S_a,S_b); centroid_axial=(S_a/N,S_b/N) as exact rationals',
    'recompute_after_each_accepted_move':True,'no_privileged_initial_center':True
  },
  'dynamics':{
    'D1_LOCAL_BOUNDARY_SLIDE':{
      'source':'occupied boundary u of current C','destination':'empty nearest-neighbor v=u+d_k that belongs to frontier(C\\{u})',
      'final_checks':['fixed N','lattice site','connected','hole-free'],'classification':'local boundary slide'
    },
    'D2_GLOBAL_BOUNDARY_RELOCATION_REFERENCE':{
      'source':'occupied boundary u of current C','destination':'any v in frontier(C\\{u}) with v not in original C and v != u',
      'final_checks':['fixed N','lattice site','connected','hole-free'],'classification':'nonlocal relocation reference; never relabel as local slide'
    }
  },
  'step_semantics':{
    'candidate_recomputation':'recompute legal move set from scratch after every accepted move','acceptance':'strict G(C_prime) < G(C) only',
    'selection':'steepest strict descent: first minimize G(C_prime), then apply frozen tie-break','plateau_moves':False,
    'stopping_condition':'no legal strict-descending move exists under the selected dynamics',
    'accepted_move_postconditions_order':['|C|=N','lattice legality','connected','hole-free','recompute centroid from all N cells','recompute legal move set','verify strict G descent']
  },
  'N_regimes':{'small_exhaustive':small,'construction':construction,'strict_holdout':holdout},
  'target_leakage_guards':{
    'classical_circle_in_move_selection':False,'teacher_center_in_move_selection':False,'radius_in_move_selection':False,
    'circumference_target_in_move_selection':False,'classical_pi_in_move_selection':False,'tangent_target_in_move_selection':False,
    'posthoc_weighted_objective':False,'external_shape_models_open_before_ledger_and_holdout_freeze':False
  }
}
energy={
 'schema':'R055_MOVE_ENERGY_REGISTRY_V1','generation':'R055-G0','status':'FROZEN_BEFORE_MOVE_SCORING',
 'primary_objective':{
   'id':'G','definition':'G(C)=N*I2(C)=sum_{unordered x<y} Q(x-y)',
   'equivalent_fast_form':'G(C)=N*sum_{x in C} Q(x)-Q(sum_{x in C} x)','integer_exact':True,'direction':'strict_decrease',
   'replacement_delta':('For d=v-u and S=sum_C x: DeltaG=N*(Q(v)-Q(u))-[L(S,d)+Q(d)], '
                        'where L((a,b),(c,d))=2ac+ad+bc+2bd=2<B(S,d)>.'),
   'move_ranking':['minimum G(C_prime)','frozen tie-break only among equal best G']
 },
 'diagnostics_not_optimization_targets':{
   'P_edge':{'definition':'number of occupied-to-empty nearest-neighbor directed cut edges','exact_integer':True},
   'A2':{'definition':'((Mxx-Myy)^2+4*Mxy^2)/trace(M)^2; exact rational via scaled axial centered coordinates','zero_means':'second-moment isotropy'},
   'boundary_squared_radius_dispersion':{'definition':'CV^2 of q_i=Q(N*b_i-S)/N^2 over occupied boundary sites; exact rational; 0 if all q_i=0'},
   'six_direction_boundary_imbalance':{'definition':'6*sum_k c_k^2/(sum_k c_k)^2 - 1 for exposed-edge direction counts c_k; exact rational'}
 },
 'objective_separation':{'G_and_P_edge_kept_separate':True,'diagnostics_do_not_select_moves':True,'weighted_combination_allowed_in_generation':False},
 'tie_breaks':[
   {'id':'T0_CANONICAL_MIN','primary':True,'rule':'Among equal-best-G candidate states choose lexicographically smallest translation+D6 canonical state encoding; then smallest canonicalized (u,v) move key.'},
   {'id':'T1_CANONICAL_MAX','primary':False,'rule':'Among equal-best-G candidate states choose lexicographically largest translation+D6 canonical state encoding; then largest canonicalized (u,v) move key.'},
   {'id':'T2_ORIENTATION_MOVE_LEX','primary':False,'rule':'Among equal-best-G moves choose lexicographically smallest (u,v) after translation-normalizing the current orientation only; candidate canonical shape is not used for the first tie.'}
 ],
 'forbidden_move_score_inputs':['external circle comparison','teacher center','radius/circumference target','classical pi','tangent target','P_edge','A2','boundary radial dispersion','directional imbalance']
}
initial={
 'schema':'R055_INITIAL_STATE_REGISTRY_V1','generation':'R055-G0','status':'FROZEN_BEFORE_CONSTRUCTION_TRAJECTORIES',
 'N_regimes':{'construction':construction,'strict_holdout':holdout},
 'common_requirements':['exactly N occupied lattice sites','connected','hole-free','no external circle/disk cut','no teacher center'],
 'families':[
   {'id':'HEX_SHELL_GROWTH','instances':['default'],'algorithm':'Start at (0,0). Add complete graph-distance shells d=max(|a|,|b|,|a+b|) in increasing d. Within each shell use the fixed six-side ring walk starting at (d,0) and directions [(0,1),(-1,1),(-1,0),(0,-1),(1,-1),(1,0)], truncating after N sites.'},
   {'id':'ELONGATED_STRIP','instances':['default'],'algorithm':'{(a,0): a=0,...,N-1}.'},
   {'id':'SIX_ARM_STAR','instances':['default'],'algorithm':'Start at origin; cyclically extend the six rays in neighbor-direction order [(1,0),(0,1),(-1,1),(-1,0),(0,-1),(1,-1)], one new site per ray per cycle until N sites.'},
   {'id':'L_SHAPE_OR_WEDGE','instances':['default'],'algorithm':'Let h=ceil((N+1)/2). Occupy (a,0) for a=0..h-1, then occupy (0,b) for b=1..N-h. This gives exactly N sites and a one-cell-thick L/wedge.'},
   {'id':'EDEN_SEEDED','instances':['seed_550001','seed_550021','seed_550057'],'prng':'SplitMix64, unsigned 64-bit arithmetic','seed_rule':'state0=(base_seed XOR (N*0x9E3779B97F4A7C15)) mod 2^64','algorithm':'Start at origin. At each step form sorted exterior frontier in lexicographic axial order; draw next SplitMix64 output; choose index output mod frontier_size; add that site. Repeat to N.','base_seeds':[550001,550021,550057]},
   {'id':'COMPACT_BFS_ALT_TIE','instances':['default'],'algorithm':'Start at origin. Repeatedly add the frontier site maximizing its number of occupied nearest neighbors; ties choose smallest tuple (graph_distance_from_origin,b,a), using graph distance max(|a|,|b|,|a+b|).'}
 ],
 'expected_instance_count_per_N':8,
 'orientation':'generators use their declared axial orientation; shape-class comparisons canonicalize by translation+D6 only after generation',
 'holdout_rule':'same frozen generators and seeds are applied without modification after theorem/counterexample ledger freeze'
}

dump('R055_RELAXATION_PROTOCOL.json',protocol)
dump('R055_MOVE_ENERGY_REGISTRY.json',energy)
dump('R055_INITIAL_STATE_REGISTRY.json',initial)
