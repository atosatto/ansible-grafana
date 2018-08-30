import os
import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.fixture()
def Grafana4ReleaseVersion():

    return "4.6.3"


def test_grafana_4_stable_release(host, Grafana4ReleaseVersion):

    cmd = host.run('/usr/sbin/grafana-server -v')

    assert 'Version ' + Grafana4ReleaseVersion in (cmd.stdout + cmd.stderr)
