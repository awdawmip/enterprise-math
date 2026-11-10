/* R697 exact native-BRC E* static binary port-count-conditional observer theorem.
 * Program is an independently runnable exact integer certificate.
 * Run: node R697_KNOWN_PORT_COUNT_VERIFY.js
 * Input: R696 at 0d0a7a3b1464685bfbdba48ea91c11943548b8eb, R692c at 3dacca5010104893d96301af4d61608d5a5a0879.
 */
const R697_exact_certificate=function R697_exact_certificate() {
  const N=[24,18,6,12];
  const K=[[6,9,0,0],[6,6,3,0],[6,3,0,6],[6,0,3,6]];
  const rows=[{w:[1,0,0,0],D:1}];
  for(let m=1;m<16;m++){
    let c=[0,0,0,0];
    for(let j=0;j<4;j++)if((m>>j)&1)for(let i=0;i<4;i++)c[i]+=K[j][i];
    rows.push({w:[c[0],c[1],c[3],c[2]],D:c.reduce((a,b)=>a+b,0)});
  }
  const dot=(a,b)=>a.reduce((x,t,i)=>x+t*b[i],0),sum=a=>a.reduce((x,y)=>x+y,0);
  const eq=(a,b)=>a.every((x,i)=>x===b[i]);
  if(!eq(rows[3].w,[12,15,0,3])||rows[3].D!==30||!eq(rows[8].w,[6,0,6,3])||rows[8].D!==15)throw Error("source row mismatch");
  const kernel=[3,-4,-7,8];
  if(sum(kernel)!==0||dot(rows[3].w,kernel)!==0||dot(rows[8].w,kernel)!==0)throw Error("kernel mismatch");
  let raw=0,byTotal=Array(61).fill(0),sigSets=Array.from({length:61},()=>new Set());
  for(let e=0;e<=24;e++)for(let t=0;t<=18;t++)for(let c=0;c<=6;c++)for(let z=0;z<=12;z++){
    const v=[e,t,c,z],s=e+t+c+z; if(!s)continue;
    raw++;byTotal[s]++;
    const n3=dot(rows[3].w,v),n8=dot(rows[8].w,v);
    if(n3%3||n8%3)throw Error("noninteger U,V");
    const U=n3/3,V=n8/3,A=U-s,B=V-s;
    const r=((2*(3*B-A))%7+7)%7;
    const tnew=(A-3*B+4*r)/7;
    if(!Number.isInteger(tnew))throw Error("reconstruction noninteger");
    const enew=tnew+B-r,znew=s-enew-tnew-r;
    if(!eq(v,[enew,tnew,r,znew]))throw Error("reconstruction failed");
    const sig=`${U},${V}`;
    if(sigSets[s].has(sig))throw Error("same-total two-probe collision");
    sigSets[s].add(sig);
  }
  if(raw!==43224||byTotal.reduce((a,b)=>a+b,0)!==raw)throw Error("population count");
  const d2=[];
  for(let i=0;i<4;i++)for(let j=i;j<4;j++){let d=[0,0,0,0];d[i]++;d[j]++;d2.push(d)}
  const singleProbeWitnesses=[];
  let paddedChecks=0;
  for(let m=0;m<16;m++){
    const seen=new Map();let hit=null;
    for(const d of d2){
      const key=dot(rows[m].w,d);
      if(seen.has(key)){hit={mask:m,left:seen.get(key),right:d,weighted_deleted_sum:key};break;}
      seen.set(key,d);
    }
    if(!hit)throw Error("single probe has no k=2 collision "+m);
    singleProbeWitnesses.push(hit);
    const a=hit.left,b=hit.right;
    const cap=N.map((Ni,i)=>Ni-Math.max(a[i],b[i]));
    if(sum(cap)<56)throw Error("paddability cap");
    for(let k=2;k<=58;k++){
      let rem=k-2;const h=cap.map(C=>{const x=Math.min(C,rem);rem-=x;return x});
      if(rem!==0)throw Error("padding unavailable");
      const left=N.map((Ni,i)=>Ni-a[i]-h[i]),right=N.map((Ni,i)=>Ni-b[i]-h[i]);
      if(eq(left,right)||sum(left)!==60-k||sum(right)!==60-k||dot(rows[m].w,left)!==dot(rows[m].w,right))throw Error("padded collision failed");
      paddedChecks++;
    }
  }
  if(paddedChecks!==912)throw Error("padded check count");
  // Four one-deletion histograms and four one-retained histograms are distinguished by mask 3.
  const singletonDelete=N.map((_,i)=>N.map((v,j)=>v-(i===j?1:0)));
  const singletonRemain=N.map((_,i)=>N.map((_,j)=>i===j?1:0));
  for(const group of [singletonDelete,singletonRemain]){
    if(new Set(group.map(v=>dot(rows[3].w,v))).size!==4)throw Error("one-probe boundary");
  }
  const classK2=rows.map(({w})=>new Set(d2.map(d=>dot(w,d))).size);
  if(Math.max(...classK2)!==9)throw Error("k2 single observer maximum");
  const widerL=[3,0,0,8],widerR=[0,4,7,0];
  if(!eq(widerL,widerR)&&sum(widerL)===sum(widerR)&&dot(rows[3].w,widerL)===dot(rows[3].w,widerR)&&dot(rows[8].w,widerL)===dot(rows[8].w,widerR)){}else throw Error("wider c>=7 sharpness witness");
  return {schema:"EM_R697_KNOWN_PORT_COUNT_TWO_PROBE_CERTIFICATE_V1",
    status:"R697_ALL_INTEGER_ASSERTIONS_PASS",input_source:{r696_commit:"0d0a7a3b1464685bfbdba48ea91c11943548b8eb",r692c_commit:"3dacca5010104893d96301af4d61608d5a5a0879"},
    scope:"E* candidate with static independent binary path ports, not V29/V39 native event authorization",
    group_capacities:N,scalar_probe_rows:{mask3:rows[3],mask8:rows[8]},
    kernel_direction:kernel,
    retained_count_side_information:"s=60-k, 1<=s<=60",
    exact_decoder:"U=10*s*T3,V=5*s*T8,A=U-s,B=V-s,c=(2*(3*B-A)) mod 7,t=(A-3*B+4*c)/7,e=t+B-c,z=s-e-t-c",
    nonzero_retained_count_histograms:raw,counts_by_retained_total:byTotal.slice(1),
    same_s_signatures_unique:true,integer_decoder_checks:raw,
    all_s_single_probe_collision_witnesses:singleProbeWitnesses,padded_single_probe_checks:paddedChecks,
    min_scalar_queries_given_exact_k:{k0:0,k1:1,k2_through_58:2,k59:1,k60:"undefined empty kernel"},
    classes_for_each_single_probe_at_two_deletions:classK2,
    mask3_singleton_extremes_pass:true,
    capacity_7_sharpness_example:{left:widerL,right:widerR,total:11,mask3_dot:dot(rows[3].w,widerL),mask8_dot:dot(rows[8].w,widerL)},
    arithmetic:"Exact integer enumeration, integer modular decoding, fixed finite complete witness family. No floating-point calculations.",
    result_scope:"known active-port count s is extra side information; individual path identity remains outside 4-bin group observer"};
};
const result=R697_exact_certificate();
console.log(JSON.stringify(result,null,2));
