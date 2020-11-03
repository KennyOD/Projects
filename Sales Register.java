package Assignments;

import java.util.ArrayList;
import java.util.Scanner;

class Garments{
    private int i = 0;
    private Scanner insert = new Scanner(System.in);
    private String ID;
    private ArrayList<String> type = new ArrayList<>();
    private ArrayList<Integer> stock = new ArrayList<>();
    private ArrayList<Integer> price = new ArrayList<>();
    private int orderQty;
    int sales;

    Garments(String a){
        ID = a;
    }
    void addGarments(){
        System.out.println("What garment would you like to add?");
        String t = insert.next();
        type.add(i,t);
        System.out.println("How much of it is in stock?");
        int s = insert.nextInt();
        stock.add(i,s);
        System.out.println("What is the price tag on the garment?");
        int p = insert.nextInt();
        price.add(i,p);
        System.out.println("Selections saved!");
        i++;
    }
    void showDetails(){
        System.out.println("What garment would you like to see?");
        String x = insert.next();
        if(type.indexOf(x) == -1){
            System.out.println("Sorry, this garment does not exist!!!");
        }else{
            System.out.println("Section: "+ID.toUpperCase());
            System.out.println("Item name: "+type.get(type.indexOf(x)).substring(0,1).toUpperCase()+type.get(type.indexOf(x)).substring(1).toLowerCase());
            // This long thing you're seeing here breaks the String using the index to capitalize the first word and adds the rest of the word in lower case.
            System.out.println("Number in stock: "+stock.get(type.indexOf(x)));
            System.out.println("Price: $"+price.get(type.indexOf(x)));
        }
    }
    int setOrder(){
        System.out.println("What garment would you like to order?");
        String o = insert.next();
        if(type.indexOf(o) == -1){
            System.out.println("Sorry, this garment does not exist!!!");
            if(stock.get(type.indexOf(o)) == 0){
                System.out.println("This garment is out of stock!!!");
            }
        }else{
            System.out.println("And how much of this would you like to order");
            orderQty = insert.nextInt();
            if(stock.get(type.indexOf(o)) > orderQty){
                System.out.println("Order received!!!");
            }else{
                System.out.println("Number in stock not enough for order");
                orderQty = 0;
            }
        }
        return orderQty*price.get(type.indexOf(o));
        }
    }

public class Arrays_Strings {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        String ask, g, shift;
        Garments[] one = {
            new Garments("Children"),
            new Garments("Women"),
            new Garments("Men"),
        };

        System.out.println("Welcome to Fashionista Garment Store");
        System.out.println("Are you an employee or a customer or would you like to leave?");
        label:
        do{
            ask = input.next();
            switch (ask) {
                case "employee":
                    System.out.println("What collection would you like to add garments to?");
                    loop:
                    do {
                        g = input.next();
                        if (g.equals("children")) {
                            loop2:
                            do {
                                one[0].addGarments();
                                System.out.println("Would you like to add more?");
                                shift = input.next();
                                if (shift.equals("yes")) {
                                } else if (shift.equals("no")) {
                                    System.out.println("Section closed. Returning to the main section...");
                                    break;
                                } else {
                                    System.out.println("Wrong option detected...");
                                    continue loop2;
                                }
                            } while (shift.equals("yes"));
                        } else if (g.equals("women")) {
                            loop2:
                            do {
                                one[1].addGarments();
                                System.out.println("Would you like to add more?");
                                shift = input.next();
                                if (shift.equals("yes")) {
                                    continue loop2;
                                } else if (shift.equals("no")) {
                                    System.out.println("Section closed. Returning to the main section...");
                                    break;
                                } else {
                                    System.out.println("Wrong option detected...");
                                    continue loop2;
                                }
                            } while (shift.equals("yes"));
                        } else if (g.equals("men")) {
                            loop2:
                            do {
                                one[2].addGarments();
                                System.out.println("Would you like to add more?");
                                shift = input.next();
                                if (shift.equals("yes")) {
                                    continue loop2;
                                } else if (shift.equals("no")) {
                                    System.out.println("Section closed. Returning to the main section...");
                                    break;
                                } else {
                                    System.out.println("Wrong option detected...");
                                    continue loop2;
                                }
                            } while (shift.equals("yes"));
                        } else if (g.equals("exit")) {
                            System.out.println("Leaving the employee menu...");
                            break loop;
                        } else {
                            System.out.println("Wrong option detected... Try again");
                        }
                    } while (!(g.equals("exit")));
                    break;
                case "customer":
                    System.out.println("Would you like to view garments or order some?");
                    String o = input.next();
                    if (o.equals("view")) {
                        System.out.println("What collection would you like to view?");
                        loop:
                        do {
                            g = input.next();
                            if (g.equals("children")) {
                                loop2:
                                do {
                                    one[0].showDetails();
                                    System.out.println("Would you like to view more?");
                                    shift = input.next();
                                    if (shift.equals("yes")) {
                                        continue loop2;
                                    } else if (shift.equals("no")) {
                                        System.out.println("Section closed. Returning to the main section...");
                                        break;
                                    } else {
                                        System.out.println("Wrong option detected...");
                                        continue loop2;
                                    }
                                } while (shift.equals("yes"));
                            } else if (g.equals("women")) {
                                loop2:
                                do {
                                    one[1].showDetails();
                                    System.out.println("Would you like to view more?");
                                    shift = input.next();
                                    if (shift.equals("yes")) {
                                        continue loop2;
                                    } else if (shift.equals("no")) {
                                        System.out.println("Section closed. Returning to the main section...");
                                        break;
                                    } else {
                                        System.out.println("Wrong option detected...");
                                        continue loop2;
                                    }
                                } while (shift.equals("yes"));
                            } else if (g.equals("men")) {
                                loop2:
                                do {
                                    one[2].showDetails();
                                    System.out.println("Would you like to view more?");
                                    shift = input.next();
                                    if (shift.equals("yes")) {
                                        continue loop2;
                                    } else if (shift.equals("no")) {
                                        System.out.println("Section closed. Returning to the main section...");
                                        break;
                                    } else {
                                        System.out.println("Wrong option detected...");
                                        continue loop2;
                                    }
                                } while (shift.equals("yes"));
                            } else if (g.equals("exit")) {
                                System.out.println("Leaving the viewing section...");
                                break loop;
                            } else {
                                System.out.println("Wrong option detected... Try again");
                            }
                        } while (!(g.equals("exit")));
                    } else if (o.equals("order")) {
                        System.out.println("What collection would you like to order from?");
                        loop:
                        do {
                            g = input.next();
                            if (g.equals("children")) {
                                loop2:
                                do {
                                    one[0].sales += one[0].setOrder();
                                    System.out.println("Would you like to buy more?");
                                    shift = input.next();
                                    if (shift.equals("yes")) {
                                        continue loop2;
                                    } else if (shift.equals("no")) {
                                        System.out.println("Section closed. Returning to the main section...");
                                        break;
                                    } else {
                                        System.out.println("Wrong option detected...");
                                        continue loop2;
                                    }
                                } while (shift.equals("yes"));
                            } else if (g.equals("women")) {
                                loop2:
                                do {
                                    one[1].sales += one[1].setOrder();
                                    System.out.println("Would you like to buy more?");
                                    shift = input.next();
                                    if (shift.equals("yes")) {
                                        continue loop2;
                                    } else if (shift.equals("no")) {
                                        System.out.println("Section closed. Returning to the main sectcuion...");
                                        break;
                                    } else {
                                        System.out.println("Wrong option detected...");
                                        continue loop2;
                                    }
                                } while (shift.equals("yes"));
                            } else if (g.equals("men")) {
                                loop2:
                                do {
                                    one[2].sales += one[2].setOrder();
                                    System.out.println("Would you like to buy more?");
                                    shift = input.next();
                                    if (shift.equals("yes")) {
                                        continue loop2;
                                    } else if (shift.equals("no")) {
                                        System.out.println("Section closed. Returning to the main section...");
                                        break;
                                    } else {
                                        System.out.println("Wrong option detected...");
                                        continue loop2;
                                    }
                                } while (shift.equals("yes"));
                            } else if (g.equals("exit")) {
                                System.out.println("Leaving the buying section...");
                                break loop;
                            } else {
                                System.out.println("Wrong option detected... Try again");
                            }
                        } while (!(g.equals("exit")));
                    }
                    break;
                case "exit":
                    int sales = one[0].sales + one[1].sales + one[2].sales;
                    if (sales > 0) {
                        System.out.println("Your total bill is $" + sales + ". Thank you for shopping with Fashionista Garment Store");
                    } else {
                        System.out.println("Thank you. Have a great day!");
                        break label;
                    }
                    break;
                default:
                    System.out.println("Pick among the listed options!!!");
                    break;
            }
        }while (!(ask.equals("exit")));
    }
    }

