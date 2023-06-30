from arbol_huffman import arbol_huffman

def test_compress():
    freq = {'A':0.2, 'F':0.17, '1':0.13, '3':0.21, '0':0.05, 'M':0.09, 'T':0.15}
    message = "AF10MTF3130A0M"
    expected_ouput = "1100000110100011000100101011001110011100101101000111000101"
    assert arbol_huffman.compress(message, freq) == expected_ouput

def test_decompress():
    freq = {'A':0.2, 'F':0.17, '1':0.13, '3':0.21, '0':0.05, 'M':0.09, 'T':0.15}
    encoded_message = "1100000110100011000100101011001110011100101101000111000101"
    expected_ouput = "AF10MTF3130A0M"
    assert arbol_huffman.decompress(encoded_message, freq) == expected_ouput