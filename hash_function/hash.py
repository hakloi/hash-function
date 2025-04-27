def simple_hash(input_bytes: bytes) -> bytes:
    """
    Простая хэш-функция, которая генерирует хэш длиной 32 байта
    с использованием нескольких раундов и базовых операций.
    """
    hash_value = 0xCAFEBABE  
    prime = 0x01000193 
    for byte in input_bytes:
        hash_value ^= byte  
        hash_value *= prime  
        hash_value = (hash_value << 7) | (hash_value >> (64 - 7))  
    
    return (hash_value & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF).to_bytes(32, byteorder='big')
