object Solution {

  var table: Array[Int] = new Array[Int](40)
  table(0) = 0
  table(1) = 1
  table(2) = 1

  def tribonacci(n: Int): Int = {
    if (n < 3)
      return table(n)

    for (i <- 3 to n) {
      table(i) = table(i-1) + table(i-2) + table(i-3)
    }
    return table(n)
  }
}