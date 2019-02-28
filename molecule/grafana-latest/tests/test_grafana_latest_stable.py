import os
import re
import semver
import pytest
from github import Github

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.fixture()
def GrafanaLatestReleaseVersion():

    gh = Github(os.getenv('GITHUB_API_TOKEN', None))
    grafana_latest_release = "0.0.0"

    # do not check the whole releases history, just check the latest 5 releases
    for rel in gh.get_repo('grafana/grafana').get_releases()[:5]:
        cv = re.sub('^v(.*)$', '\\1', rel.tag_name)
        if semver.compare(cv, grafana_latest_release) >= 0:
            grafana_latest_release = cv

    return grafana_latest_release


def test_grafana_latest_stable_release(host, GrafanaLatestReleaseVersion):

    cmd = host.run('/usr/sbin/grafana-server -v')

    assert 'Version ' + GrafanaLatestReleaseVersion in (cmd.stdout + cmd.stderr)
