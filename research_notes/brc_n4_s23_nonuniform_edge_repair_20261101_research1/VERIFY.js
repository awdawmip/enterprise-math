"use strict";
/* Exact integer verification for the BRC N4 S23 rational nonuniform bank.
 * Mathematical domain: six latent sources, six prepared input rows, four stop times,
 * eleven independent behavioral stop controls, ten policy-selected fixed decoders.
 * All arithmetic below is integer-valued, with maxima far below 2^53.
 */
const M20 = [
  [10,10,0,0,0,0], [9,11,0,0,0,0], [0,0,20,0,0,0],
  [0,0,0,10,10,0], [0,0,0,2,18,0], [0,0,0,0,0,20]
];
const BOXES = [
  "34 24 34 24", "34 23 34 34", "34 34 34 23",
  "24 24 12 12", "12 12 24 34", "12 13 23 24",
  "23 34 12 13", "24 34 12 14", "13 12 13 13",
  "12 12 14 12"
];
const GROUP = [0,0,1,2,2,3];
const A_SLOT = [0,0,0,1,1,1];
const B_SLOT = [0,0,1,0,0,2];
function mix(f) {
  return M20.map(row => Array.from({length:4}, (_, t) =>
    row.reduce((sum, weight, x) => sum + weight * f[x][t], 0)));
}
function originalDecoders() {
  return BOXES.map(spec => {
    const pairs = spec.split(" ").map(two => [Number(two[0])-1,Number(two[1])-1]);
    return GROUP.map(g => Array.from({length:4}, (_,t) =>
      pairs[g].includes(t) ? 80 : 0));
  });
}
const Q = originalDecoders();
// Replacement label 10: AU support {1,3,4} at weights 1/2,1/4,1/4,
// AV pair {1,3}, BU pair {1,4}, BV pair {1,2}.
Q[9] = [
  [80,0,40,40], [80,0,40,40], [80,0,80,0],
  [80,0,0,80], [80,0,0,80], [80,80,0,0]
];
for (const label of Q) for (const row of label) {
  if (row.reduce((a,b)=>a+b,0)!==160) throw Error("DECODER_NOT_STOCHASTIC");
}
function labelLoss(p, label, pScale, qScale) {
  let worst=0;
  for(let i=0;i<6;i++) {
    let twice=0;
    for(let t=0;t<4;t++) twice+=Math.abs(pScale*p[i][t]-qScale*Q[label][i][t]);
    worst=Math.max(worst,twice);
  }
  return worst;
}
function score(p, pScale, qScale) {
  return Math.min(...Array.from({length:10}, (_, l)=>labelLoss(p,l,pScale,qScale)));
}
function ternaryPolicy(code) {
  const d=[];
  for(let j=0;j<11;j++) { d.push(code%3); code=Math.floor(code/3); }
  const f=[];
  for(let x=0;x<6;x++) {
    const a=d[A_SLOT[x]], b=d[2+B_SLOT[x]], c=d[5+x];
    f.push([4*a,2*(2-a)*b,(2-a)*(2-b)*c,(2-a)*(2-b)*(2-c)]);
  }
  return mix(f); // denominator 160; q numerator also denominator 160.
}
function edgePrepared(side,n,d) {
  // Each latent row below has denominator d; prepared rows have denominator 20*d.
  // H: random A first stop, A latent final split; B always first stop.
  // J: random B first stop, B latent final split; A always first stop.
  let f;
  if(side==="H") f=[
    [n,0,d-n,0],[n,0,0,d-n],[n,0,d-n,0],
    [d,0,0,0],[d,0,0,0],[d,0,0,0]
  ];
  else if(side==="J") f=[
    [d,0,0,0],[d,0,0,0],[d,0,0,0],
    [n,0,0,d-n],[n,0,d-n,0],[n,0,0,d-n]
  ];
  else throw Error("UNKNOWN_EDGE");
  return mix(f);
}
function main(){
  let equal=0, below=0, greater=0, max=0;
  for(let code=0;code<3**11;code++) {
    const val=score(ternaryPolicy(code),1,1); // exactly 320*TV
    max=Math.max(max,val);
    if(val===160) equal++;
    else if(val<160) below++;
    else greater++;
  }
  if(max!==160 || equal!==168353 || below!==8794 || greater!==0)
    throw Error("TERNARY_MISMATCH "+JSON.stringify({max,equal,below,greater}));
  let hChecked=0, jChecked=0;
  for(let n=0;n<=120;n++) {
    const d=120;
    const h=edgePrepared("H",n,d);
    // Prepared numerator 20d, decoded numerator 160: compare both at 160d.
    const hRisk=score(h,8,d);
    const h10=labelLoss(h,9,8,d);
    if(hRisk!==160*d || h10!==160*d) throw Error("H_EDGE_FAILURE "+n);
    hChecked++;
    const j=edgePrepared("J",n,d);
    const losses=Array.from({length:10},(_,l)=>labelLoss(j,l,8,d));
    const expected=[
      320*d,320*d,320*d,320*d,
      32*(9*d+n),160*(d+n),
      320*d,320*d,
      Math.max(320*(d-n),160*d),
      Math.max(320*(d-n),160*d)
    ];
    if(losses.some((v,i)=>v!==expected[i])) throw Error("J_LABEL_FAILURE n="+n+" "+losses+" vs "+expected);
    const envelope=Math.min(160*(d+n),Math.max(320*(d-n),160*d));
    if(score(j,8,d)!==envelope) throw Error("J_ENVELOPE_FAILURE n="+n);
    jChecked++;
  }
  const witness=score(edgePrepared("J",1,3),8,3);
  if(witness!==640) throw Error("J_WITNESS_FAILURE "+witness); // 640/960=2/3
  const H_witness=score(edgePrepared("H",1,3),8,3);
  if(H_witness!==480) throw Error("H_WITNESS_FAILURE "+H_witness); // 480/960=1/2
  console.log("PASS_BRC_N4_S23_RATIONAL_BANK_REPAIR_DISPLACED_ADVERSARY_20261101");
  console.log(JSON.stringify({
    grid_policies:3**11,grid_denominator_for_TV:320,
    grid_max_TV:"1/2",grid_equal_half:equal,grid_below_half:below,
    grid_above_half:greater,
    H_rational_grid_points:hChecked,H_analytic_all_real_G:"1/2",
    J_rational_grid_points:jChecked,
    J_analytic_G:"min((1+t)/2,max(1-t,1/2))",
    J_peak_t:"1/3",J_peak_TV:"2/3",
    H_at_one_third_TV:"1/2",J_at_one_third_TV:"2/3"
  },null,2));
}
if(require.main===module) main();
