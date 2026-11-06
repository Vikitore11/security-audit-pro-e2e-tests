# Benign CodeQL baseline fixture. Never used in production.

def normalize_greeting(value: str) -> str:
    return 'Hello, ' + value.strip()


if __name__ == '__main__':
    print(normalize_greeting('world'))
