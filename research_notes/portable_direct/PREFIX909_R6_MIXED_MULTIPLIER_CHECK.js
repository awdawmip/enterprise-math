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
const full=new Set(),family=[];
for(const [k,ell] of [[3,2],[4,1],[4,3]]){
 const per=new Set();let witnesses=0;
 for(let i=1;i<=22;i++)for(const s of [-1,1])for(let a=L;a<=H;a+=2){
  const numer=k*a-(2**i+s);
  if(numer<ell*L||numer>ell*H||numer%ell!==0)continue;
  const b=numer/ell;if(b%2===0)continue;
  const x=s===1?1-k%2:k%2,y=x+k*a,u=x+2**i,v=y-s;
  assert(x>=0&&y<N&&u<N&&v>=0&&v<N);
  assert.equal(x^2**i,u);assert.equal(y^1,v);
  assert.equal(y-x,k*a);assert.equal(v-u,ell*b);
  assert.equal((y-x)%a,0);assert.equal((v-u)%b,0);
  per.add(encode(a,b));witnesses++;
 }
 let old=0;for(const c of per)if(inOld(...decode(c)))old++;
 family.push({k,ell,parameter_witnesses:witnesses,unique_oriented_pairs:per.size,in_C908:old,outside_C908:per.size-old});
 for(const c of per)full.add(c);
}
const novel=new Set();for(const c of full)if(!inOld(...decode(c)))novel.add(c);
let oldTranspose=0,newTranspose=0;
for(const c of full)if(full.has(transpose(c)))oldTranspose++;
for(const c of novel)if(novel.has(transpose(c)))newTranspose++;
const result={family_results:family,raw_unique_oriented:full.size,raw_reverse_intersection:oldTranspose,novel_unique_oriented:novel.size,novel_reverse_intersection:newTranspose,new_distinct_ordered_pairs:2*novel.size-newTranspose,certified_C909:7778794188+2*novel.size-newTranspose,explicit_complement:QP**2-7778794188-2*novel.size+newTranspose};
assert.deepEqual(family.map(x=>[x.parameter_witnesses,x.unique_oriented_pairs,x.outside_C908]),[[961191,939346,452790],[65536,65536,31110],[917500,895655,453522]]);
assert.deepEqual([result.raw_unique_oriented,result.raw_reverse_intersection,result.novel_unique_oriented,result.novel_reverse_intersection,result.new_distinct_ordered_pairs,result.certified_C909,result.explicit_complement],[1900472,45,937399,0,1874798,7780668986,9399200198]);
console.log(JSON.stringify(result,null,2));
