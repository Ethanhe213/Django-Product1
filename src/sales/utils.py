import uuid

def generate_code():
    return str(uuid.uuid4()).replace('-','')[:12]