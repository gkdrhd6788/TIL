char : 문자 하나를 다룰 때 사용한다. 작은따옴표( ' )를 사용해서 감싸야 한다. 예) 'A' , '가'
String : 문자열을 다룬다. 큰따옴표를 사용해야 한다. 예) "hello java"

리터럴 코드에서 개발자가 직접 적은 100 , 10.5 , true , 'A' , "Hello Java" 와 같은 고정된 값을 프로그래밍 용어로 리터럴(literal)이라 한다. 자바에서 기본 리터럴은  int이다.



자주 사용하는 타입
실무에서 자주 사용하는 타입은 다음과 같다.
정수 - int , long : 자바는 정수에 기본으로 int 를 사용한다. 만약 20억이 넘을 것 같으면 long 을 쓰
면 된다.
파일을 다룰 때는 byte 를 사용한다.
실수 - double : 실수는 고민하지 말고 double 을 쓰면 된다.
불린형 - boolean : true , false 참 거짓을 표현한다. 이후 조건문에서 자주 사용된다.
문자열 - String : 문자를 다룰 때는 문자 하나든 문자열이든 모두 String 을 사용하는 것이 편리하다.
자주 사용하는 타입을 제외하고 실무에서 나머지를 사용하는 경우는 거의 없다. 그나마 파일 전송시에 byte 를 사용하
는 것 정도이다.



자바 언어의 관례 한번에 정리
클래스는 대문자로 시작, 나머지는 소문자로 시작
자바에서 클래스 이름의 첫 글자는 대문자로 시작한다. 그리고 나머지는 모두 첫 글자를 소문자로 시작한다.
여기에 낙타 표기법을 적용하면 된다. 이렇게 하면 모든 자바 관례를 다 외울 수 있다!
예시: 클래스는 첫 글자 대문자, 나머지는 모두 첫 글자 소문자로 시작 + 낙타 표기법
클래스: Person , OrderDetail
변수를 포함한 나머지: firstName , userAccount
여기에 예외가 딱 2개 있다.
상수는 모두 대문자를 사용하고 언더바로 구분한다. (상수는 뒤에서 학습)
USER_LIMIT
패키지는 모두 소문자를 사용한다. (패키지는 뒤에서 학습)
org.spring.boot



연산자 종류
산술 연산자: + , - , * , / , % (나머지 연산자)
증감(증가 및 감소) 연산자: ++ , --
비교 연산자: == , != , > , < , >= , <=
논리 연산자: && (AND), || (OR), ! (NOT)
대입 연산자: = , += , -= , *= , /= , %=
삼항 연산자: ? :



자바에서 문자와 숫자를 더하면 숫자를 문자열로 변경한 다음에 서로 더한다.

전위, 후위 증감연산자
증감 연산자는 피연산자 앞에 두거나 뒤에 둘 수 있으며, 연산자의 위치에 따라 연산이 수행되는 시점이 달라진다.
++a : 증감 연산자를 피연산자 앞에 둘 수 있다. 이것을 앞에 있다고 해서 전위(Prefix) 증감 연산자라 한다.
a++ : 증감 연산자를 피연산자 뒤에 둘 수 있다. 이것을 뒤에 있다고 해서 후위(Postfix) 증감 연산자라 한
다

```java
package operator;
public class OperatorAdd2 {
 public static void main(String[] args) {
 // 전위 증감 연산자 사용 예
 int a = 1;
 int b = 0;
 b = ++a; // a의 값을 먼저 증가시키고, 그 결과를 b에 대입
 System.out.println("a = " + a + ", b = " + b); // 결과: a = 2, b = 2
 // 후위 증감 연산자 사용 예
 a = 1; // a 값을 다시 1로 지정
 b = 0; // b 값을 다시 0으로 지정
 b = a++; // a의 현재 값을 b에 먼저 대입하고, 그 후 a 값을 증가시킴
 System.out.println("a = " + a + ", b = " + b); // 결과: a = 2, b = 1
 }
}
```

**문자열이 같은지 비교할 때는 == 이 아니라 .equals() 메서드를 사용해야 한다. **



switch 문은 앞서 배운 if 문을 조금 더 편리하게 사용할 수 있는 기능이다.
참고로 if 문은 비교 연산자를 사용할 수 있지만, switch 문은 단순히 값이 같은지만 비교할 수 있다.

```java
switch (조건식) {
 case value1:
     // 조건식의 결과 값이 value1일 때 실행되는 코드
     break;
 case value2:
     // 조건식의 결과 값이 value2일 때 실행되는 코드
     break;
 default:
 	// 조건식의 결과 값이 위의 어떤 값에도 해당하지 않을 때 실행되는 코드
 }
```

만약 break 문이 없으면, 일치하는 case 이후의 모든 case 코드들이 순서대로 실행된다.

default 는 조건식의 결과값이 모든 case 의 값과 일치하지 않을 때 실행된다. if 문의 else 와 같다. default 구문은 선택이다.







for문도 while문과 같은 반복문이고, 코드를 반복 실행하는 역할을 한다. 
 for문이 없이 while문으로 모든 반복을 다룰 수 있다. 하지만 카운터 변수가 명확하거나, 반복 횟수가 정해진 경우에는 for문을 사용하는 것이 구조적으로 더 깔끔하고, 유지보수 하기 좋다.

for 문의 단점: 루프의 조건이 루프 내부에서 변경되는 경우, for 루프는 관리하기 어렵다.

while문의 장점: 루프의 조건이 루프 내부에서 변경되는 경우, while 루프는 이를 관리하기 쉽다.

for 문의 장점: 루프 변수의 범위가 for 루프 블록에 제한되므로, 다른 곳에서 이 변수를 실수로 변경할 가능성이 적다.

while문의 단점: 루프 변수가 while 블록 바깥에서도 접근 가능하므로, 이 변수를 실수로 변경하는 상황이 발생할 수 있다.



break 는 반복문을 즉시 종료하고 나간다. continue 는 반복문의 나머지 부분을 건너뛰고 다음 반복으로 진행하는 데 사용된다.

 참고로 while , do-while , for 와 같은 모든 반복문에서 사용할 수 있다.

```java
//문제: 1부터 시작해서 숫자를 계속 누적해서 더하다가 합계가 10보다 처음으로 큰 값은 얼마인가?

public class Break1 {
 public static void main(String[] args) {
 int sum = 0;
 int i = 1;
 while (true) {
 sum += i;
 if (sum > 10) {
 System.out.println("합이 10보다 크면 종료: i=" + i + " sum=" + sum);
 break;
 }
 i++;
 }
 }
}
```

```java
//문제: 1부터 5까지 숫자를 출력하는데, 숫자가 3일 때는 출력을 건너뛰어야 한다.
package loop;
public class Continue1 {
 public static void main(String[] args) {
 int i = 1;
 while (i <= 5) {
 if (i == 3) {
 i++;
 continue;
 }
 System.out.println(i);
 i++;
 }
 }
}
```





for 문 구조

```java
for (1.초기식; 2.조건식; 4.증감식) {
 // 3.코드
}

/*
for문은 다음 순서대로 실행된다.
1. 초기식이 실행된다. 주로 반복 횟수와 관련된 변수를 선언하고 초기화 할 때 사용한다. 초기식은 딱 1
번 사용된다.
2. 조건식을 검증한다. 참이면 코드를 실행하고, 거짓이면 for문을 빠져나간다.
3. 코드를 실행한다.
4. 코드가 종료되면 증감식을 실행한다. 주로 초기식에 넣은 반복 횟수와 관련된 변수의 값을 증가할 때
사용한다.
5. 다시 2. 조건식 부터 시작한다. (무한 반복)*/

for (;;) {
 // 코드
}
/*for문에서 초기식, 조건식, 증감식은 선택이다. 다음과 같이 모두 생략해도 된다. 단 생략해도 각 영역을 구분하는 세미
콜론( ; )은 유지해야 한다.*/
for (int i = 1; ; i++) {
    //코드
}
```





```java
/* 참고: println() 은 출력후 다음 라인으로 넘어간다. 라인을 넘기지 않고 출력하려면 print() 를 사용하면 된다 */
public static void main(String[] args) {
 int rows = 5;
 for(int i = 1; i <= rows; i++) {
 for(int j = 1; j <= i; j++) {
 System.out.print("*");
 }
 System.out.println();
 }
 }
}
```

변수는 선언한 위치에 따라 지역 변수(로컬변수), 멤버 변수(클래스 변수, 인스턴스 변수)와 같이 분류된다.

about scope

좋은 프로그램은 무한한 자유가 있는 프로그램이 아니라 적절한 제약이 있는 프로그램이다.



about 형변환

int < long < double



묵시적 형변환-- 큰거에 작은거 넣을 때 자동으로

명시적 형변환(casting)--작은거에 큰거 넣을 때 수동으로(소수점버림, 오버플로우 발생가능)

```java
// 형변환과 오버플로우
maxIntOver = 2147483648L; //int 최고값 + 1
intValue = (int) maxIntOver; //변수 값 읽기
intValue = (int) 2147483648L; //형변환 시도
intValue = -2147483648;
```

오버플로우가 발생하는 것 자체가 문제라는 점이다! 오버플로우가 발생했을 때 결과가 어떻게 되는지 계산하는데 시간을 낭비하면 안된다! 오버플로우 자체가 발생하지 않도록 막아야 한다. 이 경우 단순히 대 입하는 변수( intValue )의 타입을 int long 으로 변경해서 사이즈를 늘리면 오버플로우 문제가 해결된다.



계산과 형변환

형변환은 대입 뿐만 아니라, 계산을 할 때도 발생한다.

```java
package casting;
public class Casting4 {
 public static void main(String[] args) {
 int div1 = 3 / 2;
 System.out.println("div1 = " + div1); //1
 double div2 = 3 / 2;
 System.out.println("div2 = " + div2); //1.0
 double div3 = 3.0 / 2;
 System.out.println("div3 = " + div3); //1.5
 double div4 = (double) 3 / 2;
 System.out.println("div4 = " + div4); //1.5
 int a = 3;
 int b = 2;
 double result = (double) a / b;
 System.out.println("result = " + result); //1.5
 }
}
/*
자바에서 계산은 다음 2가지를 기억하자.
1. 같은 타입끼리의 계산은 같은 타입의 결과를 낸다.
int + int 는 int 를, double + double 은 double 의 결과가 나온다.
2. 서로 다른 타입의 계산은 큰 범위로 자동 형변환이 일어난다.
int + long 은 long + long 으로 자동 형변환이 일어난다.
int + double 은 double + double 로 자동 형변환이 일어난다. */
```



문제풀이4-2(ScannerWhileEx4)

input.nextLine() //이전에 입력된 개행문자 제거하는데에도 쓰임

chatGPT 답변

이전에 입력된 개행문자는 사용자가 입력을 마치고 Enter 키를 누를 때 생성되는 문자입니다. Java에서 `Scanner` 클래스를 사용하여 입력을 받을 때, `nextInt()`, `nextDouble()` 같은 메소드는 숫자를 입력받고 남은 개행문자(Enter 키에 의해 입력되는 `\n`)를 소비하지 않습니다. 이로 인해 바로 이어서 `nextLine()` 메소드를 사용하면 해당 개행문자를 입력으로 인식하게 되어, 실제로 사용자로부터 문자열 입력을 받기 전에 `nextLine()` 메소드가 개행문자를 입력으로 받아버리고 다음 단계로 넘어가버리는 문제가 발생합니다.

`input.nextLine()` 메소드는 한 줄의 문자열을 읽어들이는데, 이 때 개행문자까지 읽어들인 후 개행문자를 제외한 나머지 문자열을 반환합니다. 따라서 `nextInt()`, `nextDouble()` 등을 사용한 후 남아있는 개행문자를 소비하고 무시하기 위해서, 이러한 메소드들 뒤에 `input.nextLine()`을 한 번 호출하는 것이 일반적인 해결책입니다. 이 방법으로 다음 `nextLine()` 호출이 실제 사용자의 문자열 입력을 기다리게 할 수 있습니다.

요약하자면, `input.nextLine()`을 사용하여 이전 입력 후 남은 개행문자를 제거함으로써, 다음 사용자 입력이 올바르게 처리될 수 있도록 보장합니다.
