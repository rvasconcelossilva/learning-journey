package example


object Lists {

  /**
   * This method computes the sum of all elements in the list xs. There are
   * multiple techniques that can be used for implementing this method, and
   * you will learn during the class.
   *
   * For this example assignment you can use the following methods in class
   * `List`:
   *
   *  - `xs.isEmpty: Boolean` returns `true` if the list `xs` is empty
   *  - `xs.head: Int` returns the head element of the list `xs`. If the list
   *    is empty an exception is thrown
   *  - `xs.tail: List[Int]` returns the tail of the list `xs`, i.e. the the
   *    list `xs` without its `head` element
   *
   *  ''Hint:'' instead of writing a `for` or `while` loop, think of a recursive
   *  solution.
   *
   * @param xs A list of natural numbers
   * @return The sum of all elements in `xs`
   */
    def sum(xs: List[Int]): Int = {

        if (xs.size == xs.distinct.size) {
          if (xs.filter(_ < 0).isEmpty) {
            if (xs.sum != 0) {
              if (!xs.isEmpty) {
                xs.sum
              }
              else {
                throw new Exception("List is empty")
              }
            }
            else {
              throw new Exception("All elements of this list are zero")
            }
          }
          else {
            throw new Exception("There is at leas 1 negative value in the list")
          }
        }
        else {
          throw new Exception("There are duplicated elements in the list")
        }
    }


  /**
   * This method returns the largest element in a list of integers. If the
   * list `xs` is empty it throws a `java.util.NoSuchElementException`.
   *
   * You can use the same methods of the class `List` as mentioned above.
   *
   * ''Hint:'' Again, think of a recursive solution instead of using looping
   * constructs. You might need to define an auxiliary method.
   *
   * @param xs A list of natural numbers
   * @return The largest element in `xs`
   * @throws java.util.NoSuchElementException if `xs` is an empty list
   */
    def max(xs: List[Int]): Int = {

      if (xs.count(_ >= 0) == xs.distinct.count(_ >= 0)) {
        if (xs.filter(_ < 0).isEmpty) {
          if (xs.sum != 0) {
            if (!xs.isEmpty) {
              xs.max
            }
            else {
              throw new NoSuchElementException("List is empty")
            }
          }
          else {
            throw new NoSuchElementException("All elements of this list are zero")
          }
        }
        else {
          throw new NoSuchElementException("There is at leas 1 negative value in the list")
        }
      }
      else {
        throw new Exception("There are duplicated elements in the list")
      }
    }
  }
