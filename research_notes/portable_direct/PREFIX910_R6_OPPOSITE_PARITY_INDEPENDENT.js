// PREFIX-909 exact finite named-XOR witness and prior-union checker (Node.js).
// Run: node PREFIX909_R6_MIXED_MULTIPLIER_CHECK.js
'use strict';
const assert=require('node:assert/strict');
const N=2**32,T=33*N,L=262145,H=524287,QP=131072;
function gcd(a,b){while(b){const t=a%b;a=b;b=t}return a}
function prior(){
 const old=new Set();for(let h=1;h<=17;h++)old.add(2**h);
 for(let i=2;i<=17;i++)for(let j=1;j<i;j++){old.add(2**i+2**j);old.add(2**i-2**j)}
 const g905=new Set();
 for(let m=3;m<=8191;m+=2)for(let i=2;i<=17;i++)for(let j=1;j<i;j++)for(const s of [-1,1]){
  const v=2**i+s*2**j;if(v%m===0){const d=v/m;if(d>0&&d<=H-L&&d%2===0&&!old.has(d))g905.add(d)}
 }
 const g906=new Set();
 for(let m=1;m<=8191;m+=2)for(let i=18;i<=30;i++)for(let j=1;j<=17;j++)for(const s of [-1,1]){
  const v=2**i+s*2**j;if(v%m===0){const d=v/m;if(d>0&&d<=H-L&&d%2===0&&!old.has(d)&&!g905.has(d))g906.add(d)}
 }
 const U=new Set([262147,280001,300001,320003,340007,360007,380003,400009,420001,440003,460001,480007,500383,510007,520001,524285]);
 for(let q=400011;q<=400521;q+=2)U.add(q);
 for(let q=480011;q<=480521;q+=2)U.add(q);
 for(let q=L;q<=H;q+=2)for(let h=1;h<32;h++)if((2**h-1)%q===0||(2**h+1)%q===0){U.add(q);break}
 const P=new Set();for(let j=0;j<64;j++)for(const k of [1,3,5])P.add(510000+k+194*j);
 const D907=new Set();for(let i=18;i<=22;i++)for(let j=1;j<=17;j++)for(const s of [-1,1])D907.add(2**i+s*2**j);
 const D908=new Set();for(let i=1;i<=19;i++)for(const s of [-1,1])D908.add(2**i+s);
 assert.deepEqual([old.size,g905.size,g906.size,U.size,P.size,D907.size,D908.size],[258,276,857,552,192,169,37]);
 function member(a,b){
  if(a*b<T||U.has(a)||U.has(b)||a/gcd(a,b)*b<N||33*Math.ceil(N/a)>b||33*Math.ceil(N/b)>a||P.has(a)||P.has(b))return true;
  const d=Math.abs(a-b);
  return old.has(d)||g905.has(d)||g906.has(d)||D907.has(3*a-b)||D907.has(3*b-a)||D908.has(2*a-b)||D908.has(2*b-a);
 }
 return member;
}
const inOld=prior(),encode=(a,b)=>((a-L)/2)*QP+(b-L)/2;
const decode=c=>[L+2*Math.floor(c/QP),L+2*(c%QP)],transpose=c=>(c%QP)*QP+Math.floor(c/QP);

const D909=new Set();
for(let i=1;i<=22;i++)for(const s of [-1,1])D909.add(2**i+s);
function inC909(a,b){
 if(inOld(a,b))return true;
 for(const [k,ell] of [[3,2],[4,1],[4,3]]){
  if(D909.has(k*a-ell*b)||D909.has(k*b-ell*a))return true;
 }
 return false;
}
const families=[[5,2],[5,4],[6,1],[6,5],[7,2],[7,4],[7,6],[8,1],[8,3],[8,5],[8,7]];
const novel=new Set(),reports=[];
for(const [k,ell] of families){
 const familySet=new Set();let n=0;
 for(let i=1;i<=22;i++)for(const s of [-1,1])for(let a=L;a<=H;a+=2){
  const numer=k*a-(2**i+s);
  if(numer%ell!==0)continue;
  const b=numer/ell;
  if(b<L||b>H||b%2===0)continue;
  const x=s===1?1-k%2:k%2,y=x+k*a,u=x+2**i,v=y-s;
  assert(x>=0&&y<N&&u<N&&v>=0&&v<N);
  assert.equal(x^2**i,u);assert.equal(y^1,v);
  assert.equal(y-x,k*a);assert.equal(v-u,ell*b);
  familySet.add(encode(a,b));n++;
 }
 let count=0;
 for(const z of familySet){let [a,b]=decode(z);if(!inC909(a,b)){count++;novel.add(z);}}
 reports.push([k,ell,n,familySet.size,count]);
}
let overlap=0;for(const z of novel)if(novel.has(transpose(z)))overlap++;
const added=2*novel.size-overlap;
assert.deepEqual(reports,[
 [5,2,78643,78643,34493],[5,4,812650,792989,408202],
 [6,1,43690,43690,27887],[6,5,716531,699055,364840],
 [7,2,56174,56174,27775],[7,4,271508,266826,116177],
 [7,6,636632,621029,325427],[8,1,32768,32768,9371],
 [8,3,54613,54613,26551],[8,5,327680,321127,149296],
 [8,7,575775,561732,295775]]);
assert.deepEqual([novel.size,overlap,added,7780668986+added],[1785732,8,3571456,7784240442]);
console.log('PREFIX910_INDEPENDENT_JS_PASS',JSON.stringify({family:reports,oriented:novel.size,transpose_intersection:overlap,added,certified_C910:7780668986+added}));
