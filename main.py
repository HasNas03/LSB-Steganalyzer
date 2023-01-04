# import binascii
#
# def a2b(char: str) -> str:
#     """
#     Return the binary representation of an ASCII character
#     """
#     # string.encode() function turns the specified string into an array of bytes
#     byte_array = char.encode()
#     # Convert the byte_array into a binary integer
#     binary_int = int.from_bytes(byte_array, "big")
#     # Convert binary_int to a string of binary characters
#     binary_string = bin(binary_int)
#     return binary_string[0] + binary_string[2:]
# # listy = [50, 100, 50]
# # colorval = min(listy)
# # print(colorval, listy.index(colorval))
# def b2a(char: str):
#     """
#         Return the ASCII representation of a binary string
#         """
#     input_string = int(char, 2)
#     # Obtain the total number of bytes
#     Total_bytes = (input_string.bit_length() + 7) // 8
#
#     # Convert these bits to bytes
#     input_array = input_string.to_bytes(Total_bytes, "big")
#
#     # Convert the bytes to an ASCII value and display it on the output screen
#     ASCII_value = input_array.decode()
#     return ASCII_value
#
#
# # print(a2b("Hasan"))
# # #print(b2a("01100010011000000110011"))
# #
# # l = "01100010011000000110000"
# # print(l[:-2])
# def string_to_binary(text: str) -> str:
#     binary_list = []
#     # Iterate through each character in the text
#     for char in text:
#         # Convert the character to its ASCII representation and then to binary
#         binary = bin(ord(char))[2:]
#         # Pad the binary representation with leading zeros to make it 8 digits long
#         binary = '0' * (8 - len(binary)) + binary
#         # Add the binary representation to the list
#         binary_list.append(binary)
#     # Join the binary representations into a single string and return it
#     return ''.join(binary_list)
#
#
# def binary_to_string(binary: str) -> str:
#     # Split the binary string into a list of 8-digit binary strings
#     binary_list = [binary[i:i + 8] for i in range(0, len(binary), 8)]
#     # Initialize an empty string to store the decoded text
#     text = ''
#     # Iterate through each 8-digit binary string
#     for b in binary_list:
#         # Convert the binary string to an integer and then to its ASCII representation
#         char = chr(int(b, 2))
#         # Add the character to the decoded text
#         text += char
#     # Return the decoded text
#     return text
#
#
#
#
# image = [
#
#     [   [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255]   ],
#
#     [   [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255]   ],
#
#     [   [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255]   ],
#
#     [   [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255]   ],
#
#     [   [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255]   ]
#     ]
from PIL import Image


array = [[1, 2, 3, 4, 5],
         [6, 7, 8, 9, 10],
         [11, 12, 13, 14, 15],
         [16, 17, 18, 19, 20],
         [21, 22, 23, 24, 25]]



def reshape_list(arr, x, y):
    # Initialize a list to store the reshaped list
    reshaped_list = []

    # Initialize a list to store the current row of items
    row = []

    # Iterate over each item in the array
    for item in arr:
        # If the current row has reached its maximum width, add it to the reshaped list
        # and start a new row
        if len(row) == y:
            reshaped_list.append(row)
            row = []

        # If the reshaped list has reached its maximum height, stop adding rows
        if len(reshaped_list) == x:
            break

        # Add the item to the current row
        row.append(item)

    # If the current row has any remaining items, add it to the reshaped list
    if row:
        reshaped_list.append(row)

    # Return the reshaped list
    return reshaped_list


# Example usage:
test = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
reshaped_list = reshape_list(test, 12, 2)
# print(reshaped_list)


def flatten_array(arr):
    # If the input array is empty, return an empty list
    if not arr:
        return []

    # If the input array is a 1D list, return it as-is
    if not isinstance(arr[0], list):
        return arr

    # If the input array is a 2D list, flatten the first row and append the remaining rows
    return flatten_array(arr[0]) + flatten_array(arr[1:])


# Example usage:
aw = [[1, 2, 3, 4, 5],
         [6, 7, 8, 9, 10],
         [11, 12, 13, 14, 15],
         [16, 17, 18, 19, 20],
         [21, 22, 23, 24, 25]]
flattened_array = flatten_array(aw)
# print(flattened_array)


import time


def test_flatten_array(num_tests):
    # Generate a 2000x2000 array of random integers
    import random
    array = [[random.randint(0, 1000) for _ in range(2000)] for _ in
             range(2000)]

    # Define the flatten_array_1 function using itertools.chain
    def flatten_array_1(arr):
        import itertools
        flattened_array = list(itertools.chain(*arr))
        return flattened_array

    # Define the flatten_array_2 function using a loop and extend
    def flatten_array_2(arr):
        flattened_array = []
        for row in arr:
            flattened_array.extend(row)
        return flattened_array

    # Initialize variables to store the elapsed times for each function
    elapsed_times_1 = []
    elapsed_times_2 = []

    # Measure the elapsed time for each function num_tests times
    for _ in range(num_tests):
        start_time = time.perf_counter()
        flattened_array_1 = flatten_array_1(array)
        elapsed_time_1 = time.perf_counter() - start_time
        elapsed_times_1.append(elapsed_time_1)

        start_time = time.perf_counter()
        flattened_array_2 = flatten_array_2(array)
        elapsed_time_2 = time.perf_counter() - start_time
        elapsed_times_2.append(elapsed_time_2)

    # Calculate the average elapsed time for each function
    avg_elapsed_time_1 = sum(elapsed_times_1) / len(elapsed_times_1)
    avg_elapsed_time_2 = sum(elapsed_times_2) / len(elapsed_times_2)
    t = (avg_elapsed_time_1, avg_elapsed_time_2)
    return t

#print(test_flatten_array(1000))

v = 1920 * 1880
i = 0
for j in range(v):
    i+=1
#print(i)
# def a2b(char: str) -> str:
#         """
#         Return the binary representation of an ASCII character
#         """
#         # string.encode() function turns the specified string into an array of bytes
#         byte_array = char.encode()
#         # Convert the byte_array into a binary integer
#         binary_int = int.from_bytes(byte_array, "big")
#         # Convert binary_int to a string of binary characters
#         binary_string = bin(binary_int)
#         return binary_string[0] + binary_string[2:]
# def b2a(char: str):
#         """
#         Return the ASCII representation of a binary string
#         """
#         input_string = int(char, 2)
#         # Obtain the total number of bytes
#         Total_bytes = (input_string.bit_length() + 7) // 8
#         # Convert these bits to bytes
#         input_array = input_string.to_bytes(Total_bytes, "big")
#         # Convert the bytes to an ASCII value and display it on the output screen
#         ASCII_value = input_array.decode()
#         return ASCII_value

#
#
# text_index = 0
# while text_index < 20:
#         print(text_index)
#         text_index += 1
#
# print(text_index + 100)


from PIL import Image

def get_image_pixels(image_path: str) -> list:
    # Open the image
    with Image.open(image_path) as image:
        # Get the pixel data as a 2D list of tuples
        pixels = list(image.getdata())
        # Convert each tuple to a list and return the 2D list of pixels
        return [[pixel for pixel in t] for t in pixels]


# print(get_image_pixels("/Users/hasannasir/Desktop/general/testpic.png"))


def pixel_extractor(image_path: str):
    i = 0
    with Image.open(image_path) as image:
        # Get the pixel data as a 2D list of tuples
        pixels = list(image.getdata())
        # return the 2D list of pixels
        result = []
        for t in pixels:
            sublist = []
            for pixel in t[0:3]:
                i += 1
                sublist.append(pixel)
            result.append(sublist)
        # return result
        return i

#print(pixel_extractor("/Users/hasannasir/Desktop/Screenshot 2023-01-02 at 8.32.11 PM.png"))

# image = [
#
#     [   [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255]   ],
#
#     [   [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255]   ],
#
#     [   [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255]   ],
#
#     [   [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255]   ],
#
#     [   [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255]   ]
#     ]


def a2b(text: str) -> str:
    """
    :param text: a string of text to be converted
    :return: The binary representation of the ASCII string
    """
    if text.isnumeric():
        return bin(int(text))
    binary_val = []
    # Iterate through each character in the text
    for char in text:
        # Convert the character to its ASCII representation and then to binary
        binary = bin(ord(char))[2:]
        # Pad the binary representation with leading zeros to make it 8 digits long
        binary = '0' * (8 - len(binary)) + binary
        # Add the binary representation to the list
        binary_val.append(binary)
    # Join the binary representations into a single string and return it
    return ''.join(binary_val)


# for i in range(0,16):
#     v = a2b(str(i))
#     v2 = ("0" * (8-len(v[2:]))) + v[2:]
#     l = (i, v2, len(v2))
#     print(l)

# for c in "abcdABCD":
#     print(a2b(c))






# NO LONGER NEEDED
#     def pixel_extractor(self, image_path: str) -> list:
#         with Image.open(image_path) as image:
#             # Get the pixel data as a 2D list of tuples
#             pixels = list(image.getdata())
#             # return the 2D list of pixels
#             result = []
#             for t in pixels:
#                 sublist = []
#                 for pixel in t[0:3]:
#                     sublist.append(pixel)
#                 result.append(sublist)
#             self.pixel_array = result
#             return result
#             # return [[pixel for pixel in t[0:3]] for t in pixels]

g = [1,2,3,4]
#print(list(g))
import os

def pixel_extraction2(self):
    # Check if the file exists
    if not os.path.exists(self):
        raise ValueError("File does not exist")
    # Open the image and get the size
    image = Image.open(self)
    width, height = image.size
    # Get the pixel data as a list of tuples
    pixels = list(image.getdata())
    # Convert the list of tuples to a 2D list
    result = []
    for i in range(0, len(pixels), width):
        result.append(pixels[i:i + width])
    s = 0
    for i in result:
        s += len(i)
    v = (result, s)
    return v


#print(pixel_extraction2("/Users/hasannasir/Desktop/BABA.png"))

old = [[(108, 61, 39, 255), (108, 60, 34, 255),
      (118, 70, 43, 255), (121, 73, 46, 255)],
     [(106, 58, 37, 255), (107, 59, 33, 255),
      (118, 70, 44, 255), (122, 74, 47, 255)],
       # below is same
     [(102, 54, 34, 255), (106, 58, 32, 255),
      (121, 73, 46, 255), (126, 78, 51, 255)],
     [(110, 62, 41, 255), (109, 60, 34, 255),
      (122, 72, 46, 255), (126, 76, 50, 255)],
     [(112, 64, 43, 255), (111, 61, 36, 255),
      (122, 72, 46, 255), (125, 75, 49, 255)],
     [(111, 63, 42, 255), (119, 69, 43, 255),
      (121, 71, 46, 255), (120, 70, 45, 255)]]

new = [[(108, 61, 37, 255), (108, 60, 34, 255),
      (118, 70, 41, 255), (121, 73, 47, 255)],
     [(106, 58, 37, 255), (107, 59, 34, 255),
      (118, 70, 47, 255), (122, 74, 46, 255)],
       # below is same
     [(102, 54, 34, 255), (106, 58, 32, 255),
      (121, 73, 46, 255), (126, 78, 51, 255)],
     [(110, 62, 41, 255), (109, 60, 34, 255),
      (122, 72, 46, 255), (126, 76, 50, 255)],
     [(112, 64, 43, 255), (111, 61, 36, 255),
      (122, 72, 46, 255), (125, 75, 49, 255)],
     [(111, 63, 42, 255), (119, 69, 43, 255),
      (121, 71, 46, 255), (120, 70, 45, 255)]]
