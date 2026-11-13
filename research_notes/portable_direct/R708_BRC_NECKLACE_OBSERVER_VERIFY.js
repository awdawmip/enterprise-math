'use strict';
// Exact positive unit-branch BRC count and S3 observer certificate for native V38/V36 packet walks.
const assert=require('node:assert/strict');
const T={A:['012','013','023'],a:['012','023','013'],B:['012','023','123'],b:['012','123','023']};
const PA=[0,2,1],PB=[1,0,2],E=[0,1,2];
const compose=(p,q)=>q.map(x=>p[x]);
const key=(a)=>a.join('');
function* words(k,l){const C={A:k,a:k,B:l,b:l},N=2*(k+l),arr=[];
 function* go(){if(arr.length===N){yield arr.join('');return;}
 for(const c of 'AaBb')if(C[c]){--C[c];arr.push(c);yield*go();arr.pop();++C[c];}}
 yield*go();}
function walk(w){return [...w].flatMap(c=>T[c]);}
function holo(w){let h=E;for(const c of w)h=compose(h,'Aa'.includes(c)?PA:PB);return key(h);}
function profile(w){const s=walk(w),n=s.length,verts={},edges={};for(let i=0;i<n;i++){
 const a=s[i],b=s[(i+1)%n];verts[a]=(verts[a]||0)+1;const e=a+'>'+b;edges[e]=(edges[e]||0)+1;}
 return JSON.stringify({vertices:Object.entries(verts).sort(),edges:Object.entries(edges).sort()});}
const rotate=w=>w.slice(1)+w[0];
function necklace(w){let min=w,r=w;for(let i=1;i<w.length;i++){r=rotate(r);if(r<min)min=r;}return min;}
function fact(n){let p=1;for(let i=2;i<=n;i++)p*=i;return p;}
function phi(n){let q=n,r=n;for(let d=2;d*d<=r;d++)if(r%d===0){while(r%d===0)r/=d;q-=q/d;}if(r>1)q-=q/r;return q;}
function gcd(a,b){while(b)[a,b]=[b,a%b];return a;}
function necklaceFormula(k,l){const q=2*(k+l);let total=0;for(let d=1;d<=gcd(k,l);d++)if(k%d===0&&l%d===0){total+=phi(d)*fact(q/d)/(fact(k/d)**2*fact(l/d)**2);}return Math.round(total/q);}
function circularDeck(w,r){const s=walk(w),m=s.length,M=new Map();for(let i=0;i<m;i++){
 let b=[];for(let j=0;j<r;j++)b.push(s[(i+j)%m]);const x=b.join(':');M.set(x,(M.get(x)||0)+1);}return [...M].sort((a,b)=>a[0].localeCompare(b[0]));}
const runs=[];for(const [k,l] of [[1,1],[1,2],[2,1],[2,2]]){
 const groups=new Map(), H={}, all=[...words(k,l)];const firstProfile=profile(all[0]);
 for(const w of all){assert.equal(profile(w),firstProfile);const h=holo(w);H[h]=(H[h]||0)+1;
  const rep=necklace(w);if(!groups.has(rep))groups.set(rep,[]);groups.get(rep).push({w,h});
  const ph=holo(rotate(w));if(h==='012')assert.equal(ph,'012');else assert.notEqual(ph,h);
 }
 let flat=0,nonflat=0;for(const a of groups.values()){
 const hc={};for(const v of a)hc[v.h]=(hc[v.h]||0)+1;
 if(hc['012']){assert.equal(hc['012'],a.length);flat++;}
 else{assert.equal(Object.keys(hc).length,2);assert.equal(hc['120'],hc['201']);nonflat++;}
 }
 assert.equal(groups.size,necklaceFormula(k,l));
 const expected={
 '1,1':[16,4,4,6], '1,2':[108,36,36,30],
 '2,1':[108,36,36,30], '2,2':[1296,612,612,318]}[k+','+l];
 assert.deepEqual([H['012'],H['120'],H['201'],groups.size],expected);
 runs.push({k,l,branches:all.length,holonomy_counts:H,necklaces:groups.size,flat_necklaces:flat,nonflat_necklaces:nonflat,all_markov_profiles:1});
}
const witness=['AbaB','BAba'];assert.equal(necklace(witness[0]),necklace(witness[1]));
assert.equal(holo(witness[0]),'120');assert.equal(holo(witness[1]),'201');
for(const r of [1,2,3,4,6,12,24,25,48])assert.deepEqual(circularDeck(witness[0],r),circularDeck(witness[1],r));
const result={schema:'R708_BRC_NECKLACE_OBSERVER_EXACT_V1',status:'R708_EXACT_BRC_NECKLACE_PASS',source_model:'V17+V20+V36+V38+V39; unit labeled oriented BRC packet branches',tests:runs,witness:{rooted_words:witness,holonomies:witness.map(holo),cyclic_deck_radii_checked:[1,2,3,4,6,12,24,25,48]},scope:'exact complete enumeration of 2904 rooted packet orderings; universal mathematical proof in accompanying note'};
if(typeof module!=='undefined'&&require.main===module)process.stdout.write(JSON.stringify(result,null,2)+'\n');
module.exports={result};
