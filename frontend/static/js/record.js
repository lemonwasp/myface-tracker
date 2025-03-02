window.onload = function() {
  const user_id = localStorage.getItem('user_id');
  if (!user_id) {
      alert('로그인이 필요합니다.');
      window.location.href = 'login.html';
  }
};

document.getElementById('saveButton').addEventListener('click', async () => {
  const user_id = localStorage.getItem('user_id');  // 저장된 user_id 꺼내기
  if (!user_id) {
      alert('로그인이 필요합니다.');
      window.location.href = 'login.html';
      return;
  }

  const activity_name = document.getElementById('activity_name').value;
  const emotion = document.getElementById('emotion').value;
  const flow_score = document.getElementById('flow_score').value;
  const memo = document.getElementById('memo').value;

  const response = await fetch('http://127.0.0.1:8000/records', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({user_id, activity_name, emotion, flow_score, memo})
  });

  if (response.ok) {
      alert('기록 저장 완료!');
  } else {
      alert('기록 저장 실패!');
  }window.onload = function() {
    const user_id = localStorage.getItem('user_id');
    if (!user_id) {
        alert('로그인이 필요합니다.');
        window.location.href = 'login.html';
    }
};

document.getElementById('recordForm').onsubmit = async function(e) {
    e.preventDefault();

    const user_id = localStorage.getItem('user_id');
    if (!user_id) {
        alert('로그인이 필요합니다.');
        window.location.href = 'login.html';
        return;
    }

    const activity_name = document.getElementsByName('activity_name')[0].value;
    const emotion = document.getElementsByName('emotion')[0].value;
    const flow_score = document.getElementsByName('flow_score')[0].value;
    const memo = document.getElementsByName('memo')[0].value;

    const response = await fetch('http://127.0.0.1:8000/records', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({user_id, activity_name, emotion, flow_score, memo})
    });

    if (response.ok) {
        alert('기록 저장 완료!');
        document.getElementById('recordForm').reset();  // 폼 초기화
    } else {
        alert('기록 저장 실패!');
    }
  };
});