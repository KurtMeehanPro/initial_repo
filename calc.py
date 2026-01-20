"""Simple calculator functions: add, subtract, multiply, divide.

Each function accepts two numeric arguments `x` and `y` and returns
their result as a float.
"""

from __future__ import annotations

from typing import Union

Number = Union[int, float]

__all__ = ["add", "subtract", "multiply", "divide"]


def add(x: Number, y: Number) -> float:
	"""Return the sum of x and y.

	Examples:
		>>> add(1, 2)
		3.0
	"""
	return float(x + y)


def subtract(x: Number, y: Number) -> float:
	"""Return x minus y."""
	return float(x - y)


def multiply(x: Number, y: Number) -> float:
	"""Return the product of x and y."""
	return float(x * y)


def divide(x: Number, y: Number) -> float:
	"""Return x divided by y.

	Raises:
		ValueError: If `y` is zero.
	"""
	if y == 0:
		raise ValueError("Cannot divide by zero")
	return float(x / y)


def raise_power(x: Number, y: Number) -> float:
	"""Return the product of x and y."""
	return float(x ** y)


if __name__ == "__main__":
	# Quick sanity checks when run directly
	examples = [
		(add, 3, 4),
		(subtract, 10, 5),
		(multiply, 6, 7),
		(divide, 14, 2),
	]

	for fn, a, b in examples:
		print(f"{fn.__name__}({a}, {b}) = {fn(a, b)}")

	# Show divide-by-zero error handling
	try:
		divide(1, 0)
	except ValueError as exc:
		print(f"divide(1, 0) raised: {exc}")

