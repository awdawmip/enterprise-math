/* R696 exact positive-BRC E* static binary-port group-observer certificate.
 * R692C group counts and R695b independent static port candidate; not native V29/V39 permission.
 * Execute: node R696_BINARY_PORT_TOMOGRAPHY_VERIFY.js
 */
const r696 = function certificateR696() {
 const K=[[6,9,0,0],[6,6,3,0],[6,3,0,6],[6,0,3,6]],N=[24,18,6,12];
 function gcd(a,b){while(b){let t=a%b;a=b;b=t}return a}
 function gr(v){return v.reduce((a,b)=>gcd(a,b),0)}
 function mu(d){let x=d,k=0;for(let p=2;p*p<=x;p++){if(x%p===0){x/=p;k++;if(x%p===0)return 0;while(x%p===0)x/=p}}if(x>1)k++;return k%2?-1:1}
 let rows={0:[[1,0,0,0],1]};
 for(let m=1;m<=15;m++){let c=[0,0,0,0];for(let j=0;j<4;j++)if((m>>j)&1)for(let i=0;i<4;i++)c[i]+=K[j][i];rows[m]=[[c[0],c[1],c[3],c[2]],c.reduce((a,b)=>a+b,0)]}
 function sig(v,m){let [w,d]=rows[m],num=v.reduce((a,b,i)=>a+b*w[i],0),den=d*v.reduce((a,b)=>a+b,0),g=gcd(num,den);return num/g+"/"+den/g}
 let raw=0,vs=[],seen=new Set();
 for(let e=0;e<=24;e++)for(let t=0;t<=18;t++)for(let c=0;c<=6;c++)for(let z=0;z<=12;z++){
   let v=[e,t,c,z],g=gr(v);if(!g)continue;raw++;let u=v.map(x=>x/g),key=u.join(",");
   if(!seen.has(key)){seen.add(key);vs.push(u)}
 }
 vs.sort((a,b)=>a.reduce((x,y)=>x+y,0)-b.reduce((x,y)=>x+y,0)||a[0]-b[0]||a[1]-b[1]||a[2]-b[2]||a[3]-b[3]);
 let mobius=0;for(let d=1;d<=24;d++)mobius+=mu(d)*(N.reduce((a,n)=>a*(Math.floor(n/d)+1),1)-1);
 if(raw!==43224||vs.length!==38618||mobius!==38618)throw Error("primitive count");
 for(let v of vs){let r=v[0],x=v[1],y=v[2],len=v.reduce((a,b)=>a+b,0);let [R1,D1]=rows[1],[R4,D4]=rows[4];let n1=v.reduce((a,b,i)=>a+b*R1[i],0),n4=v.reduce((a,b,i)=>a+b*R4[i],0);if(n1!==6*r+9*x||n4!==6*r+3*x+6*y||D1!==15||D4!==15)throw Error("three-test inversion")}
 const small=vs.filter(v=>v.reduce((a,b)=>a+b,0)<=8);
 let wit=[],max=0,best=[],selected={};
 for(let p=0;p<16;p++)for(let q=p+1;q<16;q++){
  let known=new Map(),collision=null;
  for(let v of small){let a=sig(v,p),b=sig(v,q),key=a+"|"+b;if(known.has(key)){let prev=known.get(key);if(prev.join()!=v.join()){collision={tests:[p,q],left:prev,right:v,same:[a,b]};break}}else known.set(key,v)}
  if(!collision)throw Error("two-test collision missing "+p+","+q);
  wit.push(collision);
  let signatures=new Set();for(let v of vs)signatures.add(sig(v,p)+"|"+sig(v,q));
  if(signatures.size>max){max=signatures.size;best=[[p,q]]}else if(signatures.size===max)best.push([p,q]);
  if((p===1&&q===4)||(p===3&&q===14))selected[p+","+q]=signatures.size;
 }
 if(max!==38159||JSON.stringify(best)!=="[[3,14]]"||wit.length!==120||selected["1,4"]!==16924)throw Error("two-test maxima");
 let deleted=N.map((_,j)=>N.map((x,i)=>x-(i===j?1:0)));
 let gapmax=0,bestMasks=[],classes=[];
 for(let m=1;m<=15;m++){
   let vals=deleted.map(v=>sig(v,m));
   let asNum=vals.map(s=>s.split("/").map(Number)).sort((a,b)=>a[0]/a[1]-b[0]/b[1]);
   if(new Set(vals).size!==4)continue;
   let gaps=[];
   for(let i=1;i<4;i++){let a=asNum[i],b=asNum[i-1];gaps.push((a[0]*b[1]-b[0]*a[1])/(a[1]*b[1]))}
   let min=Math.min(...gaps);
   if(min>gapmax+1e-16){gapmax=min;bestMasks=[m]}else if(Math.abs(min-gapmax)<1e-16)bestMasks.push(m);
   classes.push({mask:m,returns:vals,minimum_gap:Number(min.toPrecision(14))})
 }
 if(JSON.stringify(bestMasks)!=="[3,6,9,15]"||Math.abs(gapmax-1/590)>1e-16)throw Error("singleton mask tests");
 let l=[0,2,2,0],rr=[3,0,0,1];
 if(sig(l,1)!=="3/10"||sig(l,4)!=="3/10"||sig(rr,1)!=="3/10"||sig(rr,4)!=="3/10"||sig(l,0)!=="0/1"||sig(rr,0)!=="3/4")throw Error("explicit collision");
 return {schema:"EM_R696_ESTAR_STATIC_BINARY_PORT_TOMOGRAPHY_V1",status:"R696_ALL_EXACT_ASSERTIONS_PASS",numeric_semantics:"Integer/reduced-rational exact tests. Only ranking finite suffix gap uses Number; crosschecked with separate Python Fraction program.",frozen_model_source:"R692C at 3dacca5010104893d96301af4d61608d5a5a0879",static_port_candidate_source:"R695b at c7f1f35e69dc4c7525ccedd33cf52a9534ecb1a8",group_bins:N,direction_rows:K,nonzero_port_fields:"1152921504606846975",group_histogram_count:raw,distinct_normalized_group_kernels:vs.length,mobius_count:mobius,available_scalar_observer_count:16,two_test_designs:120,each_pair_has_exact_collision:true,two_test_witnesses:wit,max_two_test_signature_count:max,best_pair:best,selected_pair_counts:selected,optimal_one_suffix_min_gap:"1/590",optimal_single_deletion_masks:bestMasks,single_deletion_probe_classes:classes,one_explicit_collision:{left:l,right:rr,same_T1:"3/10",same_T4:"3/10",T0_left:"0/1",T0_right:"3/4"},three_test_exact_reconstruction:"[T0,T1,T4]; x=(5*T1-2*T0)/3, y=(5*T4-2*T0-x)/2, z=1-T0-x-y",scope:"E* candidate independent static ports and external suffix selection; not proven native V29/V39 authorisation or original path-ID tomography"};
};
const result = r696();
console.log(JSON.stringify(result,null,2));
