#include <algorithm>
#include <cstdint>
#include <iostream>
#include <vector>
#include <array>
using namespace std;
using Mask=uint32_t;using Score=std::array<uint64_t,4>;
constexpr Mask whole=(Mask(1)<<29)-1;
Mask forbidden[29][29];Score scores[29][29];struct Class{Mask m;int n,c;};vector<Class>rows;
int pop(Mask m){return __builtin_popcount(m);}
int low(Mask m){return __builtin_ctz(m);}
int cost(Mask m){int c=0;for(Mask p=m;p;p&=p-1){Score sum{};for(Mask q=m;q;q&=q-1)for(int j=0;j<4;j++)sum[j]|=scores[low(p)][low(q)][j];for(auto x:sum)c+=__builtin_popcountll(x);}return c;}
bool legal(Mask m){for(Mask p=m;p;p&=p-1)for(Mask q=p&(p-1);q;q&=q-1)if(forbidden[low(p)][low(q)]&m)return false;return true;}
int minimum=100000,maximum=0;long long ncovers;
void go(Mask free,int k,const vector<int>&opts,Mask last,int fee){
 int n=pop(free),upper=pop(last);
 if(n<k||n>k*upper)return;
 if(k==1){if(n==upper&&free<=last)return;if(!legal(free))return;++ncovers;fee+=cost(free);minimum=min(minimum,fee);maximum=max(maximum,fee);return;}
 auto step=[&](Mask m,int c,vector<int>const&next){go(free^m,k-1,next,m,fee+c);};
 int need=(n+k-1)/k;
 for(int i=0;i<opts.size();i++){
  auto row=rows[opts[i]];if(row.n<need)break;
  vector<int>next;
  if(k>2)for(int j=i+1;j<opts.size();j++)if(!(row.m&rows[opts[j]].m))next.push_back(opts[j]);
  step(row.m,row.c,next);
 }
 if(need<7)for(Mask m=free;m;m=(m-1)&free){
  int sz=pop(m);if(sz<need||sz>=7||sz>upper||(sz==upper&&m<=last)||!legal(m))continue;
  step(m,cost(m),{});
 }
}
int main(){
 for(int i=0;i<29;i++)for(int j=0;j<29;j++){
  cin>>forbidden[i][j];for(auto &t:scores[i][j])cin>>t;
 }
 Mask m;int c;while(cin>>m>>c)rows.push_back({m,pop(m),c});
 sort(rows.begin(),rows.end(),[](const Class&a,const Class&b){return a.n>b.n||(a.n==b.n&&a.m<b.m);});
 vector<int>ids;for(int i=0;i<rows.size();i++)ids.push_back(i);
 go(whole,4,ids,~Mask(0),0);cout<<ncovers<<" "<<minimum<<" "<<maximum<<endl;
}
