"""Command-line interface for kimi-work-demo."""

from __future__ import annotations

import argparse
from collections.abc import Sequence

from .greeting import build_greeting


def build_parser() -> argparse.ArgumentParser:
    """Build the command-line argument parser."""
    parser = argparse.ArgumentParser(
        prog="kimi-demo",
        description="Print a friendly greeting.",
    )
    parser.add_argument(
        "--name",
        default="World",
        help="name to greet (default: World)",
    )
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    """Run the CLI and return its process exit code."""
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        message = build_greeting(args.name)
    except ValueError as exc:
        parser.error(str(exc))
    print(message)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
