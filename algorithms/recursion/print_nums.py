def print_nums(a):
    # Prints all integers from an array consisting of integers & sub-arrays of integers of any depth.
    for element in a:
        if isinstance(element, int):
            print(element)
        else:
            print_nums(element)


if __name__ == "__main__":
    arr = [
        1,
        2,
        3,
        [4, 5, 6],
        7,
        [8,
         [9, 10, 11,
          [12, 13, 14]
          ]
         ],
        [15, 16, 17, 18, 19,
         [20, 21, 22,
          [23, 24, 25,
           [26, 27, 28]
           ], 29, 30
          ], 31
         ], 32
    ]
    print_nums(arr)
