def times_table(number, rows):
    """print the times table for the given number."""
    for i in range(1, rows + 1):
        print(f"{number} x {i} = {number * i}")

table_number = float(input('which times table do you want to see : '))
total_rows = int(input('how many row do you want to print : '))

times_table(table_number, total_rows)