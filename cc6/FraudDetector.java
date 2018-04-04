
import java.util.*;
import java.util.stream.Collectors;


public class FraudDetector {



    /**
     Individual transactions exceeding $50,000
     Pawn shops, casinos and resorts
     Transactions whose value is unusually "round" (i.e. evenly divisible by $100)
     */
//    private static ArrayList<Transaction> findFraud(ArrayList<Transaction> transactions){
//        ArrayList<Transaction> posFraud = new ArrayList<>();
//
//        for (Transaction t : transactions){
//            if(t.getAmount() > 50000 || t.getAmount() % 100 == 0 || t.getMCC().contains("pawn") || t.getMCC().contains("casino")){
//                posFraud.add(t);
//            }
//
//
//        }
//
//        return  posFraud;
//    }

    private static ArrayList<Transaction> groupedFraud(ArrayList<Transaction> transactions){

        ArrayList<Transaction> posFraud = new ArrayList<>();

        Map<String, List<Transaction>> hmap = transactions.stream().collect(Collectors.groupingBy(w -> w.getCardholder()));

        for (String name: hmap.keySet()){

            /*the easy things to flag */
            for (Transaction t : hmap.get(name)){
                if(t.getAmount() > 50000 || t.getAmount() % 100 == 0 || t.getMCC().contains("pawn") || t.getMCC().contains("casino")){
                    posFraud.add(t);
                }
            }

            /* grouping by dates*/
            List<Transaction> hmapVal = hmap.get(name);
            Map<Date, List<Transaction>> inhmap = hmapVal.stream().collect(Collectors.groupingBy(w -> w.getDate() ));
            for (Date day : inhmap.keySet()){
                List<Transaction> inhampVal = inhmap.get(day);
                ArrayList<Transaction> copy = new ArrayList<>(inhampVal);
                copy.removeIf(s -> s.getAmount() <= 20000);
                if (copy.size() > 2){
                    posFraud.addAll(copy);
                }
            }
        }


        /* grouping by airline */
        transactions.removeIf(t -> (!t.getMCC().contains("airline")));

        Map<String, List<Transaction>> airlineMap = transactions.stream().collect(Collectors.groupingBy(w -> w.getMCC()));


        for (String airline : airlineMap.keySet()){
            if (airlineMap.get(airline).size() < 10){
                posFraud.addAll(airlineMap.get(airline));
                System.out.println(airline);
            }
        }





        return posFraud;


    }


    public static void main(String[] args) {
        ArrayList<Transaction> fraudChecklist = new FormTransaction(args[0]).getTransactions();




//        findFraud(fraudChecklist);

        System.out.println(groupedFraud(fraudChecklist));

//        for (Transaction t: fraudChecklist){
//            System.out.println(t);
//        }
}





}
