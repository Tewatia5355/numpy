from typing import List, TypeVar, Optional, Any, overload, Union, Tuple, Sequence, Literal

from numpy import (
    ndarray,
    dtype,
    bool_,
    unsignedinteger,
    signedinteger,
    floating,
    complexfloating,
    number,
    _OrderKACF,
)
from numpy.typing import (
    _ArrayLikeBool_co,
    _ArrayLikeUInt_co,
    _ArrayLikeInt_co,
    _ArrayLikeFloat_co,
    _ArrayLikeComplex_co,
    _DTypeLikeBool,
    _DTypeLikeUInt,
    _DTypeLikeInt,
    _DTypeLikeFloat,
    _DTypeLikeComplex,
    _DTypeLikeComplex_co,
)

_ArrayType = TypeVar(
    "_ArrayType",
    bound=ndarray[Any, dtype[Union[bool_, number[Any]]]],
)

_OptimizeKind = Union[
    None, bool, Literal["greedy", "optimal"], Sequence[Any]
]
_CastingSafe = Literal["no", "equiv", "safe", "same_kind"]
_CastingUnsafe = Literal["unsafe"]

__all__: List[str]

# TODO: Properly handle the `casting`-based combinatorics
# TODO: We need to evaluate the content `__subscripts` in order
# to identify whether or an array or scalar is returned. At a cursory
# glance this seems like something that can quite easilly be done with
# a mypy plugin.
# Something like `is_scalar = bool(__subscripts.partition("->")[-1])`
@overload
def einsum(
    __subscripts: str,
    *operands: _ArrayLikeBool_co,
    out: None = ...,
    dtype: Optional[_DTypeLikeBool] = ...,
    order: _OrderKACF = ...,
    casting: _CastingSafe = ...,
    optimize: _OptimizeKind = ...,
) -> Any: ...
@overload
def einsum(
    __subscripts: str,
    *operands: _ArrayLikeUInt_co,
    out: None = ...,
    dtype: Optional[_DTypeLikeUInt] = ...,
    order: _OrderKACF = ...,
    casting: _CastingSafe = ...,
    optimize: _OptimizeKind = ...,
) -> Any: ...
@overload
def einsum(
    __subscripts: str,
    *operands: _ArrayLikeInt_co,
    out: None = ...,
    dtype: Optional[_DTypeLikeInt] = ...,
    order: _OrderKACF = ...,
    casting: _CastingSafe = ...,
    optimize: _OptimizeKind = ...,
) -> Any: ...
@overload
def einsum(
    __subscripts: str,
    *operands: _ArrayLikeFloat_co,
    out: None = ...,
    dtype: Optional[_DTypeLikeFloat] = ...,
    order: _OrderKACF = ...,
    casting: _CastingSafe = ...,
    optimize: _OptimizeKind = ...,
) -> Any: ...
@overload
def einsum(
    __subscripts: str,
    *operands: _ArrayLikeComplex_co,
    out: None = ...,
    dtype: Optional[_DTypeLikeComplex] = ...,
    order: _OrderKACF = ...,
    casting: _CastingSafe = ...,
    optimize: _OptimizeKind = ...,
) -> Any: ...
@overload
def einsum(
    __subscripts: str,
    *operands: Any,
    casting: _CastingUnsafe,
    dtype: Optional[_DTypeLikeComplex_co] = ...,
    out: None = ...,
    order: _OrderKACF = ...,
    optimize: _OptimizeKind = ...,
) -> Any: ...
@overload
def einsum(
    __subscripts: str,
    *operands: _ArrayLikeComplex_co,
    out: _ArrayType,
    dtype: Optional[_DTypeLikeComplex_co] = ...,
    order: _OrderKACF = ...,
    casting: _CastingSafe = ...,
    optimize: _OptimizeKind = ...,
) -> _ArrayType: ...
@overload
def einsum(
    __subscripts: str,
    *operands: Any,
    out: _ArrayType,
    casting: _CastingUnsafe,
    dtype: Optional[_DTypeLikeComplex_co] = ...,
    order: _OrderKACF = ...,
    optimize: _OptimizeKind = ...,
) -> _ArrayType: ...

# NOTE: `einsum_call` is a hidden kwarg unavailable for public use.
# It is therefore excluded from the signatures below.
# NOTE: In practice the list consists of a `str` (first element)
# and a variable number of integer tuples.
def einsum_path(
    __subscripts: str,
    *operands: _ArrayLikeComplex_co,
    optimize: _OptimizeKind = ...,
) -> Tuple[List[Any], str]: ...
