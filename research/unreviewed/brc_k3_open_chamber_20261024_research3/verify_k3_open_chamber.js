'use strict';
// Node >=18. Exact rational BigInt signs, 16-mask independent enumeration.
const A=[1n,22n,2n,3n],B=[1n,22n,2n,4n],Z=[28n,29n],E=[[0,1],[0,2],[0,3],[2,3]],d=[3n,1n,2n,2n],route=[1,0,1,3];
function ab(x){return x<0n?-x:x}
function gcd(x,y){while(y){[x,y]=[y,x%y]}return ab(x)}
function r(x,y=1n){if(y<0n){x=-x;y=-y}const g=gcd(ab(x),y);return [x/g,y/g]}
function plus(a,b){return r(a[0]*b[1]+b[0]*a[1],a[1]*b[1])}
function minus(a,b){return plus(a,[-b[0],b[1]])}
function times(a,b){return r(a[0]*b[0],a[1]*b[1])}
function pow(a,k){return r(a[0]**BigInt(k),a[1]**BigInt(k))}
function cmp(a,b){let z=a[0]*b[1]-b[0]*a[1];return z<0n?-1:z>0n?1:0}
function show(a){return String(a[0])+'/'+String(a[1])}
function check(b,msg){if(!b)throw Error(msg)}
function qi(a,i){return r((a?B:A)[i],Z[a])}
function se(a,j){return plus(qi(a,E[j][0]),qi(a,E[j][1]))}
function vi(x,y,i){return times(pow(qi(0,i),x),pow(qi(1,i),y))}
function ed(x,y,j){return times(pow(se(0,j),x),pow(se(1,j),y))}
function delta(x,y){if(x+y===0)return r(0n);let z=r(0n);for(let j=0;j<4;j++)z=plus(z,ed(x,y,j));for(let i=0;i<4;i++)z=minus(z,times(r(d[i]),vi(x,y,i)));return z}
function D(x,y,a,i){return times(times(r(d[i]),minus(r(1n),qi(a,i))),vi(x,y,i))}
function C(x,y,a,j){return times(minus(r(1n),se(a,j)),ed(x,y,j))}
function min(rows){return rows.reduce((p,q)=>cmp(p.v,q.v)<=0?p:q)}
let ds=[],cuts=[],slacks=[],gaps=[];
for(let n=2;n<=4;n++)for(let x=0;x<=n;x++)for(let a=0;a<2;a++){
 const inc=minus(delta(x+(a===0),n-x+(a===1)),delta(x,n-x));
 check(cmp(inc,r(0n))<0,'increment'); ds.push({n,x,a,v:r(-inc[0],inc[1])})
}
for(let n=1;n<=4;n++)for(let x=0;x<=n;x++){
 const v=minus(D(x,n-x,0,1),C(x,n-x,0,0));check(cmp(v,r(0n))>0,'high cut');cuts.push({n,x,v})
}
for(let x=0;x<=5;x++)for(let a=0;a<2;a++)for(let j=0;j<4;j++){
 let v=C(x,5-x,a,j);
 for(let i=0;i<4;i++)if(route[i]===j)v=minus(v,D(x,5-x,a,i));
 check(cmp(v,r(0n))>0,'n5 flow');slacks.push({x,a,j,v})
}
for(let a=0;a<2;a++)for(let j=1;j<4;j++){
 let v=minus(qi(a,1),se(a,j));check(cmp(v,r(0n))>0,'forbidden arc');gaps.push({a,j,v})
}
let masks=0;
function dp(word){let states=Array(16).fill(0n);states[0]=1n;for(let a of word){
 let next=Array(16).fill(0n);
 for(let mask=0;mask<16;mask++)for(let i=0;i<4;i++)next[mask|(1<<i)]+=states[mask]*(a?B:A)[i];
 states=next;
}let z=0n;for(let [i,j] of E)z+=states[(1<<i)|(1<<j)];return z}
for(let n=1;n<=6;n++)for(let word=0;word<(1<<n);word++){
 const acts=Array.from({length:n},(_,i)=>(word>>i)&1),x=acts.filter(a=>a===0).length,y=n-x;
 const p=delta(x,y),den=28n**BigInt(x)*29n**BigInt(y);
 check(den%p[1]===0n,'fraction not integral');check(dp(acts)===p[0]*(den/p[1]),'mask DP mismatch');masks++;
}
const md=min(ds),mc=min(cuts),ms=min(slacks),mg=min(gaps),eps=r(1n,10000000n);
check(cmp(times(r(144n),eps),md.v)<0,'Lipschitz delta');
check(cmp(times(r(15n),eps),mc.v)<0,'Lipschitz cut');
check(cmp(times(r(42n),eps),ms.v)<0,'Lipschitz flow');
check(cmp(times(r(3n),eps),mg.v)<0,'Lipschitz spectrum');
check(cmp(eps,r(1n,29n))<0,'positive q');
check(cmp(times(r(2n),eps),r(1n,812n))<0,'distinct actions');
const result={schema:'EM_BRC_K3_OPEN_CHAMBER_V1',base:{alpha:'(1,22,2,3)/28',beta:'(1,22,2,4)/29'},edges:E,epsilon:'1/10000000',counts:{negative_increments:ds.length,positive_cuts:cuts.length,positive_flow_slacks:slacks.length,forbidden_spectrum_gaps:gaps.length,independent_words:masks},exact_minima:{abs_increment:{value:show(md.v),n:md.n,x:md.x,action:md.a},high_cut:{value:show(mc.v),n:mc.n,x:mc.x},n5_flow_slack:{value:show(ms.v),x:ms.x,action:ms.a,edge:ms.j},nonincident_gap:{value:show(mg.v),action:mg.a,edge:mg.j}},bounds:{increment:'144e-7',high_cut:'15e-7',flow:'42e-7',spectral_gap:'3e-7'},conclusion:'Within the open probability simplex neighborhood K0=n>=5,K1=n>=4,K2=n>=3,K3=S=n>=2; no K4 minus K3 state.',status:'AUTHOR_CHECKED_UNREVIEWED'};
if(typeof console!=='undefined')console.log(JSON.stringify(result,null,2));
result;
