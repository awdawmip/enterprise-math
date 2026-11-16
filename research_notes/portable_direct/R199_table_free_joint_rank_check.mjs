// R199 exact BigInt joint source/tail index; Node.js, no dependencies.
function P(n,j){let v=1n;for(let i=0;i<j;i++)v*=BigInt(n-i);return v}
function N(n){let v=1n;for(let i=1;i<=n;i++)v=1n+BigInt(i)*v;return v}
function prep(m,k,L){
 if(!Number.isSafeInteger(m)||m<1||!Number.isSafeInteger(k)||k<0||k>m||!Number.isSafeInteger(L)||L<0)throw Error("params");
 let w=[Array.from({length:k+1},(_,r)=>N(k-r))];
 for(let q=1;q<=L;q++){let v=[];for(let r=0;r<=k;r++)v.push(BigInt(m-k+r)*w[q-1][r]+(r===k?0n:BigInt(k-r)*w[q-1][r+1]));w.push(v)}
 let short=0n,p=1n;for(let h=0;h<L;h++){short+=p;p*=BigInt(m)}
 return {m,k,L,w,short,total:short+w[L][0]};
}
function last(t,k){let v=[],s=new Set();for(let i=t.length-1;i>=0;i--)if(t[i]<k&&!s.has(t[i])){s.add(t[i]);v.push(t[i])}return v.reverse()}
function rankP(u,a){
 let n=a.length,j=u.length,z=0n;if(j>n)throw Error("partial length");
 for(let h=0;h<j;h++)z+=P(n,h);
 a=[...a];for(let i=0;i<j;i++){let x=a.indexOf(u[i]);if(x<0)throw Error("duplicate/nonmissing");z+=BigInt(x)*P(n-i-1,j-i-1);a.splice(x,1)}return z;
}
function unrankP(z,a){
 a=[...a];let n=a.length,j=0;
 while(j<=n){let b=P(n,j);if(z<b)break;z-=b;j++}
 if(j>n)throw Error("partial range");
 let u=[];for(let i=0;i<j;i++){let b=P(n-i-1,j-i-1),x=Number(z/b);z%=b;u.push(a.splice(x,1)[0])}return u;
}
function rank(s,t,c){
 const {m,k,L,w,short}=c;
 if(t.length>L||t.some(x=>!Number.isInteger(x)||x<0||x>=m))throw Error("tail");
 if(t.length<L){
  if(s.join()!=last(t,k).join())throw Error("short support");
  let offset=0n,p=1n;for(let h=0;h<t.length;h++){offset+=p;p*=BigInt(m)}
  let digits=0n;for(let a of t)digits=digits*BigInt(m)+BigInt(a);
  return offset+digits;
 }
 let v=last(t,k),u=s.slice(0,s.length-v.length);
 if(s.length<v.length||s.slice(u.length).join()!=v.join())throw Error("full support");
 let a=Array.from({length:k},(_,i)=>i).filter(x=>!v.includes(x));
 let z=short,seen=new Set();
 for(let i=0;i<L;i++){
  for(let x=0;x<t[i];x++)z+=w[L-i-1][seen.size+(x<k&&!seen.has(x)?1:0)];
  if(t[i]<k)seen.add(t[i]);
 }
 return z+rankP(u,a);
}
function unrank(z,c){
 const {m,k,L,w,short,total}=c;
 if(z<0n||z>=total)throw Error("range");
 if(z<short){
  let h=0,p=1n;while(z>=p){z-=p;p*=BigInt(m);h++}
  let t=Array(h).fill(0);for(let i=h-1;i>=0;i--){t[i]=Number(z%BigInt(m));z/=BigInt(m)}return [last(t,k),t];
 }
 z-=short;let t=[],seen=new Set();
 for(let i=0;i<L;i++){
  let x=-1;for(let a=0;a<m;a++){let b=w[L-i-1][seen.size+(a<k&&!seen.has(a)?1:0)];if(z<b){x=a;break}z-=b}
  if(x<0)throw Error("tail decode");
  t.push(x);if(x<k)seen.add(x);
 }
 let v=last(t,k),a=Array.from({length:k},(_,i)=>i).filter(x=>!seen.has(x));
 return [unrankP(z,a).concat(v),t];
}
function* tails(m,h,t=[]){if(t.length===h){yield t;return}for(let x=0;x<m;x++)yield* tails(m,h,t.concat(x))}
function* partial(a,p=[]){yield p;for(let i=0;i<a.length;i++)yield* partial(a.filter((_,j)=>j!==i),p.concat(a[i]))}
function* states(m,k,L){
 for(let h=0;h<L;h++)for(let t of tails(m,h))yield [last(t,k),t];
 for(let t of tails(m,L)){let v=last(t,k),a=Array.from({length:k},(_,i)=>i).filter(x=>!v.includes(x));for(let u of partial(a))yield [u.concat(v),t]}
}
function run(){
 let combos=0,checks=0;
 for(let m=1;m<=5;m++)for(let k=0;k<=Math.min(m,4);k++)for(let L=0;L<=3;L++){
  let c=prep(m,k,L),seen=new Set(),count=0n;
  for(let [s,t] of states(m,k,L)){let z=rank(s,t,c),[u,v]=unrank(z,c);if(s.join()!=u.join()||t.join()!=v.join()||seen.has(String(z)))throw Error("mismatch "+[m,k,L,z]);seen.add(String(z));count++}
  if(count!==c.total||count!==BigInt(seen.size))throw Error("cardinality "+[m,k,L,count,c.total]);
  checks+=Number(count);combos++;
 }
 let c1=prep(12,6,1),full=0;
 for(let [s,t] of states(12,6,1)){let [u,v]=unrank(rank(s,t,c1),c1);if(s.join()!=u.join()||t.join()!=v.join())throw Error("X6");full++}
 if(BigInt(full)!==c1.total)throw Error("X6 count");
 let seed=199n,samples=0;
 for(let L=2;L<=4;L++){let c=prep(12,6,L),rhs=c.short;for(let j=0;j<=6;j++)rhs+=P(6,j)*BigInt(12-j)**BigInt(L);if(rhs!==c.total)throw Error("R198 formula");
  for(let i=0;i<3500;i++){seed=(seed*6364136223846793005n+1442695040888963407n)&((1n<<64n)-1n);let z=seed%c.total,[s,t]=unrank(z,c);if(rank(s,t,c)!==z)throw Error("sample");samples++}
 }
 return {schema:"R199_EXACT_COMBINATORIAL_RANK_V1",status:"PASS",scientific_input_pin:"43ec6098b1330ae86d0a7863be336c5d97f6ef34",source:"R198@89e25b035a6bffc2c05eeea5316571b534b9c874",backend:"standalone JS BigInt exact combinatorial encoding",parameter_combinations:combos,exhaustive_roundtrips:checks,X6_m12_k6_L1_exhaustive_roundtrips:full,X6_m12_k6_L2_to_L4_samples:samples,resource_rows:Array.from({length:5},(_,L)=>{let c=prep(12,6,L);return {m:12,k:6,L,states:String(c.total),bits:(c.total-1n).toString(2).length}}),independent_review:"NOT_REVIEWED",native_BRC_integration:"NOT_EXECUTED"};
}
console.log(JSON.stringify(run(),null,2));
