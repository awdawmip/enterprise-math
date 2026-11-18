// PREFIX-908: complete exact integer verifier for the declared j=0, (k,ell)=(2,1) family.
// Node.js, no dependencies. Run: node PREFIX908_R6_LOW_BIT_MIXED_PARITY_CHECK.js
// All quantities in this program are safe integers (maximum product < 2^53).
function gcd(a,b){while(b){const t=a%b;a=b;b=t;}return a;}
function compute(){
 const N=2**32,T=33*N,L=262145,H=524287,QP=131072;
 const old=new Set();
 for(let h=1;h<=17;h++)old.add(2**h);
 for(let i=2;i<=17;i++)for(let j=1;j<i;j++){old.add(2**i+2**j);old.add(2**i-2**j);}
 const g905=new Set();
 for(let m=3;m<=8191;m+=2)for(let i=2;i<=17;i++)for(let j=1;j<i;j++)for(const s of [-1,1]){
  const v=2**i+s*2**j;
  if(v%m===0){const d=v/m;if(d>0&&d<=H-L&&d%2===0&&!old.has(d))g905.add(d);}
 }
 const g906=new Set();
 for(let m=1;m<=8191;m+=2)for(let i=18;i<=30;i++)for(let j=1;j<=17;j++)for(const s of [-1,1]){
  const v=2**i+s*2**j;
  if(v%m===0){const d=v/m;if(d>0&&d<=H-L&&d%2===0&&!old.has(d)&&!g905.has(d))g906.add(d);}
 }
 const U=new Set([262147,280001,300001,320003,340007,360007,380003,400009,420001,440003,460001,480007,500383,510007,520001,524285]);
 for(let q=400011;q<=400521;q+=2)U.add(q);
 for(let q=480011;q<=480521;q+=2)U.add(q);
 for(let q=L;q<=H;q+=2)for(let h=1;h<32;h++)if((2**h-1)%q===0||(2**h+1)%q===0){U.add(q);break;}
 const P=new Set();for(let j=0;j<64;j++)for(const k of [1,3,5])P.add(510000+k+194*j);
 const D907=new Set();for(let i=18;i<=22;i++)for(let j=1;j<=17;j++)for(const s of [-1,1])D907.add(2**i+s*2**j);
 const D908=new Map();for(let i=1;i<=19;i++)for(const s of [-1,1]){const d=2**i+s;if(!D908.has(d))D908.set(d,{i,s});}
 const prev=(a,b)=>{
  if(a*b<T||U.has(a)||U.has(b)||a/gcd(a,b)*b<N||
   33*Math.floor((N+a-1)/a)>b||33*Math.floor((N+b-1)/b)>a||P.has(a)||P.has(b))return true;
  const d=Math.abs(a-b);return old.has(d)||g905.has(d)||g906.has(d);
 };
 const old907=(a,b)=>prev(a,b)||D907.has(3*a-b)||D907.has(3*b-a);
 const encode=(a,b)=>((a-L)/2)*QP+(b-L)/2;
 let raw=0,base=0,overlap907=0,formula=0,checked=0;
 const novel=new Set(),full=new Set();
 for(const [d,{i,s}] of D908.entries()){
  const lo0=Math.max(L,Math.ceil((L+d)/2)),hi0=Math.min(H,Math.floor((H+d)/2));
  const low=lo0+(lo0%2===0?1:0),high=hi0-(hi0%2===0?1:0);
  if(low<=high)formula+=1+(high-low)/2;
  for(let a=low;a<=high;a+=2){
   const b=2*a-d,Hbit=2**i,x=(s===1?1:0),y=x+2*a,u=x+Hbit,v=y-s;
   if(!(b>=L&&b<=H&&b%2===1&&x>=0&&x<N&&y<N&&u<N&&v>=0&&v<N&&
     (x^Hbit)===u&&(y^1)===v&&(y-x)%a===0&&(v-u)%b===0))
       throw Error("invalid named XOR witness for "+a+","+b);
   const code=encode(a,b);
   if(full.has(code))throw Error("duplicate d / parameter pair");
   full.add(code);raw++;checked++;
   if(prev(a,b))base++;
   else if(old907(a,b))overlap907++;
   else novel.add(code);
  }
 }
 const reverse=(c)=>(c%QP)*QP+Math.floor(c/QP);
 let rawReverseIntersection=0,novelReverseIntersection=0;
 for(const c of full)if(full.has(reverse(c)))rawReverseIntersection++;
 for(const c of novel)if(novel.has(reverse(c)))novelReverseIntersection++;
 const delta=2*novel.size-novelReverseIntersection;
 const result={
  schema:"PREFIX908_R6_LOW_BIT_MIXED_PARITY_EXACT_UNION_V1",
  date:"2026-11-18",frozen_scientific_pin:"f42f2906d77f24085c123f3ccfe9667d41caa96d",
  model:{p:32,N,strict_odd_19bit_moduli:[L,H],q_size:QP,observer:"(start mod a, end mod b); retain named XOR sources"},
  new_family:"2a-b=2^i+s, i=1..19, s=+1/-1; source j=0",
  prior_union:"C907 explicit exact union including E, panel, three gap sets and 3a-b=2^i +/- 2^j (18<=i<=22,1<=j<=17) with transposition",
  old_class_sizes:{old_gap_classes:old.size,g905_gap_classes:g905.size,g906_gap_classes:g906.size,special_moduli:U.size,panel_moduli:P.size,D907_values:D907.size},
  exact:{D908_values:D908.size,raw_oriented_pairs:raw,analytic_raw_count:formula,old_C906_oriented_overlap:base,additional_C907_oriented_overlap:overlap907,novel_oriented:novel.size,raw_reverse_intersection:rawReverseIntersection,novel_reverse_intersection:novelReverseIntersection,new_distinct_ordered_pairs:delta,prior_C907:7778425088,certified_C908:7778425088+delta,uncovered_by_explicit_C908:QP**2-7778425088-delta,witnesses_verified:checked},
  example:{a:500001,b:475713,k:2,ell:1,i:19,j:0,s:1,start1:1,end1:524289,start2:1000003,end2:1000002},
  status:"AUTHOR_PROVED / EXACT_INTEGER_FINITE_CHECKED / INDEPENDENT_PYTHON_RECOUNT / NOT_INDEPENDENTLY_REVIEWED / NOT_ADMITTED",
  limitation:"Certificate union only. Current P000 and frozen source unchanged. No native Task CLAIM or Result admission."
 };
 const e=result.exact;
 if(old.size!==258||g905.size!==276||g906.size!==857||U.size!==552||P.size!==192||D907.size!==169||D908.size!==37||
 e.raw_oriented_pairs!==393214||e.analytic_raw_count!==393214||e.old_C906_oriented_overlap!==208655||
 e.additional_C907_oriented_overlap!==9||e.novel_oriented!==184550||e.raw_reverse_intersection!==6||
 e.novel_reverse_intersection!==0||e.new_distinct_ordered_pairs!==369100||e.certified_C908!==7778794188||
 e.uncovered_by_explicit_C908!==9401074996||e.witnesses_verified!==393214)
 throw Error("exact census mismatch: "+JSON.stringify(result));
 return result;
}
console.log(JSON.stringify(compute(),null,2));
