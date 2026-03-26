import hashlib

def calchash(file_path):
    with open(file_path, 'rb') as f:
        contenuto = f.read()

    sha256 = hashlib.sha256(contenuto).hexdigest()
    md5 = hashlib.md5(contenuto).hexdigest()
    sha1 = hashlib.sha1(contenuto).hexdigest()
    return sha256, md5, sha1
