import name
#여기로 불리면 name의 이름은 name이 된다.
#그래서 name==main 밑의 절은 실행안됨

print(__name__)
print(name.__name__)#name안에서 이름을 임의로 test로 바꿨기 때문이다.
