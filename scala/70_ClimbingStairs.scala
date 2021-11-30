object Solution {
  def climbStairs(n: Int): Int = {
    if (n <= 0)
      return 0
    // 1 = 1
    // 2 = 2
    // 3 = 3
    // 4 = 5
    // nw(i) = nw(i-1)
    val ndw: Array[Int] = new Array[Int](256)
    ndw(0) = 0
    ndw(1) = 1
    ndw(2) = 2
    for (i <- 3 to n) {
      ndw(i) = ndw(i-1) + ndw(i-2)
    }
    ndw(n)
  }
}