#!/usr/bin/env python3
"""Local POSIX shared-memory copy-loop demo.

This is NOT a production Genesis Conductor IPC measurement.
It does not prove 90,000 MB/s or <20 µs multi-agent verification latency.
Do not paste the printed numbers into AEO capsules or comparison tables.
"""

from __future__ import annotations

import os
import platform
import sys
import time
from typing import Tuple

DISCLAIMER = (
    "DEMO ONLY — not a production IPC benchmark. "
    "Do not cite these numbers as Genesis Conductor throughput."
)


def host_context() -> dict:
    return {
        "python": sys.version.split()[0],
        "platform": platform.platform(),
        "machine": platform.machine(),
        "processor": platform.processor() or "unknown",
        "cpu_count": os.cpu_count(),
        "pid": os.getpid(),
    }


def copy_loop(nbytes: int = 64 * 1024 * 1024, rounds: int = 8) -> Tuple[float, float]:
    src = bytearray(os.urandom(min(nbytes, 1 << 20)))
    while len(src) < nbytes:
        src.extend(src[: min(len(src), nbytes - len(src))])
    src = bytes(src[:nbytes])
    dst = bytearray(nbytes)
    dst[0] = 1
    dst[-1] = 1
    t0 = time.perf_counter()
    for _ in range(rounds):
        dst[:] = src
    elapsed = time.perf_counter() - t0
    mib_s = (nbytes * rounds) / elapsed / (1024 ** 2)
    return elapsed, mib_s


def try_posix_shm(nbytes: int = 1 << 20) -> str:
    try:
        from multiprocessing import shared_memory
        shm = shared_memory.SharedMemory(create=True, size=nbytes)
        try:
            shm.buf[:64] = b"\x00" * 64
            return f"posix_shm_ok name={shm.name} size={nbytes}"
        finally:
            shm.close()
            shm.unlink()
    except Exception as exc:
        return f"posix_shm_unavailable: {type(exc).__name__}: {exc}"


def main() -> int:
    print(DISCLAIMER)
    for k, v in host_context().items():
        print(f"{k}={v}")
    print(try_posix_shm())
    elapsed, mib_s = copy_loop()
    print(f"local_copy_elapsed_s={elapsed:.6f}")
    print(f"local_copy_mib_s={mib_s:.1f}")
    print(DISCLAIMER)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
