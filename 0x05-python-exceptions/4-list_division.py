def list_division(my_list_1, my_list_2, list_length):
    return [
        (lambda x, y: x / y if y != 0 else (print("division by 0"), 0)[1]
         if isinstance(x, (int, float))
         and isinstance(y, (int, float))
         else (print("wrong type"), 0)[1]
         if isinstance(x, (int, float))
         else (print("out of range"), 0)[1])(
            my_list_1[i] if i < len(my_list_1) else 0,
            my_list_2[i] if i < len(my_list_2) and my_list_2[i] != 0 else 1,
        )
        for i in range(list_length)
    ]
