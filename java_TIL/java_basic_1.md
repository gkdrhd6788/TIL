# 클래스

## 순서

* 변수 선언

  *  Student student1
  * Student 타입을 받을 수 있는 변수를 선언한다

* 객체 생성

  * student1 = new Student()
  * 클래스가 사용하는 변수의 메모리 공간도 확보

* 참조값(주소)을 보관

  * student1에 보관

  * 생성했어도 주소를 알아야 접근 가능하므로

## 기타 개념

* 클래스는 객체를 생성하기 위한 '틀' 또는 '설계도'이다. 클래스는 객체가 가져야 할 속성(변수)과 기능(메서드)를 정의한다.
  
* 객체 - Object
  * 객체는 클래스에서 정의한 속성과 기능을 가진 실체이다. 객체는 서로 독립적인 상태를 가진다.
    예를 들어 위 코드에서 `student1` 은 학생1의 속성을 가지는 객체이고, `student2` 는 학생2의 속성을 가지는 객체이
    다. `student1` 과 `student2` 는 같은 클래스에서 만들어졌지만, 서로 다른 객체이다.

* 인스턴스 - Instance (비슷하다. 뉘앙스차이. 혼용해도 됨)
  * 인스턴스는 특정 클래스로부터 생성된 객체를 의미한다. 그래서 객체와 인스턴스라는 용어는 자주 혼용된다. 인스턴스
    는 주로 객체가 어떤 클래스에 속해 있는지 강조할 때 사용한다. 예를 들어서 `student1` 객체는 `Student` 클래스의
    인스턴스다. 라고 표현한다.

* 클래스에 정의한 변수들을 멤버 변수, 또는 필드라 한다. 멤버 변수(Member Variable): 이 변수들은 특정 클래스에 소속된 멤버이기 때문에 이렇게 부른다. 필드(Field): 데이터 항목을 가리키는 전통적인 용어이다. 데이터베이스, 엑셀 등에서 데이터 각각의 항목을 필드 라 한다.





# 기본형과 참조형

* 기본형(Primitive Type): int , long , double , boolean 처럼 변수에 사용할 값을 직접 넣을 수 있는 데이 터 타입을 기본형이라 한다.

* 참조형(Reference Type): Student student1 , int[] students 와 같이 데이터에 접근하기 위한 참조 (주소)를 저장하는 데이터 타입을 참조형이라 한다. 참조형은 객체 또는 배열에 사용된다. 
  * 참조형에는 객체와 배열이 있다. 객체는 . (dot)을 통해서 메모리 상에 생성된 객체를 찾아가야 사용할 수 있다. 배열은 [] 를 통해서 메모리 상에 생성된 배열을 찾아가야 사용할 수 있다

* 쉽게 이해하는 팁 기본형을 제외한 나머지는 모두 참조형이다. 기본형은 소문자로 시작한다. int , long , double , boolean 모두 소문자로 시작한다. 기본형은 자바가 기본으로 제공하는 데이터 타입이다. 이러한 기본형은 개발자가 새로 정의할 수 없다. 개발 자는 참조형인 클래스만 직접 정의할 수 있다. 클래스는 대문자로 시작한다.
* 참고 - String 자바에서 String 은 특별하다. String 은 사실은 클래스다. 따라서 참조형이다. 그런데 기본형처럼 문자 값을 바로 대입할 수 있다. 문자는 매우 자주 다루기 때문에 자바에서 특별하게 편의 기능을 제공한다. String 에 대한 자세한 내 용은 뒤에서 설명한다.

* 대원칙: 자바는 항상 변수의 값을 복사해서 대입한다. 자바에서 변수에 값을 대입하는 것은 변수에 들어 있는 값을 복사해서 대입하는 것이다. 기본형, 참조형 모두 항상 변수에 있는 값을 복사해서 대입한다. 기본형이면 변수에 들어 있는 실제 사용하는 값을 복사 해서 대입하고, 참조형이면 변수에 들어 있는 참조값을 복사해서 대입한다.

* 변수의 종류 
  * 멤버 변수(필드): 클래스에 선언 
  * 지역 변수: 메서드에 선언, 매개변수도 지역 변수의 한 종류이다.

* 변수의 값 초기화 
  * 멤버 변수: 자동 초기화 인스턴스의 멤버 변수는 인스턴스를 생성할 때 자동으로 초기화된다
    * 숫자( int )= 0 , boolean = false , 참조형 = null ( null 값은 참조할 대상이 없다는 뜻으로 사용 된다.) 
    * 개발자가 초기값을 직접 지정할 수 있다. 
  * 지역 변수: 수동 초기화 지역 변수는 항상 직접 초기화해야 한다.

* NullPointerException 이 발생하면 null 값에 . (dot)을 찍었다고 생각하면 문제를 쉽게 찾을 수 있다.



# 객체 지향

* 절차 지향은 데이터와 해당 데이터에 대한 처리방식이 분리되어있다.
* 객체 지향에서는 데이터와 메서드가 하나의 객체안에 함께 포함되어 있다.



# 생성자 (Constructor)

* 멤버 변수와 메서드의 매개변수의 이름이 같으면 둘을 어떻게 구분해야 할까? 
  * 이 경우 멤버 변수보다 매개변수가 코드 블럭의 더 안쪽에 있기 때문에 매개변수가 우선순위를 가진다. 
  * 따라서 initMember(String name,...) 메서드 안에서 name 이라고 적으면 매개변수에 접근하게 된다.
  *  멤버 변수에 접근하려면 앞에 this. 이라고 해주면 된다. 여기서 this 는 인스턴스 자신의 참조값을 가리킨다
  * 매개변수의 이름과 맴버 변수의 이름이 같은 경우 this 를 사용해서 둘을 명확하게 구분해야 한다. this 는 인스턴스 자신을 가리킨다.

* this의 생략
  * this 는 생략할 수 있다. 이 경우 변수를 찾을 때 가까운 지역변수(매개변수도 지역변수다)를 먼저 찾고 없으면 그 다음 으로 멤버 변수를 찾는다. 멤버 변수도 없으면 오류가 발생한다. 
  * 즉, 이름이 같지 않으면 생략할 수 있다.
  * 그러나 생략하지 않고, 멤버 변수에 접근하는 경우에 항상 넣어주는 코딩스타일도 있다.
  * but 요즘은  IDE가 발전하면서 구분이 쉬워져서 안쓴다.

* 생성자는 메서드와 비슷하지만 다음과 같은 차이가 있다. 
  * 생성자의 이름은 클래스 이름과 같아야 한다. 따라서 첫 글자도 대문자로 시작한다. 
  * 생성자는 반환 타입이 없다. 비워두어야 한다. 
  * 나머지는 메서드와 같다

* 생성자의 장점
  * 중복 호출 제거
  * 제약 - 생성자 호출 필수
    * 문법 오류 발생(cf. 메서드로 생성할 때는 호출 없고  null이 들어감)

*  기본 생성자
  * 매개변수가 없는 생성자를 기본 생성자라 한다. 
  * 클래스에 생성자가 하나도 없으면 자바 컴파일러는 매개변수가 없고, 작동하는 코드가 없는 기본 생성자를 자동으로 만들어준다. 
  * 생성자가 하나라도 있으면 자바는 기본 생성자를 만들지 않는다.

* 생성자 - 오버로딩과 this()
  * this.과 다름
  * 생성자도 메서드 오버로딩처럼 매개변수만 다르게 해서 여러 생성자를 제공할 수 있다
  * this() 라는 기능을 사용하면 생성자 내부에서 자신의 생성자를 호출할 수 있다. 참고로 this 는 인스턴스 자신 의 참조값을 가리킨다. 그래서 자신의 생성자를 호출한다고 생각하면 된다.
  * this() 를 사용하면 생성자 내부에서 다른 생성자를 호출할 수 있다.
  * 규칙 : this() 는 생성자 코드의 첫줄에만 작성할 수 있다