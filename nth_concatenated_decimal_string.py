class Solution {
  public:
    char nthCharacter(long long n) {
        long long digits = 1, start = 1, count = 9;

        while (n > digits * count) {
            n -= digits * count;
            digits++;
            start *= 10;
            count *= 10;
        }

        long long num = start + (n - 1) / digits;
        int index = (n - 1) % digits;

        return to_string(num)[index];
    }
};
