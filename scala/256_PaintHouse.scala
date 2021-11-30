object Solution {
  var memo: Array[Array[Int]] = null;

  def minCost(costs: Array[Array[Int]]): Int = {
    memo = Array.fill(100,20)(-1)
    findMin(costs, -1, -1)
  }

  def findMin(costs: Array[Array[Int]], i: Int, c: Int): Int = {
    if (i != -1 && c != -1)
      if (memo(i)(c) != -1)
        return memo(i)(c)

    if (i == costs.length-1) {
      return costs(i)(c)
    } else {
      val tmp = c match {
        case 0 => (findMin(costs, i+1, 1) + costs(i)(c)) min (findMin(costs, i+1, 2) + costs(i)(c))
        case 1 => (findMin(costs, i+1, 0) + costs(i)(c)) min (findMin(costs, i+1, 2) + costs(i)(c))
        case 2 => (findMin(costs, i+1, 0) + costs(i)(c)) min (findMin(costs, i+1, 1) + costs(i)(c))
        case _ => findMin(costs, i+1, 0) min findMin(costs, i+1, 1) min findMin(costs, i+1, 2)
      }

      if (i != -1 && c != -1)
        memo(i)(c) = tmp

      return tmp
    }
  }
}