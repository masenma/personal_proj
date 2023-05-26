import hmac
import hashlib
import secrets

def get_result(game_hash):
    salt = secrets.token_bytes(16)
    hm = hmac.new(str.encode(game_hash), b"", hashlib.sha256)
    hm.update(salt)
    h = hm.hexdigest()
    if int(h, 16) % 33 == 0:
        return 1
    h = int(h[:13], 16)
    e = 2**52
    return (((100 * e - h) / (e - h)) // 1) / 100 

game_hash = "77b271fe12fca03c61863dfb79d4105726ba9d4a25bb3f1964e435ccf9cb209"
print(get_result(game_hash))

if __name__ == "__main__":
    get_result()