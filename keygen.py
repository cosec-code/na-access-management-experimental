from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    backend=default_backend()
)  # Key generation
public_key = private_key.public_key()  # Public key extraction

private_key_g = private_key  # Assignment of private key to a separate variable in order to serialize

pem = private_key_g.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption()
)  # Serialization

with open('private_key.pem', 'wb') as f:
    f.write(pem)  # Write

public_key_h = public_key

pem = public_key_h.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

with open('public_key.pem', 'wb') as f:
    f.write(pem)

print("Keys generated. Pushing public key to access points!")  # Placeholder for network code
