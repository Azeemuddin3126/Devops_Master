class Median:
    def calculate_median(self, *args):
        if not 2 <= len(args) <= 5:
            raise ValueError("This method accepts between 2 and 5 integers.")
        
        sorted_args = sorted(args)
        mid = len(sorted_args) // 2
        return sorted_args[mid] if len(sorted_args) % 2 == 1 else (sorted_args[mid - 1] + sorted_args[mid]) / 2.0

# Example usage
m = Median()
print(m.calculate_median(3, 5, 1, 4, 2))  # Output: 3
print(m.calculate_median(8, 6, 4, 2))     # Output: 5.0
print(m.calculate_median(9, 3, 7))        # Output: 7
print(m.calculate_median(5, 2))           # Output: 3.5
