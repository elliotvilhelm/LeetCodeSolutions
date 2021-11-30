import scala.annotation.tailrec

object Solution {
  def searchInsert(nums: Array[Int], target: Int): Int = {
    @tailrec
    def binarySearch(start: Int, end: Int): Int = {
      if (start > end) start
      else {
        val pivot: Int = start + (end - start) / 2
        if (nums(pivot) == target) pivot
        else if (target > nums(pivot)) binarySearch(pivot + 1, end)
        else binarySearch(start, pivot - 1)
      }
    }
    binarySearch(0, nums.length-1)
  }
}