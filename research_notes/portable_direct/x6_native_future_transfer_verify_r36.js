// X6 R36 exact finite partial-labelled-system certificate, Node.js 18+.
// All arithmetic is finite exact; two named events Q0/Q1; no external libraries.
function verifyR36() {
  "use strict";
  const alphabet = ["Q0", "Q1"];
  const models = [];
  for (const n of [1, 2]) {
    const base = n + 1, total = base ** (2 * n);
    for (let k = 0; k < total; k++) {
      let x = k;
      const rows = [];
      for (let p = 0; p < n; p++) {
        const row = [];
        for (let a = 0; a < 2; a++) {
          row.push((x % base) - 1);
          x = Math.floor(x / base);
        }
        rows.push(row);
      }
      models.push({n, rows});
    }
  }
  const signatures = models.map(m => {
    const levels = [Array(m.n).fill("epsilon")];
    for (let h = 1; h <= 4; h++) {
      const prior = levels[h - 1];
      levels.push(m.rows.map(row => JSON.stringify(row.map(v => v === -1 ? null : prior[v]))));
    }
    return levels;
  });
  function shortest(a, p, b, q) {
    const queue = [[p, q, []]];
    const visited = new Set([p + ":" + q]);
    for (let i = 0; i < queue.length; i++) {
      const [u, v, word] = queue[i];
      for (let j = 0; j < 2; j++) {
        const x = a.rows[u][j], y = b.rows[v][j];
        if ((x === -1) !== (y === -1)) return word.concat(j);
        if (x !== -1) {
          const key = x + ":" + y;
          if (!visited.has(key)) {
            visited.add(key);
            queue.push([x, y, word.concat(j)]);
          }
        }
      }
    }
    return null;
  }
  const distribution = {"equivalent": 0, "1": 0, "2": 0, "3": 0, "4": 0};
  let testedPairs = 0, maxDepth = 0, sampleMax = null;
  for (let ai = 0; ai < models.length; ai++) {
    const a = models[ai];
    for (let bi = 0; bi < models.length; bi++) {
      const b = models[bi], bound = a.n * b.n;
      for (let p = 0; p < a.n; p++) {
        for (let q = 0; q < b.n; q++) {
          testedPairs++;
          const witness = shortest(a, p, b, q);
          const d = witness === null ? null : witness.length;
          const equal = signatures[ai][bound][p] === signatures[bi][bound][q];
          if ((d === null) !== equal) throw Error("finite cutoff mismatch");
          if (d !== null) {
            if (d > bound) throw Error("distinguishing depth bound exceeded");
            for (let h = 0; h < d; h++) {
              if (signatures[ai][h][p] !== signatures[bi][h][q]) throw Error("nonshortest witness");
            }
            if (signatures[ai][d][p] === signatures[bi][d][q]) throw Error("witness not distinguishing");
            distribution[String(d)]++;
            if (d > maxDepth) {
              maxDepth = d;
              sampleMax = {left: a.rows, left_state:p, right:b.rows, right_state:q, shortest_word:witness.map(i=>alphabet[i])};
            }
          } else distribution.equivalent++;
        }
      }
    }
  }
  if (models.length !== 85 || testedPairs !== 27556 || distribution.equivalent !== 3384 ||
      distribution["1"] !== 19128 || distribution["2"] !== 4884 || distribution["3"] !== 160 ||
      distribution["4"] !== 0 || maxDepth !== 3) throw Error("exhaustive control counts changed");
  function r35words(theta,feedback) {
    const out = new Set([""]);
    function visit(u0,u1,x,w) {
      if (u0 === 0 && (theta & 1)) {
        const nw = w + "Q0;";
        out.add(nw);
        visit(1,u1,feedback === "RESET" ? 0 : x,nw);
      }
      if (u1 === 0 && (((theta >> 1) & 1) || x)) {
        const nw = w + "Q1;";
        out.add(nw);
        visit(u0,1,x,nw);
      }
    }
    visit(0,0,1,"");
    return Array.from(out).sort();
  }
  const r35 = [];
  for(let theta=0;theta<4;theta++){
    const a=r35words(theta,"RESET"),b=r35words(theta,"INERT");
    r35.push({theta,agree_through_depth_1:a.filter(s=>s.split(";").length-1<=1).join("|")===b.filter(s=>s.split(";").length-1<=1).join("|"),equal_full_future:a.join("|")===b.join("|"),different_at_Q0Q1:a.includes("Q0;Q1;")!==b.includes("Q0;Q1;")});
  }
  if(!r35.every(x=>x.agree_through_depth_1) ||
     r35.filter(x=>!x.equal_full_future).map(x=>x.theta).join(",")!=="1" ||
     !r35[1].different_at_Q0Q1) throw Error("R35 cross-model witness regression");
  const noninjective_map_example = {
    left_states:2,right_states:1,
    left_transition_rows:[[-1,-1],[-1,-1]],
    right_transition_rows:[[-1,-1]],
    valid_relation:[[0,0],[1,0]],
    both_left_states_share_single_right_state:true
  };
  return {
    schema:"X6_R36_FINITE_FUTURE_TRANSFER_EXACT_CHECK_V1",
    method:"exact deterministic partial labelled-success trace recursion and pair-BFS; no approximations",
    source_model:"P000 V5 frozen; R35 conditional triadic completions",
    alphabet, automata:models.length, alphabet_size:2, state_counts:[1,2],
    state_pair_instances:testedPairs, shortest_distinguishing_word_distribution:distribution,
    max_witness_length_observed:maxDepth, maximal_witness_example:sampleMax,
    cutoff_verified:"nA*nB (<=4 for all enumerated pairs)",
    r35_cross_model_comparison:r35,
    noninjective_bisimulation_relation_example:noninjective_map_example,
    assertions:{exhaustive_all_partial_two_label_machines_with_one_or_two_states:true,
      agreement_through_product_bound_iff_full_language_equality:true,
      pair_BFS_shortest_witness_certified:true,
      exact_R35_first_split_at_two_events:true,
      noninjective_state_mapping_allowed:true},
    pass:true, review:"NOT_INDEPENDENTLY_REVIEWED",
    scope:"finite deterministic partial systems with fully named successful-event trace observer; conditional candidate triads are not established native event admission"
  };
}
if (typeof require !== 'undefined' && require.main === module) {
  process.stdout.write(JSON.stringify(verifyR36(),null,2)+'\n');
}
