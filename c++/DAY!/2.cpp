#include <iostream>
using namespace std;

int main(){
    int arr[]={12,23,45,12,00};
    int n=sizeof(arr) / sizeof(arr[0]);

    int highest=0;

    for(int i=0;i<n;i++){
        if(arr[i]>highest){
            highest=arr[i];

        }    }

    cout<<"highest"<<highest;

    return 0;
}