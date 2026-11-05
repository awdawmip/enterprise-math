"use strict";
// PREFIX-516 exact signed native X6 / typed BRC exterior-square certificate.
// Run: node prefix516_native_c6_area_certificate.js
const GATES={aab:[0,0,1],aba:[0,1,0]},ALPH="aAbBcCdDeE",COLOR=[0,4,1,2,3,3,4,4,4,4];
const IJ=[];for(let i=0;i<6;i++)for(let j=i+1;j<6;j++)IJ.push([i,j]);
const Z=n=>Array(n).fill(0),add=(a,b)=>a.map((x,i)=>x+b[i]),wedge=(a,b)=>IJ.map(([i,j])=>a[i]*b[j]-a[j]*b[i]);
const eq=(a,b)=>JSON.stringify(a)===JSON.stringify(b),check=(v,s)=>{if(!v)throw Error(s);};
function step(c){let z=Z(6),j=ALPH.indexOf(c);check(j>=0,"alphabet");z[Math.floor(j/2)]=j%2?-1:1;return z;}
function gate(g,q,c){let p=GATES[g],s=p.slice(0,q).concat([COLOR[ALPH.indexOf(c)]]);for(let k=3;k>0;k--)if(s.length>=k&&s.slice(-k).every((v,i)=>v===p[i]))return k;return 0;}
function trans(w,g){let a=[0,1,2,3];for(let c of w)a=a.map(q=>gate(g,q,c));return a;}
function sig(w,g){let y=Z(6),A=Z(15),V=0,W=0,first="N",last="N";for(let c of w){let s=step(c),i=s.findIndex(v=>v!==0);
 A=add(A,wedge(y,s));if(y[i]*s[i]<0){V+=[0,1,0,2,1,0][i];W+=[0,0,1,0,1,0][i];}y=add(y,s);
 if(i===1||i===2){let t=i===1?"B":"C";if(first==="N")first=t;last=t;}}
 return {n:w.length,y,V,W,T:trans(w,g),R:trans([...w].reverse().join(""),g),first,last,A};
}
function merge(a,b){let k=a.y.map((x,i)=>(Math.abs(x)+Math.abs(b.y[i])-Math.abs(x+b.y[i]))/2);return {n:a.n+b.n,
 y:add(a.y,b.y),V:a.V+b.V+k[1]+2*k[3]+k[4],W:a.W+b.W+k[2]+k[4],
 T:a.T.map(q=>b.T[q]),R:b.R.map(q=>a.R[q]),first:a.first!=="N"?a.first:b.first,last:b.last!=="N"?b.last:a.last,A:add(add(a.A,b.A),wedge(a.y,b.y))};}
function rev(a){return {...a,T:a.R,R:a.T,first:a.last,last:a.first,A:a.A.map(v=>-v)};}
function cref(a){return {...a,y:a.y.map((v,i)=>i===2?-v:v),A:a.A.map((v,i)=>IJ[i].includes(2)?-v:v)};}
const flip=w=>[...w].map(c=>c==="c"?"C":c==="C"?"c":c).join("");
const letter=([i,s])=>ALPH[2*i+(s<0?1:0)],neg=([i,s])=>[i,-s];
const dirs=[[0,1],[4,-1],[3,1],[0,-1],[4,1],[3,-1]];
const edges=dirs.map((a,r)=>{let b=dirs[(r+1)%6];return [letter(neg(a))+letter(b),letter(b)+letter(neg(a))];});
function word(bits){return bits.map((v,i)=>edges[i%6][v]).join("");}
function choose(n,k){let z=1;for(let i=1;i<=k;i++)z=z*(n-k+i)/i;return z;}
function histogram(m,g){const E=6*m,counts=new Map();for(let mask=0;mask<2**E;mask++){let bits=Array.from({length:E},(_,i)=>(mask>>i)&1),s=sig(word(bits),g);check(s.y.every(v=>v===0),"closed loop");let a=s.A.join(",");counts.set(a,(counts.get(a)||0)+1);}
 let base=sig(word(Z(E)),g).A,delta=[0,1,2].map(i=>{let a=sig(edges[i][0],g).A,b=sig(edges[i][1],g).A;return b.map((x,j)=>x-a[j]);}),expected=new Map();
 for(let x=0;x<=2*m;x++)for(let y=0;y<=2*m;y++)for(let z=0;z<=2*m;z++){let a=base.map((v,i)=>v+x*delta[0][i]+y*delta[1][i]+z*delta[2][i]);expected.set(a.join(","),choose(2*m,x)*choose(2*m,y)*choose(2*m,z));}
 check(counts.size===(2*m+1)**3&&eq([...counts].sort(),[...expected].sort()),"exact histogram");
 return {m,total_branch_histories:2**E,area_classes:counts.size,max_fiber:Math.max(...counts.values()),total_multiplicity:[...counts.values()].reduce((x,y)=>x+y,0)};
}
function execute(){let results={};const words=[[""]];for(let n=1;n<=3;n++)words.push(words[n-1].flatMap(w=>[...ALPH].map(c=>w+c)));
 for(let g of Object.keys(GATES)){
 let cache=new Map(words.flat().map(w=>[w,sig(w,g)])),split=0;
 for(let [w,s] of cache){check(eq(rev(s),sig([...w].reverse().join(""),g)),"reverse "+w);check(eq(cref(s),sig(flip(w),g)),"reflection "+w);}
 for(let n=0;n<=3;n++)for(let j=0;j<=n;j++)for(let u of words[j])for(let v of words[n-j]){check(eq(merge(cache.get(u),cache.get(v)),cache.get(u+v)),"composition "+u+" "+v);split++;}
 let x=sig("ed",g),y=sig("de",g),{A:ax,...bx}=x,{A:ay,...by}=y;
 check(eq(bx,by),"Gamma fiber");check(ax[IJ.findIndex(p=>p[0]===3&&p[1]===4)]===-1&&ay[IJ.findIndex(p=>p[0]===3&&p[1]===4)]===1,"local wedge");
 for(let [inner,outer] of edges){let a=sig(inner,g),b=sig(outer,g);check(eq(a.y,b.y)&&b.A.filter((v,i)=>v!==a.A[i]).length===1&&b.A.some((v,i)=>Math.abs(v-a.A[i])===2),"local C6 branch");}
 let a=sig(word(Z(6)),g),b=sig(word(Array(6).fill(1)),g),d=b.A.map((v,i)=>v-a.A[i]);
 check(eq(d,IJ.map(([i,j])=>i===0&&j===3?4:i===3&&j===4?4:i===0&&j===4?-4:0)),"loop area");
 results[g]={words_tested:cache.size,concat_splits:split,reverse_and_reflection_tests:cache.size,cycle_microtraces:edges,local_gamma_witness:["ed","de"],full_loop_area_difference:d,histograms:[histogram(1,g),histogram(2,g)]};
 }
 return {status:"ALL_CHECKS_PASS",frozen_scientific_pin:"f42f2906d77f24085c123f3ccfe9667d41caa96d",model:"STAR S_B=(L1,L4,L5), native X6 signed steps, two KMP gates",gates:results};
}
if(typeof require!=="undefined"&&require.main===module)console.log(JSON.stringify(execute(),null,2));
