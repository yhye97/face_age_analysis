# face_age_analysis

**과연 동양인은 서양인보다 동안이라는 가설이 사실일까?**

## 1. 가설 정의:
동양인은 서양인 보다 동안이다.

동양인이 서양인보다 동안이라는 가설을 증명하기 위해서는 실제로 같은 나이대인 동양인과 서양인들의 데이터를 모아서 Face Detection API를 분석하여 실제 나이와 나이차이를 알아서 이를 비교하면 가설이 참이라는 것을 증명할 수 있을거라 생각됩니다.

## 2. 인터넷을 통한 데이터 획득:
동양인과 서양인들의 사진과 실제 나이 정보를 얻기 위해서는 유명인들을 대상으로 하는 것이 가장 정확할 것이라 생각되었습니다. 그래서 저는 영화계에 진출한 유명인들의 dataset들을 관리하는 사이트인 IMDb에서 데이터를 획득할 것입니다. 또한, 영화인들 외에도 Wikipedia를 통해 유명한 스포츠 스타, 정치인 등 다양한 분야에서 이름을 알리는 사람들의 데이터를 획득할 것입니다. 

또한, 나이 예상하는 API로는 사람 얼굴 감지 및 비교할 수 있는 Microsoft Azure Face API를 사용할 것입니다.

Microsoft Azure Face API 사용
https://azure.microsoft.com/ko-kr/services/cognitive-services/face/

IMDb Dataset을 사용하여 유명인들 사진과 나이 정보 획득:
https://www.imdb.com/search/name?gender=male,female&ref_=nv_tp_cel

FamousFix 를 사용하여 유명인들 사진과 나이 정보 획득:
https://www.famousfix.com/

## 4. 분석을 위한 데이터의 가공
***Request*** module을 import하여 http request library 사용해서 html source를 가져왔습니다.
***BeautifulSoup*** module을 사용하여 원하는 데이터(이름, url, 사진 url, 생일날짜)들을 추출했습니다. 

asian actors, asian actress, white actors, white actress list를 출력해주는 page들에는 asian actors 밑에 예시를 보면 알 수 있듯이 이름, 사진 url 정보만 나와있습니다.
<br><br>
생일날짜를 알기 위해서는 actor의 이름에 걸린 url에 접속하여 생일날짜가 있는 경우에는 born에 적혀 있는 생일날짜를 가져와야합니다.

## 5. 분석 결과 도출
동안 유무를 판단하기 위해서 Celebrity의 Face Api 나이와 실제 나이를 비교해야합니다. 이제 사진 url와 생일 정보가 중요하지 않으므로 이를 제외하고 celebrity의 이름 (name), 실제 나이 (real_age), face Api 를 통해 도출한 나이 (faceappi_age), face API 나이 - 실제 나이 (dif)를 새로운 csv에 저장했습니다. <br>

## 6. 결론
![realage](https://user-images.githubusercontent.com/17666783/59972025-4e380900-95c2-11e9-9cb8-1b7afd930d25.png)
<br>
![difav](https://user-images.githubusercontent.com/17666783/59972027-5728da80-95c2-11e9-82b1-1032257fee42.png)
<br>
분석 결과는 다음과 같습니다. <br>
dif: Asian (Asian Actors, Asian Actress, Asian Celebrities) 들의 FaceAPi 나이 - 실제나이 <br>
dif2: (Caucasian Actors, Caucasian Actress, Caucasian Celebrities)들의 FaceAPI 나이 - 실제 나이를 뺀 값으로 <br>
**음수의 절댓값이 클수록 동안을 뜻합니다.**

Asians: <br>
(1194 , 4)  <br>
Real Age Average: 37.938023450586265 <br>
Dif Age Average : -8.494137353433835 <br> <br>
Caucasians: <br>
(1123, 4) <br>
Real Age Average: 39.391807658058774 <br>
Dif Age Average : -8.269813000890473 <br>
<br>
### Dif Age Average는  -8.494137353433835 <  -8.269813000890473 인 관계로
### Asians가 Caucasians들 보다 동안이다 라는 가설이 참인 것을 알 수 있습니다. <br>

하지만 dataset이 좀 더 다양해지고 많아진다면 결과는 바뀔 수도 있습니다.
