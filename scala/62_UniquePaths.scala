object Solution {
  def uniquePaths(m: Int, n: Int): Int = {


    val dp: Array[Array[Int]] = Array.ofDim(m+1, n+1)
    dp(1)(1) = 0
    // robot starts at 1,1
    for (i <- 1 to m) {
      dp(i)(1) = 1
    }

    for (i <- 1 to n) {
      dp(1)(i) = 1
    }
    for (i <- 2 to m) {
      for (j <- 2 to n) {
        // you can get to the i,j square from
        // above (m-1)
        // the left (n-1)
        dp(i)(j) = dp(i-1)(j) + dp(i)(j-1)
      }
    }
    dp(m)(n)
  }
}