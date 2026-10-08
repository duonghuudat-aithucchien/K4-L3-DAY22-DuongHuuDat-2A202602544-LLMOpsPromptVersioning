import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

class TeeLogger:
    def __init__(self, *files):
        self.files = files
    def write(self, obj):
        for f in self.files:
            f.write(obj)
            f.flush()
    def flush(self):
        for f in self.files:
            f.flush()

f1 = open('evidence/04_pii_demo_log.txt', 'w', encoding='utf-8')
f2 = open('evidence/04_json_demo_log.txt', 'w', encoding='utf-8')
sys.stdout = TeeLogger(f1, f2)

import config
from importlib import import_module
mod = import_module("04_guardrails_validator")
mod.main()
