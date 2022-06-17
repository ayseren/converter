class Converter:

  def __init__(self):
      print("converter deneme")

  #hex girecek number ve byte array
  def from_hex(self, hex, endian, byte_length):
    number_value = int(hex, 16)
    
    if endian == "big": 
      if byte_length == "8-bytes":
        byte_value = number_value.to_bytes(8, 'big')
      if byte_length == "4-bytes":
        byte_value = number_value.to_bytes(4, 'big')

    if endian == "little": 
      if byte_length == "8-bytes":
        byte_value = number_value.to_bytes(8, 'little')
      if byte_length == "4-bytes":
        byte_value = number_value.to_bytes(4, 'little')
    
    number_array_value = list(byte_value)
    byte_length = len(byte_value)

    result = { 
      "byte_array": byte_value, "byte_array_length": byte_length, "number": number_value, "number_array_value": number_array_value
    }

    print("result1",result)
  
  #int girecek hex ve byte array
  def from_int(self, number, endian, byte_length):
    hex_value = hex(number)[2:]
    
    if endian == "big": 
      if byte_length == "8-bytes":
        byte_value = number.to_bytes(8, 'big')
      if byte_length == "4-bytes":
        byte_value = number.to_bytes(4, 'big')

    if endian == "little": 
      if byte_length == "8-bytes":
        byte_value = number.to_bytes(8, 'little')
      if byte_length == "4-bytes":
        byte_value = number.to_bytes(4, 'little')

    number_array_value = list(byte_value)
    byte_length = len(byte_value)

    result = { 
      "byte_value": bytes.fromhex(hex_value), "byte_length": byte_length, "hex_value": hex_value, "number_array_value": number_array_value 
    }

    print("result2", result)

asdf = Converter()
asdf.from_hex(hex="1112", endian="little", byte_length="8-bytes")
asdf.from_int(number=17, endian="big", byte_length="4-bytes")