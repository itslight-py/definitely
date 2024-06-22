# definitely
Definitely typed.

**By**: jc (AWeirdDev)<br />
**Published as**: `definitely`

```shell
light i definitely  # @itslight-py/definitely
```

## Import

You can use the recommended import style:
```python
# Direct import
from its.definitely import definitely
```

...or use with `load()` if you added the `--minimal` flag when installing:
```python
from itslight import load

# Use load() and "~" to indicate "same as package name"
definitely = load("definitely", "~")
```

## Usage
Tricks the Python typing system in any way possible.

```python
foo = "Cool!"
assert definitely(foo, str)  # foo: str
assert definitely(foo, int)  # foo: int, actual foo: str

reveal_type(foo)
# type checking: int
# runtime type:  str
```

## Usecase
This module is useful when you're indexing into `ast` (abstract syntax trees) under a strictly-typed environment.
