import pytest


def test_option(pytestconfig):
    print('"foo" set to:', pytestconfig.getoption('foo'))
    print('"myopt" set to:', pytestconfig.getoption('myopt'))


@pytest.fixture()
def foo(pytestconfig):
    return pytestconfig.option.foo


@pytest.fixture()
def myopt(pytestconfig):
    return pytestconfig.option.myopt


def test_fixtures_for_options(foo, myopt):
    print('"foo" set to:', foo)
    print('"myopt" set to:', myopt)


def test_pytestconfig(pytestconfig):
    # print(f'args            : {pytestconfig.args}')
    # print(f'inifile         : {pytestconfig.inifile}')
    # print(f'invocation_dir  : {pytestconfig.invocation_dir}')
    # print(f'rootdir         : {pytestconfig.rootdir}')
    # print(f"-k EXPRESSION   : {pytestconfig.getoption('keyword')}")
    # print(f"-v, --verbose   : {pytestconfig.getoption('verbose')}")
    # # print(f"-q, --quiet     : {pytestconfig.getoption('quiet')}")
    # print(f"-l, --showlocals: {pytestconfig.getoption('showlocals')}")
    # print(f"--tb=style      : {pytestconfig.getoption('tbstyle')}")
    print(f"""
    args            : {pytestconfig.args}
    inifile         : {pytestconfig.inifile}
    invocation_dir  : {pytestconfig.invocation_dir}
    rootdir         : {pytestconfig.rootdir}
    -k EXPRESSION   : {pytestconfig.getoption('keyword')}
    -v, --verbose   : {pytestconfig.getoption('verbose')}
    -l, --showlocals: {pytestconfig.getoption('showlocals')}
    --tb=style      : {pytestconfig.getoption('tbstyle')}
    """)
