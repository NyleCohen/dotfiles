from typing import Any, Optional
import sys

if sys.version_info[0] >= 3:
    from io import BytesIO
    from urllib.parse import quote_from_bytes as url_quote
else:
    from cStringIO import StringIO as BytesIO
    from urllib import quote as url_quote

PY2 = ...  # type: Any
PYPY = ...  # type: Any
unichr = ...  # type: Any
range_type = ...  # type: Any
text_type = ...  # type: Any
string_types = ...  # type: Any
integer_types = ...  # type: Any
iterkeys = ...  # type: Any
itervalues = ...  # type: Any
iteritems = ...  # type: Any
NativeStringIO = ...  # type: Any

def reraise(tp, value, tb: Optional[Any] = ...): ...

ifilter = ...  # type: Any
imap = ...  # type: Any
izip = ...  # type: Any
intern = ...  # type: Any
implements_iterator = ...  # type: Any
implements_to_string = ...  # type: Any
encode_filename = ...  # type: Any
get_next = ...  # type: Any

def with_metaclass(meta, *bases): ...
