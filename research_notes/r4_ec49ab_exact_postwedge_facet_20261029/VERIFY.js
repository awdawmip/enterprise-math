"use strict";
function run(){
 function gcd(a,b){a=a<0n?-a:a;b=b<0n?-b:b;while(b){let c=a%b;a=b;b=c;}return a;}
 function f(a,b=1){a=BigInt(a);b=BigInt(b);if(b<0n){a=-a;b=-b;}if(!b)throw Error("division by zero");let g=gcd(a,b);return [a/g,b/g];}
 const z=f(0),o=f(1),add=(x,y)=>f(x[0]*y[1]+y[0]*x[1],x[1]*y[1]),sub=(x,y)=>f(x[0]*y[1]-y[0]*x[1],x[1]*y[1]),mul=(x,y)=>f(x[0]*y[0],x[1]*y[1]),div=(x,y)=>f(x[0]*y[1],x[1]*y[0]);
 const cmp=(x,y)=>{let v=x[0]*y[1]-y[0]*x[1];return v<0n?-1:v>0n?1:0;},eq=(x,y)=>cmp(x,y)===0,str=x=>x[1]===1n?String(x[0]):String(x[0])+"/"+String(x[1]),assert=(p,m)=>{if(!p)throw Error(m);};
 const k=f(5346,2341),d0=f(17,288);
 const t=(w,u)=>add(f(1,2),mul(f(2*u-1,200),f(1-w)));
 const p=(w,j)=>w===j?f(1,6):f(1,12),q=()=>f(1,9);
 function cell(x,c,u,j){
  let P=z,Q=z;for(let w=0;w<3;w++){let a=mul(x[w][c],t(w,u));P=add(P,mul(a,p(w,j)));Q=add(Q,mul(a,q()));}
  return [P,Q,sub(P,Q),sub(mul(f(3),Q),mul(f(2),P))];
 }
 function vertex(i,j,tags,bt,b){
  let h=add(f(5,16),b),x=Array.from({length:3},()=>Array.from({length:4},()=>z));
  for(let w=0;w<3;w++){let H=w===i?h:z,B=w===j?b:z;assert(cmp(add(H,B),o)<=0,"cap");x[w][tags[w]]=add(x[w][tags[w]],sub(o,add(H,B)));x[w][bt]=add(x[w][bt],B);}
  return x;
 }
 for(let source of ["P","Q"]){let s=z,n=0;for(let w=0;w<3;w++)for(let u=0;u<2;u++)for(let j=0;j<3;j++){let v=mul(t(w,u),source==="P"?p(w,j):q());assert(cmp(v,z)>0,"positivity");s=add(s,v);n++;}assert(n===18&&eq(s,o),"normalization");}
 let count=0,eqs=0,maximum=z,groups=[];
 for(let b of [z,f(1,16)]){
  let local=0,localEq=0,localMax=z;
  for(let i=0;i<3;i++)for(let j=0;j<3;j++)for(let mask=0;mask<8;mask++)for(let bt=2;bt<=3;bt++){
   let tags=[mask&1,(mask>>1)&1,(mask>>2)&1],x=vertex(i,j,tags,bt,b),s=z;
   for(let c=0;c<4;c++)for(let u=0;u<2;u++)for(let j2=0;j2<3;j2++){let a=cell(x,c,u,j2);assert(cmp(a[3],z)>=0,"negative slack");let e=sub(mul(k,a[2]),a[3]);if(cmp(e,z)>0)s=add(s,e);}
   assert(cmp(s,mul(k,d0))<=0,"dual violation");if(eq(s,mul(k,d0))){eqs++;localEq++;}if(cmp(s,maximum)>0)maximum=s;if(cmp(s,localMax)>0)localMax=s;count++;local++;
  }
  groups.push({b:str(b),vertices:local,equalities:localEq,max_score:str(localMax)});
 }
 assert(count===288&&eqs===48&&eq(maximum,mul(k,d0)),"288-vertex certificate");
 let x=[[o,z,z,z],[z,o,z,z],[f(9,16),z,f(1,16),z]],alpha=z,beta=z,T=z,b=z;
 for(let w=0;w<3;w++)for(let c=0;c<4;c++){T=add(T,x[w][c]);if(c>=2)b=add(b,x[w][c]);}
 for(let c=0;c<4;c++)for(let u=0;u<2;u++)for(let j=0;j<3;j++){let accept=(c===1&&j===1)||(c===2&&j===2)?o:(c===0&&u===1&&j===0?f(400,2341):z),v=cell(x,c,u,j);alpha=add(alpha,mul(accept,v[0]));beta=add(beta,mul(accept,v[1]));}
 let delta=sub(alpha,beta),cost1=div(add(T,b),f(3)),cost2=div(T,f(3));
 assert(eq(cost1,f(43,48))&&eq(cost2,f(7,8)),"costs");
 assert(eq(alpha,f(915,4682))&&eq(beta,f(4979,37456))&&eq(delta,f(1,16)),"witness");
 assert(eq(alpha,add(mul(f(3),delta),mul(k,sub(delta,d0)))),"primal dual equality");
 let d1=add(d0,f(2341,115200)),a1=add(f(17,96),f(4123,38400));
 assert(eq(d1,f(3047,38400))&&eq(a1,f(3641,12800))&&eq(a1,add(mul(f(3),d1),mul(k,sub(d1,d0)))),"sharp segment");
 return {schema:"EC49AB_BIGINT_EXACT_FACET_V1",status:"AUTHOR_PROVED / EXACT_BIGINT_CHECK_PASS / UNREVIEWED / NOT_ADMITTED",leaves_each_source:18,
  dual:{k:str(k),breakpoint:str(d0),cap:str(mul(k,d0)),groups,vertex_checks:count,equality_vertices:eqs},
  sharp:{delta_min:"0",delta_max:str(d1),formula:"alpha_min=3*delta+(5346/2341)*max(0,delta-17/288)"},
  witness:{delta:str(delta),alpha:str(alpha),beta:str(beta),C1:str(cost1),C2:str(cost2),extra_accept_probability:"400/2341"},
  scope:"Analytic all-real causal-convex reduction is in PROOF.md; finite endpoints checked here. No native BRC/X6 or independent review claim."};
}
if(typeof require!=="undefined"&&require.main===module)console.log(JSON.stringify(run(),null,2));