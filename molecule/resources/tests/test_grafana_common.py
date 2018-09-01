import os
import yaml
import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.fixture()
def AnsibleDefaults(Ansible):
    with open("../../defaults/main.yml", 'r') as stream:
        return yaml.load(stream)


def test_grafana_config_file(host, AnsibleDefaults):

    d = host.file('/etc/grafana/')
    assert d.exists
    assert d.user == 'root'
    assert d.group == 'root'
    assert oct(d.mode) == '0755'

    f = host.file('/etc/grafana/grafana.ini')
    assert f.exists
    assert f.user == 'root'
    assert f.group == AnsibleDefaults['grafana_group']
    assert oct(f.mode) == '0640'


@pytest.mark.parametrize('grafana_config_dir_var', [
    'grafana_paths_data',
    'grafana_paths_logs',
    'grafana_paths_plugins',
    'grafana_paths_provisioning',
])
def test_grafana_config_dirs(host, AnsibleDefaults, grafana_config_dir_var):

    f = host.file(AnsibleDefaults[grafana_config_dir_var])
    assert f.exists
    assert f.user == AnsibleDefaults['grafana_user']
    assert f.group == AnsibleDefaults['grafana_group']
    assert oct(f.mode) == '0755'


def test_grafana_service(host):

    s = host.service('grafana-server')
    assert s.is_running
    assert s.is_enabled


def test_grafana_webserver(host):

    host.socket("tcp://127.0.0.1:3000").is_listening
