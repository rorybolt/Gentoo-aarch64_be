
from catalyst import builder

class arch_arm64(builder.generic):
        "builder class for arm64"
        def __init__(self,myspec):
                builder.generic.__init__(self,myspec)
                self.settings["COMMON_FLAGS"]="-O2 -pipe"
                self.settings["CHOST"]="aarch64-unknown-linux-gnu"

class arch_arm64be(builder.generic):
        "builder class for arm64 big endian"
        def __init__(self,myspec):
                builder.generic.__init__(self,myspec)
                self.settings["COMMON_FLAGS"]="-O2 -pipe"
                self.settings["CHOST"]="aarch64_be-unknown-linux-gnu"

def register():
        "Inform main catalyst program of the contents of this plugin."
        return ({ "arm64":arch_arm64,
              "aarch64_be":arch_arm64be},
              ("aarch64","arm64", "aarch64_be"))
