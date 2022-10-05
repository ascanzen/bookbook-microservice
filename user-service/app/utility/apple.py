import json

import jwt
import requests

# https://developer.apple.com/documentation/sign_in_with_apple/
# https://pyjwt.readthedocs.io/en/latest/usage.html
# https://gist.github.com/davidhariri/b053787aabc9a8a9cc0893244e1549fe


class AppleClient:
    def __init__(
        self,
        public_key_url="https://appleid.apple.com/auth/keys",
        audience="com.yesfeeling.fitnessZ",
    ):
        self.public_key_url = public_key_url
        self.audience = audience

    def get_public_key(self, kid, alg):
        # would be good to cache this info but have to be careful not to cache it too long
        payload = requests.get(self.public_key_url).json()
        for key in payload["keys"]:
            if key["kid"] == kid and key["alg"] == alg:
                return jwt.algorithms.RSAAlgorithm.from_jwk(json.dumps(key))
        raise ValueError(f"No Apple public key with kid `{kid}` and alg `{alg}` found")

    def get_verified_email(self, id_token):
        header = jwt.get_unverified_header(id_token)
        public_key = self.get_public_key(header["kid"], header["alg"])
        # To avoid expired signature when testing: jwt.decode(... options={'verify_exp': False})
        info = jwt.decode(
            id_token,
            public_key,
            audience=self.audience,
            algorithms=header["alg"],
            options={"verify_exp": False},
        )
        if not info.get("email_verified") or not info.get("email"):
            raise ValueError("Apple id token does not contain verified email")
        return info["email"]


# @routes.register('Mutation.createAppleUser')
# def create_apple_user(caller_user_id, arguments, source, context):
#     username = arguments['username']
#     full_name = arguments.get('fullName')
#     apple_token = arguments['appleIdToken']
#     try:
#         user = user_manager.create_federated_user(
#             'apple', caller_user_id, username, apple_token, full_name=full_name
#         )
#     except UserException as err:
#         raise ClientException(str(err)) from err
#     return user.serialize(caller_user_id)


if __name__ == "__main__":
    token = "eyJraWQiOiJZdXlYb1kiLCJhbGciOiJSUzI1NiJ9.eyJpc3MiOiJodHRwczovL2FwcGxlaWQuYXBwbGUuY29tIiwiYXVkIjoiY29tLnllc2ZlZWxpbmcuZml0bmVzc1oiLCJleHAiOjE2MTYyMjM2NjQsImlhdCI6MTYxNjEzNzI2NCwic3ViIjoiMDAwNDAyLjY5ZWMyOGU4M2NiMTQ3NDdhNzE1N2U4M2FlZDAzYmJmLjA2NTQiLCJjX2hhc2giOiI2dE5jb2pLdUFyTU90ZlpQWWtQVjJBIiwiZW1haWwiOiJtNTdreGJiZzk5QHByaXZhdGVyZWxheS5hcHBsZWlkLmNvbSIsImVtYWlsX3ZlcmlmaWVkIjoidHJ1ZSIsImlzX3ByaXZhdGVfZW1haWwiOiJ0cnVlIiwiYXV0aF90aW1lIjoxNjE2MTM3MjY0LCJub25jZV9zdXBwb3J0ZWQiOnRydWV9.IOnYN0WnfiZHDSF2gwFbnKQqWvqxnNxvlsEsUkH88MdBNoxbPQFISq8rLIE4LZIMehOiYvSpdkLZIVTVa2kXhFob38BGXw9JCVxFfjgBXDZou7Dma9HZ_WGybJvTLp2Iz50HKVG_N3EsyjBNr6TUp9DBZrwYeeXalzWKH-_Taj11LvRWYYqoV6CCQ8D-UYI_MqNOlVd5WVtZhoQQKVB0HMK0iZFK_gc1jmUD6IqCtIAs5GRwrPQ_lw6--Ja_dx7rofyH3c4OjhTwZz4Hm6NxOIoMAaAsHzR0aEb6A1qHt944DOTCotrS5Xi13VU2yOFUb7IilhoC0beXROsjLToYlg"
    client = AppleClient()
    print(client.get_verified_email(token))

# python3.9 -m app.utility.apple
