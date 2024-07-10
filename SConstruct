
import os
from SCons.Script import *

env = Environment(tools=['default', 'ninja'])

# Custom builder function to use the archive.py script
def ArchiveBuilder(target, source, env):
    target_str = str(target[0])
    source_strs = [str(src) for src in source]
    cmd = ["python3", "archive.py", target_str] + source_strs
    return env.Execute(cmd)

# Register the custom builder
archive_builder = Builder(action=ArchiveBuilder)
env.Append(BUILDERS={'Archive': archive_builder})

# Build object files
objs = [env.Object(file) for file in ["main.c", "foo.c", "bar.c"]]

# Use the custom Archive builder to create the archive file
env.Archive("libfoo.a", objs)

# Build the final program, linking with the archive
env.Program("main", ["main.o"], LIBS=["foo"], LIBPATH=["."])

# Disable automatic Ninja run
env['NINJA_DISABLE_AUTO_RUN'] = 1

Default("main")
