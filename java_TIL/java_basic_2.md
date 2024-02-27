# 패키지

* 사용자와 같은 위치: PackageMain1 과 Data 는 같은 pack 이라는 패키지에 소속되어 있다. 이렇게 같은 패키 지에 있는 경우에는 패키지 경로를 생략해도 된다. 
* 사용자와 다른 위치: PackageMain1 과 User 는 서로 다른 패키지다. 이렇게 패키지가 다르면 pack.a.User 와 같이 패키지 전체 경로를 포함해서 클래스를 적어주어야 한다.
  * 이전에 본 코드와 같이 패키지가 다르다고 pack.a.User 와 같이 항상 전체 경로를 적어주는 것은 불편하다. 이때는 import 를 사용하면 된다.

* 코드에서 첫줄에는 package 를 사용하고, 다음 줄에는 import 를 사용할 수 있다. import 를 사용하면 다른 패키지에 있는 클래스를 가져와서 사용할 수 있다. import 를 사용한 덕분에 코드에서는 패키지 명을 생략하고 클래스 이름만 적을 수 있다

* 참고로 특정 패키지에 포함된 모든 클래스를 포함해서 사용하고 싶으면 import 시점에 *(별) 을 사용하면 된다.

* 참고로 특정 패키지에 포함된 모든 클래스를 포함해서 사용하고 싶으면 import 시점에 *(별) 을 사용하면 된다.

* 클래스 이름 중복

  * 패키지 덕분에 클래스 이름이 같아도 패키지 이름으로 구분해서 같은 이름의 클래스를 사용할 수 있다

  * 단, 같은 이름의 클래스가 있다면 import 는 둘중 하나만 선택할 수 있다. 이때는 자주 사용하는 클래스를 import 하고 나머지를 패키지를 포함한 전체 경로를 적어주면 된다. 물론 둘다 전체 경로를 적어준다면 import 를 사용하지 않아도 된다. 

    ```java
    package pack;
    import pack.a.User;
    public class PackageMain3 {
     public static void main(String[] args) {
     User userA = new User();
     pack.b.User userB = new pack.b.User();
     }
    }
    ```

    

* 규칙
  * 패키지의 이름과 위치는 폴더(디렉토리) 위치와 같아야 한다. (필수) 
  * 패키지 이름은 모두 소문자를 사용한다. (관례)
  * 패키지 이름의 앞 부분에는 일반적으로 회사의 도메인 이름을 거꾸로 사용한다. 예를 들어, com.company.myapp 과 같이 사용한다. (관례) 
    * 이 부분은 필수는 아니다. 하지만 수 많은 외부 라이브러리가 함께 사용되면 같은 패키지에 같은 클래스 이 름이 존재할 수도 있다. 이렇게 도메인 이름을 거꾸로 사용하면 이런 문제를 방지할 수 있다. 
    * 내가 오픈소스나 라이브러리를 만들어서 외부에 제공한다면 꼭 지키는 것이 좋다. 
    * 내가 만든 애플리케이션을 다른 곳에 공유하지 않고, 직접 배포한다면 보통 문제가 되지 않는다.

* 계층 구조

  * a 패키지와 a.b , a.c 패키지는 서로 완전히 다른 패키지 이다. 

  * 따라서 a 패키지의 클래스에서 a.b 패키지의 클래스가 필요하면 import 해서 사용해야 한다. 반대도 물론 마찬가 지이다. 

  * 정리하면 패키지가 계층 구조를 이루더라도 모든 패키지는 서로 다른 패키지이다. 

    

# 접근 제어자

* 종류(순서)
  * private : 모든 외부 호출을 막는다. (해당 클래스에서만 호출 가능)
  * default (package-private): 같은 패키지안에서 호출은 허용한다.
    * 접근 제어자를 명시하지 않으면 같은 패키지 안에서 호출을 허용하는 default 접근 제어자가 적용된다.
  *  protected : 같은 패키지안에서 호출은 허용한다. 패키지가 달라도 상속 관계의 호출은 허용한다.
  *  public : 모든 외부 호출을 허용한다.

* 접근 제어자 사용 위치 
  * 접근 제어자는 필드와 메서드, 생성자에 사용된다.
  *  추가로 클래스 레벨에도 일부 접근 제어자를 사용할 수 있다. 이 부분은 뒤에서 따로 설명한다.

* 접근 제어자의 핵심은 속성과 기능을 외부로부터 숨기는 것이다.
  * private 은 나의 클래스 안으로 속성과 기능을 숨길 때 사용, 외부 클래스에서 해당 기능을 호출할 수 없다. 
  * default 는 나의 패키지 안으로 속성과 기능을 숨길 때 사용, 외부 패키지에서 해당 기능을 호출할 수 없다. 
  * protected 는 상속 관계로 속성과 기능을 숨길 때 사용, 상속 관계가 아닌 곳에서 해당 기능을 호출할 수 없다. 
  * public 은 기능을 숨기지 않고 어디서든 호출할 수 있게 공개한다.



```java
package access.a;
public class AccessData {
 public int publicField;
 int defaultField;
 private int privateField;
 public void publicMethod() {
 System.out.println("publicMethod 호출 "+ publicField);
 }
 void defaultMethod() {
 System.out.println("defaultMethod 호출 " + defaultField);
 }
 private void privateMethod() {
 System.out.println("privateMethod 호출 " + privateField);
 }
 public void innerAccess() {
 System.out.println("내부 호출");
 publicField = 100;
 defaultField = 200;
 privateField = 300;
 publicMethod();
 defaultMethod();
 privateMethod();
 }
}


package access.a;
public class AccessInnerMain {
 public static void main(String[] args) {
 AccessData data = new AccessData();
 //public 호출 가능
 data.publicField = 1;
 data.publicMethod();
 //같은 패키지 default 호출 가능
 data.defaultField = 2;
 data.defaultMethod();
 //private 호출 불가
 //data.privateField = 3;
 //data.privateMethod();
 data.innerAccess();
 }
}

/*AccessData.innerAccess() 메서드는 public 이다. 따라서 외부에서 호출할 수 있다.
innerAccess() 메서드는 외부에서 호출되었지만 innerAccess() 메서드는 AccessData 에 포함되어
있다. 이 메서드는 자신의 private 필드와 메서드에 모두 접근할 수 있다.*/
```

* 클래스 레벨의 접근 제어자 규칙
  *  클래스 레벨의 접근 제어자는 public , default 만 사용할 수 있다. 
     * private , protected 는 사용할 수 없다.
  *  public 클래스는 반드시 파일명과 이름이 같아야 한다. 
     * 하나의 자바 파일에 public 클래스는 하나만 등장할 수 있다. 
     * 하나의 자바 파일에 default 접근 제어자를 사용하는 클래스는 무한정 만들 수 있다.

* 자바가 자동으로 생성해주시는 기본 생성자는 클래스와 같은 접근 제어자를 가진다.
* 생성자도 접근 제어자 관점에서 메서드와 비슷하다.
* 캡슐화: 데이터는 모두 숨기고, 기능은 꼭 필요한 기능만 노출하는 것이 좋은 캡슐화이다.





# 상속1

* extends 대상은 하나만 선택할 수 있다.(자바는 다중 상속 금지)
* 화살표 방향은 내가 너를 안다!는 의미

* 용어 정리
  * 부모 클래스 (슈퍼 클래스): 상속을 통해 자신의 필드와 메서드를 다른 클래스에 제공하는 클래스
  * 자식 클래스 (서브 클래스): 부모 클래스로부터 필드와 메서드를 상속받는 클래스

* 상속과 메모리 구조- 이 부분을 제대로 이해하는 것이 앞으로 정말 중요하다!
  * 상속 관계의 객체를 생성하면 그 내부에는 부모와 자식이 모두 생성된다.
  * 상속 관계의 객체를 호출할 때, 대상 타입을 정해야 한다. 이때 호출자의 타입을 통해 대상 타입을 찾는다.
  * 현재 타입에서 기능을 찾지 못하면 상위 부모 타입으로 기능을 찾아서 실행한다. 기능을 찾지 못하면 컴파일 오류 가 발생한다.

* 메서드 오버라이딩(재정의)
  * 부모에게서 상속 받은 기능을 자식이 재정의 하는 것\
  * @Override 애노테이션
    * 컴파일러는 이 애노테이션을 보고 메서드가 정확히 오버라이드 되었는지 확인한다. 오버라이딩 조건을 만족시키지 않으 면 컴파일 에러를 발생시킨다. 따라서 실수로 오버라이딩을 못하는 경우를 방지해준다. 예를 들어서 이 경우에 만약 부 모에 move() 메서드가 없다면 컴파일 오류가 발생한다. 참고로 이 기능은 필수는 아니지만 코드의 명확성을 위해 붙 여주는 것이 좋다.
  * 오버로딩(Overloading)과 오버라이딩(Overriding)
  * 메서드 오버라이딩 조건 
    * 메서드 이름: 메서드 이름이 같아야 한다. 
    * 메서드 매개변수(파라미터): 매개변수(파라미터) 타입, 순서, 개수가 같아야 한다.
    * 반환 타입: 반환 타입이 같아야 한다. 단 반환 타입이 하위 클래스 타입일 수 있다. 
    * static , final , private : 키워드가 붙은 메서드는 오버라이딩 될 수 없다. 
      * static 은 클래스 레벨에서 작동하므로 인스턴스 레벨에서 사용하는 오버라이딩이 의미가 없다. 쉽게 이 야기해서 그냥 클래스 이름을 통해 필요한 곳에 직접 접근하면 된다.
      * final 메서드는 재정의를 금지한다.
      * private 메서드는 해당 클래스에서만 접근 가능하기 때문에 하위 클래스에서 보이지 않는다. 따라서 오 버라이딩 할 수 없다. 
    * 생성자 오버라이딩: 생성자는 오버라이딩 할 수 없다.
    * 이하 아래는 참고만
    * 접근 제어자: 오버라이딩 메서드의 접근 제어자는 상위 클래스의 메서드보다 더 제한적이어서는 안된다. 예를 들 어, 상위 클래스의 메서드가 protected 로 선언되어 있으면 하위 클래스에서 이를 public 또는 protected 로 오버라이드할 수 있지만, private 또는 default 로 오버라이드 할 수 없다. 
    * 예외: 오버라이딩 메서드는 상위 클래스의 메서드보다 더 많은 체크 예외를 throws 로 선언할 수 없다. 하지만 더 적거나 같은 수의 예외, 또는 하위 타입의 예외는 선언할 수 있다. 예외를 학습해야 이해할 수 있다. 예외는 뒤 에서 다룬다.

* 상속과 접근 제어

  * protected: 패키지가 달라도 상속관계의 호출은 허용

    

# 상속2

### super- 부모 참조

* 부모와 자식의 필드명이 같거나 메서드가 오버라이딩 되어 있으면, 자식에서 부모의 필드나 메서드를 호출할 수 없다.
  이때 `super` 키워드를 사용하면 부모를 참조할 수 있다. `super` 는 이름 그대로 부모 클래스에 대한 참조를 나타낸다.

* this` 는 자기 자신의 참조를 뜻한다. `this` 는 생략할 수 있다.

### super - 생성자

* 상속 관계를 사용하면 자식 클래스의 생성자에서 부모 클래스의 생성자를 반드시 호출해야 한다.(규칙)
* 상속 관계에서 부모의 생성자를 호출할 때는 `super(...)` 를 사용하면 된다.

* 상속 관계의 생성자 호출은 결과적으로 부모에서 자식 순서로 실행된다. 따라서 부모의 데이터를 먼저 초기화하고 그 다음에 자식의 데이터를 초기화한다.

* 상속 관계에서 자식 클래스의 생성자 첫줄에 반드시 `super(...)` 를 호출해야 한다. 단 기본 생성자
  ( `super()` )인 경우 생략할 수 있다.

* this(...)와 함께 사용

  * 코드의 첫줄에 `this(...)` 를 사용하더라도 반드시 한번은 `super(...)` 를 호출해야 한다.

  ```java
  package extends1.super2;
  public class ClassB extends ClassA {
      public ClassB(int a) {
          this(a, 0); //기본 생성자 생략 가능
          System.out.println("ClassB 생성자 a=" + a);
      }
  public ClassB(int a, int b) {
  	super(); //기본 생성자 생략 가능 (반드시 한번은 super호출하는 부분)
  	System.out.println("ClassB 생성자 a=" + a + " b=" + b);
  }
  }
  ```

  

  

## 클래스와 메서드에 사용되는 final

* 클래스에 `final` 
  * 상속 끝!
  * `final` 로 선언된 클래스는 확장될 수 없다. 다른 클래스가 `final` 로 선언된 클래스를 상속받을 수 없다.
  * 예: `public final class MyFinalClass {...}`

* 메서드에 `final` 
  * 오버라이딩 끝!
  * `final` 로 선언된 메서드는 오버라이드 될 수 없다. 상속받은 서브 클래스에서 이 메서드를 변경할 수 없다.
  * 예: `public final void myFinalMethod() {...}`