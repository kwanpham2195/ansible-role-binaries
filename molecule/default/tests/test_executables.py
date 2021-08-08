import os
import stat

def test_exist_zoxide(host):
    home = host.user("root").home
    assert host.file(home+"/.local/bin/zoxide").exists
    assert host.file(home+"/.local/bin/zoxide").mode == 0o755

def test_exist_tokei(host):
    home = host.user("root").home
    assert host.file(home+"/.local/bin/tokei").exists
    assert host.file(home+"/.local/bin/tokei").mode == 0o755

def test_exist_dust(host):
    home = host.user("root").home
    assert host.file(home+"/.local/bin/dust").exists
    assert host.file(home+"/.local/bin/dust").mode == 0o755

def test_exist_dyff(host):
    home = host.user("root").home
    assert host.file(home+"/.local/bin/dyff").exists
    assert host.file(home+"/.local/bin/dyff").mode == 0o755

