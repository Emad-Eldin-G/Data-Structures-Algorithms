import java.util.Scanner;

public class Main {
    public static int binarySearch(int[] arr, int start, int end, int target) {
        int bsMid = ((start + end) / 2);

        if (start>=end){
            return (-1);
        }
        if (arr[bsMid] == target) {
            return target;
        } else if (arr[bsMid] > target) {
            return binarySearch(arr, start, bsMid - 1, target);
        } else {
            return binarySearch(arr, bsMid + 1, end, target);
        }
    }

    public static void main(String[] args) {
        int[] arr1 = {1,2,3,4,5,6,7,8,9};
        int arrMid = arr1.length / 2;
        System.out.print(binarySearch(arr1, 0, arr1.length, 2));
        }
    }
