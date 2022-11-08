object Main {
  def main(args: Array[String]): Unit = {
    println("this program for partial applied functions !")

    import java.util.Date
    object Practise_2_11_2022 {
      def main(args: Array[String]): Unit = {

        //Tutorial Practise for 2/11/2022
        val age = "50";

        age match {
          //Can be used for text or number matching (e.g "50" or 50)
          case "20" => println(age);
          case "18" => println(age);
          case "30" => println(age);
          case "40" => println(age);
          case "50" => println(age);

          case _ => println("default");
        }

        val result = age match {
          case "20" => age;
          case "18" => age;
          case "30" => age;
          case "40" => age;
          case "50" => age;

          case _ => println("default");
        }

        println("result = " + result);

        //Another way of using match
        val i = 7
        i match {
          case 1 | 3 | 5 | 7 | 9 => println("odd");
          case 2 | 4 | 6 | 8 | 10 => println("even");
        }

        // different ways of writing functions
        object Math { //keep add and square function in an object Math
          //define function name by anonymous operator
          def +(x: Int = 45, y: Int = 15): Int = {
            return x + y;
          }

          def **(x: Int) = x * x;


          def add(x: Int = 45, y: Int = 15): Int = { //default value
            return x + y;
          }

          def square(x: Int) = x * x;
        }

        def add(x: Int, y: Int): Int = {
          return x + y;
        }

        def subtract(x: Int, y: Int): Int = {
          x - y;
        }

        def multiply(x: Int, y: Int): Int = x * y;

        def divide(x: Int, y: Int) = x / y;

        var add1 = (x: Int, y: Int) => x + y;

        def print(x: Int, y: Int): Unit = {
          println(x + y);
        }

        println("---------------Scala Functions---------------------------")
        println(Math.add(45, 15));
        println(Math.square(3)); // or println(Math square 3);
        println(add(45, 15));
        println(subtract(45, 15));
        println(multiply(45, 15));
        println(divide(45, 15));

        println("------Anonymous functions / Default values function---------")
        print(100, 200);
        println(Math.+(60, 15));
        println(Math ** 3); //or println(Math.**(3));
        println(add1(300, 500))


        //Higher-Order Functions - take functions as an argument and return functions as an output
        //third argument is a function that can take any operator e.g +, -, min,max etc
        def math(x: Double, y: Double, f: (Double, Double) => Double): Double = f(x, y);

        def math1(x: Double, y: Double, z: Double, f: (Double, Double) => Double): Double = f(f(x, y), z);

        println("------------Higher-Order Functions----------------------------")
        val output = math(50, 20, (x, y) => x + y); //third
        println(output);

        val output1 = math1(50, 20, 10, (x, y) => x min y); //third
        println(output1);

        val output2 = math1(50, 20, 10, _ max _); //using wildcard also _+_ (for +)
        println(output2);


        // Scala - Partially applied functions
        val sum = (a: Int, b: Int, c: Int) => a + b + c
        val f = sum(10, 20, _: Int);
        val h = sum(10, _: Int, _: Int);

        println("------------ Scala - Partially applied functions----------------------------")
        println(f(100));
        println(h(100, 200));

        val date = new Date;
        val newLog = log(date, _: String);
        newLog("The message 1");
        newLog("The message 2");
        newLog("The message 3");
        newLog("The message 4");


        //Closure : functions which uses one or more variables declared outside the functions
        var number = 10;
        val add2 = (x: Int) => {
          x + number;
        }

        println("------------ Closures----------------------------")
        number = 100;
        println(add2(20));
        println(number)


        //Currying : technique of transforming a function that takes multiple arguments into a functions that takes a single
        //argument
        def add3(x: Int, y: Int) = x + y

        def add4(x: Int) = (y: Int) => x + y;

        def add5(x: Int)(y: Int) = x + y;

        println("------------ Currying----------------------------")
        println(add3(20, 10));
        println(add4(20)(10));
        val sum40 = add4(40);
        println(sum40(100));
        println(add5(100)(200));
        val sum50 = add5(50) _; //use wildcard
        println(sum50(400))


      }

      // Scala - Partially applied functions-
      def log(date: Date, message: String) = {
        println(date + " " + message);
      }

    }



  }
}