#!/usr/bin/env node
"use strict";
// X6 R106: exact integer certificate for the analytically complete moment box.
// Proof of the infinite-lattice and four-weight claims is in the companion MD.
function verify(){
  const den=[10,67,50,59,42,99];
  const gcd=(a,b)=>b?gcd(b,a%b):a,lcm=(a,b)=>a/gcd(a,b)*b,L=den.reduce(lcm,1);
  const q=([x,y,z])=>Math.max([x,y,z].reduce((s,t)=>s+Math.max(0,t),0),[x,y,z].reduce((s,t)=>s+Math.max(0,-t),0));
  const mom=([x,y,z])=>[x+3*y+6*z,3*x+12*y+30*z,7*x+39*y+126*z];
  const scoreN=a=>{const [u,v,h]=mom(a);return Math.max(...[u,v,h,v-u,h-u,h-v].map((t,i)=>Math.abs(t)*(L/den[i])));};
  let oriented=0; const rows=[];
  for(let u=-1;u<=1;u++)for(let v=-10;v<=10;v++)for(let h=-7;h<=7;h++){
    if(v%3||(h-u)%6||(h-u-6*v)%12)continue;
    const x=(h+19*u-8*v)/2,y=(-h-14*u+7*v)/3,z=(h+11*u-6*v)/12;
    if(!Number.isInteger(x)||!Number.isInteger(y)||!Number.isInteger(z))throw Error("moment inverse failed");
    if(x===0&&y===0&&z===0)continue;
    oriented++;
    if(x>0||(x===0&&(y>0||(y===0&&z>0))))rows.push({a:[x,y,z],q:q([x,y,z]),score_n:scoreN([x,y,z])});
  }
  rows.sort((a,b)=>a.q-b.q);
  const expected=[
    [[1,0,0],1,1,7],[[5,-4,1],6,1,7],[[9,-5,1],10,1,7],
    [[10,-5,1],11,1,10],[[14,-9,2],16,1,10],[[15,-9,2],17,1,7],
    [[19,-10,2],21,1,7],[[23,-14,3],26,1,7],
    [[24,-14,3],27,6,59],[[25,-14,3],28,1,7],
    [[29,-18,4],33,1,7],[[33,-19,4],37,9,59],
    [[34,-19,4],38,7,59],[[39,-23,5],44,9,59],
    [[43,-24,5],48,10,59],[[49,-28,6],55,10,59]
  ];
  if(oriented!==32||rows.length!==16)throw Error("candidate count mismatch");
  expected.forEach(([a,qv,n,d],i)=>{const r=rows[i];if(JSON.stringify(r.a)!==JSON.stringify(a)||r.q!==qv||r.score_n*d!==n*L)throw Error("score mismatch row "+i);});
  const strict=rows.filter(r=>20*r.score_n<3*L),gap=rows.filter(r=>59*r.score_n<=9*L);
  if(strict.length!==12||gap.length!==14)throw Error("near count mismatch");
  if(!(2*90*62>3*59*63&&2*10*63<3*7*62))throw Error("cube separation inequality");
  return {
    schema:"X6_R106_ROBUST_TWELVE_CHAMBER_EXACT_V1",
    conditional_model:"positive four-weight six-pair BRC star-gap observer",
    weights:[9,1,58,41],port_domain:"integer p>=11",
    observer_denominators:den,score_common_denominator:L,
    moment_box:{u:[-1,1],v:[-10,10],h:[-7,7],integer_triples:945},
    congruent_nonzero_oriented:oriented,unoriented_moment_candidates:rows.length,
    near_strict_three_halves:strict.length,
    directions_at_or_below_nine_over_fiftynine:gap.length,
    strict_q_thresholds:strict.map(r=>r.q).sort((a,b)=>a-b),
    count_13th_and_14th_score:"9/59 (for p>=44)",saturated_16th_score:"10/59 (for p>=55)",
    certified_one_parameter_family:"w=(9,1,C,41), 157/3<C<59",
    certified_four_weight_cube:"|w_i-(9,1,58,41)_i|<=1/25 for each i",
    ratio_inside_upper:"315/217 < 3/2",
    ratio_outside_lower:"5580/3717 > 3/2",
    rows,assertions:"PASS",
    coverage:"All 945 moment triples in the proven complete F<=9/59 box; global minimum and uniform four-weight cube from exact analytic inequalities"
  };
}
console.log(JSON.stringify(verify(),null,2));
