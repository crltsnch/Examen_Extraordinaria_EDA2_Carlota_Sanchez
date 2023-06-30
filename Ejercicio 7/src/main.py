import arbol_huffman

def main():
    freq = {'A':0.2, 'F':0.17, '1':0.13, '3':0.21, '0':0.05, 'M':0.09, 'T':0.15}
    message = "AF10MTF3130A0M"
    encoded_message = arbol_huffman.compress(message, freq)
    decoded_message = arbol_huffman.decompress(encoded_message, freq)
    print(f"Mensaje original: {message}")
    print(f"Mensaje codificado: {encoded_message}")
    print(f"Mensaje decodificado: {decoded_message}")

if __name__ == "__main__":
    main()