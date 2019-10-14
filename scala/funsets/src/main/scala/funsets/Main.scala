package funsets

object Main extends App {
  import FunSets._
  println(contains(singletonSet(1), 1))
  printSet(union(Set(1,2,3), Set(4,3,5)))
  printSet(intersect(Set(1,2,3), Set(4,3,5)))
  printSet(diff(Set(1,2,3), Set(4,3,5)))
  printSet(filter(Set(1,2,3), x => x > 1))
  printSet(map(Set(1,2,3,500), x =>  3))
}
