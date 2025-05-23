from typing import Iterator, overload, TYPE_CHECKING

if TYPE_CHECKING:
    from urllib.parse import ParseResult

__version__: str

class URL:
    hash: str
    host: str
    hostname: str
    href: str
    password: str
    pathname: str
    port: str
    protocol: str
    search: str
    username: str
    def __init__(self, *args, **kwargs) -> None: ...
    def has_credentials(self) -> bool: ...
    def has_empty_hostname(self) -> bool: ...
    def has_hash(self) -> bool: ...
    def has_hostname(self) -> bool: ...
    def has_non_empty_password(self) -> bool: ...
    def has_non_empty_username(self) -> bool: ...
    def has_password(self) -> bool: ...
    def has_port(self) -> bool: ...
    def has_search(self) -> bool: ...
    def has_valid_domain(self) -> bool: ...
    def to_diagram(self) -> str: ...
    def validate(self) -> bool: ...
    def __add__(self, arg0: str) -> URL: ...
    @property
    def origin(self) -> str: ...
    @property
    def pathname_length(self) -> int: ...

class URLSearchParams:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, arg0: str) -> None: ...
    def append(self, arg0: str, arg1: str) -> None: ...
    def copy(self) -> URLSearchParams: ...
    def get(self, arg0: str) -> str | None: ...
    def get_all(self, arg0: str) -> list[str]: ...
    def has(self, key: str, value: str | None = ...) -> bool: ...
    def keys(self) -> URLSearchParamsKeysIter: ...
    def remove(self, key: str, value: str | None = ...) -> None: ...
    def size(self) -> int: ...
    def sort(self) -> None: ...
    def values(self) -> URLSearchParamsValuesIter: ...
    def __contains__(self, arg0: str) -> bool: ...
    def __delitem__(self, arg0: str) -> None: ...
    def __getitem__(self, arg0: str) -> str: ...
    def __iter__(self) -> Iterator[tuple[str, str]]: ...
    def __len__(self) -> int: ...
    def __setitem__(self, arg0: str, arg1: str) -> None: ...

class URLSearchParamsKeysIter:
    def __init__(self, *args, **kwargs) -> None: ...
    def __iter__(self) -> URLSearchParamsKeysIter: ...
    def __next__(self) -> str | None: ...

class URLSearchParamsValuesIter:
    def __init__(self, *args, **kwargs) -> None: ...
    def __iter__(self) -> URLSearchParamsValuesIter: ...
    def __next__(self) -> str | None: ...

def can_parse(input: str, base_input: str | None = ...) -> bool: ...
def idna_decode(arg0: str) -> str: ...
def idna_encode(arg0: str) -> bytes: ...
def parse(arg0: str) -> URL: ...
def parse_compat(arg0: str) -> ParseResult: ...
