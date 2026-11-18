'use strict';
// Independent exact full double-key census via native-operation r,f,g,w counts.
const HS=[2,3,4,5,6,7,8];
function keys(h){const o=new Set();for(let w=1;w<=Math.floor((h+1)/2);w++)for(let r=0;r<=h;r++)for(let f=0;f<=h;f++){
 const g=h-2*w+1-r-f;if(g<0||r===0 && (f===0||g===0))continue;
 o.add([r+f+2*w,r+g,w].join(','));
}return [...o]}
const T=Object.fromEntries(HS.map(h=>[h,new Set(keys(h))]));
let count=0,n=0,rows=[];
for(let ia=0;ia<HS.length;ia++)for(let ja=ia+1;ja<HS.length;ja++){
 const aa=[HS[ia],HS[ja]], remain=HS.filter(x=>!aa.includes(x));
 for(let ib=0;ib<remain.length;ib++)for(let jb=ib+1;jb<remain.length;jb++){
   const bb=[remain[ib],remain[jb]];if(aa[0]>bb[0]||(aa[0]===bb[0]&&aa[1]>bb[1]))continue;
   const singles=remain.filter(x=>!bb.includes(x));let total=0;
   for(let k of T[aa[0]])if(T[aa[1]].has(k))for(let l of T[bb[0]])if(l!==k&&T[bb[1]].has(l)){
     for(let x of T[singles[0]])if(x!==k && x!==l)for(let y of T[singles[1]])if(y!==k&&y!==l&&y!==x){
       total+=[...T[singles[2]]].filter(z=>z!==k&&z!==l&&z!==x&&z!==y).length;
     }
   }
   if(total){n++;count+=total;rows.push({pairs:[aa,bb],singles,assignments:total})}
 }
}
if(n!==32||count!==1866362)throw Error('double census mismatch '+n+' '+count);
console.log(JSON.stringify({status:'PASS',double_skeletons:n,double_key_assignments:count,per_skeleton:rows},null,2));
