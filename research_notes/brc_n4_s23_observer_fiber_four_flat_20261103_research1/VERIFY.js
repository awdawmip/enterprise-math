// Exact six-source BRC S23 observer-fiber certificate (2026-11-03).
// Usage: node VERIFY.js > RUN_EVIDENCE.json
const verify = function verify(){
 const gcd=(a,b)=>{a=a<0n?-a:a;b=b<0n?-b:b;while(b){let t=a%b;a=b;b=t;}return a||1n;};
 const Q=(a,b=1n)=>{a=BigInt(a);b=BigInt(b);if(b<0n){a=-a;b=-b;}if(!b)throw Error("zero denominator");const g=gcd(a,b);return[a/g,b/g]};
 const add=(a,b)=>Q(a[0]*b[1]+b[0]*a[1],a[1]*b[1]);
 const neg=a=>Q(-a[0],a[1]);
 const sub=(a,b)=>add(a,neg(b));
 const mul=(a,b)=>Q(a[0]*b[0],a[1]*b[1]);
 const div=(a,b)=>Q(a[0]*b[1],a[1]*b[0]);
 const eq=(a,b)=>a[0]===b[0]&&a[1]===b[1];
 const one=Q(1),zero=Q(0);
 const repr=a=>a[1]===1n?String(a[0]):String(a[0])+"/"+String(a[1]);
 const A=[0,0,0,1,1,1],B=[2,2,3,2,2,4],C=[5,6,7,8,9,10];
 const M=[[10,10,0,0,0,0],[9,11,0,0,0,0],[0,0,20,0,0,0],[0,0,0,10,10,0],[0,0,0,2,18,0],[0,0,0,0,0,20]];
 const source=(a,b,c)=>[a,mul(sub(one,a),b),mul(mul(sub(one,a),sub(one,b)),c),mul(mul(sub(one,a),sub(one,b)),sub(one,c))];
 const raws=z=>A.map((_,i)=>source(z[A[i]],z[B[i]],z[C[i]]));
 const observe=z=>{const R=raws(z);return M.map(row=>[0,1,2,3].map(k=>row.reduce((s,m,j)=>add(s,mul(Q(m,20),R[j][k])),zero)))};
 const fam=(x,cs)=>[x,Q(5,6),one,Q(1,2),Q(1,2),cs[0],cs[1],one,cs[2],cs[3],Q(1,3)];
 const corner = bits=>bits.map(v=>Q(v));
 const equalMat=(p,r)=>p.every((row,i)=>row.every((v,k)=>eq(v,r[i][k])));
 const base=observe(fam(Q(1,3),[Q(1,3),Q(1,2),Q(1,2),Q(1,3)]));
 let tested=0;
 for (const x of [Q(0),Q(1,3),Q(1,2),Q(1)]){
  const std=observe(fam(x,[Q(1,3),Q(1,2),Q(1,2),Q(1,3)]));
  for(let bits=0;bits<16;bits++){
   const vals=[0,1,2,3].map(i=>Q((bits>>i)&1));
   if(!equalMat(std,observe(fam(x,vals))))throw Error("fiber mismatch "+bits);
   tested++;
  }
 }
 const p=base;
 const lin=(u,i,v,j,den=1)=>[0,1,2,3].map(k=>div(sub(mul(Q(u),p[i][k]),mul(Q(v),p[j][k])),Q(den)));
 const recovered=[lin(11,0,10,1),lin(10,1,9,0),p[2],lin(9,3,5,4,4),lin(5,4,1,3,4),p[5]];
 if(!equalMat(recovered,raws(fam(Q(1,3),corner([0,1,0,1])))))throw Error("inverse mixing mismatch");
 const a0=recovered[0][0],a1=recovered[3][0];
 const z2=div(recovered[0][1],sub(one,a0));
 const z3=div(recovered[2][1],sub(one,a0));
 const z4=div(recovered[5][1],sub(one,a1));
 const z7=div(recovered[2][2],mul(sub(one,a0),sub(one,z3)));
 const z10=div(recovered[5][2],mul(sub(one,a1),sub(one,z4)));
 const visible=[a0,a1,z2,z3,z4,z7,z10], expected=[Q(1,3),Q(5,6),one,Q(1,2),Q(1,2),one,Q(1,3)];
 if(!visible.every((v,i)=>eq(v,expected[i])))throw Error("visible-coordinate recovery failure");
 const expectedP=[[Q(1,3),Q(2,3),zero,zero],[Q(1,3),Q(2,3),zero,zero],[Q(1,3),Q(1,3),Q(1,3),zero],[Q(5,6),Q(1,6),zero,zero],[Q(5,6),Q(1,6),zero,zero],[Q(5,6),Q(1,12),Q(1,36),Q(1,18)]];
 if(!equalMat(base,expectedP))throw Error("expected source matrix mismatch");
 return {
  marker:"PASS_BRC_S23_EXACT_OBSERVER_FIBER_20261103",
  source_model:"six separately indexed causal source preparations, M/20",
  frozen_science:"43ec6098b1330ae86d0a7863be336c5d97f6ef34",
  inherited_prior_witness_commit:"1c383a8b7f5d578bd406bb519668c61ac6df0242",
  source_mixing_determinant:"1/50",
  number_of_exact_corner_equalities:tested,
  parameter_x_tests:["0","1/3","1/2","1"],
  free_coordinates:["z5","z6","z8","z9"],
  identifiable_coordinates:["z0","z1","z2","z3","z4","z7","z10"],
  observed_matrix_at_witness:base.map(row=>row.map(repr)),
  recovered_identifiable_values:visible.map(repr),
  inherited_ten_decoder_risk_vector:["1","1","1","2/3","31/36","2/3","2/3","2/3","1","43/60"],
  arithmetic:"exact normalized BigInt rational; no floating point predicates",
  claim_scope:"exact observation fiber and any fixed decoder-risk bank based solely on the observed six-source distributions",
  prior_risk_vector_recomputed_this_run:false,
  theorem_checked_with_all_real_parameters_by:"symbolic zero-factor and inverse formula proof in PROOF.md; 64 tests are independent exact implementation checks"
 };
};
console.log(JSON.stringify(verify(), null, 2));
