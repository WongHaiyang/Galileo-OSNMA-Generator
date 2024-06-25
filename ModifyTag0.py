from bitstring import BitArray


mack_start = 146
mack_length = 32
# original data
hexstring1='021333662A4249DD4A6EBB4CAE1900BD2A5CA24D14D06AAAAA73F18B0100'
hexstring2='041302FFEFFFEC47E000753A680000A6405CF3271BFA6AAAAA41F7688AC0'
nav_bits1 = BitArray(hex=hexstring1)
nav_bits2 = BitArray(hex=hexstring2)

# replaced data
target_hex = '3c2585c882'
target_bits = BitArray(hex=target_hex)

# corresponding position replacement
nav_bits1.overwrite(target_bits[:32], mack_start)
nav_bits2.overwrite(target_bits[32:], mack_start)

# hex
new_hexstring1 = nav_bits1.hex.upper()
new_hexstring2 = nav_bits2.hex.upper()

print("New hexstring1:", new_hexstring1)
print("New hexstring2:", new_hexstring2)

#prn_a:  0x02 parse tag0:  0x89345341cc gst_sf:  1251 277230
#prn_a 0x02 gst_sf 1251 277230 computed tag:  0x3c2585c882 received tag:  0x89345341cc
#277231,1251,2,021333662A4249DD4A6EBB4CAE1900BD2A5CA24D14D06AAAAA73F18B0100
#277233,1251,2,041302FFEFFFEC47E000753A680000A6405CF3271BFA6AAAAA41F7688AC0