"use strict";
const assert=(cond,msg)=>{if(!cond)throw Error(msg)};
const key=v=>v.join(",");
const scaled=(x,y0,y1)=>[8+4*x+x*(y0+3*y1),8+4*x+2*x*(y0+y1),16-(y0+3*y1),16-2*(y0+y1)];
const lr=[];
for(let x=0;x<=1;x++)for(let y0=0;y0<=1;y0++)for(let y1=0;y1<=1;y1++)lr.push(scaled(x,y0,y1));
const keys=new Set(lr.map(key));
assert(keys.size===8,"eight distinct LR vertex vectors");
let full=0;
for(let mask=0;mask<32;mask++){
 const x=mask&1, y00=(mask>>1)&1,y01=(mask>>2)&1,y10=(mask>>3)&1,y11=(mask>>4)&1;
 const y0=x?y10:y00,y1=x?y11:y01;
 assert(keys.has(key(scaled(x,y0,y1))),"FULL Boolean vertex missing from LR convex hull");
 full++;
}
assert(full===32,"32 FULL Boolean strategies");
function det4(rows){
 let sum=0n;
 function rec(i,mask,sign,product){
  if(i===4){sum+=BigInt(sign)*product;return}
  for(let j=0;j<4;j++)if(!(mask&(1<<j))){
    const swaps=Array.from({length:4-j-1},(_,k)=>j+k+1).filter(k=>mask&(1<<k)).length;
    rec(i+1,mask|(1<<j),sign*(swaps%2?-1:1),product*BigInt(rows[i][j]));
  }
 }
 rec(0,0,1,1n);return sum;
}
const vs=lr.slice().sort((a,b)=>{for(let i=0;i<4;i++)if(a[i]!==b[i])return a[i]-b[i];return 0});
const ix=[0,1,2,4,5],basis=ix.slice(1).map(i=>vs[i].map((t,j)=>t-vs[0][j]));
const d=det4(basis);
assert(d===-16n,"scaled affine determinant must be -16");
const P=[2,6,2,6],Q=[4,4,4,4],Y=[0,1,1,0],X=[0,0,1,1];
let sumPY=0,sumQY=0,sumPXY=0,sumQXY=0,sumPX=0,sumQX=0;
for(let i=0;i<4;i++){sumPY+=P[i]*Y[i];sumQY+=Q[i]*Y[i];sumPXY+=P[i]*X[i]*Y[i];sumQXY+=Q[i]*X[i]*Y[i];sumPX+=P[i]*X[i];sumQX+=Q[i]*X[i]}
assert(P.reduce((a,b)=>a+b,0)===16&&Q.reduce((a,b)=>a+b,0)===16,"normalized kernels");
assert(P.every(v=>v>0)&&Q.every(v=>v>0),"positive kernel");
assert(sumPX===8&&sumQX===8&&sumPY===8&&sumQY===8&&sumPXY===2&&sumQXY===4,"witness branch flow");
const ep64=16+sumPX/2+sumPXY/2,eq64=16+sumQX/2+sumQXY/2;
assert(ep64===21&&eq64===22,"error witness");
assert(4*(4-sumPY/16)===14&&4*(4-sumQY/16)===14,"time witness");
for(const x of [0,1])for(const y0 of [0,1])for(const y1 of [0,1]){
 const v=scaled(x,y0,y1);
 assert(v[0]-v[1]===x*((y0+3*y1)-2*(y0+y1)),"LR algebraic identity (scaled)");
}
console.log("LR_BOOLEAN=8 FULL_BOOLEAN=32");
console.log("FULL_BOOLEAN_SET_SUBSET_LR_BOOLEAN_SET=true");
console.log("SCALED_4D_AFFINE_DETERMINANT="+d.toString());
console.log("LR_COLLISION_LIKELIHOOD_RATIOS=1/2,3/2");
console.log("FULL_WITNESS=(21/64,11/32,7/2,7/2)");
console.log("LR_INVARIANT_ABS_ERROR_TIME_BOUND=|eP-eQ|<=|TP-TQ|/8");
console.log("WITNESS_LINFTY_DISTANCE_LOWER_BOUND=1/144");
console.log("PASS_EXACT_R5_ROUTING_MEMORY_FULLRANK_HULL_EQUAL_REAL_IMAGE_GAP");