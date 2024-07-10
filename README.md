- Python 3.12.3
- Linux 6.8.0-36-generic #36-Ubuntu SMP PREEMPT_DYNAMIC Mon Jun 10 10:49:14 UTC 2024 x86_64 x86_64 x86_64 GNU/Linux

1. `python -m venv .venv`
2. `python -m ensurepip && python -m pip install ninja==1.11.1.1 SCons==4.8.0` 
3. `source .venv/bin/activate`
4. `scons --experimental=ninja`
5. `ninja`
