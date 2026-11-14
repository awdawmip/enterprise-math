'use strict';
// Independently check a concrete H8, M3, S6 witness in the frozen symbolic native-X6 model.
const A={a:[-1,-1],b:[-2,-2],c:[1,2,-1,-2],d:[2,1,-2,-1],e:[3,1,1,-3],f:[1,-1],g:[2,-2]};
const hist=[['N',0],['N',1],['N',2],['A',0],['A',2],['B',0],['B',1],['AB',0],['BA',0]];
const buckets=['N','A','B','AB','BA'];const P=1000003;
const witness={
2:['ce','de','ec','ed'],
3:['feg','gef'],
4:['fegd','gefd','gefc','fegc'],
5:['fegfg','geffg'],
6:['fegdgd','gefdgd','gefcgc','fegcgc'],
7:['fegdggf','gefdggf','gefcgfg','fegcgfg'],
8:['fegfgfgg','geffgfgg']};
const check=(cond,msg)=>{if(!cond)throw Error(msg)};
const path=w=>[...w].flatMap(k=>A[k]);
const vec=s=>Array.from({length:6},(_,j)=>s.filter(t=>t===j+1).length-s.filter(t=>t===-j-1).length);
const key=s=>Array.from({length:6},(_,j)=>s.filter(t=>t===j+1).length).join(',');
function signature(s){return hist.map(([h0,p0])=>{let h=h0,p=p0;for(const t of s){if(p===1&&t===2){if(h==='N')h='A';else if(h==='B')h='BA'}else if(p===2&&t===1){if(h==='N')h='B';else if(h==='A')h='AB'}p=t;}return buckets.indexOf(h)})}
function power(a,n){let v=1;while(n){if(n%2)v=v*a%P;a=a*a%P;n=Math.floor(n/2)}return v}
function rank(sigs){let cs=sigs.flatMap(s=>buckets.map((_,b)=>s.map(v=>v===b?1:0)));
let M=Array.from({length:9},(_,i)=>cs.map(c=>c[i]));let r=0;
for(let j=0;j<cs.length&&r<9;j++){let i=r;while(i<9&&!M[i][j])i++;if(i===9)continue;
[M[r],M[i]]=[M[i],M[r]];let iv=power(M[r][j],P-2);
for(let k=j;k<cs.length;k++)M[r][k]=M[r][k]*iv%P;
for(let x=r+1;x<9;x++){let v=M[x][j];for(let k=j;k<cs.length;k++)M[x][k]=(M[x][k]-v*M[r][k]%P+P)%P;}r++;}return r;}
const all=new Set(),keys=new Set(),sigs=new Set(),rows=[];
for(let h=2;h<=8;h++){
const W=witness[h],kset=new Set(),sset=new Map();
for(const w of W){check(w.length===h,'operation horizon mismatch');const st=path(w);
check(vec(st).join(',')==='2,0,0,0,0,0','X6 return fails: '+w);
kset.add(key(st));const sg=signature(st);sset.set(sg.join(','),sg);sigs.add(sg.join(','));
for(let i=1;i<=st.length;i++)all.add(st.slice(0,i).join(','));}
check(kset.size===1,'within-h key split');let r=rank([...sset.values()]);check(r===9,'rank fails');let k=[...kset][0];keys.add(k);rows.push({h,count:W.length,key:k,signature_count:sset.size,rank:r});}
const result={status:'PASS',unit:'EC49EXF',E:all.size,M:keys.size,S:sigs.size,horizon_rows:rows,operation_words:witness};
check([result.E,result.M,result.S].join(',')==='112,3,6','witness resources differ');
console.log(JSON.stringify(result,null,2));
