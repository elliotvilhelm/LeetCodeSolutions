import scala.annotation.tailrec

object Solution {
  def search(nums: Array[Int], target: Int): Int = {
    findMin(nums, target, 0, nums.length-1)
  }

  @tailrec
  def findMin(nums: Array[Int], target: Int, start: Int, end: Int): Int = {
    val pivot = start + (end - start) / 2
    println(s"start: $start end: $end pivot: $pivot")
    if (start > end) {
      -1
    } else if (nums(pivot) == target) {
      pivot
    } else if (target < nums(pivot)) {
      findMin(nums, target, start, pivot - 1)
    } else {
      findMin(nums, target, pivot + 1, end)
    }
  }
}