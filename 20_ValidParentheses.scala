import scala.collection.mutable.Stack

object Solution {
  def isValid(s: String): Boolean = {

    var myStack: Stack[Char] = Stack[Char]()

    for (i <- s) {
      if (i == '(' || i == '{' || i == '[') {
        myStack.push(i)
      } else {
        if (myStack.isEmpty)
          return false
        val top = myStack.pop()
        if (i == ')' && top != '(')
          return false
        else if (i == ']' && top != '[')
          return false
        else if (i == '}' && top != '{')
          return false
      }
    }
    myStack.isEmpty
  }
}