// EC49EM: exact signed-X6 primitive observation and prefix witness checker.
// Integer rank over GF(1000003) is equivalent to rational rank 9 because
// zero-one 9x9 minors have absolute determinant <= 3^9 = 19683.
"use strict";
const O={a:[-1,-1],b:[-2,-2],c:[1,2,-1,-2],d:[2,1,-2,-1],
         e:[3,1,1,-3],f:[1,-1],g:[2,-2]};
const A=[["N",0],["N",1],["N",2],["A",0],["A",2],
         ["B",0],["B",1],["AB",0],["BA",0]];
const B=["N","A","B","AB","BA"],E=["A","B","AB","BA"];
const types=[];for(let t=0;t<3;t++)for(const e of E)types.push([t,e]);
const P=1000003,check=(x,s)=>{if(!x)throw Error(s)};
const nat=w=>[...w].flatMap(k=>O[k]);
function step(s,e){return e==="A"?({N:"A",B:"BA"}[s]||s):({N:"B",A:"AB"}[s]||s)}
function transfer(w){
 const path=nat(w),out=[];
 for(const [s0,l0] of A){let s=s0,last=l0;
  for(const v of path){if(last===1&&v===2)s=step(s,"A");
   if(last===2&&v===1)s=step(s,"B");last=v;}
  out.push(B.indexOf(s));}
 return out;
}
const canon=(t,e)=>["e","f","g"][t]+({A:"c",B:"d",AB:"cd",BA:"dc"}[e]||"");
function cols(sig){return B.map((b)=>sig.reduce((v,x,i)=>v|(x===B.indexOf(b)?1<<i:0),0))}
function rank(C){
 const piv=Array(9).fill(null);let r=0;
 for(const v0 of C){const v=Array.from({length:9},(_,i)=>(v0>>i)&1);
  for(let i=0;i<9;i++){if(!v[i])continue;
   if(piv[i]){const t=v[i],p=piv[i],q=p[i];
    for(let j=i;j<9;j++)v[j]=((v[j]*q-t*p[j])%P+P)%P;
   }else{piv[i]=v;r++;break;}
  }}
 return r;
}
function det(a0){
 const a=a0.map(row=>row.map(BigInt)),n=a.length;let prev=1n,sgn=1n;
 for(let k=0;k<n-1;k++){
  if(a[k][k]===0n){let j=k+1;while(j<n&&a[j][k]===0n)j++;
   if(j===n)return "0";[a[k],a[j]]=[a[j],a[k]];sgn=-sgn;}
  const p=a[k][k];for(let i=k+1;i<n;i++){
   for(let j=k+1;j<n;j++){const num=a[i][j]*p-a[i][k]*a[k][j];
    check(num%prev===0n,"Bareiss division");a[i][j]=num/prev;}
   a[i][k]=0n;
  }prev=p;
 }
 return String(sgn*a[n-1][n-1]);
}
function pcount(w){const v=nat(w);return [1,2,3,4,5,6].map(i=>v.filter(x=>x===i).length)}
function displacement(w){const v=nat(w);return [1,2,3,4,5,6].map(i=>v.filter(x=>x===i).length-v.filter(x=>x===-i).length)}
function trie(ws){const s=new Set();for(const w of ws){const v=nat(w);
 for(let i=1;i<=v.length;i++)s.add(v.slice(0,i).join(","));}return s.size}
function rankWords(ws){return rank(ws.flatMap(w=>cols(transfer(w))))}
const tc=types.map(([t,e])=>cols(transfer(canon(t,e))));
const masks=[];let fullCount=0;
for(let mask=1;mask<(1<<12);mask++){
 const c=[];for(let j=0;j<12;j++)if((mask>>j)&1)c.push(...tc[j]);
 if(rank(c)!==9)continue;fullCount++;
 if(masks.some(m=>(m&mask)===m))continue;masks.push(mask);
}
const expected=[
 [[0,"A"],[0,"B"],[1,"A"],[2,"B"]],
 [[0,"A"],[1,"A"],[1,"B"],[2,"B"]],
 [[0,"B"],[1,"A"],[2,"A"],[2,"B"]],
 [[1,"A"],[1,"B"],[2,"A"],[2,"B"]]];
check(JSON.stringify(masks.map(m=>types.filter((_,j)=>(m>>j)&1)))===JSON.stringify(expected),
 "minimal fullrank masks");
const certificates=masks.map(mask=>{
 const c=[];for(let j=0;j<12;j++)if((mask>>j)&1)c.push(...tc[j]);
 const sel=[];for(let i=0;i<c.length;i++){if(rank([...sel.map(k=>c[k]),c[i]])>sel.length)sel.push(i);
  if(sel.length===9)break;}
 const d=det(Array.from({length:9},(_,i)=>sel.map(k=>(c[k]>>i)&1)));
 check(d!=="0","rank minor");
 return {types:types.filter((_,j)=>(mask>>j)&1),columns:sel,det:d};
});
const symbols="acdefg",groups=new Map();
for(const x of symbols)for(const y of symbols){const w=x+y;
 if((w.match(/e/g)||[]).length!==(w.match(/a/g)||[]).length+1)continue;
 const k=pcount(w).join(",");if(!groups.has(k))groups.set(k,[]);groups.get(k).push(w);
}
const h2matches=[];for(const [p,ws] of groups)for(let m=1;m<(1<<ws.length);m++){
 const sel=ws.filter((_,j)=>(m>>j)&1);
 if(rankWords(sel)===9)h2matches.push({positive:p,words:sel,cost:trie(sel)});
}
const base=["ce","de","ec","ed"];
check(h2matches.length===1&&h2matches[0].cost===28&&
 h2matches[0].words.slice().sort().join(",")===base.slice().sort().join(","),"h2");
let joint=base.slice();const witness=[];
for(let h=3;h<=30;h++){
 const pair=["feg"+"f".repeat(h-3),"gef"+"f".repeat(h-3)];
 check(pair.every(w=>w.length===h&&displacement(w).join(",")==="2,0,0,0,0,0"),"return");
 check(pcount(pair[0]).join(",")===pcount(pair[1]).join(","),"same p");
 check(rankWords(pair)===9,"rank9 at h "+h);
 joint.push(...pair);check(trie(joint)===4*h+30,"prefix cost "+h);
 if([5,6,7,8,9,10,30].includes(h))witness.push({H:h,words:pair,cost:trie(joint),p:pcount(pair[0])});
}
const bounds=[];for(let h=5;h<=30;h++){
 const L=2*h+4;const qPositive=Math.min(3*(L-8)+4,(L-1)+2*(L-8),2*(L-1));
 const qZero=4*h+2;check(qPositive>=qZero,"analytic lower bound "+h);
 if([5,6,7,8,9,10,30].includes(h))bounds.push({H:h,qPositiveExtraAtLeast:qPositive,
  qZeroExtraAtLeast:qZero,totalAtLeast:28+qZero});
}
const qZeroMinorCols=[...cols(transfer("f")),...cols(transfer("g"))];
const qZeroMinor=det(Array.from({length:9},(_,i)=>qZeroMinorCols.slice(0,9).map(x=>(x>>i)&1)));
check(qZeroMinor==="-1","qzero minor");
return {status:"PASS",unit:"EC49EM",arithmetic:"exact integer / rank modulo 1000003",
 prime:P,determinant_bound:19683,rank_masks_tested:4095,full_rank_masks:fullCount,
 minimal_full_rank_masks:certificates,h2:h2matches[0],qzero_9_minor:qZeroMinor,
 witness_samples:witness,analytic_bounds_samples:bounds,
 claims:["for every integer H>=5: U_equal(H)=4H+30","U_equal(9)=66",
 "every fullrank q>=1 fiber at h=9 requires at least 70 total native-prefix edges"],
 analytic_proof:"See README_EC49EM.md; finite checks are certificate regressions."};
