import java.util.Scanner

class Main 
{
    public static void main(String[])
    {
        char operator;
        Double number1, number2, result;

        //create scanner
        Scanner input = new Scanner(System.in);

        //Ask for user Input
        System.out.println("Choose an operator: 1 - Addition, 2 - Subtraction, 3 - Multiplication, 4 - Division");
        operator = input.next().charAt(0);

        //Get numbers
        System.out.println("Enter first number");
        number1 = input.nextDouble();

        System.out.println("Enter second number");
        number2 = input.nextDouble();

        switch (operator)
        {

            case '1':
            result = number1 + number2;
            System.out.println(number1 + "+" + number2 + "=" + result);
            break;

            case '2':
            result = number1 - number2;
            System.out.println(number1 + "-" + number2 + "=" + result);
            break;

            case '3':
            result = number1 * number2;
            System.out.println(number1 + "*" + number2 + "=" + result);
            break;

            case '4':
            result = number1 / number2;
            System.out.println(number1 + "/" + number2 + "=" + result);
            break;

            default:
            System.out.println("Invalid Operator");
            break;
        }
        input.close();
    }
}