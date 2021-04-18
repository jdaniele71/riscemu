import typing
if typing.TYPE_CHECKING:
    from . import *


def launch_debug_session(cpu: 'CPU', mmu: 'MMU', reg: 'Registers', prompt=""):
    if not cpu.conf.debug_instruction:
        return
    import code
    import readline
    import rlcompleter

    # setup some aliases
    registers = reg
    memory = mmu
    mem = mmu

    vars = globals()
    vars.update(locals())

    readline.set_completer(rlcompleter.Completer(vars).complete)
    readline.parse_and_bind("tab: complete")
    code.InteractiveConsole(vars).interact(banner=prompt, exitmsg="Resuming simulation")
