#include <algorithm>
#include <array>
#include <bit>
#include <cstdint>
#include <iostream>
#include <numeric>
#include <vector>
using namespace std;using W=uint64_t;
array<array<int,4>,625> xyz;
bool forbidden(int a,int b,int c){unsigned sep=0;for(int i=0;i<4;i++){int x=xyz[a][i],y=xyz[b][i],z=xyz[c][i];if(x==y&&z!=x)sep|=4;if(y==z&&x!=y)sep|=1;if(x==z&&y!=x)sep|=2;}return popcount(sep)>1;}
struct Search{
 int target,threshold;W bad[64][64]{};long long visits=0;vector<W> rows,path;vector<int>by[64];
 void generate(W row,W free,const array<W,64>& banned,int depth){
 if(depth>=threshold){int j=rows.size();rows.push_back(row);for(W r=row;r;r&=r-1)by[countr_zero(r)].push_back(j);}
 if(depth==12)return;
 while(free&&depth+popcount(free)>=threshold){int x=countr_zero(free);free&=free-1;
  W available=free&~banned[x];array<W,64>updated;
  for(W v=available;v;v&=v-1){int j=countr_zero(v);updated[j]=banned[j]|bad[x][j];}
  generate(row|(W(1)<<x),available,updated,depth+1);}
 }
 bool cover(W free,int slots){
 ++visits;if(!slots)return !free;if(!free)return false;int minsize=max(threshold,popcount(free)-12*(slots-1));
 vector<int>best;
 for(W v=free;v;v&=v-1){int x=countr_zero(v);vector<int>opt;
 for(int j:by[x]){W r=rows[j];if(!(r&~free)&&popcount(r)>=minsize){opt.push_back(j);if(!best.empty()&&opt.size()>=best.size())break;}}
 if(opt.empty())return false;if(best.empty()||opt.size()<best.size())best.swap(opt);}
 for(int j:best){W m=rows[j];path.push_back(m);if(cover(free^m,slots-1))return true;path.pop_back();}return false;}
};
int main(){
 for(int i=0;i<625;i++){int x=i;for(int j=3;j>=0;j--){xyz[i][j]=x%5;x/=5;}}
 int id,k,n;while(cin>>id>>k>>n){vector<int>q(n);for(int&i:q)cin>>i;if(n>=64)return 1;Search s;s.threshold=n-12*(k-1);if(s.threshold<1)return 2;
 for(int a=0;a<n;a++)for(int b=0;b<a;b++)for(int c=0;c<b;c++)if(forbidden(q[a],q[b],q[c])){
 s.bad[a][b]|=W(1)<<c;s.bad[a][c]|=W(1)<<b;s.bad[b][c]|=W(1)<<a;s.bad[b][a]|=W(1)<<c;s.bad[c][a]|=W(1)<<b;s.bad[c][b]|=W(1)<<a;}
 W full=(W(1)<<n)-1;s.generate(0,full,array<W,64>{},0);bool yes=s.cover(full,k);cout<<id<<" "<<s.rows.size()<<" "<<s.visits<<" "<<yes;
 if(yes)for(W m:s.path)cout<<" "<<m;cout<<endl;}
}
