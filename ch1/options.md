# 옵션 설명

## `--collect-only`

* 실행되는 테스트에 대한 옵션과 구성에 대해서 보여줌

## `-k EXPRESSION`

* `EXPRESSION`에 작성해둔 test에 대해서만 실행을 한다.

## `-m MARKEXPR`

* `@pytest.mark` 데코레이션을 등록해둔 테스트에 대해서 진행

## `-x`

* 에러가 발생하면 다음 테스트가 있다고 하더라도 테스트를 진행하지 않는다.
* `--tb=no`: 실패한 테스트의 스택을 보여주지 않는다.

## `--maxfail=NUM`

* `-x` 옵션은 `--maxfail=1`으로 설정하는 것과 같은 효과를 가진다.

## `--lf`

* 실패한 테스트만 보여준다.

## `-q`

* 테스트를 간단하게 보여준다.
* 에러에 대해서만 보여주도록 되어있음.
