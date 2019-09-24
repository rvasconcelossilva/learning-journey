package recfun

object Main {

  def main(args: Array[String]): Unit = {

    println("Pascal's Triangle")
    for (row <- 0 to 10) {
      for (col <- 0 to row)
        print(pascal(col, row) + " ")
      println()
    }

  }

  /**
   * Exercise 1
   */

    def pascal(c: Int, r: Int): Int = {
      if(c == 0 || c==r)
        1
      else
        pascal(c-1, r-1) + pascal(c, r-1)
    }
  
  /**
   * Exercise 2
   */
    def balance(chars: List[Char]): Boolean = {
      def checkParentheses(chars: List[Char], numOpenPar: Int): Boolean =
      {
        if(chars.isEmpty){
          numOpenPar == 0
        }
        else {
          val first = chars.head

          val aux = if( first == '(' ) numOpenPar + 1
                    else if( first == ')' ) numOpenPar - 1
                    else numOpenPar

            if(aux >= 0) checkParentheses(chars.tail, aux)
            else  false
        }
      }
      checkParentheses(chars,0)
    }

   /**
   * Exercise 3
   */

    def countChange(money: Int, coins: List[Int]): Int = {

      var totalAmount = 0;

      def check(money: Int, coins: List[Int]) {
        if (!coins.isEmpty)
          if (money>coins.head) {
            check(money-coins.head, coins)
            check(money,coins.tail)
          }
          else if (money<coins.head) {
            check(money,coins.tail)
          }
          else if (money-coins.head == 0) {
            totalAmount += 1
          }
      }

      check(money,coins.sorted)
      totalAmount
    }
  }
