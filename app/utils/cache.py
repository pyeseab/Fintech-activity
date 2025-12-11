#store data temporarily 
# utils/cache.py

_cache = {}

def set_cache(key: str, value, ttl: int = None):
    """
    Store a value in the cache.
    Optionally, set a TTL (time to live in seconds).
    """
    import time
    expire_at = time.time() + ttl if ttl else None
    _cache[key] = {"value": value, "expire_at": expire_at}


def get_cache(key: str):
    """
    Retrieve a value from the cache.
    Returns None if key does not exist or is expired.
    """
    import time
    entry = _cache.get(key)
    if not entry:
        return None
    if entry["expire_at"] and time.time() > entry["expire_at"]:
        # Remove expired entry
        del _cache[key]
        return None
    return entry["value"]


def clear_cache(key: str = None):
    """
    Clear a specific cache key, or the entire cache if key is None.
    """
    if key:
        _cache.pop(key, None)
    else:
        _cache.clear()
