// Exact rational BRC-S23 nine-feature decoder certificate; node VERIFY.js
const assert = (q,m) => { if(!q) throw Error(m||"assert"); };
const abs = a => a<0n?-a:a;
const gcd = (a,b) => {a=abs(a);b=abs(b);while(b){let t=a%b;a=b;b=t;}return a||1n;};
const F = (a,b=1n) => {a=BigInt(a);b=BigInt(b);assert(b!==0n);if(b<0n){a=-a;b=-b;}let g=gcd(a,b);return [a/g,b/g];};
const Z=F(0),O=F(1),H=F(1,2);
const add=(a,b)=>F(a[0]*b[1]+b[0]*a[1],a[1]*b[1]);
const neg=a=>F(-a[0],a[1]),sub=(a,b)=>add(a,neg(b));
const mul=(a,b)=>F(a[0]*b[0],a[1]*b[1]),div=(a,b)=>F(a[0]*b[1],a[1]*b[0]);
const cmp=(a,b)=>a[0]*b[1]<b[0]*a[1]?-1:a[0]*b[1]>b[0]*a[1]?1:0;
const eq=(a,b)=>cmp(a,b)===0,abf=a=>a[0]<0n?neg(a):a;
const mmax=arr=>arr.reduce((a,b)=>cmp(a,b)>0?a:b,Z);
const sum=arr=>arr.reduce(add,Z);
const I=n=>F(n);
const A=[0,0,0,1,1,1],B=[2,2,3,2,2,4],C=[5,6,7,8,9,10];
const M=[[10,10,0,0,0,0],[9,11,0,0,0,0],[0,0,20,0,0,0],[0,0,0,10,10,0],[0,0,0,2,18,0],[0,0,0,0,0,20]];
const R=(p,q,r)=>[p,mul(sub(O,p),q),mul(mul(sub(O,p),sub(O,q)),r),mul(mul(sub(O,p),sub(O,q)),sub(O,r))];
const observed=(z,mask,beta)=> {
 let v=z.slice();
 for(let i=0;i<5;i++)if(mask&(1<<i))v[i]=beta;
 const sources=A.map((a,s)=>R(v[a],v[B[s]],v[C[s]]));
 return M.map(row=>[0,1,2,3].map(t=>div(sum(row.map((w,s)=>mul(I(w),sources[s][t]))),I(20))));
};
const schemes=[[3,31],[7,27],[11,23],[15,19]];
function construct(z,pair,betN,betE,j){
 let N=pair.find(m=>(m&4)===0),E=pair.find(m=>(m&4)!==0);
 assert(N!==undefined && E!==undefined,"mask-2");
 const isU=(g,m)=>(m&(1<<g))===0;
 const U3=isU(3,N)?"N":"E",U4=isU(4,N)?"N":"E";
 const V3=U3==="N"?"E":"N", V4=U4==="N"?"E":"N";
 const bn={N:betN,E:betE};
 const pn={N:observed(z,N,betN),E:observed(z,E,betE)};
 const r=j===0?1:0;
 const links=[["N",r,1],[U3,2,1],[U4,5,1],[V3,2,2],[V4,5,2],["E",0,2],["E",1,2],["E",3,2],["E",4,2]];
 const repair=links.filter(k=>k[1]===j);
 assert(repair.length===(j===2||j===5?2:1),"repair-count");
 const y=links.map(([view,row,t])=>pn[view][row][t]);
 return {y,links,N,E,U3,U4,V3,V4,bn};
}
function inv(y,h){
 const aN=sub(O,h.bn.N),aE=sub(O,h.bn.E),k=mul(aE,aE);
 const betaOf=v=>sub(O,h.bn[v]);
 const t0=div(y[5],k),t1=div(y[6],k),t3=div(y[7],k),t4=div(y[8],k);
 return [div(y[0],aN), div(y[1],betaOf(h.U3)),div(y[2],betaOf(h.U4)),
 sub(mul(I(11),t0),mul(I(10),t1)),
 add(mul(I(-9),t0),mul(I(10),t1)),
 div(y[3],mul(betaOf(h.V3),betaOf(h.V3))),
 div(sub(mul(I(9),t3),mul(I(5),t4)),I(4)),
 div(add(neg(t3),mul(I(5),t4)),I(4)),
 div(y[4],mul(betaOf(h.V4),betaOf(h.V4)))];
}
function inverseRows(h){
 const aN=sub(O,h.bn.N),aE=sub(O,h.bn.E),k=mul(aE,aE);
 const a=v=>sub(O,h.bn[v]),r=()=>Array(9).fill(Z);
 const rows=Array.from({length:9},r);
 rows[0][0]=div(O,aN);rows[1][1]=div(O,a(h.U3));rows[2][2]=div(O,a(h.U4));
 rows[3][5]=div(I(11),k);rows[3][6]=div(I(-10),k);
 rows[4][5]=div(I(-9),k);rows[4][6]=div(I(10),k);
 rows[5][3]=div(O,mul(a(h.V3),a(h.V3)));
 rows[6][7]=div(I(9),mul(I(4),k));rows[6][8]=div(I(-5),mul(I(4),k));
 rows[7][7]=div(I(-1),mul(I(4),k));rows[7][8]=div(I(5),mul(I(4),k));
 rows[8][4]=div(O,mul(a(h.V4),a(h.V4)));
 return rows;
}
let seed=123456789;const rng=()=>{seed=(1664525*seed+1013904223)>>>0;return seed;};
const rnd=()=>F(rng()%101,100);
const betas=[[Z,Z],[F(1,2),F(1,4)],[F(3,4),F(9,10)],[F(9,10),F(3,4)]];
let checked=0,sharp=0,maskChecks=0;
for(const pair of schemes)for(const [n,e] of betas)for(let j=0;j<6;j++){
 const dummy=Array(11).fill(H),h=construct(dummy,pair,n,e,j);
 const rows=inverseRows(h),norm=mmax(rows.map(row=>sum(row.map(abf))));
 const aN=sub(O,n),aE=sub(O,e),k=mul(aE,aE);
 const extra=h.U3==="N"?div(O,aN):div(O,aE);
 const Cpred=mmax([div(I(21),k),div(O,aN),div(O,mul(aN,aN)),extra]); // use exact row norms below, not this coarse check
 const simplified=(pair[0]===3)?mmax([div(I(21),k),div(O,aN)]):mmax([div(I(21),k),div(O,mul(aN,aN))]);
 assert(eq(norm,simplified),"closed-C");
 for(let t=0;t<16;t++){
  const z=Array.from({length:11},rnd),w=Array.from({length:11},rnd);
  let f=construct(z,pair,n,e,j),g=construct(w,pair,n,e,j);
  const x=inv(f.y,f);
  for(let u=0;u<9;u++)assert(eq(x[u],z[u+2]),"exact-recover");
  const delta=mmax(z.slice(2).map((x,u)=>abf(sub(x,w[u+2]))));
  const dy=mmax(f.y.map((x,u)=>abf(sub(x,g.y[u]))));
  assert(cmp(delta,mul(norm,dy))<=0,"stability");
  assert(f.links.filter(k=>k[1]===j).length===(j===2||j===5?2:1),"minimal-repair");
  checked++;
 }
 // Exact maximizer in image: perturb selected nine events by the signs
 // of a maximal row of the analytical inverse, around a feasible interior state.
 const ix=rows.findIndex(row=>eq(sum(row.map(abf)),norm)),eps=F(1,1000000);
 const base=construct(dummy,pair,n,e,j);
 const yt=base.y.map((val,col)=>add(val,cmp(rows[ix][col],Z)>0?eps:cmp(rows[ix][col],Z)<0?neg(eps):Z));
 const xNew=inv(yt,base);
 assert(xNew.every(v=>cmp(v,Z)>=0&&cmp(v,O)<=0),"sharp-witness-cube");
 const w=Array(11).fill(H);for(let u=0;u<9;u++)w[u+2]=xNew[u];
 const rw=construct(w,pair,n,e,j);
 assert(yt.every((v,u)=>eq(v,rw.y[u])),"sharp-feature-realization");
 const dx=mmax(w.slice(2).map(v=>abf(sub(v,H))));
 const dy=mmax(rw.y.map((v,u)=>abf(sub(v,base.y[u]))));
 assert(eq(dy,eps)&&eq(dx,mul(norm,dy)),"sharp-bound");
 sharp++;
 maskChecks++;
}
const result={flag:"PASS_BRC_S23_NINE_FEATURE_SHARP_NOISY_INVERSE_20261103",schemes:schemes.length,beta_pairs:betas.length,deletions:6,random_exact_reconstructions_and_bounds:checked,exact_feasible_sharp_witnesses:sharp,scope:"nine selected scalar event coordinates, exact rational checks"};
if (typeof process !== "undefined" && process.stdout) process.stdout.write(JSON.stringify(result)+"\n");
JSON.stringify(result);