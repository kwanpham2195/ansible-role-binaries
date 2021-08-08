import os
import stat

def test_exist_dyff(host):
    home = host.user("root").home
    assert host.file(home+"/.local/bin/dyff").exists
    assert host.file(home+"/.local/bin/dyff").mode == 0o755

