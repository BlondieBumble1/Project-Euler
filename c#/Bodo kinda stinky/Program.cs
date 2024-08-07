class Program{
    static void Main(){
        int place = BinarySeach();
        string result = (place == -1) ? "The target is not in the list" : $"The target is in position {place} in the list.";
        Console.WriteLine(result);
    }
    static int BinarySeach(){
        int[] list;
        int target;
        int left;
        int right;
        int mid;
        list = (int[])GenerateList();
        Array.Sort(list);
        target = Convert.ToInt32(Console.ReadLine());
        left = 0;
        right = list.Length - 1;
        while(left <= right){
            mid = (left + right) / 2;
            if (list[mid] == target){
                return mid;
            }
            else if (list[mid] < target){
                left = mid + 1;
            }
            else{
                right = mid - 1;
            }
    }
    return -1;
    }
    static Array GenerateList(){
        Console.WriteLine("whats the smallest number in your list?");
        int minNum = Convert.ToInt32(Console.ReadLine());
        Console.WriteLine("whats the largest number in your list?");
        int maxNum = Convert.ToInt32(Console.ReadLine());
        Random rand = new();
        int[] list = new int[10];
        for(int i = 0; i < list.Length; i++){
            list[i] = rand.Next(minNum, maxNum);
        }
        return list;
    }
}