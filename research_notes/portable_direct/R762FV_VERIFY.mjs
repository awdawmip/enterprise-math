"use strict";
// R762FV Node.js 18+ exact integer exhaustive verifier; run with node R762FV_VERIFY.mjs.
const n=6, I=[0,1,2,3,4,5], key=p=>p.join(","), mul=(p,q)=>q.map(i=>p[i]);
const check=(x,m)=>{if(!x)throw Error("FAILED "+m)};
function* perms(a,k=0){if(k===n){yield a.slice();return}for(let j=k;j<n;j++){[a[j],a[k]]=[a[k],a[j]];yield* perms(a,k+1);[a[j],a[k]]=[a[k],a[j]]}}
function typ(p){let seen=new Set(),lens=[];for(let i=0;i<n;i++){if(seen.has(i))continue;let x=i,l=0;while(!seen.has(x)){seen.add(x);x=p[x];l++}lens.push(l)}return lens.sort((a,b)=>b-a)}
function parity(p){let x=0;for(let i=0;i<n;i++)for(let j=i+1;j<n;j++)if(p[i]>p[j])x++;return x%2}
function inv(p){let q=Array(n);p.forEach((v,i)=>q[v]=i);return q}
let G=[];for(let a=0;a<6;a++)for(let b=a+1;b<6;b++)for(let c=b+1;c<6;c++){let p=I.slice();p[a]=b;p[b]=c;p[c]=a;G.push(p);p=I.slice();p[a]=c;p[c]=b;p[b]=a;G.push(p)}
function main(){
 const P=[...perms(I.slice())], A=P.filter(p=>parity(p)===0), generators=new Set(G.map(key));
 check(P.length===720&&A.length===360&&G.length===40&&generators.size===40,"sizes");
 let conj=0;for(const s of P)for(const g of G){check(generators.has(key(mul(mul(s,g),inv(s)))),"S6-equivariance");conj++}
 let dp=new Map([[key(I),1]]),seen=new Map(),rounds=[],third;
 for(let h=0;h<=4;h++){
  let classes={};for(const [s,v] of dp){const type=typ(s.split(",").map(Number)).join(",");if(!classes[type])classes[type]={size:0,per_element:v,paths:0};check(classes[type].per_element===v,"class coefficient");classes[type].size++;classes[type].paths+=v;if(!seen.has(s))seen.set(s,h)}
  rounds.push({h,reachable:dp.size,total:[...dp.values()].reduce((a,b)=>a+b,0),classes});if(h===3)third=new Map(dp);if(h===4)break;
  let nd=new Map();for(const [s,v] of dp){let p=s.split(",").map(Number);for(const g of G){let k=key(mul(g,p));nd.set(k,(nd.get(k)||0)+v)}}dp=nd
 }
 check(rounds.map(x=>x.reachable).join(",")==="1,40,270,360,360","support sequence");
 const wanted={"1,1,1,1,1,1":[1,400],"3,1,1,1":[40,306],"2,2,1,1":[45,224],"3,3":[40,114],"5,1":[144,175],"4,2":[90,128]};
 for(const [type,[size,per]] of Object.entries(wanted)){let x=rounds[3].classes[type];check(x&&x.size===size&&x.per_element===per,"third-step class "+type)}
 let direct=new Map();for(const a of G)for(const b of G){let ab=mul(a,b);for(const c of G){let k=key(mul(ab,c));direct.set(k,(direct.get(k)||0)+1)}}
 check(direct.size===360&&[...direct.values()].reduce((a,b)=>a+b,0)===64000,"direct triple words");
 for(const [k,v] of direct)check(third.get(k)===v,"independent direct/dynamic equality");
 let lengthByType={};for(const p of A){let type=typ(p),shortest=seen.get(key(p)),o=type.filter(x=>x%2===1).length;check(shortest===(6-o)/2,"minimal factor length");lengthByType[type.join(",")]=shortest}
 let min=Math.min(...direct.values());check(min===114,"lower transition");
 let abs=[...direct.values()].reduce((a,v)=>a+Math.abs(v*360-64000),0), den=2*64000*360;
 const gcd=(a,b)=>b?gcd(b,a%b):a, g=gcd(abs,den);check(abs/g===209&&den/g===1800,"TV exact");
 return {schema:"R762FV_EXACT_A6_WALK_CERTIFICATE_V1",frozen_scientific_p000:"a72226e2430ffa4786321ac86e7f0c599d5f0389",total_permutations:720,even_permutations:360,generators:40,conjugation_checks:conj,rounds,lengthByType,direct_words:64000,dynamic_direct_agree:true,min_three_step_paths:min,minorization:"513/800",three_step_TV:"209/1800",TV_bound:"(287/800)^k after 3k steps",validation:"PASS",review:"NOT_REVIEWED",native_event_permission:"UNPROVEN"}
}
if(typeof module!=="undefined"&&typeof require!=="undefined"&&require.main===module)console.log(JSON.stringify(main(),null,2));
