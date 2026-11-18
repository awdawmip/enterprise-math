'use strict';
// Independent key-first subset dynamic programming for EC49EXN stratification.
// Only integer operations and frozen native operation codewords.
const H = [2,3,4,5,6,7,8];
const key = a => a.join(',');
function eligible(h){
 const opts=new Map();
 for(let w=1;w<=Math.floor((h+1)/2);w++)
   for(let r=0;r<=h;r++)
     for(let f=0;f<=h;f++){
       let g=h-2*(w-1)-1-r-f;
       if(g<0)continue;
       if(r===0&&(f===0||g===0))continue;
       opts.set(key([r+2*w+f,r+g,w]), r>=1?'T4':'T2');
     }
 return opts;
}
const eligibleSet=new Map(H.map(h=>[h,eligible(h)]));
if(H.some((h,i)=>eligibleSet.get(h).size!==[1,4,9,17,28,43,62][i]))throw Error('key count');
const result=[];let countByN2=Array(5).fill(0);let countByL=new Map();let profileCounts=new Map();
function addTo(map,k,n){map.set(k,(map.get(k)||0)+n);}
for(let a=0;a<7;a++)for(let b=a+1;b<7;b++)for(let c=b+1;c<7;c++){
 const tri=[H[a],H[b],H[c]],single=H.filter(h=>!tri.includes(h));
 const common=[...eligibleSet.get(tri[0]).keys()].filter(k=>tri.slice(1).every(h=>eligibleSet.get(h).has(k)));
 let total=0,validKeys=0;
 for(const commonKey of common){
   const extraType=tri.filter(h=>eligibleSet.get(h).get(commonKey)==='T2').length;
   const options=single.map(h=>[...eligibleSet.get(h).entries()].filter(([k])=>k!==commonKey));
   const U=[...new Set(options.flatMap(z=>z.map(x=>x[0])))];
   // dp[filled 4-bit block mask][T2 singleton mask] = exact partial injective maps.
   let dp=new Array(16*16).fill(0); dp[0]=1;
   for(const k of U){
     const nd=dp.slice();
     for(let i=0;i<4;i++){
       const typ=eligibleSet.get(single[i]).get(k);
       if(!typ)continue;
       for(let fill=0;fill<16;fill++){
         if(fill&(1<<i))continue;
         for(let tm=0;tm<16;tm++){
           const n=dp[fill*16+tm];
           if(n)nd[(fill|(1<<i))*16+(tm|(typ==='T2'?1<<i:0))]+=n;
         }
       }
     }
     dp=nd;
   }
   let local=0;
   for(let tm=0;tm<16;tm++){
     const n=dp[15*16+tm];if(!n)continue;
     local+=n;
     const n2=extraType+popcnt(tm);
     countByN2[n2]+=n;
     const types=H.map(h=> tri.includes(h)?eligibleSet.get(h).get(commonKey) : ((tm>>single.indexOf(h))&1?'T2':'T4'));
     addTo(profileCounts, types.map(t=>t==='T2'?'2':'4').join(''),n);
   }
   if(local){validKeys++;total+=local;
     const [u,v,w]=commonKey.split(',').map(Number);
     addTo(countByL,2*(u+v+w-1),local);
   }
 }
 if(total)result.push({triple:tri,count:total,keys:validKeys});
}
function popcnt(x){let n=0;while(x){n+=x&1;x>>=1;}return n;}
const total=countByN2.reduce((s,n)=>s+n,0);
const expectedCounts=[10828,63478,39511,8682,648];
if(total!==123147 || result.length!==8 || countByN2.some((x,i)=>x!==expectedCounts[i]) || profileCounts.size!==24)throw Error(JSON.stringify({total,result,countByN2,profiles:profileCounts.size}));
const ops={a:[-1,-1],b:[-2,-2],c:[1,2,-1,-2],d:[2,1,-2,-1],e:[3,1,1,-3],f:[1,-1],g:[2,-2]};
if(new Set(Object.values(ops).map(a=>a.slice(0,2).join(','))).size!==7)throw Error('two-step code uniqueness');
const native=(word)=>[...word].flatMap(o=>ops[o]);
function lcp(a,b){let i=0;while(i<Math.min(a.length,b.length)&&a[i]===b[i])i++;return i;}
const x=native('efgc'),y=native('efgfg');
if(x.length!==12 || y.length!==12 || lcp(x,y)!==9)throw Error('sharpness example');
console.log(JSON.stringify({status:'PASS', method:'independent key-first signed-type 4-bit subset DP',total,
 triple_families:result,count_by_T2:countByN2,
 repeated_key_primitive_lengths:Object.fromEntries([...countByL].sort((a,b)=>a[0]-b[0])),
 distinct_type_profiles:profileCounts.size,
 sharpness_example:{words:['efgc','efgfg'],length:12,shared_prefix:9}},null,2));