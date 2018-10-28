class Main{
  public static void main(String [] args){
    int past = 1;
    int current = 2;
    int next = past + current;
    int sum = 0;
    
    while(current < 4000000){
      if(current % 2 == 0){
        sum += current;
      }
      past = current;
      current = next;
      next = past + current;
    }
    System.out.println(sum);
  }
}
