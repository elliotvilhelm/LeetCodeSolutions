import scala.collection.mutable.ListBuffer


object Solution {
  def findMissingRanges(nums: Array[Int], lower: Int, upper: Int): List[String] = {
    val missing = ListBuffer[String]();

    if (nums.length == 0) {
      if (lower == upper)
        missing += s"$upper"
      else
        missing += s"$lower->$upper"

      return missing.to(List)
    }

    if (nums.length == 1) {
      if (lower == upper - 1) {
        if (lower == nums(0))
          missing += upper.toString
        else if (upper == nums(0))
          missing += lower.toString
      } else if (lower == upper - 2) {
        if (nums(0) == lower) {
          missing += (lower + 1).toString
          missing += upper.toString
        } else if (nums(0) == lower +1) {
          missing += lower.toString
          missing += upper.toString
        } else if (nums(0) == lower + 2) {
          missing += lower.toString
          missing += (lower + 1).toString
        }
      } else if (lower != upper) {
        if (nums(0) >= lower + 2) {
          missing += s"$lower->${nums(0)-1}"
        } else if (nums(0) != lower) {
          missing += lower.toString
        }

        if (nums(0) <= upper -2 ) {
          missing += s"${nums(0)+1}->$upper"
        } else if (nums(0) != upper) {
          missing += upper.toString
        }
      }
      return missing.to(List)
    }

    if (nums(0) == lower + 1) {
      missing += lower.toString
    } else if (nums(0) >= lower + 2) {
      missing += s"$lower->${nums(0)-1}"
    }

    for (i <- 0 to nums.length-2) {
      if (nums(i+1) != nums(i) + 1) {
        if (nums(i) + 2 == nums(i+1)) {
          missing += s"${nums(i)+1}"
        } else {
          missing += s"${nums(i)+1}->${nums(i+1)-1}"
        }
      }
    }

    if (nums.length == 0) {
      if (lower == upper)
        missing += s"$upper"
      else
        missing += s"$lower->$upper"
    } else if (nums(nums.length-1) != upper) {
      if (upper == nums(nums.length-1) + 1) {
        missing += upper.toString
      } else {
        missing += s"${nums(nums.length-1)+1}->${upper}"
      }
    }

    missing.to(List)
  }
}