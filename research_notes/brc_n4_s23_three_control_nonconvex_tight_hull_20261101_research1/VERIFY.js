"use strict";
// Exact integer verifier for a lawful positive-source BRC N4 S23 three-control box.
// All row probabilities are multiples of 1/384. All 125 grid triples and eight corners are legal.
function verify(){
 const S=384;
 const M20=[[10,10,0,0,0,0],[9,11,0,0,0,0],[0,0,20,0,0,0],
            [0,0,0,10,10,0],[0,0,0,2,18,0],[0,0,0,0,0,20]];
 const ok=(b,msg)=>{if(!b)throw Error(msg);};
 function mix(src){return M20.map(row=>Array.from({length:4},(_,j)=>{
   const n=row.reduce((x,w,k)=>x+w*src[k][j],0);ok(n%20===0,"invalid mixture");return n/20;
 }));}
 function prepared(a,b,c){
   ok([a,b,c].every(x=>Number.isInteger(x)&&x>=2&&x<=6),"outside rational cube");
   const au=[48*a,6*(8-a)*b,3*(8-a)*(8-b),3*(8-a)*(8-b)];
   const av=[48*a,0,6*(8-a)*c,6*(8-a)*(8-c)];
   const bu=[96,36*b,18*(8-b),18*(8-b)];
   const bv=[96,96,96,96];
   return mix([au,au,av,bu,bu,bv]);
 }
 const center=mix([[176,104,52,52],[176,104,52,52],[176,0,104,104],
                   [96,144,72,72],[96,144,72,72],[96,96,96,96]]);
 function tv(p,q){
   ok(p.reduce((x,y)=>x+y,0)===S && q.reduce((x,y)=>x+y,0)===S,"mass lost");
   const n=p.reduce((x,y,j)=>x+Math.abs(y-q[j]),0);
   ok(n%2===0,"nonintegral TV");return n/2;
 }
 let grid=0,rowChecks=0,corners=0,vertexRowChecks=0,maxGrid=0;
 for(let a=2;a<=6;a++)for(let b=2;b<=6;b++)for(let c=2;c<=6;c++){
   const p=prepared(a,b,c), risks=p.map((r,i)=>tv(r,center[i]));
   ok(risks.every(x=>x<=112),"grid exceeds 7/24");
   grid++;rowChecks+=6;maxGrid=Math.max(maxGrid,...risks);
   if([2,6].includes(a)&&[2,6].includes(b)&&[2,6].includes(c)){
     ok(risks.every((x,i)=>x===[112,112,112,72,72,0][i]),"vertex row risk mismatch");
     corners++;vertexRowChecks+=6;
   }
 }
 ok(grid===125&&rowChecks===750&&corners===8&&vertexRowChecks===48&&maxGrid===112,
    "coverage/radius mismatch");
 const low=prepared(2,2,4),high=prepared(6,6,4);
 const midpoint=low.map((r,i)=>r.map((x,j)=>(x+high[i][j])/2));
 ok(midpoint[2][0]===192 && midpoint[3][1]===144 && midpoint[0][1]===72,
    "joint nonconvex midpoint mismatch");
 ok(prepared(4,4,4)[0][1]===96 && 96-midpoint[0][1]===24,
    "lawful second-stage mismatch not 1/16");
 const alpha=176,beta=104,r=112;
 ok([288-alpha,216-beta,alpha+beta-168].every(x=>x===r),"sharp AV dual mismatch");
 ok(prepared(2,6,4)[0][1]===216 && prepared(2,2,4)[0].slice(2).reduce((x,y)=>x+y,0)===216,
    "sharp AU uniqueness events mismatch");
 ok(216-center[0][1]===r && 216-center[0].slice(2).reduce((x,y)=>x+y,0)===r,
    "b uniqueness tightness mismatch");
 let midpointRadius=0;
 const mid=prepared(4,4,4);
 for(const a of [2,6])for(const b of [2,6])for(const c of [2,6])
   midpointRadius=Math.max(midpointRadius,...prepared(a,b,c).map((row,i)=>tv(row,mid[i])));
 ok(midpointRadius===120,"parameter midpoint radius mismatch");
 return {
   pass:"PASS_BRC_N4_S23_THREE_CONTROL_NONCONVEX_TIGHT_HULL_20261101",
   execution:"Node.js v22.16.0; exact integer probability scale 384",
   grid_policies:grid, prepared_row_checks:rowChecks, continuum_vertices:corners,
   vertex_row_checks:vertexRowChecks,
   corner_TV_by_prepared_row_over_384:[112,112,112,72,72,0],
   unique_lawful_anchor:["11/24","1/2","1/2"],
   lawful_radius:"7/24", convex_hull_radius:"7/24",
   parameter_midpoint_radius:"5/16", AV_dual:"3r>=7/8",
   AU_uniqueness:"two events force b>=1/2 and b<=1/2",
   nonconvexity:{inferred_a:"1/2",inferred_b:"1/2",mid_AU_time2:"3/16",
                 forced_lawful_AU_time2:"1/4",gap:"1/16"},
   all_real_coverage:"analytic multi-affine vertex argument, not grid extrapolation",
   status:"AUTHOR_ANALYTIC_PROOF_NODE_EXACT_INTEGER_EXECUTED_UNREVIEWED_NOT_ADMITTED",
   P000_native_bridge:"NOT_ESTABLISHED"
 };
}
console.log(JSON.stringify(verify(),null,2));
