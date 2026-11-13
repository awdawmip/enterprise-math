"use strict";
// Exact integer model check. Node.js: node VERIFY.js
const D = 33600;
const M = [
  [10,10,0,0,0,0], [9,11,0,0,0,0], [0,0,20,0,0,0],
  [0,0,0,10,10,0], [0,0,0,2,18,0], [0,0,0,0,0,20]
];
function assert(ok,msg){if(!ok)throw Error(msg);}
function prepared(u,v,w,x) {
  // At a=1/4,b=1/3,c=1/2+offset/840, each source law is
  // [420,420,420+offset,420-offset]/1680.
  const offsets=[u,v,0,w,x,0];
  const src=offsets.map(t=>[420,420,420+t,420-t]);
  assert(src.every(p=>p.every(x=>x>=0)&&p.reduce((a,b)=>a+b,0)===1680),"source law");
  return M.map(row=>Array.from({length:4},(_,k)=>
      row.reduce((sum,weight,i)=>sum+weight*src[i][k],0)));
}
function trial(u,v,w,x) {
  const rows=prepared(u,v,w,x);
  assert(rows.every(q=>q.reduce((a,b)=>a+b,0)===D && q.every(y=>y>=0)),"prepared law");
  const minMass=Math.min(...rows.flat());
  const gap=D-minMass-25200; // exact r(z)-3/4 in units of 1/D.
  const expect=Math.max(
    Math.abs(10*(u+v)),Math.abs(9*u+11*v),
    Math.abs(10*(w+x)),Math.abs(2*(w+9*x)));
  assert(gap===expect, "exact full-cube radius formula");
  assert(40*Math.max(Math.abs(u),Math.abs(v))<=42*gap,
      "AU inverse bound");
  assert(40*Math.max(Math.abs(w),Math.abs(x))<=7*gap,
      "BU inverse bound");
  return {gap,rows};
}
const vals=[-420,-280,-140,0,140,280,420];
let checked=0;
for(const u of vals)for(const v of vals)
for(const w of vals)for(const x of vals){trial(u,v,w,x);checked++;}
const au=trial(210,-190,0,0);
const bu=trial(0,0,210,-90);
assert(au.gap===200 && 40*210===42*au.gap,"AU sharp extremizer");
assert(bu.gap===1200 && 40*210===7*bu.gap,"BU sharp extremizer");
const erased=trial(210,-210,0,0);
assert(erased.gap===420,"erasure gap");
assert(erased.rows.every((r,i)=>i===1 || r.every(x=>x===8400)),
       "other five prepared rows not uniform");
assert(erased.rows[1][2]===7980 && erased.rows[1][3]===8820,
       "second AU observer must distinguish the sources");
const result={
  status:"PASS_BRC_N4_S23_OBSERVER_CONDITIONING_20261101",
  arithmetic:"integer_exact", prepared_denominator:D, source_denominator:1680,
  exact_grid_points:checked, bounded_offsets:"u,v,w,x in [-1/2,1/2]",
  full_cube_risk:"r(z)=1-min_{i,j} p_i(z)_j",
  exact_gap:"(1/2)max(|(u+v)/2|,|(9u+11v)/20|,|(w+x)/2|,|(w+9x)/10|)",
  au_sharp:{offsets_over_840:[210,-190,0,0],gap:"1/168",
             radius:"127/168",inverse_constant:42},
  bu_sharp:{offsets_over_840:[0,0,210,-90],gap:"1/28",
             radius:"11/14",inverse_constant:7},
  erasure_witness:{offsets_over_840:[210,-210,0,0],
                   omitted_row:1, other_rows:"uniform", full_gap:"1/80"},
  model:"six labelled sources; positive BRC weights 20M; four stops; causal S23",
  inference:"finite grid checks exact formulas, universal statements require analytic proof"
};
console.log(JSON.stringify(result,null,2));
