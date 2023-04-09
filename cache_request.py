from requests_cache import CachedSession, AnyResponse
from rich import print


session = CachedSession("requestcache", expire_after=1 * 24 * 60 * 60, backend="sqlite")
session.cache.remove_expired_responses()


def cache_request(url: str, **kwargs) -> AnyResponse:
    """
    Send a GET request to the specified URL using a cached session.
    """
    response = session.get(url, **kwargs)
    print("\n______________________________________________")
    print(f"URL: {response.url}")
    print(f"Response cache status: {response.from_cache}")
    print(f"Response created at: {response.created_at}")
    print(f"Response expiration time: {response.expires}")
    print(f"Is response expired? {response.is_expired}")
    print("______________________________________________\n")
    return response
