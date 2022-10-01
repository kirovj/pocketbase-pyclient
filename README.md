<div align="center">

# pocketbase-pyclient
Python client for [pocketbase](https://github.com/pocketbase/pocketbase)
inspired by [pocketbase/js-sdk](https://github.com/pocketbase/js-sdk) and [pocketbase/dart-sdk](https://github.com/pocketbase/dart-sdk)

</div>

## What is PocketBase?

PocketBase is an open source Go backend, consisting of:

* embedded database (SQLite) with realtime subscriptions
* built-in files and users management
* convenient Admin dashboard UI
* and simple REST-ish API

It has only two official sdk [pocketbase/js-sdk](https://github.com/pocketbase/js-sdk) and [pocketbase/dart-sdk](https://github.com/pocketbase/dart-sdk)
so pocketbase-pyclient is an easy way to interact with the API with Python.

This project is still under development.

## Installation

```bash
pip install --user pocketbase-pyclient -i "https://test.pypi.org/simple"
```

## Example

```python
from pocketbase_pyclient import PocketBase

pb = PocketBase("http://127.0.0.1:8090")
pb.auth_via_email("test@kirovj.com", "testpassword")
print(pb.list("collection"))
```

## Credits

This project is strongly inspired by [pocketbase/js-sdk] and [pocketbase/dart-sdk].

[pocketbase/js-sdk]: https://github.com/pocketbase/js-sdk
[pocketbase/dart-sdk]: https://github.com/pocketbase/dart-sdk

## License

This project is open sourced under MIT license, see the [LICENSE](LICENSE) file for more details.