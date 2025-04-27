from hash_function.hash import simple_hash

# База данных
database = []

def add_to_database(email: str):
    email_bytes = email.encode('utf-8')

    hashed_email = simple_hash(email_bytes)
    
    database.append(hashed_email)
    print(f"Email хэширован и добавлен в базу данных: {hashed_email.hex()}")

if __name__ == "__main__":
    email = input("Введите ваш email: ")
    add_to_database(email)
    print("Текущая база данных (хэши):")
    for hash_entry in database:
        print(hash_entry.hex())