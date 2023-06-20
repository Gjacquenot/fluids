#!/usr/bin/env python3
import os

tests = ['test_drag', 'test_control_valve', 'test_two_phase', 'test_two_phase_voidage', 'test_separator', 'test_piping', 'test_packed_bed', 'test_compressible', 'test_core', 'test_safety_valve', 'test_open_flow', 'test_filters', 'test_flow_meter', 'test_atmosphere', 'test_pump', 'test_friction', 'test_fittings', 'test_packed_tower', 'test_saltation', 'test_mixing', 'test_geometry', 'test_particle_size_distribution', 'test_jet_pump']
#tests = ['test_geometry']
try:
    os.remove("monkeytype.sqlite3")
except:
    pass

for t in tests:
    os.system("python3 -m monkeytype run manual_runner.py %s" %t)
for t in tests:
    mod = t[5:]
    os.system(f"python3 -m monkeytype stub fluids.{mod} > ../fluids/{mod}.pyi")
    type_hit_path = "../fluids/%s.pyi" %mod
    dat = open(type_hit_path).read()
    imports = 'from typing import List\n'
    future = 'from __future__ import annotations\n'
    dat = '# DO NOT EDIT - AUTOMATICALLY GENERATED BY tests/make_test_stubs.py!\n' + future + imports + dat
    dat = dat.replace('Union[int, float]', 'float')
    dat = dat.replace('Union[float, int]', 'float')
    dat += '\n__all__: List[str]'
    open(type_hit_path, 'w').write(dat)

"""
First thing not supported by monkeytype: Tuple[t1, ...]  in CountryPower
"""
try:
    os.remove("monkeytype.sqlite3")
except:
    pass
