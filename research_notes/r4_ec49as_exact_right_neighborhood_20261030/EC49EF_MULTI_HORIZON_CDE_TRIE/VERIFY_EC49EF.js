// EC49EF exact independent checker, native six-axis signed primitive paths.
// Node.js standard runtime only.
const ops={c:[1,2,-1,-2],d:[2,1,-2,-1],e:[3,1,1,-3]};
const atoms=['N0','N1','N2','A0','A2','B0','B1','AB','BA'];
function test(v,s){if(!v)throw Error(s)}
function native(w){return [...w].flatMap(ch=>ops[ch])}
function label(seq,s='N',prev=0){
 for(const k of seq){const a=prev===1&&k===2,b=prev===2&&k===1;
 if(s==='N')s=a?'A':b?'B':s;else if(s==='A'&&b)s='AB';else if(s==='B'&&a)s='BA';prev=k}return s
}
function atom(p){let s=label(p),z=p.at(-1);return s==='N'?(z===1?'N1':z===2?'N2':'N0'):s==='A'?(z===2?'A2':'A0'):s==='B'?(z===1?'B1':'B0'):s}
function histories(){
 let f={},p=[],freq=[[-2,2],[-1,4],[1,2],[2,2]];
 function visit(){if(Object.keys(f).length===9)return;if(p.length===10){let a=atom(p);if(!f[a])f[a]=p.slice();return}
 for(let x of freq){if(!x[1])continue;x[1]--;p.push(x[0]);visit();p.pop();x[1]++;if(Object.keys(f).length===9)return}}
 visit();test(atoms.every(a=>f[a]),'historical atoms absent');return atoms.map(a=>f[a])
}
function pos(p){return Array.from({length:6},(_,i)=>p.filter(s=>s===i+1).length)}
function displacement(p){return Array.from({length:6},(_,i)=>p.filter(s=>Math.abs(s)===i+1).reduce((v,s)=>v+(s>0?1:-1),0))}
function sig(w,h){let p=native(w);test(displacement(p).join()==='2,0,0,0,0,0','bad return');return h.map(a=>label(p,label(a),a.at(-1)))}
function col(s,b){return s.reduce((v,x,i)=>v+(x===b?(1<<i):0),0)}
function det(c){
 let a=Array.from({length:9},(_,i)=>c.map(x=>BigInt((x>>i)&1))),last=1n,sign=1n;
 for(let k=0;k<8;k++){if(!a[k][k]){let j=k+1;while(j<9&&!a[j][k])j++;if(j===9)return 0n;[a[k],a[j]]=[a[j],a[k]];sign=-sign}
 let q=a[k][k];for(let i=k+1;i<9;i++){for(let j=k+1;j<9;j++){let v=a[i][j]*q-a[i][k]*a[k][j];test(v%last===0n,'bareiss');a[i][j]=v/last}a[i][k]=0n}last=q}
 return sign*a[8][8]
}
function rank(c){
 let p=1000003,a=Array.from({length:9},(_,i)=>c.map(v=>(v>>i)&1)),r=0;
 for(let j=0;j<c.length&&r<9;j++){let k=r;while(k<9&&!a[k][j])k++;if(k===9)continue;[a[k],a[r]]=[a[r],a[k]];
 let power=(x,n)=>{let z=1;for(;n;n=Math.floor(n/2),x=x*x%p)if(n%2)z=z*x%p;return z};
 let inv=power(a[r][j],p-2);for(let l=j;l<c.length;l++)a[r][l]=a[r][l]*inv%p;
 for(let i=r+1;i<9;i++){let q=a[i][j];if(q)for(let l=j;l<c.length;l++)a[i][l]=(a[i][l]-q*a[r][l]%p+p)%p}r++}
 return r
}
function W(h){return ['e'+'c'.repeat(h-1),'e'+'d'.repeat(h-1),'c'+'e'+'c'.repeat(h-2),'d'+'e'+'d'.repeat(h-2)]}
function witness(h,paths){let [C,D,c,d]=W(h).map(w=>sig(w,paths));return [col(C,'A'),col(C,'AB'),col(C,'BA'),col(D,'B'),col(D,'AB'),col(c,'A'),col(c,'AB'),col(d,'B'),col(d,'AB')]}
function trie(ws){let s=new Set();for(let w of ws){let p=native(w);for(let i=1;i<=p.length;i++)s.add(p.slice(0,i).join(','))}return s.size}
function opts(h){let z=[];for(let a=1;a<h;a++)for(let b=1;b<h;b++)z.push(['e'+'c'.repeat(h-1),'e'+'d'.repeat(h-1),'c'.repeat(a)+'e'+'c'.repeat(h-1-a),'d'.repeat(b)+'e'+'d'.repeat(h-1-b)]);return z}
function BRC(seq,x){return pos(seq).reduce((v,n,i)=>v*BigInt(x[i])**BigInt(n),1n)}
function main(){
 const paths=histories(),sample=[[2,3,5,7,11,13],[3,4,7,11,13,17]],rows=[];
 for(const p of paths)test(p.length===10&&displacement(p).join()==='-2,0,0,0,0,0'&&pos(p).join()==='2,2,0,0,0,0','native historical path invalid');
 for(let H=2;H<=10;H++){let ws=[],largest=W(H);
 for(let h=2;h<=H;h++){let w=W(h),c=witness(h,paths);
 test(det(c)===-1n&&rank(c)===9,'unimodular rank');
 for(let i=0;i<4;i++)test(largest[i].startsWith(w[i]),'not literally prefix nested');
 for(const s of w){let p=native(s);test(p.length===4*h&&displacement(p).join()==='2,0,0,0,0,0','native steps');
 test(pos(p).join()===[h+1,h-1,1,0,0,0].join(),'BRC positive counts');
 for(const q of paths)for(const x of sample)test(BRC(q.concat(p),x)===BRC(q,x)*BRC(p,x),'BRC composition')}
 ws.push(...w)}
 let u=trie(ws),independent=8*H*H+4*H-12;test(u===16*H-4&&u===trie(largest),'union cost');
 rows.push({H,U:u,independent,saved:independent-u,terminal_rank:9,minor:-1})}
 const exhaustive=[];for(let H=3;H<=5;H++){
 let families=Array.from({length:H-1},(_,i)=>opts(i+2)),count=0,best=Infinity,winners=0;
 function visit(i,ws){if(i===families.length){let k=trie(ws);count++;if(k<best){best=k;winners=1}else if(k===best)winners++;return}for(const w of families[i])visit(i+1,ws.concat(w))}
 visit(0,[]);test(best===16*H-4,'representative search');exhaustive.push({H,count,best,winners})}
 return {status:'PASS',model:'genuine signed native X6, dual positive BRC, nine A/B-first history atoms',
 frozen_pins:{global:'773d538180bfb49e24cffeb35c3ee75eb0628e2e',em:'fc0f038e7bfd12c886b4d37f900bfb770c0f61ab'},
 original_histories:paths,windows:rows,exhaustive_representative_choices:exhaustive,
 theorem:'U_cde(H)=U_cde_equal(H)=16H-4 for all integers H>=2',proof_scope:'analytic four compulsory transfer classes and nested witness; finite arithmetic H<=10',
 rank_arithmetic:'BigInt integer Bareiss determinant; mod 1000003 exact by Hadamard bound for 9-row 0/1 minors'};
}
if(typeof module!=='undefined'&&module.exports)module.exports=main;
