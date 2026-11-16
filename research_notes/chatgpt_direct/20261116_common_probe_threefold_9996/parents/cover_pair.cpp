#include <algorithm>
#include <array>
#include <bit>
#include <cstdint>
#include <iostream>
#include <fstream>
#include <tuple>
#include <vector>
using namespace std;
using Mask=__uint128_t; using U=uint64_t;
constexpr int N=125, C=250;
int count(Mask m){return popcount(U(m))+popcount(U(m>>64));}
int bit(Mask m){return U(m)?countr_zero(U(m)):64+countr_zero(U(m>>64));}
array<Mask,C> parent;
array<vector<int>,N> through;
array<bool,C> banned{};
vector<int> current,solution;
long long nodes,leaves;int max_holes;
void search(Mask free,int ignored,int left){
 ++nodes;
 const int need=count(free)-(max_holes-ignored);
 if(need<=0){solution=current;++leaves;return;}
 if(!left||need>13*left)return;
 const int minimum=max(1,need-13*(left-1));
 array<int,C> gain{};array<int,14> histogram{};array<int,N> ways{};int options=0;
 for(int row=0;row<C;row++)if(!banned[row]){
   Mask cover=free&parent[row];int n=count(cover);if(n<minimum)continue;
   gain[row]=n;++histogram[n];++options;
 }
 if(!options)return;
 int sum=0,slots=left;
 for(int n=13;n>=minimum&&slots;n--){int take=min(slots,histogram[n]);sum+=take*n;slots-=take;}
 if(sum<need)return;
 // Remove gains that cannot form an adequate total with the best remaining left-1 rows.
 int quota=left-1,besides=0;
 for(int n=13;n>=minimum&&quota;n--){int take=min(quota,histogram[n]);besides+=take*n;quota-=take;}
 int limit=max(minimum,need-besides);
 Mask union_cand=0;
 for(int row=0;row<C;row++)if(gain[row]>=limit){
     union_cand|=parent[row];
     if(options<75)for(Mask m=parent[row]&free;m;m&=m-1)++ways[bit(m)];
 }
 Mask forced=free&~union_cand;
 if(ignored+count(forced)>max_holes)return;
 free^=forced;ignored+=count(forced);
 int pivot=-1,few=C;
 for(Mask m=free;m;m&=m-1){int p=bit(m);int n=ways[p];
   if(options>=75){for(int i:through[p])if(gain[i]>=limit && ++n>=few)break;}
   if(n<few){pivot=p;few=n;if(n==1)break;}
 }
 vector<int> opts;for(int i:through[pivot])if(gain[i]>=limit)opts.push_back(i);
 sort(opts.begin(),opts.end(),[&](int a,int b){return gain[a]!=gain[b]?gain[a]>gain[b]:a<b;});
 for(int i:opts){
   // Force the first selected candidate through this pivot. Earlier rivals stay excluded.
   banned[i]=true;current.push_back(i);search(free&~parent[i],ignored,left-1);current.pop_back();
   if(leaves)break;
 }
 if(!leaves&&ignored<max_holes)search(free^(Mask(1)<<pivot),ignored+1,left);
 for(int i:opts)banned[i]=false;
}
int main(int argc,char**argv){
 if(argc!=4)return 2;
 int k=stoi(argv[1]);max_holes=stoi(argv[2]);
 for(int i=0;i<C;i++){U lo,hi;if(!(cin>>lo>>hi))return 2;parent[i]=(Mask(hi)<<64)|lo;
 for(Mask m=parent[i];m;m&=m-1)through[bit(m)].push_back(i);}
 ifstream in(argv[3]);int j,n;long long total=0;
 while(in>>j>>n){banned.fill(true);for(int x=0,id;x<n;x++){in>>id;banned[id]=false;}
  current={0,j};banned[0]=banned[j]=true;nodes=0;search(((Mask(1)<<125)-1)&~(parent[0]|parent[j]),0,k-2);total+=nodes;
  cout<<j<<" "<<nodes<<" "<<leaves;for(int i:solution)cout<<" "<<i;cout<<endl;if(leaves)break;
 }
 cerr<<total<<endl;
}
