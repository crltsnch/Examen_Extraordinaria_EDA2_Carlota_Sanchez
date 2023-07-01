from src.arbol_huffman import arbol_huffman

def test_compress():
    freq = {'A':0.2, 'F':0.17, '1':0.13, '3':0.21, '0':0.05, 'M':0.09, 'T':0.15}
    message = "AF10MTF3130A0M"
    expected_ouput = "0011110010101011110111011000110100010101011"
    result = arbol_huffman.compress(message, freq)
    assert result == expected_ouput
    print("Test de compresión exitoso")

def test_decompress():
    freq = {'A':0.2, 'F':0.17, '1':0.13, '3':0.21, '0':0.05, 'M':0.09, 'T':0.15}
    encoded_message = "0011110010101011110111011000110100010101011"
    expected_ouput = "AF10MTF3130A0M"
    result = arbol_huffman.decompress(encoded_message, freq)
    assert result == expected_ouput
    print("Test de descompresión exitoso")

if __name__ == "__main__":
    test_compress()
    test_decompress()
