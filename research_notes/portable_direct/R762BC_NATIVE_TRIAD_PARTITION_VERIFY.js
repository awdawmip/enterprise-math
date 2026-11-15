"use strict";
// Exact BigInt independent exhaustive checker for R762BC. Node.js standard runtime.
const result=(function verifyR762BC(){
 const check=(ok,msg)=>{if(!ok)throw Error(msg)};
 const triples=[];for(let i=0;i<6;i++)for(let j=i+1;j<6;j++)for(let k=j+1;k<6;k++)triples.push([i,j,k]);
 const factorial=[1n];for(let j=1;j<=12;j++)factorial[j]=factorial[j-1]*BigInt(j);
 const encode=x=>x.join(",");
 const layers=[new Map([[encode([0,0,0,0,0,0]),1n]])];
 for(let n=1;n<=4;n++){let next=new Map();for(let [str,co] of layers[n-1]){let v=str.split(",").map(Number);for(let t of triples){let w=v.slice();for(let k of t)w[k]++;let s=encode(w);next.set(s,(next.get(s)||0n)+co)}}layers.push(next)}
 const B=(v,n)=>{let coeff=layers[n].get(encode(v))||0n;let num=coeff*v.reduce((p,c)=>p*factorial[c],1n);check(num%factorial[n]===0n,"noninteger "+v);return num/factorial[n]};
 function patterns(n){let ans=[];function walk(v,remaining){if(v.length===5){ans.push([...v,remaining]);return}for(let x=0;x<=remaining;x++)walk([...v,x],remaining-x)}walk([],3*n);return ans}
 function enumerate(type,paired=null){const N=type.length,used=Array(N).fill(false);function rec(remaining){
    if(!remaining)return 1n;
    const i=used.indexOf(false);used[i]=true;let count=0n;
    for(let j=i+1;j<N;j++){if(used[j]||type[i]===type[j])continue;used[j]=true;
      for(let k=j+1;k<N;k++){if(used[k]||type[k]===type[i]||type[k]===type[j])continue;
        if(paired){const a=[i,j,k].includes(paired[0]),b=[i,j,k].includes(paired[1]);if(a!==b)continue}
        used[k]=true;count+=rec(remaining-3);used[k]=false
      }used[j]=false
    }used[i]=false;return count
   }return rec(N)}
 const summary=[],examples={}, stats={exhaustive_partition_profiles:0,exhaustive_named_pair_lift_checks:0,infeasible_profiles:0,saturated_axis_checks:0,rotation_coefficient_checks:0};
 for(let n=0;n<=4;n++){let feasible=0,total=0,max=0n;
   for(let v of patterns(n)){
     const x=B(v,n);total++;if(x>0n)feasible++;if(x>max)max=x;
     check((x>0n)===v.every(q=>q<=n),"existence "+n+" "+v);
     if(n<=3){const types=v.flatMap((c,i)=>Array(c).fill(i));
       check(enumerate(types)===x,"partition brute mismatch "+v);
       stats.exhaustive_partition_profiles++;if(!x)stats.infeasible_profiles++;
       const first=v.map((c,i)=>c>0?types.indexOf(i):-1);
       for(let a=0;a<6;a++)for(let b=a+1;b<6;b++){
         if(first[a]<0||first[b]<0)continue;
         let predicted=0n, allowed=[];
         for(let k=0;k<6;k++){
           if(k===a||k===b||v[k]===0)continue;
           const residue=v.map((c,i)=>c-(i===a?1:0)-(i===b?1:0)-(i===k?1:0));
           const completions=B(residue,n-1);
           predicted+=BigInt(v[k])*completions;
           if(completions)allowed.push(k);
         }
         const actual=enumerate(types,[first[a],first[b]]);
         check(predicted===actual,"pair lift mismatch "+v+" "+a+","+b);
         stats.exhaustive_named_pair_lift_checks++;
         if(n===2&&encode(v)==="2,1,1,1,1,0"&&a===2&&b===3)
           examples.resource_forced_hidden_axis={counts:v,observed_axes:[a,b],allowed_third_axes:allowed,compatible_full_partitions:predicted.toString()};
         if(n===2&&encode(v)==="2,2,1,1,0,0"&&a===2&&b===3)
           examples.obstructed_pair_lift={counts:v,observed_axes:[a,b],allowed_third_axes:allowed,compatible_full_partitions:predicted.toString()};
       }
     }
     if(n>0&&v.filter(q=>q===n).length>=2){check(x===factorial[n]**2n,"saturated law "+v);stats.saturated_axis_checks++}
     if((n===2&&encode(v)==="1,1,1,1,1,1")||(n===2&&encode(v)==="2,2,2,0,0,0")||(n===3&&encode(v)==="3,3,3,0,0,0"))
       examples["distribution_"+encode(v)]={counts:v,partition_count:x.toString()};
   }
   summary.push({n,all_axis_count_profiles:total,feasible_count_profiles:feasible,max_labelled_BRC_partitions:max.toString()})
 }
 function permutations(xs){if(xs.length<2)return [xs];return xs.flatMap((x,i)=>permutations(xs.filter((_,j)=>i!==j)).map(t=>[x,...t]))}
 for(const p of permutations([0,1,2,3,4,5]))for(let [str,coeff] of layers[4]){
   let v=str.split(",").map(Number),rot=Array(6).fill(0);for(let i=0;i<6;i++)rot[p[i]]=v[i];
   check(layers[4].get(encode(rot))===coeff,"S6 covariance "+str);
   stats.rotation_coefficient_checks++;
 }
 check(examples.resource_forced_hidden_axis.allowed_third_axes.join(",")==="0","forced third");
 check(examples.obstructed_pair_lift.allowed_third_axes.length===0,"obstructed");
 return {schema:"R762BC_TRIAD_PARTITION_LIFT_EVIDENCE_V1",date:"2026-11-15",inputs:"signed X6 Cell incidence; six unsigned native axis labels; equal quantum weights; distinct names; each triad uses 3 distinct axes",status:"ALL_ASSERTIONS_PASS",algorithm:"exact BigInt elementary symmetric polynomial coefficient + independent named-partition recursion; exhaustive named-pair completion",proof_horizon:"all n >= 0 by combinatorial induction; finite tests n <= 4; direct independent n <= 3",stats,summary,examples};
})();
console.log(JSON.stringify(result,null,2));
