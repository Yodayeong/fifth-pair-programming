# 🗂️ Django Project (Pair programming)

> 일시 : 2022-10-14
>
> 내용 : 2:1로 driver, navigator로 나누어 회원가입, 로그인 기능 구현
>
> 팀 구성 : 3인 1팀 (1-8 박태호, 여다영, 이수경)



![221014](https://user-images.githubusercontent.com/106902415/195806475-d816be6e-0aff-47d8-b89b-a00c27100ccd.gif)



- HTML, CSS로 프론트엔드 구현, Django MTV 패턴으로 백엔드 구현
- User 모델
  - Django 내장 Abstract User를 상속받아 User 모델 생성
- login
  - Django 내장 UserCreationForm을 상속받아 CustomUserCreationForm 생성
- update
  - Django 내장 UserChangeForm을 상속받아 CustomUserChangeForm 생성
  - 해당 유저 프로필의 pk와 request를 요청한 user의 pk가 일치할 때만 수정하도록 설정함



## Contributors

<a href="[https://github.com/code-sum/1014-PJT/graphs/contributors%22%3E](https://github.com/code-sum/1014-PJT/graphs/contributors"> <img src="https://contrib.rocks/image?repo=code-sum/1014-PJT" /></a>



## ✒️ 실습 후기

- **박태호** : 회원 관리 기능을 구현하는데 더 익숙해지는 시간이었고 서로의 의견이 충분히 반영된 결과물이 나와서 만족스럽습니다. 드라이버 역할을 하면서 놓치고 있던 부분을 채울 수 있어서 감사한 시간이었습니다!
- **여다영** : 회원가입 기능과 로그인 기능을 직접 구현하고자 하니 힘들었지만 재미있었다. update부분에서 pk값 일치 부분을 구현하는 것은 모두가 해본적 없어서 조금 힘들었지만 구현하고 나니 재미있었다. 무엇보다 좋은 팀원분들을 만나서 좋았다 ㅎㅎ

- **이수경** : 너무 재밌었어요 ~