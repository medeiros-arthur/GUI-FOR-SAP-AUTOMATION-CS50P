import os
import sapCred
import glob

exported_path = sapCred.exportPath
sap_path = sapCred.sapExePath
sap_login = sapCred.login

def check_path(dir):
    return os.path.exists(dir)

def check_login(login):
    return login


def test_exported_path():
    assert check_path(exported_path) != None

def test_sap_path():
    assert check_path(sap_path) != None

def test_check_login():
    assert check_login(sap_login) != None



