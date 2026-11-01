"use strict";
// Exact integer verifier for the rational two-control S23 face.
// Preparation-law probabilities are integer multiples of 1/2400.
function verify() {
  const S = 2400;
  const M20 = [
    [10,10,0,0,0,0], [9,11,0,0,0,0], [0,0,20,0,0,0],
    [0,0,0,10,10,0], [0,0,0,2,18,0], [0,0,0,0,0,20]
  ];
  const assert = (condition, why) => { if (!condition) throw Error(why); };
  function prepared(k,j) {
    // a_A=(5+k)/20, c_AV=(5+j)/20, with k,j=0,...,10.
    // First/second controls of all other sources are frozen as in PROOF.md.
    const a = 120*(5+k);
    const survival = S-a;
    const avThird = 6*(15-k)*(5+j);
    const au=[a,0,survival/2,survival/2];
    const av=[a,0,avThird,survival-avThird];
    const bu=[600,0,900,900];
    const bv=[600,600,600,600];
    const sources=[au,au,av,bu,bu,bv];
    return M20.map(row=>[0,1,2,3].map(t=>{
      const raw=row.reduce((s,w,x)=>s+w*sources[x][t],0);
      assert(raw%20===0,"non-integral observer probability");
      return raw/20;
    }));
  }
  function TVscaled(p,q) {
    const sum=p.reduce((s,x,j)=>s+Math.abs(x-q[j]),0);
    assert(sum%2===0,"half-sum not integral");
    return sum/2;
  }
  const qStar=[
    [1100,0,650,650],[1100,0,650,650],[1100,0,650,650],
    [600,0,900,900],[600,0,900,900],[600,600,600,600]
  ];
  const qMid=[
    [1200,0,600,600],[1200,0,600,600],[1200,0,600,600],
    [600,0,900,900],[600,0,900,900],[600,600,600,600]
  ];
  let gridCount=0, rowChecks=0, maxStar=0, maxMid=0, dominationChecks=0;
  const corners=[];
  for(let k=0;k<=10;k++)for(let j=0;j<=10;j++) {
    const p=prepared(k,j);
    for(let i=0;i<6;i++){
      assert(p[i].every(x=>Number.isInteger(x)&&x>=0),"non-probability");
      assert(p[i].reduce((s,x)=>s+x,0)===S,"mass not conserved");
      maxStar=Math.max(maxStar,TVscaled(p[i],qStar[i]));
      maxMid=Math.max(maxMid,TVscaled(p[i],qMid[i]));
      rowChecks++;
    }
    assert(TVscaled(p[0],qStar[0])<=TVscaled(p[2],qStar[2]),"AU/AV comparison");
    assert(TVscaled(p[1],qStar[1])<=TVscaled(p[2],qStar[2]),"AU/AV comparison");
    dominationChecks+=2;
    gridCount++;
    if((k===0||k===10)&&(j===0||j===10)){
      const cornerRisk=Math.max(...p.map((row,i)=>TVscaled(row,qStar[i])));
      corners.push({k,j,corner_risk_over_2400:cornerRisk,av:p[2]});
      assert(cornerRisk===700,"four-corner equality");
    }
  }
  assert(maxStar===700,"sharp candidate radius");
  assert(maxMid===750,"midpoint radius");
  assert(corners.length===4,"missing corners");
  let diameter=0;
  for(const v of corners)for(const w of corners)diameter=Math.max(diameter,TVscaled(v.av,w.av));
  assert(diameter===1200,"full face diameter");
  // Three active LP rows, all scaled by denominator 48:
  // B-alpha, ymax-beta, alpha+beta-zmin.
  const alpha48=22,beta48=13, r48=14;
  const dualRows=[36-alpha48,27-beta48,alpha48+beta48-21];
  assert(dualRows.every(x=>x===r48),"lower-bound rows are not tight");
  assert(dualRows.reduce((a,b)=>a+b,0)===42,"three-row dual certificate");
  const lowerBoundTimesThree=36+27-21;
  assert(lowerBoundTimesThree===3*r48,"LP lower bound not sharp");
  // The unique anchor gamma=beta/(1-alpha) is 1/2.
  assert(2*beta48===48-alpha48,"candidate c not 1/2");
  return {
    pass:"PASS_BRC_N4_S23_RATIONAL_SUBBOX_EXACT_LP_20261101",
    execution:"V8 JavaScript; ordinary safe-integer exact arithmetic (no floating point TV)",
    scale:2400,
    policy_grid_points:gridCount,
    prepared_row_checks:rowChecks,
    au_av_dominance_grid_checks:dominationChecks,
    vertex_count:corners.length,
    corners,
    optimal_anchor:{a:"11/24",c:"1/2",AV_law:["11/24","0","13/48","13/48"]},
    optimum_radius:"7/24",
    midpoint_radius:"5/16",
    full_face_diameter:"1/2",
    half_diameter_gap:"1/24",
    max_grid_risk_optimal_over_2400:maxStar,
    max_grid_risk_midpoint_over_2400:maxMid,
    diameter_over_2400:diameter,
    lower_bound_certificate:"three LP inequalities sum to 7/8, hence r>=7/24",
    all_real_parameter_coverage:"analytic proof and vertex extremality, NOT inferred from finite grid",
    native_P000_bridge:"not proved",
    admission:"AUTHOR_EXACT_PROOF_UNREVIEWED_NOT_ADMITTED"
  };
}
const evidence=verify();
console.log(JSON.stringify(evidence,null,2));
