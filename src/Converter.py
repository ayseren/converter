class Converter:

  def __init__(self):
      print("converter deneme")

  def from_hex(self, hex_value):
    number = int(hex_value, 16)

    eight_big_byte = number.to_bytes(8, 'big')
    four_big_byte = number.to_bytes(4, 'big')
    eight_little_byte = number.to_bytes(8, 'little')
    four_little_byte = number.to_bytes(4, 'little')

    eight_big_number_array = list(eight_big_byte)
    four_big_number_array = list(four_big_byte)
    eight_little_number_array = list(eight_little_byte)
    four_little_number_array = list(four_little_byte)

    result = { 
      "input": hex_value,
      "number": number,
      "hex": hex_value,
      "8_byte_big_number_array": eight_big_number_array,
      "4_byte_big_number_array": four_big_number_array,
      "8_byte_little_number_array": eight_little_number_array,
      "4_byte_little_number_array": four_little_number_array
    }

    print("result1",result)

    return result

  def from_int(self, number):
    hex_value = hex(number)[2:]

    eight_big_byte = number.to_bytes(8, 'big')
    four_big_byte = number.to_bytes(4, 'big')
    eight_little_byte = number.to_bytes(8, 'little')
    four_little_byte = number.to_bytes(4, 'little')

    eight_big_number_array = list(eight_big_byte)
    four_big_number_array = list(four_big_byte)
    eight_little_number_array = list(eight_little_byte)
    four_little_number_array = list(four_little_byte)

    
    result = { 
      "input": number,
      "number": number,
      "hex": hex_value,
      "8_byte_big_number_array": eight_big_number_array,
      "4_byte_big_number_array": four_big_number_array,
      "8_byte_little_number_array": eight_little_number_array,
      "4_byte_little_number_array": four_little_number_array
    }

    print("result2", result)

    return result

asdf = Converter()
asdf.from_hex(hex_value="1112")
asdf.from_int(number=803)