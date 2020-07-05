# DO NOT EDIT - AUTOMATICALLY GENERATED BY tests/make_test_stubs.py!
from typing import List
from typing import Union


def API520_A_g(
    m: float,
    T: float,
    Z: float,
    MW: float,
    k: float,
    P1: float,
    P2: float = ...,
    Kd: float = ...,
    Kb: int = ...,
    Kc: int = ...
) -> float: ...


def API520_A_steam(m: float, T: float, P1: float, Kd: float = ..., Kb: int = ..., Kc: int = ...) -> float: ...


def API520_B(Pset: float, Pback: float, overpressure: float = ...) -> float: ...


def API520_C(k: float) -> float: ...


def API520_F2(k: float, P1: float, P2: float) -> float: ...


def API520_Kv(Re: float) -> float: ...


def API520_N(P1: float) -> float: ...


def API520_SH(T1: float, P1: float) -> float: ...


def API520_W(Pset: float, Pback: float) -> float: ...


def API520_round_size(A: float) -> float: ...

__all__: List[str]