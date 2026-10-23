
<div class="control">
  <select id="example" aria-label="예제 선택">
    <option value="0">1. 인사하기</option>
    <option value="1">2. 입력받기</option>
    <option value="2">3. 환경 실천 판정</option>
    <option value="3">4. 반복으로 응원하기</option>
    <option value="4">5. 점수 계산하기</option>
  </select>

  <button id="load">예제 불러오기</button>
  <button class="primary" id="run">▶ 실행하기</button>
  <button id="stop">■ 중지</button>
  <button id="reset">↺ 초기화</button>
</div>

<textarea
  id="code"
  spellcheck="false"
  aria-label="파이썬 코드 입력"
></textarea>

<p>
  <small>
    💬 코드에 input()이 있으면
    실행 중 입력 팝업이 나타납니다.
  </small>
</p>

<div class="status" id="status" role="status">
  실행 준비 완료
</div>
