object BinSearch
{ 
    // tests to come
    def main(args: Array[String]) {
    { 
    }

    def binary_search(arr: List[Int], left: Int, right: Int, x: Int): Int =
    {
        if(left <= right){
            val mid = left + (right - left)/2
            if(arr[mid] == x){
                return mid
            } else if(arr[mid] < x){
                return binary_search(arr, mid + 1, right, x)
            } else{
                return binary_search(arr, left, mid - 1, x)
            }
        } else{
            return -1
        }
    }
}