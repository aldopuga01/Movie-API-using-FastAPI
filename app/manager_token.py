from jwt import encode, decode

def create_token(data: dict) -> str:
    token: str = encode(payload=data, key="58703273357638792F413F4428472B4B", algorithm="HS256")
    return token

# Validate token
def validate_token(token: str) -> dict:
    data: dict = decode(token, key="58703273357638792F413F4428472B4B", algorithms=["HS256"])
    return data