#!/bin/bash

hyperfine --warmup 3 'python3 vocalSeperation.py'
hyperfine --export-csv vS.csv 'python3 vocalSeperation.py'

hyperfine --warmup 3 'python3 beatSeperation.py'
hyperfine --export-csv bS.csv 'python3 beatSeperation.py'
