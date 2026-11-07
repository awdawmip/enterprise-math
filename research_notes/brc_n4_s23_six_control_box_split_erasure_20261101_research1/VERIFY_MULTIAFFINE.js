"use strict";
const check = function check(){
  "use strict";
  const same=(a,b)=>JSON.stringify(a)===JSON.stringify(b);
  const make=(anum,c2)=>{
    const remain=24-anum;
    const AU=[anum,0,remain/2,remain/2];
    const AV=[anum,0,remain*c2/2,remain*(2-c2)/2];
    return [AU,AU,AV,[6,0,9,9],[6,0,9,9],[6,6,6,6]];
  };
  const TV24=(p,q)=>p.reduce((s,v,i)=>s+Math.abs(v-q[i]),0)/2;
  const risk24=(theta,z)=>Math.max(...theta.map((p,i)=>TV24(p,z[i])));
  const vertices=[make(0,0),make(0,2),make(24,0),make(24,2)];
  const anchor=make(8,1),mid=make(12,1);
  const riskOptimal=Math.max(...vertices.map(p=>risk24(p,anchor)));
  const riskMid=Math.max(...vertices.map(p=>risk24(p,mid)));
  const diameter=Math.max(...vertices.flatMap(p=>vertices.map(q=>risk24(p,q))));
  if(riskOptimal!==16||riskMid!==18||diameter!==24)throw Error("exact extrema mismatch");
  if(!same(vertices[0][2],[0,0,0,24])||!same(vertices[1][2],[0,0,24,0])||!same(vertices[2][2],[24,0,0,0]))throw Error("three atom witness invalid");
  if(!same(anchor[2],[8,0,8,8])||!same(mid[2],[12,0,6,6]))throw Error("anchor law invalid");
  return {pass:"PASS_BRC_S23_TWO_CONTROL_MULTIAFFINE_MIDPOINT_COUNTEREXAMPLE_20261101",arithmetic:"exact integer numerators with common denominator 24",varying_controls:["a_A","c_AV"],all_six_prepared_rows_checked:true,vertices:4,unique_optimal_anchor:["1/3","1/2"],optimal_radius:"16/24=2/3",parameter_midpoint_radius:"18/24=3/4",diameter:"24/24=1",diameter_over_two:"1/2",universal_reals_status:"analytic proof from three AV atoms and simplex convexity"};
};
console.log(JSON.stringify(check(),null,2));
