def binary_to_ascii(binary_text):
    ascii_result = ''

    # Validar que la longitud del texto binario sea un múltiplo de 8
    if len(binary_text) % 8 != 0:
        # Calcular cuántos ceros se necesitan
        padding_needed = 8 - (len(binary_text) % 8)
        binary_text = '0' * padding_needed + binary_text

    # Dividir el texto binario en grupos de 8 bits
    for i in range(0, len(binary_text), 8):
        binary_chunk = binary_text[i:i + 8]
        decimal_value = int(binary_chunk, 2)
        ascii_result += chr(decimal_value)

    return ascii_result

if __name__ == "__main__":
    binary_text = input("Ingresa el texto en binario que deseas convertir (múltiplo de 8 bits): ")
    try:
        ascii_output = binary_to_ascii(binary_text)
        print(f"Texto en ASCII: {ascii_output}")
    except Exception as e:
        print(f"Error: {e}")