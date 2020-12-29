//
//  main.c
//  test3
//
//  Created by 朱正阳 on 2019/4/8.
//  Copyright © 2019 朱正阳. All rights reserved.
//

#include <stdio.h>

//1.插入排序：直接插入与希尔排序
void insert_sort(int a[],int n){
    int i,j,temp;
    for(i=1;i<n;i++){
        temp=a[i];
        for(j=i;j>0&&a[j-1]>temp;j--){
            a[j]=a[j-1];
        }
        a[j] = temp;
    }
}
//直接插入排序，稳定

void shell_sort(int a[],int n){
    int i,j,temp,d;
    d = n/2;
    while(d>0){
        for(i=d;i<n;i++){
            temp=a[i];
            for(j=i;j>0&&a[j-d]>temp;j-=d)
                a[j]=a[j-d];
            a[j]=temp;
        }
        d/=2;
    }
}
//希尔排序，不稳定排序


//2.交换排序：冒泡和快速排序

void bubbleSort(int a[],int n){
    int i,j;
    for(i=n-1;i>0;i--){
        for(j=0;j<i;j++){
            if(a[j]>a[j+1]){
                int temp=a[j];
                a[j]=a[j+1];
                a[j+1]=temp;
            }
        }
    }
}
//冒泡排序，稳定

void quickSort(int a[],int low,int high){
    if (low>=high) return;
    int base=a[low],lowNext=low,highNext=high;
    while(low<high){
        while(a[high]>=base&&low<high) high--;
        a[low]=a[high];
        while(a[low]<=base&&low<high) low++;
        a[high]=a[low];
    }
    a[low]=base;
    quickSort(a,lowNext,low-1);
    quickSort(a,low+1,highNext);
}
//快速排序，不稳定（有些特殊情况稳定）

//3、选择排序：简单选择排序和堆排序
void selectSort(int a[],int n){
    int i,j,min;
    for(i=0;i<n;i++){
        min=i;
        for(j=i+1;j<n;j++){
            if(a[j]<a[min]) min=j;
        }
        if(min!=i){
            int temp=a[min];
            a[min]=a[i];
            a[i]=temp;
        }
    }
}
//简单选择排序，不稳定

//*************
//堆排序，不稳定

//4、归并排序，稳定
//5、基数排序，稳定



int main() {
    int arr[] = {3,45,23,101,56,24,45,78,13};
    selectSort(arr,9);
    for(int i=0;i<9;i++)
        printf ("%d ",arr[i]);
    printf("\n");
    return 1;
}
