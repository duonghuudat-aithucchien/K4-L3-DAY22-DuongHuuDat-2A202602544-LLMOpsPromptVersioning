import sys
import io
import os
sys.path.insert(0, os.path.dirname(__file__))

# Ghi thẳng output ra file với chuẩn UTF-8, không thông qua PowerShell
with open('evidence/02_ab_routing_log.txt', 'w', encoding='utf-8') as f:
    sys.stdout = f
    import config
    from importlib import import_module
    mod = import_module("02_prompt_hub_ab_routing")
    mod.main()
