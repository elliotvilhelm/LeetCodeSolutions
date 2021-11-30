import scala.annotation.tailrec

class Solution extends VersionControl {
  def firstBadVersion(n: Int): Int = {
    @tailrec
    def findBad(start: Int, end: Int, firstBad: Int): Int = {
      val pivot: Int = start + (end - start) / 2
      if (start > end) firstBad
      else if (isBadVersion(pivot)) findBad(start, pivot-1, pivot)
      else findBad(pivot+1, end, firstBad)
    }
    findBad(0, n, 0)
  }
}