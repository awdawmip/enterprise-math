// X6 R35. Exact finite labelled-language verifier, Node.js 18+.
// No floating point, no external dependencies. Q0 and Q1 are conditional event labels.
function verifyR35() {
  const labels = ["Q0", "Q1"];
  const initial = [0, 0, 1]; // used0, used1, public Link x1
  const step = (theta, state, label, feedback) => {
    const [used0, used1, x1] = state;
    if (label === "Q0") {
      if (used0 || (theta & 1) === 0) return null;
      return [1, used1, feedback === "RESET" ? 0 : x1];
    }
    if (used1 || (((theta >> 1) & 1) === 0 && x1 === 0)) return null;
    return [used0, 1, x1];
  };
  const words = (theta, state, feedback) => {
    const out = [""];
    function dfs(st, prefix) {
      for (const a of labels) {
        const next = step(theta, st, a, feedback);
        if (next !== null) {
          const w = prefix + a + ";";
          out.push(w);
          dfs(next, w);
        }
      }
    }
    dfs(state, "");
    return out.sort();
  };
  const horizon = (w, h) => w.filter(v => v === "" || v.split(";").length - 1 <= h).join("|");
  const models = {};
  for (const feedback of ["RESET", "INERT"]) {
    const initLanguages = [];
    const reachable = new Map();
    for (let theta = 0; theta < 4; theta++) {
      initLanguages.push(words(theta, initial, feedback));
      const queue = [initial];
      const visited = new Set([initial.join(",")]);
      while (queue.length > 0) {
        const s = queue.shift();
        reachable.set(theta + ":" + s.join(","), words(theta, s, feedback).join("|"));
        for (const label of labels) {
          const next = step(theta, s, label, feedback);
          if (next !== null && !visited.has(next.join(","))) {
            visited.add(next.join(","));
            queue.push(next);
          }
        }
      }
    }
    models[feedback] = {
      initial_languages: initLanguages,
      initial_language_classes_by_depth: [0, 1, 2].map(h => new Set(initLanguages.map(w => horizon(w, h))).size),
      reachable_decorated_states: reachable.size,
      global_markov_language_classes: new Set(reachable.values()).size
    };
  }
  const sameFirstStep = [0,1,2,3].every(t => horizon(models.RESET.initial_languages[t],1) === horizon(models.INERT.initial_languages[t],1));
  const aWitness = models.RESET.initial_languages[3].includes("Q0;Q1;") && !models.RESET.initial_languages[1].includes("Q0;Q1;");
  const bConceals = models.INERT.initial_languages[3].join("|") === models.INERT.initial_languages[1].join("|");
  const assertions = {
    identical_initial_one_step_success_languages: sameFirstStep,
    reset_initial_class_counts: JSON.stringify(models.RESET.initial_language_classes_by_depth) === "[1,2,3]",
    inert_initial_class_counts: JSON.stringify(models.INERT.initial_language_classes_by_depth) === "[1,2,2]",
    reset_global_classes: models.RESET.global_markov_language_classes === 5 && models.RESET.reachable_decorated_states === 12,
    inert_global_classes: models.INERT.global_markov_language_classes === 4 && models.INERT.reachable_decorated_states === 12,
    distinguishing_Q0Q1_for_theta_01_vs_11_only_in_reset: aWitness && bConceals
  };
  if (!Object.values(assertions).every(Boolean)) throw new Error("R35 exact verifier failure: "+JSON.stringify(assertions));
  return {
    schema: "X6_R35_TWO_DYNAMIC_COMPLETIONS_EXACT_LANGUAGE_CHECK_V1",
    frozen_input: "p000_reality_foundation.json@a72226e2430ffa4786321ac86e7f0c599d5f0389",
    source_model: "R33/R34 two-source one-use probe family",
    observer: "full ordered named successful event words",
    labels, histories: [0,1,2,3], models, assertions, pass: true,
    scope: "exhaustive four hidden histories, all reachable phases, finite word languages length <=2; symbolic P000 compatibility is conditional, not native admission"
  };
}
if (typeof require !== "undefined" && require.main === module) {
  process.stdout.write(JSON.stringify(verifyR35(), null, 2) + "\n");
}
