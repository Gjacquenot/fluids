# DO NOT EDIT - AUTOMATICALLY GENERATED BY tests/make_test_stubs.py!
from typing import List
from typing import (
    List,
    Optional,
    Tuple,
    Union,
)


def Bankoff(
    m: float,
    x: float,
    rhol: float,
    rhog: float,
    mul: float,
    mug: float,
    D: float,
    roughness: float = ...,
    L: int = ...
) -> float: ...


def Baroczy_Chisholm(
    m: float,
    x: float,
    rhol: float,
    rhog: float,
    mul: float,
    mug: float,
    D: float,
    roughness: float = ...,
    L: int = ...
) -> float: ...


def Beggs_Brill(
    m: float,
    x: float,
    rhol: float,
    rhog: float,
    mul: float,
    mug: float,
    sigma: float,
    P: float,
    D: float,
    angle: float,
    roughness: float = ...,
    L: float = ...,
    g: float = ...,
    acceleration: bool = ...
) -> float: ...


def Chen_Friedel(
    m: float,
    x: float,
    rhol: float,
    rhog: float,
    mul: float,
    mug: float,
    sigma: float,
    D: float,
    roughness: float = ...,
    L: int = ...
) -> float: ...


def Chisholm(
    m: float,
    x: float,
    rhol: float,
    rhog: float,
    mul: float,
    mug: float,
    D: float,
    roughness: float = ...,
    L: int = ...,
    rough_correction: bool = ...
) -> float: ...


def Friedel(
    m: float,
    x: float,
    rhol: float,
    rhog: float,
    mul: float,
    mug: float,
    sigma: float,
    D: float,
    roughness: float = ...,
    L: int = ...
) -> float: ...


def Gronnerud(
    m: float,
    x: float,
    rhol: float,
    rhog: float,
    mul: float,
    mug: float,
    D: float,
    roughness: float = ...,
    L: int = ...
) -> float: ...


def Hwang_Kim(
    m: float,
    x: float,
    rhol: float,
    rhog: float,
    mul: float,
    mug: float,
    sigma: float,
    D: float,
    roughness: float = ...,
    L: int = ...
) -> float: ...


def Jung_Radermacher(
    m: float,
    x: float,
    rhol: float,
    rhog: float,
    mul: float,
    mug: float,
    D: float,
    roughness: float = ...,
    L: int = ...
) -> float: ...


def Kim_Mudawar(
    m: float,
    x: float,
    rhol: float,
    rhog: float,
    mul: float,
    mug: float,
    sigma: float,
    D: float,
    L: int = ...
) -> float: ...


def Lockhart_Martinelli(
    m: float,
    x: float,
    rhol: float,
    rhog: float,
    mul: float,
    mug: float,
    D: float,
    L: int = ...,
    Re_c: int = ...
) -> float: ...


def Lombardi_Pedrocchi(m: float, x: float, rhol: float, rhog: float, sigma: float, D: float, L: int = ...) -> float: ...


def Mandhane_Gregory_Aziz_regime(
    m: float,
    x: float,
    rhol: float,
    rhog: float,
    mul: float,
    mug: float,
    sigma: float,
    D: float
) -> Tuple[str, float, float]: ...


def Mishima_Hibiki(
    m: float,
    x: float,
    rhol: float,
    rhog: float,
    mul: float,
    mug: float,
    sigma: float,
    D: float,
    roughness: float = ...,
    L: int = ...
) -> float: ...


def Muller_Steinhagen_Heck(
    m: float,
    x: float,
    rhol: float,
    rhog: float,
    mul: float,
    mug: float,
    D: float,
    roughness: float = ...,
    L: int = ...
) -> float: ...


def Taitel_Dukler_regime(
    m: float,
    x: float,
    rhol: float,
    rhog: float,
    mul: float,
    mug: float,
    D: float,
    angle: int,
    roughness: int = ...,
    g: float = ...
) -> Tuple[str, float, float, float, float]: ...


def Theissing(
    m: float,
    x: float,
    rhol: float,
    rhog: float,
    mul: float,
    mug: float,
    D: float,
    roughness: float = ...,
    L: int = ...
) -> float: ...


def Tran(
    m: float,
    x: float,
    rhol: float,
    rhog: float,
    mul: float,
    mug: float,
    sigma: float,
    D: float,
    roughness: float = ...,
    L: int = ...
) -> float: ...


def Wang_Chiang_Lu(
    m: float,
    x: float,
    rhol: float,
    rhog: float,
    mul: float,
    mug: float,
    D: float,
    roughness: float = ...,
    L: int = ...
) -> float: ...


def Xu_Fang(
    m: float,
    x: float,
    rhol: float,
    rhog: float,
    mul: float,
    mug: float,
    sigma: float,
    D: float,
    roughness: float = ...,
    L: int = ...
) -> float: ...


def Yu_France(
    m: float,
    x: float,
    rhol: float,
    rhog: float,
    mul: float,
    mug: float,
    D: float,
    roughness: float = ...,
    L: int = ...
) -> float: ...


def Zhang_Hibiki_Mishima(
    m: float,
    x: float,
    rhol: float,
    rhog: float,
    mul: float,
    mug: float,
    sigma: float,
    D: float,
    roughness: float = ...,
    L: int = ...,
    flowtype: str = ...
) -> float: ...


def Zhang_Webb(
    m: float,
    x: float,
    rhol: float,
    mul: float,
    P: float,
    Pc: float,
    D: float,
    roughness: float = ...,
    L: int = ...
) -> float: ...


def _Beggs_Brill_holdup(regime: int, lambda_L: float, Fr: float, angle: float, LV: float) -> float: ...


def friction_factor_Kim_Mudawar(Re: float) -> float: ...


def two_phase_dP(
    m: float,
    x: float,
    rhol: float,
    D: float,
    L: int = ...,
    rhog: Optional[float] = ...,
    mul: Optional[float] = ...,
    mug: Optional[float] = ...,
    sigma: Optional[float] = ...,
    P: Optional[float] = ...,
    Pc: Optional[float] = ...,
    roughness: float = ...,
    angle: Optional[float] = ...,
    Method: Optional[str] = ...,
    AvailableMethods: bool = ...
) -> Union[List[str], float]: ...


def two_phase_dP_acceleration(
    m: int,
    D: float,
    xi: float,
    xo: float,
    alpha_i: float,
    alpha_o: float,
    rho_li: float,
    rho_gi: float,
    rho_lo: Optional[float] = ...,
    rho_go: Optional[float] = ...
) -> float: ...


def two_phase_dP_dz_acceleration(
    m: int,
    D: float,
    x: float,
    rhol: float,
    rhog: float,
    dv_dP_l: float,
    dv_dP_g: float,
    dx_dP: float,
    dP_dL: float,
    dA_dL: float
) -> float: ...


def two_phase_dP_dz_gravitational(angle: int, alpha: float, rhol: float, rhog: float, g: float = ...) -> float: ...


def two_phase_dP_gravitational(
    angle: int,
    z: int,
    alpha_i: float,
    rho_li: float,
    rho_gi: float,
    alpha_o: Optional[float] = ...,
    rho_lo: Optional[float] = ...,
    rho_go: Optional[float] = ...,
    g: float = ...
) -> float: ...


def two_phase_dP_methods(
    m: float,
    x: float,
    rhol: float,
    D: float,
    L: int = ...,
    rhog: Optional[float] = ...,
    mul: Optional[float] = ...,
    mug: Optional[float] = ...,
    sigma: Optional[float] = ...,
    P: Optional[float] = ...,
    Pc: Optional[float] = ...,
    roughness: float = ...,
    angle: Optional[float] = ...,
    check_ranges: bool = ...
) -> List[str]: ...

__all__: List[str]