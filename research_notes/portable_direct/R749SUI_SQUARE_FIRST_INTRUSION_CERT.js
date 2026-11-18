"use strict";
/* R749SUI exact integer regression certificate; Node.js standard JavaScript, no dependencies.
 * Domain 4 <= t <= 15, M=t*t-1. Enumerate all ordered, labeled positive
 * integers a,u,v,d <= M satisfying ad-uv=1. Never quotient Port orientation.
 * Number arithmetic is exact: all products involved are < 2^53.
 */
function verifyR749SUI() {
  const rows = [];
  let checkedMatrices = 0, checkedNoncanonical = 0;
  for (let t = 4; t <= 15; t++) {
    const M = t*t-1, W = M*(M-t)*(M-t), winners = [];
    let best = -1;
    for (let a = 1; a <= M; a++) for (let d = 1; d <= M; d++) {
      const prod = a*d-1;
      if (prod < 1) continue;
      for (let u = 1; u <= M; u++) {
        if (prod%u !== 0) continue;
        const v = prod/u;
        if (v < 1 || v > M) continue;
        checkedMatrices++;
        const canonical = a===d && Math.max(u,v)===a+1 &&
                                    Math.min(u,v)===a-1;
        if (canonical) continue;
        checkedNoncanonical++;
        const tau = Math.max(u,v)*a*d;
        if (tau>best) {
          best=tau; winners.length=0; winners.push([a,u,v,d]);
        } else if (tau===best) winners.push([a,u,v,d]);
      }
    }
    let J=0;
    for (let j=1; j<=M-2; j++)
      if ((M-j+1)*(M-j)*(M-j)>W) J++;
    const a=M-t, v=t*(t-2);
    const expected=[[a,M,v,a],[a,v,M,a]];
    const exactWinners = winners.length===2 &&
      expected.every(e=>winners.some(w=>w.every((x,i)=>x===e[i])));
    const expectedJ=Math.floor((2*t+1)/3);
    if(best!==W || !exactWinners || J!==expectedJ)
      throw new Error("R749SUI_FAIL t="+t+" "+JSON.stringify({best,W,winners,J,expectedJ}));
    rows.push({t,M,threshold:W,first_intrusion_rank:J+1,canonical_before:J,
               winner_multiplicity:winners.length});
  }
  return {result:"PASS",
          domain:"4<=t<=15, M=t^2-1, all labeled 1<=a,u,v,d<=M with ad-uv=1",
          checked_matrices:checkedMatrices,
          noncanonical_checked:checkedNoncanonical,rows};
}
if (typeof module !== "undefined" && require.main===module)
  console.log(JSON.stringify(verifyR749SUI(),null,2));
module.exports={verifyR749SUI};
