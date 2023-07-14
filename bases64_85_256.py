import base64

def codificar_base64(texto):
    texto_bytes = texto.encode('utf-8')
    base64_bytes = base64.b64encode(texto_bytes)
    base64_string = base64_bytes.decode('utf-8')
    return base64_string

def decodificar_base64(base64_string):
    base64_bytes = base64_string.encode('utf-8')
    texto_bytes = base64.b64decode(base64_bytes)
    texto = texto_bytes.decode('utf-8')
    return texto

def codificar_base85(texto):
    texto_bytes = texto.encode('utf-8')
    base85_bytes = base64.b85encode(texto_bytes)
    base85_string = base85_bytes.decode('utf-8')
    return base85_string

def decodificar_base85(base85_string):
    base85_bytes = base85_string.encode('utf-8')
    texto_bytes = base64.b85decode(base85_bytes)
    texto = texto_bytes.decode('utf-8')
    return texto

def codificar_base256(texto):
    texto_bytes = texto.encode('utf-8')
    base256_string = ''.join([str(byte) for byte in texto_bytes])
    return base256_string

def decodificar_base256(base256_string):
    bytes_list = [int(base256_string[i:i+3]) for i in range(0, len(base256_string), 3)]
    texto_bytes = bytes(bytes_list)
    texto = texto_bytes.decode('utf-8')
    return texto

# Ejemplo de uso
texto_original = "¡Hola, mundo!"
print("Texto original:", texto_original)

# Codificar en Base64
codificado_base64 = codificar_base64(texto_original)
print("Codificado en Base64:", codificado_base64)

# Descodificar Base64
descodificado_base64 = decodificar_base64(codificado_base64)
print("Descodificado Base64:", descodificado_base64)

# Codificar en Base128
codificar_base85 = codificar_base85(texto_original)
print("Codificado en Base128:", codificar_base85)

# Descodificar Base128
decodificar_base85 = decodificar_base85(codificado_base64)
print("Descodificado Base128:", decodificar_base85)

# Codificar en Base256
codificado_base256 = codificar_base256(texto_original)
print("Codificado en Base256:", codificado_base256)

# Descodificar Base256
descodificado_base256 = decodificar_base256(codificado_base256)
print("Descodificado Base256:", descodificado_base256)
