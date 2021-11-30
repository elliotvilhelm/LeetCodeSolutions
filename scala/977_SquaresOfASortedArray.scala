object Solution {
  def sortedSquares(nums: Array[Int]): Array[Int] = {
    val result: Array[Int] = new Array[Int](nums.length)

    var left = 0
    var right = result.length - 1
    var walker = result.length - 1

    while (left <= right) {
      var abs_left = nums(left).abs
      var abs_right = nums(right).abs

      if (abs_left > abs_right) {
        result(walker) = abs_left * abs_left
        left += 1
        walker -= 1
      } else {
        result(walker) = abs_right * abs_right
        right -= 1
        walker -=1
      }
    }
    result
  }
}