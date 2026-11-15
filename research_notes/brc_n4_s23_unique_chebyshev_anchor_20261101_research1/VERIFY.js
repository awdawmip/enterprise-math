"use strict";
// Exact integer verification for the frozen six-source S23 model.
// Controls are integers in units of 1/24. This checker evaluates only
// the displayed rational anchors and all {0,1} box vertices.
// Universal real-domain claims are proved in PROOF.md, not by sampling.
const assert = (x, msg) => { if (!x) throw Error(msg); };
const D=24, SCALE=480;
const A=[0,0,0,1,1,1], B=[2,2,3,2,2,4], C=[5,6,7,8,9,10];
const M=[[10,10,0,0,0,0],[9,11,0,0,0,0],[0,0,20,0,0,0],
         [0,0,0,10,10,0],[0,0,0,2,18,0],[0,0,0,0,0,20]];
function law(a,b,c) {
  const n2=(D-a)*b, n3=(D-a)*(D-b)*c;
  assert(n2%D===0 && n3%(D*D)===0,"not an integer /24 stop law");
  const p=[a,n2/D,n3/(D*D)];
  p.push(D-p[0]-p[1]-p[2]);
  assert(p.every(x=>Number.isInteger(x)&&x>=0) && p.reduce((a,b)=>a+b,0)===D,"bad law");
  return p;
}
function prepared(theta) {
  const src=A.map((a,x)=>law(theta[a],theta[B[x]],theta[C[x]]));
  return M.map(row=>{
    const p=Array.from({length:4},(_,t)=>row.reduce((s,w,x)=>s+w*src[x][t],0));
    assert(p.reduce((a,b)=>a+b,0)===SCALE,"bad mixed row");
    return p;
  });
}
function tvN(p,q) {
  const positive=p.reduce((s,x,j)=>s+Math.max(0,x-q[j]),0);
  const negative=p.reduce((s,x,j)=>s+Math.max(0,q[j]-x),0);
  assert(positive===negative,"TV mismatch");
  return positive; // TV = tvN/480, exact.
}
function rowDistances(p,q) { return p.map((row,i)=>tvN(row,q[i])); }
function boxVertices(indices) {
  return Array.from({length:2**indices.length},(_,mask)=>{
    const theta=Array(11).fill(0);
    indices.forEach((i,k)=>{theta[i]=((mask>>k)&1)?D:0;});
    return theta;
  });
}
function maximaAtVertices(indices,anchor) {
  const q=prepared(anchor), maxima=Array(6).fill(0);
  for(const theta of boxVertices(indices)) {
    rowDistances(prepared(theta),q).forEach((v,i)=>{maxima[i]=Math.max(maxima[i],v);});
  }
  return maxima;
}
const fullCentre=[6,6,8,8,8,12,12,12,12,12,12]; // 1/4,1/4,1/3,1/3,1/3; six 1/2
const fullMid=Array(11).fill(12);
const faceCentre=[8,0,12,0,0,0,0,0,0,0,0]; // a_A=1/3, b_U=1/2, all others 0
const faceMid=[12,0,12,0,0,0,0,0,0,0,0];
const expectedUniform=Array.from({length:6},()=>[120,120,120,120]);
assert(JSON.stringify(prepared(fullCentre))===JSON.stringify(expectedUniform),"centre not uniform");
assert(prepared(fullMid).every(p=>JSON.stringify(p)===JSON.stringify([240,120,60,60])),"mid law");
const fullBestRows=maximaAtVertices([...Array(11).keys()],fullCentre);
const fullMidRows=maximaAtVertices([...Array(11).keys()],fullMid);
const faceBestRows=maximaAtVertices([0,2],faceCentre);
const faceMidRows=maximaAtVertices([0,2],faceMid);
assert(JSON.stringify(fullBestRows)===JSON.stringify([360,360,360,360,360,360]),"full best rows");
assert(JSON.stringify(fullMidRows)===JSON.stringify([420,420,420,420,420,420]),"full mid rows");
assert(JSON.stringify(faceBestRows)===JSON.stringify([320,320,320,240,240,0]),"face best rows");
assert(JSON.stringify(faceMidRows)===JSON.stringify([360,360,240,240,240,0]),"face mid rows");
// The four all-source atoms are feasible, so no arbitrary free centre can
// beat 3/4 in the full box. On the face row 0 has three feasible atoms.
function globalAtom(j) {
  const v=Array(11).fill(0);
  if(j===0){v[0]=D;v[1]=D;}
  if(j===1){v[2]=D;v[3]=D;v[4]=D;}
  if(j===2){for(let k=5;k<11;k++)v[k]=D;}
  return v;
}
for(let j=0;j<4;j++) {
  const atom=Array.from({length:4},(_,t)=>t===j?SCALE:0);
  assert(prepared(globalAtom(j)).every(p=>JSON.stringify(p)===JSON.stringify(atom)),
         "missing global atom "+j);
}
const faceAtoms=[[24,0],[0,24],[0,0]];
for(const [s,t] of faceAtoms){
  const v=Array(11).fill(0);v[0]=s;v[2]=t;
  const q=prepared(v)[0];
  assert(q.filter(x=>x===SCALE).length===1,"missing face atom");
}
const result={
  status:"PASS_BRC_N4_S23_UNIQUE_CHEBYSHEV_ANCHORS_20261101",
  arithmetic:"integer_exact_prepared_laws_denominator_480",
  checked_full_vertices:2048, checked_face_vertices:4,
  full_optimal_policy_anchor:"(1/4,1/4,1/3,1/3,1/3;1/2^6)",
  full_centre_row_maxima_over_480:fullBestRows,
  full_naive_midpoint_row_maxima_over_480:fullMidRows,
  face_optimal_policy_anchor:"a_A=1/3,b_U=1/2;others=0",
  face_centre_row_maxima_over_480:faceBestRows,
  face_naive_midpoint_row_maxima_over_480:faceMidRows,
  full_exact_radii:["3/4","7/8"],
  face_exact_radii:["2/3","3/4"],
  lower_bound_atom_tests:"4 global, 3 face",
  real_domain_proof:"analytic in PROOF.md; vertex tests validate rational formulas only"
};
if(typeof console!=="undefined") console.log(JSON.stringify(result,null,2));
result;
