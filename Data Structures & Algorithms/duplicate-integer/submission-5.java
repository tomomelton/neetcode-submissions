class Solution 
{
    public boolean hasDuplicate(int[] nums) 
    {
        HashMap<Integer, Integer> digitCount = new HashMap<Integer, Integer>();

        int count;

        for (int x : nums)
        {
            count = digitCount.getOrDefault(x, 0);

            count++;

            digitCount.put(x, count);

            if (count > 1)
            {
                return true;
            }
        }

        return false;
    }
}