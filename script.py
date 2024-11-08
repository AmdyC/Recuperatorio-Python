import requests
import json
def get_number_users():
    
    while True:
        try:
            n = int(input("Number of users (1-10): "))
            if 1 <= n <= 10:
                return n
            else:
                print("Error: Numbers formi 1 to 10.")
        except ValueError:
            print("Error: Enter valid number.")

def get_users(n):
    try:
        response = requests.get(f'https://jsonplaceholder.typicode.com/users?_limit={n}')
        response.raise_for_status() 
        return response.json()
    except requests.RequestException as e:
        print(f"Error API: {e}")
        return []

def split_users(users):
    users_vowels = []
    users_consonants = []
    
    for user in users:
        name = user['name']
        if name[0].lower() in 'aeiou':
            users_vowels.append(user)
        else:
            users_consonants.append(user)
    
    return users_vowels, users_consonants

def save_users(users_vowels, users_consonants):

    with open('UsersData/usersVowels.json', 'w') as file:
        json.dump(users_vowels, file, indent=4)

    with open('UsersData/usersConsonants.json', 'w') as file:
        json.dump(users_consonants, file, indent=4)


def main():
    """Función principal que ejecuta el flujo del programa."""
    n = get_number_users()  
    usuarios = get_users(n)   

    if usuarios: 
        users_vowels, users_consonats = split_users(usuarios) 
        save_users(users_vowels, users_consonats)  
        print("Finish")

if __name__ == "__main__":
    main()
