object Main {
  def main(args: Array[String]): Unit = {
    println("Hello world!")

    val mytuple = (1, 2, "hello", true);
    val mytuple2 = new Tuple3(1, 2, "hello");
    val mytuple3 = new Tuple3(1, "hello", (2, 3));
    println(mytuple._1);
    println(mytuple._2);
    println(mytuple._3);
    println(mytuple._4);

    mytuple.productIterator.foreach {
      i => println(i);
    }
  }
}