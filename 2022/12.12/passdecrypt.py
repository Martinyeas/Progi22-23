import hashlib
import base64

import hashlib
import base64

def decrypt_password(hashed_password: str) -> str:
  password_hash = hashlib.sha256(hashed_password.encode())

  password_hash_bytes = password_hash.digest()

  decoded_hash = base64.b64decode(password_hash_bytes)

  return decoded_hash.decode()


hashed_password = "HASHED_PASSWORD"

decrypted_password = decrypt_password(hashed_password)

print(decrypted_password)