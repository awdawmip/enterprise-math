"use strict";
// Exact rational verification, JavaScript BigInt only. Run via new Function(source)().
function gcd(a,b){a=a<0n?-a:a;b=b<0n?-b:b;while(b){let z=a%b;a=b;b=z;}return a;}
function q(n,d=1n){n=BigInt(n);d=BigInt(d);if(d===0n)throw Error("zero denominator");
 if(d<0n){n=-n;d=-d;}let g=gcd(n,d);return [n/g,d/g];}
function parse(s){let a=String(s).split("/");return q(a[0],a.length===1?1:a[1]);}
function add(x,y){return q(x[0]*y[1]+y[0]*x[1],x[1]*y[1]);}
function neg(x){return [-x[0],x[1]];}
function sub(x,y){return add(x,neg(y));}
function mul(x,y){return q(x[0]*y[0],x[1]*y[1]);}
function div(x,y){return q(x[0]*y[1],x[1]*y[0]);}
function ab(x){return x[0]<0n?neg(x):x;}
function cmp(x,y){let z=x[0]*y[1]-y[0]*x[1];return z<0n?-1:z>0n?1:0;}
function eq(x,y){return cmp(x,y)===0;}
function le(x,y){return cmp(x,y)<=0;}
function max(x,y){return cmp(x,y)>=0?x:y;}
function show(x){return x[1]===1n?String(x[0]):String(x[0])+"/"+String(x[1]);}
function must(ok,msg){if(!ok)throw Error("FAIL: "+msg);}
const ZERO=q(0),ONE=q(1),HALF=q(1,2);
function stop(a,b,c){let s=sub(ONE,a),t=mul(s,sub(ONE,b));
 return [a,mul(s,b),mul(t,c),mul(t,sub(ONE,c))];}
const mixing=[[10,10,0,0,0,0],[9,11,0,0,0,0],[0,0,20,0,0,0],
 [0,0,0,10,10,0],[0,0,0,2,18,0],[0,0,0,0,0,20]];
function prepared(a,b,c){
 let raw=[stop(a,b,HALF),stop(a,b,HALF),stop(a,ZERO,c),
 stop(q(1,4),b,HALF),stop(q(1,4),b,HALF),stop(q(1,4),q(1,3),HALF)];
 let out=mixing.map(row=>[0,1,2,3].map(t=>
 row.reduce((acc,w,j)=>add(acc,mul(q(w,20),raw[j][t])),ZERO)));
 for(let row of out)must(eq(row.reduce(add,ZERO),ONE),"probability normalization");
 return out;
}
function tv(p,r){return div(p.reduce((s,x,j)=>add(s,ab(sub(x,r[j]))),ZERO),q(2));}
function distance(P,R){return P.reduce((s,row,i)=>max(s,tv(row,R[i])),ZERO);}
function combine(cases){return [0,1,2,3,4,5].map(i=>
 [0,1,2,3].map(t=>cases.reduce((s,entry)=>add(s,mul(entry[0],entry[1][i][t])),ZERO)));}
const base=[[q(1,2),q(7,8)],[q(1,8),q(1,2)],[q(1,2),q(7,8)]];
const bits=[ZERO,ONE],mid=[ZERO,HALF,ONE];
function pos(box,ts){return box.map(([l,h],j)=>add(l,mul(sub(h,l),ts[j])));}
function values(box,ts){let v=pos(box,ts);return prepared(v[0],v[1],v[2]);}
const cornerParams=[];
for(let a of bits)for(let b of bits)for(let c of bits)cornerParams.push([a,b,c]);
const centerParams=[[ZERO,ZERO,ONE],[ZERO,ONE,ZERO],[ONE,ZERO,ONE],[ONE,ONE,ZERO]];
const weights=[q(4,9),q(1,18),q(2,9),q(5,18)];
must(eq(weights.reduce(add,ZERO),ONE),"joint hull weights");
function hullWitness(box){return combine(centerParams.map((t,i)=>[weights[i],values(box,t)]));}
const witness=hullWitness(base);
const expected=[
 ["11/16","1/16","1/8","1/8"],["11/16","1/16","1/8","1/8"],
 ["11/16","0","1/4","1/16"],["1/4","3/16","9/32","9/32"],
 ["1/4","3/16","9/32","9/32"],["1/4","1/4","1/4","1/4"]];
for(let i=0;i<6;i++)for(let t=0;t<4;t++)
 must(eq(witness[i][t],parse(expected[i][t])),"prior exact joint hull witness "+i+","+t);
const hullUpper=q(3,16);
let baseMax=ZERO;
for(let t of cornerParams)baseMax=max(baseMax,distance(values(base,t),witness));
must(eq(baseMax,hullUpper),"base hull radius witness all 8 vertices");
const threshold=q(31,160);
const polynomial=add(add(mul(q(32),mul(threshold,threshold)),mul(q(40),threshold)),q(-9));
must(eq(polynomial,q(-39,800)),"lawful lower discriminant at 31/160");
const delta=q(1,1024),eta=mul(q(3,2),delta);
const strictMargin=sub(sub(threshold,hullUpper),mul(q(4),eta));
must(eq(strictMargin,q(1,2560)),"positive uniform strict margin");
let paired=0, hullTests=0, maxPaired=ZERO, maxPertHull=ZERO;
for(let mask=0;mask<64;mask++){
 let pert=base.map((v,i)=>v.map((u,j)=>{
  let bit=(mask>>(2*i+j))&1;return add(u,bit===0?neg(delta):delta);
 }));
 for(let x of mid)for(let y of mid)for(let z of mid){
  let t=[x,y,z],d=distance(values(base,t),values(pert,t));
  must(le(d,eta),"paired finite perturbation TV bound "+mask);
  maxPaired=max(maxPaired,d);paired++;
 }
 let W=hullWitness(pert);
 for(let t of cornerParams){
  let d=distance(values(pert,t),W);
  must(le(d,add(hullUpper,mul(q(2),eta))),"transported hull witness "+mask);
  maxPertHull=max(maxPertHull,d);hullTests++;
 }
}
return {
 pass:"PASS_BRC_N4_S23_RATIONAL_OPEN_ROBUST_GAP_20261101",
 arithmetic:"JavaScript V8 BigInt reduced-rational exact",
 base_joint_witness_radius:show(baseMax),
 lower_polynomial_at_31_over_160:show(polynomial),
 source_aware_pairing_bound:show(eta),
 endpoint_displacement:show(delta),
 certified_open_neighborhood_gap_strictly_greater_than:show(strictMargin),
 perturbed_endpoint_sign_patterns:64,
 rational_parameter_pairs_checked:paired,
 perturbed_joint_hull_vertex_checks:hullTests,
 largest_checked_pair_distance:show(maxPaired),
 largest_checked_perturbed_hull_vertex_distance:show(maxPertHull),
 all_real_scope:"analytic causal coupling + Hausdorff radius argument; finite checks validate examples only"
};
