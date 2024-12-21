def find_deleted_number(arr, mixed_arr):
    sum_starting = sum(arr)
    sum_mixed = sum(mixed_arr)
    return sum_starting - sum_mixed
    