def xor_binary(binario1, binario2):
    """
    Aplica la operación XOR entre dos cadenas binarias de la misma longitud.
    Retorna una nueva cadena binaria resultado de binario1 XOR binario2.
    """
    if len(binario1) != len(binario2):
        raise ValueError("Las cadenas binarias deben tener la misma longitud.")
    
    resultado = []
    for b1, b2 in zip(binario1, binario2):
        # XOR bit a bit
        xor_bit = str(int(b1) ^ int(b2))
        resultado.append(xor_bit)
    
    return ''.join(resultado)

if __name__ == "__main__":
    bin1 = "1010"
    bin2 = "1100"
    resultado = xor_binary(bin1, bin2)
    print(f"Binario1 : {bin1}")
    print(f"Binario2 : {bin2}")
    print(f"XOR      : {resultado}")
