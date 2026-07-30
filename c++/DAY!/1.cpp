#include <iostream>
using namespace std;

int main(){
    int nums[]={1,2,3,4,5,6,7};

    int n=sizeof(nums)/sizeof(nums[0]);
    int sum=0;

    for(int i=0;i<n;i++){
        sum=sum+nums[i];
    }
    cout<<"sums:"<<sum;
}