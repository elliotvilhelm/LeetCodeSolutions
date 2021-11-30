object Solution {
  var fibT: Array[Int] = new Array[Int](40)
  fibT(0) = 0
  fibT(1) = 1
  def fib(n: Int): Int = {
    if (n == 0)
      return 0
    else if(n == 1)
      return 1
    else {
      for (i <- 2 to n) {
        fibT(i) = fibT(i-1) + fibT(i-2)
      }
      return fibT(n)
    }
  }
}